# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Editor 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_JIG_MOVE', 'CAD_JIG_ROTATE', 'CAD_JIG_SCALE', 'CAD_JIG_COPY', 'CAD_JIG_IDLE', 'CAD_JIG_DRAGGING', 'CAD_JIG_COMMITTED', 'CAD_JIG_CANCELLED', 'CAD_SELECT_REPLACE', 'CAD_SELECT_ADD', 'CAD_SELECT_REMOVE', 'CAD_SUBOBJECT_OBJECT', 'CAD_SUBOBJECT_FACE', 'CAD_SUBOBJECT_EDGE', 'CAD_ED_KIND_POINT', 'CAD_ED_KIND_CORNER', 'CAD_ED_KIND_DISTANCE', 'CAD_ED_KIND_ANGLE', 'CAD_ED_KIND_INTEGER', 'CAD_ED_KIND_REAL', 'CAD_ED_KIND_STRING', 'CAD_ED_KIND_KEYWORD', 'CAD_ED_KIND_ENTITY', 'CAD_ED_KIND_SELECTION', 'CAD_ED_RESULT_PENDING', 'CAD_ED_RESULT_NORMAL', 'CAD_ED_RESULT_NONE', 'CAD_ED_RESULT_KEYWORD', 'CAD_ED_RESULT_CANCEL', 'CAD_ED_NO_NULL', 'CAD_ED_NO_ZERO', 'CAD_ED_NO_NEGATIVE', 'CAD_ED_ARBITRARY', 'CAD_ED_ALLOW_SPACES', 'CAD_ED_PICKFIRST', 'CAD_ED_SINGLE', 'CAD_GetDimensionPointCount', 'CAD_GetPrompt', 'CAD_GetTransientMessage', 'CAD_ExecuteCommand', 'CAD_CancelCommand', 'CAD_RegisterCommand', 'CAD_UnregisterCommand', 'CAD_UnregisterCommandsByOwner', 'CAD_GetRegisteredCommandCount', 'CAD_GetRegisteredCommandName', 'CAD_GetRegisteredCommandTitle', 'CAD_OpenFileDialog', 'CAD_ClearAll', 'CAD_CycleMaterial', 'CAD_RemoveMaterial', 'CAD_JigBegin', 'CAD_JigBeginOne', 'CAD_JigGetState', 'CAD_JigCancel', 'CAD_JigMoveTo', 'CAD_JigCommit', 'CAD_JigSetBasePoint', 'CAD_JigGetDelta', 'CAD_JigBeginVariants', 'CAD_JigNextVariant', 'CAD_JigGetVariant', 'CAD_BeginTextEdit', 'CAD_GetTextEditId', 'CAD_TextEditInsert', 'CAD_TextEditBackspace', 'CAD_TextEditDelete', 'CAD_TextEditMoveCaret', 'CAD_TextEditCommit', 'CAD_TextEditCancel', 'CAD_GetSelectionContext', 'CAD_GetSelection', 'CAD_SetSelection', 'CAD_SetOSnapEnabled', 'CAD_GetOSnapEnabled', 'CAD_SetOSnapModes', 'CAD_GetOSnapModes', 'CAD_SetOrthoEnabled', 'CAD_GetOrthoEnabled', 'CAD_SetPolarTracking', 'CAD_GetPolarTracking', 'CAD_SnapNearPoint', 'CAD_SetSubobjectSelectionMode', 'CAD_GetSubobjectSelectionMode', 'CAD_PickSubobject', 'CAD_GetSubobjectSelection', 'CAD_GetSelectedFaceTriangles', 'CAD_EdGetPoint', 'CAD_EdGetCorner', 'CAD_EdGetDistance', 'CAD_EdGetAngle', 'CAD_EdGetInteger', 'CAD_EdGetReal', 'CAD_EdGetString', 'CAD_EdGetKeyword', 'CAD_EdEntSel', 'CAD_EdSSGet', 'CAD_EdGetInputResult', 'CAD_EdGetInputText', 'CAD_EdGetInputIds', 'CAD_EdCancelInput', 'CAD_EdSelectWindow', 'CAD_EdWorldToPixel', 'CAD_EdPixelToWorld', 'CAD_EdGetCommandState', 'CAD_EdGetCommandName']

_f = _n.native

