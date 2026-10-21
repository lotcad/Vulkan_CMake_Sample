# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Overlay 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_OVERLAY_CAPTURE_POINTER', 'CAD_OVERLAY_CAPTURE_KEYBOARD', 'CAD_SetOverlayRenderCallback', 'CAD_SetOverlayInputCallback']

_f = _n.native

CAD_OVERLAY_CAPTURE_POINTER = 1
CAD_OVERLAY_CAPTURE_KEYBOARD = 2

_n.bind("CAD_SetOverlayRenderCallback", None, [CAD_OverlayRenderFn, _c.c_void_p])
_n.bind("CAD_SetOverlayInputCallback", None, [CAD_OverlayInputFn, _c.c_void_p])


def CAD_SetOverlayRenderCallback(callback: Callable | None, user: int | None) -> None:
    """C: void CAD_SetOverlayRenderCallback( CAD_OverlayRenderFn callback, void* user)
    """
    _cb_callback = _n.callback(CAD_OverlayRenderFn, callback, ())
    _n.keep("CAD_SetOverlayRenderCallback.callback", _cb_callback, replace=True)
    _f.CAD_SetOverlayRenderCallback(_cb_callback, user)


def CAD_SetOverlayInputCallback(callback: Callable | None, user: int | None) -> None:
    """C: void CAD_SetOverlayInputCallback( CAD_OverlayInputFn callback, void* user)
    """
    _cb_callback = _n.callback(CAD_OverlayInputFn, callback, ())
    _n.keep("CAD_SetOverlayInputCallback.callback", _cb_callback, replace=True)
    _f.CAD_SetOverlayInputCallback(_cb_callback, user)
