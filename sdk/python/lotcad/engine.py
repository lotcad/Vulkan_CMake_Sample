# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Engine 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_GetVersion', 'CAD_SetUserDataPath', 'CAD_GetUserDataPath', 'CAD_CreateEngine', 'CAD_DestroyEngine', 'CAD_Tick', 'CAD_ShouldClose', 'CAD_SetIgnoreCloseRequest', 'CAD_SetRuntimeAssetPath', 'CAD_AttachView', 'CAD_ResizeView', 'CAD_DetachView', 'CAD_OnMouseDown', 'CAD_OnMouseUp', 'CAD_OnMouseMove', 'CAD_OnMouseWheel', 'CAD_OnKeyDown', 'CAD_OnKeyUp']

_f = _n.native

_n.bind("CAD_GetVersion", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_SetUserDataPath", _c.c_bool, [_c.c_char_p])
_n.bind("CAD_GetUserDataPath", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_CreateEngine", _c.c_bool, [])
_n.bind("CAD_DestroyEngine", None, [])
_n.bind("CAD_Tick", _c.c_bool, [])
_n.bind("CAD_ShouldClose", _c.c_bool, [])
_n.bind("CAD_SetIgnoreCloseRequest", None, [_c.c_bool])
_n.bind("CAD_SetRuntimeAssetPath", _c.c_bool, [_c.c_char_p])
_n.bind("CAD_AttachView", None, [_c.c_void_p, _c.c_int, _c.c_int])
_n.bind("CAD_ResizeView", None, [_c.c_int, _c.c_int])
_n.bind("CAD_DetachView", None, [])
_n.bind("CAD_OnMouseDown", None, [_c.c_int, _c.c_double, _c.c_double, _c.c_int])
_n.bind("CAD_OnMouseUp", None, [_c.c_int, _c.c_double, _c.c_double, _c.c_int])
_n.bind("CAD_OnMouseMove", None, [_c.c_double, _c.c_double])
_n.bind("CAD_OnMouseWheel", None, [_c.c_double, _c.c_double, _c.c_double, _c.c_double])
_n.bind("CAD_OnKeyDown", None, [_c.c_int, _c.c_int])
_n.bind("CAD_OnKeyUp", None, [_c.c_int, _c.c_int])


def CAD_GetVersion() -> str | None:
    """C: int CAD_GetVersion(char* buf, int bufLen)

    엔진 버전 "0.1.0-beta"(lot_version.h). 엔진을 만들기 전에도 된다. 반환 = 필요한 길이(널 제외), buf 가 짧으면 잘라 담는다.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetVersion(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_SetUserDataPath(pathUtf8: str | None) -> bool:
    """C: bool CAD_SetUserDataPath(const char* pathUtf8)

    사용자 설정 폴더(창 위치·패널 배치·언어·그래픽·외부 연결 .ini, 사용자 파티클 프리셋, 사용자 plugins/) — CAD_CreateEngine **전에**.
    NULL = OS 기본 폴더(Windows %APPDATA%\\LotCAD · macOS ~/Library/Application Support/LotCAD · 리눅스 ~/.config/lotcad,
           환경 변수 LOTCAD_USER_DIR 가 있으면 그것 — 처음 한 번 실행 폴더의 .ini 를 옮겨 담는다),
    "" = 실행 폴더(기본값 — 부르지 않으면 이것), 그 밖 = 그 폴더(없으면 만든다). 설치 폴더가 읽기 전용인 호스트는 NULL 을 넘길 것.
    에셋(models·textures·fonts·effects·languages)은 그대로 CAD_SetRuntimeAssetPath / 실행 폴더에서 읽는다.
    """
    return _f.CAD_SetUserDataPath(_n.text(pathUtf8))


def CAD_GetUserDataPath() -> str | None:
    """C: int CAD_GetUserDataPath(char* buf, int bufLen)
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetUserDataPath(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_CreateEngine() -> bool:
    """C: bool CAD_CreateEngine(void)

    CAD_API int  CAD_GetUserDataPath(char* buf, int bufLen);   /* 빈 글 = 실행 폴더
    """
    return _f.CAD_CreateEngine()


def CAD_DestroyEngine() -> None:
    """C: void CAD_DestroyEngine(void)
    """
    _f.CAD_DestroyEngine()


def CAD_Tick() -> bool:
    """C: bool CAD_Tick(void)
    """
    return _f.CAD_Tick()


def CAD_ShouldClose() -> bool:
    """C: bool CAD_ShouldClose(void)
    """
    return _f.CAD_ShouldClose()


def CAD_SetIgnoreCloseRequest(ignore: bool) -> None:
    """C: void CAD_SetIgnoreCloseRequest(bool ignore)
    """
    _f.CAD_SetIgnoreCloseRequest(ignore)


def CAD_SetRuntimeAssetPath(path: str | None) -> bool:
    """C: bool CAD_SetRuntimeAssetPath(const char* path)
    """
    return _f.CAD_SetRuntimeAssetPath(_n.text(path))


def CAD_AttachView(nativeHandle: int | None, width: int, height: int) -> None:
    """C: void CAD_AttachView(void* nativeHandle, int width, int height)
    """
    _f.CAD_AttachView(nativeHandle, width, height)


def CAD_ResizeView(width: int, height: int) -> None:
    """C: void CAD_ResizeView(int width, int height)
    """
    _f.CAD_ResizeView(width, height)


def CAD_DetachView() -> None:
    """C: void CAD_DetachView(void)
    """
    _f.CAD_DetachView()


def CAD_OnMouseDown(button: int, x: float, y: float, modifiers: int) -> None:
    """C: void CAD_OnMouseDown(int button, double x, double y, int modifiers)
    """
    _f.CAD_OnMouseDown(button, x, y, modifiers)


def CAD_OnMouseUp(button: int, x: float, y: float, modifiers: int) -> None:
    """C: void CAD_OnMouseUp(int button, double x, double y, int modifiers)
    """
    _f.CAD_OnMouseUp(button, x, y, modifiers)


def CAD_OnMouseMove(x: float, y: float) -> None:
    """C: void CAD_OnMouseMove(double x, double y)
    """
    _f.CAD_OnMouseMove(x, y)


def CAD_OnMouseWheel(x: float, y: float, deltaX: float, deltaY: float) -> None:
    """C: void CAD_OnMouseWheel(double x, double y, double deltaX, double deltaY)
    """
    _f.CAD_OnMouseWheel(x, y, deltaX, deltaY)


def CAD_OnKeyDown(key: int, modifiers: int) -> None:
    """C: void CAD_OnKeyDown(int key, int modifiers)
    """
    _f.CAD_OnKeyDown(key, modifiers)


def CAD_OnKeyUp(key: int, modifiers: int) -> None:
    """C: void CAD_OnKeyUp(int key, int modifiers)
    """
    _f.CAD_OnKeyUp(key, modifiers)
