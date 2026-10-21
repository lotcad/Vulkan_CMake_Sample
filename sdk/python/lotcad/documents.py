# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Documents 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_GetDocumentCount', 'CAD_GetActiveDocument', 'CAD_GetDocumentTitle', 'CAD_GetDocumentPath', 'CAD_IsDocumentDirty', 'CAD_NewDocument', 'CAD_OpenDocument', 'CAD_ActivateDocument', 'CAD_CloseDocument']

_f = _n.native

_n.bind("CAD_GetDocumentCount", _c.c_int, [])
_n.bind("CAD_GetActiveDocument", _c.c_int, [])
_n.bind("CAD_GetDocumentTitle", _c.c_int, [_c.c_int, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetDocumentPath", _c.c_int, [_c.c_int, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_IsDocumentDirty", _c.c_bool, [_c.c_int])
_n.bind("CAD_NewDocument", _c.c_int, [_c.c_char_p])
_n.bind("CAD_OpenDocument", _c.c_int, [_c.c_char_p])
_n.bind("CAD_ActivateDocument", _c.c_bool, [_c.c_int])
_n.bind("CAD_CloseDocument", _c.c_bool, [_c.c_int])


def CAD_GetDocumentCount() -> int:
    """C: int CAD_GetDocumentCount(void)

    여러 파일을 동시에 열고 탭으로 전환한다. 호스트(WPF/Qt)가 **자기 탭 UI** 를 그릴 수 있도록
    목록 조회 + 전환/열기/닫기를 모두 노출한다. 전환은 상태 swap 이라 비용이 거의 없다.
    """
    return _f.CAD_GetDocumentCount()


def CAD_GetActiveDocument() -> int:
    """C: int CAD_GetActiveDocument(void)

    여러 파일을 동시에 열고 탭으로 전환한다. 호스트(WPF/Qt)가 **자기 탭 UI** 를 그릴 수 있도록
    목록 조회 + 전환/열기/닫기를 모두 노출한다. 전환은 상태 swap 이라 비용이 거의 없다.
    """
    return _f.CAD_GetActiveDocument()


def CAD_GetDocumentTitle(index: int) -> str | None:
    """C: int CAD_GetDocumentTitle(int index, char* outUtf8, int cap)

    탭 라벨용 — 표시 이름(파일명 또는 "제목 없음"). 길이 반환, -1=실패. buf 는 null 허용(길이만 조회).
    """
    _need = _f.CAD_GetDocumentTitle(index, None, 0)   # 2회 호출 규약: 길이를 물으며 한 번 실행
    if _need < 0:
        return None
    _cap = _need + 1
    _buf = _c.create_string_buffer(_cap)
    if _f.CAD_GetDocumentTitle(index, _buf, _cap) < 0:   # 같은 인자 → 다시 실행하지 않고 결과만
        return None
    return _n.decode(_buf.value)


def CAD_GetDocumentPath(index: int) -> str | None:
    """C: int CAD_GetDocumentPath (int index, char* outUtf8, int cap)

    탭 라벨용 — 표시 이름(파일명 또는 "제목 없음"). 길이 반환, -1=실패. buf 는 null 허용(길이만 조회).
    """
    _need = _f.CAD_GetDocumentPath(index, None, 0)   # 2회 호출 규약: 길이를 물으며 한 번 실행
    if _need < 0:
        return None
    _cap = _need + 1
    _buf = _c.create_string_buffer(_cap)
    if _f.CAD_GetDocumentPath(index, _buf, _cap) < 0:   # 같은 인자 → 다시 실행하지 않고 결과만
        return None
    return _n.decode(_buf.value)


def CAD_IsDocumentDirty(index: int) -> bool:
    """C: bool CAD_IsDocumentDirty(int index)

    저장되지 않은 변경이 있는지 — 탭에 * 표시하거나 닫기 확인에 사용.
    """
    return _f.CAD_IsDocumentDirty(index)


def CAD_NewDocument(titleUtf8: str | None) -> int:
    """C: int CAD_NewDocument(const char* titleUtf8)

    새 빈 문서 추가 후 활성화. 반환 = 새 문서 인덱스.
    """
    return _f.CAD_NewDocument(_n.text(titleUtf8))


def CAD_OpenDocument(pathUtf8: str | None) -> int:
    """C: int CAD_OpenDocument(const char* pathUtf8)

    파일을 새 탭으로 열기. 반환 = 문서 인덱스, 실패 -1.
    """
    return _f.CAD_OpenDocument(_n.text(pathUtf8))


def CAD_ActivateDocument(index: int) -> bool:
    """C: bool CAD_ActivateDocument(int index)

    파일을 새 탭으로 열기. 반환 = 문서 인덱스, 실패 -1.
    """
    return _f.CAD_ActivateDocument(index)


def CAD_CloseDocument(index: int) -> bool:
    """C: bool CAD_CloseDocument(int index)

    닫기 — 마지막 문서는 닫지 않고 내용을 비운다(항상 문서 1개 유지).
    """
    return _f.CAD_CloseDocument(index)
