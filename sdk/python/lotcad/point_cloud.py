# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — PointCloud 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_CreatePointCloud', 'CAD_UpdatePointCloud', 'CAD_SetPointCloudSize', 'CAD_GetPointCloudCount']

_f = _n.native

_n.bind("CAD_CreatePointCloud", _c.c_uint32, [])
_n.bind("CAD_UpdatePointCloud", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.POINTER(_c.c_ubyte), _c.c_uint32])
_n.bind("CAD_SetPointCloudSize", _c.c_bool, [_c.c_uint32, _c.c_float])
_n.bind("CAD_GetPointCloudCount", _c.c_uint32, [_c.c_uint32])


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

    Load an Effekseer .efkefc/.efk with referenced resources. Inserted stopped.
    CAD_SetParticlePlayback also controls these objects. Files embed in .lot.
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
