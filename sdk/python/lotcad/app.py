# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — App 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_OVERLAY_CAPTURE_POINTER', 'CAD_OVERLAY_CAPTURE_KEYBOARD', 'CAD_GetVersion', 'CAD_SetUserDataPath', 'CAD_GetUserDataPath', 'CAD_CreateEngine', 'CAD_DestroyEngine', 'CAD_Tick', 'CAD_Post', 'CAD_IsEngineThread', 'CAD_ShouldClose', 'CAD_SetIgnoreCloseRequest', 'CAD_SetRuntimeAssetPath', 'CAD_AttachView', 'CAD_ResizeView', 'CAD_DetachView', 'CAD_OnMouseDown', 'CAD_OnMouseUp', 'CAD_OnMouseMove', 'CAD_OnMouseWheel', 'CAD_OnKeyDown', 'CAD_OnKeyUp', 'CAD_SetOverlayRenderCallback', 'CAD_SetOverlayInputCallback', 'CAD_OnKeyDownVK', 'CAD_OnKeyUpVK', 'CAD_GizmoHitTest', 'CAD_SetGizmoTouchMode', 'CAD_SetSnapTouchMode', 'CAD_SetOnCopyText', 'CAD_SetOnCopyText_cb', 'CAD_PasteText', 'CAD_ShowMessage']

_f = _n.native

CAD_OVERLAY_CAPTURE_POINTER = 1
CAD_OVERLAY_CAPTURE_KEYBOARD = 2

CAD_SetOnCopyText_cb = _c.CFUNCTYPE(None, _c.c_char_p)

