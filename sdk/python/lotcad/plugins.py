# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Plugins 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_RegisterCommand', 'CAD_UnregisterCommand', 'CAD_UnregisterCommandsByOwner', 'CAD_GetRegisteredCommandCount', 'CAD_GetRegisteredCommandName', 'CAD_GetRegisteredCommandTitle', 'CAD_AddUiItem', 'CAD_RemoveUiItem', 'CAD_RemoveUiItemsByOwner', 'CAD_GetUiItemCount', 'CAD_SetOverlayRibbonHeight', 'CAD_GetOverlayRibbonTop', 'CAD_GetUiItemId', 'CAD_GetUiItemKind', 'CAD_GetUiItemPath', 'CAD_GetUiItemTitle', 'CAD_GetUiItemCommand', 'CAD_GetUiItemIcon', 'CAD_AddUiControl', 'CAD_SetUiControlValue', 'CAD_GetUiControlValue', 'CAD_LoadPlugins', 'CAD_UnloadPlugin', 'CAD_GetPluginCount', 'CAD_GetPluginId', 'CAD_GetPluginName', 'CAD_CreateMesh', 'CAD_ReplaceMesh', 'CAD_SetPluginTag', 'CAD_ClearPluginTag', 'CAD_HasPluginTag', 'CAD_GetPluginTagOwner', 'CAD_GetPluginTagType', 'CAD_GetPluginTagData', 'CAD_SetOnPluginEntityLoaded', 'CAD_SetOnPluginEntityLoaded_cb', 'CAD_SetOnConfirm', 'CAD_SetOnConfirm_cb', 'CAD_AddEntityProperty', 'CAD_RemoveEntityPropertiesByOwner', 'CAD_SetOnPluginEntityChanged', 'CAD_SetOnPluginEntityChanged_cb', 'CAD_AddEventListener', 'CAD_RemoveEventListener', 'CAD_GetImGuiContext', 'CAD_GetImGuiAllocators', 'CAD_SetOnDrawPanel', 'CAD_SetOnDrawPanel_cb']

_f = _n.native

CAD_SetOnPluginEntityLoaded_cb = _c.CFUNCTYPE(None, _c.c_uint32, _c.c_char_p, _c.c_char_p, _c.c_char_p)
CAD_SetOnConfirm_cb = _c.CFUNCTYPE(_c.c_bool, _c.c_char_p)
CAD_SetOnPluginEntityChanged_cb = _c.CFUNCTYPE(None, _c.c_uint32, _c.c_char_p, _c.c_char_p, _c.c_char_p)
CAD_SetOnDrawPanel_cb = _c.CFUNCTYPE(None, _c.c_uint, _c.c_char_p)

