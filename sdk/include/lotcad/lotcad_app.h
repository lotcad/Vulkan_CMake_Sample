#pragma once
/* LotCAD C API - app  [AcAp (application / host)]
 * Engine lifetime, host view, input routing, overlay, clipboard, status messages.
 * 엔진 수명·호스트 창·입력 전달·오버레이·클립보드·상태줄 안내.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif
/* 엔진 버전 "0.1.0-beta"(lot_version.h). 엔진을 만들기 전에도 된다. 반환 = 전체 길이(NUL 제외), 칸이 모자라면 글자 경계에서 잘라 담는다. */
CAD_API int32_t    CAD_GetVersion(char* buf, uint32_t capacity);
/* 사용자 설정 폴더(창 위치·패널 배치·언어·그래픽·외부 연결 .ini, 사용자 파티클 프리셋, 사용자 plugins/) — CAD_CreateEngine **전에**.
 * NULL = OS 기본 폴더(Windows %APPDATA%\LotCAD · macOS ~/Library/Application Support/LotCAD · 리눅스 ~/.config/lotcad,
 *        환경 변수 LOTCAD_USER_DIR 가 있으면 그것 — 처음 한 번 실행 폴더의 .ini 를 옮겨 담는다),
 * "" = 실행 폴더(기본값 — 부르지 않으면 이것), 그 밖 = 그 폴더(없으면 만든다). 설치 폴더가 읽기 전용인 호스트는 NULL 을 넘길 것.
 * 에셋(models·textures·fonts·effects·languages)은 그대로 CAD_SetRuntimeAssetPath / 실행 폴더에서 읽는다. 폴더를 못 만들면 CAD_E_FAILED */
CAD_API CAD_Status CAD_SetUserDataPath(const char* pathUtf8);
CAD_API int32_t    CAD_GetUserDataPath(char* buf, uint32_t capacity);   /* 빈 글 = 실행 폴더 */

/* ⚠️ 루프 세 함수는 결과 코드가 아니라 **bool** 이다(사용자 결정 10/25 — 0 = 성공인 결과 코드로 바꾸면 if (!CAD_CreateEngine())·
 *    while (CAD_Tick()) 가 말없이 거꾸로 돈다). 실패 이유는 똑같이 CAD_GetLastError. */
CAD_API bool       CAD_CreateEngine(void);    /* 엔진 만들기(이미 있으면 true) — 이 스레드가 엔진 스레드가 된다. false 면 이유는 CAD_GetLastError */
CAD_API CAD_Status CAD_DestroyEngine(void);   /* 엔진 끄기(없으면 그냥 CAD_OK) — CAD_Post 로 맡기고 아직 안 불린 것은 버린다 */
CAD_API bool       CAD_Tick(void);            /* 한 프레임(맡긴 함수 → 입력 → 그리기). 창을 닫았으면 false */

/* ── 다른 스레드에서 (AcApDocManager::sendStringToExecute · executeInApplicationContext 자리) ──
 * 장면 함수는 엔진 스레드(CAD_Tick 을 부르는 스레드)에서만 부른다. 작업 스레드·네트워크 콜백은 CAD_Post 로 함수를 맡기면
 * 엔진 스레드의 다음 CAD_Tick 시작에 맡긴 차례대로 불린다(쉬고 있는 엔진 루프는 깨운다). 콜백 안에서 CAD_* 를 마음대로 불러도 된다.
 * 새 규칙: CAD_OK / fn = NULL 이면 CAD_E_INVALID_ARG / 엔진 없음 = CAD_E_NO_ENGINE. 아무 스레드에서나.
 * 엔진이 꺼질 때(CAD_DestroyEngine) 아직 안 불린 것은 부르지 않고 버린다 — user 가 가리키는 것은 부른 쪽이 정리할 것 */
typedef void (*CAD_PostFn)(void* user);
/* fn(user) 를 다음 CAD_Tick 에 엔진 스레드에서 부르도록 맡긴다 — 아무 스레드에서나 */
CAD_API CAD_Status CAD_Post(CAD_PostFn fn, void* user);
/* 지금 스레드가 엔진 스레드인가(엔진을 만든 스레드, CAD_Tick 을 부른 뒤엔 마지막으로 부른 스레드) — 아무 스레드에서나.
 * 엔진이 없으면 CAD_E_NO_ENGINE + *outIsEngine = false */
