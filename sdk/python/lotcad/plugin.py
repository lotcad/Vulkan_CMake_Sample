# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Plugin 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_AddUiItem', 'CAD_RemoveUiItem', 'CAD_RemoveUiItemsByOwner', 'CAD_GetUiItemCount', 'CAD_SetOverlayRibbonHeight', 'CAD_GetOverlayRibbonTop', 'CAD_GetUiItemId', 'CAD_GetUiItemKind', 'CAD_GetUiItemPath', 'CAD_GetUiItemTitle', 'CAD_GetUiItemCommand', 'CAD_GetUiItemIcon', 'CAD_AddUiControl', 'CAD_SetUiControlValue', 'CAD_GetUiControlValue', 'CAD_LoadPlugins', 'CAD_UnloadPlugin', 'CAD_GetPluginCount', 'CAD_GetPluginId', 'CAD_GetPluginName', 'CAD_SetPluginTag', 'CAD_ClearPluginTag', 'CAD_HasPluginTag', 'CAD_GetPluginTagOwner', 'CAD_GetPluginTagType', 'CAD_GetPluginTagData', 'CAD_SetOnPluginEntityLoaded', 'CAD_SetOnPluginEntityLoaded_cb', 'CAD_SetOnConfirm', 'CAD_SetOnConfirm_cb', 'CAD_AddEntityProperty', 'CAD_RemoveEntityPropertiesByOwner', 'CAD_SetOnPluginEntityChanged', 'CAD_SetOnPluginEntityChanged_cb', 'CAD_GetImGuiContext', 'CAD_GetImGuiAllocators', 'CAD_SetOnDrawPanel', 'CAD_SetOnDrawPanel_cb']

_f = _n.native

CAD_SetOnPluginEntityLoaded_cb = _c.CFUNCTYPE(None, _c.c_uint32, _c.c_char_p, _c.c_char_p, _c.c_char_p)
CAD_SetOnConfirm_cb = _c.CFUNCTYPE(_c.c_bool, _c.c_char_p)
CAD_SetOnPluginEntityChanged_cb = _c.CFUNCTYPE(None, _c.c_uint32, _c.c_char_p, _c.c_char_p, _c.c_char_p)
CAD_SetOnDrawPanel_cb = _c.CFUNCTYPE(None, _c.c_uint, _c.c_char_p)

