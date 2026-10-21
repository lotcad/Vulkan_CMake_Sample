# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Transform 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_SetTransform', 'CAD_GetTransform']

_f = _n.native

_n.bind("CAD_SetTransform", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_GetTransform", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float)])


def CAD_SetTransform(id: int, x: float, y: float, z: float, qx: float, qy: float, qz: float, qw: float) -> bool:
    """C: bool CAD_SetTransform(uint32_t id, float x, float y, float z, float qx, float qy, float qz, float qw)

    외부가 매 프레임 자세를 밀어넣는 경로 — 로봇 관절, 모션캡처, 시뮬레이터, ROS Pose.
    SetPosition + SetRotationAxisAngle 을 따로 부르면 호출이 두 배가 되고, 두 호출
    사이에 프레임이 끼면 "옮겨졌지만 아직 안 돌아간" 한 프레임이 보인다.

    ⚠️ 쿼터니언 성분 순서는 **(qx, qy, qz, qw)** — ROS geometry_msgs/Quaternion 과 동일.
    (glm::quat 생성자는 (w,x,y,z) 순이라 내부에서 바꿔 넣는다. 혼동 주의)
    정규화는 엔진이 한다. 길이 0 / NaN 이면 대입하지 않고 false.

    좌표계 참고 — 엔진은 ROS(REP-103)와 같은 Z-up 우수좌표계라 축 변환이 필요 없다.
    다만 전방 축이 다르다: ROS +X 전방, 엔진 +Y 전방 → 필요하면 yaw 90도만 보정.
    """
    return _f.CAD_SetTransform(id, x, y, z, qx, qy, qz, qw)


def CAD_GetTransform(id: int) -> tuple[float, float, float, float, float, float, float] | None:
    """C: bool CAD_GetTransform(uint32_t id, float* x, float* y, float* z, float* qx, float* qy, float* qz, float* qw)

    외부가 매 프레임 자세를 밀어넣는 경로 — 로봇 관절, 모션캡처, 시뮬레이터, ROS Pose.
    SetPosition + SetRotationAxisAngle 을 따로 부르면 호출이 두 배가 되고, 두 호출
    사이에 프레임이 끼면 "옮겨졌지만 아직 안 돌아간" 한 프레임이 보인다.

    ⚠️ 쿼터니언 성분 순서는 **(qx, qy, qz, qw)** — ROS geometry_msgs/Quaternion 과 동일.
    (glm::quat 생성자는 (w,x,y,z) 순이라 내부에서 바꿔 넣는다. 혼동 주의)
    정규화는 엔진이 한다. 길이 0 / NaN 이면 대입하지 않고 false.

    좌표계 참고 — 엔진은 ROS(REP-103)와 같은 Z-up 우수좌표계라 축 변환이 필요 없다.
    다만 전방 축이 다르다: ROS +X 전방, 엔진 +Y 전방 → 필요하면 yaw 90도만 보정.
    """
    x = _c.c_float()
    y = _c.c_float()
    z = _c.c_float()
    qx = _c.c_float()
    qy = _c.c_float()
    qz = _c.c_float()
    qw = _c.c_float()
    if not _f.CAD_GetTransform(id, _c.byref(x), _c.byref(y), _c.byref(z), _c.byref(qx), _c.byref(qy), _c.byref(qz), _c.byref(qw)):
        return None
    return (x.value, y.value, z.value, qx.value, qy.value, qz.value, qw.value)
