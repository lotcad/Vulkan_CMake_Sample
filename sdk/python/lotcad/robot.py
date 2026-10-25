# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Robot 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_JOINT_FIXED', 'CAD_JOINT_REVOLUTE', 'CAD_JOINT_CONTINUOUS', 'CAD_JOINT_PRISMATIC', 'CAD_LoadUrdf', 'CAD_GetRobotCount', 'CAD_GetJointCount', 'CAD_FindJoint', 'CAD_GetJointName', 'CAD_SetJointValue', 'CAD_GetJointValue', 'CAD_SetJointValues', 'CAD_SetJointValuesByName', 'CAD_GetJointInfo', 'CAD_SetJointAxis', 'CAD_SetJointType', 'CAD_SetJointOrigin', 'CAD_GetLinkObject', 'CAD_ClearRobots', 'CAD_RigAttach', 'CAD_RigDetach', 'CAD_GetObjectRobot']

_f = _n.native

CAD_JOINT_FIXED = 0
CAD_JOINT_REVOLUTE = 1
CAD_JOINT_CONTINUOUS = 2
CAD_JOINT_PRISMATIC = 3

_n.bind("CAD_LoadUrdf", _c.c_int32, [_c.c_char_p, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_GetRobotCount", _c.c_int32, [])
_n.bind("CAD_GetJointCount", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_FindJoint", _c.c_int32, [_c.c_uint32, _c.c_char_p, _c.POINTER(_c.c_int32)])
_n.bind("CAD_GetJointName", _c.c_int32, [_c.c_uint32, _c.c_int32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_SetJointValue", _c.c_int32, [_c.c_uint32, _c.c_int32, _c.c_double, _c.POINTER(_c.c_double)])
_n.bind("CAD_GetJointValue", _c.c_int32, [_c.c_uint32, _c.c_int32, _c.POINTER(_c.c_double)])
_n.bind("CAD_SetJointValues", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_int32), _c.POINTER(_c.c_double), _c.c_uint32])
_n.bind("CAD_SetJointValuesByName", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char_p), _c.POINTER(_c.c_double), _c.c_uint32])
_n.bind("CAD_GetJointInfo", _c.c_int32, [_c.c_uint32, _c.c_int32, _c.POINTER(CAD_JointInfo)])
_n.bind("CAD_SetJointAxis", _c.c_int32, [_c.c_uint32, _c.c_int32, CAD_GeVec3])
_n.bind("CAD_SetJointType", _c.c_int32, [_c.c_uint32, _c.c_int32, _c.c_int32])
_n.bind("CAD_SetJointOrigin", _c.c_int32, [_c.c_uint32, _c.c_int32, CAD_GeVec3])
_n.bind("CAD_GetLinkObject", _c.c_int32, [_c.c_uint32, _c.c_char_p, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_ClearRobots", _c.c_int32, [])
_n.bind("CAD_RigAttach", _c.c_int32, [_c.c_uint32, _c.c_uint32, CAD_GeVec3, _c.c_int32, _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_RigDetach", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_GetObjectRobot", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_uint32)])


def CAD_LoadUrdf(path: str | None) -> tuple[int, int]:
    """C: CAD_Status CAD_LoadUrdf(const char* path, uint32_t* outRobot)

    파일 없음 = CAD_E_NOT_FOUND, 못 읽음 = CAD_E_FAILED + 이유
    """
    outRobot = _c.c_uint32()
    _r = _f.CAD_LoadUrdf(_n.text(path), _c.byref(outRobot))
    return (_r, outRobot.value)


def CAD_GetRobotCount() -> int:
    """C: int32_t CAD_GetRobotCount(void)

    파일 없음 = CAD_E_NOT_FOUND, 못 읽음 = CAD_E_FAILED + 이유
    """
    return _f.CAD_GetRobotCount()


def CAD_GetJointCount(robot: int) -> int:
    """C: int32_t CAD_GetJointCount(uint32_t robot)

    파일 없음 = CAD_E_NOT_FOUND, 못 읽음 = CAD_E_FAILED + 이유
    """
    return _f.CAD_GetJointCount(robot)


def CAD_FindJoint(robot: int, jointName: str | None) -> tuple[int, int]:
    """C: CAD_Status CAD_FindJoint(uint32_t robot, const char* jointName, int32_t* outJoint)

    조인트 이름 → 번호(ROS 는 이름으로 온다). 없음 = CAD_E_NOT_FOUND(*outJoint = -1)
    """
    outJoint = _c.c_int32()
    _r = _f.CAD_FindJoint(robot, _n.text(jointName), _c.byref(outJoint))
    return (_r, outJoint.value)


def CAD_GetJointName(robot: int, joint: int) -> str | None:
    """C: int32_t CAD_GetJointName(uint32_t robot, int32_t joint, char* buf, uint32_t capacity)

    조인트 이름 → 번호(ROS 는 이름으로 온다). 없음 = CAD_E_NOT_FOUND(*outJoint = -1)
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetJointName(robot, joint, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_SetJointValue(robot: int, joint: int, value: float) -> tuple[int, float]:
    """C: CAD_Status CAD_SetJointValue(uint32_t robot, int32_t joint, double value, double* outApplied)

    값 대입/조회 — outApplied = 한계로 잘린 **실제 적용값**(NULL 가능)
    """
    outApplied = _c.c_double()
    _r = _f.CAD_SetJointValue(robot, joint, value, _c.byref(outApplied))
    return (_r, outApplied.value)


def CAD_GetJointValue(robot: int, joint: int) -> tuple[int, float]:
    """C: CAD_Status CAD_GetJointValue(uint32_t robot, int32_t joint, double* outValue)

    값 대입/조회 — outApplied = 한계로 잘린 **실제 적용값**(NULL 가능)
    """
    outValue = _c.c_double()
    _r = _f.CAD_GetJointValue(robot, joint, _c.byref(outValue))
    return (_r, outValue.value)


def CAD_SetJointValues(robot: int, joints: Sequence | None, values: Sequence | None, count: int) -> int:
    """C: int32_t CAD_SetJointValues(uint32_t robot, const int32_t* joints, const double* values, uint32_t count)

    ROS 의 sensor_msgs/JointState 는 관절 전부를 한 메시지에 담아 초당 수십 번 보낸다.
    하나씩 넣으면 관절 수만큼 계층 트리를 다시 푸느라 헛일을 한다 — 여기선 **마지막에 한 번만** 푼다.
    반환: 실제로 적용된 개수(범위 밖·고정 조인트는 건너뜀).
    """
    _a_joints = _n.array(_c.c_int32, joints)
    _a_values = _n.array(_c.c_double, values)
    return _f.CAD_SetJointValues(robot, _a_joints, _a_values, count)


def CAD_SetJointValuesByName(robot: int, names: Sequence[str] | None, values: Sequence | None, count: int) -> int:
    """C: int32_t CAD_SetJointValuesByName(uint32_t robot, const char* const* names, const double* values, uint32_t count)

    이름으로 받는 판 — JointState 콜백에 그대로 꽂힌다(position 은 double 이라 복사 없이).
    CAD_SetJointValuesByName(r, names, msg.position.data(), count);
    """
    _a_names = _n.text_array(names)
    _a_values = _n.array(_c.c_double, values)
    return _f.CAD_SetJointValuesByName(robot, _a_names, _a_values, count)


def CAD_GetJointInfo(robot: int, joint: int) -> tuple[int, CAD_JointInfo]:
    """C: CAD_Status CAD_GetJointInfo(uint32_t robot, int32_t joint, CAD_JointInfo* out)
    """
    out = CAD_JointInfo()
    out.size = _c.sizeof(CAD_JointInfo)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_GetJointInfo(robot, joint, _c.byref(out))
    return (_r, out)


def CAD_SetJointAxis(robot: int, joint: int, axis: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_SetJointAxis(uint32_t robot, int32_t joint, CAD_GeVec3 axis)

    축 방향(월드) — 엔진 안에서 리깅(URDF 로 읽은 값을 바꿔 보기). 길이 0 = CAD_E_DEGENERATE. 내부에서 정규화
    """
    return _f.CAD_SetJointAxis(robot, joint, axis)


def CAD_SetJointType(robot: int, joint: int, type: int) -> int:
    """C: CAD_Status CAD_SetJointType(uint32_t robot, int32_t joint, int32_t type)

    종류 — CAD_JOINT_*. 종류가 바뀌면 한계는 버린다(각도와 길이는 단위가 달라 그대로 쓰면 위험)
    """
    return _f.CAD_SetJointType(robot, joint, type)


def CAD_SetJointOrigin(robot: int, joint: int, position: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_SetJointOrigin(uint32_t robot, int32_t joint, CAD_GeVec3 position)

    축의 **자리**(피벗, 월드 — 관절 값 0 기준). 방향만으로는 어디를 중심으로 도는지 못 정한다. 부품은 제자리
    """
    return _f.CAD_SetJointOrigin(robot, joint, position)


def CAD_GetLinkObject(robot: int, linkName: str | None) -> tuple[int, int]:
    """C: CAD_Status CAD_GetLinkObject(uint32_t robot, const char* linkName, uint32_t* outId)

    링크 이름 → 그 링크의 씬 객체 id(형상 없는 링크는 0). 없는 이름 = CAD_E_NOT_FOUND
    """
    outId = _c.c_uint32()
    _r = _f.CAD_GetLinkObject(robot, _n.text(linkName), _c.byref(outId))
    return (_r, outId.value)


def CAD_ClearRobots() -> int:
    """C: CAD_Status CAD_ClearRobots(void)

    씬에서 로봇 전부 제거

    묶음 주석: 링크 이름 → 그 링크의 씬 객체 id(형상 없는 링크는 0). 없는 이름 = CAD_E_NOT_FOUND
    """
    return _f.CAD_ClearRobots()


def CAD_RigAttach(parentObj: int, childObj: int, axis: CAD_GeVec3, type: int, pivot: Sequence | None) -> int:
    """C: CAD_Status CAD_RigAttach(uint32_t parentObj, uint32_t childObj, CAD_GeVec3 axis, int32_t type, const CAD_GeVec3* pivot)

    "큐브 9개로 로봇 만들기". 붙여도 부품은 제자리에 그대로 있는다(월드 변환을 계층으로 옮김).
    type = CAD_JOINT_*, axis = 붙일 때의 축 방향(월드, 고정이 아니면 길이 0 = CAD_E_DEGENERATE).
    pivot(월드) = 축의 **자리**, NULL 이면 자식이 있는 자리 — 회전 중심이 부품 중심이라는 법이 없다(문 경첩은 모서리에 있다).
    이미 다른 로봇에 붙어 있음·고리가 생김 = CAD_E_FAILED + 이유
    """
    _a_pivot = _n.array(CAD_GeVec3, pivot)
    return _f.CAD_RigAttach(parentObj, childObj, axis, type, _a_pivot)


def CAD_RigDetach(obj: int) -> int:
    """C: CAD_Status CAD_RigDetach(uint32_t obj)

    이 부품과 그 **아래 가지 전체**를 떼어낸다(각자 보이는 자리 유지). 안 붙어 있음 = CAD_E_NOT_FOUND
    """
    return _f.CAD_RigDetach(obj)


def CAD_GetObjectRobot(obj: int) -> tuple[int, int]:
    """C: CAD_Status CAD_GetObjectRobot(uint32_t obj, uint32_t* outRobot)

    이 객체가 속한 로봇 핸들(안 붙어 있으면 0, CAD_OK)
    """
    outRobot = _c.c_uint32()
    _r = _f.CAD_GetObjectRobot(obj, _c.byref(outRobot))
    return (_r, outRobot.value)
