# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Types 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_OK', 'CAD_E_INVALID_ARG', 'CAD_E_BAD_HANDLE', 'CAD_E_NO_ENGINE', 'CAD_E_WRONG_TYPE', 'CAD_E_DEGENERATE', 'CAD_E_PARALLEL', 'CAD_E_NOT_PLANAR', 'CAD_E_NOT_CLOSED', 'CAD_E_NOT_ON_CURVE', 'CAD_E_OUT_OF_RANGE', 'CAD_E_NOT_SUPPORTED', 'CAD_E_FAILED', 'CAD_E_BUFFER_TOO_SMALL', 'CAD_E_NOT_CONNECTED', 'CAD_E_WRONG_THREAD', 'CAD_E_LOCKED', 'CAD_E_BUSY', 'CAD_E_NOT_READY', 'CAD_E_NOT_FOUND', 'CAD_E_DUPLICATE']

_f = _n.native

CAD_OK = 0
CAD_E_INVALID_ARG = -1
CAD_E_BAD_HANDLE = -2
CAD_E_NO_ENGINE = -3
CAD_E_WRONG_TYPE = -4
CAD_E_DEGENERATE = -5
CAD_E_PARALLEL = -6
CAD_E_NOT_PLANAR = -7
CAD_E_NOT_CLOSED = -8
CAD_E_NOT_ON_CURVE = -9
CAD_E_OUT_OF_RANGE = -10
CAD_E_NOT_SUPPORTED = -11
CAD_E_FAILED = -12
CAD_E_BUFFER_TOO_SMALL = -13
CAD_E_NOT_CONNECTED = -14
CAD_E_WRONG_THREAD = -15
CAD_E_LOCKED = -16
CAD_E_BUSY = -17
CAD_E_NOT_READY = -18
CAD_E_NOT_FOUND = -19
CAD_E_DUPLICATE = -20
