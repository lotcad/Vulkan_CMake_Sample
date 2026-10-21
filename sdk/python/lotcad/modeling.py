# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Modeling 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_CreateEllipse', 'CAD_CreateSpline', 'CAD_CreateLeader', 'CAD_StretchWindowXY', 'CAD_Lengthen', 'CAD_BreakObject', 'CAD_CheckInterference', 'CAD_CheckMesh', 'CAD_RepairMeshes', 'CAD_RepairMeshesEx', 'CAD_SmoothMeshes', 'CAD_DecimateMeshes', 'CAD_StitchMeshes', 'CAD_ThickenMeshes', 'CAD_RemeshMeshes', 'CAD_AddEdgeBevel', 'CAD_GetEdgeBevelCount', 'CAD_Array3DRect', 'CAD_Array3DPolar', 'CAD_Align3D', 'CAD_CreateWedge', 'CAD_CreatePyramid', 'CAD_CreateSphere', 'CAD_CreateCylinder', 'CAD_CreateCone', 'CAD_CreateTorus', 'CAD_CreateHatch', 'CAD_Plot', 'CAD_ExplodeView', 'CAD_WindTunnel', 'CAD_Water', 'CAD_StructuralAnalysis', 'CAD_GetMcpToolsJson', 'CAD_Offset', 'CAD_Mirror', 'CAD_Trim', 'CAD_Extend', 'CAD_CreateTube', 'CAD_SetFeatureDimensionsVisible', 'CAD_GetFeatureDimensionsVisible', 'CAD_GetFeatureDimensionCount', 'CAD_GetFeatureDimension', 'CAD_SetFeatureDimension', 'CAD_Sweep', 'CAD_Revolve', 'CAD_ApplyMaterial', 'CAD_GetMaterialCount', 'CAD_GetMaterialName', 'CAD_CaptureViewport', 'CAD_OrbitCamera', 'CAD_ShowMessage']

_f = _n.native

