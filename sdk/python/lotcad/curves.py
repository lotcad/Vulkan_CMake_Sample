# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Curves 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_SKETCH_WHOLE_ENTITY', 'CAD_SKETCH_COINCIDENT', 'CAD_SKETCH_HORIZONTAL', 'CAD_SKETCH_VERTICAL', 'CAD_SKETCH_CONCENTRIC', 'CAD_SKETCH_DISTANCE', 'CAD_SKETCH_RADIUS', 'CAD_SKETCH_DIAMETER', 'CAD_SKETCH_PARALLEL', 'CAD_SKETCH_PERPENDICULAR', 'CAD_SKETCH_EQUAL', 'CAD_SKETCH_FIXED', 'CAD_SKETCH_ANGLE', 'CAD_SKETCH_TANGENT', 'CAD_SKETCH_DISTANCE_X', 'CAD_SKETCH_DISTANCE_Y', 'CAD_SKETCH_UNDER', 'CAD_SKETCH_WELL', 'CAD_SKETCH_REDUNDANT', 'CAD_SKETCH_CONFLICT', 'CAD_SKETCH_INVALID', 'CAD_CreateLine', 'CAD_CreateCircle', 'CAD_CreateArc', 'CAD_CreatePolygon', 'CAD_CreateRectangle', 'CAD_CreatePolyline', 'CAD_CreateEllipse', 'CAD_CreateSpline', 'CAD_GetPolylinePoints', 'CAD_SetPolylinePoints', 'CAD_AddSketchConstraint', 'CAD_SetSketchConstraintValue', 'CAD_RemoveSketchConstraint', 'CAD_SolveSketchConstraints', 'CAD_GetSketchConstraintCount', 'CAD_GetSketchConstraintIds', 'CAD_GetSketchConstraintInfo', 'CAD_GetSketchDiagnosis', 'CAD_GetLastSketchConflict', 'CAD_CurveGetGeCurve', 'CAD_CurveSetFromGeCurve', 'CAD_CreateCurveFromGe', 'CAD_CurveGetInterval', 'CAD_CurveIsClosed', 'CAD_CurveEvaluate', 'CAD_CurveParamAtPoint', 'CAD_CurveLength', 'CAD_CurveParamAtLength', 'CAD_CurveClosestPoint', 'CAD_CurveArea', 'CAD_CurveIntersect', 'CAD_CurveOffset', 'CAD_CurveSplit', 'CAD_CurveReverse', 'CAD_CurveExtendToPoint']

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

