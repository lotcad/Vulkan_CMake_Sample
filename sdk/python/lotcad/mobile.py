# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Mobile 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_SetOnCopyText', 'CAD_SetOnCopyText_cb', 'CAD_PasteText', 'CAD_BeginOcrLines', 'CAD_AddOcrLine', 'CAD_EndOcrLines', 'CAD_GetLength', 'CAD_GetArea', 'CAD_GetSelectionLength', 'CAD_GetSelectionArea']

_f = _n.native

CAD_SetOnCopyText_cb = _c.CFUNCTYPE(None, _c.c_char_p)

_n.bind("CAD_SetOnCopyText", None, [CAD_SetOnCopyText_cb])
_n.bind("CAD_PasteText", None, [_c.c_char_p])
_n.bind("CAD_BeginOcrLines", None, [_c.c_uint32])
_n.bind("CAD_AddOcrLine", None, [_c.c_char_p, _c.c_int, _c.c_int, _c.c_int, _c.c_int])
_n.bind("CAD_EndOcrLines", None, [])
_n.bind("CAD_GetLength", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float)])
_n.bind("CAD_GetArea", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float)])
_n.bind("CAD_GetSelectionLength", _c.c_float, [])
_n.bind("CAD_GetSelectionArea", _c.c_float, [])


def CAD_SetOnCopyText(cb: Callable | None) -> None:
    """C: void CAD_SetOnCopyText(void (*cb)(const char* utf8))

    클립보드 (모바일용)

    데스크톱은 ImGui 백엔드가 OS 클립보드로 연결해 주지만, iOS/안드로이드는 그게 없다.
    클립보드가 Swift 의 UIPasteboard / Kotlin 의 ClipboardManager 쪽에 있어서
    C++ 에서 직접 못 만진다. 그래서 **호스트가 대신 처리**한다.

      복사      : 엔진이 복사할 때 등록한 콜백이 불린다 → 호스트가 OS 클립보드에 넣는다
      붙여넣기  : 호스트가 CAD_PasteText 로 밀어 넣는다 (엔진이 물어보지 않는다)

    붙여넣기를 "미는" 이유: 엔진이 동기로 물어보면 호스트가 돌려주는 문자열의 수명을
    누가 책임지는지가 애매해진다. 모바일 UX 도 "붙여넣기 버튼을 누른다" 라 미는 쪽이 맞다.
    데스크톱에서도 등록하면 이쪽이 우선한다(임베드 앱이 자기 정책을 쓰고 싶을 때).
    """
    _cb_cb = _n.callback(CAD_SetOnCopyText_cb, cb, (0,))
    _n.keep("CAD_SetOnCopyText.cb", _cb_cb, replace=True)
    _f.CAD_SetOnCopyText(_cb_cb)


def CAD_PasteText(utf8: str | None) -> None:
    """C: void CAD_PasteText(const char* utf8)
    """
    _f.CAD_PasteText(_n.text(utf8))


def CAD_BeginOcrLines(imageId: int) -> None:
    """C: void CAD_BeginOcrLines(uint32_t imageId)

    OCR 결과 주입 (모바일용)

    모바일은 **OS 내장 OCR 을 쓴다** — iOS Vision, 안드로이드 ML Kit.
    Tesseract(45MB)를 올릴 이유가 없고, 내장 쪽이 한글·혼합 글자에서 더 정확하다.
    다만 둘 다 Swift/Kotlin API 라 C++ 에서 부르기 번거로우므로, **호스트가 인식하고
    결과만 넘긴다.** 그 뒤 흐름(네모 표시 → 드래그로 줄 고르기 → 커서 배치)은
    데스크톱과 완전히 같다.

    imageId : CAD_AttachImage* 로 붙인 이미지
    사각형  : 그 **이미지의 픽셀 좌표**(좌상단 원점). Vision 의 정규화 좌표를 쓰면
              호스트에서 픽셀로 바꿔 넘겨야 한다.
    호출 순서대로 = 읽는 순서. "시작~끝 사이 전부" 선택이 이 순서를 따른다.

      CAD_BeginOcrLines(imageId);
      CAD_AddOcrLine("거실 3600", 29, 29, 192, 64);
      CAD_EndOcrLines();          // 여기서 화면에 네모가 뜬다
    """
    _f.CAD_BeginOcrLines(imageId)


def CAD_AddOcrLine(utf8: str | None, x0: int, y0: int, x1: int, y1: int) -> None:
    """C: void CAD_AddOcrLine(const char* utf8, int x0, int y0, int x1, int y1)
    """
    _f.CAD_AddOcrLine(_n.text(utf8), x0, y0, x1, y1)


def CAD_EndOcrLines() -> None:
    """C: void CAD_EndOcrLines(void)
    """
    _f.CAD_EndOcrLines()


def CAD_GetLength(id: int) -> float | None:
    """C: bool CAD_GetLength(uint32_t id, float* outLength)
    """
    outLength = _c.c_float()
    if not _f.CAD_GetLength(id, _c.byref(outLength)):
        return None
    return outLength.value


def CAD_GetArea(id: int) -> float | None:
    """C: bool CAD_GetArea (uint32_t id, float* outArea)
    """
    outArea = _c.c_float()
    if not _f.CAD_GetArea(id, _c.byref(outArea)):
        return None
    return outArea.value


def CAD_GetSelectionLength() -> float:
    """C: float CAD_GetSelectionLength(void)

    선택 전체의 길이·면적 합. 선택이 비었거나 잴 게 없으면 0 을 돌려준다.
    """
    return _f.CAD_GetSelectionLength()


def CAD_GetSelectionArea() -> float:
    """C: float CAD_GetSelectionArea(void)
    """
    return _f.CAD_GetSelectionArea()
