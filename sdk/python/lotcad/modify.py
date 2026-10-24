# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Modify 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_RequestMoveSelected', 'CAD_RequestRotateSelected', 'CAD_RequestScaleSelected', 'CAD_RequestCopySelected', 'CAD_RequestColorSelected', 'CAD_Explode', 'CAD_ArrayRect', 'CAD_ArrayPolar', 'CAD_StretchWindowXY', 'CAD_Lengthen', 'CAD_BreakObject', 'CAD_Array3DRect', 'CAD_Array3DPolar', 'CAD_Align3D', 'CAD_Offset', 'CAD_Mirror', 'CAD_Trim', 'CAD_Extend']

_f = _n.native

_n.bind("CAD_RequestMoveSelected", None, [_c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_RequestRotateSelected", None, [_c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_RequestScaleSelected", None, [_c.c_float])
_n.bind("CAD_RequestCopySelected", None, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_int])
_n.bind("CAD_RequestColorSelected", None, [_c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_Explode", _c.c_bool, [_c.c_bool])
_n.bind("CAD_ArrayRect", _c.c_bool, [_c.c_int, _c.c_int, _c.c_float, _c.c_float])
_n.bind("CAD_ArrayPolar", _c.c_bool, [_c.c_int, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_bool])
_n.bind("CAD_StretchWindowXY", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_Lengthen", _c.c_bool, [_c.c_uint32, _c.c_int, _c.c_float, _c.c_bool])
_n.bind("CAD_BreakObject", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_Array3DRect", _c.c_bool, [_c.c_int, _c.c_int, _c.c_int, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_Array3DPolar", _c.c_bool, [_c.c_int, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_bool])
_n.bind("CAD_Align3D", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.c_int])
_n.bind("CAD_Offset", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_Mirror", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_bool, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_Trim", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_Extend", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_float, _c.c_float, _c.c_float])


def CAD_RequestMoveSelected(dirX: float, dirY: float, dirZ: float, distance: float) -> None:
    """C: void CAD_RequestMoveSelected(float dirX, float dirY, float dirZ, float distance)
    """
    _f.CAD_RequestMoveSelected(dirX, dirY, dirZ, distance)


def CAD_RequestRotateSelected(axisX: float, axisY: float, axisZ: float, angleDeg: float) -> None:
    """C: void CAD_RequestRotateSelected(float axisX, float axisY, float axisZ, float angleDeg)
    """
    _f.CAD_RequestRotateSelected(axisX, axisY, axisZ, angleDeg)


def CAD_RequestScaleSelected(factor: float) -> None:
    """C: void CAD_RequestScaleSelected(float factor)
    """
    _f.CAD_RequestScaleSelected(factor)


def CAD_RequestCopySelected(dirX: float, dirY: float, dirZ: float, distance: float, count: int) -> None:
    """C: void CAD_RequestCopySelected(float dirX, float dirY, float dirZ, float distance, int count)
    """
    _f.CAD_RequestCopySelected(dirX, dirY, dirZ, distance, count)


def CAD_RequestColorSelected(r: float, g: float, b: float) -> None:
    """C: void CAD_RequestColorSelected(float r, float g, float b)
    """
    _f.CAD_RequestColorSelected(r, g, b)


def CAD_Explode(keepOriginal: bool) -> bool:
    """C: bool CAD_Explode(bool keepOriginal)

    분해(EXPLODE) — 선택 객체를 구성 요소로 쪼갠다.
    문자                → 글리프 윤곽선 폴리선
    폴리선/사각형/다각형 → 개별 선분 (닫힌 도형은 마지막↔첫 정점 구간까지)
    선·원·호는 더 쪼갤 수 없어 그대로 남는다. keepOriginal=true 면 원본을 지우지 않는다.
    여러 종류가 섞여 있어도 undo 는 한 번이다. 쪼갤 것이 하나도 없으면 false.
    """
    return _f.CAD_Explode(keepOriginal)


def CAD_ArrayRect(cols: int, rows: int, dx: float, dy: float) -> bool:
    """C: bool CAD_ArrayRect(int cols, int rows, float dx, float dy)

    직사각형 배열 — cols(가로 개수) × rows(세로 개수), dx/dy 간격(음수 = 반대 방향).
    원본이 (0,0) 칸을 차지하므로 실제 생성 개수는 cols*rows-1.
    평면은 활성 뷰에서 정해진다 (Top=XY, Front=XZ, Right=YZ).
    """
    return _f.CAD_ArrayRect(cols, rows, dx, dy)


def CAD_ArrayPolar(count: int, angleDeg: float, centerX: float, centerY: float, centerZ: float, rotateItems: bool) -> bool:
    """C: bool CAD_ArrayPolar(int count, float angleDeg, float centerX, float centerY, float centerZ, bool rotateItems)

    원형 배열 — count = **원본 포함** 총 개수, angleDeg = 총 채움 각(360 = 한 바퀴).
    center = 회전 중심(월드), rotateItems=false 면 항목 방향을 유지한 채 위치만 옮긴다.
    회전축은 활성 뷰의 평면 법선이다.
    """
    return _f.CAD_ArrayPolar(count, angleDeg, centerX, centerY, centerZ, rotateItems)


def CAD_StretchWindowXY(minX: float, minY: float, maxX: float, maxY: float, dx: float, dy: float, dz: float) -> int:
    """C: uint32_t CAD_StretchWindowXY(float minX, float minY, float maxX, float maxY, float dx, float dy, float dz)

    늘이기 — XY 교차 창(월드) 안의 편집점을 (dx,dy,dz) 만큼. 창 판정은 z 를 보지 않는다. 반환 = 걸린 객체 수.
    """
    return _f.CAD_StretchWindowXY(minX, minY, maxX, maxY, dx, dy, dz)


def CAD_Lengthen(id: int, mode: int, value: float, atStart: bool) -> bool:
    """C: bool CAD_Lengthen(uint32_t id, int mode, float value, bool atStart)

    길이조정 — mode 0 = 증분, 1 = 퍼센트, 2 = 전체 길이. atStart = 시작 쪽 끝. 선·열린 폴리선·호.
    """
    return _f.CAD_Lengthen(id, mode, value, atStart)


def CAD_BreakObject(id: int, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> bool:
    """C: bool CAD_BreakObject(uint32_t id, float x1, float y1, float z1, float x2, float y2, float z2)

    끊기 — 두 점(객체 위로 투영) 사이를 지운다. 같은 점이면 둘로 나눈다. 결과는 새 객체들(원본 삭제).
    """
    return _f.CAD_BreakObject(id, x1, y1, z1, x2, y2, z2)


def CAD_Array3DRect(cols: int, rows: int, levels: int, dx: float, dy: float, dz: float) -> bool:
    """C: bool CAD_Array3DRect(int cols, int rows, int levels, float dx, float dy, float dz)

    3D 배열 — 현재 선택을 월드 X(열)·Y(행)·Z(층) 격자로. 생성 = cols*rows*levels - 1.
    """
    return _f.CAD_Array3DRect(cols, rows, levels, dx, dy, dz)


def CAD_Array3DPolar(count: int, angleDeg: float, ax: float, ay: float, az: float, bx: float, by: float, bz: float, rotateItems: bool) -> bool:
    """C: bool CAD_Array3DPolar(int count, float angleDeg, float ax, float ay, float az, float bx, float by, float bz, bool rotateItems)

    3D 원형 배열 — 현재 선택을 두 점(a→b) 축 둘레로. count = 원본 포함 총 개수.
    """
    return _f.CAD_Array3DPolar(count, angleDeg, ax, ay, az, bx, by, bz, rotateItems)


def CAD_Align3D(ids: Sequence | None, count: int, srcXYZ: Sequence | None, dstXYZ: Sequence | None, pairs: int) -> int:
    """C: uint32_t CAD_Align3D(const uint32_t* ids, uint32_t count, const float* srcXYZ, const float* dstXYZ, int pairs)

    3D 정렬 — ids 를 점 pairs 쌍(1~3)으로. src/dst = pairs*3. 1 = 이동, 2 = 방향, 3 = 방향까지. 반환 = 옮긴 객체 수.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    _a_srcXYZ = _n.array(_c.c_float, srcXYZ)
    _a_dstXYZ = _n.array(_c.c_float, dstXYZ)
    return _f.CAD_Align3D(_a_ids, count, _a_srcXYZ, _a_dstXYZ, pairs)


def CAD_Offset(ids: Sequence | None, count: int, distance: float, sx: float, sy: float, sz: float, outIds: Any, outCapacity: int) -> int:
    """C: uint32_t CAD_Offset(const uint32_t* ids, uint32_t count, float distance, float sx, float sy, float sz, uint32_t* outIds, uint32_t outCapacity)

    오프셋·대칭·자르기·연장 — 클릭 대신 점을 값으로(도구와 같은 계산, 전부 undo 1). 좌표는 월드.
    outIds/outCapacity 는 새 객체 id 받을 곳(null 이면 안 받음). 반환 = 새로 만든 개수.
      CAD_Offset : 선·원·호·폴리선을 distance(>0) 만큼 (sx,sy,sz) 쪽으로 평행 복제.
      CAD_Mirror : 미러선 (x1..z1)→(x2..z2) 과 작업 평면 법선 (nx,ny,nz)(0,0,0 = 지금 작업 평면)이 이루는 면으로 반사 복제.
                   선·원·호·폴리선·메시. deleteOriginals = 원본 지움.
      CAD_Trim / CAD_Extend : 대상 하나, (px,py,pz) = 지울 부분 / 늘릴 끝 가까운 점. 경계 ids(0개 = 씬의 선·폴리선 전부).
                   원·호는 제 평면, 선·폴리선은 (nx,ny,nz)(0 = 지금 작업 평면)에 투영해 교차. 못 하면 false(변화 없음).
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_Offset(_a_ids, count, distance, sx, sy, sz, outIds, outCapacity)


def CAD_Mirror(ids: Sequence | None, count: int, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, nx: float, ny: float, nz: float, deleteOriginals: bool, outIds: Any, outCapacity: int) -> int:
    """C: uint32_t CAD_Mirror(const uint32_t* ids, uint32_t count, float x1, float y1, float z1, float x2, float y2, float z2, float nx, float ny, float nz, bool deleteOriginals, uint32_t* outIds, uint32_t outCapacity)

    오프셋·대칭·자르기·연장 — 클릭 대신 점을 값으로(도구와 같은 계산, 전부 undo 1). 좌표는 월드.
    outIds/outCapacity 는 새 객체 id 받을 곳(null 이면 안 받음). 반환 = 새로 만든 개수.
      CAD_Offset : 선·원·호·폴리선을 distance(>0) 만큼 (sx,sy,sz) 쪽으로 평행 복제.
      CAD_Mirror : 미러선 (x1..z1)→(x2..z2) 과 작업 평면 법선 (nx,ny,nz)(0,0,0 = 지금 작업 평면)이 이루는 면으로 반사 복제.
                   선·원·호·폴리선·메시. deleteOriginals = 원본 지움.
      CAD_Trim / CAD_Extend : 대상 하나, (px,py,pz) = 지울 부분 / 늘릴 끝 가까운 점. 경계 ids(0개 = 씬의 선·폴리선 전부).
                   원·호는 제 평면, 선·폴리선은 (nx,ny,nz)(0 = 지금 작업 평면)에 투영해 교차. 못 하면 false(변화 없음).
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_Mirror(_a_ids, count, x1, y1, z1, x2, y2, z2, nx, ny, nz, deleteOriginals, outIds, outCapacity)


def CAD_Trim(id: int, px: float, py: float, pz: float, boundaryIds: Sequence | None, boundaryCount: int, nx: float, ny: float, nz: float) -> bool:
    """C: bool CAD_Trim(uint32_t id, float px, float py, float pz, const uint32_t* boundaryIds, uint32_t boundaryCount, float nx, float ny, float nz)

    오프셋·대칭·자르기·연장 — 클릭 대신 점을 값으로(도구와 같은 계산, 전부 undo 1). 좌표는 월드.
    outIds/outCapacity 는 새 객체 id 받을 곳(null 이면 안 받음). 반환 = 새로 만든 개수.
      CAD_Offset : 선·원·호·폴리선을 distance(>0) 만큼 (sx,sy,sz) 쪽으로 평행 복제.
      CAD_Mirror : 미러선 (x1..z1)→(x2..z2) 과 작업 평면 법선 (nx,ny,nz)(0,0,0 = 지금 작업 평면)이 이루는 면으로 반사 복제.
                   선·원·호·폴리선·메시. deleteOriginals = 원본 지움.
      CAD_Trim / CAD_Extend : 대상 하나, (px,py,pz) = 지울 부분 / 늘릴 끝 가까운 점. 경계 ids(0개 = 씬의 선·폴리선 전부).
                   원·호는 제 평면, 선·폴리선은 (nx,ny,nz)(0 = 지금 작업 평면)에 투영해 교차. 못 하면 false(변화 없음).
    """
    _a_boundaryIds = _n.array(_c.c_uint32, boundaryIds)
    return _f.CAD_Trim(id, px, py, pz, _a_boundaryIds, boundaryCount, nx, ny, nz)


def CAD_Extend(id: int, px: float, py: float, pz: float, boundaryIds: Sequence | None, boundaryCount: int, nx: float, ny: float, nz: float) -> bool:
    """C: bool CAD_Extend(uint32_t id, float px, float py, float pz, const uint32_t* boundaryIds, uint32_t boundaryCount, float nx, float ny, float nz)

    오프셋·대칭·자르기·연장 — 클릭 대신 점을 값으로(도구와 같은 계산, 전부 undo 1). 좌표는 월드.
    outIds/outCapacity 는 새 객체 id 받을 곳(null 이면 안 받음). 반환 = 새로 만든 개수.
      CAD_Offset : 선·원·호·폴리선을 distance(>0) 만큼 (sx,sy,sz) 쪽으로 평행 복제.
      CAD_Mirror : 미러선 (x1..z1)→(x2..z2) 과 작업 평면 법선 (nx,ny,nz)(0,0,0 = 지금 작업 평면)이 이루는 면으로 반사 복제.
                   선·원·호·폴리선·메시. deleteOriginals = 원본 지움.
      CAD_Trim / CAD_Extend : 대상 하나, (px,py,pz) = 지울 부분 / 늘릴 끝 가까운 점. 경계 ids(0개 = 씬의 선·폴리선 전부).
                   원·호는 제 평면, 선·폴리선은 (nx,ny,nz)(0 = 지금 작업 평면)에 투영해 교차. 못 하면 false(변화 없음).
    """
    _a_boundaryIds = _n.array(_c.c_uint32, boundaryIds)
    return _f.CAD_Extend(id, px, py, pz, _a_boundaryIds, boundaryCount, nx, ny, nz)
