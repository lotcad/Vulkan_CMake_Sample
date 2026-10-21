# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — BRep 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_GetBRepInfo', 'CAD_GetBRepParameters', 'CAD_SetBRepBoxDimensions', 'CAD_SetBRepCylinderDimensions', 'CAD_SetBRepExtrudeHeight', 'CAD_GetBRepFaceInfo', 'CAD_PushPullBRepFace', 'CAD_CutExtrudeBRep', 'CAD_BossExtrudeBRep', 'CAD_GetBRepBossCount', 'CAD_GetBRepBossHeight', 'CAD_SetBRepBossHeight', 'CAD_GetBRepCutCount', 'CAD_GetBRepCutInfo', 'CAD_GetBRepCutProfile', 'CAD_SetBRepCut', 'CAD_SetBRepCutFromSketch', 'CAD_RemoveBRepFeatures', 'CAD_RemoveBRepCut', 'CAD_RemoveBRepBoss', 'CAD_GetBooleanCylinderCutCount', 'CAD_GetBooleanCylinderCutInfo', 'CAD_SetBooleanCylinderCut', 'CAD_RebuildBRepMesh', 'CAD_GetSelectedBRepFaceId']

_f = _n.native

_n.bind("CAD_GetBRepInfo", _c.c_bool, [_c.c_uint32, _c.POINTER(CAD_BRepInfo)])
_n.bind("CAD_GetBRepParameters", _c.c_bool, [_c.c_uint32, _c.POINTER(CAD_BRepParameters)])
_n.bind("CAD_SetBRepBoxDimensions", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_SetBRepCylinderDimensions", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float])
_n.bind("CAD_SetBRepExtrudeHeight", _c.c_bool, [_c.c_uint32, _c.c_float])
_n.bind("CAD_GetBRepFaceInfo", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.POINTER(CAD_BRepFaceInfo)])
_n.bind("CAD_PushPullBRepFace", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.c_float])
_n.bind("CAD_CutExtrudeBRep", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.c_uint32, _c.c_float, _c.c_bool])
_n.bind("CAD_BossExtrudeBRep", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.c_uint32, _c.c_float])
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
_n.bind("CAD_GetSelectedBRepFaceId", _c.c_int32, [])


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


def CAD_BossExtrudeBRep(id: int, profileXYZ: Sequence | None, pointCount: int, height: float) -> bool:
    """C: bool CAD_BossExtrudeBRep(uint32_t id, const float* profileXYZ, uint32_t pointCount, float height)

    보스(더하는 돌출) — Extrude 솔리드의 캡 안쪽에 폐프로파일을 쌓는다(피처 기록에 남아 치수·재생성이 된다).
    height > 0 = 위 캡에서 위로, < 0 = 아래 캡에서 아래로. 발자국이 외곽에 닿거나 같은 쪽 보스와 겹치거나
    기존 컷 테두리를 가로지르면 false. 이미 있던 관통 컷은 보스까지 관통한다.
    """
    _a_profileXYZ = _n.array(_c.c_float, profileXYZ)
    return _f.CAD_BossExtrudeBRep(id, _a_profileXYZ, pointCount, height)


def CAD_GetBRepBossCount(id: int) -> int:
    """C: uint32_t CAD_GetBRepBossCount(uint32_t id)
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
    """
    return _f.CAD_RemoveBRepCut(id, cutIndex)


def CAD_RemoveBRepBoss(id: int, bossIndex: int) -> bool:
    """C: bool CAD_RemoveBRepBoss(uint32_t id, uint32_t bossIndex)
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


def CAD_GetSelectedBRepFaceId() -> int:
    """C: int32_t CAD_GetSelectedBRepFaceId(void)

    현재 선택 면이 B-Rep 면이면 안정적인 face id, 아니면 -1.
    """
    return _f.CAD_GetSelectedBRepFaceId()