CAD_API CAD_Status CAD_IsEngineThread(bool* outIsEngine);
CAD_API bool       CAD_ShouldClose(void);     /* 창을 닫으라는 요청이 왔나(엔진이 없으면 true) — 루프 조건이라 bool */
/* 창 닫기 요청을 엔진이 무시하게(호스트가 자기 창 닫기로 처리할 때) */
CAD_API CAD_Status CAD_SetIgnoreCloseRequest(bool ignore);
/* 에셋 폴더(models·textures·fonts·effects·languages) — UTF-8. 빈 경로 CAD_E_INVALID_ARG · 폴더가 아님 CAD_E_NOT_FOUND */
CAD_API CAD_Status CAD_SetRuntimeAssetPath(const char* path);
/* 호스트 창(HWND · NSView · UIView · ANativeWindow · X11 Window) — CAD_CreateEngine 전이면 맡아 뒀다가 만들 때 쓰고,
 * 뒤면 그 자리에서 다시 붙인다(CAD_DetachView 다음 — 장면 그대로). 핸들 NULL CAD_E_INVALID_ARG */
CAD_API CAD_Status CAD_AttachView(void* nativeHandle, int32_t width, int32_t height);
CAD_API CAD_Status CAD_ResizeView(int32_t width, int32_t height);
CAD_API CAD_Status CAD_DetachView(void);

/* ── 입력 넘기기 — 호스트 창의 마우스·키 이벤트를 그대로. 넣기만 하고 돌려줄 것이 없어 void(엔진이 없으면 그냥 무시) ── */

CAD_API void CAD_OnMouseDown(int button, double x, double y, int modifiers);
CAD_API void CAD_OnMouseUp(int button, double x, double y, int modifiers);
CAD_API void CAD_OnMouseMove(double x, double y);
CAD_API void CAD_OnMouseWheel(double x, double y, double deltaX, double deltaY);
CAD_API void CAD_OnKeyDown(int key, int modifiers);
CAD_API void CAD_OnKeyUp(int key, int modifiers);

/* ── 외부 UI 오버레이 ────────────────────────────────────────────────
 *
 * 엔진이 이미 시작한 swapchain render pass 안에서 외부 UI가 draw command를
 * 기록할 수 있게 빌린 Vulkan 컨텍스트를 전달한다. 모든 handle은 엔진 소유다.
 * 콜백은 빌린 handle을 파괴하거나 present를 호출하면 안 된다.
 * 외부 렌더러가 자체 텍스처 업로드 명령을 graphicsQueue에 제출할 경우
 * 호스트의 렌더 명령과 동기화할 책임은 외부 렌더러에 있다.
 *
 * 콜백 반환값은 CAD_OVERLAY_CAPTURE_* 비트다. 이전 프레임 반환값을 다음 입력
 * 라우팅에 사용해, UI가 처리하는 포인터/키보드 입력이 CAD 뷰로 새지 않게 한다.
 */
typedef struct CAD_OverlayFrameInfo {
    uint32_t structSize;
    uint64_t physicalDevice;
    uint64_t device;
    uint64_t graphicsQueue;
    uint64_t renderPass;
    uint64_t commandBuffer;
    uint32_t graphicsQueueFamily;
    uint32_t frameIndex;
    uint32_t frameCount;
    uint32_t framebufferWidth;
    uint32_t framebufferHeight;
    int windowWidth;
    int windowHeight;
    float dpiScale;
    double pointerX;
    double pointerY;
    uint32_t pointerButtons;
    int modifiers;
    uint32_t sampleCount;
} CAD_OverlayFrameInfo;

enum {
    CAD_OVERLAY_CAPTURE_POINTER = 1u << 0,
    CAD_OVERLAY_CAPTURE_KEYBOARD = 1u << 1
};

typedef uint32_t (*CAD_OverlayRenderFn)(
    const CAD_OverlayFrameInfo* frame,
    void* user);

