# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Curves 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_SKETCH_WHOLE_ENTITY', 'CAD_SKETCH_COINCIDENT', 'CAD_SKETCH_HORIZONTAL', 'CAD_SKETCH_VERTICAL', 'CAD_SKETCH_CONCENTRIC', 'CAD_SKETCH_DISTANCE', 'CAD_SKETCH_RADIUS', 'CAD_SKETCH_DIAMETER', 'CAD_SKETCH_PARALLEL', 'CAD_SKETCH_PERPENDICULAR', 'CAD_SKETCH_EQUAL', 'CAD_SKETCH_FIXED', 'CAD_SKETCH_ANGLE', 'CAD_SKETCH_TANGENT', 'CAD_SKETCH_DISTANCE_X', 'CAD_SKETCH_DISTANCE_Y', 'CAD_SKETCH_UNDER', 'CAD_SKETCH_WELL', 'CAD_SKETCH_REDUNDANT', 'CAD_SKETCH_CONFLICT', 'CAD_SKETCH_INVALID', 'CAD_CreateLine', 'CAD_CreateCircle', 'CAD_AddSketchConstraint', 'CAD_SetSketchConstraintValue', 'CAD_RemoveSketchConstraint', 'CAD_SolveSketchConstraints', 'CAD_GetSketchConstraintCount', 'CAD_GetSketchConstraintIds', 'CAD_GetSketchConstraintInfo', 'CAD_GetSketchDiagnosis', 'CAD_GetLastSketchConflict', 'CAD_CreatePolygon', 'CAD_CreateArc', 'CAD_CreatePolyline', 'CAD_CreateRectangle', 'CAD_GetPolylinePoints', 'CAD_SetPolylinePoints', 'CAD_CreateEllipse', 'CAD_CreateSpline', 'CAD_CurveGetGeCurve', 'CAD_CurveSetFromGeCurve', 'CAD_CreateCurveFromGe', 'CAD_CurveGetInterval', 'CAD_CurveIsClosed', 'CAD_CurveEvaluate', 'CAD_CurveParamAtPoint', 'CAD_CurveLength', 'CAD_CurveParamAtLength', 'CAD_CurveClosestPoint', 'CAD_CurveArea', 'CAD_CurveIntersect', 'CAD_CurveOffset', 'CAD_CurveSplit', 'CAD_CurveReverse', 'CAD_CurveExtendToPoint']

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

