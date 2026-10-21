# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Navigation 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_NavBuildMap', 'CAD_NavShowGrid', 'CAD_NavAddAgent', 'CAD_NavAddSelected', 'CAD_NavRemoveAgent', 'CAD_NavClearAgents', 'CAD_NavSetAgentParams', 'CAD_NavSetGoal', 'CAD_NavStart', 'CAD_NavStop', 'CAD_NavReset', 'CAD_NavGetStateJson', 'CAD_NavGetPath']

_f = _n.native

_n.bind("CAD_NavBuildMap", _c.c_bool, [_c.c_char_p])
_n.bind("CAD_NavShowGrid", None, [_c.c_bool])
_n.bind("CAD_NavAddAgent", _c.c_uint32, [_c.c_uint32, _c.c_bool])
_n.bind("CAD_NavAddSelected", _c.c_uint32, [])
_n.bind("CAD_NavRemoveAgent", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_NavClearAgents", None, [])
_n.bind("CAD_NavSetAgentParams", _c.c_bool, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_NavSetGoal", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_NavStart", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_NavStop", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_NavReset", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_NavGetStateJson", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_NavGetPath", _c.c_uint32, [_c.c_uint32, _c.POINTER(_c.c_float), _c.c_uint32])


def CAD_NavBuildMap(paramsJson: str | None) -> bool:
    """C: bool CAD_NavBuildMap(const char* paramsJson)

    agentId = 대상의 대표 객체 id(차체·바퀴처럼 조각 모델은 가장 큰 조각). 단위 = 장면 단위(m 장면이면 m, mm 도면이면 mm).
    지도 — paramsJson: {"cellSize","agentRadius","minZ","maxZ","margin","maxCells"} 중 준 키만 자동값 위에 덮음. NULL/"" = 자동.
    """
    return _f.CAD_NavBuildMap(_n.text(paramsJson))


def CAD_NavShowGrid(on: bool) -> None:
    """C: void CAD_NavShowGrid(bool on)

    agentId = 대상의 대표 객체 id(차체·바퀴처럼 조각 모델은 가장 큰 조각). 단위 = 장면 단위(m 장면이면 m, mm 도면이면 mm).
    지도 — paramsJson: {"cellSize","agentRadius","minZ","maxZ","margin","maxCells"} 중 준 키만 자동값 위에 덮음. NULL/"" = 자동.
    """
    _f.CAD_NavShowGrid(on)


def CAD_NavAddAgent(objectId: int, isVehicle: bool) -> int:
    """C: uint32_t CAD_NavAddAgent(uint32_t objectId, bool isVehicle)

    대상 — 장면 객체를 주행 대상으로. 반환 agentId(0 실패). 자동 수집(뼈·바퀴 클립)된 대상도 Remove/Clear 하면 다시 안 들어온다.
    """
    return _f.CAD_NavAddAgent(objectId, isVehicle)


def CAD_NavAddSelected() -> int:
    """C: uint32_t CAD_NavAddSelected(void)

    대상 — 장면 객체를 주행 대상으로. 반환 agentId(0 실패). 자동 수집(뼈·바퀴 클립)된 대상도 Remove/Clear 하면 다시 안 들어온다.
    반환 = 추가된 수
    """
    return _f.CAD_NavAddSelected()


def CAD_NavRemoveAgent(agentId: int) -> bool:
    """C: bool CAD_NavRemoveAgent(uint32_t agentId)

    대상 — 장면 객체를 주행 대상으로. 반환 agentId(0 실패). 자동 수집(뼈·바퀴 클립)된 대상도 Remove/Clear 하면 다시 안 들어온다.
    """
    return _f.CAD_NavRemoveAgent(agentId)


def CAD_NavClearAgents() -> None:
    """C: void CAD_NavClearAgents(void)

    대상 — 장면 객체를 주행 대상으로. 반환 agentId(0 실패). 자동 수집(뼈·바퀴 클립)된 대상도 Remove/Clear 하면 다시 안 들어온다.
    """
    _f.CAD_NavClearAgents()


def CAD_NavSetAgentParams(agentId: int, json: str | None) -> bool:
    """C: bool CAD_NavSetAgentParams(uint32_t agentId, const char* json)

    {"speed","scanRange","radius"(0=자동),"showRays","checked","isVehicle"} 중 준 키만.
    """
    return _f.CAD_NavSetAgentParams(agentId, _n.text(json))


def CAD_NavSetGoal(agentId: int, x: float, y: float, z: float) -> bool:
    """C: bool CAD_NavSetGoal(uint32_t agentId, float x, float y, float z)

    목적지 — 경로 계획까지(출발은 Start). 길이 없으면 false + CAD_GetLastError.
    """
    return _f.CAD_NavSetGoal(agentId, x, y, z)


def CAD_NavStart(agentId: int) -> bool:
    """C: bool CAD_NavStart(uint32_t agentId)

    목적지 — 경로 계획까지(출발은 Start). 길이 없으면 false + CAD_GetLastError.
    """
    return _f.CAD_NavStart(agentId)


def CAD_NavStop(agentId: int) -> bool:
    """C: bool CAD_NavStop(uint32_t agentId)

    목적지 — 경로 계획까지(출발은 Start). 길이 없으면 false + CAD_GetLastError.
    """
    return _f.CAD_NavStop(agentId)


def CAD_NavReset(agentId: int) -> bool:
    """C: bool CAD_NavReset(uint32_t agentId)

    목적지 — 경로 계획까지(출발은 Start). 길이 없으면 false + CAD_GetLastError.
    정지·경로 삭제·출발 자리로
    """
    return _f.CAD_NavReset(agentId)


def CAD_NavGetStateJson() -> str | None:
    """C: int CAD_NavGetStateJson(char* out, int cap)

    {"grid":{"ready","showing","w","h","cellSize","origin","blockedCells","totalCells"},"activeAgent",
    "agents":[{"agentId","name","isVehicle","checked","active","hasGoal","goal","driving","pathPoints","pathIndex","pathLength",
    "position"(몸통 중심),"yaw"(도, 0=+Y 시계 — CAD_ApplyExternalPose 와 같음),"arrived","speed","scanRange","radius","showRays"}]}
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_NavGetStateJson(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_NavGetPath(agentId: int, outXY: Any, cap: int) -> int:
    """C: uint32_t CAD_NavGetPath(uint32_t agentId, float* outXY, uint32_t cap)

    경로 점 [x,y] × n — 반환 = 점 수(outXY NULL/cap 0 이면 개수만, 2회 호출). cap = 점 개수 단위(배열은 float cap×2 칸).
    """
    return _f.CAD_NavGetPath(agentId, outXY, cap)