CAD_API CAD_Status CAD_SetOverlayRenderCallback(
    CAD_OverlayRenderFn callback,
    void* user);

typedef struct CAD_OverlayPointerInfo {
    uint32_t structSize;
    int windowWidth;
    int windowHeight;
    double x;
    double y;
    uint32_t buttons;
    int modifiers;
} CAD_OverlayPointerInfo;
typedef uint32_t (*CAD_OverlayInputFn)(
    const CAD_OverlayPointerInfo* pointer,
    void* user);

CAD_API CAD_Status CAD_SetOverlayInputCallback(
    CAD_OverlayInputFn callback,
    void* user);

// ── Win32 호스트(MFC 등) 편의용 키 입력 ──
// 엔진 단축키는 GLFW 키코드 기준인데 Win32 는 VK_* 코드를 준다. WM_KEYDOWN/WM_KEYUP 의
// nChar(VK 코드)를 그대로 넘기면 내부에서 GLFW 키코드로 변환 + Ctrl/Shift/Alt 수정자를
// GetKeyState 로 자동 감지해 라우팅한다. (Windows 전용 — 호스트는 변환 신경 안 써도 됨)
#if defined(_WIN32)
CAD_API void CAD_OnKeyDownVK(int vkCode);
CAD_API void CAD_OnKeyUpVK(int vkCode);
#endif

// 터치 입력 라우팅: (x,y)(창 안 좌표) 에 이동 기즈모 핸들이 있으면 *outHit = true.
// 호출자(예: iOS)가 1손가락 드래그 시작 시 호출해 기즈모 조작(left) vs 궤도회전(right) 결정.
CAD_API CAD_Status CAD_GizmoHitTest(double x, double y, bool* outHit);
// 기즈모 핸들 hit 허용범위를 터치용으로 확대 (앱 시작 시 한 번 호출).
CAD_API CAD_Status CAD_SetGizmoTouchMode(bool enabled);
// OSnap(끝점/중점/중심…) 허용범위를 터치용으로 확대 — 12px → 18px (가상 커서 기준).
// **선택 픽 반경도 같이 커진다** — 선·폴리선·치수(치수선/보조선/화살표/값 문자) 탭 10px → 30px.
// 선택 탭은 손가락이 직접 짚으므로 3배 레티나 10pt 에 맞춘 값. 앱 시작 시 한 번 호출.
CAD_API CAD_Status CAD_SetSnapTouchMode(bool enabled);

/* ── 클립보드 (모바일용) ──────────────────────────────────────────────────
 *
 * 데스크톱은 ImGui 백엔드가 OS 클립보드로 연결해 주지만, iOS/안드로이드는 그게 없다.
 * 클립보드가 Swift 의 UIPasteboard / Kotlin 의 ClipboardManager 쪽에 있어서
 * C++ 에서 직접 못 만진다. 그래서 **호스트가 대신 처리**한다.
 *
 *   복사      : 엔진이 복사할 때 등록한 콜백이 불린다 → 호스트가 OS 클립보드에 넣는다
 *   붙여넣기  : 호스트가 CAD_PasteText 로 밀어 넣는다 (엔진이 물어보지 않는다)
 *
 * 붙여넣기를 "미는" 이유: 엔진이 동기로 물어보면 호스트가 돌려주는 문자열의 수명을
 * 누가 책임지는지가 애매해진다. 모바일 UX 도 "붙여넣기 버튼을 누른다" 라 미는 쪽이 맞다.
 * 데스크톱에서도 등록하면 이쪽이 우선한다(임베드 앱이 자기 정책을 쓰고 싶을 때).
 */
CAD_API CAD_Status CAD_SetOnCopyText(void (*cb)(const char* utf8));   /* NULL = 해제 */
CAD_API void       CAD_PasteText(const char* utf8);                    /* 입력 넘기기라 void */

/* 상태줄 임시 안내(시연 자막 등). seconds <= 0 이면 지금 문구를 지운다. */
CAD_API CAD_Status CAD_ShowMessage(const char* textUtf8, double seconds);

#ifdef __cplusplus
}
#endif