_n.bind("CAD_CreateLine", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateCircle", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
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
_n.bind("CAD_GetPolylinePoints", _c.c_uint32, [_c.c_uint32, _c.POINTER(_c.c_float), _c.c_uint32, _c.POINTER(_c.c_bool)])
_n.bind("CAD_SetPolylinePoints", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.c_uint32, _c.c_bool])
_n.bind("CAD_CreateEllipse", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateSpline", _c.c_uint32, [_c.POINTER(_c.c_float), _c.c_uint32, _c.c_bool])
_n.bind("CAD_CurveGetGeCurve", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_CurveSetFromGeCurve", _c.c_int32, [_c.c_uint32, _c.c_uint64])
_n.bind("CAD_CreateCurveFromGe", _c.c_int32, [_c.c_uint64, _c.POINTER(CAD_CurveCreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CurveGetInterval", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_double), _c.POINTER(_c.c_double)])
_n.bind("CAD_CurveIsClosed", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_bool)])
_n.bind("CAD_CurveEvaluate", _c.c_int32, [_c.c_uint32, _c.c_double, _c.POINTER(CAD_GeVec3), _c.POINTER(CAD_GeVec3), _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_CurveParamAtPoint", _c.c_int32, [_c.c_uint32, CAD_GeVec3, _c.POINTER(_c.c_double)])
_n.bind("CAD_CurveLength", _c.c_int32, [_c.c_uint32, _c.c_double, _c.c_double, _c.POINTER(_c.c_double)])
_n.bind("CAD_CurveParamAtLength", _c.c_int32, [_c.c_uint32, _c.c_double, _c.c_double, _c.POINTER(_c.c_double)])
_n.bind("CAD_CurveClosestPoint", _c.c_int32, [_c.c_uint32, CAD_GeVec3, _c.c_bool, _c.POINTER(_c.c_double), _c.POINTER(CAD_GeVec3), _c.POINTER(_c.c_double)])
_n.bind("CAD_CurveArea", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_double)])
_n.bind("CAD_CurveIntersect", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.c_int, CAD_GeVec3, _c.POINTER(CAD_GeIntersection), _c.c_uint32])
_n.bind("CAD_CurveOffset", _c.c_int32, [_c.c_uint32, _c.c_double, CAD_GeVec3, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_CurveSplit", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_double), _c.c_uint32, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_CurveReverse", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_CurveExtendToPoint", _c.c_int32, [_c.c_uint32, _c.c_bool, CAD_GeVec3])


def CAD_CreateLine(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> int:
    """C: uint32_t CAD_CreateLine(float x1, float y1, float z1, float x2, float y2, float z2)
    """
    return _f.CAD_CreateLine(x1, y1, z1, x2, y2, z2)


def CAD_CreateCircle(cx: float, cy: float, cz: float, radius: float, normalX: float, normalY: float, normalZ: float) -> int:
    """C: uint32_t CAD_CreateCircle(float cx, float cy, float cz, float radius, float normalX, float normalY, float normalZ)
    """
    return _f.CAD_CreateCircle(cx, cy, cz, radius, normalX, normalY, normalZ)


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

    반환=필요한 전체 개수. outIds/capacity가 작으면 앞부분만 복사한다.
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


def CAD_GetPolylinePoints(id: int, outXyz: Any, cap: int) -> tuple[int, bool]:
    """C: uint32_t CAD_GetPolylinePoints(uint32_t id, float* outXyz, uint32_t cap, bool* outClosed)

    닫기·열기·반전·정점 삽입/삭제는 전부 "정점 목록을 바꾸는 일" 이라, 하위 명령마다
    함수를 늘리는 대신 목록을 통째로 읽고 쓰게 한다. 호스트가 받아서 고쳐 되돌려주면 된다.

    uint32_t n = CAD_GetPolylinePoints(id, NULL, 0, NULL);   // 개수 질의
    float* buf = malloc(n * 3 * sizeof(float));
    bool closed = false;
    CAD_GetPolylinePoints(id, buf, n, &closed);
    ... 고친 뒤 ...
    CAD_SetPolylinePoints(id, buf, n, closed);               // undo 1스텝으로 적재

    xyz 는 3 × count 개 float. 좌표는 객체 로컬 (그립/스케치와 같은 공간).
    Set 은 정점이 2개 미만이면 실패. Polyline 이 아닌 객체는 0 / false.
    """
    outClosed = _c.c_bool()
    _r = _f.CAD_GetPolylinePoints(id, outXyz, cap, _c.byref(outClosed))
    return (_r, outClosed.value)


def CAD_SetPolylinePoints(id: int, xyz: Sequence | None, count: int, closed: bool) -> bool:
    """C: bool CAD_SetPolylinePoints(uint32_t id, const float* xyz, uint32_t count, bool closed)

    닫기·열기·반전·정점 삽입/삭제는 전부 "정점 목록을 바꾸는 일" 이라, 하위 명령마다
    함수를 늘리는 대신 목록을 통째로 읽고 쓰게 한다. 호스트가 받아서 고쳐 되돌려주면 된다.

    uint32_t n = CAD_GetPolylinePoints(id, NULL, 0, NULL);   // 개수 질의
    float* buf = malloc(n * 3 * sizeof(float));
    bool closed = false;
    CAD_GetPolylinePoints(id, buf, n, &closed);
    ... 고친 뒤 ...
    CAD_SetPolylinePoints(id, buf, n, closed);               // undo 1스텝으로 적재

    xyz 는 3 × count 개 float. 좌표는 객체 로컬 (그립/스케치와 같은 공간).
    Set 은 정점이 2개 미만이면 실패. Polyline 이 아닌 객체는 0 / false.
    """
    _a_xyz = _n.array(_c.c_float, xyz)
    return _f.CAD_SetPolylinePoints(id, _a_xyz, count, closed)


def CAD_CreateEllipse(cx: float, cy: float, cz: float, majorX: float, majorY: float, majorZ: float, ratio: float, normalX: float, normalY: float, normalZ: float) -> int:
    """C: uint32_t CAD_CreateEllipse(float cx, float cy, float cz, float majorX, float majorY, float majorZ, float ratio, float normalX, float normalY, float normalZ)

    타원 — 중심, 장축 반벡터(중심→장축 끝, 길이 = 장반경), 단축비(0<ratio≤1), 평면 법선(0,0,0 이면 +Z). 실패 0.
    """
    return _f.CAD_CreateEllipse(cx, cy, cz, majorX, majorY, majorZ, ratio, normalX, normalY, normalZ)


def CAD_CreateSpline(fitXYZ: Sequence | None, count: int, closed: bool) -> int:
    """C: uint32_t CAD_CreateSpline(const float* fitXYZ, uint32_t count, bool closed)

    맞춤점을 지나는 스플라인 — fitXYZ = count*3, closed = 닫힌(주기) 스플라인. 열린 것은 2점, 닫힌 것은 3점 이상. 실패 0.
    """
    _a_fitXYZ = _n.array(_c.c_float, fitXYZ)
    return _f.CAD_CreateSpline(_a_fitXYZ, count, closed)


def CAD_CurveGetGeCurve(id: int) -> tuple[int, int]:
    """C: CAD_Status CAD_CurveGetGeCurve(uint32_t id, uint64_t* outCurve)

    객체의 곡선을 기하 곡선 핸들로(getAcGeCurve) — 여기서 CAD_GeCurve* 를 다 쓸 수 있다. 다 쓰면 CAD_GeCurveFree
    """
    outCurve = _c.c_uint64()
    _r = _f.CAD_CurveGetGeCurve(id, _c.byref(outCurve))
    return (_r, outCurve.value)


def CAD_CurveSetFromGeCurve(id: int, curve: int) -> int:
    """C: CAD_Status CAD_CurveSetFromGeCurve(uint32_t id, uint64_t curve)

    객체의 모양을 기하 곡선으로 바꾼다(setFromAcGeCurve) — 같은 종류만: 선 ← 직선, 원 ← 한 바퀴 원호, 호 ← 원호, 타원 ← 타원호,
    스플라인 ← NURBS, 폴리선 ← 직선 조각 폴리선. 아니면 CAD_E_WRONG_TYPE. id·도면층·색은 그대로, 되돌리기 1. 잠긴 도면층 = CAD_E_LOCKED
    """
    return _f.CAD_CurveSetFromGeCurve(id, curve)


def CAD_CreateCurveFromGe(curve: int, opt: CAD_CurveCreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateCurveFromGe(uint64_t curve, const CAD_CurveCreateOptions* opt, uint32_t* outId)

    기하 곡선으로 새 객체 — 직선 = 선, 원호 = 원·호, 타원호 = 타원, NURBS = 스플라인, 합성 곡선 = 폴리선
    (엔진 폴리선은 직선 조각만이라 합성 곡선 안 호·타원·NURBS 조각은 원 분할 규칙으로 꺾은선이 된다). 되돌리기 1
    """
    if opt is None and fields:
        opt = CAD_CurveCreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CurveCreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateCurveFromGe(curve, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CurveGetInterval(id: int) -> tuple[int, float, float]:
    """C: CAD_Status CAD_CurveGetInterval(uint32_t id, double* outStartParam, double* outEndParam)

    매개변수 구간 — getStartParam·getEndParam
    """
    outStartParam = _c.c_double()
    outEndParam = _c.c_double()
    _r = _f.CAD_CurveGetInterval(id, _c.byref(outStartParam), _c.byref(outEndParam))
    return (_r, outStartParam.value, outEndParam.value)


def CAD_CurveIsClosed(id: int) -> tuple[int, bool]:
    """C: CAD_Status CAD_CurveIsClosed(uint32_t id, bool* outClosed)

    isClosed

    묶음 주석: 매개변수 구간 — getStartParam·getEndParam
    """
    outClosed = _c.c_bool()
    _r = _f.CAD_CurveIsClosed(id, _c.byref(outClosed))
    return (_r, outClosed.value)


def CAD_CurveEvaluate(id: int, param: float) -> tuple[int, CAD_GeVec3, CAD_GeVec3, CAD_GeVec3]:
    """C: CAD_Status CAD_CurveEvaluate(uint32_t id, double param, CAD_GeVec3* outPoint, CAD_GeVec3* outFirstDeriv, CAD_GeVec3* outSecondDeriv)

    점·1차·2차 도함수 — getPointAtParam·getFirstDeriv·getSecondDeriv
    """
    outPoint = CAD_GeVec3()
    outFirstDeriv = CAD_GeVec3()
    outSecondDeriv = CAD_GeVec3()
    _r = _f.CAD_CurveEvaluate(id, param, _c.byref(outPoint), _c.byref(outFirstDeriv), _c.byref(outSecondDeriv))
    return (_r, outPoint, outFirstDeriv, outSecondDeriv)


def CAD_CurveParamAtPoint(id: int, p: CAD_GeVec3) -> tuple[int, float]:
    """C: CAD_Status CAD_CurveParamAtPoint(uint32_t id, CAD_GeVec3 p, double* outParam)

    곡선 위 점의 매개변수(허용치 밖 = CAD_E_NOT_ON_CURVE) — getParamAtPoint
    """
    outParam = _c.c_double()
    _r = _f.CAD_CurveParamAtPoint(id, p, _c.byref(outParam))
    return (_r, outParam.value)


def CAD_CurveLength(id: int, fromParam: float, toParam: float) -> tuple[int, float]:
    """C: CAD_Status CAD_CurveLength(uint32_t id, double fromParam, double toParam, double* outLength)

    두 매개변수 사이 길이 — getDistAtParam(fromParam = 시작). 구간 밖 = CAD_E_OUT_OF_RANGE
    """
    outLength = _c.c_double()
    _r = _f.CAD_CurveLength(id, fromParam, toParam, _c.byref(outLength))
    return (_r, outLength.value)


def CAD_CurveParamAtLength(id: int, fromParam: float, length: float) -> tuple[int, float]:
    """C: CAD_Status CAD_CurveParamAtLength(uint32_t id, double fromParam, double length, double* outParam)

    fromParam 에서 곡선을 따라 length(음수 = 거꾸로) 간 곳 — getParamAtDist. 끝을 넘으면 끝에서 멈춤
    """
    outParam = _c.c_double()
    _r = _f.CAD_CurveParamAtLength(id, fromParam, length, _c.byref(outParam))
    return (_r, outParam.value)


def CAD_CurveClosestPoint(id: int, p: CAD_GeVec3, extend: bool) -> tuple[int, float, CAD_GeVec3, float]:
    """C: CAD_Status CAD_CurveClosestPoint(uint32_t id, CAD_GeVec3 p, bool extend, double* outParam, CAD_GeVec3* outPoint, double* outDistance)

    가장 가까운 점 — getClosestPointTo(pt, extend). outDistance = 그 거리
    """
    outParam = _c.c_double()
    outPoint = CAD_GeVec3()
    outDistance = _c.c_double()
    _r = _f.CAD_CurveClosestPoint(id, p, extend, _c.byref(outParam), _c.byref(outPoint), _c.byref(outDistance))
    return (_r, outParam.value, outPoint, outDistance.value)


def CAD_CurveArea(id: int) -> tuple[int, float]:
    """C: CAD_Status CAD_CurveArea(uint32_t id, double* outArea)

    닫힌 평면 곡선 넓이 — getArea. 열림 = CAD_E_NOT_CLOSED, 비평면 = CAD_E_NOT_PLANAR
    """
    outArea = _c.c_double()
    _r = _f.CAD_CurveArea(id, _c.byref(outArea))
    return (_r, outArea.value)


def CAD_CurveIntersect(id1: int, id2: int, extendMode: int, viewDir: CAD_GeVec3, outHits: Any, capacity: int) -> int:
    """C: int32_t CAD_CurveIntersect(uint32_t id1, uint32_t id2, int extendMode, CAD_GeVec3 viewDir, CAD_GeIntersection* outHits, uint32_t capacity)

    두 곡선 객체의 교차 — intersectWith. extendMode = CAD_GE_EXTEND_*, viewDir ≠ 0 이면 그 방향으로 본 교차. 결과는 id1 매개변수 순
    """
    return _f.CAD_CurveIntersect(id1, id2, extendMode, viewDir, outHits, capacity)


def CAD_CurveOffset(id: int, distance: float, planeNormal: CAD_GeVec3, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_CurveOffset(uint32_t id, double distance, CAD_GeVec3 planeNormal, uint32_t* outIds, uint32_t capacity)

    오프셋 곡선을 새 객체로 — getOffsetCurvesGivenPlaneNormal(CAD_GeCurveOffset 과 같은 규칙: distance > 0 = 진행 방향 오른쪽).
    새 객체는 원본의 도면층·색·선종류를 이어받고 원본은 그대로, 전부 되돌리기 1. 반환 = 만든(만들) 개수 — 칸이 모자라면 아무것도 안 만든다
    """
    return _f.CAD_CurveOffset(id, distance, planeNormal, outIds, capacity)


def CAD_CurveSplit(id: int, params: Sequence | None, count: int, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_CurveSplit(uint32_t id, const double* params, uint32_t count, uint32_t* outIds, uint32_t capacity)

    매개변수들에서 나눈 조각을 새 객체로 — getSplitCurves(CAD_GeCurveSplit 과 같은 규칙). 원본은 그대로(지우려면 따로), 되돌리기 1.
    반환 = 조각 수 — 칸이 모자라면 아무것도 안 만든다
    """
    _a_params = _n.array(_c.c_double, params)
    return _f.CAD_CurveSplit(id, _a_params, count, outIds, capacity)


def CAD_CurveReverse(id: int) -> int:
    """C: CAD_Status CAD_CurveReverse(uint32_t id)

    방향 뒤집기 — reverseCurve, 되돌리기 1

    묶음 주석: 매개변수들에서 나눈 조각을 새 객체로 — getSplitCurves(CAD_GeCurveSplit 과 같은 규칙). 원본은 그대로(지우려면 따로), 되돌리기 1.
    반환 = 조각 수 — 칸이 모자라면 아무것도 안 만든다
    """
    return _f.CAD_CurveReverse(id)


def CAD_CurveExtendToPoint(id: int, atStart: bool, toPoint: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_CurveExtendToPoint(uint32_t id, bool atStart, CAD_GeVec3 toPoint)

    끝을 경로 위 점까지 늘인다 — extend(fromStart, toPoint). 선·호·타원·폴리선(끝 조각이 선), 되돌리기 1
    """
    return _f.CAD_CurveExtendToPoint(id, atStart, toPoint)