_n.bind("CAD_CreateEllipse", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateSpline", _c.c_uint32, [_c.POINTER(_c.c_float), _c.c_uint32, _c.c_bool])
_n.bind("CAD_CreateLeader", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_char_p, _c.c_float])
_n.bind("CAD_StretchWindowXY", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_Lengthen", _c.c_bool, [_c.c_uint32, _c.c_int, _c.c_float, _c.c_bool])
_n.bind("CAD_BreakObject", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CheckInterference", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool, _c.POINTER(CAD_InterferenceInfo), _c.c_uint32])
_n.bind("CAD_CheckMesh", _c.c_bool, [_c.c_uint32, _c.POINTER(CAD_MeshCheckInfo)])
_n.bind("CAD_RepairMeshes", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool])
_n.bind("CAD_RepairMeshesEx", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool, _c.c_bool])
_n.bind("CAD_SmoothMeshes", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_int])
_n.bind("CAD_DecimateMeshes", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_double])
_n.bind("CAD_StitchMeshes", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_float])
_n.bind("CAD_ThickenMeshes", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_double])
_n.bind("CAD_RemeshMeshes", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_double])
_n.bind("CAD_AddEdgeBevel", _c.c_bool, [_c.c_uint32, _c.c_bool, _c.c_float, _c.c_bool, _c.c_uint32])
_n.bind("CAD_GetEdgeBevelCount", _c.c_uint32, [_c.c_uint32])
_n.bind("CAD_Array3DRect", _c.c_bool, [_c.c_int, _c.c_int, _c.c_int, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_Array3DPolar", _c.c_bool, [_c.c_int, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_bool])
_n.bind("CAD_Align3D", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.c_int])
_n.bind("CAD_CreateWedge", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreatePyramid", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_int, _c.c_float])
_n.bind("CAD_CreateSphere", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateCylinder", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateCone", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateTorus", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateHatch", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_char_p, _c.c_float, _c.c_float])
_n.bind("CAD_Plot", _c.c_bool, [_c.c_char_p, _c.c_bool, _c.c_bool, _c.c_float, _c.c_float, _c.c_int])
_n.bind("CAD_ExplodeView", _c.c_int, [_c.c_char_p, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_WindTunnel", _c.c_int, [_c.c_char_p, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_Water", _c.c_int, [_c.c_char_p, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_StructuralAnalysis", _c.c_int, [_c.c_char_p, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetMcpToolsJson", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_Offset", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_Mirror", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_bool, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_Trim", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_Extend", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateTube", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_SetFeatureDimensionsVisible", None, [_c.c_bool])
_n.bind("CAD_GetFeatureDimensionsVisible", _c.c_bool, [])
_n.bind("CAD_GetFeatureDimensionCount", _c.c_uint32, [_c.c_uint32])
_n.bind("CAD_GetFeatureDimension", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.POINTER(_c.c_int), _c.POINTER(_c.c_float), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetFeatureDimension", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.c_float])
_n.bind("CAD_Sweep", _c.c_uint32, [_c.c_uint32, _c.c_uint32])
_n.bind("CAD_Revolve", _c.c_uint32, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_int])
_n.bind("CAD_ApplyMaterial", _c.c_bool, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_GetMaterialCount", _c.c_uint32, [])
_n.bind("CAD_GetMaterialName", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_CaptureViewport", _c.c_bool, [_c.c_char_p, _c.c_bool])
_n.bind("CAD_OrbitCamera", None, [_c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_ShowMessage", None, [_c.c_char_p, _c.c_float])


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


def CAD_CreateLeader(tipX: float, tipY: float, tipZ: float, bendX: float, bendY: float, bendZ: float, textUtf8: str | None, textHeight: float) -> int:
    """C: uint32_t CAD_CreateLeader(float tipX, float tipY, float tipZ, float bendX, float bendY, float bendZ, const char* textUtf8, float textHeight)

    지시선 — 화살촉 → 꺾임 점 + 글(UTF-8, 여러 줄은 \\n). textHeight<=0 이면 2.5. 평면은 XY. 실패 0.
    """
    return _f.CAD_CreateLeader(tipX, tipY, tipZ, bendX, bendY, bendZ, _n.text(textUtf8), textHeight)


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


def CAD_CheckInterference(ids: Sequence | None, count: int, createObjects: bool, out: Any, cap: int) -> int:
    """C: uint32_t CAD_CheckInterference(const uint32_t* ids, uint32_t count, bool createObjects, CAD_InterferenceInfo* out, uint32_t cap)
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_CheckInterference(_a_ids, count, createObjects, out, cap)


def CAD_CheckMesh(id: int) -> CAD_MeshCheckInfo | None:
    """C: bool CAD_CheckMesh(uint32_t id, CAD_MeshCheckInfo* out)
    """
    out = CAD_MeshCheckInfo()
    if not _f.CAD_CheckMesh(id, _c.byref(out)):
        return None
    return out


def CAD_RepairMeshes(ids: Sequence | None, count: int, fillHoles: bool) -> int:
    """C: uint32_t CAD_RepairMeshes(const uint32_t* ids, uint32_t count, bool fillHoles)

    메시 수리 — ids 의 메시(null 이면 보이는 메시 전부)를 붙이기·퇴화/중복 제거·방향 통일·구멍 메움. 반환 = 고친 객체 수.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_RepairMeshes(_a_ids, count, fillHoles)


def CAD_RepairMeshesEx(ids: Sequence | None, count: int, fillHoles: bool, curvedFill: bool) -> int:
    """C: uint32_t CAD_RepairMeshesEx(const uint32_t* ids, uint32_t count, bool fillHoles, bool curvedFill)

    구멍 메우기 방식 지정판 — curvedFill: 둘레 곡면을 따라 둥글게(CAD_RepairMeshes 기본) / false = 평평하게.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_RepairMeshesEx(_a_ids, count, fillHoles, curvedFill)


def CAD_SmoothMeshes(ids: Sequence | None, count: int, iterations: int) -> int:
    """C: uint32_t CAD_SmoothMeshes(const uint32_t* ids, uint32_t count, int iterations)

    메시 매끈하게(토빈 — 부피가 거의 안 준다, 모서리는 둥글어진다). ids 가 비면 선택 메시(없으면 보이는 메시 전부). undo 1. 반환: 바꾼 개수.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_SmoothMeshes(_a_ids, count, iterations)


def CAD_DecimateMeshes(ids: Sequence | None, count: int, ratio: float) -> int:
    """C: uint32_t CAD_DecimateMeshes(const uint32_t* ids, uint32_t count, double ratio)

    삼각형 줄이기(QEM) — ratio = 남길 비율(0~1 사이). 경계 윤곽은 거의 그대로. undo 1. 반환: 바꾼 개수(0 = 대상 없음/범위 밖).
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_DecimateMeshes(_a_ids, count, ratio)


def CAD_StitchMeshes(ids: Sequence | None, count: int, tolerance: float) -> int:
    """C: uint32_t CAD_StitchMeshes(const uint32_t* ids, uint32_t count, float tolerance)

    틈 꿰매기 — tolerance(모델 로컬 단위) 안의 경계 점을 붙이고 T 이음을 쪼개 잇는다. 0 = 자동(대각선의 0.1%). 이미 닫힌 메시는 건너뜀.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_StitchMeshes(_a_ids, count, tolerance)


def CAD_ThickenMeshes(ids: Sequence | None, count: int, thickness: float) -> int:
    """C: uint32_t CAD_ThickenMeshes(const uint32_t* ids, uint32_t count, double thickness)

    두께 주기 — 열린 메시를 법선 방향으로 thickness 만큼 두껍게 해 닫힌 솔리드로(음수 = 반대쪽, 0 은 거부). 닫힌 메시는 건너뜀.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_ThickenMeshes(_a_ids, count, thickness)


def CAD_RemeshMeshes(ids: Sequence | None, count: int, edgeLength: float) -> int:
    """C: uint32_t CAD_RemeshMeshes(const uint32_t* ids, uint32_t count, double edgeLength)

    다시 나누기(등방 리메시) — edgeLength = 목표 모서리 길이(0 = 지금 평균). 경계·날카로운 모서리(45°↑)는 그대로.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_RemeshMeshes(_a_ids, count, edgeLength)


def CAD_AddEdgeBevel(id: int, fillet: bool, distance: float, allEdges: bool, brepEdge: int) -> bool:
    """C: bool CAD_AddEdgeBevel(uint32_t id, bool fillet, float distance, bool allEdges, uint32_t brepEdge)

    모서리 가공 기록 — B-Rep 솔리드에 필렛/모따기 하나를 더한다(스케치가 바뀌어도 다시 적용).
    allEdges = 볼록 모서리 전부, 아니면 brepEdge(B-Rep 선 모서리 id). distance = 모델 로컬 단위. 안 먹으면 false(변화 없음).
    """
    return _f.CAD_AddEdgeBevel(id, fillet, distance, allEdges, brepEdge)


def CAD_GetEdgeBevelCount(id: int) -> int:
    """C: uint32_t CAD_GetEdgeBevelCount(uint32_t id)
    """
    return _f.CAD_GetEdgeBevelCount(id)


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


def CAD_CreateWedge(x: float, y: float, z: float, sx: float, sy: float, sz: float) -> int:
    """C: uint32_t CAD_CreateWedge(float x, float y, float z, float sx, float sy, float sz)

    솔리드 — 밑면 중심(월드) 위에 +Z 로 선다. 실패 0.
      쐐기 sx·sy 밑면, sz 높이 / 피라미드 외접 반지름·높이·변 수(3~64)·윗면 반지름(0 = 뾰족) / 관 바깥·안 반지름·높이
    """
    return _f.CAD_CreateWedge(x, y, z, sx, sy, sz)


def CAD_CreatePyramid(x: float, y: float, z: float, radius: float, height: float, sides: int, topRadius: float) -> int:
    """C: uint32_t CAD_CreatePyramid(float x, float y, float z, float radius, float height, int sides, float topRadius)
    """
    return _f.CAD_CreatePyramid(x, y, z, radius, height, sides, topRadius)


def CAD_CreateSphere(x: float, y: float, z: float, radius: float) -> int:
    """C: uint32_t CAD_CreateSphere(float x, float y, float z, float radius)

    구·원기둥·원뿔·토러스 — (x,y,z) = 밑면 중심(구·토러스는 바닥에 닿는 점), 축 = +Z. 닫힌 메시, 선택 + undo 1. 잘못된 크기면 0.
    """
    return _f.CAD_CreateSphere(x, y, z, radius)


def CAD_CreateCylinder(x: float, y: float, z: float, radius: float, height: float) -> int:
    """C: uint32_t CAD_CreateCylinder(float x, float y, float z, float radius, float height)
    """
    return _f.CAD_CreateCylinder(x, y, z, radius, height)


def CAD_CreateCone(x: float, y: float, z: float, radius: float, height: float) -> int:
    """C: uint32_t CAD_CreateCone(float x, float y, float z, float radius, float height)
    """
    return _f.CAD_CreateCone(x, y, z, radius, height)


def CAD_CreateTorus(x: float, y: float, z: float, majorRadius: float, minorRadius: float) -> int:
    """C: uint32_t CAD_CreateTorus(float x, float y, float z, float majorRadius, float minorRadius)
    """
    return _f.CAD_CreateTorus(x, y, z, majorRadius, minorRadius)


def CAD_CreateHatch(ids: Sequence | None, count: int, pattern: str | None, scale: float, angleDeg: float) -> int:
    """C: uint32_t CAD_CreateHatch(const uint32_t* ids, uint32_t count, const char* pattern, float scale, float angleDeg)

    해치 — 닫힌 폴리선·사각형·원 ids(같은 평면이면 한 객체, 안쪽 루프 = 구멍). pattern: SOLID ANSI31~38 NET LINE DOTS BRICK STEEL CROSS
    (null/빈 = ANSI31), scale > 0, angleDeg. 선택이 새 해치로 바뀐다. 반환 = 해치 id, 실패 0.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_CreateHatch(_a_ids, count, _n.text(pattern), scale, angleDeg)


def CAD_Plot(path: str | None, selectedOnly: bool, monochrome: bool, paperW: float, paperH: float, pngLongSidePx: int) -> bool:
    """C: bool CAD_Plot(const char* path, bool selectedOnly, bool monochrome, float paperW, float paperH, int pngLongSidePx)

    도면 출력 — path 확장자로 .pdf(벡터)/.png(래스터). 지금 뷰 방향, 흰 종이. paperW/H mm(0 = A3 가로 420×297), pngLongSidePx(0 = 4000).
    selectedOnly = 선택만, monochrome = 흑백. 3D 메시·이미지는 아직 안 나온다.
    """
    return _f.CAD_Plot(_n.text(path), selectedOnly, monochrome, paperW, paperH, pngLongSidePx)


def CAD_ExplodeView(argsJson: str | None) -> str | None:
    """C: int CAD_ExplodeView(const char* argsJson, char* outUtf8, int cap)

    분해도·조립 설명서 — AI 액션 explode·MCP 도구 explode_view 와 같은 창구. argsJson = {"op":"status|solve|auto|clear|amount|play|back|
    part|spin|balloons|bom|manual", ids, id, t, seconds, turns, dir[3], distance, step, show, path, paper}. 결과 JSON(ok·error·t·steps·parts·items…)
    을 outUtf8 에(cap 바이트, null 이면 길이만). 반환 = 길이, 실패 -1. manual 은 여러 프레임 작업 — status 의 manual_busy 로 끝을 본다.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_ExplodeView(_n.text(argsJson), _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_WindTunnel(argsJson: str | None) -> str | None:
    """C: int CAD_WindTunnel(const char* argsJson, char* outUtf8, int cap)

    해석 — MCP 도구 wind_tunnel · water · structural_analysis 와 같은 창구(엔진 windTunnelOp·waterOp·simOp). argsJson = {"op": …, …}
    (없으면 status), 결과 JSON(ok·error·message·상태)을 outUtf8 에(cap 바이트, null 이면 길이만). 반환 = 길이, 실패 -1.
    켜기(start)는 다음 프레임에, 구조 해석 풀이(run·converge)는 작업 스레드에서 — status 로 끝을 본다.
    2회 호출(outUtf8 null 로 길이 → 버퍼)은 첫 호출에서 한 번만 실행하고, 같은 인자의 다음 호출엔 그 결과를 준다.
     바람 터널: status · start {ids|id, grid fast|normal|fine, wind 0.02~0.10} · stop · reset · pause · play ·
                view {field speed|pressure|vortex|smoke, plane x|y|z, at 0~1, smoke, surface} · wind {value}      — 바람은 +X
     물:        status · start {id(그릇), level 0~1, grid} · stop · reset · pause · play · tilt {x, y 도} · shake {amplitude 0~1, period}
     구조 해석: status(faces = 면 번호·넓이·가운데·법선) · open {id} · close · clear · run · cancel · converge(요소 × 0.7 로 한 번 더) ·
                set {type stress|heat|modal|buckling, material, size, units mm|m, modes, thermal, ref_temp, wind, wind_speed, show, scale, animate} ·
                fix|free {face} · force {face, force[3] N} · pressure {face, value MPa} · temp {face, value °C} · flux {face, value W} · convect {face, h, ambient}
                face = 번호 또는 그 면 가까운 점 [x,y,z]. 결과는 status 의 result(응력·변위·안전율·온도·진동수·좌굴 배수·convergence).
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_WindTunnel(_n.text(argsJson), _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_Water(argsJson: str | None) -> str | None:
    """C: int CAD_Water(const char* argsJson, char* outUtf8, int cap)
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_Water(_n.text(argsJson), _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_StructuralAnalysis(argsJson: str | None) -> str | None:
    """C: int CAD_StructuralAnalysis(const char* argsJson, char* outUtf8, int cap)
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_StructuralAnalysis(_n.text(argsJson), _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetMcpToolsJson() -> str | None:
    """C: int CAD_GetMcpToolsJson(char* outUtf8, int cap)

    MCP 도구 목록(JSON 배열) — 엔진을 만들지 않아도 된다. LotCAD --mcp 브리지가 앱이 꺼져 있을 때 목록을 보여 주는 데 쓴다.
    반환 = 길이, 실패 -1.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetMcpToolsJson(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


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
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_Mirror(_a_ids, count, x1, y1, z1, x2, y2, z2, nx, ny, nz, deleteOriginals, outIds, outCapacity)


def CAD_Trim(id: int, px: float, py: float, pz: float, boundaryIds: Sequence | None, boundaryCount: int, nx: float, ny: float, nz: float) -> bool:
    """C: bool CAD_Trim(uint32_t id, float px, float py, float pz, const uint32_t* boundaryIds, uint32_t boundaryCount, float nx, float ny, float nz)
    """
    _a_boundaryIds = _n.array(_c.c_uint32, boundaryIds)
    return _f.CAD_Trim(id, px, py, pz, _a_boundaryIds, boundaryCount, nx, ny, nz)


def CAD_Extend(id: int, px: float, py: float, pz: float, boundaryIds: Sequence | None, boundaryCount: int, nx: float, ny: float, nz: float) -> bool:
    """C: bool CAD_Extend(uint32_t id, float px, float py, float pz, const uint32_t* boundaryIds, uint32_t boundaryCount, float nx, float ny, float nz)
    """
    _a_boundaryIds = _n.array(_c.c_uint32, boundaryIds)
    return _f.CAD_Extend(id, px, py, pz, _a_boundaryIds, boundaryCount, nx, ny, nz)


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
    """
    return _f.CAD_GetFeatureDimensionsVisible()


def CAD_GetFeatureDimensionCount(id: int) -> int:
    """C: uint32_t CAD_GetFeatureDimensionCount(uint32_t id)
    """
    return _f.CAD_GetFeatureDimensionCount(id)


def CAD_GetFeatureDimension(id: int, index: int) -> tuple[int, float, int] | None:
    """C: bool CAD_GetFeatureDimension(uint32_t id, uint32_t index, int* outKind, float* outValue, uint32_t* outSketchId)
    """
    outKind = _c.c_int()
    outValue = _c.c_float()
    outSketchId = _c.c_uint32()
    if not _f.CAD_GetFeatureDimension(id, index, _c.byref(outKind), _c.byref(outValue), _c.byref(outSketchId)):
        return None
    return (outKind.value, outValue.value, outSketchId.value)


def CAD_SetFeatureDimension(id: int, index: int, value: float) -> bool:
    """C: bool CAD_SetFeatureDimension(uint32_t id, uint32_t index, float value)
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


def CAD_ApplyMaterial(id: int, nameUtf8: str | None) -> bool:
    """C: bool CAD_ApplyMaterial(uint32_t id, const char* nameUtf8)

    재질 — textures/ 의 파일 이름(확장자 없이, 예 "wood_oak_veneer"). 이름에 metal·steel 이 들면 금속 셰이딩.
    nameUtf8 이 null/"" 이면 재질 빼기. 재질 패널 클릭과 같다(앱과 같이 undo 없음). 없는 이름·id 는 false.
    """
    return _f.CAD_ApplyMaterial(id, _n.text(nameUtf8))


def CAD_GetMaterialCount() -> int:
    """C: uint32_t CAD_GetMaterialCount(void)
    """
    return _f.CAD_GetMaterialCount()


def CAD_GetMaterialName(index: int) -> str | None:
    """C: int CAD_GetMaterialName(uint32_t index, char* buf, int bufLen)
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetMaterialName(index, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_CaptureViewport(pathUtf8: str | None, clean: bool) -> bool:
    """C: bool CAD_CaptureViewport(const char* pathUtf8, bool clean)

    화면 캡처 → PNG(창 전체). clean = 그리드·뷰큐브 없이. 한 프레임 그려 파일이 생겼는지까지 확인하고 돌아온다
    (엔진 틱 안 — 플러그인 콜백 등 — 에서 불리면 요청만 남기고 다음 프레임에 찍는다, true = 요청됨). AI 가 결과를 눈으로 볼 때.
    """
    return _f.CAD_CaptureViewport(_n.text(pathUtf8), clean)


def CAD_OrbitCamera(ax: float, ay: float, az: float, angleDeg: float) -> None:
    """C: void CAD_OrbitCamera(float ax, float ay, float az, float angleDeg)

    카메라 — 지금 궤도 중심 둘레로 (ax,ay,az) 축 angleDeg 만큼 돌리기. 턴테이블 = (0,0,1).
    """
    _f.CAD_OrbitCamera(ax, ay, az, angleDeg)


def CAD_ShowMessage(textUtf8: str | None, seconds: float) -> None:
    """C: void CAD_ShowMessage(const char* textUtf8, float seconds)

    상태줄 임시 안내(시연 자막 등). seconds <= 0 이면 지금 문구를 지운다.
    """
    _f.CAD_ShowMessage(_n.text(textUtf8), seconds)
