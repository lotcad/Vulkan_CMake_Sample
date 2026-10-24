# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Editor 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_ED_KIND_POINT', 'CAD_ED_KIND_CORNER', 'CAD_ED_KIND_DISTANCE', 'CAD_ED_KIND_ANGLE', 'CAD_ED_KIND_INTEGER', 'CAD_ED_KIND_REAL', 'CAD_ED_KIND_STRING', 'CAD_ED_KIND_KEYWORD', 'CAD_ED_KIND_ENTITY', 'CAD_ED_KIND_SELECTION', 'CAD_ED_RESULT_PENDING', 'CAD_ED_RESULT_NORMAL', 'CAD_ED_RESULT_NONE', 'CAD_ED_RESULT_KEYWORD', 'CAD_ED_RESULT_CANCEL', 'CAD_ED_NO_NULL', 'CAD_ED_NO_ZERO', 'CAD_ED_NO_NEGATIVE', 'CAD_ED_ARBITRARY', 'CAD_ED_ALLOW_SPACES', 'CAD_ED_PICKFIRST', 'CAD_ED_SINGLE', 'CAD_GetDimensionPointCount', 'CAD_GetPrompt', 'CAD_RequestStartBoxSketch', 'CAD_RequestStartLineSketch', 'CAD_RequestStartRectangleSketch', 'CAD_RequestStartCircleSketch', 'CAD_RequestStartPolygonSketch', 'CAD_RequestCyclePolygonSides', 'CAD_ExecuteCommand', 'CAD_RegisterCommand', 'CAD_UnregisterCommand', 'CAD_UnregisterCommandsByOwner', 'CAD_GetRegisteredCommandCount', 'CAD_GetRegisteredCommandName', 'CAD_GetRegisteredCommandTitle', 'CAD_RequestStartExtrude', 'CAD_RequestStartArcSketch', 'CAD_RequestCycleArcMode', 'CAD_RequestStartPolylineSketch', 'CAD_RequestOpenFileDialog', 'CAD_RequestSelectAll', 'CAD_RequestDeleteSelected', 'CAD_RequestClearAll', 'CAD_RequestAddCube', 'CAD_RequestStartLightPlacement', 'CAD_RequestCycleMaterial', 'CAD_RequestRemoveMaterial', 'CAD_JigBegin', 'CAD_JigBeginOne', 'CAD_JigState', 'CAD_JigCancel', 'CAD_JigMoveTo', 'CAD_JigCommit', 'CAD_JigSetBasePoint', 'CAD_JigGetDelta', 'CAD_JigBeginVariants', 'CAD_JigNextVariant', 'CAD_JigVariantIndex', 'CAD_JigVariantId', 'CAD_BeginTextEdit', 'CAD_IsTextEditing', 'CAD_TextEditInsert', 'CAD_TextEditBackspace', 'CAD_TextEditDelete', 'CAD_TextEditMoveCaret', 'CAD_TextEditCommit', 'CAD_TextEditCancel', 'CAD_GetSelectionContext', 'CAD_SelectObject', 'CAD_ClearSelection', 'CAD_SetOSnapEnabled', 'CAD_GetOSnapEnabled', 'CAD_SetOSnapModes', 'CAD_GetOSnapModes', 'CAD_SetOrthoEnabled', 'CAD_GetOrthoEnabled', 'CAD_SetPolarTracking', 'CAD_GetPolarTracking', 'CAD_SnapNearPoint', 'CAD_GetSelectedCount', 'CAD_GetSelectedObjectId', 'CAD_BeginGetPoint', 'CAD_BeginGetEntSel', 'CAD_IsPicking', 'CAD_TryGetPickResult', 'CAD_CancelPick', 'CAD_SetSubobjectSelectionMode', 'CAD_GetSubobjectSelectionMode', 'CAD_PickSubobject', 'CAD_GetSubobjectSelectionId', 'CAD_GetSelectedFaceTriangles', 'CAD_GetSelectedBRepFaceId', 'CAD_GetSelectedEdge', 'CAD_RequestStartRevolve', 'CAD_GetStatusMessage', 'CAD_GetTransientMessage', 'CAD_EdGetPoint', 'CAD_EdGetCorner', 'CAD_EdGetDistance', 'CAD_EdGetAngle', 'CAD_EdGetInteger', 'CAD_EdGetReal', 'CAD_EdGetString', 'CAD_EdGetKeyword', 'CAD_EdEntSel', 'CAD_EdSSGet', 'CAD_EdGetInputResult', 'CAD_EdGetInputText', 'CAD_EdGetInputIds', 'CAD_EdCancelInput', 'CAD_EdSelectWindow', 'CAD_EdWorldToPixel', 'CAD_EdPixelToWorld', 'CAD_EdGetCommandState', 'CAD_EdGetCommandName']

_f = _n.native

CAD_ED_KIND_POINT = 1
CAD_ED_KIND_CORNER = 2
CAD_ED_KIND_DISTANCE = 3
CAD_ED_KIND_ANGLE = 4
CAD_ED_KIND_INTEGER = 5
CAD_ED_KIND_REAL = 6
CAD_ED_KIND_STRING = 7
CAD_ED_KIND_KEYWORD = 8
CAD_ED_KIND_ENTITY = 9
CAD_ED_KIND_SELECTION = 10
CAD_ED_RESULT_PENDING = 0
CAD_ED_RESULT_NORMAL = 1
CAD_ED_RESULT_NONE = 2
CAD_ED_RESULT_KEYWORD = 3
CAD_ED_RESULT_CANCEL = 4
CAD_ED_NO_NULL = 1
CAD_ED_NO_ZERO = 2
CAD_ED_NO_NEGATIVE = 4
CAD_ED_ARBITRARY = 8
CAD_ED_ALLOW_SPACES = 16
CAD_ED_PICKFIRST = 32
CAD_ED_SINGLE = 64

