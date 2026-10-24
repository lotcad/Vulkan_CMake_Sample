# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Geometry 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_GECURVE_LINE', 'CAD_GECURVE_ARC', 'CAD_GECURVE_ELLIPSE', 'CAD_GECURVE_NURBS', 'CAD_GECURVE_COMPOSITE', 'CAD_GE_EXTEND_NONE', 'CAD_GE_EXTEND_THIS', 'CAD_GE_EXTEND_ARG', 'CAD_GE_EXTEND_BOTH', 'CAD_GEVEC_NONE', 'CAD_GEVEC_CODIRECTIONAL', 'CAD_GEVEC_OPPOSITE', 'CAD_GEVEC_PERPENDICULAR', 'CAD_GEPOS_OUTSIDE', 'CAD_GEPOS_ON', 'CAD_GEPOS_INSIDE', 'CAD_GeSetTolerance', 'CAD_GeGetTolerance', 'CAD_GeVectorAngle', 'CAD_GeVectorRotate', 'CAD_GeVectorPerp', 'CAD_GeVectorRelation', 'CAD_GePointRotate', 'CAD_GePointMirror', 'CAD_GePointProject', 'CAD_GePlaneFrom3Points', 'CAD_GePlaneDistance', 'CAD_GePlaneAxes', 'CAD_GePlaneIntersectLine', 'CAD_GePlaneIntersectPlane', 'CAD_GeLineClosest', 'CAD_GeMatrixIdentity', 'CAD_GeMatrixTranslation', 'CAD_GeMatrixRotation', 'CAD_GeMatrixScaling', 'CAD_GeMatrixMirroring', 'CAD_GeMatrixCoordSys', 'CAD_GeMatrixAlignCoordSys', 'CAD_GeMatrixPlaneToWorld', 'CAD_GeMatrixWorldToPlane', 'CAD_GeMatrixInverse', 'CAD_GeMatrixMultiply', 'CAD_GeTransformPoints', 'CAD_GeTransformVectors', 'CAD_GeCurveCreateLine', 'CAD_GeCurveCreateArc', 'CAD_GeCurveCreateCircle', 'CAD_GeCurveCreateArc3Points', 'CAD_GeCurveCreateArcBulge', 'CAD_GeCurveCreateFillet', 'CAD_GeCurveCreateEllipse', 'CAD_GeCurveCreatePolyline', 'CAD_GeCurveCreatePolylineBulge', 'CAD_GeCurveCreateNurbs', 'CAD_GeCurveCreateInterpolated', 'CAD_GeCurveCreateComposite', 'CAD_GeCurveCopy', 'CAD_GeCurveFree', 'CAD_GeCurveLiveCount', 'CAD_GeCurveGetType', 'CAD_GeCurveGetInterval', 'CAD_GeCurveIsClosed', 'CAD_GeCurveIsPlanar', 'CAD_GeCurveEvaluate', 'CAD_GeCurveEvaluateMany', 'CAD_GeCurveParamAtPoint', 'CAD_GeCurveClosestPoint', 'CAD_GeCurveClosestPointAlong', 'CAD_GeCurvePerpendicularPoints', 'CAD_GeCurveTangentPoints', 'CAD_GeCurveClosestToCurve', 'CAD_GeCurveLength', 'CAD_GeCurveParamAtLength', 'CAD_GeCurveSampleParams', 'CAD_GeCurveGetBox', 'CAD_GeCurveArea', 'CAD_GeCurveContainsPoint', 'CAD_GeCurveGetLine', 'CAD_GeCurveGetArc', 'CAD_GeCurveGetEllipse', 'CAD_GeCurveGetPieceCount', 'CAD_GeCurveGetPiece', 'CAD_GeCurveGetNurbsInfo', 'CAD_GeCurveGetNurbsData', 'CAD_GeCurveToNurbs', 'CAD_GeCurveReverse', 'CAD_GeCurveTransform', 'CAD_GeCurveExtendToPoint', 'CAD_GeCurveExtendToParam', 'CAD_GeCurveSubCurve', 'CAD_GeCurveSplit', 'CAD_GeCurveOffset', 'CAD_GeCurveIntersect', 'CAD_GeCurveIntersectPlane']

_f = _n.native

CAD_GECURVE_LINE = 1
CAD_GECURVE_ARC = 2
CAD_GECURVE_ELLIPSE = 3
CAD_GECURVE_NURBS = 4
CAD_GECURVE_COMPOSITE = 5
CAD_GE_EXTEND_NONE = 0
CAD_GE_EXTEND_THIS = 1
CAD_GE_EXTEND_ARG = 2
CAD_GE_EXTEND_BOTH = 3
CAD_GEVEC_NONE = 0
CAD_GEVEC_CODIRECTIONAL = 1
CAD_GEVEC_OPPOSITE = 2
CAD_GEVEC_PERPENDICULAR = 3
CAD_GEPOS_OUTSIDE = 0
CAD_GEPOS_ON = 1
CAD_GEPOS_INSIDE = 2

