# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Drawing 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_CreateText', 'CAD_CreateDimension', 'CAD_SetTextContent', 'CAD_GetTextContent', 'CAD_CreateDrawingViews', 'CAD_CreateSectionView', 'CAD_CreateDetailView', 'CAD_MoveDrawingView', 'CAD_ClearDrawingViews', 'CAD_GetDrawingViewsJson', 'CAD_AttachImageFromFile', 'CAD_AttachImageFromMemory', 'CAD_BeginOcrLines', 'CAD_AddOcrLine', 'CAD_EndOcrLines', 'CAD_CreateLeader', 'CAD_CreateHatch', 'CAD_Plot']

_f = _n.native

_n.bind("CAD_CreateText", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_char_p, _c.c_float])
_n.bind("CAD_CreateDimension", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_SetTextContent", _c.c_bool, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_GetTextContent", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_CreateDrawingViews", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_float])
_n.bind("CAD_CreateSectionView", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateDetailView", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_MoveDrawingView", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float])
_n.bind("CAD_ClearDrawingViews", None, [])
_n.bind("CAD_GetDrawingViewsJson", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_AttachImageFromFile", _c.c_uint32, [_c.c_char_p, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_AttachImageFromMemory", _c.c_uint32, [_c.POINTER(_c.c_ubyte), _c.c_int, _c.c_int, _c.c_char_p, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_BeginOcrLines", None, [_c.c_uint32])
_n.bind("CAD_AddOcrLine", None, [_c.c_char_p, _c.c_int, _c.c_int, _c.c_int, _c.c_int])
_n.bind("CAD_EndOcrLines", None, [])
_n.bind("CAD_CreateLeader", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_char_p, _c.c_float])
_n.bind("CAD_CreateHatch", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_char_p, _c.c_float, _c.c_float])
_n.bind("CAD_Plot", _c.c_bool, [_c.c_char_p, _c.c_bool, _c.c_bool, _c.c_float, _c.c_float, _c.c_int])


def CAD_CreateText(x: float, y: float, z: float, utf8: str | None, heightMM: float) -> int:
    """C: uint32_t CAD_CreateText(float x, float y, float z, const char* utf8, float heightMM)
    """
    return _f.CAD_CreateText(x, y, z, _n.text(utf8), heightMM)


def CAD_CreateDimension(p1x: float, p1y: float, p1z: float, p2x: float, p2y: float, p2z: float, dlx: float, dly: float, dlz: float, nx: float, ny: float, nz: float) -> int:
    """C: uint32_t CAD_CreateDimension(float p1x, float p1y, float p1z, float p2x, float p2y, float p2z, float dlx, float dly, float dlz, float nx, float ny, float nz)

    선형 치수 — 측정점 p1/p2 + 치수선 위치점(dl) + 작업평면 법선(n). 반환=객체 id(0=실패).
    """
    return _f.CAD_CreateDimension(p1x, p1y, p1z, p2x, p2y, p2z, dlx, dly, dlz, nx, ny, nz)


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


