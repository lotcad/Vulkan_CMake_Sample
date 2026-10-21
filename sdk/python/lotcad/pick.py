# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Pick 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_BeginGetPoint', 'CAD_BeginGetEntSel', 'CAD_IsPicking', 'CAD_TryGetPickResult', 'CAD_CancelPick', 'CAD_SetSubobjectSelectionMode', 'CAD_GetSubobjectSelectionMode', 'CAD_PickSubobject', 'CAD_GetSubobjectSelectionId', 'CAD_GetSelectedFaceTriangles', 'CAD_GetSelectedEdge']

_f = _n.native

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
_n.bind("CAD_GetSelectedEdge", _c.c_bool, [_c.POINTER(_c.c_float)])


def CAD_BeginGetPoint(prompt: str | None) -> None:
    """C: void CAD_BeginGetPoint(const char* prompt)

    비동기: Begin 후 사용자가 클릭할 때까지 대기. 호스트가 매 프레임 bool 폴링.
    IsPicking=true            → 대기 중
    IsPicking=false + Try=true  → 완료 (좌표/엔티티 소비)
    IsPicking=false + Try=false → 취소(ESC)
    EntSel 은 빈 곳/비객체 클릭을 통과 안 시킴(유효 객체만 완료). Point 는 어디든 좌표 반환.
    """
    _f.CAD_BeginGetPoint(_n.text(prompt))


def CAD_BeginGetEntSel(prompt: str | None) -> None:
    """C: void CAD_BeginGetEntSel(const char* prompt)
    """
    _f.CAD_BeginGetEntSel(_n.text(prompt))


def CAD_IsPicking() -> bool:
    """C: bool CAD_IsPicking(void)
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
    """
    return _f.CAD_GetSubobjectSelectionMode()


def CAD_PickSubobject(ox: float, oy: float, oz: float, dx: float, dy: float, dz: float) -> bool:
    """C: bool CAD_PickSubobject(float ox, float oy, float oz, float dx, float dy, float dz)
    """
    return _f.CAD_PickSubobject(ox, oy, oz, dx, dy, dz)


def CAD_GetSubobjectSelectionId() -> int:
    """C: uint32_t CAD_GetSubobjectSelectionId(void)
    """
    return _f.CAD_GetSubobjectSelectionId()


def CAD_GetSelectedFaceTriangles(out: Any, capacity: int) -> int:
    """C: uint32_t CAD_GetSelectedFaceTriangles(uint32_t* out, uint32_t capacity)
    """
    return _f.CAD_GetSelectedFaceTriangles(out, capacity)


def CAD_GetSelectedEdge(endpoints6: Any) -> bool:
    """C: bool CAD_GetSelectedEdge(float* endpoints6)

    endpoints6 = {ax,ay,az,bx,by,bz}, world coordinates. False if no selected edge.
    """
    return _f.CAD_GetSelectedEdge(endpoints6)