_n.bind("CAD_RegisterCommand", _c.c_bool, [_c.c_char_p, _c.c_char_p, CAD_CommandFn, _c.c_void_p, _c.c_uint])
_n.bind("CAD_UnregisterCommand", _c.c_bool, [_c.c_char_p])
_n.bind("CAD_UnregisterCommandsByOwner", _c.c_uint, [_c.c_uint])
_n.bind("CAD_GetRegisteredCommandCount", _c.c_uint, [])
_n.bind("CAD_GetRegisteredCommandName", _c.c_int, [_c.c_uint, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetRegisteredCommandTitle", _c.c_int, [_c.c_uint, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_AddUiItem", _c.c_uint, [_c.c_int, _c.c_char_p, _c.c_char_p, _c.c_char_p, _c.c_char_p, _c.c_uint])
_n.bind("CAD_RemoveUiItem", _c.c_bool, [_c.c_uint])
_n.bind("CAD_RemoveUiItemsByOwner", _c.c_uint, [_c.c_uint])
_n.bind("CAD_GetUiItemCount", _c.c_uint, [])
_n.bind("CAD_SetOverlayRibbonHeight", None, [_c.c_float])
_n.bind("CAD_GetOverlayRibbonTop", _c.c_float, [])
_n.bind("CAD_GetUiItemId", _c.c_uint, [_c.c_uint])
_n.bind("CAD_GetUiItemKind", _c.c_int, [_c.c_uint])
_n.bind("CAD_GetUiItemPath", _c.c_int, [_c.c_uint, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetUiItemTitle", _c.c_int, [_c.c_uint, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetUiItemCommand", _c.c_int, [_c.c_uint, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetUiItemIcon", _c.c_int, [_c.c_uint, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_AddUiControl", _c.c_uint, [_c.c_int, _c.c_char_p, _c.c_char_p, _c.c_char_p, _c.c_double, _c.c_double, _c.c_double, _c.c_uint])
_n.bind("CAD_SetUiControlValue", _c.c_bool, [_c.c_uint, _c.c_double])
_n.bind("CAD_GetUiControlValue", _c.c_bool, [_c.c_uint, _c.POINTER(_c.c_double), _c.POINTER(_c.c_double), _c.POINTER(_c.c_double)])
_n.bind("CAD_LoadPlugins", _c.c_uint, [_c.c_char_p])
_n.bind("CAD_UnloadPlugin", _c.c_bool, [_c.c_uint])
_n.bind("CAD_GetPluginCount", _c.c_uint, [])
_n.bind("CAD_GetPluginId", _c.c_uint, [_c.c_uint])
_n.bind("CAD_GetPluginName", _c.c_int, [_c.c_uint, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_CreateMesh", _c.c_uint32, [_c.POINTER(_c.c_float), _c.c_uint, _c.POINTER(_c.c_uint), _c.c_uint, _c.POINTER(_c.c_float)])
_n.bind("CAD_ReplaceMesh", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.c_uint, _c.POINTER(_c.c_uint), _c.c_uint, _c.POINTER(_c.c_float)])
_n.bind("CAD_SetPluginTag", _c.c_bool, [_c.c_uint32, _c.c_char_p, _c.c_char_p, _c.c_char_p])
_n.bind("CAD_ClearPluginTag", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_HasPluginTag", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_GetPluginTagOwner", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetPluginTagType", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetPluginTagData", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_SetOnPluginEntityLoaded", None, [CAD_SetOnPluginEntityLoaded_cb])
_n.bind("CAD_SetOnConfirm", None, [CAD_SetOnConfirm_cb])
_n.bind("CAD_AddEntityProperty", _c.c_bool, [_c.c_char_p, _c.c_char_p, _c.c_char_p, _c.c_char_p, _c.c_int, _c.c_float, _c.c_float, _c.c_uint])
_n.bind("CAD_RemoveEntityPropertiesByOwner", _c.c_uint, [_c.c_uint])
_n.bind("CAD_SetOnPluginEntityChanged", None, [CAD_SetOnPluginEntityChanged_cb])
_n.bind("CAD_AddEventListener", _c.c_uint, [_c.c_int, CAD_EventFn, _c.c_void_p, _c.c_uint])
_n.bind("CAD_RemoveEventListener", _c.c_bool, [_c.c_uint])
_n.bind("CAD_GetImGuiContext", _c.c_void_p, [])
_n.bind("CAD_GetImGuiAllocators", None, [_c.POINTER(_c.c_void_p), _c.POINTER(_c.c_void_p), _c.POINTER(_c.c_void_p)])
_n.bind("CAD_SetOnDrawPanel", None, [CAD_SetOnDrawPanel_cb])


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


def CAD_AddUiItem(kind: int, path: str | None, title: str | None, command: str | None, icon: str | None, owner: int) -> int:
    """C: unsigned int CAD_AddUiItem(int kind, const char* path, const char* title, const char* command, const char* icon, unsigned int owner)

    UI 등록 (플러그인)

    플러그인은 UI 를 **직접 그리지 않는다.** (이름, 위치, 명령) 만 올리면 엔진이 그린다.
    그래서 ImGui 버전에 묶이지 않고, C#/Python 플러그인도 같은 방식을 쓰며,
    **호스트 임베드(MFC/WPF)에서도 산다** — 호스트가 이 목록을 읽어 자기 메뉴로 그리면 된다.

    kind: 0=메뉴항목 1=구분선 2=툴바버튼 3=리본버튼 4=패널
    path: 위치. 구분자는 '/'.
            메뉴 "건축" · "건축/가져오기"   툴바/리본 "건축/벽체"
            패널은 도킹 위치를 여기 넣는다("left"/"right"/"bottom").
    command: 누르면 실행할 명령 이름. 명령행과 **같은 입구**로 들어간다.
             구분선·패널은 NULL 가능. 그 외엓 비어 둘 수 없다 —
             눌러도 아무 일이 안 생기는 항목은 등록 단계에서 막는다.
    icon: 짧은 글자/이모지. 지금은 글자로 보여주고 나중에 아이콘으로 바꾼다. NULL 가능.
    owner: 플러그인 ID. 언로드 시 이 값으로 묶어 한꺼번에 지운다.

    반환 = 항목 id (0 이면 실패). 이 id 로 개별 제거한다.
    ⚠️ 패널은 **존재만** 등록된다 — 내용은 플러그인이 ImGui 후크로 그려야 하고,
       그건 단독 실행 전용이다(호스트 임베드엔 ImGui 컨텍스트가 없다).
    """
    return _f.CAD_AddUiItem(kind, _n.text(path), _n.text(title), _n.text(command), _n.text(icon), owner)


def CAD_RemoveUiItem(id: int) -> bool:
    """C: bool CAD_RemoveUiItem(unsigned int id)

    UI 등록 (플러그인)

    플러그인은 UI 를 **직접 그리지 않는다.** (이름, 위치, 명령) 만 올리면 엔진이 그린다.
    그래서 ImGui 버전에 묶이지 않고, C#/Python 플러그인도 같은 방식을 쓰며,
    **호스트 임베드(MFC/WPF)에서도 산다** — 호스트가 이 목록을 읽어 자기 메뉴로 그리면 된다.

    kind: 0=메뉴항목 1=구분선 2=툴바버튼 3=리본버튼 4=패널
    path: 위치. 구분자는 '/'.
            메뉴 "건축" · "건축/가져오기"   툴바/리본 "건축/벽체"
            패널은 도킹 위치를 여기 넣는다("left"/"right"/"bottom").
    command: 누르면 실행할 명령 이름. 명령행과 **같은 입구**로 들어간다.
             구분선·패널은 NULL 가능. 그 외엓 비어 둘 수 없다 —
             눌러도 아무 일이 안 생기는 항목은 등록 단계에서 막는다.
    icon: 짧은 글자/이모지. 지금은 글자로 보여주고 나중에 아이콘으로 바꾼다. NULL 가능.
    owner: 플러그인 ID. 언로드 시 이 값으로 묶어 한꺼번에 지운다.

    반환 = 항목 id (0 이면 실패). 이 id 로 개별 제거한다.
    ⚠️ 패널은 **존재만** 등록된다 — 내용은 플러그인이 ImGui 후크로 그려야 하고,
       그건 단독 실행 전용이다(호스트 임베드엔 ImGui 컨텍스트가 없다).
    """
    return _f.CAD_RemoveUiItem(id)


def CAD_RemoveUiItemsByOwner(owner: int) -> int:
    """C: unsigned int CAD_RemoveUiItemsByOwner(unsigned int owner)

    UI 등록 (플러그인)

    플러그인은 UI 를 **직접 그리지 않는다.** (이름, 위치, 명령) 만 올리면 엔진이 그린다.
    그래서 ImGui 버전에 묶이지 않고, C#/Python 플러그인도 같은 방식을 쓰며,
    **호스트 임베드(MFC/WPF)에서도 산다** — 호스트가 이 목록을 읽어 자기 메뉴로 그리면 된다.

    kind: 0=메뉴항목 1=구분선 2=툴바버튼 3=리본버튼 4=패널
    path: 위치. 구분자는 '/'.
            메뉴 "건축" · "건축/가져오기"   툴바/리본 "건축/벽체"
            패널은 도킹 위치를 여기 넣는다("left"/"right"/"bottom").
    command: 누르면 실행할 명령 이름. 명령행과 **같은 입구**로 들어간다.
             구분선·패널은 NULL 가능. 그 외엓 비어 둘 수 없다 —
             눌러도 아무 일이 안 생기는 항목은 등록 단계에서 막는다.
    icon: 짧은 글자/이모지. 지금은 글자로 보여주고 나중에 아이콘으로 바꾼다. NULL 가능.
    owner: 플러그인 ID. 언로드 시 이 값으로 묶어 한꺼번에 지운다.

    반환 = 항목 id (0 이면 실패). 이 id 로 개별 제거한다.
    ⚠️ 패널은 **존재만** 등록된다 — 내용은 플러그인이 ImGui 후크로 그려야 하고,
       그건 단독 실행 전용이다(호스트 임베드엔 ImGui 컨텍스트가 없다).
    """
    return _f.CAD_RemoveUiItemsByOwner(owner)


def CAD_GetUiItemCount() -> int:
    """C: unsigned int CAD_GetUiItemCount(void)

    호스트가 메뉴·툴바를 직접 그릴 때 읽는다. index 는 등록 순서 = 화면 나열 순서.
    """
    return _f.CAD_GetUiItemCount()


def CAD_SetOverlayRibbonHeight(logicalHeight: float) -> None:
    """C: void CAD_SetOverlayRibbonHeight(float logicalHeight)

    Positive height reserves the built-in ribbon region for an external overlay.
    Zero restores the original ImGui ribbon and plugin ribbon.
    """
    _f.CAD_SetOverlayRibbonHeight(logicalHeight)


def CAD_GetOverlayRibbonTop() -> float:
    """C: float CAD_GetOverlayRibbonTop(void)

    Logical Y coordinate immediately below the host menu bar.
    """
    return _f.CAD_GetOverlayRibbonTop()


def CAD_GetUiItemId(index: int) -> int:
    """C: unsigned int CAD_GetUiItemId(unsigned int index)

    Logical Y coordinate immediately below the host menu bar.
    """
    return _f.CAD_GetUiItemId(index)


def CAD_GetUiItemKind(index: int) -> int:
    """C: int CAD_GetUiItemKind(unsigned int index)

    Logical Y coordinate immediately below the host menu bar.
    """
    return _f.CAD_GetUiItemKind(index)


def CAD_GetUiItemPath(index: int) -> str | None:
    """C: int CAD_GetUiItemPath(unsigned int index, char* buf, int bufLen)

    Logical Y coordinate immediately below the host menu bar.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetUiItemPath(index, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetUiItemTitle(index: int) -> str | None:
    """C: int CAD_GetUiItemTitle(unsigned int index, char* buf, int bufLen)

    Logical Y coordinate immediately below the host menu bar.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetUiItemTitle(index, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetUiItemCommand(index: int) -> str | None:
    """C: int CAD_GetUiItemCommand(unsigned int index, char* buf, int bufLen)

    Logical Y coordinate immediately below the host menu bar.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetUiItemCommand(index, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetUiItemIcon(index: int) -> str | None:
    """C: int CAD_GetUiItemIcon(unsigned int index, char* buf, int bufLen)

    Logical Y coordinate immediately below the host menu bar.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetUiItemIcon(index, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_AddUiControl(kind: int, path: str | None, title: str | None, command: str | None, minimum: float, maximum: float, value: float, owner: int) -> int:
    """C: unsigned int CAD_AddUiControl(int kind, const char* path, const char* title, const char* command, double minimum, double maximum, double value, unsigned int owner)

    LotUI ribbon controls owned by the host, not by a plugin DLL.
    kind: 5=checkbox, 6=slider. path is "tab/group". command runs after a
    user change; the command callback reads the new value by item id.
    A checkbox uses 0/1; its range arguments are ignored. A slider requires
    finite minimum < maximum and clamps the initial/current value.
    Plugins must remove their items and commands on unload.
    """
    return _f.CAD_AddUiControl(kind, _n.text(path), _n.text(title), _n.text(command), minimum, maximum, value, owner)


def CAD_SetUiControlValue(id: int, value: float) -> bool:
    """C: bool CAD_SetUiControlValue(unsigned int id, double value)

    LotUI ribbon controls owned by the host, not by a plugin DLL.
    kind: 5=checkbox, 6=slider. path is "tab/group". command runs after a
    user change; the command callback reads the new value by item id.
    A checkbox uses 0/1; its range arguments are ignored. A slider requires
    finite minimum < maximum and clamps the initial/current value.
    Plugins must remove their items and commands on unload.
    """
    return _f.CAD_SetUiControlValue(id, value)


def CAD_GetUiControlValue(id: int) -> tuple[float, float, float] | None:
    """C: bool CAD_GetUiControlValue(unsigned int id, double* value, double* minimum, double* maximum)

    LotUI ribbon controls owned by the host, not by a plugin DLL.
    kind: 5=checkbox, 6=slider. path is "tab/group". command runs after a
    user change; the command callback reads the new value by item id.
    A checkbox uses 0/1; its range arguments are ignored. A slider requires
    finite minimum < maximum and clamps the initial/current value.
    Plugins must remove their items and commands on unload.
    """
    value = _c.c_double()
    minimum = _c.c_double()
    maximum = _c.c_double()
    if not _f.CAD_GetUiControlValue(id, _c.byref(value), _c.byref(minimum), _c.byref(maximum)):
        return None
    return (value.value, minimum.value, maximum.value)


def CAD_LoadPlugins(dir: str | None) -> int:
    """C: unsigned int CAD_LoadPlugins(const char* dir)

    플러그인 로더

    엔진은 시작할 때 플러그인을 붙이지 않는다(2026-10-11부터). 필요하면 호스트가 CAD_LoadPlugins("plugins") 처럼 부르고,
    앱 사용자는 명령 `pload all`(실행 폴더·사용자 설정 폴더의 plugins/) · `punload all` 로 붙이고 내린다.

    플러그인은 plugin/lot_plugin_sdk.h 의 심볼 셋을 내보내야 한다:
      CAD_PluginAbiVersion / CAD_PluginLoad / CAD_PluginUnload
    ABI 번호가 다르면 아예 올리지 않는다 — 엔진과 같은 컴파일러·런타임으로 빌드해야 한다.

    언로드하면 그 플러그인이 올린 명령과 UI 항목이 **엔진이 알아서** 같이 지워진다.
    """
    return _f.CAD_LoadPlugins(_n.text(dir))


def CAD_UnloadPlugin(id: int) -> bool:
    """C: bool CAD_UnloadPlugin(unsigned int id)

    플러그인 로더

    엔진은 시작할 때 플러그인을 붙이지 않는다(2026-10-11부터). 필요하면 호스트가 CAD_LoadPlugins("plugins") 처럼 부르고,
    앱 사용자는 명령 `pload all`(실행 폴더·사용자 설정 폴더의 plugins/) · `punload all` 로 붙이고 내린다.

    플러그인은 plugin/lot_plugin_sdk.h 의 심볼 셋을 내보내야 한다:
      CAD_PluginAbiVersion / CAD_PluginLoad / CAD_PluginUnload
    ABI 번호가 다르면 아예 올리지 않는다 — 엔진과 같은 컴파일러·런타임으로 빌드해야 한다.

    언로드하면 그 플러그인이 올린 명령과 UI 항목이 **엔진이 알아서** 같이 지워진다.
    """
    return _f.CAD_UnloadPlugin(id)


def CAD_GetPluginCount() -> int:
    """C: unsigned int CAD_GetPluginCount(void)

    플러그인 로더

    엔진은 시작할 때 플러그인을 붙이지 않는다(2026-10-11부터). 필요하면 호스트가 CAD_LoadPlugins("plugins") 처럼 부르고,
    앱 사용자는 명령 `pload all`(실행 폴더·사용자 설정 폴더의 plugins/) · `punload all` 로 붙이고 내린다.

    플러그인은 plugin/lot_plugin_sdk.h 의 심볼 셋을 내보내야 한다:
      CAD_PluginAbiVersion / CAD_PluginLoad / CAD_PluginUnload
    ABI 번호가 다르면 아예 올리지 않는다 — 엔진과 같은 컴파일러·런타임으로 빌드해야 한다.

    언로드하면 그 플러그인이 올린 명령과 UI 항목이 **엔진이 알아서** 같이 지워진다.
    """
    return _f.CAD_GetPluginCount()


def CAD_GetPluginId(index: int) -> int:
    """C: unsigned int CAD_GetPluginId(unsigned int index)

    플러그인 로더

    엔진은 시작할 때 플러그인을 붙이지 않는다(2026-10-11부터). 필요하면 호스트가 CAD_LoadPlugins("plugins") 처럼 부르고,
    앱 사용자는 명령 `pload all`(실행 폴더·사용자 설정 폴더의 plugins/) · `punload all` 로 붙이고 내린다.

    플러그인은 plugin/lot_plugin_sdk.h 의 심볼 셋을 내보내야 한다:
      CAD_PluginAbiVersion / CAD_PluginLoad / CAD_PluginUnload
    ABI 번호가 다르면 아예 올리지 않는다 — 엔진과 같은 컴파일러·런타임으로 빌드해야 한다.

    언로드하면 그 플러그인이 올린 명령과 UI 항목이 **엔진이 알아서** 같이 지워진다.
    """
    return _f.CAD_GetPluginId(index)


def CAD_GetPluginName(index: int) -> str | None:
    """C: int CAD_GetPluginName(unsigned int index, char* buf, int bufLen)

    플러그인 로더

    엔진은 시작할 때 플러그인을 붙이지 않는다(2026-10-11부터). 필요하면 호스트가 CAD_LoadPlugins("plugins") 처럼 부르고,
    앱 사용자는 명령 `pload all`(실행 폴더·사용자 설정 폴더의 plugins/) · `punload all` 로 붙이고 내린다.

    플러그인은 plugin/lot_plugin_sdk.h 의 심볼 셋을 내보내야 한다:
      CAD_PluginAbiVersion / CAD_PluginLoad / CAD_PluginUnload
    ABI 번호가 다르면 아예 올리지 않는다 — 엔진과 같은 컴파일러·런타임으로 빌드해야 한다.

    언로드하면 그 플러그인이 올린 명령과 UI 항목이 **엔진이 알아서** 같이 지워진다.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetPluginName(index, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_CreateMesh(xyz: Sequence | None, vertexCount: int, indices: Sequence | None, indexCount: int, normals: Sequence | None) -> int:
    """C: uint32_t CAD_CreateMesh(const float* xyz, unsigned int vertexCount, const unsigned int* indices, unsigned int indexCount, const float* normals)

    플러그인 엔티티

    새 객체 종류를 만들지 않는다. 플러그인이 **형상(메시)을 공급**하고, 객체에 **딱지**를 붙인다.
    객체는 평범한 메시라 그리기·픽킹·저장이 전부 그대로 동작하고, 플러그인이 없는 곳에서
    열어도 형상은 보인다. 딱지는 보존돼 나중에 플러그인이 있으면 도로 살아난다.

      id = CAD_CreateMesh(xyz, nv, idx, ni, NULL);          // 형상
      CAD_SetPluginTag(id, "ArchBuilder", "wall", json);   // 딱지
      ... 값이 바뀌면 → CAD_ReplaceMesh(id, ...)           // 재생성

    .lot 을 열어 딱지 붙은 객체가 복원되면 CAD_SetOnPluginEntityLoaded 콜백으로 알려준다.
    플러그인은 owner 가 자기 이름이면 data 를 읽어 살아 있는 엔티티로 넘겨받는다.

    사용자가 그립·불리언·밀당·분해로 메시를 직접 고치면 정의와 형상이 어긋나므로 엔진이
    먼저 묻고, "계속" 이면 딱지를 뗀다(그냥 메시가 된다). 호스트 임베드는 ImGui 가 없어
    CAD_SetOnConfirm 으로 대신 물어야 한다 — 안 달면 안전한 쪽(취소)으로 간다.

    xyz = 3*vertexCount, indices = 3*triangleCount. normals 는 NULL 가능(삼각형별 flat).
    """
    _a_xyz = _n.array(_c.c_float, xyz)
    _a_indices = _n.array(_c.c_uint, indices)
    _a_normals = _n.array(_c.c_float, normals)
    return _f.CAD_CreateMesh(_a_xyz, vertexCount, _a_indices, indexCount, _a_normals)


def CAD_ReplaceMesh(id: int, xyz: Sequence | None, vertexCount: int, indices: Sequence | None, indexCount: int, normals: Sequence | None) -> bool:
    """C: bool CAD_ReplaceMesh(uint32_t id, const float* xyz, unsigned int vertexCount, const unsigned int* indices, unsigned int indexCount, const float* normals)

    플러그인 엔티티

    새 객체 종류를 만들지 않는다. 플러그인이 **형상(메시)을 공급**하고, 객체에 **딱지**를 붙인다.
    객체는 평범한 메시라 그리기·픽킹·저장이 전부 그대로 동작하고, 플러그인이 없는 곳에서
    열어도 형상은 보인다. 딱지는 보존돼 나중에 플러그인이 있으면 도로 살아난다.

      id = CAD_CreateMesh(xyz, nv, idx, ni, NULL);          // 형상
      CAD_SetPluginTag(id, "ArchBuilder", "wall", json);   // 딱지
      ... 값이 바뀌면 → CAD_ReplaceMesh(id, ...)           // 재생성

    .lot 을 열어 딱지 붙은 객체가 복원되면 CAD_SetOnPluginEntityLoaded 콜백으로 알려준다.
    플러그인은 owner 가 자기 이름이면 data 를 읽어 살아 있는 엔티티로 넘겨받는다.

    사용자가 그립·불리언·밀당·분해로 메시를 직접 고치면 정의와 형상이 어긋나므로 엔진이
    먼저 묻고, "계속" 이면 딱지를 뗀다(그냥 메시가 된다). 호스트 임베드는 ImGui 가 없어
    CAD_SetOnConfirm 으로 대신 물어야 한다 — 안 달면 안전한 쪽(취소)으로 간다.

    xyz = 3*vertexCount, indices = 3*triangleCount. normals 는 NULL 가능(삼각형별 flat).
    """
    _a_xyz = _n.array(_c.c_float, xyz)
    _a_indices = _n.array(_c.c_uint, indices)
    _a_normals = _n.array(_c.c_float, normals)
    return _f.CAD_ReplaceMesh(id, _a_xyz, vertexCount, _a_indices, indexCount, _a_normals)


def CAD_SetPluginTag(id: int, owner: str | None, type: str | None, data: str | None) -> bool:
    """C: bool CAD_SetPluginTag(uint32_t id, const char* owner, const char* type, const char* data)

    플러그인 엔티티

    새 객체 종류를 만들지 않는다. 플러그인이 **형상(메시)을 공급**하고, 객체에 **딱지**를 붙인다.
    객체는 평범한 메시라 그리기·픽킹·저장이 전부 그대로 동작하고, 플러그인이 없는 곳에서
    열어도 형상은 보인다. 딱지는 보존돼 나중에 플러그인이 있으면 도로 살아난다.

      id = CAD_CreateMesh(xyz, nv, idx, ni, NULL);          // 형상
      CAD_SetPluginTag(id, "ArchBuilder", "wall", json);   // 딱지
      ... 값이 바뀌면 → CAD_ReplaceMesh(id, ...)           // 재생성

    .lot 을 열어 딱지 붙은 객체가 복원되면 CAD_SetOnPluginEntityLoaded 콜백으로 알려준다.
    플러그인은 owner 가 자기 이름이면 data 를 읽어 살아 있는 엔티티로 넘겨받는다.

    사용자가 그립·불리언·밀당·분해로 메시를 직접 고치면 정의와 형상이 어긋나므로 엔진이
    먼저 묻고, "계속" 이면 딱지를 뗀다(그냥 메시가 된다). 호스트 임베드는 ImGui 가 없어
    CAD_SetOnConfirm 으로 대신 물어야 한다 — 안 달면 안전한 쪽(취소)으로 간다.

    xyz = 3*vertexCount, indices = 3*triangleCount. normals 는 NULL 가능(삼각형별 flat).
    """
    return _f.CAD_SetPluginTag(id, _n.text(owner), _n.text(type), _n.text(data))


def CAD_ClearPluginTag(id: int) -> bool:
    """C: bool CAD_ClearPluginTag(uint32_t id)

    플러그인 엔티티

    새 객체 종류를 만들지 않는다. 플러그인이 **형상(메시)을 공급**하고, 객체에 **딱지**를 붙인다.
    객체는 평범한 메시라 그리기·픽킹·저장이 전부 그대로 동작하고, 플러그인이 없는 곳에서
    열어도 형상은 보인다. 딱지는 보존돼 나중에 플러그인이 있으면 도로 살아난다.

      id = CAD_CreateMesh(xyz, nv, idx, ni, NULL);          // 형상
      CAD_SetPluginTag(id, "ArchBuilder", "wall", json);   // 딱지
      ... 값이 바뀌면 → CAD_ReplaceMesh(id, ...)           // 재생성

    .lot 을 열어 딱지 붙은 객체가 복원되면 CAD_SetOnPluginEntityLoaded 콜백으로 알려준다.
    플러그인은 owner 가 자기 이름이면 data 를 읽어 살아 있는 엔티티로 넘겨받는다.

    사용자가 그립·불리언·밀당·분해로 메시를 직접 고치면 정의와 형상이 어긋나므로 엔진이
    먼저 묻고, "계속" 이면 딱지를 뗀다(그냥 메시가 된다). 호스트 임베드는 ImGui 가 없어
    CAD_SetOnConfirm 으로 대신 물어야 한다 — 안 달면 안전한 쪽(취소)으로 간다.

    xyz = 3*vertexCount, indices = 3*triangleCount. normals 는 NULL 가능(삼각형별 flat).
    """
    return _f.CAD_ClearPluginTag(id)


def CAD_HasPluginTag(id: int) -> bool:
    """C: bool CAD_HasPluginTag(uint32_t id)

    플러그인 엔티티

    새 객체 종류를 만들지 않는다. 플러그인이 **형상(메시)을 공급**하고, 객체에 **딱지**를 붙인다.
    객체는 평범한 메시라 그리기·픽킹·저장이 전부 그대로 동작하고, 플러그인이 없는 곳에서
    열어도 형상은 보인다. 딱지는 보존돼 나중에 플러그인이 있으면 도로 살아난다.

      id = CAD_CreateMesh(xyz, nv, idx, ni, NULL);          // 형상
      CAD_SetPluginTag(id, "ArchBuilder", "wall", json);   // 딱지
      ... 값이 바뀌면 → CAD_ReplaceMesh(id, ...)           // 재생성

    .lot 을 열어 딱지 붙은 객체가 복원되면 CAD_SetOnPluginEntityLoaded 콜백으로 알려준다.
    플러그인은 owner 가 자기 이름이면 data 를 읽어 살아 있는 엔티티로 넘겨받는다.

    사용자가 그립·불리언·밀당·분해로 메시를 직접 고치면 정의와 형상이 어긋나므로 엔진이
    먼저 묻고, "계속" 이면 딱지를 뗀다(그냥 메시가 된다). 호스트 임베드는 ImGui 가 없어
    CAD_SetOnConfirm 으로 대신 물어야 한다 — 안 달면 안전한 쪽(취소)으로 간다.

    xyz = 3*vertexCount, indices = 3*triangleCount. normals 는 NULL 가능(삼각형별 flat).
    """
    return _f.CAD_HasPluginTag(id)


def CAD_GetPluginTagOwner(id: int) -> str | None:
    """C: int CAD_GetPluginTagOwner(uint32_t id, char* buf, int bufLen)

    플러그인 엔티티

    새 객체 종류를 만들지 않는다. 플러그인이 **형상(메시)을 공급**하고, 객체에 **딱지**를 붙인다.
    객체는 평범한 메시라 그리기·픽킹·저장이 전부 그대로 동작하고, 플러그인이 없는 곳에서
    열어도 형상은 보인다. 딱지는 보존돼 나중에 플러그인이 있으면 도로 살아난다.

      id = CAD_CreateMesh(xyz, nv, idx, ni, NULL);          // 형상
      CAD_SetPluginTag(id, "ArchBuilder", "wall", json);   // 딱지
      ... 값이 바뀌면 → CAD_ReplaceMesh(id, ...)           // 재생성

    .lot 을 열어 딱지 붙은 객체가 복원되면 CAD_SetOnPluginEntityLoaded 콜백으로 알려준다.
    플러그인은 owner 가 자기 이름이면 data 를 읽어 살아 있는 엔티티로 넘겨받는다.

    사용자가 그립·불리언·밀당·분해로 메시를 직접 고치면 정의와 형상이 어긋나므로 엔진이
    먼저 묻고, "계속" 이면 딱지를 뗀다(그냥 메시가 된다). 호스트 임베드는 ImGui 가 없어
    CAD_SetOnConfirm 으로 대신 물어야 한다 — 안 달면 안전한 쪽(취소)으로 간다.

    xyz = 3*vertexCount, indices = 3*triangleCount. normals 는 NULL 가능(삼각형별 flat).
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetPluginTagOwner(id, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetPluginTagType(id: int) -> str | None:
    """C: int CAD_GetPluginTagType (uint32_t id, char* buf, int bufLen)

    플러그인 엔티티

    새 객체 종류를 만들지 않는다. 플러그인이 **형상(메시)을 공급**하고, 객체에 **딱지**를 붙인다.
    객체는 평범한 메시라 그리기·픽킹·저장이 전부 그대로 동작하고, 플러그인이 없는 곳에서
    열어도 형상은 보인다. 딱지는 보존돼 나중에 플러그인이 있으면 도로 살아난다.

      id = CAD_CreateMesh(xyz, nv, idx, ni, NULL);          // 형상
      CAD_SetPluginTag(id, "ArchBuilder", "wall", json);   // 딱지
      ... 값이 바뀌면 → CAD_ReplaceMesh(id, ...)           // 재생성

    .lot 을 열어 딱지 붙은 객체가 복원되면 CAD_SetOnPluginEntityLoaded 콜백으로 알려준다.
    플러그인은 owner 가 자기 이름이면 data 를 읽어 살아 있는 엔티티로 넘겨받는다.

    사용자가 그립·불리언·밀당·분해로 메시를 직접 고치면 정의와 형상이 어긋나므로 엔진이
    먼저 묻고, "계속" 이면 딱지를 뗀다(그냥 메시가 된다). 호스트 임베드는 ImGui 가 없어
    CAD_SetOnConfirm 으로 대신 물어야 한다 — 안 달면 안전한 쪽(취소)으로 간다.

    xyz = 3*vertexCount, indices = 3*triangleCount. normals 는 NULL 가능(삼각형별 flat).
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetPluginTagType(id, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetPluginTagData(id: int) -> str | None:
    """C: int CAD_GetPluginTagData (uint32_t id, char* buf, int bufLen)

    플러그인 엔티티

    새 객체 종류를 만들지 않는다. 플러그인이 **형상(메시)을 공급**하고, 객체에 **딱지**를 붙인다.
    객체는 평범한 메시라 그리기·픽킹·저장이 전부 그대로 동작하고, 플러그인이 없는 곳에서
    열어도 형상은 보인다. 딱지는 보존돼 나중에 플러그인이 있으면 도로 살아난다.

      id = CAD_CreateMesh(xyz, nv, idx, ni, NULL);          // 형상
      CAD_SetPluginTag(id, "ArchBuilder", "wall", json);   // 딱지
      ... 값이 바뀌면 → CAD_ReplaceMesh(id, ...)           // 재생성

    .lot 을 열어 딱지 붙은 객체가 복원되면 CAD_SetOnPluginEntityLoaded 콜백으로 알려준다.
    플러그인은 owner 가 자기 이름이면 data 를 읽어 살아 있는 엔티티로 넘겨받는다.

    사용자가 그립·불리언·밀당·분해로 메시를 직접 고치면 정의와 형상이 어긋나므로 엔진이
    먼저 묻고, "계속" 이면 딱지를 뗀다(그냥 메시가 된다). 호스트 임베드는 ImGui 가 없어
    CAD_SetOnConfirm 으로 대신 물어야 한다 — 안 달면 안전한 쪽(취소)으로 간다.

    xyz = 3*vertexCount, indices = 3*triangleCount. normals 는 NULL 가능(삼각형별 flat).
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetPluginTagData(id, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_SetOnPluginEntityLoaded(cb: Callable | None) -> None:
    """C: void CAD_SetOnPluginEntityLoaded(void (*cb)(uint32_t id, const char* owner, const char* type, const char* data))

    플러그인 엔티티

    새 객체 종류를 만들지 않는다. 플러그인이 **형상(메시)을 공급**하고, 객체에 **딱지**를 붙인다.
    객체는 평범한 메시라 그리기·픽킹·저장이 전부 그대로 동작하고, 플러그인이 없는 곳에서
    열어도 형상은 보인다. 딱지는 보존돼 나중에 플러그인이 있으면 도로 살아난다.

      id = CAD_CreateMesh(xyz, nv, idx, ni, NULL);          // 형상
      CAD_SetPluginTag(id, "ArchBuilder", "wall", json);   // 딱지
      ... 값이 바뀌면 → CAD_ReplaceMesh(id, ...)           // 재생성

    .lot 을 열어 딱지 붙은 객체가 복원되면 CAD_SetOnPluginEntityLoaded 콜백으로 알려준다.
    플러그인은 owner 가 자기 이름이면 data 를 읽어 살아 있는 엔티티로 넘겨받는다.

    사용자가 그립·불리언·밀당·분해로 메시를 직접 고치면 정의와 형상이 어긋나므로 엔진이
    먼저 묻고, "계속" 이면 딱지를 뗀다(그냥 메시가 된다). 호스트 임베드는 ImGui 가 없어
    CAD_SetOnConfirm 으로 대신 물어야 한다 — 안 달면 안전한 쪽(취소)으로 간다.

    xyz = 3*vertexCount, indices = 3*triangleCount. normals 는 NULL 가능(삼각형별 flat).
    """
    _cb_cb = _n.callback(CAD_SetOnPluginEntityLoaded_cb, cb, (1, 2, 3))
    _n.keep("CAD_SetOnPluginEntityLoaded.cb", _cb_cb, replace=True)
    _f.CAD_SetOnPluginEntityLoaded(_cb_cb)


def CAD_SetOnConfirm(cb: Callable | None) -> None:
    """C: void CAD_SetOnConfirm(bool (*cb)(const char* text))

    반환 true = 계속. 호스트 임베드(MFC/WPF)는 반드시 달 것 — 없으면 취소로 간다.
    """
    _cb_cb = _n.callback(CAD_SetOnConfirm_cb, cb, (0,))
    _n.keep("CAD_SetOnConfirm.cb", _cb_cb, replace=True)
    _f.CAD_SetOnConfirm(_cb_cb)


def CAD_AddEntityProperty(owner: str | None, type: str | None, key: str | None, label: str | None, kind: int, minV: float, maxV: float, pluginId: int) -> bool:
    """C: bool CAD_AddEntityProperty(const char* owner, const char* type, const char* key, const char* label, int kind, float minV, float maxV, unsigned int pluginId)

    엔티티 속성 (특성창)

    플러그인은 특성창을 직접 그리지 않는다. "두께는 0.05~2.0 실수" 라고 **말만** 하고
    엔진이 슬라이더를 그린다. ImGui 버전에 안 묶이고, 호스트 임베드에서도 산다.

      CAD_AddEntityProperty("HelloPlugin", "wall", "thick", "두께", 0, 0.05f, 2.0f, id);

    ⭐ 값은 딱지 data 에 **JSON 오브젝트**로 들어 있어야 한다. 엔진이 그 JSON 을 읽고 쓴다.
       그래서 플러그인이 없어도 값이 보인다(그때는 읽기 전용 — 형상을 다시 만들 코드가 없다).

    kind: 0=실수 1=정수 2=참거짓 3=문자(읽기전용)
    minV/maxV: min>=max 면 범위 없음. 실패: 빈 이름 · 같은 (owner,type,key) 중복.

    사용자가 값을 바꾸면 엔진이 딱지 JSON 을 갱신하고 CAD_SetOnPluginEntityChanged 를 부른다.
    플러그인은 거기서 CAD_ReplaceMesh 로 형상을 다시 만든다.
    """
    return _f.CAD_AddEntityProperty(_n.text(owner), _n.text(type), _n.text(key), _n.text(label), kind, minV, maxV, pluginId)


def CAD_RemoveEntityPropertiesByOwner(pluginId: int) -> int:
    """C: unsigned int CAD_RemoveEntityPropertiesByOwner(unsigned int pluginId)

    엔티티 속성 (특성창)

    플러그인은 특성창을 직접 그리지 않는다. "두께는 0.05~2.0 실수" 라고 **말만** 하고
    엔진이 슬라이더를 그린다. ImGui 버전에 안 묶이고, 호스트 임베드에서도 산다.

      CAD_AddEntityProperty("HelloPlugin", "wall", "thick", "두께", 0, 0.05f, 2.0f, id);

    ⭐ 값은 딱지 data 에 **JSON 오브젝트**로 들어 있어야 한다. 엔진이 그 JSON 을 읽고 쓴다.
       그래서 플러그인이 없어도 값이 보인다(그때는 읽기 전용 — 형상을 다시 만들 코드가 없다).

    kind: 0=실수 1=정수 2=참거짓 3=문자(읽기전용)
    minV/maxV: min>=max 면 범위 없음. 실패: 빈 이름 · 같은 (owner,type,key) 중복.

    사용자가 값을 바꾸면 엔진이 딱지 JSON 을 갱신하고 CAD_SetOnPluginEntityChanged 를 부른다.
    플러그인은 거기서 CAD_ReplaceMesh 로 형상을 다시 만든다.
    """
    return _f.CAD_RemoveEntityPropertiesByOwner(pluginId)


def CAD_SetOnPluginEntityChanged(cb: Callable | None) -> None:
    """C: void CAD_SetOnPluginEntityChanged(void (*cb)(uint32_t id, const char* owner, const char* type, const char* data))

    엔티티 속성 (특성창)

    플러그인은 특성창을 직접 그리지 않는다. "두께는 0.05~2.0 실수" 라고 **말만** 하고
    엔진이 슬라이더를 그린다. ImGui 버전에 안 묶이고, 호스트 임베드에서도 산다.

      CAD_AddEntityProperty("HelloPlugin", "wall", "thick", "두께", 0, 0.05f, 2.0f, id);

    ⭐ 값은 딱지 data 에 **JSON 오브젝트**로 들어 있어야 한다. 엔진이 그 JSON 을 읽고 쓴다.
       그래서 플러그인이 없어도 값이 보인다(그때는 읽기 전용 — 형상을 다시 만들 코드가 없다).

    kind: 0=실수 1=정수 2=참거짓 3=문자(읽기전용)
    minV/maxV: min>=max 면 범위 없음. 실패: 빈 이름 · 같은 (owner,type,key) 중복.

    사용자가 값을 바꾸면 엔진이 딱지 JSON 을 갱신하고 CAD_SetOnPluginEntityChanged 를 부른다.
    플러그인은 거기서 CAD_ReplaceMesh 로 형상을 다시 만든다.
    """
    _cb_cb = _n.callback(CAD_SetOnPluginEntityChanged_cb, cb, (1, 2, 3))
    _n.keep("CAD_SetOnPluginEntityChanged.cb", _cb_cb, replace=True)
    _f.CAD_SetOnPluginEntityChanged(_cb_cb)


def CAD_AddEventListener(kinds: int, fn: Callable | None, user: int | None, pluginId: int) -> int:
    """C: unsigned int CAD_AddEventListener(int kinds, CAD_EventFn fn, void* user, unsigned int pluginId)

    엔진 이벤트 구독

    ⚠️ 위 CAD_SetOnXxx 계열은 **한 칸짜리**다 — 플러그인이 걸면 호스트 것을 덮어쓴다.
       플러그인은 여러 개가 동시에 올라오므로 이쪽(목록)으로 구독한다. 둘 다 발화한다.

    kinds 는 비트 OR: 1=객체생성 2=객체삭제 4=선택변경 8=문서변경
      생성/삭제 → id = 그 객체. 선택변경 → id = 0. 문서변경 → id = dirty ? 1 : 0.

    반환 = 핸들(0 이면 실패). 언로드 때는 엔진이 pluginId 로 묶어 알아서 지운다.
    콜백은 엔진과 같은 스레드에서 프레임 끝에 불린다 — 안에서 CAD_* 를 불러도 된다.
    """
    _cb_fn = _n.callback(CAD_EventFn, fn, ())
    _n.keep("CAD_AddEventListener.fn", _cb_fn, replace=False)
    return _f.CAD_AddEventListener(kinds, _cb_fn, user, pluginId)


def CAD_RemoveEventListener(handle: int) -> bool:
    """C: bool CAD_RemoveEventListener(unsigned int handle)

    엔진 이벤트 구독

    ⚠️ 위 CAD_SetOnXxx 계열은 **한 칸짜리**다 — 플러그인이 걸면 호스트 것을 덮어쓴다.
       플러그인은 여러 개가 동시에 올라오므로 이쪽(목록)으로 구독한다. 둘 다 발화한다.

    kinds 는 비트 OR: 1=객체생성 2=객체삭제 4=선택변경 8=문서변경
      생성/삭제 → id = 그 객체. 선택변경 → id = 0. 문서변경 → id = dirty ? 1 : 0.

    반환 = 핸들(0 이면 실패). 언로드 때는 엔진이 pluginId 로 묶어 알아서 지운다.
    콜백은 엔진과 같은 스레드에서 프레임 끝에 불린다 — 안에서 CAD_* 를 불러도 된다.
    """
    return _f.CAD_RemoveEventListener(handle)


def CAD_GetImGuiContext() -> int | None:
    """C: void* CAD_GetImGuiContext(void)

    플러그인 패널 (ImGui 직접 그리기)

    패널은 CAD_AddUiItem(kind 4) 로 등록하면 엔진이 창을 만들고, 그 **안을 플러그인이**
    ImGui 로 그린다. 메뉴·툴바·리본과 달리 이것만 플러그인이 ImGui 를 직접 부른다.

    ⚠️ 그래서 제약이 붙는다:
       · 플러그인이 엔진과 **같은 ImGui 버전**을 컴파일해 넣어야 한다
       · 아래 두 함수로 컨텍스트와 할당자를 받아 ImGui::SetCurrentContext /
         ImGui::SetAllocatorFunctions 를 먼저 불러야 한다 — DLL 경계를 넘으면
         ImGui 전역과 힙이 공유되지 않는다(ImGui 문서의 그 항목)
       · **호스트 임베드(MFC/WPF)에선 안 뜬다** — 거기엔 ImGui 컨텍스트가 없다
         (CAD_GetImGuiContext 가 NULL 을 돌려준다)

    값 편집만 필요하면 CAD_AddEntityProperty(특성창) 가 이 제약을 전부 피한다.
    그래서 패널은 "그래프·미리보기처럼 정말 직접 그려야 하는 것" 에만 쓰는 게 좋다.

      void drawPanel(unsigned id, const char* title) { ImGui::Text("..."); }
      ImGui::SetCurrentContext((ImGuiContext*)CAD_GetImGuiContext());
      CAD_GetImGuiAllocators(&a, &f, &u); ImGui::SetAllocatorFunctions(a, f, u);
      CAD_SetOnDrawPanel(&drawPanel);
    """
    return _f.CAD_GetImGuiContext()


def CAD_GetImGuiAllocators() -> tuple[int | None, int | None, int | None]:
    """C: void CAD_GetImGuiAllocators(void** allocFn, void** freeFn, void** userData)

    플러그인 패널 (ImGui 직접 그리기)

    패널은 CAD_AddUiItem(kind 4) 로 등록하면 엔진이 창을 만들고, 그 **안을 플러그인이**
    ImGui 로 그린다. 메뉴·툴바·리본과 달리 이것만 플러그인이 ImGui 를 직접 부른다.

    ⚠️ 그래서 제약이 붙는다:
       · 플러그인이 엔진과 **같은 ImGui 버전**을 컴파일해 넣어야 한다
       · 아래 두 함수로 컨텍스트와 할당자를 받아 ImGui::SetCurrentContext /
         ImGui::SetAllocatorFunctions 를 먼저 불러야 한다 — DLL 경계를 넘으면
         ImGui 전역과 힙이 공유되지 않는다(ImGui 문서의 그 항목)
       · **호스트 임베드(MFC/WPF)에선 안 뜬다** — 거기엔 ImGui 컨텍스트가 없다
         (CAD_GetImGuiContext 가 NULL 을 돌려준다)

    값 편집만 필요하면 CAD_AddEntityProperty(특성창) 가 이 제약을 전부 피한다.
    그래서 패널은 "그래프·미리보기처럼 정말 직접 그려야 하는 것" 에만 쓰는 게 좋다.

      void drawPanel(unsigned id, const char* title) { ImGui::Text("..."); }
      ImGui::SetCurrentContext((ImGuiContext*)CAD_GetImGuiContext());
      CAD_GetImGuiAllocators(&a, &f, &u); ImGui::SetAllocatorFunctions(a, f, u);
      CAD_SetOnDrawPanel(&drawPanel);
    """
    allocFn = _c.c_void_p()
    freeFn = _c.c_void_p()
    userData = _c.c_void_p()
    _f.CAD_GetImGuiAllocators(_c.byref(allocFn), _c.byref(freeFn), _c.byref(userData))
    return (allocFn.value, freeFn.value, userData.value)


def CAD_SetOnDrawPanel(cb: Callable | None) -> None:
    """C: void CAD_SetOnDrawPanel(void (*cb)(unsigned int panelId, const char* title))

    플러그인 패널 (ImGui 직접 그리기)

    패널은 CAD_AddUiItem(kind 4) 로 등록하면 엔진이 창을 만들고, 그 **안을 플러그인이**
    ImGui 로 그린다. 메뉴·툴바·리본과 달리 이것만 플러그인이 ImGui 를 직접 부른다.

    ⚠️ 그래서 제약이 붙는다:
       · 플러그인이 엔진과 **같은 ImGui 버전**을 컴파일해 넣어야 한다
       · 아래 두 함수로 컨텍스트와 할당자를 받아 ImGui::SetCurrentContext /
         ImGui::SetAllocatorFunctions 를 먼저 불러야 한다 — DLL 경계를 넘으면
         ImGui 전역과 힙이 공유되지 않는다(ImGui 문서의 그 항목)
       · **호스트 임베드(MFC/WPF)에선 안 뜬다** — 거기엔 ImGui 컨텍스트가 없다
         (CAD_GetImGuiContext 가 NULL 을 돌려준다)

    값 편집만 필요하면 CAD_AddEntityProperty(특성창) 가 이 제약을 전부 피한다.
    그래서 패널은 "그래프·미리보기처럼 정말 직접 그려야 하는 것" 에만 쓰는 게 좋다.

      void drawPanel(unsigned id, const char* title) { ImGui::Text("..."); }
      ImGui::SetCurrentContext((ImGuiContext*)CAD_GetImGuiContext());
      CAD_GetImGuiAllocators(&a, &f, &u); ImGui::SetAllocatorFunctions(a, f, u);
      CAD_SetOnDrawPanel(&drawPanel);
    """
    _cb_cb = _n.callback(CAD_SetOnDrawPanel_cb, cb, (1,))
    _n.keep("CAD_SetOnDrawPanel.cb", _cb_cb, replace=True)
    _f.CAD_SetOnDrawPanel(_cb_cb)
