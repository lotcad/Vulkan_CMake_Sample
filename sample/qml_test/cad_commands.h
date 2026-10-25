#pragma once

// CadCommands — QML 툴바 버튼이 호출하는 얇은 명령 브릿지.
// QML 에서 Q_INVOKABLE 메서드로 CAD_ExecuteCommand / CAD_Undo 등 C API 를 부른다.
// (엔진 상태 변경은 전부 C API 경계를 지나가므로 QML 은 엔진 내부를 전혀 모른다.)

#include "../../sdk/include/LotCAD_API.h"

#include <QObject>
#include <QByteArray>
#include <QFileDialog>
#include <QFileInfo>
#include <QString>
#include <QtQml/qqmlregistration.h>

class CadCommands : public QObject {
    Q_OBJECT
    QML_ELEMENT
    QML_SINGLETON   // QML 에서 CadCommands.addCube() 처럼 전역 싱글톤으로 접근

public:
    explicit CadCommands(QObject* parent = nullptr) : QObject(parent) {}

    Q_INVOKABLE void addCube()        { start("cube"); }
    Q_INVOKABLE void selectAll()      { start("selectall"); }
    Q_INVOKABLE void deleteSelected() { start("delete"); }
    Q_INVOKABLE void clearAll()       { CAD_ClearAll(); }
    Q_INVOKABLE void zoomExtents()    { CAD_ZoomExtents(); }
    Q_INVOKABLE void focusSelected()  { CAD_FocusSelected(); }
    Q_INVOKABLE void toggleProjection(){ bool ortho = false; if (CAD_GetProjection(&ortho) == CAD_OK) CAD_SetProjection(!ortho); }
    Q_INVOKABLE void setView(int v)   { CAD_SetView(v); }   // 0정면 1평면 2우측 3Iso
    Q_INVOKABLE void undo()           { CAD_Undo(); }
    Q_INVOKABLE void redo()           { CAD_Redo(); }

    // 명령행과 같은 입구 — 이름은 영문·별칭·한글 모두 받는다.
    // 진행 중인 도구가 있으면 값 입력("12,30")으로 들어간다(그래서 버튼은 아래 startCommand 를 쓴다).
    // 반환 = 성공 여부(결과 코드 CAD_OK). 모르는 명령은 CAD_E_NOT_FOUND → false.
    Q_INVOKABLE bool executeCommand(const QString& name) {
        return CAD_ExecuteCommand(name.toUtf8().constData()) == CAD_OK;
    }

    // 버튼용 — 진행 중인 명령을 먼저 끝내고(CAD_CancelCommand, 선택은 그대로) 새로 시작한다(오토캐드 ^C^C).
    // 리본 버튼·기능 패널의 "화면에서 고르기" 가 이걸로 엔진 도구를 띄워 3D 뷰에서 클릭을 받게 한다.
    Q_INVOKABLE bool startCommand(const QString& name) {
        return start(name.toUtf8().constData());
    }

    // 스케치 도구 — 엔진 명령 이름으로 시작한다
    Q_INVOKABLE void startBox()       { start("box"); }
    Q_INVOKABLE void startLine()      { start("line"); }
    Q_INVOKABLE void startRect()      { start("rect"); }
    Q_INVOKABLE void startCircle()    { start("circle"); }
    Q_INVOKABLE void startPolyline()  { start("polyline"); }
    Q_INVOKABLE void startExtrude()   { start("extrude"); }

    // ── 파일 ──
    // QtQuick.Dialogs(qml6-module-qtquick-dialogs) 는 배포처에 없을 수 있어 QFileDialog 를 쓴다.
    // qt6-base 에 이미 들어 있으므로 런타임 패키지가 늘지 않고, 별도 최상위 창이라
    // 네이티브 3D 자식 창에 가리지도 않는다.
    // 확장자로 포맷이 갈리는 건 엔진 몫이라 호스트는 경로만 넘긴다.
    Q_INVOKABLE void newDocument() { CAD_NewDocument("제목 없음"); }

    Q_INVOKABLE bool openDocument() {   // 새 탭으로 열기
        const QString p = QFileDialog::getOpenFileName(nullptr, "열기", QString(), kOpenFilter);
        return !p.isEmpty() && CAD_OpenDocument(p.toUtf8().constData()) >= 0;
    }

    Q_INVOKABLE bool importFile() {     // 현재 문서에 추가
        const QString p = QFileDialog::getOpenFileName(nullptr, "가져오기", QString(), kOpenFilter);
        return !p.isEmpty() && CAD_OpenFile(p.toUtf8().constData());
    }

    Q_INVOKABLE bool saveAs(bool selectedOnly = false) {
        QString p = QFileDialog::getSaveFileName(
            nullptr, selectedOnly ? "선택만 내보내기" : "다른 이름으로 저장", QString(), kSaveFilter);
        if (p.isEmpty()) return false;
        // 확장자를 안 붙이면 엔진이 포맷을 못 고른다 — 기본값으로 네이티브 형식을 채운다.
        if (QFileInfo(p).suffix().isEmpty()) p += ".lot";
        return CAD_SaveAs(p.toUtf8().constData(), selectedOnly);
    }

    // 실패 사유 표시용 — CAD_SaveAs/CAD_OpenFile 이 false 를 준 뒤 읽는다.
    Q_INVOKABLE QString statusMessage() const {
        char buf[512] = {0};
        // 반환 = 전체 길이(NUL 제외) — 칸보다 길면 잘라 담으므로 NUL 까지 읽는다
        const int32_t n = CAD_GetPrompt(buf, uint32_t(sizeof(buf)));
        return n > 0 ? QString::fromUtf8(buf) : QString();
    }

private:
    // 취소 후 실행 — ExecuteCommand 만 부르면 선 그리던 중 "rect" 가 값으로 먹혀 도구가 안 바뀐다
    static bool start(const char* name) {
        CAD_CancelCommand();
        return CAD_ExecuteCommand(name) == CAD_OK;
    }

    static constexpr const char* kOpenFilter =
        "모든 지원 형식 (*.lot *.obj *.stl *.dxf *.ply *.gltf *.glb);;"
        "프로젝트 (*.lot);;메시 (*.obj *.stl *.gltf *.glb);;도면 (*.dxf);;점군 (*.ply);;"
        "모든 파일 (*)";
    static constexpr const char* kSaveFilter =
        "프로젝트 (*.lot);;OBJ (*.obj);;STL (*.stl);;DXF (*.dxf);;glTF (*.glb *.gltf);;"
        "모든 파일 (*)";
};