_n.bind("CAD_CreateLine", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateCircle", _c.c_int32, [CAD_GeVec3, _c.c_double, CAD_GeVec3, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateArc", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreatePolygon", _c.c_int32, [CAD_GeVec3, _c.c_double, _c.c_int32, CAD_GeVec3, CAD_GeVec3, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateRectangle", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreatePolyline", _c.c_int32, [_c.POINTER(CAD_GeVec3), _c.c_uint32, _c.c_bool, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateEllipse", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, _c.c_double, CAD_GeVec3, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateSpline", _c.c_int32, [_c.POINTER(CAD_GeVec3), _c.c_uint32, _c.c_bool, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_GetPolylinePoints", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_GeVec3), _c.c_uint32, _c.POINTER(_c.c_bool)])
_n.bind("CAD_SetPolylinePoints", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_GeVec3), _c.c_uint32, _c.c_bool])
_n.bind("CAD_AddSketchConstraint", _c.c_int32, [_c.c_int32, _c.c_uint32, _c.c_int32, _c.c_uint32, _c.c_int32, _c.c_double, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetSketchConstraintValue", _c.c_int32, [_c.c_uint32, _c.c_double])
_n.bind("CAD_RemoveSketchConstraint", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_SolveSketchConstraints", _c.c_int32, [])
_n.bind("CAD_GetSketchConstraintCount", _c.c_int32, [])
_n.bind("CAD_GetSketchConstraintIds", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_GetSketchConstraintInfo", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_SketchConstraintInfo)])
_n.bind("CAD_GetSketchDiagnosis", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_int32), _c.POINTER(_c.c_int32), _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_GetLastSketchConflict", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_CurveGetGeCurve", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_CurveSetFromGeCurve", _c.c_int32, [_c.c_uint32, _c.c_uint64])
_n.bind("CAD_CreateCurveFromGe", _c.c_int32, [_c.c_uint64, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
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


def CAD_CreateLine(start: CAD_GeVec3, end: CAD_GeVec3, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateLine(CAD_GeVec3 start, CAD_GeVec3 end, const CAD_CreateOptions* opt, uint32_t* outId)

    만들기 선택 CAD_CreateOptions(도면층·색 이어받기)는 lotcad_types.h — 모든 만들기 함수가 같이 쓴다
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateLine(start, end, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateCircle(center: CAD_GeVec3, radius: float, normal: CAD_GeVec3, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateCircle(CAD_GeVec3 center, double radius, CAD_GeVec3 normal, const CAD_CreateOptions* opt, uint32_t* outId)

    원 — normal = 원이 놓인 평면의 법선
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateCircle(center, radius, normal, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateArc(start: CAD_GeVec3, through: CAD_GeVec3, end: CAD_GeVec3, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateArc(CAD_GeVec3 start, CAD_GeVec3 through, CAD_GeVec3 end, const CAD_CreateOptions* opt, uint32_t* outId)

    세 점 호 — 시작 → 지나는 점 → 끝
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateArc(start, through, end, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreatePolygon(center: CAD_GeVec3, radius: float, sides: int, normal: CAD_GeVec3, firstVertexDir: CAD_GeVec3, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreatePolygon(CAD_GeVec3 center, double radius, int32_t sides, CAD_GeVec3 normal, CAD_GeVec3 firstVertexDir, const CAD_CreateOptions* opt, uint32_t* outId)

    정다각형(닫힌 폴리선) — 꼭짓점이 중심에서 radius(외접원), sides = 3..1024, firstVertexDir = 첫 꼭짓점 방향(평면 안, (0,0,0) = 평면의 첫 축)
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreatePolygon(center, radius, sides, normal, firstVertexDir, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateRectangle(corner0: CAD_GeVec3, corner2: CAD_GeVec3, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateRectangle(CAD_GeVec3 corner0, CAD_GeVec3 corner2, const CAD_CreateOptions* opt, uint32_t* outId)

    사각형(닫힌 폴리선) — 맞모서리 두 점. 두 점이 이루는 축 평면(XY·YZ·XZ)에 놓인다
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateRectangle(corner0, corner2, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreatePolyline(points: Sequence | None, count: int, closed: bool, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreatePolyline(const CAD_GeVec3* points, uint32_t count, bool closed, const CAD_CreateOptions* opt, uint32_t* outId)

    폴리선 — 점 count 개(2 이상), closed = 마지막 → 첫 점까지
    """
    _a_points = _n.array(CAD_GeVec3, points)
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreatePolyline(_a_points, count, closed, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateEllipse(center: CAD_GeVec3, majorAxis: CAD_GeVec3, ratio: float, normal: CAD_GeVec3, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateEllipse(CAD_GeVec3 center, CAD_GeVec3 majorAxis, double ratio, CAD_GeVec3 normal, const CAD_CreateOptions* opt, uint32_t* outId)

    타원 — 중심, 장축 반벡터(중심 → 장축 끝, 길이 = 장반경, 평면 안), 단축비(0 < ratio ≤ 1), 평면 법선
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateEllipse(center, majorAxis, ratio, normal, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateSpline(fitPoints: Sequence | None, count: int, closed: bool, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateSpline(const CAD_GeVec3* fitPoints, uint32_t count, bool closed, const CAD_CreateOptions* opt, uint32_t* outId)

    맞춤점을 지나는 스플라인 — 열린 것은 2점, 닫힌(주기) 것은 3점 이상(최대 100000)
    """
    _a_fitPoints = _n.array(CAD_GeVec3, fitPoints)
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateSpline(_a_fitPoints, count, closed, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_GetPolylinePoints(id: int, outPoints: Any, capacity: int) -> tuple[int, bool]:
    """C: int32_t CAD_GetPolylinePoints(uint32_t id, CAD_GeVec3* outPoints, uint32_t capacity, bool* outClosed)

    폴리선 정점 목록 (PEDIT · AcDbPolyline getPointAt/setPointAt)
    닫기·열기·반전·정점 넣기/빼기는 전부 "정점 목록을 바꾸는 일" 이라 목록을 통째로 읽고 쓴다. 좌표 = **월드** mm(객체의 이동·회전·축척이
    걸린 화면 자리 — 객체 JSON 의 points 와 같다). 폴리선이 아니면 CAD_E_WRONG_TYPE(선·원·호는 CAD_Curve* 로).

      int32_t n = CAD_GetPolylinePoints(id, NULL, 0, NULL);     // 개수
      CAD_GeVec3* p = malloc(sizeof(CAD_GeVec3) * n);
      bool closed = false;
      CAD_GetPolylinePoints(id, p, (uint32_t)n, &closed);
      ... 고친 뒤 ...
      CAD_SetPolylinePoints(id, p, (uint32_t)n, closed);        // 되돌리기 1

    Get 반환 = 정점 수(capacity 만큼만 채움). Set 은 2점 이상, 잠긴 도면층 = CAD_E_LOCKED.
    """
    outClosed = _c.c_bool()
    _r = _f.CAD_GetPolylinePoints(id, outPoints, capacity, _c.byref(outClosed))
    return (_r, outClosed.value)


def CAD_SetPolylinePoints(id: int, points: Sequence | None, count: int, closed: bool) -> int:
    """C: CAD_Status CAD_SetPolylinePoints(uint32_t id, const CAD_GeVec3* points, uint32_t count, bool closed)

    폴리선 정점 목록 (PEDIT · AcDbPolyline getPointAt/setPointAt)
    닫기·열기·반전·정점 넣기/빼기는 전부 "정점 목록을 바꾸는 일" 이라 목록을 통째로 읽고 쓴다. 좌표 = **월드** mm(객체의 이동·회전·축척이
    걸린 화면 자리 — 객체 JSON 의 points 와 같다). 폴리선이 아니면 CAD_E_WRONG_TYPE(선·원·호는 CAD_Curve* 로).

      int32_t n = CAD_GetPolylinePoints(id, NULL, 0, NULL);     // 개수
      CAD_GeVec3* p = malloc(sizeof(CAD_GeVec3) * n);
      bool closed = false;
      CAD_GetPolylinePoints(id, p, (uint32_t)n, &closed);
      ... 고친 뒤 ...
      CAD_SetPolylinePoints(id, p, (uint32_t)n, closed);        // 되돌리기 1

    Get 반환 = 정점 수(capacity 만큼만 채움). Set 은 2점 이상, 잠긴 도면층 = CAD_E_LOCKED.
    """
    _a_points = _n.array(CAD_GeVec3, points)
    return _f.CAD_SetPolylinePoints(id, _a_points, count, closed)


def CAD_AddSketchConstraint(type: int, entityA: int, pointA: int, entityB: int, pointB: int, value: float) -> tuple[int, int]:
    """C: CAD_Status CAD_AddSketchConstraint(int32_t type, uint32_t entityA, int32_t pointA, uint32_t entityB, int32_t pointB, double value, uint32_t* outId)

    제약 더하기 — 바로 풀어 형상을 맞춘다, 되돌리기 1. 같은 제약이 이미 있으면 그 id(CAD_OK).
    없는 객체 = CAD_E_BAD_HANDLE, 잠김 = CAD_E_LOCKED, 선·원 아님 = CAD_E_WRONG_TYPE, 그 종류에 안 맞는 점·값 = CAD_E_INVALID_ARG
    """
    outId = _c.c_uint32()
    _r = _f.CAD_AddSketchConstraint(type, entityA, pointA, entityB, pointB, value, _c.byref(outId))
    return (_r, outId.value)


def CAD_SetSketchConstraintValue(constraintId: int, value: float) -> int:
    """C: CAD_Status CAD_SetSketchConstraintValue(uint32_t constraintId, double value)

    값 바꾸기(거리·반지름·직경 > 0, 각도·가로·세로 거리는 부호 있음) — 값 없는 제약 = CAD_E_WRONG_TYPE, 없는 id = CAD_E_BAD_HANDLE
    """
    return _f.CAD_SetSketchConstraintValue(constraintId, value)


def CAD_RemoveSketchConstraint(constraintId: int) -> int:
    """C: CAD_Status CAD_RemoveSketchConstraint(uint32_t constraintId)

    값 바꾸기(거리·반지름·직경 > 0, 각도·가로·세로 거리는 부호 있음) — 값 없는 제약 = CAD_E_WRONG_TYPE, 없는 id = CAD_E_BAD_HANDLE
    """
    return _f.CAD_RemoveSketchConstraint(constraintId)


def CAD_SolveSketchConstraints() -> int:
    """C: CAD_Status CAD_SolveSketchConstraints(void)

    장면의 제약 전부를 다시 푼다 — 풀 수 없으면 CAD_E_CONFLICT(형상은 그대로)
    """
    return _f.CAD_SolveSketchConstraints()


def CAD_GetSketchConstraintCount() -> int:
    """C: int32_t CAD_GetSketchConstraintCount(void)

    장면의 제약 전부를 다시 푼다 — 풀 수 없으면 CAD_E_CONFLICT(형상은 그대로)
    """
    return _f.CAD_GetSketchConstraintCount()


def CAD_GetSketchConstraintIds(outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_GetSketchConstraintIds(uint32_t* outIds, uint32_t capacity)

    장면의 제약 전부를 다시 푼다 — 풀 수 없으면 CAD_E_CONFLICT(형상은 그대로)
    """
    return _f.CAD_GetSketchConstraintIds(outIds, capacity)


def CAD_GetSketchConstraintInfo(constraintId: int) -> tuple[int, CAD_SketchConstraintInfo]:
    """C: CAD_Status CAD_GetSketchConstraintInfo(uint32_t constraintId, CAD_SketchConstraintInfo* outInfo)

    장면의 제약 전부를 다시 푼다 — 풀 수 없으면 CAD_E_CONFLICT(형상은 그대로)
    """
    outInfo = CAD_SketchConstraintInfo()
    outInfo.size = _c.sizeof(CAD_SketchConstraintInfo)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_GetSketchConstraintInfo(constraintId, _c.byref(outInfo))
    return (_r, outInfo)


def CAD_GetSketchDiagnosis(entityId: int, outProblemIds: Any, capacity: int) -> tuple[int, int, int]:
    """C: int32_t CAD_GetSketchDiagnosis(uint32_t entityId, int32_t* outDof, int32_t* outStatus, uint32_t* outProblemIds, uint32_t capacity)

    이 선·원과 제약으로 이어진 묶음의 자유도·구속 상태(CAD_SKETCH_UNDER …). 형상은 바꾸지 않는다.
    반환 = 문제가 된 제약 수(충돌·잘못된 참조·중복 — 상태에 따라), outProblemIds 에 capacity 만큼
    """
    outDof = _c.c_int32()
    outStatus = _c.c_int32()
    _r = _f.CAD_GetSketchDiagnosis(entityId, _c.byref(outDof), _c.byref(outStatus), outProblemIds, capacity)
    return (_r, outDof.value, outStatus.value)


def CAD_GetLastSketchConflict(outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_GetLastSketchConflict(uint32_t* outIds, uint32_t capacity)

    마지막 더하기·값 바꾸기·풀기가 CAD_E_CONFLICT 였을 때 부딪친 제약 id 들 — 반환 = 전체 개수
    """
    return _f.CAD_GetLastSketchConflict(outIds, capacity)


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


def CAD_CreateCurveFromGe(curve: int, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateCurveFromGe(uint64_t curve, const CAD_CreateOptions* opt, uint32_t* outId)

    기하 곡선으로 새 객체 — 직선 = 선, 원호 = 원·호, 타원호 = 타원, NURBS = 스플라인, 합성 곡선 = 폴리선
    (엔진 폴리선은 직선 조각만이라 합성 곡선 안 호·타원·NURBS 조각은 원 분할 규칙으로 꺾은선이 된다). 되돌리기 1
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
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
