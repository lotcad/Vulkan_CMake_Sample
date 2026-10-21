# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — SketchConstraints 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_SKETCH_WHOLE_ENTITY', 'CAD_SKETCH_COINCIDENT', 'CAD_SKETCH_HORIZONTAL', 'CAD_SKETCH_VERTICAL', 'CAD_SKETCH_CONCENTRIC', 'CAD_SKETCH_DISTANCE', 'CAD_SKETCH_RADIUS', 'CAD_SKETCH_DIAMETER', 'CAD_SKETCH_PARALLEL', 'CAD_SKETCH_PERPENDICULAR', 'CAD_SKETCH_EQUAL', 'CAD_SKETCH_FIXED', 'CAD_SKETCH_ANGLE', 'CAD_SKETCH_TANGENT', 'CAD_SKETCH_DISTANCE_X', 'CAD_SKETCH_DISTANCE_Y', 'CAD_SKETCH_UNDER', 'CAD_SKETCH_WELL', 'CAD_SKETCH_REDUNDANT', 'CAD_SKETCH_CONFLICT', 'CAD_SKETCH_INVALID', 'CAD_AddSketchConstraint', 'CAD_SetSketchConstraintValue', 'CAD_RemoveSketchConstraint', 'CAD_SolveSketchConstraints', 'CAD_GetSketchConstraintCount', 'CAD_GetSketchConstraintIds', 'CAD_GetSketchConstraintInfo', 'CAD_GetSketchDiagnosis', 'CAD_GetLastSketchConflict', 'CAD_CreatePolygon', 'CAD_CreateArc', 'CAD_CreatePolyline', 'CAD_CreateRectangle', 'CAD_CreateExtrude', 'CAD_DeleteObject', 'CAD_SelectObject', 'CAD_ClearSelection', 'CAD_GetObjectCount', 'CAD_GetPosition', 'CAD_SetPosition', 'CAD_GetScale', 'CAD_SetScale', 'CAD_GetRotationAxisAngle', 'CAD_SetRotationAxisAngle']

_f = _n.native

CAD_SKETCH_WHOLE_ENTITY = 255
CAD_SKETCH_COINCIDENT = 0
CAD_SKETCH_HORIZONTAL = 1
CAD_SKETCH_VERTICAL = 2
CAD_SKETCH_CONCENTRIC = 3
CAD_SKETCH_DISTANCE = 4
CAD_SKETCH_RADIUS = 5
CAD_SKETCH_DIAMETER = 6
CAD_SKETCH_PARALLEL = 7
CAD_SKETCH_PERPENDICULAR = 8
CAD_SKETCH_EQUAL = 9
CAD_SKETCH_FIXED = 10
CAD_SKETCH_ANGLE = 11
CAD_SKETCH_TANGENT = 12
CAD_SKETCH_DISTANCE_X = 13
CAD_SKETCH_DISTANCE_Y = 14
CAD_SKETCH_UNDER = 0
CAD_SKETCH_WELL = 1
CAD_SKETCH_REDUNDANT = 2
CAD_SKETCH_CONFLICT = 3
CAD_SKETCH_INVALID = 4

