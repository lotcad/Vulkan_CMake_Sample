#pragma once

// AnalysisApi — 해석 C API(CAD_WindTunnel · CAD_Water · CAD_StructuralAnalysis) 브릿지.
//
// 세 API 모두 {"op": …} JSON 을 받아 결과 JSON 을 돌려준다(MCP 도구 wind_tunnel·water·structural_analysis 와 같은 창구).
// 엔진의 해석 패널(ImGui)은 호스트 창 안에서 그려지지 않으므로 QML 패널이 이 API 로 같은 일을 한다.
//
// ⚠️ 2회 호출 규약을 꼭 지킨다 — out=NULL 로 길이를 먼저 묻고(이때 한 번 실행), 같은 인자로 버퍼를 넘기면
//    엔진이 다시 실행하지 않고 그 결과를 준다. 고정 버퍼로 불렀다가 모자라 **버퍼로 다시** 부르면
//    run·start 가 두 번 들어가 "이미 도는 중" 이 된다.
//
// 해석 모듈(libLotCADSim·libLotCADCfd)은 엔진 라이브러리 옆(sdk/)에 있어야 한다 — 없으면 start·run 이 error 로 알려 준다.
// 켜기(start)는 다음 프레임에, 구조 해석 풀이(run)는 작업 스레드에서 돈다 — QML 이 Timer 로 refresh() 해 상태를 본다.

#include "cad_json.h"

#include <QJsonDocument>
#include <QJsonObject>
#include <QObject>
#include <QString>
#include <QVariantList>
#include <QVariantMap>
#include <QtQml/qqmlregistration.h>

#include <vector>

class AnalysisApi : public QObject {
    Q_OBJECT
    QML_ELEMENT
    QML_SINGLETON

    Q_PROPERTY(QVariantMap wind  READ wind  NOTIFY stateChanged)   // 바람 터널 status
    Q_PROPERTY(QVariantMap water READ water NOTIFY stateChanged)   // 물 status
    Q_PROPERTY(QVariantMap sim   READ sim   NOTIFY stateChanged)   // 구조 해석 status(faces·conditions·result)
    Q_PROPERTY(QString lastError READ lastError NOTIFY lastErrorChanged)

public:
    explicit AnalysisApi(QObject* parent = nullptr) : QObject(parent) {}

    QVariantMap wind() const  { return wind_; }
    QVariantMap water() const { return water_; }
    QVariantMap sim() const   { return sim_; }
    QString lastError() const { return lastError_; }

    // which = "wind" | "water" | "sim". args 는 {"op": …} 그대로(QML 객체 리터럴). 결과 JSON 을 돌려주고 상태도 갱신한다.
    Q_INVOKABLE QVariantMap call(const QString& which, const QVariantMap& args) {
        const QJsonObject r = invoke(which, args);
        // 결과에 status 가 같이 오는 op 가 많다 — 그 해석 상태를 바로 바꿔 QML 이 다음 Timer 를 기다리지 않게
        if (r.contains("ok")) store(which, r);
        const QString err = r.value("error").toString();
        if (lastError_ != err) { lastError_ = err; emit lastErrorChanged(); }
        return r.toVariantMap();
    }

    // 세 해석 상태를 다시 읽는다 — 패널이 보이는 동안 Timer 로.
    Q_INVOKABLE void refresh() {
        for (const char* w : {"wind", "water", "sim"}) store(w, invoke(w, {{"op", "status"}}));
    }

    // 지금 선택한 객체 id — 해석 대상(솔리드·그릇)을 고르는 데 쓴다.
    Q_INVOKABLE QVariantList selectedIds() const {
        QVariantList ids;
        // 개수만 먼저(NULL, 0) 묻고 그만큼 칸을 잡아 한 번에 받는다
        const int32_t n = CAD_GetSelection(nullptr, 0);
        if (n <= 0) return ids;
        std::vector<uint32_t> buf(static_cast<size_t>(n));
        const int32_t got = CAD_GetSelection(buf.data(), static_cast<uint32_t>(buf.size()));
        for (int32_t i = 0; i < got && i < n; ++i) ids.append(buf[static_cast<size_t>(i)]);
        return ids;
    }

signals:
    void stateChanged();
    void lastErrorChanged();

private:
    static QJsonObject invoke(const QString& which, const QVariantMap& args) {
        using Fn = int32_t (*)(const char*, char*, uint32_t);   // 반환 = 전체 길이, 실패 = 음수 CAD_E_*
        const Fn fn = which == "wind" ? &CAD_WindTunnel : which == "water" ? &CAD_Water : &CAD_StructuralAnalysis;
        const QByteArray in = QJsonDocument(QJsonObject::fromVariantMap(args)).toJson(QJsonDocument::Compact);
        const int32_t need = fn(in.constData(), nullptr, 0);   // 길이 질의 — 여기서 한 번 실행된다
        if (need < 0) return {{"ok", false}, {"error", cadjson::lastError()}};
        QByteArray buf(need + 1, '\0');
        const int32_t n = fn(in.constData(), buf.data(), uint32_t(buf.size()));   // 같은 인자 → 다시 실행하지 않고 결과만
        if (n < 0) return {{"ok", false}, {"error", cadjson::lastError()}};
        buf.resize(qMin(n, int(buf.size())));
        return QJsonDocument::fromJson(buf).object();
    }

    void store(const QString& which, const QJsonObject& r) {
        if (r.isEmpty()) return;
        QVariantMap& slot = which == "wind" ? wind_ : which == "water" ? water_ : sim_;
        const QVariantMap m = r.toVariantMap();
        if (slot == m) return;
        slot = m;
        emit stateChanged();
    }

    QVariantMap wind_, water_, sim_;
    QString lastError_;
};
