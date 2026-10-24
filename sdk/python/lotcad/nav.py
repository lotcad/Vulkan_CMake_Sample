# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Nav 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_LinkStart', 'CAD_LinkStop', 'CAD_LinkPort', 'CAD_LinkSend', 'CAD_ApplyExternalPose', 'CAD_NavBuildMap', 'CAD_NavShowGrid', 'CAD_NavAddAgent', 'CAD_NavAddSelected', 'CAD_NavRemoveAgent', 'CAD_NavClearAgents', 'CAD_NavSetAgentParams', 'CAD_NavSetGoal', 'CAD_NavStart', 'CAD_NavStop', 'CAD_NavReset', 'CAD_NavGetStateJson', 'CAD_NavGetPath']

_f = _n.native

_n.bind("CAD_LinkStart", _c.c_bool, [_c.c_int, _c.c_bool])
_n.bind("CAD_LinkStop", None, [])
_n.bind("CAD_LinkPort", _c.c_int, [])
_n.bind("CAD_LinkSend", _c.c_bool, [_c.c_char_p])
_n.bind("CAD_ApplyExternalPose", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.c_bool, _c.POINTER(_c.c_bool)])
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


def CAD_LinkStart(port: int, clamp: bool) -> bool:
    """C: bool CAD_LinkStart(int port, bool clamp)

    외부 연결(link) — 태그 추적 스크립트·로봇·머리 추적 같은 바깥 프로세스가 붙는 TCP 문
    127.0.0.1:port 에서 듣고, 줄 하나 = JSON 객체 하나("\\n" 구분). 처리는 엔진 메인 스레드(다음 tick)에서.
      {"type":"pose","id":"기둥A"|12,"x":..,"y":..,"yaw":90,"mode":"clamp"|"twin"}
          id 는 객체 이름 또는 번호. (x,y) = 객체의 **월드 경계 중심**(원점 아님), 단위 = 도면 단위(mm). z 는 그대로.
          yaw 는 도, 0 = +Y, 시계 방향 양수(내비 규약). 생략하면 향 유지.
          mode 생략 시 CAD_LinkStart 의 clamp. clamp = 벽(다른 메시)에 막히면 벽 앞에 선다(도면이 진실),
          twin = 그대로 비춘다(현실이 진실). 직전 위치와의 속도가 몸 크기의 0.3배/초를 넘으면 걷기 애니가 켜지고,
          0.5초 동안 소식이 없으면 꺼진다.
      {"type":"ping"}  →  엔진이 {"type":"pong"} 을 되돌린다.
    명령행 `link [on|off|port N|clamp|twin]` 과 같은 것. 파이썬 예: tools/tag_tracker.py(AprilTag), tools/fake_pose.py.
    로컬 전용 — 원격·토큰은 없다.
    port 0 = 빈 포트를 고름(CAD_LinkPort 로 확인). 실패 false + CAD_GetLastError
    """
    return _f.CAD_LinkStart(port, clamp)


def CAD_LinkStop() -> None:
    """C: void CAD_LinkStop(void)

    외부 연결(link) — 태그 추적 스크립트·로봇·머리 추적 같은 바깥 프로세스가 붙는 TCP 문
    127.0.0.1:port 에서 듣고, 줄 하나 = JSON 객체 하나("\\n" 구분). 처리는 엔진 메인 스레드(다음 tick)에서.
      {"type":"pose","id":"기둥A"|12,"x":..,"y":..,"yaw":90,"mode":"clamp"|"twin"}
          id 는 객체 이름 또는 번호. (x,y) = 객체의 **월드 경계 중심**(원점 아님), 단위 = 도면 단위(mm). z 는 그대로.
          yaw 는 도, 0 = +Y, 시계 방향 양수(내비 규약). 생략하면 향 유지.
          mode 생략 시 CAD_LinkStart 의 clamp. clamp = 벽(다른 메시)에 막히면 벽 앞에 선다(도면이 진실),
          twin = 그대로 비춘다(현실이 진실). 직전 위치와의 속도가 몸 크기의 0.3배/초를 넘으면 걷기 애니가 켜지고,
          0.5초 동안 소식이 없으면 꺼진다.
      {"type":"ping"}  →  엔진이 {"type":"pong"} 을 되돌린다.
    명령행 `link [on|off|port N|clamp|twin]` 과 같은 것. 파이썬 예: tools/tag_tracker.py(AprilTag), tools/fake_pose.py.
    로컬 전용 — 원격·토큰은 없다.
    """
    _f.CAD_LinkStop()


