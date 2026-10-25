# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Solids 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_MAX_BREP_PROFILE_POINTS', 'CAD_CreateBox', 'CAD_CreateWedge', 'CAD_CreatePyramid', 'CAD_CreateSphere', 'CAD_CreateCylinder', 'CAD_CreateCone', 'CAD_CreateTorus', 'CAD_CreateTube', 'CAD_CreateExtrude', 'CAD_Sweep', 'CAD_Revolve', 'CAD_Loft', 'CAD_PushPullSelectedFace', 'CAD_InsetSelectedFace', 'CAD_GetBRepInfo', 'CAD_GetBRepFaceInfo', 'CAD_PushPullBRepFace', 'CAD_CutExtrudeBRep', 'CAD_CutExtrudeFromSketch', 'CAD_BossExtrudeBRep', 'CAD_BossExtrudeFromSketch', 'CAD_GetBRepBossCount', 'CAD_GetBRepBossHeight', 'CAD_SetBRepBossHeight', 'CAD_GetBRepCutCount', 'CAD_GetBRepCutInfo', 'CAD_GetBRepCutProfile', 'CAD_SetBRepCut', 'CAD_SetBRepCutFromSketch', 'CAD_RemoveBRepFeatures', 'CAD_RemoveBRepCut', 'CAD_RemoveBRepBoss', 'CAD_GetBooleanCylinderCutCount', 'CAD_GetBooleanCylinderCutInfo', 'CAD_SetBooleanCylinderCut', 'CAD_RebuildBRepMesh', 'CAD_Shell', 'CAD_EdgeFillet', 'CAD_EdgeChamfer', 'CAD_AddEdgeBevel', 'CAD_GetEdgeBevelCount', 'CAD_BooleanUnion', 'CAD_BooleanIntersection', 'CAD_BooleanSubtract', 'CAD_CheckInterference', 'CAD_ExplodeView', 'CAD_SetFeatureDimensionsVisible', 'CAD_GetFeatureDimensionsVisible', 'CAD_GetFeatureDimensionCount', 'CAD_GetFeatureDimension', 'CAD_SetFeatureDimension']

_f = _n.native

CAD_MAX_BREP_PROFILE_POINTS = 2048

