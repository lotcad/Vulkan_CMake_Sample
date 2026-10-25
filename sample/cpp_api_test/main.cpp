#include "../../sdk/include/LotCAD_API.h"

#include <chrono>
#include <cstdint>
#include <filesystem>
#include <iostream>
#include <thread>
#include <vector>

int main() {
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
    CAD_SelectObject(boxId, false);
    CAD_RequestZoomExtents();

    CAD_GeVec3 p{};
    if (CAD_GetPosition(boxId, &p) == CAD_OK) {
        std::cout << "[cpp_api_test] box position: "
                  << p.x << ", " << p.y << ", " << p.z << std::endl;
    }

    std::cout << "[cpp_api_test] object count: "
              << CAD_GetObjectCount() << std::endl;
    std::cout << "[cpp_api_test] selected count: "
              << CAD_GetSelectedCount() << std::endl;

    // ── 편집 명령 예시 ──
    // 배열 — 박스를 X 로 3 × Y 로 2(간격 1.5) 복제. 대상은 id 로, 간격은 월드 벡터로. 반환 = 만든 사본 수
    uint32_t copies[5] = {};
    if (CAD_EntityArrayRect(&boxId, 1, 3, 2, 1, CAD_GeVec3{1.5, 0.0, 0.0}, CAD_GeVec3{0.0, 1.5, 0.0}, CAD_GeVec3{0.0, 0.0, 0.0},
                            copies, 5) == 5)
        std::cout << "[cpp_api_test] array -> count: " << CAD_GetObjectCount() << std::endl;

    // 분해 — 문자를 윤곽선 폴리선으로 쪼갠다.
    // (폴리선·사각형이면 개별 선분으로 쪼개진다. 선·원·호는 대상이 아니다)
    // 새 id 를 주는 함수는 outIds = NULL 이면 개수만 알려 주고 아무것도 안 바꾼다 — 개수를 묻고 그만큼 칸을 준다.
    const uint32_t textId = CAD_CreateText(0.0f, -2.0f, 0.0f, "CAD", 300.0f);
    if (textId != 0) {
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
    CAD_RequestZoomExtents();

    while (!CAD_ShouldClose()) {
        if (!CAD_Tick()) break;
        std::this_thread::sleep_for(std::chrono::milliseconds(16));
    }

    CAD_DeleteObject(boxId);
    CAD_DestroyEngine();

    std::cout << "[cpp_api_test] done" << std::endl;
    return 0;
}