def CAD_LinkPort() -> int:
    """C: int CAD_LinkPort(void)

    0 = 닫힘

    묶음 주석: 외부 연결(link) — 태그 추적 스크립트·로봇·머리 추적 같은 바깥 프로세스가 붙는 TCP 문
    127.0.0.1:port 에서 듣고, 줄 하나 = JSON 객체 하나("\\n" 구분). 처리는 엔진 메인 스레드(다음 tick)에서.
      {"type":"pose","id":"기둥A"|12,"x":..,"y":..,"yaw":90,"mode":"clamp"|"twin"}
          id 는 객체 이름 또는 번호. (x,y) = 객체의 **월드 경계 중심**(원점 아님), 단위 = 도면 단위(mm). z 는 그대로.
          yaw 는 도, 0 = +Y, 시계 방향 양수(내비 규약). 생략하면 향 유지.
          mode 생략 시 CAD_LinkStart 의 clamp. clamp = 벽(다른 메시)에 막히면 벽 앞에 선다(도면이 진실),
          twin = 그대로 비춘다(현실이 진실). 직전 위치와의 속도가 몸 크기의 0.3배/초를 넘으면 걷기 애니가 켜지고,
          0.5초 동안 소식이 없으면 꺼진다.
      {"type":"ping"}  →  엔진이 {"type":"pong"} 을 되돌린다.
    명령행 `link [on|off|port N|clamp|twin]` 과 같은 것. 파이썬 예: tools/tag_tracker.py(AprilTag), tools/fake_pose.py.
    로컬 전용 — 원격·토큰은 없다.
    """
    return _f.CAD_LinkPort()


def CAD_LinkSend(jsonLine: str | None) -> bool:
    """C: bool CAD_LinkSend(const char* jsonLine)

    붙은 클라이언트 전부에 한 줄(끝에 "\\n" 붙임). 접속 없으면 false

    묶음 주석: 외부 연결(link) — 태그 추적 스크립트·로봇·머리 추적 같은 바깥 프로세스가 붙는 TCP 문
    127.0.0.1:port 에서 듣고, 줄 하나 = JSON 객체 하나("\\n" 구분). 처리는 엔진 메인 스레드(다음 tick)에서.
      {"type":"pose","id":"기둥A"|12,"x":..,"y":..,"yaw":90,"mode":"clamp"|"twin"}
          id 는 객체 이름 또는 번호. (x,y) = 객체의 **월드 경계 중심**(원점 아님), 단위 = 도면 단위(mm). z 는 그대로.
          yaw 는 도, 0 = +Y, 시계 방향 양수(내비 규약). 생략하면 향 유지.
          mode 생략 시 CAD_LinkStart 의 clamp. clamp = 벽(다른 메시)에 막히면 벽 앞에 선다(도면이 진실),
          twin = 그대로 비춘다(현실이 진실). 직전 위치와의 속도가 몸 크기의 0.3배/초를 넘으면 걷기 애니가 켜지고,
          0.5초 동안 소식이 없으면 꺼진다.
      {"type":"ping"}  →  엔진이 {"type":"pong"} 을 되돌린다.
    명령행 `link [on|off|port N|clamp|twin]` 과 같은 것. 파이썬 예: tools/tag_tracker.py(AprilTag), tools/fake_pose.py.
    로컬 전용 — 원격·토큰은 없다.
    """
    return _f.CAD_LinkSend(_n.text(jsonLine))


def CAD_ApplyExternalPose(id: int, x: float, y: float, yawDeg: float, clamp: bool) -> bool | None:
    """C: bool CAD_ApplyExternalPose(uint32_t id, float x, float y, float yawDeg, bool clamp, bool* outBlocked)

    소켓 없이 호스트가 직접 위치를 넣는다(iOS ARKit·자체 추적기). pose 메시지와 같은 규약. yawDeg 에 NaN 을 주면 향 유지.
    반환 = 적용됨. outBlocked 는 clamp 로 벽에 막혔는가(NULL 가능).
    """
    outBlocked = _c.c_bool()
    if not _f.CAD_ApplyExternalPose(id, x, y, yawDeg, clamp, _c.byref(outBlocked)):
        return None
    return outBlocked.value


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

    반환 = 추가된 수

    묶음 주석: 대상 — 장면 객체를 주행 대상으로. 반환 agentId(0 실패). 자동 수집(뼈·바퀴 클립)된 대상도 Remove/Clear 하면 다시 안 들어온다.
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

    정지·경로 삭제·출발 자리로

    묶음 주석: 목적지 — 경로 계획까지(출발은 Start). 길이 없으면 false + CAD_GetLastError.
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