_n.bind("CAD_CreateBox", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateWedge", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreatePyramid", _c.c_int32, [CAD_GeVec3, _c.c_double, _c.c_double, _c.c_int32, _c.c_double, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateSphere", _c.c_int32, [CAD_GeVec3, _c.c_double, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateCylinder", _c.c_int32, [CAD_GeVec3, _c.c_double, _c.c_double, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateCone", _c.c_int32, [CAD_GeVec3, _c.c_double, _c.c_double, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateTorus", _c.c_int32, [CAD_GeVec3, _c.c_double, _c.c_double, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateTube", _c.c_int32, [CAD_GeVec3, _c.c_double, _c.c_double, _c.c_double, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateExtrude", _c.c_int32, [_c.c_uint32, _c.c_double, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_Sweep", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_Revolve", _c.c_int32, [_c.c_uint32, CAD_GeVec3, CAD_GeVec3, _c.c_int32, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_Loft", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_PushPullSelectedFace", _c.c_int32, [_c.c_double])
_n.bind("CAD_InsetSelectedFace", _c.c_int32, [_c.c_double])
_n.bind("CAD_GetBRepInfo", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_BRepInfo)])
_n.bind("CAD_GetBRepFaceInfo", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.POINTER(CAD_BRepFaceInfo)])
_n.bind("CAD_PushPullBRepFace", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.c_double])
_n.bind("CAD_CutExtrudeBRep", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_GeVec3), _c.c_uint32, _c.c_double, _c.c_bool])
_n.bind("CAD_CutExtrudeFromSketch", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.c_double, _c.c_bool])
_n.bind("CAD_BossExtrudeBRep", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_GeVec3), _c.c_uint32, _c.c_double])
_n.bind("CAD_BossExtrudeFromSketch", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.c_double])
_n.bind("CAD_GetBRepBossCount", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_GetBRepBossHeight", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.POINTER(_c.c_double)])
_n.bind("CAD_SetBRepBossHeight", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.c_double])
_n.bind("CAD_GetBRepCutCount", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_GetBRepCutInfo", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.POINTER(CAD_BRepCutInfo)])
_n.bind("CAD_GetBRepCutProfile", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.POINTER(CAD_GeVec3), _c.c_uint32])
_n.bind("CAD_SetBRepCut", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.POINTER(CAD_GeVec3), _c.c_uint32, _c.c_double, _c.c_bool])
_n.bind("CAD_SetBRepCutFromSketch", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.c_uint32, _c.c_double, _c.c_bool])
_n.bind("CAD_RemoveBRepFeatures", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_uint32), _c.c_uint32, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_RemoveBRepCut", _c.c_int32, [_c.c_uint32, _c.c_uint32])
_n.bind("CAD_RemoveBRepBoss", _c.c_int32, [_c.c_uint32, _c.c_uint32])
_n.bind("CAD_GetBooleanCylinderCutCount", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_GetBooleanCylinderCutInfo", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.POINTER(CAD_BooleanCylinderCutInfo)])
_n.bind("CAD_SetBooleanCylinderCut", _c.c_int32, [_c.c_uint32, _c.c_uint32, CAD_GeVec3, CAD_GeVec3, _c.c_double, _c.c_double])
_n.bind("CAD_RebuildBRepMesh", _c.c_int32, [_c.c_uint32, _c.c_uint32])
_n.bind("CAD_Shell", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_double, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_EdgeFillet", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_double, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_EdgeChamfer", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_double, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_AddEdgeBevel", _c.c_int32, [_c.c_uint32, _c.c_bool, _c.c_double, _c.c_bool, _c.c_uint32])
_n.bind("CAD_GetEdgeBevelCount", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_BooleanUnion", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_BooleanIntersection", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_BooleanSubtract", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool, _c.c_bool, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_CheckInterference", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool, _c.POINTER(CAD_InterferenceInfo), _c.c_uint32])
_n.bind("CAD_ExplodeView", _c.c_int32, [_c.c_char_p, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_SetFeatureDimensionsVisible", _c.c_int32, [_c.c_bool])
_n.bind("CAD_GetFeatureDimensionsVisible", _c.c_int32, [_c.POINTER(_c.c_bool)])
_n.bind("CAD_GetFeatureDimensionCount", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_GetFeatureDimension", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.POINTER(_c.c_int32), _c.POINTER(_c.c_double), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetFeatureDimension", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.c_double])


def CAD_CreateBox(center: CAD_GeVec3, size: CAD_GeVec3, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateBox(CAD_GeVec3 center, CAD_GeVec3 size, const CAD_CreateOptions* opt, uint32_t* outId)

    상자 — center = 상자 가운데, size = 가로·세로·높이(월드 X·Y·Z)
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateBox(center, size, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateWedge(base: CAD_GeVec3, size: CAD_GeVec3, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateWedge(CAD_GeVec3 base, CAD_GeVec3 size, const CAD_CreateOptions* opt, uint32_t* outId)

    아래는 base = 밑면 가운데(구·토러스는 바닥에 닿는 점), 축 = +Z.
      쐐기 size = 밑면 가로·세로·높이 / 피라미드 외접 반지름·높이·변 수(3~64)·윗면 반지름(0 = 뾰족) / 관 바깥·안 반지름(안 < 바깥)·높이
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateWedge(base, size, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreatePyramid(base: CAD_GeVec3, radius: float, height: float, sides: int, topRadius: float, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreatePyramid(CAD_GeVec3 base, double radius, double height, int32_t sides, double topRadius, const CAD_CreateOptions* opt, uint32_t* outId)

    아래는 base = 밑면 가운데(구·토러스는 바닥에 닿는 점), 축 = +Z.
      쐐기 size = 밑면 가로·세로·높이 / 피라미드 외접 반지름·높이·변 수(3~64)·윗면 반지름(0 = 뾰족) / 관 바깥·안 반지름(안 < 바깥)·높이
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreatePyramid(base, radius, height, sides, topRadius, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateSphere(base: CAD_GeVec3, radius: float, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateSphere(CAD_GeVec3 base, double radius, const CAD_CreateOptions* opt, uint32_t* outId)

    아래는 base = 밑면 가운데(구·토러스는 바닥에 닿는 점), 축 = +Z.
      쐐기 size = 밑면 가로·세로·높이 / 피라미드 외접 반지름·높이·변 수(3~64)·윗면 반지름(0 = 뾰족) / 관 바깥·안 반지름(안 < 바깥)·높이
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateSphere(base, radius, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateCylinder(base: CAD_GeVec3, radius: float, height: float, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateCylinder(CAD_GeVec3 base, double radius, double height, const CAD_CreateOptions* opt, uint32_t* outId)

    아래는 base = 밑면 가운데(구·토러스는 바닥에 닿는 점), 축 = +Z.
      쐐기 size = 밑면 가로·세로·높이 / 피라미드 외접 반지름·높이·변 수(3~64)·윗면 반지름(0 = 뾰족) / 관 바깥·안 반지름(안 < 바깥)·높이
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateCylinder(base, radius, height, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateCone(base: CAD_GeVec3, radius: float, height: float, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateCone(CAD_GeVec3 base, double radius, double height, const CAD_CreateOptions* opt, uint32_t* outId)

    아래는 base = 밑면 가운데(구·토러스는 바닥에 닿는 점), 축 = +Z.
      쐐기 size = 밑면 가로·세로·높이 / 피라미드 외접 반지름·높이·변 수(3~64)·윗면 반지름(0 = 뾰족) / 관 바깥·안 반지름(안 < 바깥)·높이
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateCone(base, radius, height, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateTorus(base: CAD_GeVec3, majorRadius: float, minorRadius: float, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateTorus(CAD_GeVec3 base, double majorRadius, double minorRadius, const CAD_CreateOptions* opt, uint32_t* outId)

    minor < major

    묶음 주석: 아래는 base = 밑면 가운데(구·토러스는 바닥에 닿는 점), 축 = +Z.
      쐐기 size = 밑면 가로·세로·높이 / 피라미드 외접 반지름·높이·변 수(3~64)·윗면 반지름(0 = 뾰족) / 관 바깥·안 반지름(안 < 바깥)·높이
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateTorus(base, majorRadius, minorRadius, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateTube(base: CAD_GeVec3, outerRadius: float, innerRadius: float, height: float, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateTube(CAD_GeVec3 base, double outerRadius, double innerRadius, double height, const CAD_CreateOptions* opt, uint32_t* outId)

    아래는 base = 밑면 가운데(구·토러스는 바닥에 닿는 점), 축 = +Z.
      쐐기 size = 밑면 가로·세로·높이 / 피라미드 외접 반지름·높이·변 수(3~64)·윗면 반지름(0 = 뾰족) / 관 바깥·안 반지름(안 < 바깥)·높이
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateTube(base, outerRadius, innerRadius, height, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateExtrude(profileId: int, height: float, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateExtrude(uint32_t profileId, double height, const CAD_CreateOptions* opt, uint32_t* outId)

    돌출 — 닫힌 단면(사각형·원·닫힌 폴리선) id 를 그 평면 법선 쪽으로 height. B-Rep 피처라 단면을 고치면 다시 만들어진다
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateExtrude(profileId, height, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_Sweep(profileId: int, pathId: int, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_Sweep(uint32_t profileId, uint32_t pathId, const CAD_CreateOptions* opt, uint32_t* outId)

    스윕 — 닫힌 단면 id 를 열린 경로(폴리선·선) id 를 따라 쓸어 솔리드. 단면은 경로 시작점으로 옮겨지고 경로 방향에 맞게 돌려진다
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_Sweep(profileId, pathId, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_Revolve(profileId: int, axisStart: CAD_GeVec3, axisEnd: CAD_GeVec3, segments: int, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_Revolve(uint32_t profileId, CAD_GeVec3 axisStart, CAD_GeVec3 axisEnd, int32_t segments, const CAD_CreateOptions* opt, uint32_t* outId)

    회전체 — 단면 스케치 id 를 axisStart → axisEnd 둘레로 360°, segments 분할(0 = 32). 스윕처럼 피처 기록이 남아 단면을 고치면 다시 만든다
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_Revolve(profileId, axisStart, axisEnd, segments, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_Loft(sectionIds: Sequence | None, count: int, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_Loft(const uint32_t* sectionIds, uint32_t count, const CAD_CreateOptions* opt, uint32_t* outId)

    로프트 — 닫힌 단면 id 들(2개 이상)을 **준 차례대로** 이어 솔리드. 닫히지 않은 단면 = CAD_E_NOT_CLOSED
    """
    _a_sectionIds = _n.array(_c.c_uint32, sectionIds)
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_Loft(_a_sectionIds, count, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_PushPullSelectedFace(distance: float) -> int:
    """C: CAD_Status CAD_PushPullSelectedFace(double distance)

    고른 면 하나 (하위 객체 선택 — CAD_SetSubobjectSelectionMode 로 면 모드에서 고른 면)
    PushPull = 법선 방향으로 distance(mm, 양수 = 바깥) 밀기, Inset = 평면 볼록 면 안쪽에 distance 폭 링(0 = 자동).
    고른 면이 없거나 안 되는 면이면 CAD_E_FAILED + 이유. 되돌리기 1
    """
    return _f.CAD_PushPullSelectedFace(distance)


def CAD_InsetSelectedFace(distance: float) -> int:
    """C: CAD_Status CAD_InsetSelectedFace(double distance)

    고른 면 하나 (하위 객체 선택 — CAD_SetSubobjectSelectionMode 로 면 모드에서 고른 면)
    PushPull = 법선 방향으로 distance(mm, 양수 = 바깥) 밀기, Inset = 평면 볼록 면 안쪽에 distance 폭 링(0 = 자동).
    고른 면이 없거나 안 되는 면이면 CAD_E_FAILED + 이유. 되돌리기 1
    """
    return _f.CAD_InsetSelectedFace(distance)


def CAD_GetBRepInfo(id: int) -> tuple[int, CAD_BRepInfo]:
    """C: CAD_Status CAD_GetBRepInfo(uint32_t id, CAD_BRepInfo* outInfo)
    """
    outInfo = CAD_BRepInfo()
    outInfo.size = _c.sizeof(CAD_BRepInfo)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_GetBRepInfo(id, _c.byref(outInfo))
    return (_r, outInfo)


def CAD_GetBRepFaceInfo(id: int, faceId: int) -> tuple[int, CAD_BRepFaceInfo]:
    """C: CAD_Status CAD_GetBRepFaceInfo(uint32_t id, uint32_t faceId, CAD_BRepFaceInfo* outInfo)
    """
    outInfo = CAD_BRepFaceInfo()
    outInfo.size = _c.sizeof(CAD_BRepFaceInfo)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_GetBRepFaceInfo(id, faceId, _c.byref(outInfo))
    return (_r, outInfo)


def CAD_PushPullBRepFace(id: int, faceId: int, distance: float) -> int:
    """C: CAD_Status CAD_PushPullBRepFace(uint32_t id, uint32_t faceId, double distance)

    면 밀기 — distance(mm) 만큼 바깥으로. 상자 평면은 반대편 고정, 원통 옆면은 반지름, 돌출 옆면은 단면 변 평행 이동
    """
    return _f.CAD_PushPullBRepFace(id, faceId, distance)


def CAD_CutExtrudeBRep(id: int, profile: Sequence | None, count: int, depth: float, throughAll: bool) -> int:
    """C: CAD_Status CAD_CutExtrudeBRep(uint32_t id, const CAD_GeVec3* profile, uint32_t count, double depth, bool throughAll)

    돌출 컷 — 닫힌 단면 점(월드, 3..CAD_MAX_BREP_PROFILE_POINTS)을 캡과 나란한 평면에 둔다(엔진이 아래 기준면으로 투영). throughAll = 관통(depth 무시).
    FromSketch = 닫힌 스케치(사각형·원·닫힌 폴리선) id 로 — 피처 기록이 남아 스케치를 고치면 컷도 다시 만든다
    """
    _a_profile = _n.array(CAD_GeVec3, profile)
    return _f.CAD_CutExtrudeBRep(id, _a_profile, count, depth, throughAll)


def CAD_CutExtrudeFromSketch(id: int, sketchId: int, depth: float, throughAll: bool) -> int:
    """C: CAD_Status CAD_CutExtrudeFromSketch(uint32_t id, uint32_t sketchId, double depth, bool throughAll)

    돌출 컷 — 닫힌 단면 점(월드, 3..CAD_MAX_BREP_PROFILE_POINTS)을 캡과 나란한 평면에 둔다(엔진이 아래 기준면으로 투영). throughAll = 관통(depth 무시).
    FromSketch = 닫힌 스케치(사각형·원·닫힌 폴리선) id 로 — 피처 기록이 남아 스케치를 고치면 컷도 다시 만든다
    """
    return _f.CAD_CutExtrudeFromSketch(id, sketchId, depth, throughAll)


def CAD_BossExtrudeBRep(id: int, profile: Sequence | None, count: int, height: float) -> int:
    """C: CAD_Status CAD_BossExtrudeBRep(uint32_t id, const CAD_GeVec3* profile, uint32_t count, double height)

    보스(더하는 돌출) — height > 0 = 위 캡에서 위로, < 0 = 아래 캡에서 아래로(월드 mm). 발자국이 외곽에 닿거나 같은 쪽 보스와 겹치면 CAD_E_FAILED.
    FromSketch = 스케치가 가까운 캡 쪽으로 height(양수)
    """
    _a_profile = _n.array(CAD_GeVec3, profile)
    return _f.CAD_BossExtrudeBRep(id, _a_profile, count, height)


def CAD_BossExtrudeFromSketch(id: int, sketchId: int, height: float) -> int:
    """C: CAD_Status CAD_BossExtrudeFromSketch(uint32_t id, uint32_t sketchId, double height)

    보스(더하는 돌출) — height > 0 = 위 캡에서 위로, < 0 = 아래 캡에서 아래로(월드 mm). 발자국이 외곽에 닿거나 같은 쪽 보스와 겹치면 CAD_E_FAILED.
    FromSketch = 스케치가 가까운 캡 쪽으로 height(양수)
    """
    return _f.CAD_BossExtrudeFromSketch(id, sketchId, height)


def CAD_GetBRepBossCount(id: int) -> int:
    """C: int32_t CAD_GetBRepBossCount(uint32_t id)

    보스(더하는 돌출) — height > 0 = 위 캡에서 위로, < 0 = 아래 캡에서 아래로(월드 mm). 발자국이 외곽에 닿거나 같은 쪽 보스와 겹치면 CAD_E_FAILED.
    FromSketch = 스케치가 가까운 캡 쪽으로 height(양수)
    """
    return _f.CAD_GetBRepBossCount(id)


def CAD_GetBRepBossHeight(id: int, bossIndex: int) -> tuple[int, float]:
    """C: CAD_Status CAD_GetBRepBossHeight(uint32_t id, uint32_t bossIndex, double* outHeight)

    부호 = 위/아래

    묶음 주석: 보스(더하는 돌출) — height > 0 = 위 캡에서 위로, < 0 = 아래 캡에서 아래로(월드 mm). 발자국이 외곽에 닿거나 같은 쪽 보스와 겹치면 CAD_E_FAILED.
    FromSketch = 스케치가 가까운 캡 쪽으로 height(양수)
    """
    outHeight = _c.c_double()
    _r = _f.CAD_GetBRepBossHeight(id, bossIndex, _c.byref(outHeight))
    return (_r, outHeight.value)


def CAD_SetBRepBossHeight(id: int, bossIndex: int, height: float) -> int:
    """C: CAD_Status CAD_SetBRepBossHeight(uint32_t id, uint32_t bossIndex, double height)

    보스(더하는 돌출) — height > 0 = 위 캡에서 위로, < 0 = 아래 캡에서 아래로(월드 mm). 발자국이 외곽에 닿거나 같은 쪽 보스와 겹치면 CAD_E_FAILED.
    FromSketch = 스케치가 가까운 캡 쪽으로 height(양수)
    """
    return _f.CAD_SetBRepBossHeight(id, bossIndex, height)


def CAD_GetBRepCutCount(id: int) -> int:
    """C: int32_t CAD_GetBRepCutCount(uint32_t id)
    """
    return _f.CAD_GetBRepCutCount(id)


def CAD_GetBRepCutInfo(id: int, cutIndex: int) -> tuple[int, CAD_BRepCutInfo]:
    """C: CAD_Status CAD_GetBRepCutInfo(uint32_t id, uint32_t cutIndex, CAD_BRepCutInfo* outInfo)
    """
    outInfo = CAD_BRepCutInfo()
    outInfo.size = _c.sizeof(CAD_BRepCutInfo)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_GetBRepCutInfo(id, cutIndex, _c.byref(outInfo))
    return (_r, outInfo)


def CAD_GetBRepCutProfile(id: int, cutIndex: int, outPoints: Any, capacity: int) -> int:
    """C: int32_t CAD_GetBRepCutProfile(uint32_t id, uint32_t cutIndex, CAD_GeVec3* outPoints, uint32_t capacity)

    컷 단면 점(월드) — 반환 = 점 수, capacity 만큼 채운다
    """
    return _f.CAD_GetBRepCutProfile(id, cutIndex, outPoints, capacity)


def CAD_SetBRepCut(id: int, cutIndex: int, profile: Sequence | None, count: int, depth: float, throughAll: bool) -> int:
    """C: CAD_Status CAD_SetBRepCut(uint32_t id, uint32_t cutIndex, const CAD_GeVec3* profile, uint32_t count, double depth, bool throughAll)

    컷 바꾸기 — 단면(월드)·깊이·관통을 통째로, 또는 닫힌 스케치로
    """
    _a_profile = _n.array(CAD_GeVec3, profile)
    return _f.CAD_SetBRepCut(id, cutIndex, _a_profile, count, depth, throughAll)


def CAD_SetBRepCutFromSketch(id: int, cutIndex: int, sketchId: int, depth: float, throughAll: bool) -> int:
    """C: CAD_Status CAD_SetBRepCutFromSketch(uint32_t id, uint32_t cutIndex, uint32_t sketchId, double depth, bool throughAll)

    컷 바꾸기 — 단면(월드)·깊이·관통을 통째로, 또는 닫힌 스케치로
    """
    return _f.CAD_SetBRepCutFromSketch(id, cutIndex, sketchId, depth, throughAll)


def CAD_RemoveBRepFeatures(id: int, cutIndices: Sequence | None, cutCount: int, bossIndices: Sequence | None, bossCount: int) -> int:
    """C: CAD_Status CAD_RemoveBRepFeatures(uint32_t id, const uint32_t* cutIndices, uint32_t cutCount, const uint32_t* bossIndices, uint32_t bossCount)

    컷·보스 지우기(솔리드웍스 피처 삭제처럼) — 여러 개를 한 번에 빼고 남은 것으로 한 번 다시 만든다. 그 피처만 쓰던 스케치도 지운다.
    번호는 지우기 전 번호(지운 뒤엔 뒤쪽이 당겨진다). 되돌리기 1. 남은 것으로 모양을 못 만들면(보스를 지워 그 안 컷이 허공에 남음 …) CAD_E_FAILED
    """
    _a_cutIndices = _n.array(_c.c_uint32, cutIndices)
    _a_bossIndices = _n.array(_c.c_uint32, bossIndices)
    return _f.CAD_RemoveBRepFeatures(id, _a_cutIndices, cutCount, _a_bossIndices, bossCount)


def CAD_RemoveBRepCut(id: int, cutIndex: int) -> int:
    """C: CAD_Status CAD_RemoveBRepCut(uint32_t id, uint32_t cutIndex)

    하나만 — CAD_RemoveBRepFeatures 와 같다

    묶음 주석: 컷·보스 지우기(솔리드웍스 피처 삭제처럼) — 여러 개를 한 번에 빼고 남은 것으로 한 번 다시 만든다. 그 피처만 쓰던 스케치도 지운다.
    번호는 지우기 전 번호(지운 뒤엔 뒤쪽이 당겨진다). 되돌리기 1. 남은 것으로 모양을 못 만들면(보스를 지워 그 안 컷이 허공에 남음 …) CAD_E_FAILED
    """
    return _f.CAD_RemoveBRepCut(id, cutIndex)


def CAD_RemoveBRepBoss(id: int, bossIndex: int) -> int:
    """C: CAD_Status CAD_RemoveBRepBoss(uint32_t id, uint32_t bossIndex)

    컷·보스 지우기(솔리드웍스 피처 삭제처럼) — 여러 개를 한 번에 빼고 남은 것으로 한 번 다시 만든다. 그 피처만 쓰던 스케치도 지운다.
    번호는 지우기 전 번호(지운 뒤엔 뒤쪽이 당겨진다). 되돌리기 1. 남은 것으로 모양을 못 만들면(보스를 지워 그 안 컷이 허공에 남음 …) CAD_E_FAILED
    """
    return _f.CAD_RemoveBRepBoss(id, bossIndex)


def CAD_GetBooleanCylinderCutCount(id: int) -> int:
    """C: int32_t CAD_GetBooleanCylinderCutCount(uint32_t id)
    """
    return _f.CAD_GetBooleanCylinderCutCount(id)


def CAD_GetBooleanCylinderCutInfo(id: int, cutIndex: int) -> tuple[int, CAD_BooleanCylinderCutInfo]:
    """C: CAD_Status CAD_GetBooleanCylinderCutInfo(uint32_t id, uint32_t cutIndex, CAD_BooleanCylinderCutInfo* outInfo)
    """
    outInfo = CAD_BooleanCylinderCutInfo()
    outInfo.size = _c.sizeof(CAD_BooleanCylinderCutInfo)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_GetBooleanCylinderCutInfo(id, cutIndex, _c.byref(outInfo))
    return (_r, outInfo)


def CAD_SetBooleanCylinderCut(id: int, cutIndex: int, center: CAD_GeVec3, axis: CAD_GeVec3, radius: float, height: float) -> int:
    """C: CAD_Status CAD_SetBooleanCylinderCut(uint32_t id, uint32_t cutIndex, CAD_GeVec3 center, CAD_GeVec3 axis, double radius, double height)
    """
    return _f.CAD_SetBooleanCylinderCut(id, cutIndex, center, axis, radius, height)


def CAD_RebuildBRepMesh(id: int, curvedSegments: int) -> int:
    """C: CAD_Status CAD_RebuildBRepMesh(uint32_t id, uint32_t curvedSegments)

    화면 메시를 B-Rep 정의로 다시 — 곡면 분할 3..512(밖이면 그 끝으로)
    """
    return _f.CAD_RebuildBRepMesh(id, curvedSegments)


def CAD_Shell(ids: Sequence | None, count: int, thickness: float, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_Shell(const uint32_t* ids, uint32_t count, double thickness, uint32_t* outIds, uint32_t capacity)

    셸 — 속을 비워 두께만 남긴다(닫힌 셸). thickness <= 0 = 자동(바운딩박스 최소변의 5%). 결과는 새 객체(원본은 지움)
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_Shell(_a_ids, count, thickness, outIds, capacity)


def CAD_EdgeFillet(ids: Sequence | None, count: int, distance: float, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_EdgeFillet(const uint32_t* ids, uint32_t count, double distance, uint32_t* outIds, uint32_t capacity)

    볼록 모서리 전부 필렛·모따기 — distance(mm) <= 0 = 자동(최소변의 12%). B-Rep 솔리드는 **같은 id** 에 가공 기록(스케치를 고쳐도 다시 적용),
    그 밖의 메시는 새 객체(원본은 지움). 모서리 하나만은 CAD_AddEdgeBevel
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_EdgeFillet(_a_ids, count, distance, outIds, capacity)


def CAD_EdgeChamfer(ids: Sequence | None, count: int, distance: float, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_EdgeChamfer(const uint32_t* ids, uint32_t count, double distance, uint32_t* outIds, uint32_t capacity)

    볼록 모서리 전부 필렛·모따기 — distance(mm) <= 0 = 자동(최소변의 12%). B-Rep 솔리드는 **같은 id** 에 가공 기록(스케치를 고쳐도 다시 적용),
    그 밖의 메시는 새 객체(원본은 지움). 모서리 하나만은 CAD_AddEdgeBevel
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_EdgeChamfer(_a_ids, count, distance, outIds, capacity)


def CAD_AddEdgeBevel(id: int, fillet: bool, distance: float, allEdges: bool, brepEdge: int) -> int:
    """C: CAD_Status CAD_AddEdgeBevel(uint32_t id, bool fillet, double distance, bool allEdges, uint32_t brepEdge)

    모서리 가공 기록 — B-Rep 솔리드에 필렛/모따기 하나를 더한다(스케치가 바뀌어도 다시 적용). allEdges = 볼록 모서리 전부,
    아니면 brepEdge(B-Rep 선 모서리 id). distance = 월드 mm. B-Rep 이 아님 = CAD_E_WRONG_TYPE, 안 먹으면 CAD_E_FAILED(변화 없음)
    """
    return _f.CAD_AddEdgeBevel(id, fillet, distance, allEdges, brepEdge)


def CAD_GetEdgeBevelCount(id: int) -> int:
    """C: int32_t CAD_GetEdgeBevelCount(uint32_t id)

    모서리 가공 기록 — B-Rep 솔리드에 필렛/모따기 하나를 더한다(스케치가 바뀌어도 다시 적용). allEdges = 볼록 모서리 전부,
    아니면 brepEdge(B-Rep 선 모서리 id). distance = 월드 mm. B-Rep 이 아님 = CAD_E_WRONG_TYPE, 안 먹으면 CAD_E_FAILED(변화 없음)
    """
    return _f.CAD_GetEdgeBevelCount(id)


def CAD_BooleanUnion(ids: Sequence | None, count: int, keepOriginals: bool) -> tuple[int, int]:
    """C: CAD_Status CAD_BooleanUnion(const uint32_t* ids, uint32_t count, bool keepOriginals, uint32_t* outId)

    합집합 — ids 2개 이상 → 한 객체(떨어져 있어도 한 객체에 덩어리 여럿)
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    outId = _c.c_uint32()
    _r = _f.CAD_BooleanUnion(_a_ids, count, keepOriginals, _c.byref(outId))
    return (_r, outId.value)


def CAD_BooleanIntersection(ids: Sequence | None, count: int, keepOriginals: bool) -> tuple[int, int]:
    """C: CAD_Status CAD_BooleanIntersection(const uint32_t* ids, uint32_t count, bool keepOriginals, uint32_t* outId)

    교집합 — ids 2개 이상 **모두의** 공통 부분
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    outId = _c.c_uint32()
    _r = _f.CAD_BooleanIntersection(_a_ids, count, keepOriginals, _c.byref(outId))
    return (_r, outId.value)


def CAD_BooleanSubtract(baseIds: Sequence | None, baseCount: int, cutIds: Sequence | None, cutCount: int, keepOriginals: bool, perBase: bool, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_BooleanSubtract(const uint32_t* baseIds, uint32_t baseCount, const uint32_t* cutIds, uint32_t cutCount, bool keepOriginals, bool perBase, uint32_t* outIds, uint32_t capacity)

    차집합 — 기준 baseIds 에서 cutIds 전부를 뺀다. perBase = false: union(기준) − union(빼는 것) → 결과 1개(오토캐드 SUBTRACT),
    true: 기준마다 따로(판 3장에 같은 구멍 → 판 3장, 통째로 깎인 기준은 결과 없음). 반환 = 결과 수(outIds = NULL 이면 해 본 뒤 물려 개수만)
    """
    _a_baseIds = _n.array(_c.c_uint32, baseIds)
    _a_cutIds = _n.array(_c.c_uint32, cutIds)
    return _f.CAD_BooleanSubtract(_a_baseIds, baseCount, _a_cutIds, cutCount, keepOriginals, perBase, outIds, capacity)


def CAD_CheckInterference(ids: Sequence | None, count: int, createObjects: bool, out: Any, capacity: int) -> int:
    """C: int32_t CAD_CheckInterference(const uint32_t* ids, uint32_t count, bool createObjects, CAD_InterferenceInfo* out, uint32_t capacity)
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_CheckInterference(_a_ids, count, createObjects, out, capacity)


def CAD_ExplodeView(argsJson: str | None) -> str | None:
    """C: int32_t CAD_ExplodeView(const char* argsJson, char* buf, uint32_t capacity)

    분해도·조립 설명서 — AI 액션 explode·MCP 도구 explode_view 와 같은 창구. argsJson = {"op":"status|solve|auto|clear|amount|play|back|
    part|spin|balloons|bom|manual", ids, id, t, seconds, turns, dir[3], distance, step, show, path, paper}. 결과 JSON(ok·error·t·steps·parts·items…).
    글자 출력 규칙(int32_t 전체 길이, buf = NULL 이면 길이만) — 2회 호출(길이 → 버퍼)은 첫 호출에서 한 번만 실행한다.
    argsJson NULL·빈 글 = {} (status), JSON 객체가 아니면 CAD_E_INVALID_ARG. op 의 성공·실패는 결과 JSON 의 ok·error. manual 은 여러 프레임 작업 — status 의 manual_busy 로 끝을 본다
    """
    _need = _f.CAD_ExplodeView(_n.text(argsJson), None, 0)   # 2회 호출 규약: 길이를 물으며 한 번 실행
    if _need < 0:
        return None
    _cap = _need + 1
    _buf = _c.create_string_buffer(_cap)
    if _f.CAD_ExplodeView(_n.text(argsJson), _buf, _cap) < 0:   # 같은 인자 → 다시 실행하지 않고 결과만
        return None
    return _n.decode(_buf.value)


def CAD_SetFeatureDimensionsVisible(visible: bool) -> int:
    """C: CAD_Status CAD_SetFeatureDimensionsVisible(bool visible)

    피처 치수 (솔리드웍스 Instant3D 식)
    솔리드를 만든 치수. 상자: 가로·세로·높이 / 원기둥: 지름·높이 / 돌출: 높이 + 단면·컷 스케치의 원 지름, 직사각형 가로·세로. 값은 월드 mm.
    일반 폴리선 단면(12꼭짓점까지)은 변마다 길이 — 바꾸면 그 변 끝 너머 꼭짓점을 같이 민다(STRETCH, 직각 유지).
    kind: 0=가로 1=세로 2=높이 3=지름 4=변 5=위치(원 컷·원 보스 중심 — 바닥 단면 모서리에서 거리, 바꾸면 그 원 스케치를 옮긴다).
    sketchId = 값이 사는 스케치(0 = 솔리드 자체). 위치 치수는 크기 치수 뒤에 붙는다(기존 번호는 그대로).
    Set 은 다시 만들기, 되돌리기 1 — 모양을 못 만드는 값이면 CAD_E_FAILED + 이유(바꾸지 않음), 번호 밖 = CAD_E_OUT_OF_RANGE.
    Visible = 선택한 솔리드 위에 파란 치수 표시(명령 fdim, 상태바 "치수") — 더블클릭하면 그 자리에서 고친다
    """
    return _f.CAD_SetFeatureDimensionsVisible(visible)


def CAD_GetFeatureDimensionsVisible() -> tuple[int, bool]:
    """C: CAD_Status CAD_GetFeatureDimensionsVisible(bool* outVisible)

    피처 치수 (솔리드웍스 Instant3D 식)
    솔리드를 만든 치수. 상자: 가로·세로·높이 / 원기둥: 지름·높이 / 돌출: 높이 + 단면·컷 스케치의 원 지름, 직사각형 가로·세로. 값은 월드 mm.
    일반 폴리선 단면(12꼭짓점까지)은 변마다 길이 — 바꾸면 그 변 끝 너머 꼭짓점을 같이 민다(STRETCH, 직각 유지).
    kind: 0=가로 1=세로 2=높이 3=지름 4=변 5=위치(원 컷·원 보스 중심 — 바닥 단면 모서리에서 거리, 바꾸면 그 원 스케치를 옮긴다).
    sketchId = 값이 사는 스케치(0 = 솔리드 자체). 위치 치수는 크기 치수 뒤에 붙는다(기존 번호는 그대로).
    Set 은 다시 만들기, 되돌리기 1 — 모양을 못 만드는 값이면 CAD_E_FAILED + 이유(바꾸지 않음), 번호 밖 = CAD_E_OUT_OF_RANGE.
    Visible = 선택한 솔리드 위에 파란 치수 표시(명령 fdim, 상태바 "치수") — 더블클릭하면 그 자리에서 고친다
    """
    outVisible = _c.c_bool()
    _r = _f.CAD_GetFeatureDimensionsVisible(_c.byref(outVisible))
    return (_r, outVisible.value)


def CAD_GetFeatureDimensionCount(id: int) -> int:
    """C: int32_t CAD_GetFeatureDimensionCount(uint32_t id)

    피처 치수 (솔리드웍스 Instant3D 식)
    솔리드를 만든 치수. 상자: 가로·세로·높이 / 원기둥: 지름·높이 / 돌출: 높이 + 단면·컷 스케치의 원 지름, 직사각형 가로·세로. 값은 월드 mm.
    일반 폴리선 단면(12꼭짓점까지)은 변마다 길이 — 바꾸면 그 변 끝 너머 꼭짓점을 같이 민다(STRETCH, 직각 유지).
    kind: 0=가로 1=세로 2=높이 3=지름 4=변 5=위치(원 컷·원 보스 중심 — 바닥 단면 모서리에서 거리, 바꾸면 그 원 스케치를 옮긴다).
    sketchId = 값이 사는 스케치(0 = 솔리드 자체). 위치 치수는 크기 치수 뒤에 붙는다(기존 번호는 그대로).
    Set 은 다시 만들기, 되돌리기 1 — 모양을 못 만드는 값이면 CAD_E_FAILED + 이유(바꾸지 않음), 번호 밖 = CAD_E_OUT_OF_RANGE.
    Visible = 선택한 솔리드 위에 파란 치수 표시(명령 fdim, 상태바 "치수") — 더블클릭하면 그 자리에서 고친다
    """
    return _f.CAD_GetFeatureDimensionCount(id)


def CAD_GetFeatureDimension(id: int, index: int) -> tuple[int, int, float, int]:
    """C: CAD_Status CAD_GetFeatureDimension(uint32_t id, uint32_t index, int32_t* outKind, double* outValue, uint32_t* outSketchId)

    피처 치수 (솔리드웍스 Instant3D 식)
    솔리드를 만든 치수. 상자: 가로·세로·높이 / 원기둥: 지름·높이 / 돌출: 높이 + 단면·컷 스케치의 원 지름, 직사각형 가로·세로. 값은 월드 mm.
    일반 폴리선 단면(12꼭짓점까지)은 변마다 길이 — 바꾸면 그 변 끝 너머 꼭짓점을 같이 민다(STRETCH, 직각 유지).
    kind: 0=가로 1=세로 2=높이 3=지름 4=변 5=위치(원 컷·원 보스 중심 — 바닥 단면 모서리에서 거리, 바꾸면 그 원 스케치를 옮긴다).
    sketchId = 값이 사는 스케치(0 = 솔리드 자체). 위치 치수는 크기 치수 뒤에 붙는다(기존 번호는 그대로).
    Set 은 다시 만들기, 되돌리기 1 — 모양을 못 만드는 값이면 CAD_E_FAILED + 이유(바꾸지 않음), 번호 밖 = CAD_E_OUT_OF_RANGE.
    Visible = 선택한 솔리드 위에 파란 치수 표시(명령 fdim, 상태바 "치수") — 더블클릭하면 그 자리에서 고친다
    """
    outKind = _c.c_int32()
    outValue = _c.c_double()
    outSketchId = _c.c_uint32()
    _r = _f.CAD_GetFeatureDimension(id, index, _c.byref(outKind), _c.byref(outValue), _c.byref(outSketchId))
    return (_r, outKind.value, outValue.value, outSketchId.value)


def CAD_SetFeatureDimension(id: int, index: int, value: float) -> int:
    """C: CAD_Status CAD_SetFeatureDimension(uint32_t id, uint32_t index, double value)

    피처 치수 (솔리드웍스 Instant3D 식)
    솔리드를 만든 치수. 상자: 가로·세로·높이 / 원기둥: 지름·높이 / 돌출: 높이 + 단면·컷 스케치의 원 지름, 직사각형 가로·세로. 값은 월드 mm.
    일반 폴리선 단면(12꼭짓점까지)은 변마다 길이 — 바꾸면 그 변 끝 너머 꼭짓점을 같이 민다(STRETCH, 직각 유지).
    kind: 0=가로 1=세로 2=높이 3=지름 4=변 5=위치(원 컷·원 보스 중심 — 바닥 단면 모서리에서 거리, 바꾸면 그 원 스케치를 옮긴다).
    sketchId = 값이 사는 스케치(0 = 솔리드 자체). 위치 치수는 크기 치수 뒤에 붙는다(기존 번호는 그대로).
    Set 은 다시 만들기, 되돌리기 1 — 모양을 못 만드는 값이면 CAD_E_FAILED + 이유(바꾸지 않음), 번호 밖 = CAD_E_OUT_OF_RANGE.
    Visible = 선택한 솔리드 위에 파란 치수 표시(명령 fdim, 상태바 "치수") — 더블클릭하면 그 자리에서 고친다
    """
    return _f.CAD_SetFeatureDimension(id, index, value)
