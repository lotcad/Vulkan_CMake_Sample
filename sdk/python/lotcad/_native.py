# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""엔진 라이브러리 불러오기와 감싸기 함수가 쓰는 공용 도우미."""
from __future__ import annotations

import ctypes as _c
import itertools
import os
import sys
import threading

__all__ = ["native", "SDK_DIR", "LIBRARY_PATH", "buffer"]

if sys.platform.startswith("win"):
    _LIBRARY = "LotCADCore.dll"
elif sys.platform == "darwin":
    _LIBRARY = "libLotCADCore.dylib"
else:
    _LIBRARY = "libLotCADCore.so"

# sdk/python/lotcad/_native.py → sdk/  (라이브러리·models·fonts·textures 가 있는 곳)
SDK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

_dll_dirs = []   # os.add_dll_directory 핸들 — 닫히면 효력이 없어져 붙잡아 둔다


def _load():
    """찾는 순서: 환경 변수 LOTCAD_LIBRARY(파일 경로) → SDK 폴더 → 시스템 검색 경로(PATH 등)."""
    tried = []
    candidates = [os.environ.get("LOTCAD_LIBRARY"), os.path.join(SDK_DIR, _LIBRARY), _LIBRARY]
    for path in [c for c in candidates if c]:
        if os.path.isabs(path) and not os.path.exists(path):
            tried.append(f"{path}: 없음")
            continue
        try:
            if os.path.isabs(path) and hasattr(os, "add_dll_directory"):
                _dll_dirs.append(os.add_dll_directory(os.path.dirname(path)))   # 같은 폴더의 의존 DLL 도 찾게
            return _c.CDLL(path), path
        except OSError as e:
            tried.append(f"{path}: {e}")
    raise OSError("LotCAD 엔진 라이브러리를 찾지 못했습니다 — LOTCAD_LIBRARY 환경 변수에 파일 경로를 지정하세요.\n  "
                  + "\n  ".join(tried))


_lib, LIBRARY_PATH = _load()


class _Native:
    """원시 ctypes 함수 — 헤더와 **똑같은 인자**(포인터·버퍼를 직접 다룬다). lotcad.native.CAD_xxx"""


native = _Native()


def bind(name, restype, argtypes):
    try:
        f = getattr(_lib, name)
    except AttributeError:
        def missing(*_args, **_kwargs):
            raise NotImplementedError(f"{name}: 이 OS 의 엔진 라이브러리에 없는 함수입니다 ({LIBRARY_PATH})")
        missing.__name__ = name
        setattr(native, name, missing)
        return
    f.restype = restype
    f.argtypes = argtypes
    setattr(native, name, f)


def text(value):
    """str → UTF-8 바이트(엔진은 UTF-8 만 받는다). None = NULL."""
    if value is None or isinstance(value, bytes):
        return value
    if isinstance(value, str):
        return value.encode("utf-8")
    if isinstance(value, (bytearray, memoryview)):
        return bytes(value)
    raise TypeError(f"문자열이어야 합니다: {type(value).__name__}")


def text_array(values):
    if values is None:
        return None
    items = [text(v) for v in values]
    return (_c.c_char_p * len(items))(*items)


def array(ctype, values):
    """목록·튜플 → ctypes 배열. ctypes 배열·포인터는 그대로, bytes 는 unsigned char 배열로."""
    if values is None or isinstance(values, (_c.Array, _c._Pointer)):
        return values
    if ctype is _c.c_ubyte and isinstance(values, (bytes, bytearray, memoryview)):
        return (_c.c_ubyte * len(values)).from_buffer_copy(values)
    items = list(values)
    return (ctype * len(items))(*items)


def buffer(ctype, count):
    """배열을 돌려받는 함수에 넘길 빈 버퍼. 예: ids = lotcad.buffer(ctypes.c_uint32, n)"""
    return (ctype * count)()


def decode(raw):
    return raw.decode("utf-8", "replace")


def callback(cftype, fn, text_args=()):
    """파이썬 함수 → C 함수 포인터. const char* 인자는 str 로 풀어 준다. None = NULL(콜백 해제)."""
    if fn is None:
        return cftype()   # ctypes 는 None 을 함수 포인터 인자로 받지 않는다 — 빈 형식 객체가 NULL
    if isinstance(fn, cftype):
        return fn
    returns = cftype._restype_ is not None

    def adapter(*args):
        if text_args:
            args = [decode(a) if (i in text_args and a is not None) else a for i, a in enumerate(args)]
        result = fn(*args)
        return 0 if (returns and result is None) else result

    return cftype(adapter)


_alive = {}
_once = {}            # 한 번 불리는 콜백(CAD_Post) — 번호 → 함수 포인터. 불릴 때까지만
_once_done = []       # 불린 것 — 다음 맡기기 때 놓는다(불리는 중인 콜백을 그 안에서 지우지 않게 한 박자 늦게)
_once_lock = threading.Lock()   # 맡기기는 아무 스레드에서나, 불리기는 엔진 스레드에서
_once_seq = itertools.count(1)


def callback_once(cftype, fn, text_args=()):
    """한 번 불리고 끝나는 콜백 — 불릴 때까지 붙잡고, 불린 뒤엔 놓는다(CAD_Post 를 자주 불러도 쌓이지 않게)."""
    if fn is None:
        return cftype()
    with _once_lock:
        for k in _once_done:
            _once.pop(k, None)
        _once_done.clear()
        key = next(_once_seq)

    def run(*args):
        try:
            return fn(*args)
        finally:
            with _once_lock:
                _once_done.append(key)

    cb = callback(cftype, run, text_args)
    with _once_lock:
        _once[key] = cb
    return cb


def release_once(cb):
    """맡기지 못한 콜백을 바로 놓는다."""
    with _once_lock:
        for k, v in list(_once.items()):
            if v is cb:
                del _once[k]


def forget_once():
    """엔진을 끌 때 — 엔진이 아직 안 부른 것은 버리므로 전부 놓는다."""
    with _once_lock:
        _once.clear()
        _once_done.clear()


def keep(key, cb, replace):
    """엔진에 넘긴 콜백을 붙잡아 둔다 — 파이썬 GC 가 거두면 엔진이 사라진 함수를 부른다.
    CAD_SetXxx 는 한 칸이라 바꿔 끼우고, Register/Add 는 쌓는다."""
    is_null = cb is None or not cb   # NULL 함수 포인터는 거짓
    if replace:
        if is_null:
            _alive.pop(key, None)
        else:
            _alive[key] = cb
    elif not is_null:
        _alive.setdefault(key, []).append(cb)
