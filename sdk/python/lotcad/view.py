# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — View 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_VIEW_FRONT', 'CAD_VIEW_TOP', 'CAD_VIEW_RIGHT', 'CAD_VIEW_ISOMETRIC', 'CAD_VIEW_LEFT', 'CAD_VIEW_BOTTOM', 'CAD_VIEW_BACK', 'CAD_SECTION_OFF', 'CAD_SECTION_PLANE', 'CAD_SECTION_SLICE', 'CAD_SECTION_BOX', 'CAD_LAYOUT_SINGLE', 'CAD_LAYOUT_DUAL', 'CAD_LAYOUT_TRIPLE', 'CAD_LAYOUT_QUAD', 'CAD_STYLE_SHADED', 'CAD_STYLE_SHADED_EDGE', 'CAD_STYLE_WIREFRAME', 'CAD_STYLE_WIREFRAME_EDGE', 'CAD_STYLE_HIDDEN_LINE', 'CAD_ZoomExtents', 'CAD_FocusSelected', 'CAD_SetView', 'CAD_SetProjection', 'CAD_GetProjection', 'CAD_SetViewDirection', 'CAD_SetViewPivot', 'CAD_ClearViewPivot', 'CAD_GetViewPivot', 'CAD_OrbitCamera', 'CAD_SetSection', 'CAD_SetSectionBox', 'CAD_SetSectionOptions', 'CAD_GetSectionStateJson', 'CAD_ExtractSectionTo2D', 'CAD_SetViewportLayout', 'CAD_GetViewportLayout', 'CAD_SetActiveViewport', 'CAD_GetActiveViewport', 'CAD_SetGridEnabled', 'CAD_SetDemoLighting', 'CAD_SetVisualStyle', 'CAD_SetSelectionStyle', 'CAD_GetSelectionStyle', 'CAD_SetSelectionLineWidth', 'CAD_SetHoverHighlight', 'CAD_GetHoverHighlight', 'CAD_SetHoverStyle', 'CAD_GetHoveredObject', 'CAD_SetDimensionTextScreenFixed', 'CAD_GetDimensionTextScreenFixed', 'CAD_AdjustTextureScale', 'CAD_AdjustLineWidth', 'CAD_SetCollisionEnabled', 'CAD_GetCollisionEnabled', 'CAD_CaptureViewport']

_f = _n.native

CAD_VIEW_FRONT = 0
CAD_VIEW_TOP = 1
CAD_VIEW_RIGHT = 2
CAD_VIEW_ISOMETRIC = 3
CAD_VIEW_LEFT = 4
CAD_VIEW_BOTTOM = 5
CAD_VIEW_BACK = 6
CAD_SECTION_OFF = 0
CAD_SECTION_PLANE = 1
CAD_SECTION_SLICE = 2
CAD_SECTION_BOX = 3
CAD_LAYOUT_SINGLE = 0
CAD_LAYOUT_DUAL = 1
CAD_LAYOUT_TRIPLE = 2
CAD_LAYOUT_QUAD = 3
CAD_STYLE_SHADED = 0
CAD_STYLE_SHADED_EDGE = 1
CAD_STYLE_WIREFRAME = 2
CAD_STYLE_WIREFRAME_EDGE = 3
CAD_STYLE_HIDDEN_LINE = 4