_n.bind("CAD_GeSetTolerance", _c.c_int32, [_c.c_double, _c.c_double])
_n.bind("CAD_GeGetTolerance", _c.c_int32, [_c.POINTER(_c.c_double), _c.POINTER(_c.c_double)])
_n.bind("CAD_GeVectorAngle", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, _c.POINTER(_c.c_double)])
_n.bind("CAD_GeVectorRotate", _c.c_int32, [CAD_GeVec3, _c.c_double, CAD_GeVec3, _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_GeVectorPerp", _c.c_int32, [CAD_GeVec3, _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_GeVectorRelation", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, _c.POINTER(_c.c_int)])
_n.bind("CAD_GePointRotate", _c.c_int32, [CAD_GeVec3, _c.c_double, CAD_GeVec3, CAD_GeVec3, _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_GePointMirror", _c.c_int32, [CAD_GeVec3, CAD_GePlane, _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_GePointProject", _c.c_int32, [CAD_GeVec3, CAD_GePlane, CAD_GeVec3, _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_GePlaneFrom3Points", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, _c.POINTER(CAD_GePlane)])
_n.bind("CAD_GePlaneDistance", _c.c_int32, [CAD_GePlane, CAD_GeVec3, _c.POINTER(_c.c_double)])
_n.bind("CAD_GePlaneAxes", _c.c_int32, [CAD_GePlane, _c.POINTER(CAD_GeVec3), _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_GePlaneIntersectLine", _c.c_int32, [CAD_GePlane, CAD_GeVec3, CAD_GeVec3, _c.POINTER(_c.c_double), _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_GePlaneIntersectPlane", _c.c_int32, [CAD_GePlane, CAD_GePlane, _c.POINTER(CAD_GeVec3), _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_GeLineClosest", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, _c.c_bool, CAD_GeVec3, CAD_GeVec3, _c.c_bool, _c.POINTER(_c.c_double), _c.POINTER(_c.c_double), _c.POINTER(CAD_GeVec3), _c.POINTER(CAD_GeVec3), _c.POINTER(_c.c_bool)])
_n.bind("CAD_GeMatrixIdentity", _c.c_int32, [_c.POINTER(CAD_GeMatrix)])
_n.bind("CAD_GeMatrixTranslation", _c.c_int32, [CAD_GeVec3, _c.POINTER(CAD_GeMatrix)])
_n.bind("CAD_GeMatrixRotation", _c.c_int32, [_c.c_double, CAD_GeVec3, CAD_GeVec3, _c.POINTER(CAD_GeMatrix)])
_n.bind("CAD_GeMatrixScaling", _c.c_int32, [_c.c_double, CAD_GeVec3, _c.POINTER(CAD_GeMatrix)])
_n.bind("CAD_GeMatrixMirroring", _c.c_int32, [CAD_GePlane, _c.POINTER(CAD_GeMatrix)])
_n.bind("CAD_GeMatrixCoordSys", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, _c.POINTER(CAD_GeMatrix)])
_n.bind("CAD_GeMatrixAlignCoordSys", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, _c.POINTER(CAD_GeMatrix)])
_n.bind("CAD_GeMatrixPlaneToWorld", _c.c_int32, [CAD_GePlane, _c.POINTER(CAD_GeMatrix)])
_n.bind("CAD_GeMatrixWorldToPlane", _c.c_int32, [CAD_GePlane, _c.POINTER(CAD_GeMatrix)])
_n.bind("CAD_GeMatrixInverse", _c.c_int32, [CAD_GeMatrix, _c.POINTER(CAD_GeMatrix)])
_n.bind("CAD_GeMatrixMultiply", _c.c_int32, [CAD_GeMatrix, CAD_GeMatrix, _c.POINTER(CAD_GeMatrix)])
_n.bind("CAD_GeTransformPoints", _c.c_int32, [CAD_GeMatrix, _c.POINTER(_c.c_double), _c.c_uint32, _c.POINTER(_c.c_double), _c.c_uint32])
_n.bind("CAD_GeTransformVectors", _c.c_int32, [CAD_GeMatrix, _c.POINTER(_c.c_double), _c.c_uint32, _c.POINTER(_c.c_double), _c.c_uint32])
_n.bind("CAD_GeCurveCreateLine", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_GeCurveCreateArc", _c.c_int32, [CAD_GeArc, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_GeCurveCreateCircle", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, _c.c_double, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_GeCurveCreateArc3Points", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_GeCurveCreateArcBulge", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, _c.c_double, CAD_GeVec3, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_GeCurveCreateFillet", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, _c.c_double, _c.POINTER(_c.c_uint64), _c.POINTER(_c.c_double), _c.POINTER(_c.c_double)])
_n.bind("CAD_GeCurveCreateEllipse", _c.c_int32, [CAD_GeEllipse, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_GeCurveCreatePolyline", _c.c_int32, [_c.POINTER(_c.c_double), _c.c_uint32, _c.c_bool, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_GeCurveCreatePolylineBulge", _c.c_int32, [_c.POINTER(_c.c_double), _c.c_uint32, _c.POINTER(_c.c_double), _c.c_uint32, _c.c_bool, CAD_GeVec3, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_GeCurveCreateNurbs", _c.c_int32, [_c.c_int, _c.POINTER(_c.c_double), _c.c_uint32, _c.POINTER(_c.c_double), _c.c_uint32, _c.POINTER(_c.c_double), _c.c_uint32, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_GeCurveCreateInterpolated", _c.c_int32, [_c.POINTER(_c.c_double), _c.c_uint32, _c.c_int, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_GeCurveCreateComposite", _c.c_int32, [_c.POINTER(_c.c_uint64), _c.c_uint32, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_GeCurveCopy", _c.c_int32, [_c.c_uint64, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_GeCurveFree", _c.c_int32, [_c.c_uint64])
_n.bind("CAD_GeCurveLiveCount", _c.c_int32, [])
_n.bind("CAD_GeCurveGetType", _c.c_int32, [_c.c_uint64, _c.POINTER(_c.c_int)])
_n.bind("CAD_GeCurveGetInterval", _c.c_int32, [_c.c_uint64, _c.POINTER(_c.c_double), _c.POINTER(_c.c_double)])
_n.bind("CAD_GeCurveIsClosed", _c.c_int32, [_c.c_uint64, _c.POINTER(_c.c_bool)])
_n.bind("CAD_GeCurveIsPlanar", _c.c_int32, [_c.c_uint64, _c.POINTER(_c.c_bool), _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_GeCurveEvaluate", _c.c_int32, [_c.c_uint64, _c.c_double, _c.POINTER(CAD_GeVec3), _c.POINTER(CAD_GeVec3), _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_GeCurveEvaluateMany", _c.c_int32, [_c.c_uint64, _c.POINTER(_c.c_double), _c.c_uint32, _c.POINTER(_c.c_double), _c.c_uint32])
_n.bind("CAD_GeCurveParamAtPoint", _c.c_int32, [_c.c_uint64, CAD_GeVec3, _c.POINTER(_c.c_double)])
_n.bind("CAD_GeCurveClosestPoint", _c.c_int32, [_c.c_uint64, CAD_GeVec3, _c.c_bool, _c.POINTER(_c.c_double), _c.POINTER(CAD_GeVec3), _c.POINTER(_c.c_double)])
_n.bind("CAD_GeCurveClosestPointAlong", _c.c_int32, [_c.c_uint64, CAD_GeVec3, CAD_GeVec3, _c.c_bool, _c.POINTER(_c.c_double), _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_GeCurvePerpendicularPoints", _c.c_int32, [_c.c_uint64, CAD_GeVec3, _c.c_bool, _c.POINTER(_c.c_double), _c.c_uint32])
_n.bind("CAD_GeCurveTangentPoints", _c.c_int32, [_c.c_uint64, CAD_GeVec3, CAD_GeVec3, _c.POINTER(_c.c_double), _c.c_uint32])
_n.bind("CAD_GeCurveClosestToCurve", _c.c_int32, [_c.c_uint64, _c.c_uint64, _c.POINTER(_c.c_double), _c.POINTER(_c.c_double), _c.POINTER(_c.c_double)])
_n.bind("CAD_GeCurveLength", _c.c_int32, [_c.c_uint64, _c.c_double, _c.c_double, _c.POINTER(_c.c_double)])
_n.bind("CAD_GeCurveParamAtLength", _c.c_int32, [_c.c_uint64, _c.c_double, _c.c_double, _c.POINTER(_c.c_double)])
_n.bind("CAD_GeCurveSampleParams", _c.c_int32, [_c.c_uint64, _c.c_double, _c.POINTER(_c.c_double), _c.c_uint32])
_n.bind("CAD_GeCurveGetBox", _c.c_int32, [_c.c_uint64, _c.POINTER(CAD_GeVec3), _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_GeCurveArea", _c.c_int32, [_c.c_uint64, _c.POINTER(_c.c_double)])
_n.bind("CAD_GeCurveContainsPoint", _c.c_int32, [_c.c_uint64, CAD_GeVec3, _c.POINTER(_c.c_int)])
_n.bind("CAD_GeCurveGetLine", _c.c_int32, [_c.c_uint64, _c.POINTER(CAD_GeVec3), _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_GeCurveGetArc", _c.c_int32, [_c.c_uint64, _c.POINTER(CAD_GeArc)])
_n.bind("CAD_GeCurveGetEllipse", _c.c_int32, [_c.c_uint64, _c.POINTER(CAD_GeEllipse)])
_n.bind("CAD_GeCurveGetPieceCount", _c.c_int32, [_c.c_uint64])
_n.bind("CAD_GeCurveGetPiece", _c.c_int32, [_c.c_uint64, _c.c_uint32, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_GeCurveGetNurbsInfo", _c.c_int32, [_c.c_uint64, _c.POINTER(_c.c_int), _c.POINTER(_c.c_uint32), _c.POINTER(_c.c_uint32), _c.POINTER(_c.c_bool)])
_n.bind("CAD_GeCurveGetNurbsData", _c.c_int32, [_c.c_uint64, _c.POINTER(_c.c_double), _c.c_uint32, _c.POINTER(_c.c_double), _c.c_uint32, _c.POINTER(_c.c_double), _c.c_uint32])
_n.bind("CAD_GeCurveToNurbs", _c.c_int32, [_c.c_uint64, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_GeCurveReverse", _c.c_int32, [_c.c_uint64])
_n.bind("CAD_GeCurveTransform", _c.c_int32, [_c.c_uint64, CAD_GeMatrix])
_n.bind("CAD_GeCurveExtendToPoint", _c.c_int32, [_c.c_uint64, _c.c_bool, CAD_GeVec3])
_n.bind("CAD_GeCurveExtendToParam", _c.c_int32, [_c.c_uint64, _c.c_double])
_n.bind("CAD_GeCurveSubCurve", _c.c_int32, [_c.c_uint64, _c.c_double, _c.c_double, _c.POINTER(_c.c_uint64)])
_n.bind("CAD_GeCurveSplit", _c.c_int32, [_c.c_uint64, _c.POINTER(_c.c_double), _c.c_uint32, _c.POINTER(_c.c_uint64), _c.c_uint32])
_n.bind("CAD_GeCurveOffset", _c.c_int32, [_c.c_uint64, _c.c_double, CAD_GeVec3, _c.POINTER(_c.c_uint64), _c.c_uint32])
_n.bind("CAD_GeCurveIntersect", _c.c_int32, [_c.c_uint64, _c.c_uint64, _c.c_int, CAD_GeVec3, _c.POINTER(CAD_GeIntersection), _c.c_uint32])
_n.bind("CAD_GeCurveIntersectPlane", _c.c_int32, [_c.c_uint64, CAD_GePlane, _c.POINTER(_c.c_double), _c.c_uint32])


def CAD_GeSetTolerance(equalPoint: float, equalVector: float) -> int:
    """C: CAD_Status CAD_GeSetTolerance(double equalPoint, double equalVector)

    허용치(AcGeContext::gTol) — 프로세스 전체(모든 스레드) 한 벌. 기본 점 1e-5 mm, 벡터 1e-10(1 − cos)
    둘 다 > 0(아니면 CAD_E_INVALID_ARG)
    """
    return _f.CAD_GeSetTolerance(equalPoint, equalVector)


def CAD_GeGetTolerance() -> tuple[int, float, float]:
    """C: CAD_Status CAD_GeGetTolerance(double* outEqualPoint, double* outEqualVector)

    지금 허용치

    묶음 주석: 허용치(AcGeContext::gTol) — 프로세스 전체(모든 스레드) 한 벌. 기본 점 1e-5 mm, 벡터 1e-10(1 − cos)
    """
    outEqualPoint = _c.c_double()
    outEqualVector = _c.c_double()
    _r = _f.CAD_GeGetTolerance(_c.byref(outEqualPoint), _c.byref(outEqualVector))
    return (_r, outEqualPoint.value, outEqualVector.value)


def CAD_GeVectorAngle(a: CAD_GeVec3, b: CAD_GeVec3, refAxis: CAD_GeVec3) -> tuple[int, float]:
    """C: CAD_Status CAD_GeVectorAngle(CAD_GeVec3 a, CAD_GeVec3 b, CAD_GeVec3 refAxis, double* outAngle)

    a → b 각. refAxis 가 0 이면 0..π, 아니면 refAxis 둘레 오른손 방향으로 잰 0..2π. 길이 0 = CAD_E_DEGENERATE
    """
    outAngle = _c.c_double()
    _r = _f.CAD_GeVectorAngle(a, b, refAxis, _c.byref(outAngle))
    return (_r, outAngle.value)


def CAD_GeVectorRotate(v: CAD_GeVec3, angle: float, axis: CAD_GeVec3) -> tuple[int, CAD_GeVec3]:
    """C: CAD_Status CAD_GeVectorRotate(CAD_GeVec3 v, double angle, CAD_GeVec3 axis, CAD_GeVec3* outVector)

    axis 둘레 오른손 방향 angle(rad)

    묶음 주석: a → b 각. refAxis 가 0 이면 0..π, 아니면 refAxis 둘레 오른손 방향으로 잰 0..2π. 길이 0 = CAD_E_DEGENERATE
    """
    outVector = CAD_GeVec3()
    _r = _f.CAD_GeVectorRotate(v, angle, axis, _c.byref(outVector))
    return (_r, outVector)


def CAD_GeVectorPerp(v: CAD_GeVec3) -> tuple[int, CAD_GeVec3]:
    """C: CAD_Status CAD_GeVectorPerp(CAD_GeVec3 v, CAD_GeVec3* outVector)

    수직인 단위 벡터(늘 같은 규칙)

    묶음 주석: a → b 각. refAxis 가 0 이면 0..π, 아니면 refAxis 둘레 오른손 방향으로 잰 0..2π. 길이 0 = CAD_E_DEGENERATE
    """
    outVector = CAD_GeVec3()
    _r = _f.CAD_GeVectorPerp(v, _c.byref(outVector))
    return (_r, outVector)


def CAD_GeVectorRelation(a: CAD_GeVec3, b: CAD_GeVec3) -> tuple[int, int]:
    """C: CAD_Status CAD_GeVectorRelation(CAD_GeVec3 a, CAD_GeVec3 b, int* outRelation)

    CAD_GEVEC_* (허용치 = 벡터 허용치)

    묶음 주석: a → b 각. refAxis 가 0 이면 0..π, 아니면 refAxis 둘레 오른손 방향으로 잰 0..2π. 길이 0 = CAD_E_DEGENERATE
    """
    outRelation = _c.c_int()
    _r = _f.CAD_GeVectorRelation(a, b, _c.byref(outRelation))
    return (_r, outRelation.value)


def CAD_GePointRotate(p: CAD_GeVec3, angle: float, axisPoint: CAD_GeVec3, axisDir: CAD_GeVec3) -> tuple[int, CAD_GeVec3]:
    """C: CAD_Status CAD_GePointRotate(CAD_GeVec3 p, double angle, CAD_GeVec3 axisPoint, CAD_GeVec3 axisDir, CAD_GeVec3* outPoint)

    점 p 를 축(axisPoint 를 지나는 axisDir) 둘레로 오른손 방향 angle(rad) 돌린 점
    """
    outPoint = CAD_GeVec3()
    _r = _f.CAD_GePointRotate(p, angle, axisPoint, axisDir, _c.byref(outPoint))
    return (_r, outPoint)


def CAD_GePointMirror(p: CAD_GeVec3, plane: CAD_GePlane) -> tuple[int, CAD_GeVec3]:
    """C: CAD_Status CAD_GePointMirror(CAD_GeVec3 p, CAD_GePlane plane, CAD_GeVec3* outPoint)

    평면에 비친 점

    묶음 주석: 점 p 를 축(axisPoint 를 지나는 axisDir) 둘레로 오른손 방향 angle(rad) 돌린 점
    """
    outPoint = CAD_GeVec3()
    _r = _f.CAD_GePointMirror(p, plane, _c.byref(outPoint))
    return (_r, outPoint)


def CAD_GePointProject(p: CAD_GeVec3, plane: CAD_GePlane, dir: CAD_GeVec3) -> tuple[int, CAD_GeVec3]:
    """C: CAD_Status CAD_GePointProject(CAD_GeVec3 p, CAD_GePlane plane, CAD_GeVec3 dir, CAD_GeVec3* outPoint)

    평면에 투영 — dir 이 0 이면 수직, 아니면 dir 방향으로(dir 이 평면과 나란하면 CAD_E_PARALLEL)
    """
    outPoint = CAD_GeVec3()
    _r = _f.CAD_GePointProject(p, plane, dir, _c.byref(outPoint))
    return (_r, outPoint)


def CAD_GePlaneFrom3Points(a: CAD_GeVec3, b: CAD_GeVec3, c: CAD_GeVec3) -> tuple[int, CAD_GePlane]:
    """C: CAD_Status CAD_GePlaneFrom3Points(CAD_GeVec3 a, CAD_GeVec3 b, CAD_GeVec3 c, CAD_GePlane* outPlane)

    평면 (AcGePlane)
    한 줄 = CAD_E_PARALLEL
    """
    outPlane = CAD_GePlane()
    _r = _f.CAD_GePlaneFrom3Points(a, b, c, _c.byref(outPlane))
    return (_r, outPlane)


def CAD_GePlaneDistance(plane: CAD_GePlane, p: CAD_GeVec3) -> tuple[int, float]:
    """C: CAD_Status CAD_GePlaneDistance(CAD_GePlane plane, CAD_GeVec3 p, double* outSignedDistance)

    법선 쪽 +

    묶음 주석: 평면 (AcGePlane)
    """
    outSignedDistance = _c.c_double()
    _r = _f.CAD_GePlaneDistance(plane, p, _c.byref(outSignedDistance))
    return (_r, outSignedDistance.value)


def CAD_GePlaneAxes(plane: CAD_GePlane) -> tuple[int, CAD_GeVec3, CAD_GeVec3]:
    """C: CAD_Status CAD_GePlaneAxes(CAD_GePlane plane, CAD_GeVec3* outXAxis, CAD_GeVec3* outYAxis)

    평면 안 두 축(법선에 수직, 오른손) — 오토캐드 임의 축 규칙(DXF OCS 와 같다)
    """
    outXAxis = CAD_GeVec3()
    outYAxis = CAD_GeVec3()
    _r = _f.CAD_GePlaneAxes(plane, _c.byref(outXAxis), _c.byref(outYAxis))
    return (_r, outXAxis, outYAxis)


def CAD_GePlaneIntersectLine(plane: CAD_GePlane, linePoint: CAD_GeVec3, lineDir: CAD_GeVec3) -> tuple[int, float, CAD_GeVec3]:
    """C: CAD_Status CAD_GePlaneIntersectLine(CAD_GePlane plane, CAD_GeVec3 linePoint, CAD_GeVec3 lineDir, double* outParam, CAD_GeVec3* outPoint)

    무한 직선(점 + 방향) ∩ 평면 — outParam = 방향 1 당 매개변수. 나란하면 CAD_E_PARALLEL
    """
    outParam = _c.c_double()
    outPoint = CAD_GeVec3()
    _r = _f.CAD_GePlaneIntersectLine(plane, linePoint, lineDir, _c.byref(outParam), _c.byref(outPoint))
    return (_r, outParam.value, outPoint)


def CAD_GePlaneIntersectPlane(a: CAD_GePlane, b: CAD_GePlane) -> tuple[int, CAD_GeVec3, CAD_GeVec3]:
    """C: CAD_Status CAD_GePlaneIntersectPlane(CAD_GePlane a, CAD_GePlane b, CAD_GeVec3* outPoint, CAD_GeVec3* outDir)

    평면 ∩ 평면 = 직선(점 + 단위 방향). 나란하면 CAD_E_PARALLEL
    """
    outPoint = CAD_GeVec3()
    outDir = CAD_GeVec3()
    _r = _f.CAD_GePlaneIntersectPlane(a, b, _c.byref(outPoint), _c.byref(outDir))
    return (_r, outPoint, outDir)


def CAD_GeLineClosest(a0: CAD_GeVec3, a1: CAD_GeVec3, segmentA: bool, b0: CAD_GeVec3, b1: CAD_GeVec3, segmentB: bool) -> tuple[int, float, float, CAD_GeVec3, CAD_GeVec3, bool]:
    """C: CAD_Status CAD_GeLineClosest(CAD_GeVec3 a0, CAD_GeVec3 a1, bool segmentA, CAD_GeVec3 b0, CAD_GeVec3 b1, bool segmentB, double* outParamA, double* outParamB, CAD_GeVec3* outPointA, CAD_GeVec3* outPointB, bool* outParallel)

    두 선의 가장 가까운 두 점 — a0→a1 이 매개변수 0→1. segmentA/B = 선분(0..1 안으로). 두 점이 같으면 교점.
    outParallel = 나란함(그때는 가까운 점 한 쌍을 골라 줌). 길이 0 인 선 = CAD_E_DEGENERATE
    """
    outParamA = _c.c_double()
    outParamB = _c.c_double()
    outPointA = CAD_GeVec3()
    outPointB = CAD_GeVec3()
    outParallel = _c.c_bool()
    _r = _f.CAD_GeLineClosest(a0, a1, segmentA, b0, b1, segmentB, _c.byref(outParamA), _c.byref(outParamB), _c.byref(outPointA), _c.byref(outPointB), _c.byref(outParallel))
    return (_r, outParamA.value, outParamB.value, outPointA, outPointB, outParallel.value)


def CAD_GeMatrixIdentity() -> tuple[int, CAD_GeMatrix]:
    """C: CAD_Status CAD_GeMatrixIdentity(CAD_GeMatrix* outMatrix)

    행렬 (AcGeMatrix3d)
    단위 행렬
    """
    outMatrix = CAD_GeMatrix()
    _r = _f.CAD_GeMatrixIdentity(_c.byref(outMatrix))
    return (_r, outMatrix)


def CAD_GeMatrixTranslation(v: CAD_GeVec3) -> tuple[int, CAD_GeMatrix]:
    """C: CAD_Status CAD_GeMatrixTranslation(CAD_GeVec3 v, CAD_GeMatrix* outMatrix)

    v 만큼 옮기기

    묶음 주석: 행렬 (AcGeMatrix3d)
    """
    outMatrix = CAD_GeMatrix()
    _r = _f.CAD_GeMatrixTranslation(v, _c.byref(outMatrix))
    return (_r, outMatrix)


def CAD_GeMatrixRotation(angle: float, axis: CAD_GeVec3, center: CAD_GeVec3) -> tuple[int, CAD_GeMatrix]:
    """C: CAD_Status CAD_GeMatrixRotation(double angle, CAD_GeVec3 axis, CAD_GeVec3 center, CAD_GeMatrix* outMatrix)

    center 를 지나는 axis 둘레 오른손 방향 angle(rad) 회전
    """
    outMatrix = CAD_GeMatrix()
    _r = _f.CAD_GeMatrixRotation(angle, axis, center, _c.byref(outMatrix))
    return (_r, outMatrix)


def CAD_GeMatrixScaling(scale: float, center: CAD_GeVec3) -> tuple[int, CAD_GeMatrix]:
    """C: CAD_Status CAD_GeMatrixScaling(double scale, CAD_GeVec3 center, CAD_GeMatrix* outMatrix)

    center 기준 고른 배율

    묶음 주석: center 를 지나는 axis 둘레 오른손 방향 angle(rad) 회전
    """
    outMatrix = CAD_GeMatrix()
    _r = _f.CAD_GeMatrixScaling(scale, center, _c.byref(outMatrix))
    return (_r, outMatrix)


def CAD_GeMatrixMirroring(plane: CAD_GePlane) -> tuple[int, CAD_GeMatrix]:
    """C: CAD_Status CAD_GeMatrixMirroring(CAD_GePlane plane, CAD_GeMatrix* outMatrix)

    평면 대칭

    묶음 주석: center 를 지나는 axis 둘레 오른손 방향 angle(rad) 회전
    """
    outMatrix = CAD_GeMatrix()
    _r = _f.CAD_GeMatrixMirroring(plane, _c.byref(outMatrix))
    return (_r, outMatrix)


def CAD_GeMatrixCoordSys(origin: CAD_GeVec3, xAxis: CAD_GeVec3, yAxis: CAD_GeVec3, zAxis: CAD_GeVec3) -> tuple[int, CAD_GeMatrix]:
    """C: CAD_Status CAD_GeMatrixCoordSys(CAD_GeVec3 origin, CAD_GeVec3 xAxis, CAD_GeVec3 yAxis, CAD_GeVec3 zAxis, CAD_GeMatrix* outMatrix)

    좌표계 → 월드(AcGeMatrix3d::setCoordSystem). 축이 한 평면 = CAD_E_DEGENERATE
    """
    outMatrix = CAD_GeMatrix()
    _r = _f.CAD_GeMatrixCoordSys(origin, xAxis, yAxis, zAxis, _c.byref(outMatrix))
    return (_r, outMatrix)


def CAD_GeMatrixAlignCoordSys(fromOrigin: CAD_GeVec3, fromX: CAD_GeVec3, fromY: CAD_GeVec3, fromZ: CAD_GeVec3, toOrigin: CAD_GeVec3, toX: CAD_GeVec3, toY: CAD_GeVec3, toZ: CAD_GeVec3) -> tuple[int, CAD_GeMatrix]:
    """C: CAD_Status CAD_GeMatrixAlignCoordSys(CAD_GeVec3 fromOrigin, CAD_GeVec3 fromX, CAD_GeVec3 fromY, CAD_GeVec3 fromZ, CAD_GeVec3 toOrigin, CAD_GeVec3 toX, CAD_GeVec3 toY, CAD_GeVec3 toZ, CAD_GeMatrix* outMatrix)

    좌표계 from 에 놓인 것을 좌표계 to 로(alignCoordSys)
    """
    outMatrix = CAD_GeMatrix()
    _r = _f.CAD_GeMatrixAlignCoordSys(fromOrigin, fromX, fromY, fromZ, toOrigin, toX, toY, toZ, _c.byref(outMatrix))
    return (_r, outMatrix)


def CAD_GeMatrixPlaneToWorld(plane: CAD_GePlane) -> tuple[int, CAD_GeMatrix]:
    """C: CAD_Status CAD_GeMatrixPlaneToWorld(CAD_GePlane plane, CAD_GeMatrix* outMatrix)

    평면 좌표(CAD_GePlaneAxes, z = 법선) → 월드

    묶음 주석: 좌표계 from 에 놓인 것을 좌표계 to 로(alignCoordSys)
    """
    outMatrix = CAD_GeMatrix()
    _r = _f.CAD_GeMatrixPlaneToWorld(plane, _c.byref(outMatrix))
    return (_r, outMatrix)


def CAD_GeMatrixWorldToPlane(plane: CAD_GePlane) -> tuple[int, CAD_GeMatrix]:
    """C: CAD_Status CAD_GeMatrixWorldToPlane(CAD_GePlane plane, CAD_GeMatrix* outMatrix)

    PlaneToWorld 의 역

    묶음 주석: 좌표계 from 에 놓인 것을 좌표계 to 로(alignCoordSys)
    """
    outMatrix = CAD_GeMatrix()
    _r = _f.CAD_GeMatrixWorldToPlane(plane, _c.byref(outMatrix))
    return (_r, outMatrix)


def CAD_GeMatrixInverse(m: CAD_GeMatrix) -> tuple[int, CAD_GeMatrix]:
    """C: CAD_Status CAD_GeMatrixInverse(CAD_GeMatrix m, CAD_GeMatrix* outMatrix)

    특이 = CAD_E_DEGENERATE

    묶음 주석: 좌표계 from 에 놓인 것을 좌표계 to 로(alignCoordSys)
    """
    outMatrix = CAD_GeMatrix()
    _r = _f.CAD_GeMatrixInverse(m, _c.byref(outMatrix))
    return (_r, outMatrix)


def CAD_GeMatrixMultiply(a: CAD_GeMatrix, b: CAD_GeMatrix) -> tuple[int, CAD_GeMatrix]:
    """C: CAD_Status CAD_GeMatrixMultiply(CAD_GeMatrix a, CAD_GeMatrix b, CAD_GeMatrix* outMatrix)

    a·b (b 를 먼저 적용)

    묶음 주석: 좌표계 from 에 놓인 것을 좌표계 to 로(alignCoordSys)
    """
    outMatrix = CAD_GeMatrix()
    _r = _f.CAD_GeMatrixMultiply(a, b, _c.byref(outMatrix))
    return (_r, outMatrix)


def CAD_GeTransformPoints(m: CAD_GeMatrix, xyz: Sequence | None, count: int, outXyz: Any, outCapacity: int) -> int:
    """C: int32_t CAD_GeTransformPoints(CAD_GeMatrix m, const double* xyz, uint32_t count, double* outXyz, uint32_t outCapacity)

    점 여러 개를 한 번에 — xyz = 3 × count, outXyz 도(같은 배열을 줘도 됨). 반환 = count
    """
    _a_xyz = _n.array(_c.c_double, xyz)
    return _f.CAD_GeTransformPoints(m, _a_xyz, count, outXyz, outCapacity)


def CAD_GeTransformVectors(m: CAD_GeMatrix, xyz: Sequence | None, count: int, outXyz: Any, outCapacity: int) -> int:
    """C: int32_t CAD_GeTransformVectors(CAD_GeMatrix m, const double* xyz, uint32_t count, double* outXyz, uint32_t outCapacity)

    벡터 여러 개 — 점과 같되 이동은 빼고 돌리기·배율만
    """
    _a_xyz = _n.array(_c.c_double, xyz)
    return _f.CAD_GeTransformVectors(m, _a_xyz, count, outXyz, outCapacity)


def CAD_GeCurveCreateLine(start: CAD_GeVec3, end: CAD_GeVec3) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveCreateLine(CAD_GeVec3 start, CAD_GeVec3 end, uint64_t* outCurve)

    곡선 핸들 (AcGeCurve3d) — 만들기. 다 쓰면 CAD_GeCurveFree
    매개변수 = 시작부터 거리
    """
    outCurve = _c.c_uint64()
    _r = _f.CAD_GeCurveCreateLine(start, end, _c.byref(outCurve))
    return (_r, outCurve.value)


def CAD_GeCurveCreateArc(arc: CAD_GeArc) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveCreateArc(CAD_GeArc arc, uint64_t* outCurve)

    radius > 0, start < end ≤ start + 2π

    묶음 주석: 곡선 핸들 (AcGeCurve3d) — 만들기. 다 쓰면 CAD_GeCurveFree
    """
    outCurve = _c.c_uint64()
    _r = _f.CAD_GeCurveCreateArc(arc, _c.byref(outCurve))
    return (_r, outCurve.value)


def CAD_GeCurveCreateCircle(center: CAD_GeVec3, normal: CAD_GeVec3, radius: float) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveCreateCircle(CAD_GeVec3 center, CAD_GeVec3 normal, double radius, uint64_t* outCurve)

    원(한 바퀴 호, 매개변수 0..2π — 시작 방향은 CAD_GePlaneAxes 의 X 축)
    """
    outCurve = _c.c_uint64()
    _r = _f.CAD_GeCurveCreateCircle(center, normal, radius, _c.byref(outCurve))
    return (_r, outCurve.value)


def CAD_GeCurveCreateArc3Points(start: CAD_GeVec3, through: CAD_GeVec3, end: CAD_GeVec3) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveCreateArc3Points(CAD_GeVec3 start, CAD_GeVec3 through, CAD_GeVec3 end, uint64_t* outCurve)

    start → through → end 를 지나는 호. 세 점이 한 줄 = CAD_E_PARALLEL
    """
    outCurve = _c.c_uint64()
    _r = _f.CAD_GeCurveCreateArc3Points(start, through, end, _c.byref(outCurve))
    return (_r, outCurve.value)


def CAD_GeCurveCreateArcBulge(start: CAD_GeVec3, end: CAD_GeVec3, bulge: float, normal: CAD_GeVec3) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveCreateArcBulge(CAD_GeVec3 start, CAD_GeVec3 end, double bulge, CAD_GeVec3 normal, uint64_t* outCurve)

    두 점 + bulge(LWPOLYLINE 42: tan(포함각/4), + = normal 둘레 반시계)
    """
    outCurve = _c.c_uint64()
    _r = _f.CAD_GeCurveCreateArcBulge(start, end, bulge, normal, _c.byref(outCurve))
    return (_r, outCurve.value)


def CAD_GeCurveCreateFillet(pointA: CAD_GeVec3, dirA: CAD_GeVec3, pointB: CAD_GeVec3, dirB: CAD_GeVec3, radius: float) -> tuple[int, int, float, float]:
    """C: CAD_Status CAD_GeCurveCreateFillet(CAD_GeVec3 pointA, CAD_GeVec3 dirA, CAD_GeVec3 pointB, CAD_GeVec3 dirB, double radius, uint64_t* outCurve, double* outParamA, double* outParamB)

    두 무한 직선(점 + 방향)에 접하는 반지름 r 호 — 두 방향이 가리키는 쪽 사이 칸에. outParamA/B = 접점의 직선 매개변수(방향 1 당)
    """
    outCurve = _c.c_uint64()
    outParamA = _c.c_double()
    outParamB = _c.c_double()
    _r = _f.CAD_GeCurveCreateFillet(pointA, dirA, pointB, dirB, radius, _c.byref(outCurve), _c.byref(outParamA), _c.byref(outParamB))
    return (_r, outCurve.value, outParamA.value, outParamB.value)


def CAD_GeCurveCreateEllipse(ellipse: CAD_GeEllipse) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveCreateEllipse(CAD_GeEllipse ellipse, uint64_t* outCurve)

    타원·타원호(CAD_GeEllipse)

    묶음 주석: 두 무한 직선(점 + 방향)에 접하는 반지름 r 호 — 두 방향이 가리키는 쪽 사이 칸에. outParamA/B = 접점의 직선 매개변수(방향 1 당)
    """
    outCurve = _c.c_uint64()
    _r = _f.CAD_GeCurveCreateEllipse(ellipse, _c.byref(outCurve))
    return (_r, outCurve.value)


def CAD_GeCurveCreatePolyline(xyz: Sequence | None, count: int, closed: bool) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveCreatePolyline(const double* xyz, uint32_t count, bool closed, uint64_t* outCurve)

    폴리선 — xyz = 3 × count. closed 면 끝 → 처음 조각까지(조각 수 = 정점 수)
    """
    _a_xyz = _n.array(_c.c_double, xyz)
    outCurve = _c.c_uint64()
    _r = _f.CAD_GeCurveCreatePolyline(_a_xyz, count, closed, _c.byref(outCurve))
    return (_r, outCurve.value)


def CAD_GeCurveCreatePolylineBulge(xyz: Sequence | None, count: int, bulges: Sequence | None, bulgeCount: int, closed: bool, normal: CAD_GeVec3) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveCreatePolylineBulge(const double* xyz, uint32_t count, const double* bulges, uint32_t bulgeCount, bool closed, CAD_GeVec3 normal, uint64_t* outCurve)

    bulge 있는 폴리선(LWPOLYLINE) — bulges[i] = 정점 i → i+1 조각(0 = 직선). bulgeCount = 조각 수(열린 것 count−1, 닫힌 것 count) 또는 0
    """
    _a_xyz = _n.array(_c.c_double, xyz)
    _a_bulges = _n.array(_c.c_double, bulges)
    outCurve = _c.c_uint64()
    _r = _f.CAD_GeCurveCreatePolylineBulge(_a_xyz, count, _a_bulges, bulgeCount, closed, normal, _c.byref(outCurve))
    return (_r, outCurve.value)


def CAD_GeCurveCreateNurbs(degree: int, knots: Sequence | None, knotCount: int, controlXyz: Sequence | None, controlCount: int, weights: Sequence | None, weightCount: int) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveCreateNurbs(int degree, const double* knots, uint32_t knotCount, const double* controlXyz, uint32_t controlCount, const double* weights, uint32_t weightCount, uint64_t* outCurve)

    NURBS — 매듭 = 제어점 + 차수 + 1, weights 는 비우거나(0 개 = 다항) 제어점 수만큼
    """
    _a_knots = _n.array(_c.c_double, knots)
    _a_controlXyz = _n.array(_c.c_double, controlXyz)
    _a_weights = _n.array(_c.c_double, weights)
    outCurve = _c.c_uint64()
    _r = _f.CAD_GeCurveCreateNurbs(degree, _a_knots, knotCount, _a_controlXyz, controlCount, _a_weights, weightCount, _c.byref(outCurve))
    return (_r, outCurve.value)


def CAD_GeCurveCreateInterpolated(xyz: Sequence | None, count: int, degree: int) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveCreateInterpolated(const double* xyz, uint32_t count, int degree, uint64_t* outCurve)

    점들을 지나는 곡선(전역 보간, 현 길이 매개변수) — 차수는 점 수에 맞춰 낮춘다
    """
    _a_xyz = _n.array(_c.c_double, xyz)
    outCurve = _c.c_uint64()
    _r = _f.CAD_GeCurveCreateInterpolated(_a_xyz, count, degree, _c.byref(outCurve))
    return (_r, outCurve.value)


def CAD_GeCurveCreateComposite(curves: Sequence | None, count: int) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveCreateComposite(const uint64_t* curves, uint32_t count, uint64_t* outCurve)

    곡선들을 끝 → 시작으로 이어(복사) — 이음매가 떨어지면 CAD_E_NOT_CONNECTED. 합성 곡선은 펼쳐 넣는다
    """
    _a_curves = _n.array(_c.c_uint64, curves)
    outCurve = _c.c_uint64()
    _r = _f.CAD_GeCurveCreateComposite(_a_curves, count, _c.byref(outCurve))
    return (_r, outCurve.value)


def CAD_GeCurveCopy(curve: int) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveCopy(uint64_t curve, uint64_t* outCurve)

    같은 곡선의 새 핸들

    묶음 주석: 곡선들을 끝 → 시작으로 이어(복사) — 이음매가 떨어지면 CAD_E_NOT_CONNECTED. 합성 곡선은 펼쳐 넣는다
    """
    outCurve = _c.c_uint64()
    _r = _f.CAD_GeCurveCopy(curve, _c.byref(outCurve))
    return (_r, outCurve.value)


def CAD_GeCurveFree(curve: int) -> int:
    """C: CAD_Status CAD_GeCurveFree(uint64_t curve)

    핸들 풀기(이미 푼 것·0 = CAD_E_BAD_HANDLE)

    묶음 주석: 곡선들을 끝 → 시작으로 이어(복사) — 이음매가 떨어지면 CAD_E_NOT_CONNECTED. 합성 곡선은 펼쳐 넣는다
    """
    return _f.CAD_GeCurveFree(curve)


def CAD_GeCurveLiveCount() -> int:
    """C: int32_t CAD_GeCurveLiveCount(void)

    살아 있는 핸들 수(새는지 볼 때)

    묶음 주석: 곡선들을 끝 → 시작으로 이어(복사) — 이음매가 떨어지면 CAD_E_NOT_CONNECTED. 합성 곡선은 펼쳐 넣는다
    """
    return _f.CAD_GeCurveLiveCount()


def CAD_GeCurveGetType(curve: int) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveGetType(uint64_t curve, int* outType)

    곡선 읽기
    CAD_GECURVE_*
    """
    outType = _c.c_int()
    _r = _f.CAD_GeCurveGetType(curve, _c.byref(outType))
    return (_r, outType.value)


def CAD_GeCurveGetInterval(curve: int) -> tuple[int, float, float]:
    """C: CAD_Status CAD_GeCurveGetInterval(uint64_t curve, double* outStartParam, double* outEndParam)

    매개변수 구간

    묶음 주석: 곡선 읽기
    """
    outStartParam = _c.c_double()
    outEndParam = _c.c_double()
    _r = _f.CAD_GeCurveGetInterval(curve, _c.byref(outStartParam), _c.byref(outEndParam))
    return (_r, outStartParam.value, outEndParam.value)


def CAD_GeCurveIsClosed(curve: int) -> tuple[int, bool]:
    """C: CAD_Status CAD_GeCurveIsClosed(uint64_t curve, bool* outClosed)

    끝 = 시작(허용치 안). 선은 늘 열림

    묶음 주석: 곡선 읽기
    """
    outClosed = _c.c_bool()
    _r = _f.CAD_GeCurveIsClosed(curve, _c.byref(outClosed))
    return (_r, outClosed.value)


def CAD_GeCurveIsPlanar(curve: int) -> tuple[int, bool, CAD_GeVec3]:
    """C: CAD_Status CAD_GeCurveIsPlanar(uint64_t curve, bool* outPlanar, CAD_GeVec3* outNormal)

    평면 곡선인가 + 법선(닫힌 곡선은 반시계로 보이는 쪽). 직선은 평면(그에 수직인 아무 법선)
    """
    outPlanar = _c.c_bool()
    outNormal = CAD_GeVec3()
    _r = _f.CAD_GeCurveIsPlanar(curve, _c.byref(outPlanar), _c.byref(outNormal))
    return (_r, outPlanar.value, outNormal)


def CAD_GeCurveEvaluate(curve: int, param: float) -> tuple[int, CAD_GeVec3, CAD_GeVec3, CAD_GeVec3]:
    """C: CAD_Status CAD_GeCurveEvaluate(uint64_t curve, double param, CAD_GeVec3* outPoint, CAD_GeVec3* outFirstDeriv, CAD_GeVec3* outSecondDeriv)

    점·1차·2차 도함수(매개변수 1 당) — AcDbCurve::getPointAtParam·getFirstDeriv·getSecondDeriv
    """
    outPoint = CAD_GeVec3()
    outFirstDeriv = CAD_GeVec3()
    outSecondDeriv = CAD_GeVec3()
    _r = _f.CAD_GeCurveEvaluate(curve, param, _c.byref(outPoint), _c.byref(outFirstDeriv), _c.byref(outSecondDeriv))
    return (_r, outPoint, outFirstDeriv, outSecondDeriv)


def CAD_GeCurveEvaluateMany(curve: int, params: Sequence | None, count: int, outXyz: Any, outCapacity: int) -> int:
    """C: int32_t CAD_GeCurveEvaluateMany(uint64_t curve, const double* params, uint32_t count, double* outXyz, uint32_t outCapacity)

    여러 매개변수의 점 — outXyz = 3 × count. 반환 = count
    """
    _a_params = _n.array(_c.c_double, params)
    return _f.CAD_GeCurveEvaluateMany(curve, _a_params, count, outXyz, outCapacity)


def CAD_GeCurveParamAtPoint(curve: int, p: CAD_GeVec3) -> tuple[int, float]:
    """C: CAD_Status CAD_GeCurveParamAtPoint(uint64_t curve, CAD_GeVec3 p, double* outParam)

    곡선 위 점의 매개변수(허용치 밖 = CAD_E_NOT_ON_CURVE) — getParamAtPoint
    """
    outParam = _c.c_double()
    _r = _f.CAD_GeCurveParamAtPoint(curve, p, _c.byref(outParam))
    return (_r, outParam.value)


def CAD_GeCurveClosestPoint(curve: int, p: CAD_GeVec3, extend: bool) -> tuple[int, float, CAD_GeVec3, float]:
    """C: CAD_Status CAD_GeCurveClosestPoint(uint64_t curve, CAD_GeVec3 p, bool extend, double* outParam, CAD_GeVec3* outPoint, double* outDistance)

    가장 가까운 점 — extend = 연장한 경로에서(getClosestPointTo(pt, extend)). outDistance = 그 거리
    """
    outParam = _c.c_double()
    outPoint = CAD_GeVec3()
    outDistance = _c.c_double()
    _r = _f.CAD_GeCurveClosestPoint(curve, p, extend, _c.byref(outParam), _c.byref(outPoint), _c.byref(outDistance))
    return (_r, outParam.value, outPoint, outDistance.value)


def CAD_GeCurveClosestPointAlong(curve: int, p: CAD_GeVec3, viewDir: CAD_GeVec3, extend: bool) -> tuple[int, float, CAD_GeVec3]:
    """C: CAD_Status CAD_GeCurveClosestPointAlong(uint64_t curve, CAD_GeVec3 p, CAD_GeVec3 viewDir, bool extend, double* outParam, CAD_GeVec3* outPoint)

    viewDir 방향으로 본 가장 가까운 점(돌려주는 점은 곡선 위 3D) — getClosestPointTo(pt, normal, extend)
    """
    outParam = _c.c_double()
    outPoint = CAD_GeVec3()
    _r = _f.CAD_GeCurveClosestPointAlong(curve, p, viewDir, extend, _c.byref(outParam), _c.byref(outPoint))
    return (_r, outParam.value, outPoint)


def CAD_GeCurvePerpendicularPoints(curve: int, p: CAD_GeVec3, extend: bool, outParams: Any, capacity: int) -> int:
    """C: int32_t CAD_GeCurvePerpendicularPoints(uint64_t curve, CAD_GeVec3 p, bool extend, double* outParams, uint32_t capacity)

    수직점 — 점 p 에서 곡선에 내린 수선의 발 전부(가까운 것부터) — getNormalPoint · OSNAP 수직. 끝점은 수직일 때만
    """
    return _f.CAD_GeCurvePerpendicularPoints(curve, p, extend, outParams, capacity)


def CAD_GeCurveTangentPoints(curve: int, p: CAD_GeVec3, planeNormal: CAD_GeVec3, outParams: Any, capacity: int) -> int:
    """C: int32_t CAD_GeCurveTangentPoints(uint64_t curve, CAD_GeVec3 p, CAD_GeVec3 planeNormal, double* outParams, uint32_t capacity)

    접점 — 점 p 에서 그은 접선이 곡선에 닿는 곳(평면 법선 planeNormal, 0 이면 곡선 평면) — OSNAP 접점
    """
    return _f.CAD_GeCurveTangentPoints(curve, p, planeNormal, outParams, capacity)


def CAD_GeCurveClosestToCurve(curve1: int, curve2: int) -> tuple[int, float, float, float]:
    """C: CAD_Status CAD_GeCurveClosestToCurve(uint64_t curve1, uint64_t curve2, double* outParamA, double* outParamB, double* outDistance)

    두 곡선의 가장 가까운 두 점(만나면 거리 0) — getClosestPointTo(curve)
    """
    outParamA = _c.c_double()
    outParamB = _c.c_double()
    outDistance = _c.c_double()
    _r = _f.CAD_GeCurveClosestToCurve(curve1, curve2, _c.byref(outParamA), _c.byref(outParamB), _c.byref(outDistance))
    return (_r, outParamA.value, outParamB.value, outDistance.value)


def CAD_GeCurveLength(curve: int, fromParam: float, toParam: float) -> tuple[int, float]:
    """C: CAD_Status CAD_GeCurveLength(uint64_t curve, double fromParam, double toParam, double* outLength)

    두 매개변수 사이 길이(getDistAtParam 은 fromParam = 시작). 구간 밖 = CAD_E_OUT_OF_RANGE
    """
    outLength = _c.c_double()
    _r = _f.CAD_GeCurveLength(curve, fromParam, toParam, _c.byref(outLength))
    return (_r, outLength.value)


def CAD_GeCurveParamAtLength(curve: int, fromParam: float, length: float) -> tuple[int, float]:
    """C: CAD_Status CAD_GeCurveParamAtLength(uint64_t curve, double fromParam, double length, double* outParam)

    fromParam 에서 곡선을 따라 length(음수 = 거꾸로) 간 곳 — getParamAtDist. 끝을 넘으면 끝에서 멈춤
    """
    outParam = _c.c_double()
    _r = _f.CAD_GeCurveParamAtLength(curve, fromParam, length, _c.byref(outParam))
    return (_r, outParam.value)


def CAD_GeCurveSampleParams(curve: int, chordTolerance: float, outParams: Any, capacity: int) -> int:
    """C: int32_t CAD_GeCurveSampleParams(uint64_t curve, double chordTolerance, double* outParams, uint32_t capacity)

    곡선 ↔ 현 거리 ≤ chordTolerance 가 되게 나눈 매개변수(양 끝 포함) — 그리기·다른 계산용 표본
    """
    return _f.CAD_GeCurveSampleParams(curve, chordTolerance, outParams, capacity)


def CAD_GeCurveGetBox(curve: int) -> tuple[int, CAD_GeVec3, CAD_GeVec3]:
    """C: CAD_Status CAD_GeCurveGetBox(uint64_t curve, CAD_GeVec3* outMin, CAD_GeVec3* outMax)

    꼭 맞는 상자

    묶음 주석: 곡선 ↔ 현 거리 ≤ chordTolerance 가 되게 나눈 매개변수(양 끝 포함) — 그리기·다른 계산용 표본
    """
    outMin = CAD_GeVec3()
    outMax = CAD_GeVec3()
    _r = _f.CAD_GeCurveGetBox(curve, _c.byref(outMin), _c.byref(outMax))
    return (_r, outMin, outMax)


def CAD_GeCurveArea(curve: int) -> tuple[int, float]:
    """C: CAD_Status CAD_GeCurveArea(uint64_t curve, double* outArea)

    닫힌 평면 곡선 넓이 — getArea. 열림 = CAD_E_NOT_CLOSED, 비평면 = CAD_E_NOT_PLANAR
    """
    outArea = _c.c_double()
    _r = _f.CAD_GeCurveArea(curve, _c.byref(outArea))
    return (_r, outArea.value)


def CAD_GeCurveContainsPoint(curve: int, p: CAD_GeVec3) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveContainsPoint(uint64_t curve, CAD_GeVec3 p, int* outPosition)

    점이 닫힌 평면 곡선 안인가(곡선 평면에 투영해서) — CAD_GEPOS_*
    """
    outPosition = _c.c_int()
    _r = _f.CAD_GeCurveContainsPoint(curve, p, _c.byref(outPosition))
    return (_r, outPosition.value)


def CAD_GeCurveGetLine(curve: int) -> tuple[int, CAD_GeVec3, CAD_GeVec3]:
    """C: CAD_Status CAD_GeCurveGetLine(uint64_t curve, CAD_GeVec3* outStart, CAD_GeVec3* outEnd)

    선이 아니면 CAD_E_WRONG_TYPE

    묶음 주석: 점이 닫힌 평면 곡선 안인가(곡선 평면에 투영해서) — CAD_GEPOS_*
    """
    outStart = CAD_GeVec3()
    outEnd = CAD_GeVec3()
    _r = _f.CAD_GeCurveGetLine(curve, _c.byref(outStart), _c.byref(outEnd))
    return (_r, outStart, outEnd)


def CAD_GeCurveGetArc(curve: int) -> tuple[int, CAD_GeArc]:
    """C: CAD_Status CAD_GeCurveGetArc(uint64_t curve, CAD_GeArc* outArc)

    원·호가 아니면 CAD_E_WRONG_TYPE

    묶음 주석: 점이 닫힌 평면 곡선 안인가(곡선 평면에 투영해서) — CAD_GEPOS_*
    """
    outArc = CAD_GeArc()
    _r = _f.CAD_GeCurveGetArc(curve, _c.byref(outArc))
    return (_r, outArc)


def CAD_GeCurveGetEllipse(curve: int) -> tuple[int, CAD_GeEllipse]:
    """C: CAD_Status CAD_GeCurveGetEllipse(uint64_t curve, CAD_GeEllipse* outEllipse)

    타원이 아니면 CAD_E_WRONG_TYPE

    묶음 주석: 점이 닫힌 평면 곡선 안인가(곡선 평면에 투영해서) — CAD_GEPOS_*
    """
    outEllipse = CAD_GeEllipse()
    _r = _f.CAD_GeCurveGetEllipse(curve, _c.byref(outEllipse))
    return (_r, outEllipse)


def CAD_GeCurveGetPieceCount(curve: int) -> int:
    """C: int32_t CAD_GeCurveGetPieceCount(uint64_t curve)

    합성 곡선 조각 수(그 밖은 1)

    묶음 주석: 점이 닫힌 평면 곡선 안인가(곡선 평면에 투영해서) — CAD_GEPOS_*
    """
    return _f.CAD_GeCurveGetPieceCount(curve)


def CAD_GeCurveGetPiece(curve: int, index: int) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveGetPiece(uint64_t curve, uint32_t index, uint64_t* outPiece)

    조각 사본(새 핸들)

    묶음 주석: 점이 닫힌 평면 곡선 안인가(곡선 평면에 투영해서) — CAD_GEPOS_*
    """
    outPiece = _c.c_uint64()
    _r = _f.CAD_GeCurveGetPiece(curve, index, _c.byref(outPiece))
    return (_r, outPiece.value)


def CAD_GeCurveGetNurbsInfo(curve: int) -> tuple[int, int, int, int, bool]:
    """C: CAD_Status CAD_GeCurveGetNurbsInfo(uint64_t curve, int* outDegree, uint32_t* outControlCount, uint32_t* outKnotCount, bool* outRational)

    NURBS 핸들만

    묶음 주석: 점이 닫힌 평면 곡선 안인가(곡선 평면에 투영해서) — CAD_GEPOS_*
    """
    outDegree = _c.c_int()
    outControlCount = _c.c_uint32()
    outKnotCount = _c.c_uint32()
    outRational = _c.c_bool()
    _r = _f.CAD_GeCurveGetNurbsInfo(curve, _c.byref(outDegree), _c.byref(outControlCount), _c.byref(outKnotCount), _c.byref(outRational))
    return (_r, outDegree.value, outControlCount.value, outKnotCount.value, outRational.value)


def CAD_GeCurveGetNurbsData(curve: int, outControlXyz: Any, controlCapacity: int, outKnots: Any, knotCapacity: int, outWeights: Any, weightCapacity: int) -> int:
    """C: CAD_Status CAD_GeCurveGetNurbsData(uint64_t curve, double* outControlXyz, uint32_t controlCapacity, double* outKnots, uint32_t knotCapacity, double* outWeights, uint32_t weightCapacity)

    NURBS 데이터 — 칸은 점 수·매듭 수·무게 수 단위. 하나라도 모자라면 CAD_E_BUFFER_TOO_SMALL(아무것도 안 씀). 다항이면 무게는 전부 1
    """
    return _f.CAD_GeCurveGetNurbsData(curve, outControlXyz, controlCapacity, outKnots, knotCapacity, outWeights, weightCapacity)


def CAD_GeCurveToNurbs(curve: int) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveToNurbs(uint64_t curve, uint64_t* outCurve)

    같은 곡선의 NURBS(새 핸들, 선·원·타원은 정확)

    묶음 주석: NURBS 데이터 — 칸은 점 수·매듭 수·무게 수 단위. 하나라도 모자라면 CAD_E_BUFFER_TOO_SMALL(아무것도 안 씀). 다항이면 무게는 전부 1
    """
    outCurve = _c.c_uint64()
    _r = _f.CAD_GeCurveToNurbs(curve, _c.byref(outCurve))
    return (_r, outCurve.value)


def CAD_GeCurveReverse(curve: int) -> int:
    """C: CAD_Status CAD_GeCurveReverse(uint64_t curve)

    곡선 바꾸기(그 핸들의 곡선을 바꿔 끼움)
    방향 뒤집기(시작 ↔ 끝) — reverseCurve
    """
    return _f.CAD_GeCurveReverse(curve)


def CAD_GeCurveTransform(curve: int, m: CAD_GeMatrix) -> int:
    """C: CAD_Status CAD_GeCurveTransform(uint64_t curve, CAD_GeMatrix m)

    닮음 변환이면 원·호·타원 그대로, 아니면 그 부분은 NURBS 가 된다(정확, 매개변수 바뀜)
    """
    return _f.CAD_GeCurveTransform(curve, m)


def CAD_GeCurveExtendToPoint(curve: int, atStart: bool, toPoint: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_GeCurveExtendToPoint(uint64_t curve, bool atStart, CAD_GeVec3 toPoint)

    끝을 경로 위 점까지 늘인다 — 선·원호·타원·폴리선(첫·끝 조각이 선·호) — extend(start, pt).
    경로 밖 = CAD_E_NOT_ON_CURVE, 지금 곡선 위 = CAD_E_INVALID_ARG, NURBS = CAD_E_NOT_SUPPORTED
    """
    return _f.CAD_GeCurveExtendToPoint(curve, atStart, toPoint)


def CAD_GeCurveExtendToParam(curve: int, newParam: float) -> int:
    """C: CAD_Status CAD_GeCurveExtendToParam(uint64_t curve, double newParam)

    구간 밖 매개변수까지 — extend(param)

    묶음 주석: 끝을 경로 위 점까지 늘인다 — 선·원호·타원·폴리선(첫·끝 조각이 선·호) — extend(start, pt).
    경로 밖 = CAD_E_NOT_ON_CURVE, 지금 곡선 위 = CAD_E_INVALID_ARG, NURBS = CAD_E_NOT_SUPPORTED
    """
    return _f.CAD_GeCurveExtendToParam(curve, newParam)


def CAD_GeCurveSubCurve(curve: int, fromParam: float, toParam: float) -> tuple[int, int]:
    """C: CAD_Status CAD_GeCurveSubCurve(uint64_t curve, double fromParam, double toParam, uint64_t* outCurve)

    fromParam < toParam 부분의 새 곡선(매개변수 그대로). 선·호·타원은 구간 밖까지(연장), NURBS·폴리선은 구간 안만(밖 = CAD_E_OUT_OF_RANGE)
    """
    outCurve = _c.c_uint64()
    _r = _f.CAD_GeCurveSubCurve(curve, fromParam, toParam, _c.byref(outCurve))
    return (_r, outCurve.value)


def CAD_GeCurveSplit(curve: int, params: Sequence | None, count: int, outCurves: Any, capacity: int) -> int:
    """C: int32_t CAD_GeCurveSplit(uint64_t curve, const double* params, uint32_t count, uint64_t* outCurves, uint32_t capacity)

    나누기 — 열린 곡선: 시작→p1→…→끝, 닫힌 곡선: p1→…→pn→(이음매를 지나)p1. 끝·같은 값은 버린다 — getSplitCurves
    """
    _a_params = _n.array(_c.c_double, params)
    return _f.CAD_GeCurveSplit(curve, _a_params, count, outCurves, capacity)


def CAD_GeCurveOffset(curve: int, distance: float, planeNormal: CAD_GeVec3, outCurves: Any, capacity: int) -> int:
    """C: int32_t CAD_GeCurveOffset(uint64_t curve, double distance, CAD_GeVec3 planeNormal, uint64_t* outCurves, uint32_t capacity)

    오프셋 — planeNormal 평면 안에서(0 이면 곡선 평면), distance > 0 = 진행 방향 오른쪽(반시계 닫힌 곡선이면 바깥, 호는 반지름 + d).
    선·호 정확, 타원·NURBS 는 NURBS 근사(허용치 안), 폴리선은 이음매를 교점까지 늘이거나 자르고 안 만나면 둥글게 — getOffsetCurvesGivenPlaneNormal
    """
    return _f.CAD_GeCurveOffset(curve, distance, planeNormal, outCurves, capacity)


def CAD_GeCurveIntersect(curve1: int, curve2: int, extendMode: int, viewDir: CAD_GeVec3, outHits: Any, capacity: int) -> int:
    """C: int32_t CAD_GeCurveIntersect(uint64_t curve1, uint64_t curve2, int extendMode, CAD_GeVec3 viewDir, CAD_GeIntersection* outHits, uint32_t capacity)

    교차점 — extendMode = CAD_GE_EXTEND_*, viewDir ≠ 0 이면 그 방향으로 본 교차(높이가 달라도 만남). 결과는 곡선 1 매개변수 순
    """
    return _f.CAD_GeCurveIntersect(curve1, curve2, extendMode, viewDir, outHits, capacity)


def CAD_GeCurveIntersectPlane(curve: int, plane: CAD_GePlane, outParams: Any, capacity: int) -> int:
    """C: int32_t CAD_GeCurveIntersectPlane(uint64_t curve, CAD_GePlane plane, double* outParams, uint32_t capacity)

    곡선 ∩ 평면 — 지나는 점과 닿는 점의 매개변수(곡선이 평면 안에 누우면 0 개)
    """
    return _f.CAD_GeCurveIntersectPlane(curve, plane, outParams, capacity)
