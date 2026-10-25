# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Events 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_EVENT_OBJECT_CREATED', 'CAD_EVENT_OBJECT_DELETED', 'CAD_EVENT_SELECTION_CHANGED', 'CAD_EVENT_DOCUMENT_DIRTY', 'CAD_EVENT_COMMAND_STARTED', 'CAD_EVENT_COMMAND_ENDED', 'CAD_EVENT_COMMAND_CANCELLED', 'CAD_AddEventListener', 'CAD_RemoveEventListener', 'CAD_SetOnPrompt', 'CAD_SetOnPrompt_cb']

_f = _n.native

CAD_EVENT_OBJECT_CREATED = 1
CAD_EVENT_OBJECT_DELETED = 2
CAD_EVENT_SELECTION_CHANGED = 4
CAD_EVENT_DOCUMENT_DIRTY = 8
CAD_EVENT_COMMAND_STARTED = 16
CAD_EVENT_COMMAND_ENDED = 32
CAD_EVENT_COMMAND_CANCELLED = 64

CAD_SetOnPrompt_cb = _c.CFUNCTYPE(None, _c.c_char_p)

_n.bind("CAD_AddEventListener", _c.c_int32, [_c.c_uint32, CAD_EventFn, _c.c_void_p, _c.c_uint32, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_RemoveEventListener", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_SetOnPrompt", _c.c_int32, [CAD_SetOnPrompt_cb])


def CAD_AddEventListener(kinds: int, fn: Callable | None, user: int | None, pluginId: int) -> tuple[int, int]:
    """C: CAD_Status CAD_AddEventListener(uint32_t kinds, CAD_EventFn fn, void* user, uint32_t pluginId, uint32_t* outHandle)
    """
    _cb_fn = _n.callback(CAD_EventFn, fn, ())
    _n.keep("CAD_AddEventListener.fn", _cb_fn, replace=False)
    outHandle = _c.c_uint32()
    _r = _f.CAD_AddEventListener(kinds, _cb_fn, user, pluginId, _c.byref(outHandle))
    return (_r, outHandle.value)


def CAD_RemoveEventListener(handle: int) -> int:
    """C: CAD_Status CAD_RemoveEventListener(uint32_t handle)

    없는 핸들 CAD_E_NOT_FOUND
    """
    return _f.CAD_RemoveEventListener(handle)


def CAD_SetOnPrompt(cb: Callable | None) -> int:
    """C: CAD_Status CAD_SetOnPrompt(void (*cb)(const char* text))

    하단 안내문(명령 프롬프트/임시 메시지)이 바뀔 때 — 글을 넘겨 주는 알림이라 한 칸 콜백으로 남겼다. 호스트 상태바에 그대로 띄우면 된다.
    CAD_Tick 안(프레임 끝, 엔진 스레드)에서 바뀐 때만. NULL = 해제
    """
    _cb_cb = _n.callback(CAD_SetOnPrompt_cb, cb, (0,))
    _n.keep("CAD_SetOnPrompt.cb", _cb_cb, replace=True)
    return _f.CAD_SetOnPrompt(_cb_cb)
