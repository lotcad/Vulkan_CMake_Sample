# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Robot 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_LoadUrdf', 'CAD_GetRobotCount', 'CAD_GetJointCount', 'CAD_FindJoint', 'CAD_GetJointName', 'CAD_SetJointValue', 'CAD_GetJointValue', 'CAD_SetJointValues', 'CAD_SetJointValuesByName', 'CAD_GetJointInfo', 'CAD_SetJointAxis', 'CAD_GetJointAxis', 'CAD_SetJointType', 'CAD_SetJointOrigin', 'CAD_GetJointOrigin', 'CAD_GetLinkObject', 'CAD_ClearRobots', 'CAD_RigAttach', 'CAD_RigDetach', 'CAD_GetObjectRobot']

_f = _n.native

_n.bind("CAD_LoadUrdf", _c.c_uint32, [_c.c_char_p])
_n.bind("CAD_GetRobotCount", _c.c_uint32, [])
_n.bind("CAD_GetJointCount", _c.c_uint32, [_c.c_uint32])
_n.bind("CAD_FindJoint", _c.c_int, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_GetJointName", _c.c_int, [_c.c_uint32, _c.c_int, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_SetJointValue", _c.c_float, [_c.c_uint32, _c.c_int, _c.c_float])
_n.bind("CAD_GetJointValue", _c.c_float, [_c.c_uint32, _c.c_int])
_n.bind("CAD_SetJointValues", _c.c_uint32, [_c.c_uint32, _c.POINTER(_c.c_int), _c.POINTER(_c.c_float), _c.c_uint32])
_n.bind("CAD_SetJointValuesByName", _c.c_uint32, [_c.c_uint32, _c.POINTER(_c.c_char_p), _c.POINTER(_c.c_float), _c.c_uint32])
_n.bind("CAD_GetJointInfo", _c.c_bool, [_c.c_uint32, _c.c_int, _c.POINTER(_c.c_int), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_bool)])
_n.bind("CAD_SetJointAxis", _c.c_bool, [_c.c_uint32, _c.c_int, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_GetJointAxis", _c.c_bool, [_c.c_uint32, _c.c_int, _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float)])
_n.bind("CAD_SetJointType", _c.c_bool, [_c.c_uint32, _c.c_int, _c.c_int])
_n.bind("CAD_SetJointOrigin", _c.c_bool, [_c.c_uint32, _c.c_int, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_GetJointOrigin", _c.c_bool, [_c.c_uint32, _c.c_int, _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float)])
_n.bind("CAD_GetLinkObject", _c.c_uint32, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_ClearRobots", None, [])
_n.bind("CAD_RigAttach", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.c_int, _c.c_float, _c.c_float, _c.c_float, _c.c_bool])
_n.bind("CAD_RigDetach", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_GetObjectRobot", _c.c_uint32, [_c.c_uint32])


def CAD_LoadUrdf(path: str | None) -> int:
    """C: uint32_t CAD_LoadUrdf(const char* path)

    URDF 는 ROS 의 로봇 정의 포맷이지만 파일 자체는 XML 이라 **ROS 없이도** 읽고 그린다.
    좌표계도 맞는다 — URDF 와 이 엔진 둘 다 Z-up 우수좌표계·미터라 축 변환이 없다.

    uint32_t r = CAD_LoadUrdf("models/demo_arm.urdf");   // 0 = 실패, 아니면 로봇 인덱스+1
    CAD_SetJointValue(r, CAD_FindJoint(r, "joint_elbow"), 0.7f);   // 라디안

    조인트는 1자유도다 — URDF <axis> 가 축이고 값은 그 축의 회전각(revolute, 라디안)
    또는 이동거리(prismatic, 미터). 한계가 있으면 엔진이 잘라 넣는다.

    로봇 핸들은 **1부터** — 0 을 실패로 쓰기 위해서다. 내부 인덱스 = handle-1.
    지원 형상: box / cylinder / sphere. mesh(STL/DAE) 링크는 아직 건너뛴다.
    """
    return _f.CAD_LoadUrdf(_n.text(path))


def CAD_GetRobotCount() -> int:
    """C: uint32_t CAD_GetRobotCount(void)
    """
    return _f.CAD_GetRobotCount()


def CAD_GetJointCount(robot: int) -> int:
    """C: uint32_t CAD_GetJointCount(uint32_t robot)
    """
    return _f.CAD_GetJointCount(robot)


def CAD_FindJoint(robot: int, jointName: str | None) -> int:
    """C: int CAD_FindJoint(uint32_t robot, const char* jointName)

    조인트 이름 → 인덱스. 없으면 -1. (ROS 는 이름으로 오므로 필요)
    """
    return _f.CAD_FindJoint(robot, _n.text(jointName))


def CAD_GetJointName(robot: int, jointIdx: int) -> str | None:
    """C: int CAD_GetJointName(uint32_t robot, int jointIdx, char* outUtf8, int cap)
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetJointName(robot, jointIdx, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_SetJointValue(robot: int, jointIdx: int, value: float) -> float:
    """C: float CAD_SetJointValue(uint32_t robot, int jointIdx, float value)

    값 대입/조회. 반환은 한계로 잘린 **실제 적용값**.
    """
    return _f.CAD_SetJointValue(robot, jointIdx, value)


def CAD_GetJointValue(robot: int, jointIdx: int) -> float:
    """C: float CAD_GetJointValue(uint32_t robot, int jointIdx)
    """
    return _f.CAD_GetJointValue(robot, jointIdx)


def CAD_SetJointValues(robot: int, jointIdx: Sequence | None, values: Sequence | None, count: int) -> int:
    """C: uint32_t CAD_SetJointValues(uint32_t robot, const int* jointIdx, const float* values, uint32_t count)

    ROS 의 sensor_msgs/JointState 는 관절 전부를 한 메시지에 담아 초당 수십 번 보낸다.
    하나씩 넣으면 관절 수만큼 계층 트리를 다시 푸느라 헛일을 한다 — 여기선 **마지막에 한 번만** 푼다.
    반환: 실제로 적용된 개수(범위 밖·고정 조인트는 건너뜀).
    """
    _a_jointIdx = _n.array(_c.c_int, jointIdx)
    _a_values = _n.array(_c.c_float, values)
    return _f.CAD_SetJointValues(robot, _a_jointIdx, _a_values, count)


def CAD_SetJointValuesByName(robot: int, names: Sequence[str] | None, values: Sequence | None, count: int) -> int:
    """C: uint32_t CAD_SetJointValuesByName(uint32_t robot, const char* const* names, const float* values, uint32_t count)

    이름으로 받는 판 — ROS 는 인덱스가 아니라 이름으로 온다. JointState 콜백에 그대로 꽂힌다.
    CAD_SetJointValuesByName(r, msg.name.data(), msg.position.data(), msg.name.size());
    """
    _a_names = _n.text_array(names)
    _a_values = _n.array(_c.c_float, values)
    return _f.CAD_SetJointValuesByName(robot, _a_names, _a_values, count)


def CAD_GetJointInfo(robot: int, jointIdx: int) -> tuple[int, float, float, bool] | None:
    """C: bool CAD_GetJointInfo(uint32_t robot, int jointIdx, int* outType, float* outLower, float* outUpper, bool* outHasLimit)

    한계와 종류(0=fixed 1=revolute 2=continuous 3=prismatic). hasLimit=false 면 lower/upper 무의미.
    """
    outType = _c.c_int()
    outLower = _c.c_float()
    outUpper = _c.c_float()
    outHasLimit = _c.c_bool()
    if not _f.CAD_GetJointInfo(robot, jointIdx, _c.byref(outType), _c.byref(outLower), _c.byref(outUpper), _c.byref(outHasLimit)):
        return None
    return (outType.value, outLower.value, outUpper.value, outHasLimit.value)


def CAD_SetJointAxis(robot: int, jointIdx: int, x: float, y: float, z: float) -> bool:
    """C: bool CAD_SetJointAxis(uint32_t robot, int jointIdx, float x, float y, float z)

    축/종류 지정 — 엔진 안에서 리깅 (URDF 로 읽은 값을 바꿔 보기).
    축은 길이 0 이면 무시하고 false. 내부에서 정규화한다.
    """
    return _f.CAD_SetJointAxis(robot, jointIdx, x, y, z)


def CAD_GetJointAxis(robot: int, jointIdx: int) -> tuple[float, float, float] | None:
    """C: bool CAD_GetJointAxis(uint32_t robot, int jointIdx, float* x, float* y, float* z)
    """
    x = _c.c_float()
    y = _c.c_float()
    z = _c.c_float()
    if not _f.CAD_GetJointAxis(robot, jointIdx, _c.byref(x), _c.byref(y), _c.byref(z)):
        return None
    return (x.value, y.value, z.value)


def CAD_SetJointType(robot: int, jointIdx: int, type: int) -> bool:
    """C: bool CAD_SetJointType(uint32_t robot, int jointIdx, int type)

    type: 0=fixed 1=revolute 2=continuous 3=prismatic.
    종류가 바뀌면 한계는 버린다 — 각도(라디안)와 길이(미터)는 단위가 달라 그대로 쓰면 위험하다.
    """
    return _f.CAD_SetJointType(robot, jointIdx, type)


def CAD_SetJointOrigin(robot: int, jointIdx: int, x: float, y: float, z: float) -> bool:
    """C: bool CAD_SetJointOrigin(uint32_t robot, int jointIdx, float x, float y, float z)

    축의 **위치**(피벗). 부모 링크 좌표 기준. 방향만으로는 어디를 중심으로 도는지 못 정한다.
    """
    return _f.CAD_SetJointOrigin(robot, jointIdx, x, y, z)


def CAD_GetJointOrigin(robot: int, jointIdx: int) -> tuple[float, float, float] | None:
    """C: bool CAD_GetJointOrigin(uint32_t robot, int jointIdx, float* x, float* y, float* z)
    """
    x = _c.c_float()
    y = _c.c_float()
    z = _c.c_float()
    if not _f.CAD_GetJointOrigin(robot, jointIdx, _c.byref(x), _c.byref(y), _c.byref(z)):
        return None
    return (x.value, y.value, z.value)


def CAD_GetLinkObject(robot: int, linkName: str | None) -> int:
    """C: uint32_t CAD_GetLinkObject(uint32_t robot, const char* linkName)

    링크 이름 → 그 링크의 씬 객체 ID (형상 없는 링크는 0). 색/재질 변경 등에 사용.
    """
    return _f.CAD_GetLinkObject(robot, _n.text(linkName))


def CAD_ClearRobots() -> None:
    """C: void CAD_ClearRobots(void)

    씬에서 로봇 전부 제거.
    """
    _f.CAD_ClearRobots()


def CAD_RigAttach(parentObj: int, childObj: int, axisX: float, axisY: float, axisZ: float, type: int, pivotX: float, pivotY: float, pivotZ: float, usePivot: bool) -> bool:
    """C: bool CAD_RigAttach(uint32_t parentObj, uint32_t childObj, float axisX, float axisY, float axisZ, int type, float pivotX, float pivotY, float pivotZ, bool usePivot)

    "큐브 9개로 로봇 만들기". 붙여도 부품은 제자리에 그대로 있는다(월드 변환을 계층으로 옮김).
    type: 0=고정 1=회전 2=연속회전 3=직선. axis 는 붙일 때의 축 방향.
    pivot(월드) = 축의 **위치**. usePivot=false 면 자식이 있는 자리를 쓴다.
    회전 중심이 부품 중심이라는 법이 없다 — 문 경첩은 모서리에 있다.
    """
    return _f.CAD_RigAttach(parentObj, childObj, axisX, axisY, axisZ, type, pivotX, pivotY, pivotZ, usePivot)


def CAD_RigDetach(obj: int) -> bool:
    """C: bool CAD_RigDetach(uint32_t obj)

    이 부품과 그 **아래 가지 전체**를 떼어낸다. 각자 보이는 자리를 유지한다.
    """
    return _f.CAD_RigDetach(obj)


def CAD_GetObjectRobot(obj: int) -> int:
    """C: uint32_t CAD_GetObjectRobot(uint32_t obj)

    이 객체가 속한 로봇 핸들 (0 = 안 붙어 있음).
    """
    return _f.CAD_GetObjectRobot(obj)
