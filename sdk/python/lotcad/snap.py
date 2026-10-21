# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Snap 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_SetOSnapEnabled', 'CAD_GetOSnapEnabled', 'CAD_SetOSnapModes', 'CAD_GetOSnapModes', 'CAD_SetOrthoEnabled', 'CAD_GetOrthoEnabled', 'CAD_SetPolarTracking', 'CAD_GetPolarTracking']

_f = _n.native

_n.bind("CAD_SetOSnapEnabled", _c.c_bool, [_c.c_bool])
_n.bind("CAD_GetOSnapEnabled", _c.c_bool, [])
_n.bind("CAD_SetOSnapModes", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_GetOSnapModes", _c.c_uint32, [])
_n.bind("CAD_SetOrthoEnabled", None, [_c.c_bool])
_n.bind("CAD_GetOrthoEnabled", _c.c_bool, [])
_n.bind("CAD_SetPolarTracking", _c.c_bool, [_c.c_bool, _c.c_float])
_n.bind("CAD_GetPolarTracking", _c.c_bool, [_c.POINTER(_c.c_float)])


def CAD_SetOSnapEnabled(on: bool) -> bool:
    """C: bool CAD_SetOSnapEnabled(bool on)

    모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처)
    """
    return _f.CAD_SetOSnapEnabled(on)


def CAD_GetOSnapEnabled() -> bool:
    """C: bool CAD_GetOSnapEnabled(void)
    """
    return _f.CAD_GetOSnapEnabled()


def CAD_SetOSnapModes(mask: int) -> bool:
    """C: bool CAD_SetOSnapModes(uint32_t mask)
    """
    return _f.CAD_SetOSnapModes(mask)


def CAD_GetOSnapModes() -> int:
    """C: uint32_t CAD_GetOSnapModes(void)
    """
    return _f.CAD_GetOSnapModes()


def CAD_SetOrthoEnabled(on: bool) -> None:
    """C: void CAD_SetOrthoEnabled(bool on)
    """
    _f.CAD_SetOrthoEnabled(on)


def CAD_GetOrthoEnabled() -> bool:
    """C: bool CAD_GetOrthoEnabled(void)
    """
    return _f.CAD_GetOrthoEnabled()


def CAD_SetPolarTracking(on: bool, incrementDeg: float) -> bool:
    """C: bool CAD_SetPolarTracking(bool on, float incrementDeg)

    incrementDeg <= 0 = 지금 값 유지(기본 45°, 1~90)
    """
    return _f.CAD_SetPolarTracking(on, incrementDeg)


def CAD_GetPolarTracking() -> float | None:
    """C: bool CAD_GetPolarTracking(float* incrementDeg)

    켜짐 여부, incrementDeg NULL 가능
    """
    incrementDeg = _c.c_float()
    if not _f.CAD_GetPolarTracking(_c.byref(incrementDeg)):
        return None
    return incrementDeg.value