_n.bind("CAD_ZoomExtents", _c.c_int32, [])
_n.bind("CAD_FocusSelected", _c.c_int32, [])
_n.bind("CAD_SetView", _c.c_int32, [_c.c_int32])
_n.bind("CAD_SetProjection", _c.c_int32, [_c.c_bool])
_n.bind("CAD_GetProjection", _c.c_int32, [_c.POINTER(_c.c_bool)])
_n.bind("CAD_SetViewDirection", _c.c_int32, [CAD_GeVec3])
_n.bind("CAD_SetViewPivot", _c.c_int32, [CAD_GeVec3, _c.c_int32])
_n.bind("CAD_ClearViewPivot", _c.c_int32, [])
_n.bind("CAD_GetViewPivot", _c.c_int32, [_c.POINTER(CAD_GeVec3), _c.POINTER(_c.c_int32)])
_n.bind("CAD_OrbitCamera", _c.c_int32, [CAD_GeVec3, _c.c_double])
_n.bind("CAD_SetSection", _c.c_int32, [_c.c_int32, _c.c_int32, _c.c_double, _c.c_bool, _c.c_double])
_n.bind("CAD_SetSectionBox", _c.c_int32, [CAD_GeVec3, CAD_GeVec3])
_n.bind("CAD_SetSectionOptions", _c.c_int32, [_c.c_bool, _c.c_bool])
_n.bind("CAD_GetSectionStateJson", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_ExtractSectionTo2D", _c.c_int32, [_c.c_bool, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_SetViewportLayout", _c.c_int32, [_c.c_int32])
_n.bind("CAD_GetViewportLayout", _c.c_int32, [])
_n.bind("CAD_SetActiveViewport", _c.c_int32, [_c.c_int32])
_n.bind("CAD_GetActiveViewport", _c.c_int32, [])
_n.bind("CAD_SetGridEnabled", _c.c_int32, [_c.c_bool])
_n.bind("CAD_SetDemoLighting", _c.c_int32, [_c.c_bool])
_n.bind("CAD_SetVisualStyle", _c.c_int32, [_c.c_int32])
_n.bind("CAD_SetSelectionStyle", _c.c_int32, [_c.c_int32])
_n.bind("CAD_GetSelectionStyle", _c.c_int32, [])
_n.bind("CAD_SetSelectionLineWidth", _c.c_int32, [_c.c_double])
_n.bind("CAD_SetHoverHighlight", _c.c_int32, [_c.c_bool])
_n.bind("CAD_GetHoverHighlight", _c.c_int32, [_c.POINTER(_c.c_bool)])
_n.bind("CAD_SetHoverStyle", _c.c_int32, [CAD_Color, _c.c_double])
_n.bind("CAD_GetHoveredObject", _c.c_int32, [_c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetDimensionTextScreenFixed", _c.c_int32, [_c.c_bool])
_n.bind("CAD_GetDimensionTextScreenFixed", _c.c_int32, [_c.POINTER(_c.c_bool)])
_n.bind("CAD_AdjustTextureScale", _c.c_int32, [_c.c_double])
_n.bind("CAD_AdjustLineWidth", _c.c_int32, [_c.c_double])
_n.bind("CAD_SetCollisionEnabled", _c.c_int32, [_c.c_bool])
_n.bind("CAD_GetCollisionEnabled", _c.c_int32, [_c.POINTER(_c.c_bool)])
_n.bind("CAD_CaptureViewport", _c.c_int32, [_c.c_char_p, _c.c_bool])


def CAD_ZoomExtents() -> int:
    """C: CAD_Status CAD_ZoomExtents(void)

    카메라·뷰
    전체 보기
    """
    return _f.CAD_ZoomExtents()


def CAD_FocusSelected() -> int:
    """C: CAD_Status CAD_FocusSelected(void)

    고른 것 보기 — 선택이 없으면 CAD_E_NOT_FOUND

    묶음 주석: 카메라·뷰
    """
    return _f.CAD_FocusSelected()


def CAD_SetView(viewType: int) -> int:
    """C: CAD_Status CAD_SetView(int32_t viewType)

    CAD_VIEW_*, 범위 밖 CAD_E_OUT_OF_RANGE
    """
    return _f.CAD_SetView(viewType)


def CAD_SetProjection(ortho: bool) -> int:
    """C: CAD_Status CAD_SetProjection(bool ortho)

    직교 / 원근
    """
    return _f.CAD_SetProjection(ortho)


def CAD_GetProjection() -> tuple[int, bool]:
    """C: CAD_Status CAD_GetProjection(bool* outOrtho)

    활성 칸이 직교인가(맡긴 SetProjection 은 다음 틱 뒤에 보인다)
    """
    outOrtho = _c.c_bool()
    _r = _f.CAD_GetProjection(_c.byref(outOrtho))
    return (_r, outOrtho.value)


def CAD_SetViewDirection(direction: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_SetViewDirection(CAD_GeVec3 direction)

    임의 방향 시점 — 뷰큐브의 모서리(2면)·꼭짓점(3면)처럼. direction = 타겟에서 카메라 쪽 월드 방향(길이 무관, 0 = CAD_E_DEGENERATE).
    예: (1,-1,1) = 앞·우·위 꼭짓점
    """
    return _f.CAD_SetViewDirection(direction)


def CAD_SetViewPivot(point: CAD_GeVec3, axis: int) -> int:
    """C: CAD_Status CAD_SetViewPivot(CAD_GeVec3 point, int32_t axis)

    화면 회전 피벗(viewucs) — 작업 평면 UCS 와 별개로 화면을 돌릴 때의 중심·축. axis -1 = 축 자유(피벗만), 0·1·2 = X·Y·Z 축 둘레 턴테이블
    """
    return _f.CAD_SetViewPivot(point, axis)


def CAD_ClearViewPivot() -> int:
    """C: CAD_Status CAD_ClearViewPivot(void)

    화면 회전 피벗(viewucs) — 작업 평면 UCS 와 별개로 화면을 돌릴 때의 중심·축. axis -1 = 축 자유(피벗만), 0·1·2 = X·Y·Z 축 둘레 턴테이블
    """
    return _f.CAD_ClearViewPivot()


def CAD_GetViewPivot() -> tuple[int, CAD_GeVec3, int]:
    """C: CAD_Status CAD_GetViewPivot(CAD_GeVec3* outPoint, int32_t* outAxis)

    지금 피벗 — 없으면 CAD_E_NOT_FOUND. 출력은 NULL 가능
    """
    outPoint = CAD_GeVec3()
    outAxis = _c.c_int32()
    _r = _f.CAD_GetViewPivot(_c.byref(outPoint), _c.byref(outAxis))
    return (_r, outPoint, outAxis.value)


def CAD_OrbitCamera(axis: CAD_GeVec3, angle: float) -> int:
    """C: CAD_Status CAD_OrbitCamera(CAD_GeVec3 axis, double angle)

    지금 궤도 중심 둘레로 axis 축 angle(rad, 오른손) 만큼 — 턴테이블 = (0,0,1). 바로 돈다
    """
    return _f.CAD_OrbitCamera(axis, angle)


def CAD_SetSection(mode: int, axis: int, position: float, flip: bool, thickness: float) -> int:
    """C: CAD_Status CAD_SetSection(int32_t mode, int32_t axis, double position, bool flip, double thickness)
    """
    return _f.CAD_SetSection(mode, axis, position, flip, thickness)


def CAD_SetSectionBox(min: CAD_GeVec3, max: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_SetSectionBox(CAD_GeVec3 min, CAD_GeVec3 max)

    상자 값만(켜기는 CAD_SetSection(CAD_SECTION_BOX, …)), min < max
    """
    return _f.CAD_SetSectionBox(min, max)


def CAD_SetSectionOptions(showArrows: bool, selectedOnly: bool) -> int:
    """C: CAD_Status CAD_SetSectionOptions(bool showArrows, bool selectedOnly)
    """
    return _f.CAD_SetSectionOptions(showArrows, selectedOnly)


def CAD_GetSectionStateJson() -> str | None:
    """C: int32_t CAD_GetSectionStateJson(char* buf, uint32_t capacity)

    {"mode","modeName","axis","pos","flip","thickness","box":{"min","max"},"showArrows","selectedOnly","sceneBounds":{"min","max"}} — sceneBounds = 슬라이더 범위
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetSectionStateJson(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_ExtractSectionTo2D(includeBehind: bool, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_ExtractSectionTo2D(bool includeBehind, uint32_t* outIds, uint32_t capacity)

    지금 평면 단면 → 2D 윤곽(편집 가능한 폴리선, includeBehind 면 뒤쪽 회색 참조선 하나 더)을 모델 오른쪽 XY 평면에. 되돌리기 1.
    반환 = 만든 객체 수, outIds = 그 id(outIds = NULL·칸 모자람이면 아무것도 안 만들고 개수만). 평면 단면이 아니면 CAD_E_NOT_READY.
    """
    return _f.CAD_ExtractSectionTo2D(includeBehind, outIds, capacity)


def CAD_SetViewportLayout(layout: int) -> int:
    """C: CAD_Status CAD_SetViewportLayout(int32_t layout)

    CAD_LAYOUT_*
    """
    return _f.CAD_SetViewportLayout(layout)


def CAD_GetViewportLayout() -> int:
    """C: int32_t CAD_GetViewportLayout(void)

    CAD_LAYOUT_*, 음수 = 오류
    """
    return _f.CAD_GetViewportLayout()


def CAD_SetActiveViewport(index: int) -> int:
    """C: CAD_Status CAD_SetActiveViewport(int32_t index)

    칸 번호 0 ~ (지금 칸 수 − 1)
    """
    return _f.CAD_SetActiveViewport(index)


def CAD_GetActiveViewport() -> int:
    """C: int32_t CAD_GetActiveViewport(void)
    """
    return _f.CAD_GetActiveViewport()


def CAD_SetGridEnabled(enabled: bool) -> int:
    """C: CAD_Status CAD_SetGridEnabled(bool enabled)

    표시
    """
    return _f.CAD_SetGridEnabled(enabled)


def CAD_SetDemoLighting(enabled: bool) -> int:
    """C: CAD_Status CAD_SetDemoLighting(bool enabled)

    표시
    """
    return _f.CAD_SetDemoLighting(enabled)


def CAD_SetVisualStyle(style: int) -> int:
    """C: CAD_Status CAD_SetVisualStyle(int32_t style)

    CAD_STYLE_*
    """
    return _f.CAD_SetVisualStyle(style)


def CAD_SetSelectionStyle(style: int) -> int:
    """C: CAD_Status CAD_SetSelectionStyle(int32_t style)

    선택 강조 — 0 = 실루엣(JFA 외곽선), 1 = 모서리(노란 특징선, CAD 식)
    """
    return _f.CAD_SetSelectionStyle(style)


def CAD_GetSelectionStyle() -> int:
    """C: int32_t CAD_GetSelectionStyle(void)

    선택 강조 — 0 = 실루엣(JFA 외곽선), 1 = 모서리(노란 특징선, CAD 식)
    """
    return _f.CAD_GetSelectionStyle()


def CAD_SetSelectionLineWidth(width: float) -> int:
    """C: CAD_Status CAD_SetSelectionLineWidth(double width)

    선택 표시 두께(px, 색은 노란색 고정 — CAD 관례)
    """
    return _f.CAD_SetSelectionLineWidth(width)


def CAD_SetHoverHighlight(enabled: bool) -> int:
    """C: CAD_Status CAD_SetHoverHighlight(bool enabled)

    호버 강조 — 마우스가 올라간 객체를 연한 하늘색 모서리로(기본 켬)
    """
    return _f.CAD_SetHoverHighlight(enabled)


def CAD_GetHoverHighlight() -> tuple[int, bool]:
    """C: CAD_Status CAD_GetHoverHighlight(bool* outEnabled)

    호버 강조 — 마우스가 올라간 객체를 연한 하늘색 모서리로(기본 켬)
    """
    outEnabled = _c.c_bool()
    _r = _f.CAD_GetHoverHighlight(_c.byref(outEnabled))
    return (_r, outEnabled.value)


def CAD_SetHoverStyle(color: CAD_Color, width: float) -> int:
    """C: CAD_Status CAD_SetHoverStyle(CAD_Color color, double width)

    호버 색·두께(px 0.5~10). ⚠️ 두께는 GPU 가 굵은 선을 받을 때만(못 받는 장치는 1px)
    """
    return _f.CAD_SetHoverStyle(color, width)


def CAD_GetHoveredObject() -> tuple[int, int]:
    """C: CAD_Status CAD_GetHoveredObject(uint32_t* outId)

    지금 커서 아래 객체(없으면 0 — 오류 아님). 호스트가 상태바·툴팁에 이름을 띄울 때
    """
    outId = _c.c_uint32()
    _r = _f.CAD_GetHoveredObject(_c.byref(outId))
    return (_r, outId.value)


def CAD_SetDimensionTextScreenFixed(enabled: bool) -> int:
    """C: CAD_Status CAD_SetDimensionTextScreenFixed(bool enabled)

    치수 **글자**를 줌과 무관하게 화면에서 같은 크기로(기본 끔). 모바일 측정 도구용 — 도면 출력은 월드 크기여야 하니 데스크톱은 끔
    """
    return _f.CAD_SetDimensionTextScreenFixed(enabled)


def CAD_GetDimensionTextScreenFixed() -> tuple[int, bool]:
    """C: CAD_Status CAD_GetDimensionTextScreenFixed(bool* outEnabled)

    치수 **글자**를 줌과 무관하게 화면에서 같은 크기로(기본 끔). 모바일 측정 도구용 — 도면 출력은 월드 크기여야 하니 데스크톱은 끔
    """
    outEnabled = _c.c_bool()
    _r = _f.CAD_GetDimensionTextScreenFixed(_c.byref(outEnabled))
    return (_r, outEnabled.value)


def CAD_AdjustTextureScale(delta: float) -> int:
    """C: CAD_Status CAD_AdjustTextureScale(double delta)

    고른 객체의 텍스처 축척을 delta 만큼 · 선 두께(px)를 deltaPx 만큼 늘리고 줄이기
    """
    return _f.CAD_AdjustTextureScale(delta)


def CAD_AdjustLineWidth(deltaPx: float) -> int:
    """C: CAD_Status CAD_AdjustLineWidth(double deltaPx)

    고른 객체의 텍스처 축척을 delta 만큼 · 선 두께(px)를 deltaPx 만큼 늘리고 줄이기
    """
    return _f.CAD_AdjustLineWidth(deltaPx)


def CAD_SetCollisionEnabled(enabled: bool) -> int:
    """C: CAD_Status CAD_SetCollisionEnabled(bool enabled)

    벽 충돌(걷기·캐릭터 모드) — 끄면 벽을 지나간다. ⚠️ 정적 형상 대상의 캐릭터 충돌이지 물리 엔진이 아니다
    """
    return _f.CAD_SetCollisionEnabled(enabled)


def CAD_GetCollisionEnabled() -> tuple[int, bool]:
    """C: CAD_Status CAD_GetCollisionEnabled(bool* outEnabled)

    벽 충돌(걷기·캐릭터 모드) — 끄면 벽을 지나간다. ⚠️ 정적 형상 대상의 캐릭터 충돌이지 물리 엔진이 아니다
    """
    outEnabled = _c.c_bool()
    _r = _f.CAD_GetCollisionEnabled(_c.byref(outEnabled))
    return (_r, outEnabled.value)


def CAD_CaptureViewport(pathUtf8: str | None, clean: bool) -> int:
    """C: CAD_Status CAD_CaptureViewport(const char* pathUtf8, bool clean)

    화면 캡처 → PNG(창 전체, 경로 UTF-8). clean = 격자·뷰큐브 없이. 한 프레임 그려 파일이 생겼는지까지 보고 돌아온다
    (엔진 틱 안 — 플러그인 콜백 등 — 에서 불리면 요청만 남기고 다음 프레임에 찍는다, CAD_OK = 맡김). 못 찍으면 CAD_E_FAILED.
    """
    return _f.CAD_CaptureViewport(_n.text(pathUtf8), clean)
