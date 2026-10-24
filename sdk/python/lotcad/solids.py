# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Solids 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_MAX_BREP_PROFILE_POINTS', 'CAD_CreateBox', 'CAD_PushPullSelectedFace', 'CAD_InsetSelectedFace', 'CAD_CreateExtrude', 'CAD_GetBRepInfo', 'CAD_GetBRepParameters', 'CAD_SetBRepBoxDimensions', 'CAD_SetBRepCylinderDimensions', 'CAD_SetBRepExtrudeHeight', 'CAD_GetBRepFaceInfo', 'CAD_PushPullBRepFace', 'CAD_CutExtrudeBRep', 'CAD_CutExtrudeFromSketch', 'CAD_BossExtrudeBRep', 'CAD_BossExtrudeFromSketch', 'CAD_GetBRepBossCount', 'CAD_GetBRepBossHeight', 'CAD_SetBRepBossHeight', 'CAD_GetBRepCutCount', 'CAD_GetBRepCutInfo', 'CAD_GetBRepCutProfile', 'CAD_SetBRepCut', 'CAD_SetBRepCutFromSketch', 'CAD_RemoveBRepFeatures', 'CAD_RemoveBRepCut', 'CAD_RemoveBRepBoss', 'CAD_GetBooleanCylinderCutCount', 'CAD_GetBooleanCylinderCutInfo', 'CAD_SetBooleanCylinderCut', 'CAD_RebuildBRepMesh', 'CAD_Loft', 'CAD_Shell', 'CAD_EdgeFillet', 'CAD_EdgeChamfer', 'CAD_BooleanUnion', 'CAD_BooleanIntersection', 'CAD_BooleanDifference', 'CAD_BooleanUnionIds', 'CAD_BooleanIntersectionIds', 'CAD_BooleanSubtract', 'CAD_CheckInterference', 'CAD_AddEdgeBevel', 'CAD_GetEdgeBevelCount', 'CAD_CreateWedge', 'CAD_CreatePyramid', 'CAD_CreateSphere', 'CAD_CreateCylinder', 'CAD_CreateCone', 'CAD_CreateTorus', 'CAD_ExplodeView', 'CAD_CreateTube', 'CAD_SetFeatureDimensionsVisible', 'CAD_GetFeatureDimensionsVisible', 'CAD_GetFeatureDimensionCount', 'CAD_GetFeatureDimension', 'CAD_SetFeatureDimension', 'CAD_Sweep', 'CAD_Revolve']

_f = _n.native

CAD_MAX_BREP_PROFILE_POINTS = 2048