_n.bind("CAD_AddSketchConstraint", _c.c_uint32, [_c.c_int, _c.c_uint32, _c.c_int, _c.c_uint32, _c.c_int, _c.c_float])
_n.bind("CAD_SetSketchConstraintValue", _c.c_bool, [_c.c_uint32, _c.c_float])
_n.bind("CAD_RemoveSketchConstraint", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_SolveSketchConstraints", _c.c_bool, [])
_n.bind("CAD_GetSketchConstraintCount", _c.c_uint32, [])
_n.bind("CAD_GetSketchConstraintIds", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_GetSketchConstraintInfo", _c.c_bool, [_c.c_uint32, _c.POINTER(CAD_SketchConstraintInfo)])
_n.bind("CAD_GetSketchDiagnosis", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_int), _c.POINTER(_c.c_int), _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_GetLastSketchConflict", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_CreatePolygon", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_int, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateArc", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreatePolyline", _c.c_uint32, [_c.POINTER(_c.c_float), _c.c_uint32, _c.c_bool])
_n.bind("CAD_CreateRectangle", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateExtrude", _c.c_uint32, [_c.c_uint32, _c.c_float])
_n.bind("CAD_DeleteObject", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_SelectObject", _c.c_bool, [_c.c_uint32, _c.c_bool])
_n.bind("CAD_ClearSelection", None, [])
_n.bind("CAD_GetObjectCount", _c.c_uint32, [])
_n.bind("CAD_GetPosition", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float)])
_n.bind("CAD_SetPosition", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_GetScale", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float)])
_n.bind("CAD_SetScale", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_GetRotationAxisAngle", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float)])
_n.bind("CAD_SetRotationAxisAngle", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.c_float])


def CAD_AddSketchConstraint(type: int, entityA: int, pointA: int, entityB: int, pointB: int, value: float) -> int:
    """C: uint32_t CAD_AddSketchConstraint(int type, uint32_t entityA, int pointA, uint32_t entityB, int pointB, float value)
    """
    return _f.CAD_AddSketchConstraint(type, entityA, pointA, entityB, pointB, value)


def CAD_SetSketchConstraintValue(constraintId: int, value: float) -> bool:
    """C: bool CAD_SetSketchConstraintValue(uint32_t constraintId, float value)
    """
    return _f.CAD_SetSketchConstraintValue(constraintId, value)


def CAD_RemoveSketchConstraint(constraintId: int) -> bool:
    """C: bool CAD_RemoveSketchConstraint(uint32_t constraintId)
    """
    return _f.CAD_RemoveSketchConstraint(constraintId)


def CAD_SolveSketchConstraints() -> bool:
    """C: bool CAD_SolveSketchConstraints(void)
    """
    return _f.CAD_SolveSketchConstraints()


def CAD_GetSketchConstraintCount() -> int:
    """C: uint32_t CAD_GetSketchConstraintCount(void)
    """
    return _f.CAD_GetSketchConstraintCount()


def CAD_GetSketchConstraintIds(outIds: Any, capacity: int) -> int:
    """C: uint32_t CAD_GetSketchConstraintIds(uint32_t* outIds, uint32_t capacity)

    반환=필요한 전체 개수. outIds/capacity가 작으면 앞부분만 복사한다.
    """
    return _f.CAD_GetSketchConstraintIds(outIds, capacity)


def CAD_GetSketchConstraintInfo(constraintId: int) -> CAD_SketchConstraintInfo | None:
    """C: bool CAD_GetSketchConstraintInfo(uint32_t constraintId, CAD_SketchConstraintInfo* outInfo)
    """
    outInfo = CAD_SketchConstraintInfo()
    if not _f.CAD_GetSketchConstraintInfo(constraintId, _c.byref(outInfo)):
        return None
    return outInfo


def CAD_GetSketchDiagnosis(entityId: int, outProblemIds: Any, capacity: int) -> tuple[int, int, int]:
    """C: int CAD_GetSketchDiagnosis(uint32_t entityId, int* outDof, int* outStatus, uint32_t* outProblemIds, uint32_t capacity)

    이 선·원과 제약으로 이어진 묶음의 자유도·구속 상태. 형상은 바꾸지 않는다.
    outProblemIds 에는 충돌(또는 중복) 제약 id — 반환 = 필요한 전체 개수, capacity 만큼만 복사. 실패 시 -1.
    """
    outDof = _c.c_int()
    outStatus = _c.c_int()
    _r = _f.CAD_GetSketchDiagnosis(entityId, _c.byref(outDof), _c.byref(outStatus), outProblemIds, capacity)
    return (_r, outDof.value, outStatus.value)


def CAD_GetLastSketchConflict(outIds: Any, capacity: int) -> int:
    """C: uint32_t CAD_GetLastSketchConflict(uint32_t* outIds, uint32_t capacity)

    마지막 제약 추가·값 편집이 충돌로 실패했을 때 부딪친 제약 id 들. 반환 = 전체 개수.
    """
    return _f.CAD_GetLastSketchConflict(outIds, capacity)


def CAD_CreatePolygon(cx: float, cy: float, cz: float, radius: float, sides: int, normalX: float, normalY: float, normalZ: float, firstVertexDirX: float, firstVertexDirY: float, firstVertexDirZ: float) -> int:
    """C: uint32_t CAD_CreatePolygon(float cx, float cy, float cz, float radius, int sides, float normalX, float normalY, float normalZ, float firstVertexDirX, float firstVertexDirY, float firstVertexDirZ)
    """
    return _f.CAD_CreatePolygon(cx, cy, cz, radius, sides, normalX, normalY, normalZ, firstVertexDirX, firstVertexDirY, firstVertexDirZ)


def CAD_CreateArc(startX: float, startY: float, startZ: float, throughX: float, throughY: float, throughZ: float, endX: float, endY: float, endZ: float) -> int:
    """C: uint32_t CAD_CreateArc(float startX, float startY, float startZ, float throughX, float throughY, float throughZ, float endX, float endY, float endZ)
    """
    return _f.CAD_CreateArc(startX, startY, startZ, throughX, throughY, throughZ, endX, endY, endZ)


def CAD_CreatePolyline(xyz: Sequence | None, pointCount: int, closed: bool) -> int:
    """C: uint32_t CAD_CreatePolyline(const float* xyz, uint32_t pointCount, bool closed)
    """
    _a_xyz = _n.array(_c.c_float, xyz)
    return _f.CAD_CreatePolyline(_a_xyz, pointCount, closed)


def CAD_CreateRectangle(x0: float, y0: float, z0: float, x2: float, y2: float, z2: float) -> int:
    """C: uint32_t CAD_CreateRectangle(float x0, float y0, float z0, float x2, float y2, float z2)
    """
    return _f.CAD_CreateRectangle(x0, y0, z0, x2, y2, z2)


def CAD_CreateExtrude(sourceId: int, height: float) -> int:
    """C: uint32_t CAD_CreateExtrude(uint32_t sourceId, float height)
    """
    return _f.CAD_CreateExtrude(sourceId, height)


def CAD_DeleteObject(id: int) -> bool:
    """C: bool CAD_DeleteObject(uint32_t id)
    """
    return _f.CAD_DeleteObject(id)


def CAD_SelectObject(id: int, additive: bool) -> bool:
    """C: bool CAD_SelectObject(uint32_t id, bool additive)
    """
    return _f.CAD_SelectObject(id, additive)


def CAD_ClearSelection() -> None:
    """C: void CAD_ClearSelection(void)
    """
    _f.CAD_ClearSelection()


def CAD_GetObjectCount() -> int:
    """C: uint32_t CAD_GetObjectCount(void)
    """
    return _f.CAD_GetObjectCount()


def CAD_GetPosition(id: int) -> tuple[float, float, float] | None:
    """C: bool CAD_GetPosition(uint32_t id, float* x, float* y, float* z)
    """
    x = _c.c_float()
    y = _c.c_float()
    z = _c.c_float()
    if not _f.CAD_GetPosition(id, _c.byref(x), _c.byref(y), _c.byref(z)):
        return None
    return (x.value, y.value, z.value)


def CAD_SetPosition(id: int, x: float, y: float, z: float) -> bool:
    """C: bool CAD_SetPosition(uint32_t id, float x, float y, float z)
    """
    return _f.CAD_SetPosition(id, x, y, z)


def CAD_GetScale(id: int) -> tuple[float, float, float] | None:
    """C: bool CAD_GetScale(uint32_t id, float* sx, float* sy, float* sz)
    """
    sx = _c.c_float()
    sy = _c.c_float()
    sz = _c.c_float()
    if not _f.CAD_GetScale(id, _c.byref(sx), _c.byref(sy), _c.byref(sz)):
        return None
    return (sx.value, sy.value, sz.value)


def CAD_SetScale(id: int, sx: float, sy: float, sz: float) -> bool:
    """C: bool CAD_SetScale(uint32_t id, float sx, float sy, float sz)
    """
    return _f.CAD_SetScale(id, sx, sy, sz)


def CAD_GetRotationAxisAngle(id: int) -> tuple[float, float, float, float] | None:
    """C: bool CAD_GetRotationAxisAngle(uint32_t id, float* axisX, float* axisY, float* axisZ, float* angleRadians)
    """
    axisX = _c.c_float()
    axisY = _c.c_float()
    axisZ = _c.c_float()
    angleRadians = _c.c_float()
    if not _f.CAD_GetRotationAxisAngle(id, _c.byref(axisX), _c.byref(axisY), _c.byref(axisZ), _c.byref(angleRadians)):
        return None
    return (axisX.value, axisY.value, axisZ.value, angleRadians.value)


def CAD_SetRotationAxisAngle(id: int, axisX: float, axisY: float, axisZ: float, angleRadians: float) -> bool:
    """C: bool CAD_SetRotationAxisAngle(uint32_t id, float axisX, float axisY, float axisZ, float angleRadians)
    """
    return _f.CAD_SetRotationAxisAngle(id, axisX, axisY, axisZ, angleRadians)
