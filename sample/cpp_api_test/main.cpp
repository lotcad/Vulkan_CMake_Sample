#include "../../sdk/include/LotCAD_API.h"

#include <chrono>
#include <cstdint>
#include <filesystem>
#include <iostream>
#include <string>
#include <thread>
#include <vector>

namespace {
// 실패 이유 — 결과 코드가 CAD_OK 가 아닐 때 바로 읽는다(다음 성공이 지운다)
std::string lastError() {
    char buf[512] = {};
    return CAD_GetLastError(buf, sizeof buf) > 0 ? buf : "";
}
void ticks(int n) { for (int i = 0; i < n; ++i) CAD_Tick(); }   // 명령·그래프 계산은 다음 프레임에 반영된다

// ── 명령행 — 명령행에 치는 것과 같은 입구(명령 수백 개). 점은 "x,y", 값은 숫자, Enter 는 " " ──
// 명령은 다음 프레임에 도구가 켜진다 — 입력마다 한 프레임 돌린다(바로 이어 치면 "모르는 명령").
CAD_Status command(const char* text) {
    const CAD_Status st = CAD_ExecuteCommand(text);
    ticks(1);
    return st;
}

void commandLineTest() {
    const int32_t before = CAD_GetObjectCount();
    CAD_CancelCommand();                        // 진행 중인 도구를 먼저 끝낸다(도구 막대 ^C^C)
    command("line"); command("0,-4"); command("3,-4");          // 선 — 두 점이면 끝
    command("c"); command("5,-4"); command("1");                // 원 — 중심, 반지름
    const CAD_Status unknown = CAD_ExecuteCommand("nosuchcommand");
    const std::string why = lastError();        // 바로 읽는다 — 다음 성공한 호출이 지운다
    std::cout << "[cpp_api_test] command line: line + circle -> objects " << before << " -> " << CAD_GetObjectCount()
              << ", unknown command = " << unknown << " (" << why << ")" << std::endl;
}

// ── NURBS — 핸들(uint64)로 다루는 기하 곡선. 다 쓰면 CAD_GeCurveFree ──
void nurbsTest() {
    // 3차, 조절점 4개, 열린 균일 매듭(0,0,0,0,1,1,1,1) — 매듭 수 = 조절점 + 차수 + 1
    const double knots[] = {0, 0, 0, 0, 1, 1, 1, 1};
    const double ctrl[] = {0, 0, 0,   1, 2, 0,   3, 2, 0,   4, 0, 0};
    uint64_t curve = 0;
    if (CAD_GeCurveCreateNurbs(3, knots, 8, ctrl, 4, nullptr, 0, &curve) != CAD_OK) {
        std::cerr << "[cpp_api_test] NURBS create failed: " << lastError() << std::endl;
        return;
    }
    CAD_GeVec3 mid{}, d1{}, d2{};
    double length = 0;
    CAD_GeCurveEvaluate(curve, 0.5, &mid, &d1, &d2);
    CAD_GeCurveLength(curve, 0.0, 1.0, &length);
    uint32_t objectId = 0;
    CAD_CreateCurveFromGe(curve, nullptr, &objectId);   // 장면에 곡선 객체로(핸들은 그대로 내 것)
    std::cout << "[cpp_api_test] NURBS: point(0.5) = " << mid.x << ", " << mid.y << ", " << mid.z
              << "  length = " << length << "  object #" << objectId << std::endl;

    // 원 → NURBS(정확한 유리 곡선): 2차, 조절점 9개
    uint64_t circle = 0, asNurbs = 0;
    CAD_GeCurveCreateCircle(CAD_GeVec3{0, 0, 0}, CAD_GeVec3{0, 0, 1}, 1.0, &circle);
    if (CAD_GeCurveToNurbs(circle, &asNurbs) == CAD_OK) {
        int degree = 0;
        uint32_t controls = 0, knotCount = 0;
        bool rational = false;
        CAD_GeCurveGetNurbsInfo(asNurbs, &degree, &controls, &knotCount, &rational);
        std::cout << "[cpp_api_test] circle -> NURBS: degree " << degree << ", controls " << controls
                  << ", knots " << knotCount << (rational ? ", rational" : "") << std::endl;
    }
    CAD_GeCurveFree(asNurbs);
    CAD_GeCurveFree(circle);
    CAD_GeCurveFree(curve);
    std::cout << "[cpp_api_test] NURBS handles left: " << CAD_GeCurveLiveCount() << std::endl;
}

// ── 노드 그래프 — 상자 → 선형 배열(5개) → 출력. 엔진이 다음 프레임에 계산해 장면 객체를 만든다 ──
void nodeGraphTest() {
    uint32_t box = 0, arr = 0, out = 0;
    CAD_NodeGraphClear();
    CAD_NodeGraphAddNode("box", 0, 0, &box);
    CAD_NodeGraphAddNode("array.linear", 220, 0, &arr);
    CAD_NodeGraphAddNode("output", 440, 0, &out);
    CAD_NodeGraphSetNumber(box, "width", 0.4);
    CAD_NodeGraphSetNumber(box, "depth", 0.4);
    CAD_NodeGraphSetNumber(box, "height", 0.4);
    CAD_NodeGraphSetPoint(box, "center", CAD_GeVec3{0, 3, 0.2});
    CAD_NodeGraphSetNumber(arr, "count", 5);
    CAD_NodeGraphSetPoint(arr, "offset", CAD_GeVec3{0.6, 0, 0});
    if (CAD_NodeGraphConnect(box, "solid", arr, "objects") != CAD_OK ||
        CAD_NodeGraphConnect(arr, "objects", out, "objects") != CAD_OK) {
        std::cerr << "[cpp_api_test] node graph connect failed: " << lastError() << std::endl;
        return;
    }
    const int32_t errors = CAD_NodeGraphEvaluate();   // 반환 = 오류 난 노드 수
    ticks(3);
    std::cout << "[cpp_api_test] node graph: errors " << errors
              << ", output objects " << CAD_NodeGraphGetNodeObjects(out, nullptr, 0) << std::endl;
}

// ── 문서 — 저장(형식 = 확장자) · 새 탭 · 탭으로 열기 · 닫기 · 지금 문서에 불러오기 ──
void documentTest() {
    const auto dir = std::filesystem::temp_directory_path() / "lotcad_cpp_api_test";
    std::filesystem::create_directories(dir);
    const std::string lot = (dir / "sample.lot").string(), step = (dir / "sample.step").string();
    const CAD_Status savedLot = CAD_SaveAs(lot.c_str(), false);
    const CAD_Status savedStep = CAD_SaveAs(step.c_str(), false);   // B-Rep 솔리드만 들어간다
    std::cout << "[cpp_api_test] save .lot = " << savedLot << ", .step = " << savedStep << " -> " << dir.string() << std::endl;

    int32_t fresh = -1, opened = -1;
    CAD_NewDocument("new", &fresh);
    if (CAD_OpenDocument(lot.c_str(), &opened) == CAD_OK) {
        char title[256] = {};
        CAD_GetDocumentTitle(opened, title, sizeof title);
        std::cout << "[cpp_api_test] documents: " << CAD_GetDocumentCount() << " (opened '" << title << "' at " << opened
                  << ", objects " << CAD_GetObjectCount() << ")" << std::endl;
        CAD_CloseDocument(opened);
    }
    CAD_CloseDocument(fresh);
    CAD_ActivateDocument(0);
    const int32_t before = CAD_GetObjectCount();
    const CAD_Status merged = CAD_OpenFile(step.c_str());           // 지금 문서에 더한다(새 탭 아님)
    ticks(2);
    std::cout << "[cpp_api_test] open .step into current = " << merged << ", objects " << before << " -> "
              << CAD_GetObjectCount() << std::endl;
}
}   // namespace

