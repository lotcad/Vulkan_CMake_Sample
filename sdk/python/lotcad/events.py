# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Events 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_EVENT_OBJECT_CREATED', 'CAD_EVENT_OBJECT_DELETED', 'CAD_EVENT_SELECTION_CHANGED', 'CAD_EVENT_DOCUMENT_DIRTY', 'CAD_EVENT_COMMAND_STARTED', 'CAD_EVENT_COMMAND_ENDED', 'CAD_EVENT_COMMAND_CANCELLED', 'CAD_AddEventListener', 'CAD_RemoveEventListener', 'CAD_SetOnSelectionChanged', 'CAD_SetOnSelectionChanged_cb', 'CAD_SetOnObjectCreated', 'CAD_SetOnObjectCreated_cb', 'CAD_SetOnObjectDeleted', 'CAD_SetOnObjectDeleted_cb', 'CAD_SetOnDocumentDirty', 'CAD_SetOnDocumentDirty_cb', 'CAD_SetOnPrompt', 'CAD_SetOnPrompt_cb']

_f = _n.native

CAD_EVENT_OBJECT_CREATED = 1
CAD_EVENT_OBJECT_DELETED = 2
CAD_EVENT_SELECTION_CHANGED = 4
CAD_EVENT_DOCUMENT_DIRTY = 8
CAD_EVENT_COMMAND_STARTED = 16
CAD_EVENT_COMMAND_ENDED = 32
CAD_EVENT_COMMAND_CANCELLED = 64

CAD_SetOnSelectionChanged_cb = _c.CFUNCTYPE(None)
CAD_SetOnObjectCreated_cb = _c.CFUNCTYPE(None, _c.c_uint32)
CAD_SetOnObjectDeleted_cb = _c.CFUNCTYPE(None, _c.c_uint32)
CAD_SetOnDocumentDirty_cb = _c.CFUNCTYPE(None, _c.c_bool)
CAD_SetOnPrompt_cb = _c.CFUNCTYPE(None, _c.c_char_p)

_n.bind("CAD_AddEventListener", _c.c_uint, [_c.c_int, CAD_EventFn, _c.c_void_p, _c.c_uint])
_n.bind("CAD_RemoveEventListener", _c.c_bool, [_c.c_uint])
_n.bind("CAD_SetOnSelectionChanged", None, [CAD_SetOnSelectionChanged_cb])
_n.bind("CAD_SetOnObjectCreated", None, [CAD_SetOnObjectCreated_cb])
_n.bind("CAD_SetOnObjectDeleted", None, [CAD_SetOnObjectDeleted_cb])
_n.bind("CAD_SetOnDocumentDirty", None, [CAD_SetOnDocumentDirty_cb])
_n.bind("CAD_SetOnPrompt", None, [CAD_SetOnPrompt_cb])


def CAD_AddEventListener(kinds: int, fn: Callable | None, user: int | None, pluginId: int) -> int:
    """C: unsigned int CAD_AddEventListener(int kinds, CAD_EventFn fn, void* user, unsigned int pluginId)
    """
    _cb_fn = _n.callback(CAD_EventFn, fn, ())
    _n.keep("CAD_AddEventListener.fn", _cb_fn, replace=False)
    return _f.CAD_AddEventListener(kinds, _cb_fn, user, pluginId)


def CAD_RemoveEventListener(handle: int) -> bool:
    """C: bool CAD_RemoveEventListener(unsigned int handle)
    """
    return _f.CAD_RemoveEventListener(handle)


def CAD_SetOnSelectionChanged(cb: Callable | None) -> None:
    """C: void CAD_SetOnSelectionChanged(void (*cb)(void))

    알림(콜백)

    엔진 → 호스트 UI 방향의 알림. 이게 없으면 호스트는 **매 프레임 물어보는 수밖에**
    없다(선택이 바뀌었는지 알려고 GetSelectedCount 를 계속 호출하는 식).
    속성 패널·씬 트리·제목표시줄의 * 표시 같은 걸 붙이려면 사실상 필수다.
    ObjectARX 의 리액터(AcDbDatabaseReactor)와 같은 역할.

    ⚠️ 호출 시점은 **CAD_Tick 안**이다 — 프레임당 한 번, 엔진과 같은 스레드.
       그래서 콜백 안에서 다른 CAD_* 를 불러도 안전하다.
       변화가 **한 프레임에 여러 번** 나도 한 번으로 합쳐 알린다(UI 갱신엔 충분).
    nullptr 를 주면 해제된다.
    """
    _cb_cb = _n.callback(CAD_SetOnSelectionChanged_cb, cb, ())
    _n.keep("CAD_SetOnSelectionChanged.cb", _cb_cb, replace=True)
    _f.CAD_SetOnSelectionChanged(_cb_cb)


