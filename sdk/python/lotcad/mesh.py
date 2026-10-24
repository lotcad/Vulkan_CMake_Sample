# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Mesh 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_CreateMesh', 'CAD_ReplaceMesh', 'CAD_CreateVolumeMesh', 'CAD_CreateLabelMeshes', 'CAD_CreatePointCloud', 'CAD_UpdatePointCloud', 'CAD_SetPointCloudSize', 'CAD_GetPointCloudCount', 'CAD_CheckMesh', 'CAD_RepairMeshes', 'CAD_RepairMeshesEx', 'CAD_SmoothMeshes', 'CAD_DecimateMeshes', 'CAD_StitchMeshes', 'CAD_ThickenMeshes', 'CAD_RemeshMeshes']

_f = _n.native

_n.bind("CAD_CreateMesh", _c.c_uint32, [_c.POINTER(_c.c_float), _c.c_uint, _c.POINTER(_c.c_uint), _c.c_uint, _c.POINTER(_c.c_float)])
_n.bind("CAD_ReplaceMesh", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.c_uint, _c.POINTER(_c.c_uint), _c.c_uint, _c.POINTER(_c.c_float)])
_n.bind("CAD_CreateVolumeMesh", _c.c_uint32, [_c.c_char_p, _c.c_float, _c.c_int])
_n.bind("CAD_CreateLabelMeshes", _c.c_uint32, [_c.c_char_p, _c.c_int])
_n.bind("CAD_CreatePointCloud", _c.c_uint32, [])
_n.bind("CAD_UpdatePointCloud", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.POINTER(_c.c_ubyte), _c.c_uint32])
_n.bind("CAD_SetPointCloudSize", _c.c_bool, [_c.c_uint32, _c.c_float])
_n.bind("CAD_GetPointCloudCount", _c.c_uint32, [_c.c_uint32])
_n.bind("CAD_CheckMesh", _c.c_bool, [_c.c_uint32, _c.POINTER(CAD_MeshCheckInfo)])
_n.bind("CAD_RepairMeshes", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool])
_n.bind("CAD_RepairMeshesEx", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool, _c.c_bool])
_n.bind("CAD_SmoothMeshes", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_int])
_n.bind("CAD_DecimateMeshes", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_double])
_n.bind("CAD_StitchMeshes", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_float])
_n.bind("CAD_ThickenMeshes", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_double])
_n.bind("CAD_RemeshMeshes", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_double])


def CAD_CreateMesh(xyz: Sequence | None, vertexCount: int, indices: Sequence | None, indexCount: int, normals: Sequence | None) -> int:
    """C: uint32_t CAD_CreateMesh(const float* xyz, unsigned int vertexCount, const unsigned int* indices, unsigned int indexCount, const float* normals)

    메시 객체 만들기·형상 바꿔 끼우기 — 플러그인 객체(lotcad_plugin.h 의 딱지)의 형상도 이것으로.
    xyz = 3*vertexCount, indices = 3*triangleCount. normals 는 NULL 가능(삼각형별 flat).
    """
    _a_xyz = _n.array(_c.c_float, xyz)
    _a_indices = _n.array(_c.c_uint, indices)
    _a_normals = _n.array(_c.c_float, normals)
    return _f.CAD_CreateMesh(_a_xyz, vertexCount, _a_indices, indexCount, _a_normals)


def CAD_ReplaceMesh(id: int, xyz: Sequence | None, vertexCount: int, indices: Sequence | None, indexCount: int, normals: Sequence | None) -> bool:
    """C: bool CAD_ReplaceMesh(uint32_t id, const float* xyz, unsigned int vertexCount, const unsigned int* indices, unsigned int indexCount, const float* normals)

    메시 객체 만들기·형상 바꿔 끼우기 — 플러그인 객체(lotcad_plugin.h 의 딱지)의 형상도 이것으로.
    xyz = 3*vertexCount, indices = 3*triangleCount. normals 는 NULL 가능(삼각형별 flat).
    """
    _a_xyz = _n.array(_c.c_float, xyz)
    _a_indices = _n.array(_c.c_uint, indices)
    _a_normals = _n.array(_c.c_float, normals)
    return _f.CAD_ReplaceMesh(id, _a_xyz, vertexCount, _a_indices, indexCount, _a_normals)


