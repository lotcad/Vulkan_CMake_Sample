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

_n.bind("CAD_CreateText", _c.c_int32, [CAD_GeVec3, _c.c_char_p, _c.c_double, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateDimension", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetTextContent", _c.c_int32, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_GetTextContent", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_CreateDrawingViews", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_double])
_n.bind("CAD_CreateSectionView", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateDetailView", _c.c_int32, [CAD_GeVec3, _c.c_double, _c.c_double, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_MoveDrawingView", _c.c_int32, [_c.c_uint32, CAD_GeVec3])
_n.bind("CAD_ClearDrawingViews", _c.c_int32, [])
_n.bind("CAD_GetDrawingViewsJson", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_AttachImageFromFile", _c.c_int32, [_c.c_char_p, _c.c_double, CAD_GeVec3, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_AttachImageFromMemory", _c.c_int32, [_c.POINTER(_c.c_ubyte), _c.c_int32, _c.c_int32, _c.c_char_p, _c.c_double, CAD_GeVec3, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_BeginOcrLines", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_AddOcrLine", _c.c_int32, [_c.c_char_p, _c.c_int32, _c.c_int32, _c.c_int32, _c.c_int32])
_n.bind("CAD_EndOcrLines", _c.c_int32, [])
_n.bind("CAD_CreateLeader", _c.c_int32, [CAD_GeVec3, CAD_GeVec3, _c.c_char_p, _c.c_double, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateHatch", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_char_p, _c.c_double, _c.c_double, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_Plot", _c.c_int32, [_c.c_char_p, _c.c_bool, _c.c_bool, _c.c_double, _c.c_double, _c.c_int32])


def CAD_CreateText(position: CAD_GeVec3, utf8: str | None, height: float, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateText(CAD_GeVec3 position, const char* utf8, double height, const CAD_CreateOptions* opt, uint32_t* outId)

    문자 — position = 기준점, height > 0(mm). 빈 글 "" 도 된다
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateText(position, _n.text(utf8), height, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateDimension(p1: CAD_GeVec3, p2: CAD_GeVec3, dimLinePoint: CAD_GeVec3, normal: CAD_GeVec3, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateDimension(CAD_GeVec3 p1, CAD_GeVec3 p2, CAD_GeVec3 dimLinePoint, CAD_GeVec3 normal, const CAD_CreateOptions* opt, uint32_t* outId)

    선형 치수 — 측정점 p1/p2 + 치수선 위치점 + 작업평면 법선. p1 = p2 · 법선 0 = CAD_E_DEGENERATE
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateDimension(p1, p2, dimLinePoint, normal, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_SetTextContent(id: int, utf8: str | None) -> int:
    """C: CAD_Status CAD_SetTextContent(uint32_t id, const char* utf8)

    글 바꾸기(되돌리기 1). 문자가 아님 = CAD_E_WRONG_TYPE, 잠김 = CAD_E_LOCKED
    """
    return _f.CAD_SetTextContent(id, _n.text(utf8))


def CAD_GetTextContent(id: int) -> str | None:
    """C: int32_t CAD_GetTextContent(uint32_t id, char* buf, uint32_t capacity)

    글 읽기 — buf 에 NUL 까지(모자라면 글자 경계에서 자름), 반환 = 전체 길이(NUL 제외). 문자가 아님 = CAD_E_WRONG_TYPE
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
    """C: int32_t CAD_CreateDrawingViews(const uint32_t* ids, uint32_t count, double scale)

    정면·평면·우측면(3각법) + 등각(0.6배), 모델 치수 자동. 반환 = 만든 뷰 수(4). ids 없으면(count 0) 보이는 솔리드 전부. scale 0 = 1
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_CreateDrawingViews(_a_ids, count, scale)


def CAD_CreateSectionView(a: CAD_GeVec3, b: CAD_GeVec3) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateSectionView(CAD_GeVec3 a, CAD_GeVec3 b, uint32_t* outViewId)

    단면도 A-A — 정투상 뷰를 가로지르는 선(첫 점 → 둘째 점), 보는 쪽 = 선의 왼쪽. *outViewId = 뷰 id
    """
    outViewId = _c.c_uint32()
    _r = _f.CAD_CreateSectionView(a, b, _c.byref(outViewId))
    return (_r, outViewId.value)


def CAD_CreateDetailView(center: CAD_GeVec3, radius: float, factor: float) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateDetailView(CAD_GeVec3 center, double radius, double factor, uint32_t* outViewId)

    상세도 — 정투상 뷰 위 원(중심·반지름 > 0)을 factor 배(0 = 2)로 도면 오른쪽에
    """
    outViewId = _c.c_uint32()
    _r = _f.CAD_CreateDetailView(center, radius, factor, _c.byref(outViewId))
    return (_r, outViewId.value)


def CAD_MoveDrawingView(viewId: int, offset: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_MoveDrawingView(uint32_t viewId, CAD_GeVec3 offset)

    뷰 옮기기(offset 의 x·y) — 3각법 정렬 유지(평면도는 위아래, 우측면도는 좌우, 정면도는 매달린 뷰·단면도와 함께).
    그 뷰가 없거나 정렬 때문에 못 움직임 = CAD_E_NOT_FOUND
    """
    return _f.CAD_MoveDrawingView(viewId, offset)


def CAD_ClearDrawingViews() -> int:
    """C: CAD_Status CAD_ClearDrawingViews(void)

    뷰 옮기기(offset 의 x·y) — 3각법 정렬 유지(평면도는 위아래, 우측면도는 좌우, 정면도는 매달린 뷰·단면도와 함께).
    그 뷰가 없거나 정렬 때문에 못 움직임 = CAD_E_NOT_FOUND
    """
    return _f.CAD_ClearDrawingViews()


def CAD_GetDrawingViewsJson() -> str | None:
    """C: int32_t CAD_GetDrawingViewsJson(char* buf, uint32_t capacity)

    뷰 목록 JSON — [{"id","name","kind":"base|section|detail","dir","up","origin","scale","hidden","dims","sources",
    "parent","label"(단면·상세),"bounds":{"min":[x,y],"max":[x,y]}}] — bounds = 뷰가 차지하는 자리(선 + 모델 치수 + 이름). 반환 = 전체 길이
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetDrawingViewsJson(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_AttachImageFromFile(pathUtf8: str | None, widthWorld: float, origin: CAD_GeVec3, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_AttachImageFromFile(const char* pathUtf8, double widthWorld, CAD_GeVec3 origin, const CAD_CreateOptions* opt, uint32_t* outId)

    이미지 붙이기

    도면 밑에 깔 이미지(평면도 사진 등)를 XY 평면에 붙인다.
    엔진의 imageattach 명령은 **파일 대화상자를 띄우므로 모바일에서 못 쓴다** —
    호스트가 사진 앱(PHPicker / Intent)에서 고른 뒤 여기로 넘긴다.

      FromFile   : 경로로. 데스크톱·모바일 공통. 파일이 없음 = CAD_E_NOT_FOUND, 못 읽음 = CAD_E_FAILED.
      FromMemory : RGBA8 픽셀(width × height × 4 바이트)을 직접. 사진 앱이 경로 대신 데이터를 주는 경우
                   (iOS PHPicker 가 그렇다) 파일로 떨구지 않고 바로 넘길 수 있다. displayName NULL = "이미지".

    widthWorld = 0 이면 긴 변이 10 단위가 되게 자동. 종횡비는 항상 보존한다. origin = 왼쪽 아래.
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_AttachImageFromFile(_n.text(pathUtf8), widthWorld, origin, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_AttachImageFromMemory(rgba: Sequence | None, width: int, height: int, displayName: str | None, widthWorld: float, origin: CAD_GeVec3, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_AttachImageFromMemory(const unsigned char* rgba, int32_t width, int32_t height, const char* displayName, double widthWorld, CAD_GeVec3 origin, const CAD_CreateOptions* opt, uint32_t* outId)

    이미지 붙이기

    도면 밑에 깔 이미지(평면도 사진 등)를 XY 평면에 붙인다.
    엔진의 imageattach 명령은 **파일 대화상자를 띄우므로 모바일에서 못 쓴다** —
    호스트가 사진 앱(PHPicker / Intent)에서 고른 뒤 여기로 넘긴다.

      FromFile   : 경로로. 데스크톱·모바일 공통. 파일이 없음 = CAD_E_NOT_FOUND, 못 읽음 = CAD_E_FAILED.
      FromMemory : RGBA8 픽셀(width × height × 4 바이트)을 직접. 사진 앱이 경로 대신 데이터를 주는 경우
                   (iOS PHPicker 가 그렇다) 파일로 떨구지 않고 바로 넘길 수 있다. displayName NULL = "이미지".

    widthWorld = 0 이면 긴 변이 10 단위가 되게 자동. 종횡비는 항상 보존한다. origin = 왼쪽 아래.
    """
    _a_rgba = _n.array(_c.c_ubyte, rgba)
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_AttachImageFromMemory(_a_rgba, width, height, _n.text(displayName), widthWorld, origin, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_BeginOcrLines(imageId: int) -> int:
    """C: CAD_Status CAD_BeginOcrLines(uint32_t imageId)

    OCR 결과 주입 (모바일용)

    모바일은 **OS 내장 OCR 을 쓴다** — iOS Vision, 안드로이드 ML Kit.
    Tesseract(45MB)를 올릴 이유가 없고, 내장 쪽이 한글·혼합 글자에서 더 정확하다.
    다만 둘 다 Swift/Kotlin API 라 C++ 에서 부르기 번거로우므로, **호스트가 인식하고
    결과만 넘긴다.** 그 뒤 흐름(네모 표시 → 드래그로 줄 고르기 → 커서 배치)은
    데스크톱과 완전히 같다.

    imageId : CAD_AttachImage* 로 붙인 이미지(없으면 CAD_E_BAD_HANDLE)
    사각형  : 그 **이미지의 픽셀 좌표**(좌상단 원점). Vision 의 정규화 좌표를 쓰면
              호스트에서 픽셀로 바꿔 넘겨야 한다.
    호출 순서대로 = 읽는 순서. "시작~끝 사이 전부" 선택이 이 순서를 따른다.
    Begin 없이 Add·End = CAD_E_NOT_READY, 빈 글 = CAD_E_INVALID_ARG.

      CAD_BeginOcrLines(imageId);
      CAD_AddOcrLine("거실 3600", 29, 29, 192, 64);
      CAD_EndOcrLines();          // 여기서 화면에 네모가 뜬다
    """
    return _f.CAD_BeginOcrLines(imageId)


def CAD_AddOcrLine(utf8: str | None, x0: int, y0: int, x1: int, y1: int) -> int:
    """C: CAD_Status CAD_AddOcrLine(const char* utf8, int32_t x0, int32_t y0, int32_t x1, int32_t y1)

    OCR 결과 주입 (모바일용)

    모바일은 **OS 내장 OCR 을 쓴다** — iOS Vision, 안드로이드 ML Kit.
    Tesseract(45MB)를 올릴 이유가 없고, 내장 쪽이 한글·혼합 글자에서 더 정확하다.
    다만 둘 다 Swift/Kotlin API 라 C++ 에서 부르기 번거로우므로, **호스트가 인식하고
    결과만 넘긴다.** 그 뒤 흐름(네모 표시 → 드래그로 줄 고르기 → 커서 배치)은
    데스크톱과 완전히 같다.

    imageId : CAD_AttachImage* 로 붙인 이미지(없으면 CAD_E_BAD_HANDLE)
    사각형  : 그 **이미지의 픽셀 좌표**(좌상단 원점). Vision 의 정규화 좌표를 쓰면
              호스트에서 픽셀로 바꿔 넘겨야 한다.
    호출 순서대로 = 읽는 순서. "시작~끝 사이 전부" 선택이 이 순서를 따른다.
    Begin 없이 Add·End = CAD_E_NOT_READY, 빈 글 = CAD_E_INVALID_ARG.

      CAD_BeginOcrLines(imageId);
      CAD_AddOcrLine("거실 3600", 29, 29, 192, 64);
      CAD_EndOcrLines();          // 여기서 화면에 네모가 뜬다
    """
    return _f.CAD_AddOcrLine(_n.text(utf8), x0, y0, x1, y1)


def CAD_EndOcrLines() -> int:
    """C: CAD_Status CAD_EndOcrLines(void)

    OCR 결과 주입 (모바일용)

    모바일은 **OS 내장 OCR 을 쓴다** — iOS Vision, 안드로이드 ML Kit.
    Tesseract(45MB)를 올릴 이유가 없고, 내장 쪽이 한글·혼합 글자에서 더 정확하다.
    다만 둘 다 Swift/Kotlin API 라 C++ 에서 부르기 번거로우므로, **호스트가 인식하고
    결과만 넘긴다.** 그 뒤 흐름(네모 표시 → 드래그로 줄 고르기 → 커서 배치)은
    데스크톱과 완전히 같다.

    imageId : CAD_AttachImage* 로 붙인 이미지(없으면 CAD_E_BAD_HANDLE)
    사각형  : 그 **이미지의 픽셀 좌표**(좌상단 원점). Vision 의 정규화 좌표를 쓰면
              호스트에서 픽셀로 바꿔 넘겨야 한다.
    호출 순서대로 = 읽는 순서. "시작~끝 사이 전부" 선택이 이 순서를 따른다.
    Begin 없이 Add·End = CAD_E_NOT_READY, 빈 글 = CAD_E_INVALID_ARG.

      CAD_BeginOcrLines(imageId);
      CAD_AddOcrLine("거실 3600", 29, 29, 192, 64);
      CAD_EndOcrLines();          // 여기서 화면에 네모가 뜬다
    """
    return _f.CAD_EndOcrLines()


def CAD_CreateLeader(tip: CAD_GeVec3, bend: CAD_GeVec3, textUtf8: str | None, textHeight: float, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateLeader(CAD_GeVec3 tip, CAD_GeVec3 bend, const char* textUtf8, double textHeight, const CAD_CreateOptions* opt, uint32_t* outId)

    지시선 — 화살촉 → 꺾임 점 + 글(UTF-8, 여러 줄은 \\n, NULL = 글 없음). textHeight <= 0 이면 2.5. 평면은 XY
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateLeader(tip, bend, _n.text(textUtf8), textHeight, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateHatch(ids: Sequence | None, count: int, pattern: str | None, scale: float, angle: float, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateHatch(const uint32_t* ids, uint32_t count, const char* pattern, double scale, double angle, const CAD_CreateOptions* opt, uint32_t* outId)

    해치 — 닫힌 폴리선·사각형·원 ids(같은 평면이면 한 객체, 안쪽 루프 = 구멍). pattern: SOLID ANSI31~38 NET LINE DOTS BRICK STEEL CROSS
    (NULL/빈 = ANSI31), scale > 0, angle rad. 선택이 새 해치로 바뀐다. 경계가 맞지 않음 = CAD_E_FAILED + 이유
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateHatch(_a_ids, count, _n.text(pattern), scale, angle, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_Plot(path: str | None, selectedOnly: bool, monochrome: bool, paperW: float, paperH: float, pngLongSidePx: int) -> int:
    """C: CAD_Status CAD_Plot(const char* path, bool selectedOnly, bool monochrome, double paperW, double paperH, int32_t pngLongSidePx)

    도면 출력 — path 확장자로 .pdf(벡터)/.png(래스터). 지금 뷰 방향, 흰 종이. paperW/H mm(0 = A3 가로 420×297), pngLongSidePx(0 = 4000).
    selectedOnly = 선택만(선택 없음 = CAD_E_NOT_FOUND), monochrome = 흑백. 3D 메시·이미지는 아직 안 나온다
    """
    return _f.CAD_Plot(_n.text(path), selectedOnly, monochrome, paperW, paperH, pngLongSidePx)