def CAD_SetOnObjectCreated(cb: Callable | None) -> None:
    """C: void CAD_SetOnObjectCreated (void (*cb)(uint32_t id))

    알림(콜백)

    엔진 → 호스트 UI 방향의 알림. 이게 없으면 호스트는 **매 프레임 물어보는 수밖에**
    없다(선택이 바뀌었는지 알려고 GetSelectedCount 를 계속 호출하는 식).
    속성 패널·씬 트리·제목표시줄의 * 표시 같은 걸 붙이려면 사실상 필수다.
    ObjectARX 의 리액터(AcDbDatabaseReactor)와 같은 역할.

    ⚠️ 호출 시점은 **CAD_Tick 안**이다 — 프레임당 한 번, 엔진과 같은 스레드.
       그래서 콜백 안에서 다른 CAD_* 를 불러도 안전하다.
       변화가 **한 프레임에 여러 번** 나도 한 번으로 합쳐 알린다(UI 갱신엔 충분).
    nullptr 를 주면 해제된다.
    """
    _cb_cb = _n.callback(CAD_SetOnObjectCreated_cb, cb, ())
    _n.keep("CAD_SetOnObjectCreated.cb", _cb_cb, replace=True)
    _f.CAD_SetOnObjectCreated(_cb_cb)


def CAD_SetOnObjectDeleted(cb: Callable | None) -> None:
    """C: void CAD_SetOnObjectDeleted (void (*cb)(uint32_t id))

    알림(콜백)

    엔진 → 호스트 UI 방향의 알림. 이게 없으면 호스트는 **매 프레임 물어보는 수밖에**
    없다(선택이 바뀌었는지 알려고 GetSelectedCount 를 계속 호출하는 식).
    속성 패널·씬 트리·제목표시줄의 * 표시 같은 걸 붙이려면 사실상 필수다.
    ObjectARX 의 리액터(AcDbDatabaseReactor)와 같은 역할.

    ⚠️ 호출 시점은 **CAD_Tick 안**이다 — 프레임당 한 번, 엔진과 같은 스레드.
       그래서 콜백 안에서 다른 CAD_* 를 불러도 안전하다.
       변화가 **한 프레임에 여러 번** 나도 한 번으로 합쳐 알린다(UI 갱신엔 충분).
    nullptr 를 주면 해제된다.
    """
    _cb_cb = _n.callback(CAD_SetOnObjectDeleted_cb, cb, ())
    _n.keep("CAD_SetOnObjectDeleted.cb", _cb_cb, replace=True)
    _f.CAD_SetOnObjectDeleted(_cb_cb)


def CAD_SetOnDocumentDirty(cb: Callable | None) -> None:
    """C: void CAD_SetOnDocumentDirty (void (*cb)(bool dirty))

    알림(콜백)

    엔진 → 호스트 UI 방향의 알림. 이게 없으면 호스트는 **매 프레임 물어보는 수밖에**
    없다(선택이 바뀌었는지 알려고 GetSelectedCount 를 계속 호출하는 식).
    속성 패널·씬 트리·제목표시줄의 * 표시 같은 걸 붙이려면 사실상 필수다.
    ObjectARX 의 리액터(AcDbDatabaseReactor)와 같은 역할.

    ⚠️ 호출 시점은 **CAD_Tick 안**이다 — 프레임당 한 번, 엔진과 같은 스레드.
       그래서 콜백 안에서 다른 CAD_* 를 불러도 안전하다.
       변화가 **한 프레임에 여러 번** 나도 한 번으로 합쳐 알린다(UI 갱신엔 충분).
    nullptr 를 주면 해제된다.
    """
    _cb_cb = _n.callback(CAD_SetOnDocumentDirty_cb, cb, ())
    _n.keep("CAD_SetOnDocumentDirty.cb", _cb_cb, replace=True)
    _f.CAD_SetOnDocumentDirty(_cb_cb)


def CAD_SetOnPrompt(cb: Callable | None) -> None:
    """C: void CAD_SetOnPrompt (void (*cb)(const char* text))

    하단 안내문(명령 프롬프트/임시 메시지)이 바뀔 때. 호스트 상태바에 그대로 띄우면 된다.
    """
    _cb_cb = _n.callback(CAD_SetOnPrompt_cb, cb, (0,))
    _n.keep("CAD_SetOnPrompt.cb", _cb_cb, replace=True)
    _f.CAD_SetOnPrompt(_cb_cb)
