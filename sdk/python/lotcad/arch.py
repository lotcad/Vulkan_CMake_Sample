# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Arch 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_OPENING_DOOR', 'CAD_OPENING_WINDOW', 'CAD_WALL_SOUTH', 'CAD_WALL_NORTH', 'CAD_WALL_WEST', 'CAD_WALL_EAST', 'CAD_OPENING_CENTER', 'CAD_OPENING_START', 'CAD_OPENING_END', 'CAD_CreateRoom', 'CAD_CreateFloorplan', 'CAD_FloorplanExtractFromImage', 'CAD_FloorplanExtractFromRgba', 'CAD_CreateWallGraph', 'CAD_CreateFloorplanFromImage']

_f = _n.native

CAD_OPENING_DOOR = 0
CAD_OPENING_WINDOW = 1
CAD_WALL_SOUTH = 0
CAD_WALL_NORTH = 1
CAD_WALL_WEST = 2
CAD_WALL_EAST = 3
CAD_OPENING_CENTER = 0
CAD_OPENING_START = 1
CAD_OPENING_END = 2

_n.bind("CAD_CreateRoom", _c.c_int32, [CAD_GeVec3, _c.c_double, _c.c_double, _c.c_double, _c.c_double, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateFloorplan", _c.c_int32, [_c.c_double, _c.POINTER(_c.c_double), _c.c_uint32, _c.c_double, _c.c_double, _c.POINTER(CAD_FloorplanOpeningDesc), _c.c_uint32, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_FloorplanExtractFromImage", _c.c_int32, [_c.c_char_p, _c.c_double, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_FloorplanExtractFromRgba", _c.c_int32, [_c.POINTER(_c.c_ubyte), _c.c_int32, _c.c_int32, _c.c_double, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_CreateWallGraph", _c.c_int32, [_c.c_double, _c.POINTER(_c.c_double), _c.c_uint32, _c.c_double, _c.c_double, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_CreateFloorplanFromImage", _c.c_int32, [_c.c_char_p, _c.c_double, _c.c_double, _c.c_bool, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32), _c.c_uint32])


def CAD_CreateRoom(floorCenter: CAD_GeVec3, width: float, depth: float, height: float, wallThickness: float, outWallIds: Any, opt: CAD_CreateOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_CreateRoom(CAD_GeVec3 floorCenter, double width, double depth, double height, double wallThickness, const CAD_CreateOptions* opt, uint32_t* outWallIds)

    방 하나 — floorCenter = 바닥 가운데, width·depth = 안쪽 크기, 모두 > 0. outWallIds = 4칸(NULL 가능), 차례 남·북·서·동
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_CreateRoom(floorCenter, width, depth, height, wallThickness, _p_opt, outWallIds)


def CAD_CreateFloorplan(baseZ: float, rectBounds: Sequence | None, spaceCount: int, height: float, wallThickness: float, openings: Sequence | None, openingCount: int, outWallIds: Any, capacity: int, opt: CAD_CreateOptions | None = None, **fields) -> int:
    """C: int32_t CAD_CreateFloorplan(double baseZ, const double* rectBounds, uint32_t spaceCount, double height, double wallThickness, const CAD_FloorplanOpeningDesc* openings, uint32_t openingCount, const CAD_CreateOptions* opt, uint32_t* outWallIds, uint32_t capacity)

    평면도 — rectBounds = 방마다 [minX,minY,maxX,maxY](월드 XY) × spaceCount, 맞닿은 벽은 하나로. 문·창은 openings(없으면 NULL, 0).
    반환 = 만든 벽 조각 수(개구부를 뺀 뒤), outWallIds 에 capacity 개까지. 방·종류·쪽·맞춤 번호 범위 밖 = CAD_E_OUT_OF_RANGE
    """
    _a_rectBounds = _n.array(_c.c_double, rectBounds)
    _a_openings = _n.array(CAD_FloorplanOpeningDesc, openings)
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_CreateFloorplan(baseZ, _a_rectBounds, spaceCount, height, wallThickness, _a_openings, openingCount, _p_opt, outWallIds, capacity)


def CAD_FloorplanExtractFromImage(path: str | None, widthMm: float) -> str | None:
    """C: int32_t CAD_FloorplanExtractFromImage(const char* path, double widthMm, char* buf, uint32_t capacity)

    추출은 장면을 바꾸지 않는다. widthMm = 도면 전체 폭(벽 중심선, mm), 0 이면 문 폭 900mm 로 축척 추정.
    출력 JSON(mm, 좌하단 원점·Y 위): {"widthMm","depthMm","walls":[{"x1","y1","x2","y2","thicknessMm","exterior"}],
    "outerThicknessMm","innerThicknessMm","scaleEstimated","doorCount","imageWidthMm","imageOrigin":[x,y],"summary"}
    — imageWidthMm/imageOrigin = 이미지 **전체**의 실폭·좌하단(바닥에 깔 때). 반환 = 전체 길이. 벽 없음·못 읽음 = CAD_E_FAILED + 이유
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_FloorplanExtractFromImage(_n.text(path), widthMm, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_FloorplanExtractFromRgba(rgba: Sequence | None, width: int, height: int, widthMm: float) -> str | None:
    """C: int32_t CAD_FloorplanExtractFromRgba(const unsigned char* rgba, int32_t width, int32_t height, double widthMm, char* buf, uint32_t capacity)

    rgba = 4바이트 × width × height(행 우선, 위에서 아래) — 모바일 카메라·사진 선택기용.
    """
    _a_rgba = _n.array(_c.c_ubyte, rgba)
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_FloorplanExtractFromRgba(_a_rgba, width, height, widthMm, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_CreateWallGraph(baseZ: float, segments: Sequence | None, count: int, height: float, defaultThickness: float, outIds: Any, capacity: int, opt: CAD_CreateOptions | None = None, **fields) -> int:
    """C: int32_t CAD_CreateWallGraph(double baseZ, const double* segments, uint32_t count, double height, double defaultThickness, const CAD_CreateOptions* opt, uint32_t* outIds, uint32_t capacity)

    벽 그래프 → 3D 벽. segments = [x1,y1,x2,y2,thickness](월드 XY, m) × count, 축에 나란한 벽만. thickness <= 0 이면 defaultThickness.
    반환 = 만든 벽 수, outIds 에 capacity 개까지
    """
    _a_segments = _n.array(_c.c_double, segments)
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_CreateWallGraph(baseZ, _a_segments, count, height, defaultThickness, _p_opt, outIds, capacity)


def CAD_CreateFloorplanFromImage(path: str | None, widthMm: float, height: float, underlayImage: bool, outIds: Any, capacity: int, opt: CAD_CreateOptions | None = None, **fields) -> int:
    """C: int32_t CAD_CreateFloorplanFromImage(const char* path, double widthMm, double height, bool underlayImage, const CAD_CreateOptions* opt, uint32_t* outIds, uint32_t capacity)

    편의 — 이미지에서 벽을 찾아 m 로 세우고, underlayImage 면 원본을 같은 축척으로 바닥에(AI create_wall_graph 와 같음).
    반환 = 만든 벽 수(바닥 이미지는 outIds 에 안 들어감 — 되돌리기는 함께)
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_CreateFloorplanFromImage(_n.text(path), widthMm, height, underlayImage, _p_opt, outIds, capacity)