_n.bind("CAD_GetVersion", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_SetUserDataPath", _c.c_int32, [_c.c_char_p])
_n.bind("CAD_GetUserDataPath", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_CreateEngine", _c.c_bool, [])
_n.bind("CAD_DestroyEngine", _c.c_int32, [])
_n.bind("CAD_Tick", _c.c_bool, [])
_n.bind("CAD_Post", _c.c_int32, [CAD_PostFn, _c.c_void_p])
_n.bind("CAD_IsEngineThread", _c.c_int32, [_c.POINTER(_c.c_bool)])
_n.bind("CAD_ShouldClose", _c.c_bool, [])
_n.bind("CAD_SetIgnoreCloseRequest", _c.c_int32, [_c.c_bool])
_n.bind("CAD_SetRuntimeAssetPath", _c.c_int32, [_c.c_char_p])
_n.bind("CAD_AttachView", _c.c_int32, [_c.c_void_p, _c.c_int32, _c.c_int32])
_n.bind("CAD_ResizeView", _c.c_int32, [_c.c_int32, _c.c_int32])
_n.bind("CAD_DetachView", _c.c_int32, [])
_n.bind("CAD_OnMouseDown", None, [_c.c_int, _c.c_double, _c.c_double, _c.c_int])
_n.bind("CAD_OnMouseUp", None, [_c.c_int, _c.c_double, _c.c_double, _c.c_int])
_n.bind("CAD_OnMouseMove", None, [_c.c_double, _c.c_double])
_n.bind("CAD_OnMouseWheel", None, [_c.c_double, _c.c_double, _c.c_double, _c.c_double])
_n.bind("CAD_OnKeyDown", None, [_c.c_int, _c.c_int])
_n.bind("CAD_OnKeyUp", None, [_c.c_int, _c.c_int])
_n.bind("CAD_SetOverlayRenderCallback", _c.c_int32, [CAD_OverlayRenderFn, _c.c_void_p])
_n.bind("CAD_SetOverlayInputCallback", _c.c_int32, [CAD_OverlayInputFn, _c.c_void_p])
_n.bind("CAD_OnKeyDownVK", None, [_c.c_int])
_n.bind("CAD_OnKeyUpVK", None, [_c.c_int])
_n.bind("CAD_GizmoHitTest", _c.c_int32, [_c.c_double, _c.c_double, _c.POINTER(_c.c_bool)])
_n.bind("CAD_SetGizmoTouchMode", _c.c_int32, [_c.c_bool])
_n.bind("CAD_SetSnapTouchMode", _c.c_int32, [_c.c_bool])
_n.bind("CAD_SetOnCopyText", _c.c_int32, [CAD_SetOnCopyText_cb])
_n.bind("CAD_PasteText", None, [_c.c_char_p])
_n.bind("CAD_ShowMessage", _c.c_int32, [_c.c_char_p, _c.c_double])


def CAD_GetVersion() -> str | None:
    """C: int32_t CAD_GetVersion(char* buf, uint32_t capacity)

    엔진 버전 "0.1.0-beta"(lot_version.h). 엔진을 만들기 전에도 된다. 반환 = 전체 길이(NUL 제외), 칸이 모자라면 글자 경계에서 잘라 담는다.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetVersion(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_SetUserDataPath(pathUtf8: str | None) -> int:
    """C: CAD_Status CAD_SetUserDataPath(const char* pathUtf8)

    사용자 설정 폴더(창 위치·패널 배치·언어·그래픽·외부 연결 .ini, 사용자 파티클 프리셋, 사용자 plugins/) — CAD_CreateEngine **전에**.
    NULL = OS 기본 폴더(Windows %APPDATA%\\LotCAD · macOS ~/Library/Application Support/LotCAD · 리눅스 ~/.config/lotcad,
           환경 변수 LOTCAD_USER_DIR 가 있으면 그것 — 처음 한 번 실행 폴더의 .ini 를 옮겨 담는다),
    "" = 실행 폴더(기본값 — 부르지 않으면 이것), 그 밖 = 그 폴더(없으면 만든다). 설치 폴더가 읽기 전용인 호스트는 NULL 을 넘길 것.
    에셋(models·textures·fonts·effects·languages)은 그대로 CAD_SetRuntimeAssetPath / 실행 폴더에서 읽는다. 폴더를 못 만들면 CAD_E_FAILED
    """
    return _f.CAD_SetUserDataPath(_n.text(pathUtf8))


def CAD_GetUserDataPath() -> str | None:
    """C: int32_t CAD_GetUserDataPath(char* buf, uint32_t capacity)

    빈 글 = 실행 폴더

    묶음 주석: 사용자 설정 폴더(창 위치·패널 배치·언어·그래픽·외부 연결 .ini, 사용자 파티클 프리셋, 사용자 plugins/) — CAD_CreateEngine **전에**.
    NULL = OS 기본 폴더(Windows %APPDATA%\\LotCAD · macOS ~/Library/Application Support/LotCAD · 리눅스 ~/.config/lotcad,
           환경 변수 LOTCAD_USER_DIR 가 있으면 그것 — 처음 한 번 실행 폴더의 .ini 를 옮겨 담는다),
    "" = 실행 폴더(기본값 — 부르지 않으면 이것), 그 밖 = 그 폴더(없으면 만든다). 설치 폴더가 읽기 전용인 호스트는 NULL 을 넘길 것.
    에셋(models·textures·fonts·effects·languages)은 그대로 CAD_SetRuntimeAssetPath / 실행 폴더에서 읽는다. 폴더를 못 만들면 CAD_E_FAILED
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetUserDataPath(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_CreateEngine() -> bool:
    """C: bool CAD_CreateEngine(void)

    ⚠️ 루프 세 함수는 결과 코드가 아니라 **bool** 이다(사용자 결정 10/25 — 0 = 성공인 결과 코드로 바꾸면 if (!CAD_CreateEngine())·
       while (CAD_Tick()) 가 말없이 거꾸로 돈다). 실패 이유는 똑같이 CAD_GetLastError.
    엔진 만들기(이미 있으면 true) — 이 스레드가 엔진 스레드가 된다. false 면 이유는 CAD_GetLastError
    """
    return _f.CAD_CreateEngine()


def CAD_DestroyEngine() -> int:
    """C: CAD_Status CAD_DestroyEngine(void)

    엔진 끄기(없으면 그냥 CAD_OK) — CAD_Post 로 맡기고 아직 안 불린 것은 버린다

    묶음 주석: ⚠️ 루프 세 함수는 결과 코드가 아니라 **bool** 이다(사용자 결정 10/25 — 0 = 성공인 결과 코드로 바꾸면 if (!CAD_CreateEngine())·
       while (CAD_Tick()) 가 말없이 거꾸로 돈다). 실패 이유는 똑같이 CAD_GetLastError.
    """
    _n.forget_once()   # 엔진이 버린 맡긴 콜백
    return _f.CAD_DestroyEngine()


def CAD_Tick() -> bool:
    """C: bool CAD_Tick(void)

    한 프레임(맡긴 함수 → 입력 → 그리기). 창을 닫았으면 false

    묶음 주석: ⚠️ 루프 세 함수는 결과 코드가 아니라 **bool** 이다(사용자 결정 10/25 — 0 = 성공인 결과 코드로 바꾸면 if (!CAD_CreateEngine())·
       while (CAD_Tick()) 가 말없이 거꾸로 돈다). 실패 이유는 똑같이 CAD_GetLastError.
    """
    return _f.CAD_Tick()


def CAD_Post(fn: Callable | None, user: int | None) -> int:
    """C: CAD_Status CAD_Post(CAD_PostFn fn, void* user)

    fn(user) 를 다음 CAD_Tick 에 엔진 스레드에서 부르도록 맡긴다 — 아무 스레드에서나
    """
    _cb_fn = _n.callback_once(CAD_PostFn, fn, ())
    _r = _f.CAD_Post(_cb_fn, user)
    if _r != 0:   # 맡기지 못함 — 불릴 일이 없으니 바로 놓는다
        _n.release_once(_cb_fn)
    return _r


def CAD_IsEngineThread() -> tuple[int, bool]:
    """C: CAD_Status CAD_IsEngineThread(bool* outIsEngine)

    지금 스레드가 엔진 스레드인가(엔진을 만든 스레드, CAD_Tick 을 부른 뒤엔 마지막으로 부른 스레드) — 아무 스레드에서나.
    엔진이 없으면 CAD_E_NO_ENGINE + *outIsEngine = false
    """
    outIsEngine = _c.c_bool()
    _r = _f.CAD_IsEngineThread(_c.byref(outIsEngine))
    return (_r, outIsEngine.value)


def CAD_ShouldClose() -> bool:
    """C: bool CAD_ShouldClose(void)

    창을 닫으라는 요청이 왔나(엔진이 없으면 true) — 루프 조건이라 bool

    묶음 주석: 지금 스레드가 엔진 스레드인가(엔진을 만든 스레드, CAD_Tick 을 부른 뒤엔 마지막으로 부른 스레드) — 아무 스레드에서나.
    엔진이 없으면 CAD_E_NO_ENGINE + *outIsEngine = false
    """
    return _f.CAD_ShouldClose()


def CAD_SetIgnoreCloseRequest(ignore: bool) -> int:
    """C: CAD_Status CAD_SetIgnoreCloseRequest(bool ignore)

    창 닫기 요청을 엔진이 무시하게(호스트가 자기 창 닫기로 처리할 때)
    """
    return _f.CAD_SetIgnoreCloseRequest(ignore)


def CAD_SetRuntimeAssetPath(path: str | None) -> int:
    """C: CAD_Status CAD_SetRuntimeAssetPath(const char* path)

    에셋 폴더(models·textures·fonts·effects·languages) — UTF-8. 빈 경로 CAD_E_INVALID_ARG · 폴더가 아님 CAD_E_NOT_FOUND
    """
    return _f.CAD_SetRuntimeAssetPath(_n.text(path))


def CAD_AttachView(nativeHandle: int | None, width: int, height: int) -> int:
    """C: CAD_Status CAD_AttachView(void* nativeHandle, int32_t width, int32_t height)

    호스트 창(HWND · NSView · UIView · ANativeWindow · X11 Window) — CAD_CreateEngine 전이면 맡아 뒀다가 만들 때 쓰고,
    뒤면 그 자리에서 다시 붙인다(CAD_DetachView 다음 — 장면 그대로). 핸들 NULL CAD_E_INVALID_ARG
    """
    return _f.CAD_AttachView(nativeHandle, width, height)


def CAD_ResizeView(width: int, height: int) -> int:
    """C: CAD_Status CAD_ResizeView(int32_t width, int32_t height)

    호스트 창(HWND · NSView · UIView · ANativeWindow · X11 Window) — CAD_CreateEngine 전이면 맡아 뒀다가 만들 때 쓰고,
    뒤면 그 자리에서 다시 붙인다(CAD_DetachView 다음 — 장면 그대로). 핸들 NULL CAD_E_INVALID_ARG
    """
    return _f.CAD_ResizeView(width, height)


def CAD_DetachView() -> int:
    """C: CAD_Status CAD_DetachView(void)

    호스트 창(HWND · NSView · UIView · ANativeWindow · X11 Window) — CAD_CreateEngine 전이면 맡아 뒀다가 만들 때 쓰고,
    뒤면 그 자리에서 다시 붙인다(CAD_DetachView 다음 — 장면 그대로). 핸들 NULL CAD_E_INVALID_ARG
    """
    return _f.CAD_DetachView()


def CAD_OnMouseDown(button: int, x: float, y: float, modifiers: int) -> None:
    """C: void CAD_OnMouseDown(int button, double x, double y, int modifiers)

    입력 넘기기 — 호스트 창의 마우스·키 이벤트를 그대로. 넣기만 하고 돌려줄 것이 없어 void(엔진이 없으면 그냥 무시)
    """
    _f.CAD_OnMouseDown(button, x, y, modifiers)


def CAD_OnMouseUp(button: int, x: float, y: float, modifiers: int) -> None:
    """C: void CAD_OnMouseUp(int button, double x, double y, int modifiers)

    입력 넘기기 — 호스트 창의 마우스·키 이벤트를 그대로. 넣기만 하고 돌려줄 것이 없어 void(엔진이 없으면 그냥 무시)
    """
    _f.CAD_OnMouseUp(button, x, y, modifiers)


def CAD_OnMouseMove(x: float, y: float) -> None:
    """C: void CAD_OnMouseMove(double x, double y)

    입력 넘기기 — 호스트 창의 마우스·키 이벤트를 그대로. 넣기만 하고 돌려줄 것이 없어 void(엔진이 없으면 그냥 무시)
    """
    _f.CAD_OnMouseMove(x, y)


def CAD_OnMouseWheel(x: float, y: float, deltaX: float, deltaY: float) -> None:
    """C: void CAD_OnMouseWheel(double x, double y, double deltaX, double deltaY)

    입력 넘기기 — 호스트 창의 마우스·키 이벤트를 그대로. 넣기만 하고 돌려줄 것이 없어 void(엔진이 없으면 그냥 무시)
    """
    _f.CAD_OnMouseWheel(x, y, deltaX, deltaY)


def CAD_OnKeyDown(key: int, modifiers: int) -> None:
    """C: void CAD_OnKeyDown(int key, int modifiers)

    입력 넘기기 — 호스트 창의 마우스·키 이벤트를 그대로. 넣기만 하고 돌려줄 것이 없어 void(엔진이 없으면 그냥 무시)
    """
    _f.CAD_OnKeyDown(key, modifiers)


def CAD_OnKeyUp(key: int, modifiers: int) -> None:
    """C: void CAD_OnKeyUp(int key, int modifiers)

    입력 넘기기 — 호스트 창의 마우스·키 이벤트를 그대로. 넣기만 하고 돌려줄 것이 없어 void(엔진이 없으면 그냥 무시)
    """
    _f.CAD_OnKeyUp(key, modifiers)


def CAD_SetOverlayRenderCallback(callback: Callable | None, user: int | None) -> int:
    """C: CAD_Status CAD_SetOverlayRenderCallback( CAD_OverlayRenderFn callback, void* user)
    """
    _cb_callback = _n.callback(CAD_OverlayRenderFn, callback, ())
    _n.keep("CAD_SetOverlayRenderCallback.callback", _cb_callback, replace=True)
    return _f.CAD_SetOverlayRenderCallback(_cb_callback, user)


def CAD_SetOverlayInputCallback(callback: Callable | None, user: int | None) -> int:
    """C: CAD_Status CAD_SetOverlayInputCallback( CAD_OverlayInputFn callback, void* user)
    """
    _cb_callback = _n.callback(CAD_OverlayInputFn, callback, ())
    _n.keep("CAD_SetOverlayInputCallback.callback", _cb_callback, replace=True)
    return _f.CAD_SetOverlayInputCallback(_cb_callback, user)


def CAD_OnKeyDownVK(vkCode: int) -> None:
    """C: void CAD_OnKeyDownVK(int vkCode)
    Windows 전용 — 다른 OS 의 라이브러리엔 없어 부르면 NotImplementedError.
    """
    _f.CAD_OnKeyDownVK(vkCode)


def CAD_OnKeyUpVK(vkCode: int) -> None:
    """C: void CAD_OnKeyUpVK(int vkCode)
    Windows 전용 — 다른 OS 의 라이브러리엔 없어 부르면 NotImplementedError.
    """
    _f.CAD_OnKeyUpVK(vkCode)


def CAD_GizmoHitTest(x: float, y: float) -> tuple[int, bool]:
    """C: CAD_Status CAD_GizmoHitTest(double x, double y, bool* outHit)

    터치 입력 라우팅: (x,y)(창 안 좌표) 에 이동 기즈모 핸들이 있으면 *outHit = true.
    호출자(예: iOS)가 1손가락 드래그 시작 시 호출해 기즈모 조작(left) vs 궤도회전(right) 결정.
    """
    outHit = _c.c_bool()
    _r = _f.CAD_GizmoHitTest(x, y, _c.byref(outHit))
    return (_r, outHit.value)


def CAD_SetGizmoTouchMode(enabled: bool) -> int:
    """C: CAD_Status CAD_SetGizmoTouchMode(bool enabled)

    기즈모 핸들 hit 허용범위를 터치용으로 확대 (앱 시작 시 한 번 호출).
    """
    return _f.CAD_SetGizmoTouchMode(enabled)


def CAD_SetSnapTouchMode(enabled: bool) -> int:
    """C: CAD_Status CAD_SetSnapTouchMode(bool enabled)

    OSnap(끝점/중점/중심…) 허용범위를 터치용으로 확대 — 12px → 18px (가상 커서 기준).
    **선택 픽 반경도 같이 커진다** — 선·폴리선·치수(치수선/보조선/화살표/값 문자) 탭 10px → 30px.
    선택 탭은 손가락이 직접 짚으므로 3배 레티나 10pt 에 맞춘 값. 앱 시작 시 한 번 호출.
    """
    return _f.CAD_SetSnapTouchMode(enabled)


def CAD_SetOnCopyText(cb: Callable | None) -> int:
    """C: CAD_Status CAD_SetOnCopyText(void (*cb)(const char* utf8))

    클립보드 (모바일용)

    데스크톱은 ImGui 백엔드가 OS 클립보드로 연결해 주지만, iOS/안드로이드는 그게 없다.
    클립보드가 Swift 의 UIPasteboard / Kotlin 의 ClipboardManager 쪽에 있어서
    C++ 에서 직접 못 만진다. 그래서 **호스트가 대신 처리**한다.

      복사      : 엔진이 복사할 때 등록한 콜백이 불린다 → 호스트가 OS 클립보드에 넣는다
      붙여넣기  : 호스트가 CAD_PasteText 로 밀어 넣는다 (엔진이 물어보지 않는다)

    붙여넣기를 "미는" 이유: 엔진이 동기로 물어보면 호스트가 돌려주는 문자열의 수명을
    누가 책임지는지가 애매해진다. 모바일 UX 도 "붙여넣기 버튼을 누른다" 라 미는 쪽이 맞다.
    데스크톱에서도 등록하면 이쪽이 우선한다(임베드 앱이 자기 정책을 쓰고 싶을 때).
    NULL = 해제
    """
    _cb_cb = _n.callback(CAD_SetOnCopyText_cb, cb, (0,))
    _n.keep("CAD_SetOnCopyText.cb", _cb_cb, replace=True)
    return _f.CAD_SetOnCopyText(_cb_cb)


def CAD_PasteText(utf8: str | None) -> None:
    """C: void CAD_PasteText(const char* utf8)

    입력 넘기기라 void

    묶음 주석: 클립보드 (모바일용)

    데스크톱은 ImGui 백엔드가 OS 클립보드로 연결해 주지만, iOS/안드로이드는 그게 없다.
    클립보드가 Swift 의 UIPasteboard / Kotlin 의 ClipboardManager 쪽에 있어서
    C++ 에서 직접 못 만진다. 그래서 **호스트가 대신 처리**한다.

      복사      : 엔진이 복사할 때 등록한 콜백이 불린다 → 호스트가 OS 클립보드에 넣는다
      붙여넣기  : 호스트가 CAD_PasteText 로 밀어 넣는다 (엔진이 물어보지 않는다)

    붙여넣기를 "미는" 이유: 엔진이 동기로 물어보면 호스트가 돌려주는 문자열의 수명을
    누가 책임지는지가 애매해진다. 모바일 UX 도 "붙여넣기 버튼을 누른다" 라 미는 쪽이 맞다.
    데스크톱에서도 등록하면 이쪽이 우선한다(임베드 앱이 자기 정책을 쓰고 싶을 때).
    """
    _f.CAD_PasteText(_n.text(utf8))


def CAD_ShowMessage(textUtf8: str | None, seconds: float) -> int:
    """C: CAD_Status CAD_ShowMessage(const char* textUtf8, double seconds)

    상태줄 임시 안내(시연 자막 등). seconds <= 0 이면 지금 문구를 지운다.
    """
    return _f.CAD_ShowMessage(_n.text(textUtf8), seconds)