def CAD_CreateVolumeMesh(path: str | None, iso: float, step: int) -> int:
    """C: uint32_t CAD_CreateVolumeMesh(const char* path, float iso, int step)

    볼륨(CT/MR: .nrrd/.nhdr/.nii/.nii.gz) → 등가면 메시 객체. iso 는 값 문턱(NaN 이면 범위 중간, CT 뼈 ≈ 300, 피부 ≈ -300),
    step 은 복셀 건너뛰기(1=전부, 2=삼각형 1/4). 보통 mesh 객체(이름 "파일@iso")를 만들고 선택까지. 반환 id, 실패 0 + CAD_GetLastError.
    """
    return _f.CAD_CreateVolumeMesh(_n.text(path), iso, step)


def CAD_CreateLabelMeshes(path: str | None, step: int) -> int:
    """C: uint32_t CAD_CreateLabelMeshes(const char* path, int step)

    의료 분할(라벨 볼륨: 정수 라벨 0..N 의 .nii/.nrrd, TotalSegmentator 등) → 라벨마다 색 메시 객체(해부 이름, 도면층 "분할:<파일>").
    step 0=자동. 반환 = 만든 객체 수, 실패 0 + CAD_GetLastError. 트랜잭션 한 단계.
    """
    return _f.CAD_CreateLabelMeshes(_n.text(path), step)


def CAD_CreatePointCloud() -> int:
    """C: uint32_t CAD_CreatePointCloud(void)

    생성과 갱신이 분리돼 있다. 센서는 초당 수십 번 갱신하는데, 그때마다 객체를 지웠다
    만들면 ID 가 바뀌어 선택·트랜스폼이 매번 풀린다. 한 번 만들고 계속 Update 한다.

    uint32_t pc = CAD_CreatePointCloud();
    매 스캔마다
    CAD_UpdatePointCloud(pc, xyz, rgba, count);

    xyz  : 3 × count 개의 float (x,y,z 반복). 객체 로컬 좌표 — 센서 위치/자세는
    CAD_SetTransform 으로 따로 준다(점을 미리 변환하지 말 것. 그러면 매 프레임
    count 개를 CPU 에서 곱해야 한다).
    rgba : 4 × count 개의 uint8. NULL 이면 객체 색으로 단색 표시(LaserScan 처럼 색이 없는 소스).
    count: 점 개수. 0 이면 비운다.

    ⚠️ 규모 전제: **수만~수십만 점**. 수백만 점(측량 스캔)은 옥트리 LOD 가 있어야 하고,
    그건 이 API 위에 얹을 별도 레이어다 — 함수 모양은 그때도 바뀌지 않는다.
    갱신은 GPU 스톨 없이 host-visible 버퍼 memcpy 로 처리된다(매 프레임 호출해도 안전).
    """
    return _f.CAD_CreatePointCloud()


def CAD_UpdatePointCloud(id: int, xyz: Sequence | None, rgba: Sequence | None, count: int) -> bool:
    """C: bool CAD_UpdatePointCloud(uint32_t id, const float* xyz, const unsigned char* rgba, uint32_t count)
    """
    _a_xyz = _n.array(_c.c_float, xyz)
    _a_rgba = _n.array(_c.c_ubyte, rgba)
    return _f.CAD_UpdatePointCloud(id, _a_xyz, _a_rgba, count)


def CAD_SetPointCloudSize(id: int, pointSizePx: float) -> bool:
    """C: bool CAD_SetPointCloudSize(uint32_t id, float pointSizePx)

    화면 픽셀 크기 (1~64 로 클램프). 기본 2.
    """
    return _f.CAD_SetPointCloudSize(id, pointSizePx)


def CAD_GetPointCloudCount(id: int) -> int:
    """C: uint32_t CAD_GetPointCloudCount(uint32_t id)

    화면 픽셀 크기 (1~64 로 클램프). 기본 2.
    """
    return _f.CAD_GetPointCloudCount(id)


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