def CAD_CreateDrawingViews(ids: Sequence | None, count: int, scale: float) -> int:
    """C: uint32_t CAD_CreateDrawingViews(const uint32_t* ids, uint32_t count, float scale)

    3D 를 고치면 따라온다(연관). 만들기·지우기·옮기기는 undo 1. 실패 0/false + CAD_GetLastError.
    CreateDrawingViews: 정면·평면·우측면(3각법) + 등각(0.6배), 모델 치수 자동. 반환 = 만든 뷰 수(4). ids 없으면(count 0) 보이는 솔리드 전부.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_CreateDrawingViews(_a_ids, count, scale)


def CAD_CreateSectionView(ax: float, ay: float, bx: float, by: float) -> int:
    """C: uint32_t CAD_CreateSectionView(float ax, float ay, float bx, float by)

    단면도 A-A — 정투상 뷰를 가로지르는 선(첫 점 → 둘째 점), 보는 쪽 = 선의 왼쪽. 반환 = 뷰 id.
    """
    return _f.CAD_CreateSectionView(ax, ay, bx, by)


def CAD_CreateDetailView(cx: float, cy: float, radius: float, factor: float) -> int:
    """C: uint32_t CAD_CreateDetailView(float cx, float cy, float radius, float factor)

    상세도 — 정투상 뷰 위 원(중심·반지름)을 factor 배(0 이면 2)로 도면 오른쪽에. 반환 = 뷰 id.
    """
    return _f.CAD_CreateDetailView(cx, cy, radius, factor)


def CAD_MoveDrawingView(viewId: int, dx: float, dy: float) -> bool:
    """C: bool CAD_MoveDrawingView(uint32_t viewId, float dx, float dy)

    뷰 옮기기 — 3각법 정렬 유지(평면도는 위아래, 우측면도는 좌우, 정면도는 매달린 뷰·단면도와 함께).
    """
    return _f.CAD_MoveDrawingView(viewId, dx, dy)


def CAD_ClearDrawingViews() -> None:
    """C: void CAD_ClearDrawingViews(void)

    뷰 옮기기 — 3각법 정렬 유지(평면도는 위아래, 우측면도는 좌우, 정면도는 매달린 뷰·단면도와 함께).
    """
    _f.CAD_ClearDrawingViews()


def CAD_GetDrawingViewsJson() -> str | None:
    """C: int CAD_GetDrawingViewsJson(char* out, int cap)

    뷰 목록 JSON — [{"id","name","kind":"base|section|detail","dir","up","origin","scale","hidden","dims","sources",
    "parent","label"(단면·상세),"bounds":{"min":[x,y],"max":[x,y]}}] — bounds = 뷰가 차지하는 자리(선 + 모델 치수 + 이름). 2회 호출 규약.
    """
    _need = _f.CAD_GetDrawingViewsJson(None, 0)   # 2회 호출 규약: 길이를 물으며 한 번 실행
    if _need < 0:
        return None
    _cap = _need + 1
    _buf = _c.create_string_buffer(_cap)
    if _f.CAD_GetDrawingViewsJson(_buf, _cap) < 0:   # 같은 인자 → 다시 실행하지 않고 결과만
        return None
    return _n.decode(_buf.value)


def CAD_AttachImageFromFile(pathUtf8: str | None, widthWorld: float, originX: float, originY: float, originZ: float) -> int:
    """C: uint32_t CAD_AttachImageFromFile(const char* pathUtf8, float widthWorld, float originX, float originY, float originZ)

    이미지 붙이기

    도면 밑에 깔 이미지(평면도 사진 등)를 XY 평면에 붙인다.
    엔진의 imageattach 명령은 **파일 대화상자를 띄우므로 모바일에서 못 쓴다** —
    호스트가 사진 앱(PHPicker / Intent)에서 고른 뒤 여기로 넘긴다.

      FromFile   : 경로로. 데스크톱·모바일 공통.
      FromMemory : RGBA8 픽셀을 직접. 사진 앱이 경로 대신 데이터를 주는 경우
                   (iOS PHPicker 가 그렇다) 파일로 떨구지 않고 바로 넘길 수 있다.

    widthWorld = 0 이면 긴 변이 10 단위가 되게 자동. 종횡비는 항상 보존한다.
    반환: 만들어진 객체 id (실패 0).
    """
    return _f.CAD_AttachImageFromFile(_n.text(pathUtf8), widthWorld, originX, originY, originZ)


def CAD_AttachImageFromMemory(rgba: Sequence | None, width: int, height: int, displayName: str | None, widthWorld: float, originX: float, originY: float, originZ: float) -> int:
    """C: uint32_t CAD_AttachImageFromMemory(const unsigned char* rgba, int width, int height, const char* displayName, float widthWorld, float originX, float originY, float originZ)

    이미지 붙이기

    도면 밑에 깔 이미지(평면도 사진 등)를 XY 평면에 붙인다.
    엔진의 imageattach 명령은 **파일 대화상자를 띄우므로 모바일에서 못 쓴다** —
    호스트가 사진 앱(PHPicker / Intent)에서 고른 뒤 여기로 넘긴다.

      FromFile   : 경로로. 데스크톱·모바일 공통.
      FromMemory : RGBA8 픽셀을 직접. 사진 앱이 경로 대신 데이터를 주는 경우
                   (iOS PHPicker 가 그렇다) 파일로 떨구지 않고 바로 넘길 수 있다.

    widthWorld = 0 이면 긴 변이 10 단위가 되게 자동. 종횡비는 항상 보존한다.
    반환: 만들어진 객체 id (실패 0).
    """
    _a_rgba = _n.array(_c.c_ubyte, rgba)
    return _f.CAD_AttachImageFromMemory(_a_rgba, width, height, _n.text(displayName), widthWorld, originX, originY, originZ)


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
    _f.CAD_AddOcrLine(_n.text(utf8), x0, y0, x1, y1)


def CAD_EndOcrLines() -> None:
    """C: void CAD_EndOcrLines(void)

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
    _f.CAD_EndOcrLines()


def CAD_CreateLeader(tipX: float, tipY: float, tipZ: float, bendX: float, bendY: float, bendZ: float, textUtf8: str | None, textHeight: float) -> int:
    """C: uint32_t CAD_CreateLeader(float tipX, float tipY, float tipZ, float bendX, float bendY, float bendZ, const char* textUtf8, float textHeight)

    지시선 — 화살촉 → 꺾임 점 + 글(UTF-8, 여러 줄은 \\n). textHeight<=0 이면 2.5. 평면은 XY. 실패 0.
    """
    return _f.CAD_CreateLeader(tipX, tipY, tipZ, bendX, bendY, bendZ, _n.text(textUtf8), textHeight)


def CAD_CreateHatch(ids: Sequence | None, count: int, pattern: str | None, scale: float, angleDeg: float) -> int:
    """C: uint32_t CAD_CreateHatch(const uint32_t* ids, uint32_t count, const char* pattern, float scale, float angleDeg)

    해치 — 닫힌 폴리선·사각형·원 ids(같은 평면이면 한 객체, 안쪽 루프 = 구멍). pattern: SOLID ANSI31~38 NET LINE DOTS BRICK STEEL CROSS
    (null/빈 = ANSI31), scale > 0, angleDeg. 선택이 새 해치로 바뀐다. 반환 = 해치 id, 실패 0.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_CreateHatch(_a_ids, count, _n.text(pattern), scale, angleDeg)


def CAD_Plot(path: str | None, selectedOnly: bool, monochrome: bool, paperW: float, paperH: float, pngLongSidePx: int) -> bool:
    """C: bool CAD_Plot(const char* path, bool selectedOnly, bool monochrome, float paperW, float paperH, int pngLongSidePx)

    도면 출력 — path 확장자로 .pdf(벡터)/.png(래스터). 지금 뷰 방향, 흰 종이. paperW/H mm(0 = A3 가로 420×297), pngLongSidePx(0 = 4000).
    selectedOnly = 선택만, monochrome = 흑백. 3D 메시·이미지는 아직 안 나온다.
    """
    return _f.CAD_Plot(_n.text(path), selectedOnly, monochrome, paperW, paperH, pngLongSidePx)
