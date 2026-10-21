# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Link 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_LinkStart', 'CAD_LinkStop', 'CAD_LinkPort', 'CAD_LinkSend', 'CAD_ApplyExternalPose', 'CAD_CreateVolumeMesh', 'CAD_CreateLabelMeshes', 'CAD_CreateLine', 'CAD_CreateCircle']

_f = _n.native

_n.bind("CAD_LinkStart", _c.c_bool, [_c.c_int, _c.c_bool])
_n.bind("CAD_LinkStop", None, [])
_n.bind("CAD_LinkPort", _c.c_int, [])
_n.bind("CAD_LinkSend", _c.c_bool, [_c.c_char_p])
_n.bind("CAD_ApplyExternalPose", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float, _c.c_bool, _c.POINTER(_c.c_bool)])
_n.bind("CAD_CreateVolumeMesh", _c.c_uint32, [_c.c_char_p, _c.c_float, _c.c_int])
_n.bind("CAD_CreateLabelMeshes", _c.c_uint32, [_c.c_char_p, _c.c_int])
_n.bind("CAD_CreateLine", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateCircle", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])


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
    """
    return _f.CAD_LinkStart(port, clamp)


def CAD_LinkStop() -> None:
    """C: void CAD_LinkStop(void)

    CAD_API bool     CAD_LinkStart(int port, bool clamp);       /* port 0 = 빈 포트를 고름(CAD_LinkPort 로 확인). 실패 false + CAD_GetLastError
    """
    _f.CAD_LinkStop()


def CAD_LinkPort() -> int:
    """C: int CAD_LinkPort(void)
    """
    return _f.CAD_LinkPort()


def CAD_LinkSend(jsonLine: str | None) -> bool:
    """C: bool CAD_LinkSend(const char* jsonLine)

    CAD_API int      CAD_LinkPort(void);                         /* 0 = 닫힘
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


def CAD_CreateLine(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> int:
    """C: uint32_t CAD_CreateLine(float x1, float y1, float z1, float x2, float y2, float z2)
    """
    return _f.CAD_CreateLine(x1, y1, z1, x2, y2, z2)


def CAD_CreateCircle(cx: float, cy: float, cz: float, radius: float, normalX: float, normalY: float, normalZ: float) -> int:
    """C: uint32_t CAD_CreateCircle(float cx, float cy, float cz, float radius, float normalX, float normalY, float normalZ)
    """
    return _f.CAD_CreateCircle(cx, cy, cz, radius, normalX, normalY, normalZ)