CAD_JIG_MOVE = 0
CAD_JIG_ROTATE = 1
CAD_JIG_SCALE = 2
CAD_JIG_COPY = 3
CAD_JIG_IDLE = 0
CAD_JIG_DRAGGING = 1
CAD_JIG_COMMITTED = 2
CAD_JIG_CANCELLED = 3
CAD_SELECT_REPLACE = 0
CAD_SELECT_ADD = 1
CAD_SELECT_REMOVE = 2
CAD_SUBOBJECT_OBJECT = 0
CAD_SUBOBJECT_FACE = 1
CAD_SUBOBJECT_EDGE = 2
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

_n.bind("CAD_GetDimensionPointCount", _c.c_int32, [])
_n.bind("CAD_GetPrompt", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_GetTransientMessage", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_ExecuteCommand", _c.c_int32, [_c.c_char_p])
_n.bind("CAD_CancelCommand", _c.c_int32, [])
_n.bind("CAD_RegisterCommand", _c.c_int32, [_c.c_char_p, _c.c_char_p, CAD_CommandFn, _c.c_void_p, _c.c_uint32])
_n.bind("CAD_UnregisterCommand", _c.c_int32, [_c.c_char_p])
_n.bind("CAD_UnregisterCommandsByOwner", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_GetRegisteredCommandCount", _c.c_int32, [])
_n.bind("CAD_GetRegisteredCommandName", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_GetRegisteredCommandTitle", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_OpenFileDialog", _c.c_int32, [])
_n.bind("CAD_ClearAll", _c.c_int32, [])
_n.bind("CAD_CycleMaterial", _c.c_int32, [])
_n.bind("CAD_RemoveMaterial", _c.c_int32, [])
_n.bind("CAD_JigBegin", _c.c_int32, [_c.c_int32, _c.POINTER(_c.c_uint32), _c.c_uint32, CAD_GeVec3])
_n.bind("CAD_JigBeginOne", _c.c_int32, [_c.c_int32, _c.c_uint32, CAD_GeVec3])
_n.bind("CAD_JigGetState", _c.c_int32, [_c.POINTER(_c.c_int32)])
_n.bind("CAD_JigCancel", _c.c_int32, [])
_n.bind("CAD_JigMoveTo", _c.c_int32, [CAD_GeVec3])
_n.bind("CAD_JigCommit", _c.c_int32, [])
_n.bind("CAD_JigSetBasePoint", _c.c_int32, [CAD_GeVec3])
_n.bind("CAD_JigGetDelta", _c.c_int32, [_c.POINTER(CAD_JigDelta)])
_n.bind("CAD_JigBeginVariants", _c.c_int32, [_c.c_int32, _c.POINTER(_c.c_uint32), _c.c_uint32, CAD_GeVec3])
_n.bind("CAD_JigNextVariant", _c.c_int32, [])
_n.bind("CAD_JigGetVariant", _c.c_int32, [_c.POINTER(_c.c_int32), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_BeginTextEdit", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_GetTextEditId", _c.c_int32, [_c.POINTER(_c.c_uint32)])
_n.bind("CAD_TextEditInsert", _c.c_int32, [_c.c_char_p])
_n.bind("CAD_TextEditBackspace", _c.c_int32, [])
_n.bind("CAD_TextEditDelete", _c.c_int32, [])
_n.bind("CAD_TextEditMoveCaret", _c.c_int32, [_c.c_int32])
_n.bind("CAD_TextEditCommit", _c.c_int32, [])
_n.bind("CAD_TextEditCancel", _c.c_int32, [])
_n.bind("CAD_GetSelectionContext", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_GetSelection", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_SetSelection", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_int32])
_n.bind("CAD_SetOSnapEnabled", _c.c_int32, [_c.c_bool])
_n.bind("CAD_GetOSnapEnabled", _c.c_int32, [_c.POINTER(_c.c_bool)])
_n.bind("CAD_SetOSnapModes", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_GetOSnapModes", _c.c_int32, [_c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetOrthoEnabled", _c.c_int32, [_c.c_bool])
_n.bind("CAD_GetOrthoEnabled", _c.c_int32, [_c.POINTER(_c.c_bool)])
_n.bind("CAD_SetPolarTracking", _c.c_int32, [_c.c_bool, _c.c_double])
_n.bind("CAD_GetPolarTracking", _c.c_int32, [_c.POINTER(_c.c_bool), _c.POINTER(_c.c_double)])
_n.bind("CAD_SnapNearPoint", _c.c_int32, [CAD_GeVec3, _c.c_double, _c.c_uint32, _c.POINTER(CAD_OsnapOptions), _c.POINTER(CAD_OsnapPoint)])
_n.bind("CAD_SetSubobjectSelectionMode", _c.c_int32, [_c.c_int32])
_n.bind("CAD_GetSubobjectSelectionMode", _c.c_int32, [_c.POINTER(_c.c_int32)])
_n.bind("CAD_PickSubobject", _c.c_int32, [CAD_GeVec3, CAD_GeVec3])
_n.bind("CAD_GetSubobjectSelection", _c.c_int32, [_c.POINTER(CAD_SubobjectSelection)])
_n.bind("CAD_GetSelectedFaceTriangles", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
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
    """C: int32_t CAD_GetDimensionPointCount(void)

    진행 중인 치수 도구의 점 개수 — 치수 도구가 아니면 CAD_E_NOT_READY.
    모바일 커서 UI 의 [선택] 버튼 문구·끝 판단에 쓴다(클릭을 세면 엔진이 거부한 클릭과 어긋나니 엔진 값을 본다).
    """
    return _f.CAD_GetDimensionPointCount()


def CAD_GetPrompt() -> str | None:
    """C: int32_t CAD_GetPrompt(char* buf, uint32_t capacity)

    진행 중인 도구·묻기의 안내("첫 번째 점을 지정" 등) — 없으면 ""(길이 0). 모바일 커서 UI 가 도구 종류와 무관하게 매 틱 읽는다.
    반환 = 전체 길이(NUL 제외), 칸이 모자라면 글자 경계에서 잘라 담는다.
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


def CAD_GetTransientMessage() -> str | None:
    """C: int32_t CAD_GetTransientMessage(char* buf, uint32_t capacity)

    한동안 뜨는 안내(몇 초 뒤 스스로 사라짐) — 프롬프트(지금 뭘 할지, 상시)와 다른 값: "방금 왜 안 됐는지".
      예: "각도: 선을 클릭하세요". 없거나 지났으면 "". 데스크톱은 상태바가 그리지만 모바일은 이게 유일한 길(안 띄우면 클릭이 씹힌 듯 보인다).
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


def CAD_ExecuteCommand(text: str | None) -> int:
    """C: CAD_Status CAD_ExecuteCommand(const char* text)

    명령 실행

    엔진의 **모든 명령**을 이름으로 실행한다 — 도구 시작(line·circle·rect·arc·polygon·polyline·box·extrude·revolve·light …),
    도구 선택지(sides·arcmode), trim·offset·fillet·ocr·navmap … 200개가 넘는다. 새 명령이 생겨도 API 를 늘리지 않는다.

      CAD_ExecuteCommand("line");        // 선 도구 시작
      CAD_ExecuteCommand("2,3");         // 진행 중인 도구에 좌표·값
      CAD_ExecuteCommand(" ");           // 빈 Enter

    글은 하단 명령행에 치는 것과 **똑같다**(영문·짧은 별칭·한글, 진행 중인 도구가 있으면 값 입력) — 명령행과 같은 길.
    모르는 명령은 AI 로 보내지 않는다(자연어는 CAD_AiSubmit). 반환: CAD_OK · 모르는 명령 CAD_E_NOT_FOUND ·
    기다리는 도구가 없는데 빈 Enter CAD_E_NOT_READY · 진행 중인 도구가 받지 않는 입력(선 그리는 중 "circle" 같은 새 명령 이름) CAD_E_BUSY
    — 도구를 바꾸려면 CAD_CancelCommand 먼저.
    """
    return _f.CAD_ExecuteCommand(_n.text(text))


def CAD_CancelCommand() -> int:
    """C: CAD_Status CAD_CancelCommand(void)

    진행 중인 명령·도구·묻기(CAD_EdGetXxx)·Jig·문자 고쳐 쓰기를 **그 자리에서** 전부 끝낸다 — 사람이 ESC 를 누른 것과 같은 정리
    (끄던 것은 끌기 전으로, 미리보기는 지움), 단 객체 선택은 그대로. 진행 중인 것이 없으면 아무 일 없이 CAD_OK.
    도구 막대 버튼은 이것 다음 CAD_ExecuteCommand — 오토캐드 도구 막대 매크로 ^C^C 와 같다:
      CAD_CancelCommand(); CAD_ExecuteCommand("rect");     // 선 그리던 중이어도 사각형으로
    (CAD_ExecuteCommand 는 명령행에 친 것과 같아서, 도구가 진행 중이면 새 명령 이름을 받지 않는다.)
    명령 알림(이벤트)은 '취소됨'. 작업 스레드가 끝나야 하는 일(OCR 인식 등)이 남으면 CAD_E_BUSY. 엔진 스레드에서만
    """
    return _f.CAD_CancelCommand()


def CAD_RegisterCommand(name: str | None, title: str | None, fn: Callable | None, user: int | None, owner: int) -> int:
    """C: CAD_Status CAD_RegisterCommand(const char* name, const char* title, CAD_CommandFn fn, void* user, uint32_t owner)

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

    실패: 빈 이름·fn NULL = CAD_E_INVALID_ARG · 이미 등록된 이름·엔진 기본 명령(line/circle …)과 같은 이름 = CAD_E_DUPLICATE
      (기본 명령이 먼저 조회돼 절대 불리지 않으니 받지 않는다 — 플러그인이 기본 동작을 가로채는 것도 막는다).
    ⚠️ 콜백은 **엔진과 같은 스레드**에서 불린다 — 안에서 CAD_* 를 부른다. 던진 예외는 엔진이 잡아 삼킨다(프레임 루프가 죽지 않게).
    """
    _cb_fn = _n.callback(CAD_CommandFn, fn, ())
    _n.keep("CAD_RegisterCommand.fn", _cb_fn, replace=False)
    return _f.CAD_RegisterCommand(_n.text(name), _n.text(title), _cb_fn, user, owner)


def CAD_UnregisterCommand(name: str | None) -> int:
    """C: CAD_Status CAD_UnregisterCommand(const char* name)

    없는 이름 CAD_E_NOT_FOUND

    묶음 주석: 명령 등록 (플러그인)

    플러그인이 **콘솔 명령을 추가**한다. 명령행이 이 엔진의 모든 기능 진입점이라,
    이것만 있으면 플러그인이 "기능" 이 된다. ObjectARX 의 acedRegCmds 자리.

      등록 후  명령행에 wall → 콜백 호출
                 CAD_ExecuteCommand("wall") 도 같은 경로

    name   조회 키. 대소문자를 안 가린다(한글 이름도 된다).
    title  메뉴·툴바에 들어갈 표시 이름. NULL 이면 name 을 쓴다.
    fn     콜백. **C 함수 포인터**라 C++/C#/Python 어디서든 같은 모양으로 쓴다.
    user   그대로 돌려받는다(플러그인 인스턴스 포인터 등).
    owner  플러그인 ID. 언로드할 때 이 값으로 묶어 한꺼번에 지운다. 0 = 소유자 없음.

    실패: 빈 이름·fn NULL = CAD_E_INVALID_ARG · 이미 등록된 이름·엔진 기본 명령(line/circle …)과 같은 이름 = CAD_E_DUPLICATE
      (기본 명령이 먼저 조회돼 절대 불리지 않으니 받지 않는다 — 플러그인이 기본 동작을 가로채는 것도 막는다).
    ⚠️ 콜백은 **엔진과 같은 스레드**에서 불린다 — 안에서 CAD_* 를 부른다. 던진 예외는 엔진이 잡아 삼킨다(프레임 루프가 죽지 않게).
    """
    return _f.CAD_UnregisterCommand(_n.text(name))


def CAD_UnregisterCommandsByOwner(owner: int) -> int:
    """C: int32_t CAD_UnregisterCommandsByOwner(uint32_t owner)

    그 플러그인이 등록한 명령을 전부 지운다. 반환 = 지운 개수(owner 0 은 아무것도 안 지움).
    언로드 길에서 반드시 부른다 — 안 지우면 사라진 DLL 의 함수를 부르게 된다.
    """
    return _f.CAD_UnregisterCommandsByOwner(owner)


def CAD_GetRegisteredCommandCount() -> int:
    """C: int32_t CAD_GetRegisteredCommandCount(void)

    등록된 명령 수 · index 번째 이름·표시 이름(메뉴·리본을 그릴 때). index 범위 밖 CAD_E_OUT_OF_RANGE
    """
    return _f.CAD_GetRegisteredCommandCount()


def CAD_GetRegisteredCommandName(index: int) -> str | None:
    """C: int32_t CAD_GetRegisteredCommandName(uint32_t index, char* buf, uint32_t capacity)

    등록된 명령 수 · index 번째 이름·표시 이름(메뉴·리본을 그릴 때). index 범위 밖 CAD_E_OUT_OF_RANGE
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
    """C: int32_t CAD_GetRegisteredCommandTitle(uint32_t index, char* buf, uint32_t capacity)

    등록된 명령 수 · index 번째 이름·표시 이름(메뉴·리본을 그릴 때). index 범위 밖 CAD_E_OUT_OF_RANGE
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


def CAD_OpenFileDialog() -> int:
    """C: CAD_Status CAD_OpenFileDialog(void)

    파일 열기 창(엔진 창이 있는 호스트) · 장면 비우기 · 고른 객체 재질을 다음 것으로 · 고른 객체 재질 떼기 — 다음 틱에 한다(CAD_OK = 맡김).
    한 객체에 이름으로 재질을 주는 것은 CAD_ApplyMaterial(id, 이름)
    """
    return _f.CAD_OpenFileDialog()


def CAD_ClearAll() -> int:
    """C: CAD_Status CAD_ClearAll(void)

    파일 열기 창(엔진 창이 있는 호스트) · 장면 비우기 · 고른 객체 재질을 다음 것으로 · 고른 객체 재질 떼기 — 다음 틱에 한다(CAD_OK = 맡김).
    한 객체에 이름으로 재질을 주는 것은 CAD_ApplyMaterial(id, 이름)
    """
    return _f.CAD_ClearAll()


def CAD_CycleMaterial() -> int:
    """C: CAD_Status CAD_CycleMaterial(void)

    파일 열기 창(엔진 창이 있는 호스트) · 장면 비우기 · 고른 객체 재질을 다음 것으로 · 고른 객체 재질 떼기 — 다음 틱에 한다(CAD_OK = 맡김).
    한 객체에 이름으로 재질을 주는 것은 CAD_ApplyMaterial(id, 이름)
    """
    return _f.CAD_CycleMaterial()


def CAD_RemoveMaterial() -> int:
    """C: CAD_Status CAD_RemoveMaterial(void)

    파일 열기 창(엔진 창이 있는 호스트) · 장면 비우기 · 고른 객체 재질을 다음 것으로 · 고른 객체 재질 떼기 — 다음 틱에 한다(CAD_OK = 맡김).
    한 객체에 이름으로 재질을 주는 것은 CAD_ApplyMaterial(id, 이름)
    """
    return _f.CAD_RemoveMaterial()


def CAD_JigBegin(mode: int, ids: Sequence | None, count: int, pivot: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_JigBegin(int32_t mode, const uint32_t* ids, uint32_t count, CAD_GeVec3 pivot)
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_JigBegin(mode, _a_ids, count, pivot)


def CAD_JigBeginOne(mode: int, id: int, pivot: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_JigBeginOne(int32_t mode, uint32_t id, CAD_GeVec3 pivot)
    """
    return _f.CAD_JigBeginOne(mode, id, pivot)


def CAD_JigGetState() -> tuple[int, int]:
    """C: CAD_Status CAD_JigGetState(int32_t* outState)
    """
    outState = _c.c_int32()
    _r = _f.CAD_JigGetState(_c.byref(outState))
    return (_r, outState.value)


def CAD_JigCancel() -> int:
    """C: CAD_Status CAD_JigCancel(void)

    Jig 중이면 취소(ESC 와 같다 — 상태는 다음에 CANCELLED). Jig 중이 아니면 아무 일 없이 CAD_OK
    """
    return _f.CAD_JigCancel()


def CAD_JigMoveTo(point: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_JigMoveTo(CAD_GeVec3 point)

    코드로 끌기 — 모바일(버튼으로)·자동 시연. Jig 중이 아니면 CAD_E_NOT_READY.
      MoveTo: 커서를 월드 점으로(스냅 없음). 그 뒤 실제 마우스가 움직이면 다시 마우스를 따른다.
      Commit: 좌클릭과 같은 확정(되돌리기 1) — 상태는 다음에 COMMITTED.
      SetBasePoint: 이동·복사의 기준점, 회전·축척은 기준(pivot)을 바꾼다.
    """
    return _f.CAD_JigMoveTo(point)


def CAD_JigCommit() -> int:
    """C: CAD_Status CAD_JigCommit(void)

    코드로 끌기 — 모바일(버튼으로)·자동 시연. Jig 중이 아니면 CAD_E_NOT_READY.
      MoveTo: 커서를 월드 점으로(스냅 없음). 그 뒤 실제 마우스가 움직이면 다시 마우스를 따른다.
      Commit: 좌클릭과 같은 확정(되돌리기 1) — 상태는 다음에 COMMITTED.
      SetBasePoint: 이동·복사의 기준점, 회전·축척은 기준(pivot)을 바꾼다.
    """
    return _f.CAD_JigCommit()


def CAD_JigSetBasePoint(point: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_JigSetBasePoint(CAD_GeVec3 point)

    코드로 끌기 — 모바일(버튼으로)·자동 시연. Jig 중이 아니면 CAD_E_NOT_READY.
      MoveTo: 커서를 월드 점으로(스냅 없음). 그 뒤 실제 마우스가 움직이면 다시 마우스를 따른다.
      Commit: 좌클릭과 같은 확정(되돌리기 1) — 상태는 다음에 COMMITTED.
      SetBasePoint: 이동·복사의 기준점, 회전·축척은 기준(pivot)을 바꾼다.
    """
    return _f.CAD_JigSetBasePoint(point)


def CAD_JigGetDelta() -> tuple[int, CAD_JigDelta]:
    """C: CAD_Status CAD_JigGetDelta(CAD_JigDelta* out)
    """
    out = CAD_JigDelta()
    out.size = _c.sizeof(CAD_JigDelta)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_JigGetDelta(_c.byref(out))
    return (_r, out)


def CAD_JigBeginVariants(mode: int, ids: Sequence | None, count: int, pivot: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_JigBeginVariants(int32_t mode, const uint32_t* ids, uint32_t count, CAD_GeVec3 pivot)

    변형(variant) Jig — 끌면서 Tab 으로 **형상 자체를 바꾼다** (문 좌/우 열림·볼트 규격 등)
    후보 객체들을 미리 만들어 넘기면 첫 후보가 커서를 따라오고 Tab(또는 CAD_JigNextVariant)마다 다음 후보로 갈아 끼운다.
    쉬는 후보는 장면에서 잠시 빠져 안 보인다. 확정 = 그때 후보만 남고 나머지는 지움(AcEdJig 의 "성공할 때만 남긴다"),
    취소 = 후보 전부 지움(임시 형상). 실패는 CAD_JigBegin 과 같다
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_JigBeginVariants(mode, _a_ids, count, pivot)


def CAD_JigNextVariant() -> int:
    """C: CAD_Status CAD_JigNextVariant(void)

    다음 후보로(Tab 과 같다) — 변형 Jig 가 아니거나 후보가 하나뿐이면 CAD_E_NOT_READY
    """
    return _f.CAD_JigNextVariant()


def CAD_JigGetVariant() -> tuple[int, int, int]:
    """C: CAD_Status CAD_JigGetVariant(int32_t* outIndex, uint32_t* outId)

    지금 후보 — 번호(0부터)·id, 출력은 NULL 가능. 변형 Jig 가 아니면 CAD_E_NOT_READY
    """
    outIndex = _c.c_int32()
    outId = _c.c_uint32()
    _r = _f.CAD_JigGetVariant(_c.byref(outIndex), _c.byref(outId))
    return (_r, outIndex.value, outId.value)


def CAD_BeginTextEdit(id: int) -> int:
    """C: CAD_Status CAD_BeginTextEdit(uint32_t id)

    시작 — 커서는 글 끝. 없는 id CAD_E_BAD_HANDLE · 문자가 아닌 객체 CAD_E_NOT_SUPPORTED · 잠긴 도면층 CAD_E_LOCKED.
    다른 문자를 고치는 중이었으면 그것을 먼저 확정한다
    """
    return _f.CAD_BeginTextEdit(id)


def CAD_GetTextEditId() -> tuple[int, int]:
    """C: CAD_Status CAD_GetTextEditId(uint32_t* outId)

    고치는 중인 문자 id — 아니면 0(그래도 CAD_OK)
    """
    outId = _c.c_uint32()
    _r = _f.CAD_GetTextEditId(_c.byref(outId))
    return (_r, outId.value)


def CAD_TextEditInsert(utf8: str | None) -> int:
    """C: CAD_Status CAD_TextEditInsert(const char* utf8)

    커서 자리에 넣기(여러 글자 가능, 범위가 잡혀 있으면 덮어씀)

    묶음 주석: 고치는 중인 문자 id — 아니면 0(그래도 CAD_OK)
    """
    return _f.CAD_TextEditInsert(_n.text(utf8))


def CAD_TextEditBackspace() -> int:
    """C: CAD_Status CAD_TextEditBackspace(void)

    고치는 중인 문자 id — 아니면 0(그래도 CAD_OK)
    """
    return _f.CAD_TextEditBackspace()


def CAD_TextEditDelete() -> int:
    """C: CAD_Status CAD_TextEditDelete(void)

    고치는 중인 문자 id — 아니면 0(그래도 CAD_OK)
    """
    return _f.CAD_TextEditDelete()


def CAD_TextEditMoveCaret(delta: int) -> int:
    """C: CAD_Status CAD_TextEditMoveCaret(int32_t delta)

    글자 수만큼(−1 왼쪽 · +1 오른쪽), 끝에서 멈춤

    묶음 주석: 고치는 중인 문자 id — 아니면 0(그래도 CAD_OK)
    """
    return _f.CAD_TextEditMoveCaret(delta)


def CAD_TextEditCommit() -> int:
    """C: CAD_Status CAD_TextEditCommit(void)

    확정(바뀐 게 있으면 되돌리기 1) + 끝

    묶음 주석: 고치는 중인 문자 id — 아니면 0(그래도 CAD_OK)
    """
    return _f.CAD_TextEditCommit()


def CAD_TextEditCancel() -> int:
    """C: CAD_Status CAD_TextEditCancel(void)

    원래 글로 + 끝

    묶음 주석: 고치는 중인 문자 id — 아니면 0(그래도 CAD_OK)
    """
    return _f.CAD_TextEditCancel()


def CAD_GetSelectionContext() -> str | None:
    """C: int32_t CAD_GetSelectionContext(char* buf, uint32_t capacity)

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


def CAD_GetSelection(outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_GetSelection(uint32_t* outIds, uint32_t capacity)

    지금 선택 — 칸만큼 채우고 전체 개수(outIds = NULL 이면 개수만)
    """
    return _f.CAD_GetSelection(outIds, capacity)


def CAD_SetSelection(ids: Sequence | None, count: int, mode: int) -> int:
    """C: CAD_Status CAD_SetSelection(const uint32_t* ids, uint32_t count, int32_t mode)

    선택 바꾸기 — mode = CAD_SELECT_*(REPLACE + count 0 = 비우기). 없는 id CAD_E_BAD_HANDLE, 넣을 것이 잠긴 도면층 CAD_E_LOCKED,
    숨김·모양 없음(고를 수 없음) CAD_E_NOT_SUPPORTED — 하나라도 그러면 아무것도 안 바꾼다. 보기 상태라 되돌리기에 안 남는다
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_SetSelection(_a_ids, count, mode)


def CAD_SetOSnapEnabled(on: bool) -> int:
    """C: CAD_Status CAD_SetOSnapEnabled(bool on)

    객체 스냅·직교·극좌표 — 상태바 버튼(객체스냅·직교(F8)·극좌표(F10))과 같은 설정. 명령 osnap/ortho/polar [on|off] 과도 같다.
    모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처)
    """
    return _f.CAD_SetOSnapEnabled(on)


def CAD_GetOSnapEnabled() -> tuple[int, bool]:
    """C: CAD_Status CAD_GetOSnapEnabled(bool* outOn)

    객체 스냅·직교·극좌표 — 상태바 버튼(객체스냅·직교(F8)·극좌표(F10))과 같은 설정. 명령 osnap/ortho/polar [on|off] 과도 같다.
    모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처)
    """
    outOn = _c.c_bool()
    _r = _f.CAD_GetOSnapEnabled(_c.byref(outOn))
    return (_r, outOn.value)


def CAD_SetOSnapModes(mask: int) -> int:
    """C: CAD_Status CAD_SetOSnapModes(uint32_t mask)

    모르는 비트 CAD_E_INVALID_ARG

    묶음 주석: 객체 스냅·직교·극좌표 — 상태바 버튼(객체스냅·직교(F8)·극좌표(F10))과 같은 설정. 명령 osnap/ortho/polar [on|off] 과도 같다.
    모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처)
    """
    return _f.CAD_SetOSnapModes(mask)


def CAD_GetOSnapModes() -> tuple[int, int]:
    """C: CAD_Status CAD_GetOSnapModes(uint32_t* outMask)

    객체 스냅·직교·극좌표 — 상태바 버튼(객체스냅·직교(F8)·극좌표(F10))과 같은 설정. 명령 osnap/ortho/polar [on|off] 과도 같다.
    모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처)
    """
    outMask = _c.c_uint32()
    _r = _f.CAD_GetOSnapModes(_c.byref(outMask))
    return (_r, outMask.value)


def CAD_SetOrthoEnabled(on: bool) -> int:
    """C: CAD_Status CAD_SetOrthoEnabled(bool on)

    객체 스냅·직교·극좌표 — 상태바 버튼(객체스냅·직교(F8)·극좌표(F10))과 같은 설정. 명령 osnap/ortho/polar [on|off] 과도 같다.
    모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처)
    """
    return _f.CAD_SetOrthoEnabled(on)


def CAD_GetOrthoEnabled() -> tuple[int, bool]:
    """C: CAD_Status CAD_GetOrthoEnabled(bool* outOn)

    객체 스냅·직교·극좌표 — 상태바 버튼(객체스냅·직교(F8)·극좌표(F10))과 같은 설정. 명령 osnap/ortho/polar [on|off] 과도 같다.
    모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처)
    """
    outOn = _c.c_bool()
    _r = _f.CAD_GetOrthoEnabled(_c.byref(outOn))
    return (_r, outOn.value)


def CAD_SetPolarTracking(on: bool, increment: float) -> int:
    """C: CAD_Status CAD_SetPolarTracking(bool on, double increment)

    극좌표 추적 — increment = 각 증분(rad, 1°~90°, 0 이하 = 지금 값 그대로, 기본 45°). 범위 밖 CAD_E_OUT_OF_RANGE
    """
    return _f.CAD_SetPolarTracking(on, increment)


def CAD_GetPolarTracking() -> tuple[int, bool, float]:
    """C: CAD_Status CAD_GetPolarTracking(bool* outOn, double* outIncrement)

    출력은 NULL 가능

    묶음 주석: 극좌표 추적 — increment = 각 증분(rad, 1°~90°, 0 이하 = 지금 값 그대로, 기본 45°). 범위 밖 CAD_E_OUT_OF_RANGE
    """
    outOn = _c.c_bool()
    outIncrement = _c.c_double()
    _r = _f.CAD_GetPolarTracking(_c.byref(outOn), _c.byref(outIncrement))
    return (_r, outOn.value, outIncrement.value)


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


def CAD_SetSubobjectSelectionMode(mode: int) -> int:
    """C: CAD_Status CAD_SetSubobjectSelectionMode(int32_t mode)

    모드 바꾸기(고른 면·모서리는 비움, 면·모서리 모드면 객체 선택도 비움). 범위 밖 CAD_E_OUT_OF_RANGE ·
    도구·Jig·그립 끌기 진행 중에 면·모서리 모드로 CAD_E_BUSY
    """
    return _f.CAD_SetSubobjectSelectionMode(mode)


def CAD_GetSubobjectSelectionMode() -> tuple[int, int]:
    """C: CAD_Status CAD_GetSubobjectSelectionMode(int32_t* outMode)

    모드 바꾸기(고른 면·모서리는 비움, 면·모서리 모드면 객체 선택도 비움). 범위 밖 CAD_E_OUT_OF_RANGE ·
    도구·Jig·그립 끌기 진행 중에 면·모서리 모드로 CAD_E_BUSY
    """
    outMode = _c.c_int32()
    _r = _f.CAD_GetSubobjectSelectionMode(_c.byref(outMode))
    return (_r, outMode.value)


def CAD_PickSubobject(origin: CAD_GeVec3, direction: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_PickSubobject(CAD_GeVec3 origin, CAD_GeVec3 direction)

    광선(월드)으로 면·모서리 하나 고르기 — 화면 클릭과 같은 판정(모서리는 맞은 면의 테두리 중 화면에서 가까운 것, 10px 안).
    객체 모드면 CAD_E_NOT_READY · 방향 0 CAD_E_DEGENERATE · 맞은 것이 없으면 CAD_E_NOT_FOUND(고른 것도 비움). 숨긴 객체는 안 맞는다
    """
    return _f.CAD_PickSubobject(origin, direction)


def CAD_GetSubobjectSelection() -> tuple[int, CAD_SubobjectSelection]:
    """C: CAD_Status CAD_GetSubobjectSelection(CAD_SubobjectSelection* out)

    지금 고른 면·모서리 — 없으면 CAD_E_NOT_FOUND(객체 모드 포함)
    """
    out = CAD_SubobjectSelection()
    out.size = _c.sizeof(CAD_SubobjectSelection)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_GetSubobjectSelection(_c.byref(out))
    return (_r, out)


def CAD_GetSelectedFaceTriangles(outTriangles: Any, capacity: int) -> int:
    """C: int32_t CAD_GetSelectedFaceTriangles(uint32_t* outTriangles, uint32_t capacity)

    고른 면의 삼각형 번호(모델 인덱스 ÷ 3) — 칸만큼 채우고 전체 개수. 고른 면이 없으면 CAD_E_NOT_FOUND
    """
    return _f.CAD_GetSelectedFaceTriangles(outTriangles, capacity)


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
    선택은 바꾸지 않는다(필요하면 CAD_SetSelection). 칸만큼 채우고 전체 개수. 구석이 카메라 뒤면 CAD_E_INVALID_ARG,
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