// --exit: 시험만 하고 창 없이 끝낸다(CI·자동 확인)
int main(int argc, char** argv) {
    const bool exitAfterTests = argc > 1 && std::string(argv[1]) == "--exit";
#ifdef LOTCAD_DEFAULT_ASSET_PATH
    // 엔진은 models/ fonts/ 를 상대 경로로 연다. macOS·Linux 는 에셋을 복사하지 않으므로(CMakeLists.txt)
    // 실행 폴더에 없으면 SDK 폴더를 알려 준다 — 없으면 빌드 폴더에서 실행할 때 CreateEngine 이 실패한다.
    if (!std::filesystem::exists("models"))
        CAD_SetRuntimeAssetPath(LOTCAD_DEFAULT_ASSET_PATH);
#endif
    std::cout << "[cpp_api_test] create engine" << std::endl;
    if (!CAD_CreateEngine()) {
        std::cerr << "[cpp_api_test] CAD_CreateEngine failed" << std::endl;
        return 1;
    }
    uint32_t boxId = 0;   // 만들기 = 결과 코드 + 새 id(실패면 이유는 CAD_GetLastError)
    if (CAD_CreateBox(CAD_GeVec3{0.0, 0.0, 1.0}, CAD_GeVec3{0.5, 0.5, 0.5}, nullptr, &boxId) != CAD_OK) {
        std::cerr << "[cpp_api_test] CAD_CreateBox failed" << std::endl;
        CAD_DestroyEngine();
        return 1;
    }

    // 결과 코드(CAD_Status) — 0 = CAD_OK, 음수 = 이유 코드(이유 글은 CAD_GetLastError)
    CAD_SetPosition(boxId, CAD_GeVec3{1.0, 0.0, 1.5});
    CAD_SetScale(boxId, CAD_GeVec3{0.8, 0.8, 0.8});
    CAD_SetRotationAxisAngle(boxId, CAD_GeVec3{0.0, 0.0, 1.0}, 0.7853982);
    CAD_SetSelection(&boxId, 1, CAD_SELECT_REPLACE);
    CAD_ZoomExtents();

    CAD_GeVec3 p{};
    if (CAD_GetPosition(boxId, &p) == CAD_OK) {
        std::cout << "[cpp_api_test] box position: "
                  << p.x << ", " << p.y << ", " << p.z << std::endl;
    }

    std::cout << "[cpp_api_test] object count: "
              << CAD_GetObjectCount() << std::endl;
    std::cout << "[cpp_api_test] selected count: "
              << CAD_GetSelection(nullptr, 0) << std::endl;   // NULL, 0 = 개수만

    // ── 편집 명령 예시 ──
    // 배열 — 박스를 X 로 3 × Y 로 2(간격 1.5) 복제. 대상은 id 로, 간격은 월드 벡터로. 반환 = 만든 사본 수
    uint32_t copies[5] = {};
    if (CAD_EntityArrayRect(&boxId, 1, 3, 2, 1, CAD_GeVec3{1.5, 0.0, 0.0}, CAD_GeVec3{0.0, 1.5, 0.0}, CAD_GeVec3{0.0, 0.0, 0.0},
                            copies, 5) == 5)
        std::cout << "[cpp_api_test] array -> count: " << CAD_GetObjectCount() << std::endl;

    // 분해 — 문자를 윤곽선 폴리선으로 쪼갠다.
    // (폴리선·사각형이면 개별 선분으로 쪼개진다. 선·원·호는 대상이 아니다)
    // 새 id 를 주는 함수는 outIds = NULL 이면 개수만 알려 주고 아무것도 안 바꾼다 — 개수를 묻고 그만큼 칸을 준다.
    uint32_t textId = 0;
    if (CAD_CreateText(CAD_GeVec3{0.0, -2.0, 0.0}, "CAD", 300.0, nullptr, &textId) == CAD_OK) {
        const int32_t before = CAD_GetObjectCount();
        const int32_t n = CAD_EntityExplode(&textId, 1, /*keepOriginal*/false, nullptr, 0);
        if (n > 0) {
            std::vector<uint32_t> parts(static_cast<size_t>(n));
            CAD_EntityExplode(&textId, 1, false, parts.data(), static_cast<uint32_t>(parts.size()));
            std::cout << "[cpp_api_test] explode: " << before
                      << " -> " << CAD_GetObjectCount() << std::endl;
            CAD_Undo();     // 한 스텝이면 통째로 복원된다
            std::cout << "[cpp_api_test] after undo: " << CAD_GetObjectCount() << std::endl;
        }
    }
    ticks(1);   // 노드 그래프 등은 엔진이 한 프레임 돈 뒤에
    commandLineTest();
    nurbsTest();
    nodeGraphTest();
    documentTest();
    CAD_ZoomExtents();

    while (!exitAfterTests && !CAD_ShouldClose()) {
        if (!CAD_Tick()) break;
        std::this_thread::sleep_for(std::chrono::milliseconds(16));
    }

    CAD_DeleteObject(boxId);
    CAD_DestroyEngine();

    std::cout << "[cpp_api_test] done" << std::endl;
    return 0;
}
