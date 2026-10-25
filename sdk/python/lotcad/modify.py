# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Modify 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_LENGTHEN_DELTA', 'CAD_LENGTHEN_PERCENT', 'CAD_LENGTHEN_TOTAL', 'CAD_StretchWindowXY', 'CAD_Lengthen', 'CAD_BreakObject', 'CAD_Align3D', 'CAD_Offset', 'CAD_Trim', 'CAD_Extend']

_f = _n.native

CAD_LENGTHEN_DELTA = 0
CAD_LENGTHEN_PERCENT = 1
CAD_LENGTHEN_TOTAL = 2

_n.bind("CAD_StretchWindowXY", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, CAD_GeVec3])
_n.bind("CAD_Lengthen", _c.c_int32, [_c.c_uint32, _c.c_int32, _c.c_double, _c.c_bool])
_n.bind("CAD_BreakObject", _c.c_int32, [_c.c_uint32, CAD_GeVec3, CAD_GeVec3, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_Align3D", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.POINTER(CAD_GeVec3), _c.POINTER(CAD_GeVec3), _c.c_uint32])
_n.bind("CAD_Offset", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_double, CAD_GeVec3, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_Trim", _c.c_int32, [_c.c_uint32, CAD_GeVec3, _c.POINTER(_c.c_uint32), _c.c_uint32, CAD_GeVec3, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_Extend", _c.c_int32, [_c.c_uint32, CAD_GeVec3, _c.POINTER(_c.c_uint32), _c.c_uint32, CAD_GeVec3, _c.POINTER(_c.c_uint32), _c.c_uint32])


def CAD_StretchWindowXY(corner1: CAD_GeVec3, corner2: CAD_GeVec3, offset: CAD_GeVec3) -> int:
    """C: int32_t CAD_StretchWindowXY(CAD_GeVec3 corner1, CAD_GeVec3 corner2, CAD_GeVec3 offset)

    늘이기(STRETCH) — 교차 창(corner1·corner2 의 월드 x·y, z 는 안 봄 — 평면도용) 안에 든 편집점만 offset 만큼.
    반환 = 걸린 객체 수(0 = 창에 걸린 것 없음 — 오류 아님). 고를 수 없는 객체(숨김·잠긴 도면층)는 건너뛴다.
    """
    return _f.CAD_StretchWindowXY(corner1, corner2, offset)


def CAD_Lengthen(id: int, mode: int, value: float, atStart: bool) -> int:
    """C: CAD_Status CAD_Lengthen(uint32_t id, int32_t mode, double value, bool atStart)

    그 밖의 종류 CAD_E_WRONG_TYPE, 길이가 0 이하가 되거나 호가 한 바퀴를 넘으면 CAD_E_OUT_OF_RANGE.
    """
    return _f.CAD_Lengthen(id, mode, value, atStart)


def CAD_BreakObject(id: int, point1: CAD_GeVec3, point2: CAD_GeVec3, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_BreakObject(uint32_t id, CAD_GeVec3 point1, CAD_GeVec3 point2, uint32_t* outIds, uint32_t capacity)

    끊기(BREAK) — 두 점(곡선 위로 투영) 사이를 지운다. 같은 점이면 그 자리에서 둘로 나눈다(원·닫힌 폴리선은 두 점이어야).
    선·폴리선·원·호. 반환 = 남은 조각 수, outIds = 그 id(원본은 지워진다).
    """
    return _f.CAD_BreakObject(id, point1, point2, outIds, capacity)


def CAD_Align3D(ids: Sequence | None, count: int, source: Sequence | None, target: Sequence | None, pairs: int) -> int:
    """C: int32_t CAD_Align3D(const uint32_t* ids, uint32_t count, const CAD_GeVec3* source, const CAD_GeVec3* target, uint32_t pairs)

    3D 정렬(3DALIGN) — ids 를 점 쌍 pairs 개(1~3)로: 1 = 옮기기, 2 = 방향 맞추기(최단 회전), 3 = 방향까지(틀 맞춤).
    source·target = pairs 개씩. 반환 = 옮긴 객체 수. 하나라도 없거나 잠겼으면 아무것도 안 옮긴다.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    _a_source = _n.array(CAD_GeVec3, source)
    _a_target = _n.array(CAD_GeVec3, target)
    return _f.CAD_Align3D(_a_ids, count, _a_source, _a_target, pairs)


def CAD_Offset(ids: Sequence | None, count: int, distance: float, sidePoint: CAD_GeVec3, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_Offset(const uint32_t* ids, uint32_t count, double distance, CAD_GeVec3 sidePoint, uint32_t* outIds, uint32_t capacity)

    오프셋(OFFSET) — 선·원·호·폴리선을 distance(> 0) 만큼 sidePoint 쪽으로 평행 복제. 반환 = 새로 만든 개수.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_Offset(_a_ids, count, distance, sidePoint, outIds, capacity)


def CAD_Trim(id: int, pickPoint: CAD_GeVec3, boundaryIds: Sequence | None, boundaryCount: int, planeNormal: CAD_GeVec3, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_Trim(uint32_t id, CAD_GeVec3 pickPoint, const uint32_t* boundaryIds, uint32_t boundaryCount, CAD_GeVec3 planeNormal, uint32_t* outIds, uint32_t capacity)

    자르기(TRIM)·연장(EXTEND) — 대상 하나. pickPoint = 지울 부분 / 늘릴 끝 가까운 점. 경계 = boundaryIds(0 개 = 장면의 선·폴리선 전부).
    원·호는 제 평면에서, 선·폴리선은 planeNormal(0,0,0 = 지금 작업 평면)에 투영해 교차. 원본은 지워지고 결과 조각이 새 id 로.
    반환 = 결과 조각 수(자르기는 0 = 통째로 지움), 교차가 없어 못 하면 CAD_E_FAILED(아무것도 안 바뀜).
    """
    _a_boundaryIds = _n.array(_c.c_uint32, boundaryIds)
    return _f.CAD_Trim(id, pickPoint, _a_boundaryIds, boundaryCount, planeNormal, outIds, capacity)


def CAD_Extend(id: int, pickPoint: CAD_GeVec3, boundaryIds: Sequence | None, boundaryCount: int, planeNormal: CAD_GeVec3, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_Extend(uint32_t id, CAD_GeVec3 pickPoint, const uint32_t* boundaryIds, uint32_t boundaryCount, CAD_GeVec3 planeNormal, uint32_t* outIds, uint32_t capacity)

    자르기(TRIM)·연장(EXTEND) — 대상 하나. pickPoint = 지울 부분 / 늘릴 끝 가까운 점. 경계 = boundaryIds(0 개 = 장면의 선·폴리선 전부).
    원·호는 제 평면에서, 선·폴리선은 planeNormal(0,0,0 = 지금 작업 평면)에 투영해 교차. 원본은 지워지고 결과 조각이 새 id 로.
    반환 = 결과 조각 수(자르기는 0 = 통째로 지움), 교차가 없어 못 하면 CAD_E_FAILED(아무것도 안 바뀜).
    """
    _a_boundaryIds = _n.array(_c.c_uint32, boundaryIds)
    return _f.CAD_Extend(id, pickPoint, _a_boundaryIds, boundaryCount, planeNormal, outIds, capacity)