_n.bind("CAD_GetDimensionPointCount", _c.c_int, [])
_n.bind("CAD_GetPrompt", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_RequestStartBoxSketch", None, [])
_n.bind("CAD_RequestStartLineSketch", None, [])
_n.bind("CAD_RequestStartRectangleSketch", None, [])
_n.bind("CAD_RequestStartCircleSketch", None, [])
_n.bind("CAD_RequestStartPolygonSketch", None, [])
_n.bind("CAD_RequestCyclePolygonSides", None, [])
_n.bind("CAD_ExecuteCommand", _c.c_bool, [_c.c_char_p])
_n.bind("CAD_RegisterCommand", _c.c_bool, [_c.c_char_p, _c.c_char_p, CAD_CommandFn, _c.c_void_p, _c.c_uint])
_n.bind("CAD_UnregisterCommand", _c.c_bool, [_c.c_char_p])
_n.bind("CAD_UnregisterCommandsByOwner", _c.c_uint, [_c.c_uint])
_n.bind("CAD_GetRegisteredCommandCount", _c.c_uint, [])
_n.bind("CAD_GetRegisteredCommandName", _c.c_int, [_c.c_uint, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetRegisteredCommandTitle", _c.c_int, [_c.c_uint, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_RequestStartExtrude", None, [])
_n.bind("CAD_RequestStartArcSketch", None, [])
_n.bind("CAD_RequestCycleArcMode", None, [])
_n.bind("CAD_RequestStartPolylineSketch", None, [])
_n.bind("CAD_RequestOpenFileDialog", None, [])
_n.bind("CAD_RequestSelectAll", None, [])
_n.bind("CAD_RequestDeleteSelected", None, [])
_n.bind("CAD_RequestClearAll", None, [])
_n.bind("CAD_RequestAddCube", None, [])
_n.bind("CAD_RequestStartLightPlacement", None, [])
_n.bind("CAD_RequestCycleMaterial", None, [])
_n.bind("CAD_RequestRemoveMaterial", None, [])
_n.bind("CAD_JigBegin", _c.c_bool, [_c.c_int, _c.POINTER(_c.c_uint32), _c.c_int, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_JigBeginOne", _c.c_bool, [_c.c_int, _c.c_uint32, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_JigState", _c.c_int, [])
_n.bind("CAD_JigCancel", None, [])
_n.bind("CAD_JigMoveTo", _c.c_bool, [_c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_JigCommit", _c.c_bool, [])
_n.bind("CAD_JigSetBasePoint", _c.c_bool, [_c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_JigGetDelta", _c.c_bool, [_c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float)])
_n.bind("CAD_JigBeginVariants", _c.c_bool, [_c.c_int, _c.POINTER(_c.c_uint32), _c.c_int, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_JigNextVariant", _c.c_bool, [])
_n.bind("CAD_JigVariantIndex", _c.c_int, [])
_n.bind("CAD_JigVariantId", _c.c_uint32, [])
_n.bind("CAD_BeginTextEdit", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_IsTextEditing", _c.c_bool, [])
_n.bind("CAD_TextEditInsert", None, [_c.c_char_p])
_n.bind("CAD_TextEditBackspace", None, [])
_n.bind("CAD_TextEditDelete", None, [])
_n.bind("CAD_TextEditMoveCaret", None, [_c.c_int])
_n.bind("CAD_TextEditCommit", None, [])
_n.bind("CAD_TextEditCancel", None, [])
_n.bind("CAD_GetSelectionContext", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_SelectObject", _c.c_bool, [_c.c_uint32, _c.c_bool])
_n.bind("CAD_ClearSelection", None, [])
_n.bind("CAD_SetOSnapEnabled", _c.c_bool, [_c.c_bool])
_n.bind("CAD_GetOSnapEnabled", _c.c_bool, [])
_n.bind("CAD_SetOSnapModes", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_GetOSnapModes", _c.c_uint32, [])
_n.bind("CAD_SetOrthoEnabled", None, [_c.c_bool])
_n.bind("CAD_GetOrthoEnabled", _c.c_bool, [])
_n.bind("CAD_SetPolarTracking", _c.c_bool, [_c.c_bool, _c.c_float])
_n.bind("CAD_GetPolarTracking", _c.c_bool, [_c.POINTER(_c.c_float)])
_n.bind("CAD_SnapNearPoint", _c.c_int32, [CAD_GeVec3, _c.c_double, _c.c_uint32, _c.POINTER(CAD_OsnapOptions), _c.POINTER(CAD_OsnapPoint)])
_n.bind("CAD_GetSelectedCount", _c.c_uint32, [])
_n.bind("CAD_GetSelectedObjectId", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_BeginGetPoint", None, [_c.c_char_p])
_n.bind("CAD_BeginGetEntSel", None, [_c.c_char_p])
_n.bind("CAD_IsPicking", _c.c_bool, [])
_n.bind("CAD_TryGetPickResult", _c.c_bool, [_c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CancelPick", None, [])
_n.bind("CAD_SetSubobjectSelectionMode", _c.c_bool, [_c.c_int])
_n.bind("CAD_GetSubobjectSelectionMode", _c.c_int, [])
_n.bind("CAD_PickSubobject", _c.c_bool, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_GetSubobjectSelectionId", _c.c_uint32, [])
_n.bind("CAD_GetSelectedFaceTriangles", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_GetSelectedBRepFaceId", _c.c_int32, [])
_n.bind("CAD_GetSelectedEdge", _c.c_bool, [_c.POINTER(_c.c_float)])
_n.bind("CAD_RequestStartRevolve", None, [])
_n.bind("CAD_GetStatusMessage", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetTransientMessage", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_EdGetPoint", _c.c_int32, [_c.c_char_p, _c.POINTER(CAD_EdInputOptions)])
_n.bind("CAD_EdGetCorner", _c.c_int32, [_c.c_char_p, CAD_GeVec3, _c.POINTER(CAD_EdInputOptions)])
_n.bind("CAD_EdGetDistance", _c.c_int32, [_c.c_char_p, _c.POINTER(CAD_EdInputOptions)])
_n.bind("CAD_EdGetAngle", _c.c_int32, [_c.c_char_p, _c.POINTER(CAD_EdInputOptions)])
_n.bind("CAD_EdGetInteger", _c.c_int32, [_c.c_char_p, _c.POINTER(CAD_EdInputOptions)])
_n.bind("CAD_EdGetReal", _c.c_int32, [_c.c_char_p, _c.POINTER(CAD_EdInputOptions)])
_n.bind("CAD_EdGetString", _c.c_int32, [_c.c_char_p, _c.POINTER(CAD_EdInputOptions)])
_n.bind("CAD_EdGetKeyword", _c.c_int32, [_c.c_char_p, _c.POINTER(CAD_EdInputOptions)])
_n.bind("CAD_EdEntSel", _c.c_int32, [_c.c_char_p, _c.POINTER(CAD_EdInputOptions)])
_n.bind("CAD_EdSSGet", _c.c_int32, [_c.c_char_p, _c.POINTER(CAD_EdInputOptions)])
_n.bind("CAD_EdGetInputResult", _c.c_int32, [_c.POINTER(CAD_EdInputResult)])
_n.bind("CAD_EdGetInputText", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_EdGetInputIds", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_EdCancelInput", _c.c_int32, [])
_n.bind("CAD_EdSelectWindow", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, _c.POINTER(CAD_EdSelectOptions), _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_EdWorldToPixel", _c.c_int32, [CAD_GeVec3, _c.POINTER(_c.c_double), _c.POINTER(_c.c_double)])
_n.bind("CAD_EdPixelToWorld", _c.c_int32, [_c.c_double, _c.c_double, _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_EdGetCommandState", _c.c_int32, [_c.POINTER(CAD_EdCommandState)])
_n.bind("CAD_EdGetCommandName", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])


def CAD_GetDimensionPointCount() -> int:
    """C: int CAD_GetDimensionPointCount(void)

    진행 중인 치수 도구의 점 개수. 비활성이면 -1.
    모바일 커서 UI 의 [선택] 버튼 문구/종료 판단에 쓴다 — 클라이언트가 클릭을 세면
    엔진이 클릭을 거부하는 경우와 어긋나므로 반드시 엔진 값을 본다.
    """
    return _f.CAD_GetDimensionPointCount()


def CAD_GetPrompt() -> str | None:
    """C: int CAD_GetPrompt(char* buf, int bufLen)

    진행 중인 도구의 안내 문구("첫 번째 점을 지정" 등). 도구가 없으면 빈 문자열.
    모바일 커서 UI 가 **도구 종류와 무관하게** 활성 여부/안내를 알기 위해 매 틱 폴링한다.
    반환: 복사한 길이(널 제외). buf 가 작으면 잘라서 복사한다.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetPrompt(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_RequestStartBoxSketch() -> None:
    """C: void CAD_RequestStartBoxSketch(void)
    """
    _f.CAD_RequestStartBoxSketch()


def CAD_RequestStartLineSketch() -> None:
    """C: void CAD_RequestStartLineSketch(void)
    """
    _f.CAD_RequestStartLineSketch()


def CAD_RequestStartRectangleSketch() -> None:
    """C: void CAD_RequestStartRectangleSketch(void)
    """
    _f.CAD_RequestStartRectangleSketch()


def CAD_RequestStartCircleSketch() -> None:
    """C: void CAD_RequestStartCircleSketch(void)
    """
    _f.CAD_RequestStartCircleSketch()


def CAD_RequestStartPolygonSketch() -> None:
    """C: void CAD_RequestStartPolygonSketch(void)
    """
    _f.CAD_RequestStartPolygonSketch()


def CAD_RequestCyclePolygonSides() -> None:
    """C: void CAD_RequestCyclePolygonSides(void)
    """
    _f.CAD_RequestCyclePolygonSides()


def CAD_ExecuteCommand(name: str | None) -> bool:
    """C: bool CAD_ExecuteCommand(const char* name)

    명령 실행

    엔진의 **모든 명령**을 이름으로 실행한다. 아래 CAD_RequestXxx 들은 자주 쓰는 것만
    개별 함수로 뽑아 둔 것이고, 엔진에는 명령이 200개가 넘는다(trim / offset / fillet /
    ocr / navmap / imageattach …). 이 함수 하나면 그 전부가 열리고, 새 명령을 추가할
    때마다 API 를 늘리지 않아도 된다.

      CAD_ExecuteCommand("trim");        // 자르기
      CAD_ExecuteCommand("offset");      // 오프셋
      CAD_ExecuteCommand("2,3");         // 진행 중인 도구에 좌표/값 전달

    이름은 하단 명령행에 치는 것과 **똑같다**(영문·짧은 별칭·한글 모두).
    진행 중인 도구가 있으면 값 입력으로 전달된다 — 명령행과 완전히 같은 경로. "" (또는 " ") = 빈 Enter.
    반환: 알 수 없는 이름이면 false. 값 입력으로 소비된 경우도 true. 기다리는 도구가 없는데 "" 면 false.
    """
    return _f.CAD_ExecuteCommand(_n.text(name))


def CAD_RegisterCommand(name: str | None, title: str | None, fn: Callable | None, user: int | None, owner: int) -> bool:
    """C: bool CAD_RegisterCommand(const char* name, const char* title, CAD_CommandFn fn, void* user, unsigned int owner)

    명령 등록 (플러그인)

    플러그인이 **콘솔 명령을 추가**한다. 명령행이 이 엔진의 모든 기능 진입점이라,
    이것만 있으면 플러그인이 "기능" 이 된다. ObjectARX 의 acedRegCmds 자리.

      등록 후  명령행에 wall → 콜백 호출
                 CAD_ExecuteCommand("wall") 도 같은 경로

    name   조회 키. 대소문자를 안 가린다(한글 이름도 된다).
    title  메뉴·툴바에 들어갈 표시 이름. NULL 이면 name 을 쓴다.
    fn     콜백. **C 함수 포인터**라 C++/C#/Python 어디서든 같은 모양으로 쓴다.
    user   그대로 돌려받는다(플러그인 인스턴스 포인터 등).
    owner  플러그인 ID. 언로드할 때 이 값으로 묶어 한꺼번에 지운다. 0 = 소유자 없음.

    실패 조건: 빈 이름 · fn 이 NULL · 이미 등록된 이름.
    ⚠️ 엔진 기본 명령(line/circle …)과 같은 이름은 등록도지만 불리지 않는다 —
       기본 명령이 먼저 조회된다(플러그인이 기본 동작을 가로채는 것을 막는다).
    ⚠️ 콜백은 **엔진과 같은 스레드**에서 불린다 — 안에서 CAD_* 를 부릅니다.
       콜백이 던진 예외는 엔진이 잡아 삼킨다(프레임 루프가 죽지 않게).
    """
    _cb_fn = _n.callback(CAD_CommandFn, fn, ())
    _n.keep("CAD_RegisterCommand.fn", _cb_fn, replace=False)
    return _f.CAD_RegisterCommand(_n.text(name), _n.text(title), _cb_fn, user, owner)


def CAD_UnregisterCommand(name: str | None) -> bool:
    """C: bool CAD_UnregisterCommand(const char* name)

    명령 등록 (플러그인)

    플러그인이 **콘솔 명령을 추가**한다. 명령행이 이 엔진의 모든 기능 진입점이라,
    이것만 있으면 플러그인이 "기능" 이 된다. ObjectARX 의 acedRegCmds 자리.

      등록 후  명령행에 wall → 콜백 호출
                 CAD_ExecuteCommand("wall") 도 같은 경로

    name   조회 키. 대소문자를 안 가린다(한글 이름도 된다).
    title  메뉴·툴바에 들어갈 표시 이름. NULL 이면 name 을 쓴다.
    fn     콜백. **C 함수 포인터**라 C++/C#/Python 어디서든 같은 모양으로 쓴다.
    user   그대로 돌려받는다(플러그인 인스턴스 포인터 등).
    owner  플러그인 ID. 언로드할 때 이 값으로 묶어 한꺼번에 지운다. 0 = 소유자 없음.

    실패 조건: 빈 이름 · fn 이 NULL · 이미 등록된 이름.
    ⚠️ 엔진 기본 명령(line/circle …)과 같은 이름은 등록도지만 불리지 않는다 —
       기본 명령이 먼저 조회된다(플러그인이 기본 동작을 가로채는 것을 막는다).
    ⚠️ 콜백은 **엔진과 같은 스레드**에서 불린다 — 안에서 CAD_* 를 부릅니다.
       콜백이 던진 예외는 엔진이 잡아 삼킨다(프레임 루프가 죽지 않게).
    """
    return _f.CAD_UnregisterCommand(_n.text(name))


def CAD_UnregisterCommandsByOwner(owner: int) -> int:
    """C: unsigned int CAD_UnregisterCommandsByOwner(unsigned int owner)

    그 플러그인이 등록한 명령을 전부 제거. 반환 = 지운 개수. owner 0 은 아무것도 안 지운다.
    언로드 경로에서 반드시 부른다 — 안 지우면 사라진 DLL 의 함수를 부르게 된다.
    """
    return _f.CAD_UnregisterCommandsByOwner(owner)


def CAD_GetRegisteredCommandCount() -> int:
    """C: unsigned int CAD_GetRegisteredCommandCount(void)

    등록된 명령 수 / i 번째 이름·표시이름 — 메뉴·리본을 그릴 때 호스트가 읽는다.
    buf 가 NULL 이거나 짧으면 필요한 길이(널문자 포함)를 반환한다.
    """
    return _f.CAD_GetRegisteredCommandCount()


def CAD_GetRegisteredCommandName(index: int) -> str | None:
    """C: int CAD_GetRegisteredCommandName(unsigned int index, char* buf, int bufLen)

    등록된 명령 수 / i 번째 이름·표시이름 — 메뉴·리본을 그릴 때 호스트가 읽는다.
    buf 가 NULL 이거나 짧으면 필요한 길이(널문자 포함)를 반환한다.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetRegisteredCommandName(index, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetRegisteredCommandTitle(index: int) -> str | None:
    """C: int CAD_GetRegisteredCommandTitle(unsigned int index, char* buf, int bufLen)

    등록된 명령 수 / i 번째 이름·표시이름 — 메뉴·리본을 그릴 때 호스트가 읽는다.
    buf 가 NULL 이거나 짧으면 필요한 길이(널문자 포함)를 반환한다.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetRegisteredCommandTitle(index, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_RequestStartExtrude() -> None:
    """C: void CAD_RequestStartExtrude(void)
    """
    _f.CAD_RequestStartExtrude()


def CAD_RequestStartArcSketch() -> None:
    """C: void CAD_RequestStartArcSketch(void)
    """
    _f.CAD_RequestStartArcSketch()


def CAD_RequestCycleArcMode() -> None:
    """C: void CAD_RequestCycleArcMode(void)
    """
    _f.CAD_RequestCycleArcMode()


def CAD_RequestStartPolylineSketch() -> None:
    """C: void CAD_RequestStartPolylineSketch(void)
    """
    _f.CAD_RequestStartPolylineSketch()


def CAD_RequestOpenFileDialog() -> None:
    """C: void CAD_RequestOpenFileDialog(void)
    """
    _f.CAD_RequestOpenFileDialog()


def CAD_RequestSelectAll() -> None:
    """C: void CAD_RequestSelectAll(void)
    """
    _f.CAD_RequestSelectAll()


def CAD_RequestDeleteSelected() -> None:
    """C: void CAD_RequestDeleteSelected(void)
    """
    _f.CAD_RequestDeleteSelected()


def CAD_RequestClearAll() -> None:
    """C: void CAD_RequestClearAll(void)
    """
    _f.CAD_RequestClearAll()


def CAD_RequestAddCube() -> None:
    """C: void CAD_RequestAddCube(void)
    """
    _f.CAD_RequestAddCube()


def CAD_RequestStartLightPlacement() -> None:
    """C: void CAD_RequestStartLightPlacement(void)
    """
    _f.CAD_RequestStartLightPlacement()


def CAD_RequestCycleMaterial() -> None:
    """C: void CAD_RequestCycleMaterial(void)
    """
    _f.CAD_RequestCycleMaterial()


def CAD_RequestRemoveMaterial() -> None:
    """C: void CAD_RequestRemoveMaterial(void)
    """
    _f.CAD_RequestRemoveMaterial()


def CAD_JigBegin(mode: int, ids: Sequence | None, count: int, px: float, py: float, pz: float) -> bool:
    """C: bool CAD_JigBegin(int mode, const uint32_t* ids, int count, float px, float py, float pz)

    객체 id 를 물려 시작하면 그 객체가 **커서를 따라다니고**, 좌클릭에 그 자리로 확정된다
    (undo 1스텝). ESC 로 원복. OSnap·직교 트랙킹(F8)·콘솔 값 입력이 그대로 적용된다.
    mode: 0=이동 1=회전 2=축척 3=복사
    회전/축척은 (px,py,pz) 가 피벗. 이동/복사는 무시하고 선택 전체의 시각 중심을 기준점으로 잡는다.
    반환 false = 유효한 객체가 없어 시작 못 함.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_JigBegin(mode, _a_ids, count, px, py, pz)


def CAD_JigBeginOne(mode: int, id: int, px: float, py: float, pz: float) -> bool:
    """C: bool CAD_JigBeginOne(int mode, uint32_t id, float px, float py, float pz)

    객체 id 를 물려 시작하면 그 객체가 **커서를 따라다니고**, 좌클릭에 그 자리로 확정된다
    (undo 1스텝). ESC 로 원복. OSnap·직교 트랙킹(F8)·콘솔 값 입력이 그대로 적용된다.
    mode: 0=이동 1=회전 2=축척 3=복사
    회전/축척은 (px,py,pz) 가 피벗. 이동/복사는 무시하고 선택 전체의 시각 중심을 기준점으로 잡는다.
    반환 false = 유효한 객체가 없어 시작 못 함.
    """
    return _f.CAD_JigBeginOne(mode, id, px, py, pz)


def CAD_JigState() -> int:
    """C: int CAD_JigState(void)

    상태 폴링 — 0=비활성 1=끌는 중 2=직전 확정됨 3=직전 취소됨 (2/3 은 1회만 반환).
    """
    return _f.CAD_JigState()


def CAD_JigCancel() -> None:
    """C: void CAD_JigCancel(void)

    상태 폴링 — 0=비활성 1=끌는 중 2=직전 확정됨 3=직전 취소됨 (2/3 은 1회만 반환).
    """
    _f.CAD_JigCancel()


def CAD_JigMoveTo(x: float, y: float, z: float) -> bool:
    """C: bool CAD_JigMoveTo(float x, float y, float z)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    return _f.CAD_JigMoveTo(x, y, z)


def CAD_JigCommit() -> bool:
    """C: bool CAD_JigCommit(void)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    return _f.CAD_JigCommit()


def CAD_JigSetBasePoint(x: float, y: float, z: float) -> bool:
    """C: bool CAD_JigSetBasePoint(float x, float y, float z)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    return _f.CAD_JigSetBasePoint(x, y, z)


def CAD_JigGetDelta() -> tuple[float, float, float, float, float] | None:
    """C: bool CAD_JigGetDelta(float* dx, float* dy, float* dz, float* angleDeg, float* scale)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    dx = _c.c_float()
    dy = _c.c_float()
    dz = _c.c_float()
    angleDeg = _c.c_float()
    scale = _c.c_float()
    if not _f.CAD_JigGetDelta(_c.byref(dx), _c.byref(dy), _c.byref(dz), _c.byref(angleDeg), _c.byref(scale)):
        return None
    return (dx.value, dy.value, dz.value, angleDeg.value, scale.value)


def CAD_JigBeginVariants(mode: int, ids: Sequence | None, count: int, px: float, py: float, pz: float) -> bool:
    """C: bool CAD_JigBeginVariants(int mode, const uint32_t* ids, int count, float px, float py, float pz)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_JigBeginVariants(mode, _a_ids, count, px, py, pz)


def CAD_JigNextVariant() -> bool:
    """C: bool CAD_JigNextVariant(void)

    Tab 과 동일 (호스트 버튼으로 전환할 때)

    묶음 주석: 후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    return _f.CAD_JigNextVariant()


def CAD_JigVariantIndex() -> int:
    """C: int CAD_JigVariantIndex(void)

    현재 후보 번호, -1 = 변형 Jig 아님

    묶음 주석: 후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    return _f.CAD_JigVariantIndex()


def CAD_JigVariantId() -> int:
    """C: uint32_t CAD_JigVariantId(void)

    지금 끌고 있는 후보 id (없으면 0)

    묶음 주석: 후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    return _f.CAD_JigVariantId()


def CAD_BeginTextEdit(id: int) -> bool:
    """C: bool CAD_BeginTextEdit(uint32_t id)
    """
    return _f.CAD_BeginTextEdit(id)


def CAD_IsTextEditing() -> bool:
    """C: bool CAD_IsTextEditing(void)
    """
    return _f.CAD_IsTextEditing()


def CAD_TextEditInsert(utf8: str | None) -> None:
    """C: void CAD_TextEditInsert(const char* utf8)

    커서 위치에 삽입(여러 글자 가능)
    """
    _f.CAD_TextEditInsert(_n.text(utf8))


def CAD_TextEditBackspace() -> None:
    """C: void CAD_TextEditBackspace(void)
    """
    _f.CAD_TextEditBackspace()


def CAD_TextEditDelete() -> None:
    """C: void CAD_TextEditDelete(void)
    """
    _f.CAD_TextEditDelete()


def CAD_TextEditMoveCaret(delta: int) -> None:
    """C: void CAD_TextEditMoveCaret(int delta)

    -1/+1 등
    """
    _f.CAD_TextEditMoveCaret(delta)


def CAD_TextEditCommit() -> None:
    """C: void CAD_TextEditCommit(void)

    undo 적재 + 종료
    """
    _f.CAD_TextEditCommit()


def CAD_TextEditCancel() -> None:
    """C: void CAD_TextEditCancel(void)

    원복 + 종료
    """
    _f.CAD_TextEditCancel()


def CAD_GetSelectionContext() -> str | None:
    """C: int CAD_GetSelectionContext(char* outUtf8, int cap)

    선택 문맥 JSON — 사람이 화면에서 고른 것. AI 요청마다 자동으로 붙는 것과 같은 문자열.
    {"mode":"object|face|edge","view":"top|…","count":N,"objects":[CAD_GetObjectJson 과 같은 객체…],"more":n,
     "face":{"id","normal","center","area","triangles"},"edge":{"id","a","b","length"}}  반환=길이, 실패 -1.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetSelectionContext(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_SelectObject(id: int, additive: bool) -> bool:
    """C: bool CAD_SelectObject(uint32_t id, bool additive)
    """
    return _f.CAD_SelectObject(id, additive)


def CAD_ClearSelection() -> None:
    """C: void CAD_ClearSelection(void)
    """
    _f.CAD_ClearSelection()


def CAD_SetOSnapEnabled(on: bool) -> bool:
    """C: bool CAD_SetOSnapEnabled(bool on)

    모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처)
    """
    return _f.CAD_SetOSnapEnabled(on)


def CAD_GetOSnapEnabled() -> bool:
    """C: bool CAD_GetOSnapEnabled(void)

    모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처)
    """
    return _f.CAD_GetOSnapEnabled()


def CAD_SetOSnapModes(mask: int) -> bool:
    """C: bool CAD_SetOSnapModes(uint32_t mask)

    모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처)
    """
    return _f.CAD_SetOSnapModes(mask)


def CAD_GetOSnapModes() -> int:
    """C: uint32_t CAD_GetOSnapModes(void)

    모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처)
    """
    return _f.CAD_GetOSnapModes()


def CAD_SetOrthoEnabled(on: bool) -> None:
    """C: void CAD_SetOrthoEnabled(bool on)

    모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처)
    """
    _f.CAD_SetOrthoEnabled(on)


def CAD_GetOrthoEnabled() -> bool:
    """C: bool CAD_GetOrthoEnabled(void)

    모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처)
    """
    return _f.CAD_GetOrthoEnabled()


def CAD_SetPolarTracking(on: bool, incrementDeg: float) -> bool:
    """C: bool CAD_SetPolarTracking(bool on, float incrementDeg)

    incrementDeg <= 0 = 지금 값 유지(기본 45°, 1~90)

    묶음 주석: 모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처)
    """
    return _f.CAD_SetPolarTracking(on, incrementDeg)


def CAD_GetPolarTracking() -> float | None:
    """C: bool CAD_GetPolarTracking(float* incrementDeg)

    켜짐 여부, incrementDeg NULL 가능

    묶음 주석: 모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처)
    """
    incrementDeg = _c.c_float()
    if not _f.CAD_GetPolarTracking(_c.byref(incrementDeg)):
        return None
    return incrementDeg.value


def CAD_SnapNearPoint(point: CAD_GeVec3, radius: float, modes: int, opt: CAD_OsnapOptions | None = None, **fields) -> tuple[int, CAD_OsnapPoint]:
    """C: CAD_Status CAD_SnapNearPoint(CAD_GeVec3 point, double radius, uint32_t modes, const CAD_OsnapOptions* opt, CAD_OsnapPoint* outPoint)

    장면에서 point 의 반경 radius(mm) 안 가장 가까운 스냅점 — 화면·커서 없이(AI·스크립트가 "이 근처 끝점" 을 잡을 때).
    modes = CAD_OSNAP_* 합(상태바 설정과 무관), 보이는 객체만, 근처(NEA)는 다른 스냅이 없을 때만(오토캐드처럼).
    opt 의 직전 점은 수직·접선에 쓴다(고른 점은 point). 새 규칙: 찾으면 CAD_OK + outPoint(id = 그 객체),
    없으면 CAD_E_NOT_ON_CURVE. 엔진 스레드에서만
    """
    if opt is None and fields:
        opt = CAD_OsnapOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_OsnapOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outPoint = CAD_OsnapPoint()
    _r = _f.CAD_SnapNearPoint(point, radius, modes, _p_opt, _c.byref(outPoint))
    return (_r, outPoint)


def CAD_GetSelectedCount() -> int:
    """C: uint32_t CAD_GetSelectedCount(void)
    """
    return _f.CAD_GetSelectedCount()


def CAD_GetSelectedObjectId(index: int) -> int | None:
    """C: bool CAD_GetSelectedObjectId(uint32_t index, uint32_t* id)
    """
    id = _c.c_uint32()
    if not _f.CAD_GetSelectedObjectId(index, _c.byref(id)):
        return None
    return id.value


def CAD_BeginGetPoint(prompt: str | None) -> None:
    """C: void CAD_BeginGetPoint(const char* prompt)

    비동기: Begin 후 사용자가 클릭할 때까지 대기. 호스트가 매 프레임 bool 폴링.
    IsPicking=true            → 대기 중
    IsPicking=false + Try=true  → 완료 (좌표/엔티티 소비)
    IsPicking=false + Try=false → 취소(ESC)
    EntSel 은 빈 곳/비객체 클릭을 통과 안 시킴(유효 객체만 완료). Point 는 어디든 좌표 반환.
    옛 함수 — 새 코드는 CAD_EdGetPoint · CAD_EdEntSel(아래 「명령행 입력 받기」, 2단계에서 정리). 속은 같은 길이라
    안내가 명령행에 늘 보이고 좌표("x,y")도 받는다. 다른 명령이 진행 중이면 그것을 끄고 시작한다(예전 그대로).
    """
    _f.CAD_BeginGetPoint(_n.text(prompt))


def CAD_BeginGetEntSel(prompt: str | None) -> None:
    """C: void CAD_BeginGetEntSel(const char* prompt)

    비동기: Begin 후 사용자가 클릭할 때까지 대기. 호스트가 매 프레임 bool 폴링.
    IsPicking=true            → 대기 중
    IsPicking=false + Try=true  → 완료 (좌표/엔티티 소비)
    IsPicking=false + Try=false → 취소(ESC)
    EntSel 은 빈 곳/비객체 클릭을 통과 안 시킴(유효 객체만 완료). Point 는 어디든 좌표 반환.
    옛 함수 — 새 코드는 CAD_EdGetPoint · CAD_EdEntSel(아래 「명령행 입력 받기」, 2단계에서 정리). 속은 같은 길이라
    안내가 명령행에 늘 보이고 좌표("x,y")도 받는다. 다른 명령이 진행 중이면 그것을 끄고 시작한다(예전 그대로).
    """
    _f.CAD_BeginGetEntSel(_n.text(prompt))


def CAD_IsPicking() -> bool:
    """C: bool CAD_IsPicking(void)

    비동기: Begin 후 사용자가 클릭할 때까지 대기. 호스트가 매 프레임 bool 폴링.
    IsPicking=true            → 대기 중
    IsPicking=false + Try=true  → 완료 (좌표/엔티티 소비)
    IsPicking=false + Try=false → 취소(ESC)
    EntSel 은 빈 곳/비객체 클릭을 통과 안 시킴(유효 객체만 완료). Point 는 어디든 좌표 반환.
    옛 함수 — 새 코드는 CAD_EdGetPoint · CAD_EdEntSel(아래 「명령행 입력 받기」, 2단계에서 정리). 속은 같은 길이라
    안내가 명령행에 늘 보이고 좌표("x,y")도 받는다. 다른 명령이 진행 중이면 그것을 끄고 시작한다(예전 그대로).
    """
    return _f.CAD_IsPicking()


def CAD_TryGetPickResult() -> tuple[float, float, float, int] | None:
    """C: bool CAD_TryGetPickResult(float* x, float* y, float* z, uint32_t* outId)

    완료됐으면 true(1회 소비) + 좌표(+EntSel 은 outId). Point 는 outId=0. 대기/취소면 false.
    """
    x = _c.c_float()
    y = _c.c_float()
    z = _c.c_float()
    outId = _c.c_uint32()
    if not _f.CAD_TryGetPickResult(_c.byref(x), _c.byref(y), _c.byref(z), _c.byref(outId)):
        return None
    return (x.value, y.value, z.value, outId.value)


def CAD_CancelPick() -> None:
    """C: void CAD_CancelPick(void)

    완료됐으면 true(1회 소비) + 좌표(+EntSel 은 outId). Point 는 outId=0. 대기/취소면 false.
    """
    _f.CAD_CancelPick()


def CAD_SetSubobjectSelectionMode(mode: int) -> bool:
    """C: bool CAD_SetSubobjectSelectionMode(int mode)

    Static mesh component selection, main thread. Mode: 0 object, 1 face, 2 edge.
    Pick ray is in world coordinates. Face output contains triangle numbers (not corners).
    GetSelectedFaceTriangles returns required count; writes up to capacity if out != NULL.
    """
    return _f.CAD_SetSubobjectSelectionMode(mode)


def CAD_GetSubobjectSelectionMode() -> int:
    """C: int CAD_GetSubobjectSelectionMode(void)

    Static mesh component selection, main thread. Mode: 0 object, 1 face, 2 edge.
    Pick ray is in world coordinates. Face output contains triangle numbers (not corners).
    GetSelectedFaceTriangles returns required count; writes up to capacity if out != NULL.
    """
    return _f.CAD_GetSubobjectSelectionMode()


def CAD_PickSubobject(ox: float, oy: float, oz: float, dx: float, dy: float, dz: float) -> bool:
    """C: bool CAD_PickSubobject(float ox, float oy, float oz, float dx, float dy, float dz)

    Static mesh component selection, main thread. Mode: 0 object, 1 face, 2 edge.
    Pick ray is in world coordinates. Face output contains triangle numbers (not corners).
    GetSelectedFaceTriangles returns required count; writes up to capacity if out != NULL.
    """
    return _f.CAD_PickSubobject(ox, oy, oz, dx, dy, dz)


def CAD_GetSubobjectSelectionId() -> int:
    """C: uint32_t CAD_GetSubobjectSelectionId(void)

    Static mesh component selection, main thread. Mode: 0 object, 1 face, 2 edge.
    Pick ray is in world coordinates. Face output contains triangle numbers (not corners).
    GetSelectedFaceTriangles returns required count; writes up to capacity if out != NULL.
    """
    return _f.CAD_GetSubobjectSelectionId()


def CAD_GetSelectedFaceTriangles(out: Any, capacity: int) -> int:
    """C: uint32_t CAD_GetSelectedFaceTriangles(uint32_t* out, uint32_t capacity)

    Static mesh component selection, main thread. Mode: 0 object, 1 face, 2 edge.
    Pick ray is in world coordinates. Face output contains triangle numbers (not corners).
    GetSelectedFaceTriangles returns required count; writes up to capacity if out != NULL.
    """
    return _f.CAD_GetSelectedFaceTriangles(out, capacity)


def CAD_GetSelectedBRepFaceId() -> int:
    """C: int32_t CAD_GetSelectedBRepFaceId(void)

    현재 선택 면이 B-Rep 면이면 안정적인 face id, 아니면 -1.
    """
    return _f.CAD_GetSelectedBRepFaceId()


def CAD_GetSelectedEdge(endpoints6: Any) -> bool:
    """C: bool CAD_GetSelectedEdge(float* endpoints6)

    endpoints6 = {ax,ay,az,bx,by,bz}, world coordinates. False if no selected edge.
    """
    return _f.CAD_GetSelectedEdge(endpoints6)


def CAD_RequestStartRevolve() -> None:
    """C: void CAD_RequestStartRevolve(void)
    """
    _f.CAD_RequestStartRevolve()


def CAD_GetStatusMessage() -> str | None:
    """C: int CAD_GetStatusMessage(char* buf, int bufLen)

    명령 프롬프트(현재 대화형 도구 안내). buf 에 UTF-8 로 복사, 반환=문자열 길이(널 제외).
    호스트가 자기 상태바에 표시하려고 매 프레임 폴링. buf/bufLen 0 이면 길이만 반환.
    """
    _need = _f.CAD_GetStatusMessage(None, 0)   # 2회 호출 규약: 길이를 물으며 한 번 실행
    if _need < 0:
        return None
    _cap = _need + 1
    _buf = _c.create_string_buffer(_cap)
    if _f.CAD_GetStatusMessage(_buf, _cap) < 0:   # 같은 인자 → 다시 실행하지 않고 결과만
        return None
    return _n.decode(_buf.value)


def CAD_GetTransientMessage() -> str | None:
    """C: int CAD_GetTransientMessage(char* buf, int bufLen)

    일회성 안내 (몇 초 뒤 스스로 사라짐). 프롬프트와 **다른 값**이다 —
    프롬프트는 "지금 뭘 해야 하는지"(상시), 이쪽은 "방금 왜 안 됐는지"(일시).
    예: "각도: 선을 클릭하세요", "선: 커서를 방향으로 옮긴 뒤 거리를 입력하세요"
    없거나 만료됐으면 빈 문자열(길이 0). 데스크톱은 ImGui 상태바가 그리지만 모바일은
    표시할 곳이 없어 이게 유일한 경로다 — 안 띄우면 클릭이 씹힌 것처럼 보인다.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetTransientMessage(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_EdGetPoint(prompt: str | None, opt: CAD_EdInputOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_EdGetPoint(const char* prompt, const CAD_EdInputOptions* opt)

    점 하나(acedGetPoint) — 클릭(객체 스냅) 또는 좌표 글. opt.hasBase 면 기준점에서 고무줄 선·직교
    """
    if opt is None and fields:
        opt = CAD_EdInputOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_EdInputOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_EdGetPoint(_n.text(prompt), _p_opt)


def CAD_EdGetCorner(prompt: str | None, base: CAD_GeVec3, opt: CAD_EdInputOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_EdGetCorner(const char* prompt, CAD_GeVec3 base, const CAD_EdInputOptions* opt)

    base 의 반대쪽 구석(acedGetCorner) — XY 사각형 미리보기. opt->base 대신 이 base
    """
    if opt is None and fields:
        opt = CAD_EdInputOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_EdInputOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_EdGetCorner(_n.text(prompt), base, _p_opt)


def CAD_EdGetDistance(prompt: str | None, opt: CAD_EdInputOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_EdGetDistance(const char* prompt, const CAD_EdInputOptions* opt)

    거리(acedGetDist) — 숫자 또는 두 점(opt.hasBase 면 기준점에서 한 점), 결과 value(mm)
    """
    if opt is None and fields:
        opt = CAD_EdInputOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_EdInputOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_EdGetDistance(_n.text(prompt), _p_opt)


def CAD_EdGetAngle(prompt: str | None, opt: CAD_EdInputOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_EdGetAngle(const char* prompt, const CAD_EdInputOptions* opt)

    각도(acedGetAngle) — 숫자(도) 또는 두 점, 결과 value = rad, XY 평면에서 +X 부터 반시계 0~2π
    """
    if opt is None and fields:
        opt = CAD_EdInputOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_EdInputOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_EdGetAngle(_n.text(prompt), _p_opt)


def CAD_EdGetInteger(prompt: str | None, opt: CAD_EdInputOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_EdGetInteger(const char* prompt, const CAD_EdInputOptions* opt)

    정수(acedGetInt) — 결과 value(정수 값), 소수는 거절하고 다시 묻는다
    """
    if opt is None and fields:
        opt = CAD_EdInputOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_EdInputOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_EdGetInteger(_n.text(prompt), _p_opt)


def CAD_EdGetReal(prompt: str | None, opt: CAD_EdInputOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_EdGetReal(const char* prompt, const CAD_EdInputOptions* opt)

    실수(acedGetReal) — 결과 value
    """
    if opt is None and fields:
        opt = CAD_EdInputOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_EdInputOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_EdGetReal(_n.text(prompt), _p_opt)


def CAD_EdGetString(prompt: str | None, opt: CAD_EdInputOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_EdGetString(const char* prompt, const CAD_EdInputOptions* opt)

    글(acedGetString) — 결과는 CAD_EdGetInputText. Space 를 띄어쓰기로 받으려면 CAD_ED_ALLOW_SPACES
    """
    if opt is None and fields:
        opt = CAD_EdInputOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_EdInputOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_EdGetString(_n.text(prompt), _p_opt)


def CAD_EdGetKeyword(prompt: str | None, opt: CAD_EdInputOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_EdGetKeyword(const char* prompt, const CAD_EdInputOptions* opt)

    키워드만(acedGetKword) — opt.keywords 필수, 결과 keywordIndex + CAD_EdGetInputText(낱말 그대로)
    """
    if opt is None and fields:
        opt = CAD_EdInputOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_EdInputOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_EdGetKeyword(_n.text(prompt), _p_opt)


def CAD_EdEntSel(prompt: str | None, opt: CAD_EdInputOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_EdEntSel(const char* prompt, const CAD_EdInputOptions* opt)

    객체 하나(acedEntSel) — 빈 곳 클릭은 다시 묻는다, 결과 id + 찍은 점
    """
    if opt is None and fields:
        opt = CAD_EdInputOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_EdInputOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_EdEntSel(_n.text(prompt), _p_opt)


def CAD_EdSSGet(prompt: str | None, opt: CAD_EdInputOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_EdSSGet(const char* prompt, const CAD_EdInputOptions* opt)

    여러 객체(acedSSGet) — 시작할 때 선택을 비운다(CAD_ED_PICKFIRST 이고 고른 것이 있으면 그것으로 바로 끝). 고르는 동안은 보통 선택
    그대로, Enter 는 하나 이상 골라야 끝난다. 끝난 뒤 고른 것은 선택으로 남는다(엔진 명령이 그대로 쓰게). 결과 CAD_EdGetInputIds
    """
    if opt is None and fields:
        opt = CAD_EdInputOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_EdInputOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_EdSSGet(_n.text(prompt), _p_opt)


def CAD_EdGetInputResult() -> tuple[int, CAD_EdInputResult]:
    """C: CAD_Status CAD_EdGetInputResult(CAD_EdInputResult* out)

    마지막 답(또는 묻는 중이면 status PENDING). 한 번도 안 물었으면 CAD_E_NOT_READY
    """
    out = CAD_EdInputResult()
    out.size = _c.sizeof(CAD_EdInputResult)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_EdGetInputResult(_c.byref(out))
    return (_r, out)


def CAD_EdGetInputText() -> str | None:
    """C: int32_t CAD_EdGetInputText(char* buf, uint32_t capacity)

    마지막 답의 글(글·키워드) — buf 에 NUL 까지 담고(모자라면 잘라서) 전체 길이(NUL 제외)
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_EdGetInputText(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_EdGetInputIds(outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_EdGetInputIds(uint32_t* outIds, uint32_t capacity)

    마지막 답의 객체들(SELECTION·ENTITY) — 칸만큼 채우고 전체 개수
    """
    return _f.CAD_EdGetInputIds(outIds, capacity)


def CAD_EdCancelInput() -> int:
    """C: CAD_Status CAD_EdCancelInput(void)

    묻는 중이면 CAD_ED_RESULT_CANCEL 로 끝낸다(onDone 도 불림). 안 묻는 중이면 아무 일 없이 CAD_OK
    """
    return _f.CAD_EdCancelInput()


def CAD_EdSelectWindow(corner1: CAD_GeVec3, corner2: CAD_GeVec3, outIds: Any, capacity: int, opt: CAD_EdSelectOptions | None = None, **fields) -> int:
    """C: int32_t CAD_EdSelectWindow(CAD_GeVec3 corner1, CAD_GeVec3 corner2, const CAD_EdSelectOptions* opt, uint32_t* outIds, uint32_t capacity)

    화면 없이 창 선택 — 두 구석(월드)을 지금 보기(활성 칸 카메라)로 화면에 옮겨 사람이 드래그한 것과 같은 판정.
    선택은 바꾸지 않는다(필요하면 CAD_SelectObject). 칸만큼 채우고 전체 개수. 구석이 카메라 뒤면 CAD_E_INVALID_ARG,
    화면에서 3px 도 안 벌어지면 CAD_E_DEGENERATE
    """
    if opt is None and fields:
        opt = CAD_EdSelectOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_EdSelectOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_EdSelectWindow(corner1, corner2, _p_opt, outIds, capacity)


def CAD_EdWorldToPixel(point: CAD_GeVec3) -> tuple[int, float, float]:
    """C: CAD_Status CAD_EdWorldToPixel(CAD_GeVec3 point, double* outX, double* outY)

    월드 ↔ 화면 좌표(acedCoordFromWorldToPixel · acedCoordFromPixelToWorld) — 활성 칸 카메라, 화면 = 창 안 좌표(CAD_OnMouseXxx 와
    같은 단위, 왼쪽 위 0,0). PixelToWorld 는 클릭이 고르는 점과 같은 작업 평면 위 점(스냅 없음). 화면이 아직 없으면 CAD_E_NOT_READY,
    점이 카메라 뒤면 CAD_E_INVALID_ARG
    """
    outX = _c.c_double()
    outY = _c.c_double()
    _r = _f.CAD_EdWorldToPixel(point, _c.byref(outX), _c.byref(outY))
    return (_r, outX.value, outY.value)


def CAD_EdPixelToWorld(x: float, y: float) -> tuple[int, CAD_GeVec3]:
    """C: CAD_Status CAD_EdPixelToWorld(double x, double y, CAD_GeVec3* outPoint)

    창 안 좌표 → 월드(acedCoordFromPixelToWorld) — 그 자리를 클릭하면 고르는 작업 평면 위 점(스냅 없음)
    """
    outPoint = CAD_GeVec3()
    _r = _f.CAD_EdPixelToWorld(x, y, _c.byref(outPoint))
    return (_r, outPoint)


def CAD_EdGetCommandState() -> tuple[int, CAD_EdCommandState]:
    """C: CAD_Status CAD_EdGetCommandState(CAD_EdCommandState* out)

    명령이 진행 중인지·묻는 중인 종류 — out->size 를 sizeof 로 채워 넘긴다
    """
    out = CAD_EdCommandState()
    out.size = _c.sizeof(CAD_EdCommandState)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_EdGetCommandState(_c.byref(out))
    return (_r, out)


def CAD_EdGetCommandName() -> str | None:
    """C: int32_t CAD_EdGetCommandName(char* buf, uint32_t capacity)

    진행 중인(끝났으면 마지막으로 실행한) 명령 이름 — 명령행에 친 첫 낱말, 소문자(CMDNAMES). 없으면 ""
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_EdGetCommandName(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)
