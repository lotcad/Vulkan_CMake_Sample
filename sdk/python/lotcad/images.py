# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Images 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_AttachImageFromFile', 'CAD_AttachImageFromMemory']

_f = _n.native

_n.bind("CAD_AttachImageFromFile", _c.c_uint32, [_c.c_char_p, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_AttachImageFromMemory", _c.c_uint32, [_c.POINTER(_c.c_ubyte), _c.c_int, _c.c_int, _c.c_char_p, _c.c_float, _c.c_float, _c.c_float, _c.c_float])


def CAD_AttachImageFromFile(pathUtf8: str | None, widthWorld: float, originX: float, originY: float, originZ: float) -> int:
    """C: uint32_t CAD_AttachImageFromFile(const char* pathUtf8, float widthWorld, float originX, float originY, float originZ)

    이미지 붙이기

    도면 밑에 깔 이미지(평면도 사진 등)를 XY 평면에 붙인다.
    엔진의 imageattach 명령은 **파일 대화상자를 띄우므로 모바일에서 못 쓴다** —
    호스트가 사진 앱(PHPicker / Intent)에서 고른 뒤 여기로 넘긴다.

      FromFile   : 경로로. 데스크톱·모바일 공통.
      FromMemory : RGBA8 픽셀을 직접. 사진 앱이 경로 대신 데이터를 주는 경우
                   (iOS PHPicker 가 그렇다) 파일로 떨구지 않고 바로 넘길 수 있다.

    widthWorld = 0 이면 긴 변이 10 단위가 되게 자동. 종횡비는 항상 보존한다.
    반환: 만들어진 객체 id (실패 0).
    """
    return _f.CAD_AttachImageFromFile(_n.text(pathUtf8), widthWorld, originX, originY, originZ)


def CAD_AttachImageFromMemory(rgba: Sequence | None, width: int, height: int, displayName: str | None, widthWorld: float, originX: float, originY: float, originZ: float) -> int:
    """C: uint32_t CAD_AttachImageFromMemory(const unsigned char* rgba, int width, int height, const char* displayName, float widthWorld, float originX, float originY, float originZ)
    """
    _a_rgba = _n.array(_c.c_ubyte, rgba)
    return _f.CAD_AttachImageFromMemory(_a_rgba, width, height, _n.text(displayName), widthWorld, originX, originY, originZ)
