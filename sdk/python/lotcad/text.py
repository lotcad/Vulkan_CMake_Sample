# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Text 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_CreateText', 'CAD_CreateDimension', 'CAD_BeginTextEdit', 'CAD_IsTextEditing', 'CAD_TextEditInsert', 'CAD_TextEditBackspace', 'CAD_TextEditDelete', 'CAD_TextEditMoveCaret', 'CAD_TextEditCommit', 'CAD_TextEditCancel', 'CAD_SetTextContent', 'CAD_GetTextContent', 'CAD_PushPullSelectedFace', 'CAD_InsetSelectedFace']

_f = _n.native

_n.bind("CAD_CreateText", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_char_p, _c.c_float])
_n.bind("CAD_CreateDimension", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_BeginTextEdit", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_IsTextEditing", _c.c_bool, [])
_n.bind("CAD_TextEditInsert", None, [_c.c_char_p])
_n.bind("CAD_TextEditBackspace", None, [])
_n.bind("CAD_TextEditDelete", None, [])
_n.bind("CAD_TextEditMoveCaret", None, [_c.c_int])
_n.bind("CAD_TextEditCommit", None, [])
_n.bind("CAD_TextEditCancel", None, [])
_n.bind("CAD_SetTextContent", _c.c_bool, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_GetTextContent", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_PushPullSelectedFace", _c.c_bool, [_c.c_float])
_n.bind("CAD_InsetSelectedFace", _c.c_bool, [_c.c_float])


def CAD_CreateText(x: float, y: float, z: float, utf8: str | None, heightMM: float) -> int:
    """C: uint32_t CAD_CreateText(float x, float y, float z, const char* utf8, float heightMM)
    """
    return _f.CAD_CreateText(x, y, z, _n.text(utf8), heightMM)


def CAD_CreateDimension(p1x: float, p1y: float, p1z: float, p2x: float, p2y: float, p2z: float, dlx: float, dly: float, dlz: float, nx: float, ny: float, nz: float) -> int:
    """C: uint32_t CAD_CreateDimension(float p1x, float p1y, float p1z, float p2x, float p2y, float p2z, float dlx, float dly, float dlz, float nx, float ny, float nz)

    선형 치수 — 측정점 p1/p2 + 치수선 위치점(dl) + 작업평면 법선(n). 반환=객체 id(0=실패).
    """
    return _f.CAD_CreateDimension(p1x, p1y, p1z, p2x, p2y, p2z, dlx, dly, dlz, nx, ny, nz)


def CAD_BeginTextEdit(id: int) -> bool:
    """C: bool CAD_BeginTextEdit(uint32_t id)
    """
    return _f.CAD_BeginTextEdit(id)


def CAD_IsTextEditing() -> bool:
    """C: bool CAD_IsTextEditing(void)
    """
    return _f.CAD_IsTextEditing()


def CAD_TextEditInsert(utf8: str | None) -> None:
    """C: void CAD_TextEditInsert(const char* utf8)

    커서 위치에 삽입(여러 글자 가능)
    """
    _f.CAD_TextEditInsert(_n.text(utf8))


def CAD_TextEditBackspace() -> None:
    """C: void CAD_TextEditBackspace(void)
    """
    _f.CAD_TextEditBackspace()


def CAD_TextEditDelete() -> None:
    """C: void CAD_TextEditDelete(void)
    """
    _f.CAD_TextEditDelete()


def CAD_TextEditMoveCaret(delta: int) -> None:
    """C: void CAD_TextEditMoveCaret(int delta)

    -1/+1 등
    """
    _f.CAD_TextEditMoveCaret(delta)


def CAD_TextEditCommit() -> None:
    """C: void CAD_TextEditCommit(void)

    undo 적재 + 종료
    """
    _f.CAD_TextEditCommit()


def CAD_TextEditCancel() -> None:
    """C: void CAD_TextEditCancel(void)

    원복 + 종료
    """
    _f.CAD_TextEditCancel()


def CAD_SetTextContent(id: int, utf8: str | None) -> bool:
    """C: bool CAD_SetTextContent(uint32_t id, const char* utf8)

    비대화형 변경(undo)
    """
    return _f.CAD_SetTextContent(id, _n.text(utf8))


def CAD_GetTextContent(id: int) -> str | None:
    """C: int CAD_GetTextContent(uint32_t id, char* outUtf8, int cap)

    길이 반환, -1=실패
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetTextContent(id, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_PushPullSelectedFace(distance: float) -> bool:
    """C: bool CAD_PushPullSelectedFace(float distance)

    선택한 면(면 선택 모드에서 클릭한 면)을 법선 방향으로 distance(mm, 양수=바깥) 밀어 새 메시로 — undo 1단계.
    면 선택이 없으면 false.
    """
    return _f.CAD_PushPullSelectedFace(distance)


def CAD_InsetSelectedFace(distance: float) -> bool:
    """C: bool CAD_InsetSelectedFace(float distance)

    선택한 평면의 볼록 면에 distance(mm) 폭의 안쪽 링을 만든다. distance=0 이면 자동 폭.
    면 선택이 없거나 오목/다중 경계 면이면 false. undo 1단계.
    """
    return _f.CAD_InsetSelectedFace(distance)
