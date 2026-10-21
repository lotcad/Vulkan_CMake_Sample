# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Section 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_SetSection', 'CAD_SetSectionBox', 'CAD_SetSectionOptions', 'CAD_GetSectionStateJson', 'CAD_ExtractSectionTo2D']

_f = _n.native

_n.bind("CAD_SetSection", _c.c_bool, [_c.c_int, _c.c_int, _c.c_float, _c.c_bool, _c.c_float])
_n.bind("CAD_SetSectionBox", _c.c_bool, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_SetSectionOptions", None, [_c.c_bool, _c.c_bool])
_n.bind("CAD_GetSectionStateJson", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_ExtractSectionTo2D", _c.c_uint32, [_c.c_bool])


def CAD_SetSection(mode: int, axis: int, pos: float, flip: bool, thickness: float) -> bool:
    """C: bool CAD_SetSection(int mode, int axis, float pos, bool flip, float thickness)

    mode 0 끄기 1 평면(axis 위치 pos 보다 큰 쪽을 자름, flip 이면 반대) 2 슬라이스(pos 중심 thickness 두께만 남김) 3 상자(SetSectionBox).
    axis 0 X 1 Y 2 Z. thickness 는 슬라이스에만(0 이하면 지금 값 유지). 틀린 값 false.
    """
    return _f.CAD_SetSection(mode, axis, pos, flip, thickness)


def CAD_SetSectionBox(minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float) -> bool:
    """C: bool CAD_SetSectionBox(float minX, float minY, float minZ, float maxX, float maxY, float maxZ)

    mode 0 끄기 1 평면(axis 위치 pos 보다 큰 쪽을 자름, flip 이면 반대) 2 슬라이스(pos 중심 thickness 두께만 남김) 3 상자(SetSectionBox).
    axis 0 X 1 Y 2 Z. thickness 는 슬라이스에만(0 이하면 지금 값 유지). 틀린 값 false.
    상자 값만(켜기는 SetSection(3,…))
    """
    return _f.CAD_SetSectionBox(minX, minY, minZ, maxX, maxY, maxZ)


def CAD_SetSectionOptions(showArrows: bool, selectedOnly: bool) -> None:
    """C: void CAD_SetSectionOptions(bool showArrows, bool selectedOnly)

    mode 0 끄기 1 평면(axis 위치 pos 보다 큰 쪽을 자름, flip 이면 반대) 2 슬라이스(pos 중심 thickness 두께만 남김) 3 상자(SetSectionBox).
    axis 0 X 1 Y 2 Z. thickness 는 슬라이스에만(0 이하면 지금 값 유지). 틀린 값 false.
    """
    _f.CAD_SetSectionOptions(showArrows, selectedOnly)


def CAD_GetSectionStateJson() -> str | None:
    """C: int CAD_GetSectionStateJson(char* out, int cap)

    {"mode","modeName","axis","pos","flip","thickness","box":{"min","max"},"showArrows","selectedOnly","sceneBounds":{"min","max"}} — sceneBounds = 슬라이더 범위
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetSectionStateJson(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_ExtractSectionTo2D(includeBehind: bool) -> int:
    """C: uint32_t CAD_ExtractSectionTo2D(bool includeBehind)

    지금 평면 단면 → 2D 윤곽(편집 가능한 폴리선, includeBehind 면 뒤쪽 회색 참조선 1개 더)을 모델 오른쪽 XY 평면에. 반환 = 만든 객체 수, undo 1.
    """
    return _f.CAD_ExtractSectionTo2D(includeBehind)
