# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Arch 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_CreateRoom', 'CAD_CreateFloorplan', 'CAD_CreateFloorplanWithOpenings', 'CAD_FloorplanExtractFromImage', 'CAD_FloorplanExtractFromRgba', 'CAD_CreateWallGraph', 'CAD_CreateFloorplanFromImage']

_f = _n.native

_n.bind("CAD_CreateRoom", _c.c_bool, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateFloorplan", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.POINTER(_c.c_float), _c.c_uint32, _c.c_float, _c.c_float, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_CreateFloorplanWithOpenings", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.POINTER(_c.c_float), _c.c_uint32, _c.c_float, _c.c_float, _c.POINTER(CAD_FloorplanOpeningDesc), _c.c_uint32, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_FloorplanExtractFromImage", _c.c_int, [_c.c_char_p, _c.c_float, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_FloorplanExtractFromRgba", _c.c_int, [_c.POINTER(_c.c_ubyte), _c.c_int, _c.c_int, _c.c_float, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_CreateWallGraph", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.POINTER(_c.c_float), _c.c_uint32, _c.c_float, _c.c_float, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_CreateFloorplanFromImage", _c.c_uint32, [_c.c_char_p, _c.c_float, _c.c_float, _c.c_bool, _c.POINTER(_c.c_uint32), _c.c_uint32])


def CAD_CreateRoom(originX: float, originY: float, originZ: float, width: float, depth: float, height: float, wallThickness: float, outWallIds: Any) -> bool:
    """C: bool CAD_CreateRoom(float originX, float originY, float originZ, float width, float depth, float height, float wallThickness, uint32_t* outWallIds)

    origin = floor center; width/depth = interior clear size; all values are metres.
    outWallIds must point to storage for 4 ids. Order: south, north, west, east.
    """
    return _f.CAD_CreateRoom(originX, originY, originZ, width, depth, height, wallThickness, outWallIds)


def CAD_CreateFloorplan(originX: float, originY: float, originZ: float, rectBounds: Sequence | None, spaceCount: int, height: float, wallThickness: float, outWallIds: Any, outCapacity: int) -> int:
    """C: uint32_t CAD_CreateFloorplan(float originX, float originY, float originZ, const float* rectBounds, uint32_t spaceCount, float height, float wallThickness, uint32_t* outWallIds, uint32_t outCapacity)

    rectBounds contains spaceCount groups of [minX,minY,maxX,maxY], local to origin.
    Returns the total number of unique walls created and copies up to outCapacity ids.
    """
    _a_rectBounds = _n.array(_c.c_float, rectBounds)
    return _f.CAD_CreateFloorplan(originX, originY, originZ, _a_rectBounds, spaceCount, height, wallThickness, outWallIds, outCapacity)


def CAD_CreateFloorplanWithOpenings(originX: float, originY: float, originZ: float, rectBounds: Sequence | None, spaceCount: int, height: float, wallThickness: float, openings: Sequence | None, openingCount: int, outWallIds: Any, outCapacity: int) -> int:
    """C: uint32_t CAD_CreateFloorplanWithOpenings( float originX, float originY, float originZ, const float* rectBounds, uint32_t spaceCount, float height, float wallThickness, const CAD_FloorplanOpeningDesc* openings, uint32_t openingCount, uint32_t* outWallIds, uint32_t outCapacity)

    Returns the number of solid wall pieces after openings are removed.
    """
    _a_rectBounds = _n.array(_c.c_float, rectBounds)
    _a_openings = _n.array(CAD_FloorplanOpeningDesc, openings)
    return _f.CAD_CreateFloorplanWithOpenings(originX, originY, originZ, _a_rectBounds, spaceCount, height, wallThickness, _a_openings, openingCount, outWallIds, outCapacity)


def CAD_FloorplanExtractFromImage(path: str | None, widthMm: float) -> str | None:
    """C: int CAD_FloorplanExtractFromImage(const char* path, float widthMm, char* outJson, int cap)

    추출은 장면을 바꾸지 않는다. widthMm = 도면 전체 폭(벽 중심선, mm), 0 이면 문 폭 900mm 로 축척 추정.
    출력 JSON(mm, 좌하단 원점·Y 위): {"widthMm","depthMm","walls":[{"x1","y1","x2","y2","thicknessMm","exterior"}],
    "outerThicknessMm","innerThicknessMm","scaleEstimated","doorCount","imageWidthMm","imageOrigin":[x,y],"summary"}
    — imageWidthMm/imageOrigin = 이미지 **전체**의 실폭·좌하단(바닥에 깔 때). 실패 -1 + CAD_GetLastError. 2회 호출 규약.
    """
    _need = _f.CAD_FloorplanExtractFromImage(_n.text(path), widthMm, None, 0)   # 2회 호출 규약: 길이를 물으며 한 번 실행
    if _need < 0:
        return None
    _cap = _need + 1
    _buf = _c.create_string_buffer(_cap)
    if _f.CAD_FloorplanExtractFromImage(_n.text(path), widthMm, _buf, _cap) < 0:   # 같은 인자 → 다시 실행하지 않고 결과만
        return None
    return _n.decode(_buf.value)


def CAD_FloorplanExtractFromRgba(rgba: Sequence | None, w: int, h: int, widthMm: float) -> str | None:
    """C: int CAD_FloorplanExtractFromRgba(const unsigned char* rgba, int w, int h, float widthMm, char* outJson, int cap)

    rgba = 4바이트 × w × h(행 우선, 위에서 아래) — 모바일 카메라·사진 선택기용.
    """
    _a_rgba = _n.array(_c.c_ubyte, rgba)
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_FloorplanExtractFromRgba(_a_rgba, w, h, widthMm, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_CreateWallGraph(ox: float, oy: float, oz: float, segs: Sequence | None, count: int, height: float, defaultThickness: float, outIds: Any, cap: int) -> int:
    """C: uint32_t CAD_CreateWallGraph(float ox, float oy, float oz, const float* segs, uint32_t count, float height, float defaultThickness, uint32_t* outIds, uint32_t cap)

    벽 그래프 → 3D 벽. segs = [x1,y1,x2,y2,thickness] × count, **단위 m**(CAD_CreateFloorplan 과 같음), 축에 나란한 벽만.
    thickness <= 0 이면 defaultThickness. 반환 = 만든 벽 수, outIds 에 최대 cap 개. undo 1.
    """
    _a_segs = _n.array(_c.c_float, segs)
    return _f.CAD_CreateWallGraph(ox, oy, oz, _a_segs, count, height, defaultThickness, outIds, cap)


def CAD_CreateFloorplanFromImage(path: str | None, widthMm: float, height: float, underlayImage: bool, outIds: Any, cap: int) -> int:
    """C: uint32_t CAD_CreateFloorplanFromImage(const char* path, float widthMm, float height, bool underlayImage, uint32_t* outIds, uint32_t cap)

    편의 — 이미지에서 벽을 찾아 m 로 세우고, underlayImage 면 원본을 같은 축척으로 바닥에(AI create_wall_graph 와 같음).
    """
    return _f.CAD_CreateFloorplanFromImage(_n.text(path), widthMm, height, underlayImage, outIds, cap)