_n.bind("CAD_CreateBox", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_PushPullSelectedFace", _c.c_bool, [_c.c_float])
_n.bind("CAD_InsetSelectedFace", _c.c_bool, [_c.c_float])
_n.bind("CAD_CreateExtrude", _c.c_uint32, [_c.c_uint32, _c.c_float])
_n.bind("CAD_GetBRepInfo", _c.c_bool, [_c.c_uint32, _c.POINTER(CAD_BRepInfo)])
_n.bind("CAD_GetBRepParameters", _c.c_bool, [_c.c_uint32, _c.POINTER(CAD_BRepParameters)])
_n.bind("CAD_SetBRepBoxDimensions", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_SetBRepCylinderDimensions", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float])
_n.bind("CAD_SetBRepExtrudeHeight", _c.c_bool, [_c.c_uint32, _c.c_float])
_n.bind("CAD_GetBRepFaceInfo", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.POINTER(CAD_BRepFaceInfo)])
_n.bind("CAD_PushPullBRepFace", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.c_float])
_n.bind("CAD_CutExtrudeBRep", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.c_uint32, _c.c_float, _c.c_bool])
_n.bind("CAD_CutExtrudeFromSketch", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.c_float, _c.c_bool])
_n.bind("CAD_BossExtrudeBRep", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.c_uint32, _c.c_float])
_n.bind("CAD_BossExtrudeFromSketch", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.c_float])
_n.bind("CAD_GetBRepBossCount", _c.c_uint32, [_c.c_uint32])
_n.bind("CAD_GetBRepBossHeight", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.POINTER(_c.c_float)])
_n.bind("CAD_SetBRepBossHeight", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.c_float])
_n.bind("CAD_GetBRepCutCount", _c.c_uint32, [_c.c_uint32])
_n.bind("CAD_GetBRepCutInfo", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.POINTER(CAD_BRepCutInfo)])
_n.bind("CAD_GetBRepCutProfile", _c.c_uint32, [_c.c_uint32, _c.c_uint32, _c.POINTER(_c.c_float), _c.c_uint32])
_n.bind("CAD_SetBRepCut", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.POINTER(_c.c_float), _c.c_uint32, _c.c_float, _c.c_bool])
_n.bind("CAD_SetBRepCutFromSketch", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.c_uint32, _c.c_float, _c.c_bool])
_n.bind("CAD_RemoveBRepFeatures", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_uint32), _c.c_uint32, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_RemoveBRepCut", _c.c_bool, [_c.c_uint32, _c.c_uint32])
_n.bind("CAD_RemoveBRepBoss", _c.c_bool, [_c.c_uint32, _c.c_uint32])
_n.bind("CAD_GetBooleanCylinderCutCount", _c.c_uint32, [_c.c_uint32])
_n.bind("CAD_GetBooleanCylinderCutInfo", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.POINTER(CAD_BooleanCylinderCutInfo)])
_n.bind("CAD_SetBooleanCylinderCut", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_RebuildBRepMesh", _c.c_bool, [_c.c_uint32, _c.c_uint32])
_n.bind("CAD_Loft", _c.c_bool, [])
_n.bind("CAD_Shell", _c.c_bool, [_c.c_float])
_n.bind("CAD_EdgeFillet", _c.c_bool, [_c.c_float])
_n.bind("CAD_EdgeChamfer", _c.c_bool, [_c.c_float])
_n.bind("CAD_BooleanUnion", None, [_c.c_bool])
_n.bind("CAD_BooleanIntersection", None, [_c.c_bool])
_n.bind("CAD_BooleanDifference", None, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool])
_n.bind("CAD_BooleanUnionIds", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool])
_n.bind("CAD_BooleanIntersectionIds", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool])
_n.bind("CAD_BooleanSubtract", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool, _c.c_bool, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_CheckInterference", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool, _c.POINTER(CAD_InterferenceInfo), _c.c_uint32])
_n.bind("CAD_AddEdgeBevel", _c.c_bool, [_c.c_uint32, _c.c_bool, _c.c_float, _c.c_bool, _c.c_uint32])
_n.bind("CAD_GetEdgeBevelCount", _c.c_uint32, [_c.c_uint32])
_n.bind("CAD_CreateWedge", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreatePyramid", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_int, _c.c_float])
_n.bind("CAD_CreateSphere", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateCylinder", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateCone", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateTorus", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_ExplodeView", _c.c_int, [_c.c_char_p, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_CreateTube", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_SetFeatureDimensionsVisible", None, [_c.c_bool])
_n.bind("CAD_GetFeatureDimensionsVisible", _c.c_bool, [])
_n.bind("CAD_GetFeatureDimensionCount", _c.c_uint32, [_c.c_uint32])
_n.bind("CAD_GetFeatureDimension", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.POINTER(_c.c_int), _c.POINTER(_c.c_float), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetFeatureDimension", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.c_float])
_n.bind("CAD_Sweep", _c.c_uint32, [_c.c_uint32, _c.c_uint32])
_n.bind("CAD_Revolve", _c.c_uint32, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_int])


def CAD_CreateBox(x: float, y: float, z: float, sx: float, sy: float, sz: float) -> int:
    """C: uint32_t CAD_CreateBox(float x, float y, float z, float sx, float sy, float sz)
    """
    return _f.CAD_CreateBox(x, y, z, sx, sy, sz)


def CAD_PushPullSelectedFace(distance: float) -> bool:
    """C: bool CAD_PushPullSelectedFace(float distance)

    선택한 면(면 선택 모드에서 클릭한 면)을 법선 방향으로 distance(mm, 양수=바깥) 밀어 새 메시로 — undo 1단계.
    면 선택이 없으면 false.
    """
    return _f.CAD_PushPullSelectedFace(distance)


def CAD_InsetSelectedFace(distance: float) -> bool:
    """C: bool CAD_InsetSelectedFace(float distance)

    선택한 평면의 볼록 면에 distance(mm) 폭의 안쪽 링을 만든다. distance=0 이면 자동 폭.
    면 선택이 없거나 오목/다중 경계 면이면 false. undo 1단계.
    """
    return _f.CAD_InsetSelectedFace(distance)


def CAD_CreateExtrude(sourceId: int, height: float) -> int:
    """C: uint32_t CAD_CreateExtrude(uint32_t sourceId, float height)
    """
    return _f.CAD_CreateExtrude(sourceId, height)


def CAD_GetBRepInfo(id: int) -> CAD_BRepInfo | None:
    """C: bool CAD_GetBRepInfo(uint32_t id, CAD_BRepInfo* outInfo)
    """
    outInfo = CAD_BRepInfo()
    if not _f.CAD_GetBRepInfo(id, _c.byref(outInfo)):
        return None
    return outInfo


def CAD_GetBRepParameters(id: int) -> CAD_BRepParameters | None:
    """C: bool CAD_GetBRepParameters(uint32_t id, CAD_BRepParameters* outParams)
    """
    outParams = CAD_BRepParameters()
    if not _f.CAD_GetBRepParameters(id, _c.byref(outParams)):
        return None
    return outParams


def CAD_SetBRepBoxDimensions(id: int, x: float, y: float, z: float) -> bool:
    """C: bool CAD_SetBRepBoxDimensions(uint32_t id, float x, float y, float z)
    """
    return _f.CAD_SetBRepBoxDimensions(id, x, y, z)


def CAD_SetBRepCylinderDimensions(id: int, radius: float, height: float) -> bool:
    """C: bool CAD_SetBRepCylinderDimensions(uint32_t id, float radius, float height)
    """
    return _f.CAD_SetBRepCylinderDimensions(id, radius, height)


def CAD_SetBRepExtrudeHeight(id: int, height: float) -> bool:
    """C: bool CAD_SetBRepExtrudeHeight(uint32_t id, float height)
    """
    return _f.CAD_SetBRepExtrudeHeight(id, height)


def CAD_GetBRepFaceInfo(id: int, faceId: int) -> CAD_BRepFaceInfo | None:
    """C: bool CAD_GetBRepFaceInfo(uint32_t id, uint32_t faceId, CAD_BRepFaceInfo* outInfo)
    """
    outInfo = CAD_BRepFaceInfo()
    if not _f.CAD_GetBRepFaceInfo(id, faceId, _c.byref(outInfo)):
        return None
    return outInfo


def CAD_PushPullBRepFace(id: int, faceId: int, distance: float) -> bool:
    """C: bool CAD_PushPullBRepFace(uint32_t id, uint32_t faceId, float distance)

    지정 면을 바깥쪽으로 이동한다. 박스 평면은 반대편 면을 고정하고,
    원통 옆면(surfaceType=1)은 반지름을 변경하며, 돌출체 옆면은 프로파일 변을 평행 이동한다.
    distance는 월드 단위다.
    """
    return _f.CAD_PushPullBRepFace(id, faceId, distance)


def CAD_CutExtrudeBRep(id: int, profileXYZ: Sequence | None, pointCount: int, depth: float, throughAll: bool) -> bool:
    """C: bool CAD_CutExtrudeBRep(uint32_t id, const float* profileXYZ, uint32_t pointCount, float depth, bool throughAll)
    """
    _a_profileXYZ = _n.array(_c.c_float, profileXYZ)
    return _f.CAD_CutExtrudeBRep(id, _a_profileXYZ, pointCount, depth, throughAll)


def CAD_CutExtrudeFromSketch(id: int, sketchId: int, depth: float, throughAll: bool) -> bool:
    """C: bool CAD_CutExtrudeFromSketch(uint32_t id, uint32_t sketchId, float depth, bool throughAll)

    기존 닫힌 2D 스케치를 프로파일로 사용한다. 스케치의 월드 변환을 대상 솔리드의
    로컬 좌표로 자동 변환하므로 화면에서 그린 사각형·원·폴리선을 바로 사용할 수 있다.
    """
    return _f.CAD_CutExtrudeFromSketch(id, sketchId, depth, throughAll)


def CAD_BossExtrudeBRep(id: int, profileXYZ: Sequence | None, pointCount: int, height: float) -> bool:
    """C: bool CAD_BossExtrudeBRep(uint32_t id, const float* profileXYZ, uint32_t pointCount, float height)

    보스(더하는 돌출) — Extrude 솔리드의 캡 안쪽에 폐프로파일을 쌓는다(피처 기록에 남아 치수·재생성이 된다).
    height > 0 = 위 캡에서 위로, < 0 = 아래 캡에서 아래로. 발자국이 외곽에 닿거나 같은 쪽 보스와 겹치거나
    기존 컷 테두리를 가로지르면 false. 이미 있던 관통 컷은 보스까지 관통한다.
    """
    _a_profileXYZ = _n.array(_c.c_float, profileXYZ)
    return _f.CAD_BossExtrudeBRep(id, _a_profileXYZ, pointCount, height)


def CAD_BossExtrudeFromSketch(id: int, sketchId: int, height: float) -> bool:
    """C: bool CAD_BossExtrudeFromSketch(uint32_t id, uint32_t sketchId, float height)

    닫힌 스케치로 — 스케치가 가까운 캡(위/아래) 쪽으로 height(양수) 만큼. 스케치가 바뀌면 다시 만든다.
    """
    return _f.CAD_BossExtrudeFromSketch(id, sketchId, height)


def CAD_GetBRepBossCount(id: int) -> int:
    """C: uint32_t CAD_GetBRepBossCount(uint32_t id)

    닫힌 스케치로 — 스케치가 가까운 캡(위/아래) 쪽으로 height(양수) 만큼. 스케치가 바뀌면 다시 만든다.
    """
    return _f.CAD_GetBRepBossCount(id)


def CAD_GetBRepBossHeight(id: int, bossIndex: int) -> float | None:
    """C: bool CAD_GetBRepBossHeight(uint32_t id, uint32_t bossIndex, float* outHeight)

    보스 높이 읽기·바꾸기(부호 = 위/아래). 바꾸기는 undo 1.
    """
    outHeight = _c.c_float()
    if not _f.CAD_GetBRepBossHeight(id, bossIndex, _c.byref(outHeight)):
        return None
    return outHeight.value


def CAD_SetBRepBossHeight(id: int, bossIndex: int, height: float) -> bool:
    """C: bool CAD_SetBRepBossHeight(uint32_t id, uint32_t bossIndex, float height)

    보스 높이 읽기·바꾸기(부호 = 위/아래). 바꾸기는 undo 1.
    """
    return _f.CAD_SetBRepBossHeight(id, bossIndex, height)


def CAD_GetBRepCutCount(id: int) -> int:
    """C: uint32_t CAD_GetBRepCutCount(uint32_t id)
    """
    return _f.CAD_GetBRepCutCount(id)


def CAD_GetBRepCutInfo(id: int, cutIndex: int) -> CAD_BRepCutInfo | None:
    """C: bool CAD_GetBRepCutInfo(uint32_t id, uint32_t cutIndex, CAD_BRepCutInfo* outInfo)
    """
    outInfo = CAD_BRepCutInfo()
    if not _f.CAD_GetBRepCutInfo(id, cutIndex, _c.byref(outInfo)):
        return None
    return outInfo


def CAD_GetBRepCutProfile(id: int, cutIndex: int, outXYZ: Any, capacity: int) -> int:
    """C: uint32_t CAD_GetBRepCutProfile(uint32_t id, uint32_t cutIndex, float* outXYZ, uint32_t capacity)

    필요한 점 개수를 반환한다. outXYZ가 null이거나 capacity가 작으면 복사하지 않는다.
    """
    return _f.CAD_GetBRepCutProfile(id, cutIndex, outXYZ, capacity)


def CAD_SetBRepCut(id: int, cutIndex: int, profileXYZ: Sequence | None, pointCount: int, depth: float, throughAll: bool) -> bool:
    """C: bool CAD_SetBRepCut(uint32_t id, uint32_t cutIndex, const float* profileXYZ, uint32_t pointCount, float depth, bool throughAll)

    기존 컷의 프로파일과 관통/포켓 깊이를 교체한다. cutIndex는 GetBRepCutInfo의 값이다.
    profileXYZ는 대상 솔리드의 객체 로컬 좌표이며, 임포트한 폐폴리라인 좌표도 사용할 수 있다.
    """
    _a_profileXYZ = _n.array(_c.c_float, profileXYZ)
    return _f.CAD_SetBRepCut(id, cutIndex, _a_profileXYZ, pointCount, depth, throughAll)


def CAD_SetBRepCutFromSketch(id: int, cutIndex: int, sketchId: int, depth: float, throughAll: bool) -> bool:
    """C: bool CAD_SetBRepCutFromSketch(uint32_t id, uint32_t cutIndex, uint32_t sketchId, float depth, bool throughAll)

    닫힌 엔진 스케치(직접 그린 형상 또는 DXF 등에서 변환한 형상)로 기존 컷을 교체한다.
    """
    return _f.CAD_SetBRepCutFromSketch(id, cutIndex, sketchId, depth, throughAll)


def CAD_RemoveBRepFeatures(id: int, cutIndices: Sequence | None, cutCount: int, bossIndices: Sequence | None, bossCount: int) -> bool:
    """C: bool CAD_RemoveBRepFeatures(uint32_t id, const uint32_t* cutIndices, uint32_t cutCount, const uint32_t* bossIndices, uint32_t bossCount)

    컷·보스 지우기(솔리드웍스 피처 삭제처럼) — 여러 개를 한 번에 빼고 남은 것으로 한 번 다시 만든다. 그 피처만 쓰던 스케치도 지운다.
    번호는 CAD_GetBRepCutInfo / 보스 순서(지우기 전 번호 — 지운 뒤엔 뒤쪽 번호가 당겨진다). 되돌리기 한 단계.
    남은 것으로 모양을 못 만들면(보스를 지워 그 안 컷이 허공에 남음 등) 아무것도 안 바꾸고 false + CAD_GetLastError.
    """
    _a_cutIndices = _n.array(_c.c_uint32, cutIndices)
    _a_bossIndices = _n.array(_c.c_uint32, bossIndices)
    return _f.CAD_RemoveBRepFeatures(id, _a_cutIndices, cutCount, _a_bossIndices, bossCount)


def CAD_RemoveBRepCut(id: int, cutIndex: int) -> bool:
    """C: bool CAD_RemoveBRepCut(uint32_t id, uint32_t cutIndex)

    하나만 — CAD_RemoveBRepFeatures 와 같다

    묶음 주석: 컷·보스 지우기(솔리드웍스 피처 삭제처럼) — 여러 개를 한 번에 빼고 남은 것으로 한 번 다시 만든다. 그 피처만 쓰던 스케치도 지운다.
    번호는 CAD_GetBRepCutInfo / 보스 순서(지우기 전 번호 — 지운 뒤엔 뒤쪽 번호가 당겨진다). 되돌리기 한 단계.
    남은 것으로 모양을 못 만들면(보스를 지워 그 안 컷이 허공에 남음 등) 아무것도 안 바꾸고 false + CAD_GetLastError.
    """
    return _f.CAD_RemoveBRepCut(id, cutIndex)


def CAD_RemoveBRepBoss(id: int, bossIndex: int) -> bool:
    """C: bool CAD_RemoveBRepBoss(uint32_t id, uint32_t bossIndex)

    컷·보스 지우기(솔리드웍스 피처 삭제처럼) — 여러 개를 한 번에 빼고 남은 것으로 한 번 다시 만든다. 그 피처만 쓰던 스케치도 지운다.
    번호는 CAD_GetBRepCutInfo / 보스 순서(지우기 전 번호 — 지운 뒤엔 뒤쪽 번호가 당겨진다). 되돌리기 한 단계.
    남은 것으로 모양을 못 만들면(보스를 지워 그 안 컷이 허공에 남음 등) 아무것도 안 바꾸고 false + CAD_GetLastError.
    """
    return _f.CAD_RemoveBRepBoss(id, bossIndex)


def CAD_GetBooleanCylinderCutCount(id: int) -> int:
    """C: uint32_t CAD_GetBooleanCylinderCutCount(uint32_t id)
    """
    return _f.CAD_GetBooleanCylinderCutCount(id)


def CAD_GetBooleanCylinderCutInfo(id: int, cutIndex: int) -> CAD_BooleanCylinderCutInfo | None:
    """C: bool CAD_GetBooleanCylinderCutInfo(uint32_t id, uint32_t cutIndex, CAD_BooleanCylinderCutInfo* outInfo)
    """
    outInfo = CAD_BooleanCylinderCutInfo()
    if not _f.CAD_GetBooleanCylinderCutInfo(id, cutIndex, _c.byref(outInfo)):
        return None
    return outInfo


def CAD_SetBooleanCylinderCut(id: int, cutIndex: int, centerX: float, centerY: float, centerZ: float, axisX: float, axisY: float, axisZ: float, radius: float, height: float) -> bool:
    """C: bool CAD_SetBooleanCylinderCut(uint32_t id, uint32_t cutIndex, float centerX, float centerY, float centerZ, float axisX, float axisY, float axisZ, float radius, float height)
    """
    return _f.CAD_SetBooleanCylinderCut(id, cutIndex, centerX, centerY, centerZ, axisX, axisY, axisZ, radius, height)


def CAD_RebuildBRepMesh(id: int, curvedSegments: int) -> bool:
    """C: bool CAD_RebuildBRepMesh(uint32_t id, uint32_t curvedSegments)

    B-Rep 정의로 렌더 메시 캐시를 강제 재생성한다. 곡면 분할은 3~512로 제한된다.
    """
    return _f.CAD_RebuildBRepMesh(id, curvedSegments)


def CAD_Loft() -> bool:
    """C: bool CAD_Loft(void)

    로프트 — 선택된 **닫힌 단면 2개 이상**을 축 순서로 이어 솔리드 생성.
    단면이 지그재그로 놓여 순서를 직접 주고 싶으면 화면에서 클릭 순서로 지정해야 한다.
    """
    return _f.CAD_Loft()


def CAD_Shell(thickness: float) -> bool:
    """C: bool CAD_Shell(float thickness)

    셸 — 선택 솔리드의 속을 비우고 두께만 남긴다. thickness<=0 이면 크기에 맞춰 자동.
    """
    return _f.CAD_Shell(thickness)


def CAD_EdgeFillet(distance: float) -> bool:
    """C: bool CAD_EdgeFillet(float distance)

    모서리 필렛/챔퍼 — 선택 솔리드의 볼록 모서리를 굴리거나(fillet) 깎는다(chamfer).
    distance<=0 이면 객체 크기에 맞춰 자동.
    """
    return _f.CAD_EdgeFillet(distance)


def CAD_EdgeChamfer(distance: float) -> bool:
    """C: bool CAD_EdgeChamfer(float distance)

    모서리 필렛/챔퍼 — 선택 솔리드의 볼록 모서리를 굴리거나(fillet) 깎는다(chamfer).
    distance<=0 이면 객체 크기에 맞춰 자동.
    """
    return _f.CAD_EdgeChamfer(distance)


def CAD_BooleanUnion(keepOriginals: bool) -> None:
    """C: void CAD_BooleanUnion(bool keepOriginals)

    **요청형**(예전부터 있던 셋) — 반환값 없음, 다음 프레임에 실행. 결과 id·실패를 알 수 없다.
    Union/Intersection 은 **부른 순간의 선택**(메시만)이 대상. keepOriginals=false 면 원본 삭제(되돌리기 한 단계).
    결과가 필요하거나 여러 번 이어 부를 땐 아래 바로 실행형(CAD_BooleanUnionIds …)을 쓴다.
    """
    _f.CAD_BooleanUnion(keepOriginals)


def CAD_BooleanIntersection(keepOriginals: bool) -> None:
    """C: void CAD_BooleanIntersection(bool keepOriginals)

    **요청형**(예전부터 있던 셋) — 반환값 없음, 다음 프레임에 실행. 결과 id·실패를 알 수 없다.
    Union/Intersection 은 **부른 순간의 선택**(메시만)이 대상. keepOriginals=false 면 원본 삭제(되돌리기 한 단계).
    결과가 필요하거나 여러 번 이어 부를 땐 아래 바로 실행형(CAD_BooleanUnionIds …)을 쓴다.
    """
    _f.CAD_BooleanIntersection(keepOriginals)


def CAD_BooleanDifference(baseIds: Sequence | None, baseCount: int, subtractIds: Sequence | None, subtractCount: int, keepOriginals: bool) -> None:
    """C: void CAD_BooleanDifference(const uint32_t* baseIds, uint32_t baseCount, const uint32_t* subtractIds, uint32_t subtractCount, bool keepOriginals)

    Difference: union(baseIds) − union(subtractIds). id 배열 + 개수 전달.
    """
    _a_baseIds = _n.array(_c.c_uint32, baseIds)
    _a_subtractIds = _n.array(_c.c_uint32, subtractIds)
    _f.CAD_BooleanDifference(_a_baseIds, baseCount, _a_subtractIds, subtractCount, keepOriginals)


def CAD_BooleanUnionIds(ids: Sequence | None, count: int, keepOriginals: bool) -> int:
    """C: uint32_t CAD_BooleanUnionIds(const uint32_t* ids, uint32_t count, bool keepOriginals)

    **바로 실행형**(2026-10-04) — 부르면 그 자리에서 계산하고 결과를 돌려준다. 선택과 무관(넘긴 id 만),
    한 프레임에 여러 번 이어 불러도 된다. 공통 규칙:
    · 입력을 먼저 전부 검사 — 없는 id·메시 아님·잠긴 도면층·닫히지 않은 메시·중복(기준과 빼는 쪽 사이 포함)이
    하나라도 있으면 **아무것도 바꾸지 않고** 0, 이유는 CAD_GetLastError.
    · 결과(들) 추가 + 원본 삭제(keepOriginals=false) = 되돌리기 한 단계. 끝나면 결과만 선택된다.
    · 결과는 첫 원본(기준)의 이름·도면층·색·금속·불투명도를 이어받는다(텍스처는 안 이어받음 — UV 없음).
    · 여러 개는 한 번에 계산(Manifold BatchBoolean) — 순서 무관.
    합집합 — ids 2개 이상 → 한 객체(떨어져 있어도 한 객체에 덩어리 여럿). 결과 id, 실패 0.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_BooleanUnionIds(_a_ids, count, keepOriginals)


def CAD_BooleanIntersectionIds(ids: Sequence | None, count: int, keepOriginals: bool) -> int:
    """C: uint32_t CAD_BooleanIntersectionIds(const uint32_t* ids, uint32_t count, bool keepOriginals)

    교집합 — ids 2개 이상 **모두의** 공통 부분(A∩B∩C). 공통 부분이 없으면 0. 결과 id, 실패 0.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_BooleanIntersectionIds(_a_ids, count, keepOriginals)


def CAD_BooleanSubtract(baseIds: Sequence | None, baseCount: int, cutIds: Sequence | None, cutCount: int, keepOriginals: bool, perBase: bool, outIds: Any, cap: int) -> int:
    """C: uint32_t CAD_BooleanSubtract(const uint32_t* baseIds, uint32_t baseCount, const uint32_t* cutIds, uint32_t cutCount, bool keepOriginals, bool perBase, uint32_t* outIds, uint32_t cap)

    차집합 — 기준 baseIds 에서 cutIds 전부를 뺀다.
    perBase=false: union(기준) − union(빼는 것) → 결과 1개(기준들이 한 덩어리로 합쳐짐, 오토캐드 SUBTRACT 와 같음)
    perBase=true : 기준마다 따로(판 3장에 같은 구멍 → 판 3장). 통째로 깎여 사라진 기준은 결과가 없다.
    반환 = 결과 개수(실패 0), outIds 에 cap 개까지 결과 id. outIds=NULL 이면 **빼기는 하고** 개수만 — 같은 프레임에 같은 인자로
    버퍼를 들고 다시 부르면 다시 빼지 않고 그 결과 id 를 준다(2회 호출 규약). CAD_Offset·CAD_Mirror·CAD_CheckInterference 도 같다.
    """
    _a_baseIds = _n.array(_c.c_uint32, baseIds)
    _a_cutIds = _n.array(_c.c_uint32, cutIds)
    return _f.CAD_BooleanSubtract(_a_baseIds, baseCount, _a_cutIds, cutCount, keepOriginals, perBase, outIds, cap)


def CAD_CheckInterference(ids: Sequence | None, count: int, createObjects: bool, out: Any, cap: int) -> int:
    """C: uint32_t CAD_CheckInterference(const uint32_t* ids, uint32_t count, bool createObjects, CAD_InterferenceInfo* out, uint32_t cap)
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_CheckInterference(_a_ids, count, createObjects, out, cap)


def CAD_AddEdgeBevel(id: int, fillet: bool, distance: float, allEdges: bool, brepEdge: int) -> bool:
    """C: bool CAD_AddEdgeBevel(uint32_t id, bool fillet, float distance, bool allEdges, uint32_t brepEdge)

    모서리 가공 기록 — B-Rep 솔리드에 필렛/모따기 하나를 더한다(스케치가 바뀌어도 다시 적용).
    allEdges = 볼록 모서리 전부, 아니면 brepEdge(B-Rep 선 모서리 id). distance = 모델 로컬 단위. 안 먹으면 false(변화 없음).
    """
    return _f.CAD_AddEdgeBevel(id, fillet, distance, allEdges, brepEdge)


def CAD_GetEdgeBevelCount(id: int) -> int:
    """C: uint32_t CAD_GetEdgeBevelCount(uint32_t id)

    모서리 가공 기록 — B-Rep 솔리드에 필렛/모따기 하나를 더한다(스케치가 바뀌어도 다시 적용).
    allEdges = 볼록 모서리 전부, 아니면 brepEdge(B-Rep 선 모서리 id). distance = 모델 로컬 단위. 안 먹으면 false(변화 없음).
    """
    return _f.CAD_GetEdgeBevelCount(id)


def CAD_CreateWedge(x: float, y: float, z: float, sx: float, sy: float, sz: float) -> int:
    """C: uint32_t CAD_CreateWedge(float x, float y, float z, float sx, float sy, float sz)

    솔리드 — 밑면 중심(월드) 위에 +Z 로 선다. 실패 0.
      쐐기 sx·sy 밑면, sz 높이 / 피라미드 외접 반지름·높이·변 수(3~64)·윗면 반지름(0 = 뾰족) / 관 바깥·안 반지름·높이
    """
    return _f.CAD_CreateWedge(x, y, z, sx, sy, sz)


def CAD_CreatePyramid(x: float, y: float, z: float, radius: float, height: float, sides: int, topRadius: float) -> int:
    """C: uint32_t CAD_CreatePyramid(float x, float y, float z, float radius, float height, int sides, float topRadius)

    솔리드 — 밑면 중심(월드) 위에 +Z 로 선다. 실패 0.
      쐐기 sx·sy 밑면, sz 높이 / 피라미드 외접 반지름·높이·변 수(3~64)·윗면 반지름(0 = 뾰족) / 관 바깥·안 반지름·높이
    """
    return _f.CAD_CreatePyramid(x, y, z, radius, height, sides, topRadius)


def CAD_CreateSphere(x: float, y: float, z: float, radius: float) -> int:
    """C: uint32_t CAD_CreateSphere(float x, float y, float z, float radius)

    구·원기둥·원뿔·토러스 — (x,y,z) = 밑면 중심(구·토러스는 바닥에 닿는 점), 축 = +Z. 닫힌 메시, 선택 + undo 1. 잘못된 크기면 0.
    """
    return _f.CAD_CreateSphere(x, y, z, radius)


def CAD_CreateCylinder(x: float, y: float, z: float, radius: float, height: float) -> int:
    """C: uint32_t CAD_CreateCylinder(float x, float y, float z, float radius, float height)

    구·원기둥·원뿔·토러스 — (x,y,z) = 밑면 중심(구·토러스는 바닥에 닿는 점), 축 = +Z. 닫힌 메시, 선택 + undo 1. 잘못된 크기면 0.
    """
    return _f.CAD_CreateCylinder(x, y, z, radius, height)


def CAD_CreateCone(x: float, y: float, z: float, radius: float, height: float) -> int:
    """C: uint32_t CAD_CreateCone(float x, float y, float z, float radius, float height)

    구·원기둥·원뿔·토러스 — (x,y,z) = 밑면 중심(구·토러스는 바닥에 닿는 점), 축 = +Z. 닫힌 메시, 선택 + undo 1. 잘못된 크기면 0.
    """
    return _f.CAD_CreateCone(x, y, z, radius, height)


def CAD_CreateTorus(x: float, y: float, z: float, majorRadius: float, minorRadius: float) -> int:
    """C: uint32_t CAD_CreateTorus(float x, float y, float z, float majorRadius, float minorRadius)

    minor < major

    묶음 주석: 구·원기둥·원뿔·토러스 — (x,y,z) = 밑면 중심(구·토러스는 바닥에 닿는 점), 축 = +Z. 닫힌 메시, 선택 + undo 1. 잘못된 크기면 0.
    """
    return _f.CAD_CreateTorus(x, y, z, majorRadius, minorRadius)


def CAD_ExplodeView(argsJson: str | None) -> str | None:
    """C: int CAD_ExplodeView(const char* argsJson, char* outUtf8, int cap)

    분해도·조립 설명서 — AI 액션 explode·MCP 도구 explode_view 와 같은 창구. argsJson = {"op":"status|solve|auto|clear|amount|play|back|
    part|spin|balloons|bom|manual", ids, id, t, seconds, turns, dir[3], distance, step, show, path, paper}. 결과 JSON(ok·error·t·steps·parts·items…)
    을 outUtf8 에(cap 바이트, null 이면 길이만). 반환 = 길이, 실패 -1. manual 은 여러 프레임 작업 — status 의 manual_busy 로 끝을 본다.
    """
    _need = _f.CAD_ExplodeView(_n.text(argsJson), None, 0)   # 2회 호출 규약: 길이를 물으며 한 번 실행
    if _need < 0:
        return None
    _cap = _need + 1
    _buf = _c.create_string_buffer(_cap)
    if _f.CAD_ExplodeView(_n.text(argsJson), _buf, _cap) < 0:   # 같은 인자 → 다시 실행하지 않고 결과만
        return None
    return _n.decode(_buf.value)


def CAD_CreateTube(x: float, y: float, z: float, outerRadius: float, innerRadius: float, height: float) -> int:
    """C: uint32_t CAD_CreateTube(float x, float y, float z, float outerRadius, float innerRadius, float height)
    """
    return _f.CAD_CreateTube(x, y, z, outerRadius, innerRadius, height)


def CAD_SetFeatureDimensionsVisible(visible: bool) -> None:
    """C: void CAD_SetFeatureDimensionsVisible(bool visible)

    피처 치수 — 솔리드를 만든 치수(솔리드웍스 Instant3D 식). 상자: 가로·세로·높이 / 원기둥: 지름·높이 /
    돌출: 높이 + 단면·컷 스케치의 원 지름, 직사각형 가로·세로. 값은 월드 단위.
    일반 폴리선 단면(12꼭짓점까지)은 변마다 길이 — 바꾸면 그 변 끝 너머 꼭짓점을 같이 민다(STRETCH, 직각 유지).
    kind: 0=가로 1=세로 2=높이 3=지름 4=변 5=위치(원 컷·원 보스 중심 — 바닥 단면 모서리에서 거리, 바꾸면 그 원 스케치를 옮긴다).
    sketchId = 값이 사는 스케치(0 = 솔리드 자체). 위치 치수는 크기 치수 뒤에 붙는다(기존 번호는 그대로). 모양을 못 만드는 값이면 false + CAD_GetLastError.
    Set 은 재생성(스케치 치수는 스케치를 고쳐 피처가 다음 프레임에 따라온다), undo 1. 실패 false.
    Visible = 선택한 솔리드 위에 파란 치수 표시(명령 fdim, 상태바 "치수") — 더블클릭하면 명령행이 새 값을 기다린다.
    """
    _f.CAD_SetFeatureDimensionsVisible(visible)


def CAD_GetFeatureDimensionsVisible() -> bool:
    """C: bool CAD_GetFeatureDimensionsVisible(void)

    피처 치수 — 솔리드를 만든 치수(솔리드웍스 Instant3D 식). 상자: 가로·세로·높이 / 원기둥: 지름·높이 /
    돌출: 높이 + 단면·컷 스케치의 원 지름, 직사각형 가로·세로. 값은 월드 단위.
    일반 폴리선 단면(12꼭짓점까지)은 변마다 길이 — 바꾸면 그 변 끝 너머 꼭짓점을 같이 민다(STRETCH, 직각 유지).
    kind: 0=가로 1=세로 2=높이 3=지름 4=변 5=위치(원 컷·원 보스 중심 — 바닥 단면 모서리에서 거리, 바꾸면 그 원 스케치를 옮긴다).
    sketchId = 값이 사는 스케치(0 = 솔리드 자체). 위치 치수는 크기 치수 뒤에 붙는다(기존 번호는 그대로). 모양을 못 만드는 값이면 false + CAD_GetLastError.
    Set 은 재생성(스케치 치수는 스케치를 고쳐 피처가 다음 프레임에 따라온다), undo 1. 실패 false.
    Visible = 선택한 솔리드 위에 파란 치수 표시(명령 fdim, 상태바 "치수") — 더블클릭하면 명령행이 새 값을 기다린다.
    """
    return _f.CAD_GetFeatureDimensionsVisible()


def CAD_GetFeatureDimensionCount(id: int) -> int:
    """C: uint32_t CAD_GetFeatureDimensionCount(uint32_t id)

    피처 치수 — 솔리드를 만든 치수(솔리드웍스 Instant3D 식). 상자: 가로·세로·높이 / 원기둥: 지름·높이 /
    돌출: 높이 + 단면·컷 스케치의 원 지름, 직사각형 가로·세로. 값은 월드 단위.
    일반 폴리선 단면(12꼭짓점까지)은 변마다 길이 — 바꾸면 그 변 끝 너머 꼭짓점을 같이 민다(STRETCH, 직각 유지).
    kind: 0=가로 1=세로 2=높이 3=지름 4=변 5=위치(원 컷·원 보스 중심 — 바닥 단면 모서리에서 거리, 바꾸면 그 원 스케치를 옮긴다).
    sketchId = 값이 사는 스케치(0 = 솔리드 자체). 위치 치수는 크기 치수 뒤에 붙는다(기존 번호는 그대로). 모양을 못 만드는 값이면 false + CAD_GetLastError.
    Set 은 재생성(스케치 치수는 스케치를 고쳐 피처가 다음 프레임에 따라온다), undo 1. 실패 false.
    Visible = 선택한 솔리드 위에 파란 치수 표시(명령 fdim, 상태바 "치수") — 더블클릭하면 명령행이 새 값을 기다린다.
    """
    return _f.CAD_GetFeatureDimensionCount(id)


def CAD_GetFeatureDimension(id: int, index: int) -> tuple[int, float, int] | None:
    """C: bool CAD_GetFeatureDimension(uint32_t id, uint32_t index, int* outKind, float* outValue, uint32_t* outSketchId)

    피처 치수 — 솔리드를 만든 치수(솔리드웍스 Instant3D 식). 상자: 가로·세로·높이 / 원기둥: 지름·높이 /
    돌출: 높이 + 단면·컷 스케치의 원 지름, 직사각형 가로·세로. 값은 월드 단위.
    일반 폴리선 단면(12꼭짓점까지)은 변마다 길이 — 바꾸면 그 변 끝 너머 꼭짓점을 같이 민다(STRETCH, 직각 유지).
    kind: 0=가로 1=세로 2=높이 3=지름 4=변 5=위치(원 컷·원 보스 중심 — 바닥 단면 모서리에서 거리, 바꾸면 그 원 스케치를 옮긴다).
    sketchId = 값이 사는 스케치(0 = 솔리드 자체). 위치 치수는 크기 치수 뒤에 붙는다(기존 번호는 그대로). 모양을 못 만드는 값이면 false + CAD_GetLastError.
    Set 은 재생성(스케치 치수는 스케치를 고쳐 피처가 다음 프레임에 따라온다), undo 1. 실패 false.
    Visible = 선택한 솔리드 위에 파란 치수 표시(명령 fdim, 상태바 "치수") — 더블클릭하면 명령행이 새 값을 기다린다.
    """
    outKind = _c.c_int()
    outValue = _c.c_float()
    outSketchId = _c.c_uint32()
    if not _f.CAD_GetFeatureDimension(id, index, _c.byref(outKind), _c.byref(outValue), _c.byref(outSketchId)):
        return None
    return (outKind.value, outValue.value, outSketchId.value)


def CAD_SetFeatureDimension(id: int, index: int, value: float) -> bool:
    """C: bool CAD_SetFeatureDimension(uint32_t id, uint32_t index, float value)

    피처 치수 — 솔리드를 만든 치수(솔리드웍스 Instant3D 식). 상자: 가로·세로·높이 / 원기둥: 지름·높이 /
    돌출: 높이 + 단면·컷 스케치의 원 지름, 직사각형 가로·세로. 값은 월드 단위.
    일반 폴리선 단면(12꼭짓점까지)은 변마다 길이 — 바꾸면 그 변 끝 너머 꼭짓점을 같이 민다(STRETCH, 직각 유지).
    kind: 0=가로 1=세로 2=높이 3=지름 4=변 5=위치(원 컷·원 보스 중심 — 바닥 단면 모서리에서 거리, 바꾸면 그 원 스케치를 옮긴다).
    sketchId = 값이 사는 스케치(0 = 솔리드 자체). 위치 치수는 크기 치수 뒤에 붙는다(기존 번호는 그대로). 모양을 못 만드는 값이면 false + CAD_GetLastError.
    Set 은 재생성(스케치 치수는 스케치를 고쳐 피처가 다음 프레임에 따라온다), undo 1. 실패 false.
    Visible = 선택한 솔리드 위에 파란 치수 표시(명령 fdim, 상태바 "치수") — 더블클릭하면 명령행이 새 값을 기다린다.
    """
    return _f.CAD_SetFeatureDimension(id, index, value)


def CAD_Sweep(profileId: int, pathId: int) -> int:
    """C: uint32_t CAD_Sweep(uint32_t profileId, uint32_t pathId)

    스윕 — 닫힌 단면(원·사각형·닫힌 폴리선) id 를 열린 경로(폴리선·선) id 를 따라 쓸어 솔리드. 단면은 경로 시작점으로
    옮겨지고 경로 방향에 맞게 돌려진다(어디에 그렸든 된다). 새 솔리드는 선택되고 undo 1. 실패 0.
    """
    return _f.CAD_Sweep(profileId, pathId)


def CAD_Revolve(profileId: int, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, segments: int) -> int:
    """C: uint32_t CAD_Revolve(uint32_t profileId, float x1, float y1, float z1, float x2, float y2, float z2, int segments)

    회전체 — 단면 스케치(폴리선·원·사각형) id 를 축 (x1,y1,z1)→(x2,y2,z2) 둘레로 360°, segments 분할(0 = 32).
    새 솔리드는 선택되고 undo 1. 스윕과 같이 피처 기록이 남아 단면을 고치면 다시 만들어진다(피처 치수로도). 실패 0.
    """
    return _f.CAD_Revolve(profileId, x1, y1, z1, x2, y2, z2, segments)