_n.bind("CAD_AddUiItem", _c.c_int32, [_c.c_int32, _c.c_char_p, _c.c_char_p, _c.c_char_p, _c.c_char_p, _c.c_uint32, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_RemoveUiItem", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_RemoveUiItemsByOwner", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_GetUiItemCount", _c.c_int32, [])
_n.bind("CAD_SetOverlayRibbonHeight", _c.c_int32, [_c.c_double])
_n.bind("CAD_GetOverlayRibbonTop", _c.c_int32, [_c.POINTER(_c.c_double)])
_n.bind("CAD_GetUiItemId", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_GetUiItemKind", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_int32)])
_n.bind("CAD_GetUiItemPath", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_GetUiItemTitle", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_GetUiItemCommand", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_GetUiItemIcon", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_AddUiControl", _c.c_int32, [_c.c_int32, _c.c_char_p, _c.c_char_p, _c.c_char_p, _c.c_double, _c.c_double, _c.c_double, _c.c_uint32, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetUiControlValue", _c.c_int32, [_c.c_uint32, _c.c_double])
_n.bind("CAD_GetUiControlValue", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_double), _c.POINTER(_c.c_double), _c.POINTER(_c.c_double)])
_n.bind("CAD_LoadPlugins", _c.c_int32, [_c.c_char_p])
_n.bind("CAD_UnloadPlugin", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_GetPluginCount", _c.c_int32, [])
_n.bind("CAD_GetPluginId", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_GetPluginName", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_SetPluginTag", _c.c_int32, [_c.c_uint32, _c.c_char_p, _c.c_char_p, _c.c_char_p])
_n.bind("CAD_ClearPluginTag", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_HasPluginTag", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_bool)])
_n.bind("CAD_GetPluginTagOwner", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_GetPluginTagType", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_GetPluginTagData", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_SetOnPluginEntityLoaded", _c.c_int32, [CAD_SetOnPluginEntityLoaded_cb])
_n.bind("CAD_SetOnConfirm", _c.c_int32, [CAD_SetOnConfirm_cb])
_n.bind("CAD_AddEntityProperty", _c.c_int32, [_c.c_char_p, _c.c_char_p, _c.c_char_p, _c.c_char_p, _c.c_int32, _c.c_double, _c.c_double, _c.c_uint32])
_n.bind("CAD_RemoveEntityPropertiesByOwner", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_SetOnPluginEntityChanged", _c.c_int32, [CAD_SetOnPluginEntityChanged_cb])
_n.bind("CAD_GetImGuiContext", _c.c_int32, [_c.POINTER(_c.c_void_p)])
_n.bind("CAD_GetImGuiAllocators", _c.c_int32, [_c.POINTER(_c.c_void_p), _c.POINTER(_c.c_void_p), _c.POINTER(_c.c_void_p)])
_n.bind("CAD_SetOnDrawPanel", _c.c_int32, [CAD_SetOnDrawPanel_cb])


def CAD_AddUiItem(kind: int, path: str | None, title: str | None, command: str | None, icon: str | None, owner: int) -> tuple[int, int]:
    """C: CAD_Status CAD_AddUiItem(int32_t kind, const char* path, const char* title, const char* command, const char* icon, uint32_t owner, uint32_t* outItemId)

    UI 등록 (플러그인)

    플러그인은 UI 를 **직접 그리지 않는다.** (이름, 위치, 명령) 만 올리면 엔진이 그린다.
    그래서 ImGui 버전에 묶이지 않고, C#/Python 플러그인도 같은 방식을 쓰며,
    **호스트 임베드(MFC/WPF)에서도 산다** — 호스트가 이 목록을 읽어 자기 메뉴로 그리면 된다.

    kind: 0=메뉴항목 1=구분선 2=툴바버튼 3=리본버튼 4=패널
    path: 위치. 구분자는 '/'.
            메뉴 "건축" · "건축/가져오기"   툴바/리본 "건축/벽체"
            패널은 도킹 위치를 여기 넣는다("left"/"right"/"bottom").
    command: 누르면 실행할 명령 이름. 명령행과 **같은 입구**로 들어간다.
             구분선·패널은 NULL 가능. 그 외엔 title·command 가 비면 CAD_E_INVALID_ARG —
             눌러도 아무 일이 안 생기는 항목은 등록 단계에서 막는다.
    icon: 짧은 글자/이모지. 지금은 글자로 보여주고 나중에 아이콘으로 바꾼다. NULL 가능.
    owner: 플러그인 ID. 언로드 시 이 값으로 묶어 한꺼번에 지운다.

    성공하면 *outItemId = 항목 id(NULL 가능) — 이 id 로 개별 제거한다. kind 범위 밖 CAD_E_OUT_OF_RANGE(5·6 = CAD_AddUiControl).
    ⚠️ 패널은 **존재만** 등록된다 — 내용은 플러그인이 ImGui 후크로 그려야 하고,
       그건 단독 실행 전용이다(호스트 임베드엔 ImGui 컨텍스트가 없다).
    """
    outItemId = _c.c_uint32()
    _r = _f.CAD_AddUiItem(kind, _n.text(path), _n.text(title), _n.text(command), _n.text(icon), owner, _c.byref(outItemId))
    return (_r, outItemId.value)


def CAD_RemoveUiItem(id: int) -> int:
    """C: CAD_Status CAD_RemoveUiItem(uint32_t id)

    없는 id CAD_E_NOT_FOUND

    묶음 주석: UI 등록 (플러그인)

    플러그인은 UI 를 **직접 그리지 않는다.** (이름, 위치, 명령) 만 올리면 엔진이 그린다.
    그래서 ImGui 버전에 묶이지 않고, C#/Python 플러그인도 같은 방식을 쓰며,
    **호스트 임베드(MFC/WPF)에서도 산다** — 호스트가 이 목록을 읽어 자기 메뉴로 그리면 된다.

    kind: 0=메뉴항목 1=구분선 2=툴바버튼 3=리본버튼 4=패널
    path: 위치. 구분자는 '/'.
            메뉴 "건축" · "건축/가져오기"   툴바/리본 "건축/벽체"
            패널은 도킹 위치를 여기 넣는다("left"/"right"/"bottom").
    command: 누르면 실행할 명령 이름. 명령행과 **같은 입구**로 들어간다.
             구분선·패널은 NULL 가능. 그 외엔 title·command 가 비면 CAD_E_INVALID_ARG —
             눌러도 아무 일이 안 생기는 항목은 등록 단계에서 막는다.
    icon: 짧은 글자/이모지. 지금은 글자로 보여주고 나중에 아이콘으로 바꾼다. NULL 가능.
    owner: 플러그인 ID. 언로드 시 이 값으로 묶어 한꺼번에 지운다.

    성공하면 *outItemId = 항목 id(NULL 가능) — 이 id 로 개별 제거한다. kind 범위 밖 CAD_E_OUT_OF_RANGE(5·6 = CAD_AddUiControl).
    ⚠️ 패널은 **존재만** 등록된다 — 내용은 플러그인이 ImGui 후크로 그려야 하고,
       그건 단독 실행 전용이다(호스트 임베드엔 ImGui 컨텍스트가 없다).
    """
    return _f.CAD_RemoveUiItem(id)


def CAD_RemoveUiItemsByOwner(owner: int) -> int:
    """C: int32_t CAD_RemoveUiItemsByOwner(uint32_t owner)

    지운 개수

    묶음 주석: UI 등록 (플러그인)

    플러그인은 UI 를 **직접 그리지 않는다.** (이름, 위치, 명령) 만 올리면 엔진이 그린다.
    그래서 ImGui 버전에 묶이지 않고, C#/Python 플러그인도 같은 방식을 쓰며,
    **호스트 임베드(MFC/WPF)에서도 산다** — 호스트가 이 목록을 읽어 자기 메뉴로 그리면 된다.

    kind: 0=메뉴항목 1=구분선 2=툴바버튼 3=리본버튼 4=패널
    path: 위치. 구분자는 '/'.
            메뉴 "건축" · "건축/가져오기"   툴바/리본 "건축/벽체"
            패널은 도킹 위치를 여기 넣는다("left"/"right"/"bottom").
    command: 누르면 실행할 명령 이름. 명령행과 **같은 입구**로 들어간다.
             구분선·패널은 NULL 가능. 그 외엔 title·command 가 비면 CAD_E_INVALID_ARG —
             눌러도 아무 일이 안 생기는 항목은 등록 단계에서 막는다.
    icon: 짧은 글자/이모지. 지금은 글자로 보여주고 나중에 아이콘으로 바꾼다. NULL 가능.
    owner: 플러그인 ID. 언로드 시 이 값으로 묶어 한꺼번에 지운다.

    성공하면 *outItemId = 항목 id(NULL 가능) — 이 id 로 개별 제거한다. kind 범위 밖 CAD_E_OUT_OF_RANGE(5·6 = CAD_AddUiControl).
    ⚠️ 패널은 **존재만** 등록된다 — 내용은 플러그인이 ImGui 후크로 그려야 하고,
       그건 단독 실행 전용이다(호스트 임베드엔 ImGui 컨텍스트가 없다).
    """
    return _f.CAD_RemoveUiItemsByOwner(owner)


def CAD_GetUiItemCount() -> int:
    """C: int32_t CAD_GetUiItemCount(void)

    호스트가 메뉴·툴바를 직접 그릴 때 읽는다. index 는 등록 순서 = 화면 나열 순서(0 ~ 개수 − 1, 범위 밖 CAD_E_OUT_OF_RANGE).
    """
    return _f.CAD_GetUiItemCount()


def CAD_SetOverlayRibbonHeight(logicalHeight: float) -> int:
    """C: CAD_Status CAD_SetOverlayRibbonHeight(double logicalHeight)

    양수 높이 = 바깥 오버레이용으로 기본 리본 자리를 비워 둔다(논리 픽셀). 0 = 원래 ImGui 리본·플러그인 리본으로
    """
    return _f.CAD_SetOverlayRibbonHeight(logicalHeight)


def CAD_GetOverlayRibbonTop() -> tuple[int, float]:
    """C: CAD_Status CAD_GetOverlayRibbonTop(double* outTop)

    호스트 메뉴줄 바로 아래 논리 Y(ImGui 가 없으면 0)
    """
    outTop = _c.c_double()
    _r = _f.CAD_GetOverlayRibbonTop(_c.byref(outTop))
    return (_r, outTop.value)


def CAD_GetUiItemId(index: int) -> tuple[int, int]:
    """C: CAD_Status CAD_GetUiItemId(uint32_t index, uint32_t* outItemId)

    호스트 메뉴줄 바로 아래 논리 Y(ImGui 가 없으면 0)
    """
    outItemId = _c.c_uint32()
    _r = _f.CAD_GetUiItemId(index, _c.byref(outItemId))
    return (_r, outItemId.value)


def CAD_GetUiItemKind(index: int) -> tuple[int, int]:
    """C: CAD_Status CAD_GetUiItemKind(uint32_t index, int32_t* outKind)

    호스트 메뉴줄 바로 아래 논리 Y(ImGui 가 없으면 0)
    """
    outKind = _c.c_int32()
    _r = _f.CAD_GetUiItemKind(index, _c.byref(outKind))
    return (_r, outKind.value)


def CAD_GetUiItemPath(index: int) -> str | None:
    """C: int32_t CAD_GetUiItemPath(uint32_t index, char* buf, uint32_t capacity)

    호스트 메뉴줄 바로 아래 논리 Y(ImGui 가 없으면 0)
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
    """C: int32_t CAD_GetUiItemTitle(uint32_t index, char* buf, uint32_t capacity)

    호스트 메뉴줄 바로 아래 논리 Y(ImGui 가 없으면 0)
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
    """C: int32_t CAD_GetUiItemCommand(uint32_t index, char* buf, uint32_t capacity)

    호스트 메뉴줄 바로 아래 논리 Y(ImGui 가 없으면 0)
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
    """C: int32_t CAD_GetUiItemIcon(uint32_t index, char* buf, uint32_t capacity)

    호스트 메뉴줄 바로 아래 논리 Y(ImGui 가 없으면 0)
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


def CAD_AddUiControl(kind: int, path: str | None, title: str | None, command: str | None, minimum: float, maximum: float, value: float, owner: int) -> tuple[int, int]:
    """C: CAD_Status CAD_AddUiControl(int32_t kind, const char* path, const char* title, const char* command, double minimum, double maximum, double value, uint32_t owner, uint32_t* outItemId)

    리본 조작 항목 — kind 5 = 체크 상자(값 0/1, 범위 무시), 6 = 슬라이더(유한한 minimum < maximum, 값은 그 안으로).
    path = "탭/그룹". 사용자가 바꾸면 command 가 불리고, 그 명령이 CAD_GetUiControlValue(id) 로 새 값을 읽는다.
    잘못된 값·범위 CAD_E_INVALID_ARG, 없는 id CAD_E_NOT_FOUND. 플러그인은 언로드 때 엔진이 owner 로 지운다.
    """
    outItemId = _c.c_uint32()
    _r = _f.CAD_AddUiControl(kind, _n.text(path), _n.text(title), _n.text(command), minimum, maximum, value, owner, _c.byref(outItemId))
    return (_r, outItemId.value)


def CAD_SetUiControlValue(id: int, value: float) -> int:
    """C: CAD_Status CAD_SetUiControlValue(uint32_t id, double value)

    리본 조작 항목 — kind 5 = 체크 상자(값 0/1, 범위 무시), 6 = 슬라이더(유한한 minimum < maximum, 값은 그 안으로).
    path = "탭/그룹". 사용자가 바꾸면 command 가 불리고, 그 명령이 CAD_GetUiControlValue(id) 로 새 값을 읽는다.
    잘못된 값·범위 CAD_E_INVALID_ARG, 없는 id CAD_E_NOT_FOUND. 플러그인은 언로드 때 엔진이 owner 로 지운다.
    """
    return _f.CAD_SetUiControlValue(id, value)


def CAD_GetUiControlValue(id: int) -> tuple[int, float, float, float]:
    """C: CAD_Status CAD_GetUiControlValue(uint32_t id, double* value, double* minimum, double* maximum)

    출력은 NULL 가능

    묶음 주석: 리본 조작 항목 — kind 5 = 체크 상자(값 0/1, 범위 무시), 6 = 슬라이더(유한한 minimum < maximum, 값은 그 안으로).
    path = "탭/그룹". 사용자가 바꾸면 command 가 불리고, 그 명령이 CAD_GetUiControlValue(id) 로 새 값을 읽는다.
    잘못된 값·범위 CAD_E_INVALID_ARG, 없는 id CAD_E_NOT_FOUND. 플러그인은 언로드 때 엔진이 owner 로 지운다.
    """
    value = _c.c_double()
    minimum = _c.c_double()
    maximum = _c.c_double()
    _r = _f.CAD_GetUiControlValue(id, _c.byref(value), _c.byref(minimum), _c.byref(maximum))
    return (_r, value.value, minimum.value, maximum.value)


def CAD_LoadPlugins(dir: str | None) -> int:
    """C: int32_t CAD_LoadPlugins(const char* dir)

    dir 의 플러그인을 붙인다(이미 붙은 것은 건너뜀). 반환 = 새로 붙인 개수(0 이면 이유 — ABI 다름 등 — 가 CAD_GetLastError 에 있을 수 있다).
    폴더가 아님 CAD_E_NOT_FOUND
    """
    return _f.CAD_LoadPlugins(_n.text(dir))


def CAD_UnloadPlugin(id: int) -> int:
    """C: CAD_Status CAD_UnloadPlugin(uint32_t id)

    없는 id CAD_E_NOT_FOUND

    묶음 주석: dir 의 플러그인을 붙인다(이미 붙은 것은 건너뜀). 반환 = 새로 붙인 개수(0 이면 이유 — ABI 다름 등 — 가 CAD_GetLastError 에 있을 수 있다).
    폴더가 아님 CAD_E_NOT_FOUND
    """
    return _f.CAD_UnloadPlugin(id)


def CAD_GetPluginCount() -> int:
    """C: int32_t CAD_GetPluginCount(void)

    dir 의 플러그인을 붙인다(이미 붙은 것은 건너뜀). 반환 = 새로 붙인 개수(0 이면 이유 — ABI 다름 등 — 가 CAD_GetLastError 에 있을 수 있다).
    폴더가 아님 CAD_E_NOT_FOUND
    """
    return _f.CAD_GetPluginCount()


def CAD_GetPluginId(index: int) -> tuple[int, int]:
    """C: CAD_Status CAD_GetPluginId(uint32_t index, uint32_t* outPluginId)

    dir 의 플러그인을 붙인다(이미 붙은 것은 건너뜀). 반환 = 새로 붙인 개수(0 이면 이유 — ABI 다름 등 — 가 CAD_GetLastError 에 있을 수 있다).
    폴더가 아님 CAD_E_NOT_FOUND
    """
    outPluginId = _c.c_uint32()
    _r = _f.CAD_GetPluginId(index, _c.byref(outPluginId))
    return (_r, outPluginId.value)


def CAD_GetPluginName(index: int) -> str | None:
    """C: int32_t CAD_GetPluginName(uint32_t index, char* buf, uint32_t capacity)

    dir 의 플러그인을 붙인다(이미 붙은 것은 건너뜀). 반환 = 새로 붙인 개수(0 이면 이유 — ABI 다름 등 — 가 CAD_GetLastError 에 있을 수 있다).
    폴더가 아님 CAD_E_NOT_FOUND
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


def CAD_SetPluginTag(id: int, owner: str | None, type: str | None, data: str | None) -> int:
    """C: CAD_Status CAD_SetPluginTag(uint32_t id, const char* owner, const char* type, const char* data)

    없는 객체 CAD_E_BAD_HANDLE · owner 빈 글 CAD_E_INVALID_ARG · 딱지 없는 객체의 Get* = CAD_E_NOT_FOUND
    """
    return _f.CAD_SetPluginTag(id, _n.text(owner), _n.text(type), _n.text(data))


def CAD_ClearPluginTag(id: int) -> int:
    """C: CAD_Status CAD_ClearPluginTag(uint32_t id)

    없는 객체 CAD_E_BAD_HANDLE · owner 빈 글 CAD_E_INVALID_ARG · 딱지 없는 객체의 Get* = CAD_E_NOT_FOUND
    """
    return _f.CAD_ClearPluginTag(id)


def CAD_HasPluginTag(id: int) -> tuple[int, bool]:
    """C: CAD_Status CAD_HasPluginTag(uint32_t id, bool* outHas)

    없는 객체 CAD_E_BAD_HANDLE · owner 빈 글 CAD_E_INVALID_ARG · 딱지 없는 객체의 Get* = CAD_E_NOT_FOUND
    """
    outHas = _c.c_bool()
    _r = _f.CAD_HasPluginTag(id, _c.byref(outHas))
    return (_r, outHas.value)


def CAD_GetPluginTagOwner(id: int) -> str | None:
    """C: int32_t CAD_GetPluginTagOwner(uint32_t id, char* buf, uint32_t capacity)

    없는 객체 CAD_E_BAD_HANDLE · owner 빈 글 CAD_E_INVALID_ARG · 딱지 없는 객체의 Get* = CAD_E_NOT_FOUND
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
    """C: int32_t CAD_GetPluginTagType(uint32_t id, char* buf, uint32_t capacity)

    없는 객체 CAD_E_BAD_HANDLE · owner 빈 글 CAD_E_INVALID_ARG · 딱지 없는 객체의 Get* = CAD_E_NOT_FOUND
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
    """C: int32_t CAD_GetPluginTagData(uint32_t id, char* buf, uint32_t capacity)

    없는 객체 CAD_E_BAD_HANDLE · owner 빈 글 CAD_E_INVALID_ARG · 딱지 없는 객체의 Get* = CAD_E_NOT_FOUND
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


def CAD_SetOnPluginEntityLoaded(cb: Callable | None) -> int:
    """C: CAD_Status CAD_SetOnPluginEntityLoaded(void (*cb)(uint32_t id, const char* owner, const char* type, const char* data))

    없는 객체 CAD_E_BAD_HANDLE · owner 빈 글 CAD_E_INVALID_ARG · 딱지 없는 객체의 Get* = CAD_E_NOT_FOUND
    """
    _cb_cb = _n.callback(CAD_SetOnPluginEntityLoaded_cb, cb, (1, 2, 3))
    _n.keep("CAD_SetOnPluginEntityLoaded.cb", _cb_cb, replace=True)
    return _f.CAD_SetOnPluginEntityLoaded(_cb_cb)


def CAD_SetOnConfirm(cb: Callable | None) -> int:
    """C: CAD_Status CAD_SetOnConfirm(bool (*cb)(const char* text))

    콜백 반환 true = 계속. 호스트 임베드(MFC/WPF)는 반드시 달 것 — 없으면 취소로 간다.
    """
    _cb_cb = _n.callback(CAD_SetOnConfirm_cb, cb, (0,))
    _n.keep("CAD_SetOnConfirm.cb", _cb_cb, replace=True)
    return _f.CAD_SetOnConfirm(_cb_cb)


def CAD_AddEntityProperty(owner: str | None, type: str | None, key: str | None, label: str | None, kind: int, minV: float, maxV: float, pluginId: int) -> int:
    """C: CAD_Status CAD_AddEntityProperty(const char* owner, const char* type, const char* key, const char* label, int32_t kind, double minV, double maxV, uint32_t pluginId)

    엔티티 속성 (특성창)

    플러그인은 특성창을 직접 그리지 않는다. "두께는 0.05~2.0 실수" 라고 **말만** 하고
    엔진이 슬라이더를 그린다. ImGui 버전에 안 묶이고, 호스트 임베드에서도 산다.

      CAD_AddEntityProperty("HelloPlugin", "wall", "thick", "두께", 0, 0.05f, 2.0f, id);

    ⭐ 값은 딱지 data 에 **JSON 오브젝트**로 들어 있어야 한다. 엔진이 그 JSON 을 읽고 쓴다.
       그래서 플러그인이 없어도 값이 보인다(그때는 읽기 전용 — 형상을 다시 만들 코드가 없다).

    kind: 0=실수 1=정수 2=참거짓 3=문자(읽기전용)
    minV/maxV: min>=max 면 범위 없음. 실패: owner·type·key 빈 글 CAD_E_INVALID_ARG · kind 범위 밖 CAD_E_OUT_OF_RANGE ·
      같은 (owner,type,key) CAD_E_DUPLICATE.

    사용자가 값을 바꾸면 엔진이 딱지 JSON 을 갱신하고 CAD_SetOnPluginEntityChanged 를 부른다.
    플러그인은 거기서 CAD_ReplaceMesh 로 형상을 다시 만든다.
    """
    return _f.CAD_AddEntityProperty(_n.text(owner), _n.text(type), _n.text(key), _n.text(label), kind, minV, maxV, pluginId)


def CAD_RemoveEntityPropertiesByOwner(pluginId: int) -> int:
    """C: int32_t CAD_RemoveEntityPropertiesByOwner(uint32_t pluginId)

    지운 개수

    묶음 주석: 엔티티 속성 (특성창)

    플러그인은 특성창을 직접 그리지 않는다. "두께는 0.05~2.0 실수" 라고 **말만** 하고
    엔진이 슬라이더를 그린다. ImGui 버전에 안 묶이고, 호스트 임베드에서도 산다.

      CAD_AddEntityProperty("HelloPlugin", "wall", "thick", "두께", 0, 0.05f, 2.0f, id);

    ⭐ 값은 딱지 data 에 **JSON 오브젝트**로 들어 있어야 한다. 엔진이 그 JSON 을 읽고 쓴다.
       그래서 플러그인이 없어도 값이 보인다(그때는 읽기 전용 — 형상을 다시 만들 코드가 없다).

    kind: 0=실수 1=정수 2=참거짓 3=문자(읽기전용)
    minV/maxV: min>=max 면 범위 없음. 실패: owner·type·key 빈 글 CAD_E_INVALID_ARG · kind 범위 밖 CAD_E_OUT_OF_RANGE ·
      같은 (owner,type,key) CAD_E_DUPLICATE.

    사용자가 값을 바꾸면 엔진이 딱지 JSON 을 갱신하고 CAD_SetOnPluginEntityChanged 를 부른다.
    플러그인은 거기서 CAD_ReplaceMesh 로 형상을 다시 만든다.
    """
    return _f.CAD_RemoveEntityPropertiesByOwner(pluginId)


def CAD_SetOnPluginEntityChanged(cb: Callable | None) -> int:
    """C: CAD_Status CAD_SetOnPluginEntityChanged(void (*cb)(uint32_t id, const char* owner, const char* type, const char* data))

    엔티티 속성 (특성창)

    플러그인은 특성창을 직접 그리지 않는다. "두께는 0.05~2.0 실수" 라고 **말만** 하고
    엔진이 슬라이더를 그린다. ImGui 버전에 안 묶이고, 호스트 임베드에서도 산다.

      CAD_AddEntityProperty("HelloPlugin", "wall", "thick", "두께", 0, 0.05f, 2.0f, id);

    ⭐ 값은 딱지 data 에 **JSON 오브젝트**로 들어 있어야 한다. 엔진이 그 JSON 을 읽고 쓴다.
       그래서 플러그인이 없어도 값이 보인다(그때는 읽기 전용 — 형상을 다시 만들 코드가 없다).

    kind: 0=실수 1=정수 2=참거짓 3=문자(읽기전용)
    minV/maxV: min>=max 면 범위 없음. 실패: owner·type·key 빈 글 CAD_E_INVALID_ARG · kind 범위 밖 CAD_E_OUT_OF_RANGE ·
      같은 (owner,type,key) CAD_E_DUPLICATE.

    사용자가 값을 바꾸면 엔진이 딱지 JSON 을 갱신하고 CAD_SetOnPluginEntityChanged 를 부른다.
    플러그인은 거기서 CAD_ReplaceMesh 로 형상을 다시 만든다.
    """
    _cb_cb = _n.callback(CAD_SetOnPluginEntityChanged_cb, cb, (1, 2, 3))
    _n.keep("CAD_SetOnPluginEntityChanged.cb", _cb_cb, replace=True)
    return _f.CAD_SetOnPluginEntityChanged(_cb_cb)


def CAD_GetImGuiContext() -> tuple[int, int | None]:
    """C: CAD_Status CAD_GetImGuiContext(void** outContext)

    플러그인 패널 (ImGui 직접 그리기)

    패널은 CAD_AddUiItem(kind 4) 로 등록하면 엔진이 창을 만들고, 그 **안을 플러그인이**
    ImGui 로 그린다. 메뉴·툴바·리본과 달리 이것만 플러그인이 ImGui 를 직접 부른다.

    ⚠️ 그래서 제약이 붙는다:
       · 플러그인이 엔진과 **같은 ImGui 버전**을 컴파일해 넣어야 한다
       · 아래 두 함수로 컨텍스트와 할당자를 받아 ImGui::SetCurrentContext /
         ImGui::SetAllocatorFunctions 를 먼저 불러야 한다 — DLL 경계를 넘으면
         ImGui 전역과 힙이 공유되지 않는다(ImGui 문서의 그 항목)
       · **호스트 임베드(MFC/WPF)에선 안 뜬다** — 거기엔 ImGui 컨텍스트가 없다
         (CAD_GetImGuiContext 가 CAD_E_NOT_SUPPORTED)

    값 편집만 필요하면 CAD_AddEntityProperty(특성창) 가 이 제약을 전부 피한다.
    그래서 패널은 "그래프·미리보기처럼 정말 직접 그려야 하는 것" 에만 쓰는 게 좋다.

      void drawPanel(unsigned id, const char* title) { ImGui::Text("..."); }
      void* ctx = NULL; if (CAD_GetImGuiContext(&ctx) == CAD_OK) ImGui::SetCurrentContext((ImGuiContext*)ctx);
      CAD_GetImGuiAllocators(&a, &f, &u); ImGui::SetAllocatorFunctions(a, f, u);
      CAD_SetOnDrawPanel(&drawPanel);
    *outContext = ImGuiContext* — ImGui 가 없으면 CAD_E_NOT_SUPPORTED + NULL
    """
    outContext = _c.c_void_p()
    _r = _f.CAD_GetImGuiContext(_c.byref(outContext))
    return (_r, outContext.value)


def CAD_GetImGuiAllocators() -> tuple[int, int | None, int | None, int | None]:
    """C: CAD_Status CAD_GetImGuiAllocators(void** allocFn, void** freeFn, void** userData)

    플러그인 패널 (ImGui 직접 그리기)

    패널은 CAD_AddUiItem(kind 4) 로 등록하면 엔진이 창을 만들고, 그 **안을 플러그인이**
    ImGui 로 그린다. 메뉴·툴바·리본과 달리 이것만 플러그인이 ImGui 를 직접 부른다.

    ⚠️ 그래서 제약이 붙는다:
       · 플러그인이 엔진과 **같은 ImGui 버전**을 컴파일해 넣어야 한다
       · 아래 두 함수로 컨텍스트와 할당자를 받아 ImGui::SetCurrentContext /
         ImGui::SetAllocatorFunctions 를 먼저 불러야 한다 — DLL 경계를 넘으면
         ImGui 전역과 힙이 공유되지 않는다(ImGui 문서의 그 항목)
       · **호스트 임베드(MFC/WPF)에선 안 뜬다** — 거기엔 ImGui 컨텍스트가 없다
         (CAD_GetImGuiContext 가 CAD_E_NOT_SUPPORTED)

    값 편집만 필요하면 CAD_AddEntityProperty(특성창) 가 이 제약을 전부 피한다.
    그래서 패널은 "그래프·미리보기처럼 정말 직접 그려야 하는 것" 에만 쓰는 게 좋다.

      void drawPanel(unsigned id, const char* title) { ImGui::Text("..."); }
      void* ctx = NULL; if (CAD_GetImGuiContext(&ctx) == CAD_OK) ImGui::SetCurrentContext((ImGuiContext*)ctx);
      CAD_GetImGuiAllocators(&a, &f, &u); ImGui::SetAllocatorFunctions(a, f, u);
      CAD_SetOnDrawPanel(&drawPanel);
    """
    allocFn = _c.c_void_p()
    freeFn = _c.c_void_p()
    userData = _c.c_void_p()
    _r = _f.CAD_GetImGuiAllocators(_c.byref(allocFn), _c.byref(freeFn), _c.byref(userData))
    return (_r, allocFn.value, freeFn.value, userData.value)


def CAD_SetOnDrawPanel(cb: Callable | None) -> int:
    """C: CAD_Status CAD_SetOnDrawPanel(void (*cb)(unsigned int panelId, const char* title))

    플러그인 패널 (ImGui 직접 그리기)

    패널은 CAD_AddUiItem(kind 4) 로 등록하면 엔진이 창을 만들고, 그 **안을 플러그인이**
    ImGui 로 그린다. 메뉴·툴바·리본과 달리 이것만 플러그인이 ImGui 를 직접 부른다.

    ⚠️ 그래서 제약이 붙는다:
       · 플러그인이 엔진과 **같은 ImGui 버전**을 컴파일해 넣어야 한다
       · 아래 두 함수로 컨텍스트와 할당자를 받아 ImGui::SetCurrentContext /
         ImGui::SetAllocatorFunctions 를 먼저 불러야 한다 — DLL 경계를 넘으면
         ImGui 전역과 힙이 공유되지 않는다(ImGui 문서의 그 항목)
       · **호스트 임베드(MFC/WPF)에선 안 뜬다** — 거기엔 ImGui 컨텍스트가 없다
         (CAD_GetImGuiContext 가 CAD_E_NOT_SUPPORTED)

    값 편집만 필요하면 CAD_AddEntityProperty(특성창) 가 이 제약을 전부 피한다.
    그래서 패널은 "그래프·미리보기처럼 정말 직접 그려야 하는 것" 에만 쓰는 게 좋다.

      void drawPanel(unsigned id, const char* title) { ImGui::Text("..."); }
      void* ctx = NULL; if (CAD_GetImGuiContext(&ctx) == CAD_OK) ImGui::SetCurrentContext((ImGuiContext*)ctx);
      CAD_GetImGuiAllocators(&a, &f, &u); ImGui::SetAllocatorFunctions(a, f, u);
      CAD_SetOnDrawPanel(&drawPanel);
    """
    _cb_cb = _n.callback(CAD_SetOnDrawPanel_cb, cb, (1,))
    _n.keep("CAD_SetOnDrawPanel.cb", _cb_cb, replace=True)
    return _f.CAD_SetOnDrawPanel(_cb_cb)
