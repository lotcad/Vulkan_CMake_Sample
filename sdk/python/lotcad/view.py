# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — View 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_SetDimensionTextScreenFixed', 'CAD_GetDimensionTextScreenFixed', 'CAD_RequestZoomExtents', 'CAD_RequestFocusSelected', 'CAD_RequestToggleProjection', 'CAD_RequestToggleDemoLighting', 'CAD_RequestAdjustTextureScale', 'CAD_RequestAdjustLineWidth', 'CAD_RequestSetView', 'CAD_RequestSetProjection', 'CAD_RequestSetViewDirection', 'CAD_RequestSetViewPivot', 'CAD_RequestClearViewPivot', 'CAD_GetViewPivot', 'CAD_SetSection', 'CAD_SetSectionBox', 'CAD_SetSectionOptions', 'CAD_GetSectionStateJson', 'CAD_ExtractSectionTo2D', 'CAD_SetViewportLayout', 'CAD_GetViewportLayout', 'CAD_SetActiveViewport', 'CAD_GetActiveViewport', 'CAD_SetGridEnabled', 'CAD_SetDemoLighting', 'CAD_SetVisualStyle', 'CAD_SetSelectionStyle', 'CAD_GetSelectionStyle', 'CAD_SetHoverHighlight', 'CAD_GetHoverHighlight', 'CAD_GetHoveredObject', 'CAD_SetHoverStyle', 'CAD_SetSelectionLineWidth', 'CAD_SetCollisionEnabled', 'CAD_GetCollisionEnabled', 'CAD_CaptureViewport', 'CAD_OrbitCamera']

_f = _n.native

_n.bind("CAD_SetDimensionTextScreenFixed", None, [_c.c_bool])
_n.bind("CAD_GetDimensionTextScreenFixed", _c.c_bool, [])
_n.bind("CAD_RequestZoomExtents", None, [])
_n.bind("CAD_RequestFocusSelected", None, [])
_n.bind("CAD_RequestToggleProjection", None, [])
_n.bind("CAD_RequestToggleDemoLighting", None, [])
_n.bind("CAD_RequestAdjustTextureScale", None, [_c.c_float])
_n.bind("CAD_RequestAdjustLineWidth", None, [_c.c_float])
_n.bind("CAD_RequestSetView", None, [_c.c_int])
_n.bind("CAD_RequestSetProjection", None, [_c.c_bool])
_n.bind("CAD_RequestSetViewDirection", None, [_c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_RequestSetViewPivot", None, [_c.c_float, _c.c_float, _c.c_float, _c.c_int])
_n.bind("CAD_RequestClearViewPivot", None, [])
_n.bind("CAD_GetViewPivot", _c.c_bool, [_c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_int)])
_n.bind("CAD_SetSection", _c.c_bool, [_c.c_int, _c.c_int, _c.c_float, _c.c_bool, _c.c_float])
_n.bind("CAD_SetSectionBox", _c.c_bool, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_SetSectionOptions", None, [_c.c_bool, _c.c_bool])
_n.bind("CAD_GetSectionStateJson", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_ExtractSectionTo2D", _c.c_uint32, [_c.c_bool])
_n.bind("CAD_SetViewportLayout", None, [_c.c_int])
_n.bind("CAD_GetViewportLayout", _c.c_int, [])
_n.bind("CAD_SetActiveViewport", None, [_c.c_int])
_n.bind("CAD_GetActiveViewport", _c.c_int, [])
_n.bind("CAD_SetGridEnabled", None, [_c.c_bool])
_n.bind("CAD_SetDemoLighting", None, [_c.c_bool])
_n.bind("CAD_SetVisualStyle", None, [_c.c_int])
_n.bind("CAD_SetSelectionStyle", None, [_c.c_int])
_n.bind("CAD_GetSelectionStyle", _c.c_int, [])
_n.bind("CAD_SetHoverHighlight", None, [_c.c_bool])
_n.bind("CAD_GetHoverHighlight", _c.c_bool, [])
_n.bind("CAD_GetHoveredObject", _c.c_uint, [])
_n.bind("CAD_SetHoverStyle", None, [_c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_SetSelectionLineWidth", None, [_c.c_float])
_n.bind("CAD_SetCollisionEnabled", None, [_c.c_bool])
_n.bind("CAD_GetCollisionEnabled", _c.c_bool, [])
_n.bind("CAD_CaptureViewport", _c.c_bool, [_c.c_char_p, _c.c_bool])
_n.bind("CAD_OrbitCamera", None, [_c.c_float, _c.c_float, _c.c_float, _c.c_float])


def CAD_SetDimensionTextScreenFixed(enabled: bool) -> None:
    """C: void CAD_SetDimensionTextScreenFixed(bool enabled)

    치수 **문자**를 줌과 무관하게 화면상 같은 크기로 그릴지 (기본 false).
    모바일에서 치수는 도면 요소보다 "측정 도구" 에 가깝다 — 줌아웃하면 글자가 같이 작아져
    값을 못 읽는 게 문제였다. 켜면 글자가 항상 읽히는 크기로 남는다(선·화살표는 그대로).
    데스크톱은 끄는 게 맞다 — 도면 출력에선 월드 크기여야 한다.
    매 프레임 비용은 없다(플래그를 정점에 굽는다). 전환 시 기존 치수를 한 번 다시 만든다.
    """
    _f.CAD_SetDimensionTextScreenFixed(enabled)


def CAD_GetDimensionTextScreenFixed() -> bool:
    """C: bool CAD_GetDimensionTextScreenFixed(void)

    치수 **문자**를 줌과 무관하게 화면상 같은 크기로 그릴지 (기본 false).
    모바일에서 치수는 도면 요소보다 "측정 도구" 에 가깝다 — 줌아웃하면 글자가 같이 작아져
    값을 못 읽는 게 문제였다. 켜면 글자가 항상 읽히는 크기로 남는다(선·화살표는 그대로).
    데스크톱은 끄는 게 맞다 — 도면 출력에선 월드 크기여야 한다.
    매 프레임 비용은 없다(플래그를 정점에 굽는다). 전환 시 기존 치수를 한 번 다시 만든다.
    """
    return _f.CAD_GetDimensionTextScreenFixed()


def CAD_RequestZoomExtents() -> None:
    """C: void CAD_RequestZoomExtents(void)
    """
    _f.CAD_RequestZoomExtents()


def CAD_RequestFocusSelected() -> None:
    """C: void CAD_RequestFocusSelected(void)
    """
    _f.CAD_RequestFocusSelected()


def CAD_RequestToggleProjection() -> None:
    """C: void CAD_RequestToggleProjection(void)
    """
    _f.CAD_RequestToggleProjection()


def CAD_RequestToggleDemoLighting() -> None:
    """C: void CAD_RequestToggleDemoLighting(void)
    """
    _f.CAD_RequestToggleDemoLighting()


def CAD_RequestAdjustTextureScale(delta: float) -> None:
    """C: void CAD_RequestAdjustTextureScale(float delta)
    """
    _f.CAD_RequestAdjustTextureScale(delta)


def CAD_RequestAdjustLineWidth(deltaPx: float) -> None:
    """C: void CAD_RequestAdjustLineWidth(float deltaPx)
    """
    _f.CAD_RequestAdjustLineWidth(deltaPx)


def CAD_RequestSetView(viewType: int) -> None:
    """C: void CAD_RequestSetView(int viewType)

    viewType: 0=Front 1=Top 2=Right 3=Isometric 4=Left 5=Bottom 6=Back
    """
    _f.CAD_RequestSetView(viewType)


def CAD_RequestSetProjection(ortho: bool) -> None:
    """C: void CAD_RequestSetProjection(bool ortho)

    viewType: 0=Front 1=Top 2=Right 3=Isometric 4=Left 5=Bottom 6=Back
    """
    _f.CAD_RequestSetProjection(ortho)


def CAD_RequestSetViewDirection(dirX: float, dirY: float, dirZ: float) -> None:
    """C: void CAD_RequestSetViewDirection(float dirX, float dirY, float dirZ)

    임의 방향 시점 — 뷰큐브의 모서리(2면)/꼭짓점(3면)처럼 표준 6뷰가 아닌 방향에서 보기.
    dir = 타겟에서 카메라를 향하는 월드 방향(정규화 불필요). 예: (1,-1,1)=앞·우·위 꼭짓점.
    """
    _f.CAD_RequestSetViewDirection(dirX, dirY, dirZ)


def CAD_RequestSetViewPivot(x: float, y: float, z: float, axis: int) -> None:
    """C: void CAD_RequestSetViewPivot(float x, float y, float z, int axis)

    뷰 회전 피벗 (viewucs) — 작업평면 UCS 와 별개로, 화면을 돌릴 때의 중심/축을 지정한다.
    axis: -1=축 자유(피벗만 고정), 0=X 축 고정, 1=Y, 2=Z (축 고정 시 그 축 기준 턴테이블 회전)
    """
    _f.CAD_RequestSetViewPivot(x, y, z, axis)


def CAD_RequestClearViewPivot() -> None:
    """C: void CAD_RequestClearViewPivot(void)

    뷰 회전 피벗 (viewucs) — 작업평면 UCS 와 별개로, 화면을 돌릴 때의 중심/축을 지정한다.
    axis: -1=축 자유(피벗만 고정), 0=X 축 고정, 1=Y, 2=Z (축 고정 시 그 축 기준 턴테이블 회전)
    """
    _f.CAD_RequestClearViewPivot()


def CAD_GetViewPivot() -> tuple[float, float, float, int] | None:
    """C: bool CAD_GetViewPivot(float* x, float* y, float* z, int* axis)

    현재 피벗 조회 — 설정돼 있으면 true. out 인자는 null 허용.
    """
    x = _c.c_float()
    y = _c.c_float()
    z = _c.c_float()
    axis = _c.c_int()
    if not _f.CAD_GetViewPivot(_c.byref(x), _c.byref(y), _c.byref(z), _c.byref(axis)):
        return None
    return (x.value, y.value, z.value, axis.value)


def CAD_SetSection(mode: int, axis: int, pos: float, flip: bool, thickness: float) -> bool:
    """C: bool CAD_SetSection(int mode, int axis, float pos, bool flip, float thickness)

    mode 0 끄기 1 평면(axis 위치 pos 보다 큰 쪽을 자름, flip 이면 반대) 2 슬라이스(pos 중심 thickness 두께만 남김) 3 상자(SetSectionBox).
    axis 0 X 1 Y 2 Z. thickness 는 슬라이스에만(0 이하면 지금 값 유지). 틀린 값 false.
    """
    return _f.CAD_SetSection(mode, axis, pos, flip, thickness)


def CAD_SetSectionBox(minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float) -> bool:
    """C: bool CAD_SetSectionBox(float minX, float minY, float minZ, float maxX, float maxY, float maxZ)

    상자 값만(켜기는 SetSection(3,…))

    묶음 주석: mode 0 끄기 1 평면(axis 위치 pos 보다 큰 쪽을 자름, flip 이면 반대) 2 슬라이스(pos 중심 thickness 두께만 남김) 3 상자(SetSectionBox).
    axis 0 X 1 Y 2 Z. thickness 는 슬라이스에만(0 이하면 지금 값 유지). 틀린 값 false.
    """
    return _f.CAD_SetSectionBox(minX, minY, minZ, maxX, maxY, maxZ)


def CAD_SetSectionOptions(showArrows: bool, selectedOnly: bool) -> None:
    """C: void CAD_SetSectionOptions(bool showArrows, bool selectedOnly)

    mode 0 끄기 1 평면(axis 위치 pos 보다 큰 쪽을 자름, flip 이면 반대) 2 슬라이스(pos 중심 thickness 두께만 남김) 3 상자(SetSectionBox).
    axis 0 X 1 Y 2 Z. thickness 는 슬라이스에만(0 이하면 지금 값 유지). 틀린 값 false.
    """
    _f.CAD_SetSectionOptions(showArrows, selectedOnly)


def CAD_GetSectionStateJson() -> str | None:
    """C: int CAD_GetSectionStateJson(char* out, int cap)

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


def CAD_ExtractSectionTo2D(includeBehind: bool) -> int:
    """C: uint32_t CAD_ExtractSectionTo2D(bool includeBehind)

    지금 평면 단면 → 2D 윤곽(편집 가능한 폴리선, includeBehind 면 뒤쪽 회색 참조선 1개 더)을 모델 오른쪽 XY 평면에. 반환 = 만든 객체 수, undo 1.
    """
    return _f.CAD_ExtractSectionTo2D(includeBehind)


def CAD_SetViewportLayout(layout: int) -> None:
    """C: void CAD_SetViewportLayout(int layout)

    layout: 0=Single(단일) 1=Dual(좌우) 2=Triple 3=Quad(2x2)
    """
    _f.CAD_SetViewportLayout(layout)


def CAD_GetViewportLayout() -> int:
    """C: int CAD_GetViewportLayout(void)

    layout: 0=Single(단일) 1=Dual(좌우) 2=Triple 3=Quad(2x2)
    """
    return _f.CAD_GetViewportLayout()


def CAD_SetActiveViewport(index: int) -> None:
    """C: void CAD_SetActiveViewport(int index)

    활성(클릭) 뷰포트 칸 인덱스 0~3.
    """
    _f.CAD_SetActiveViewport(index)


def CAD_GetActiveViewport() -> int:
    """C: int CAD_GetActiveViewport(void)

    활성(클릭) 뷰포트 칸 인덱스 0~3.
    """
    return _f.CAD_GetActiveViewport()


def CAD_SetGridEnabled(enabled: bool) -> None:
    """C: void CAD_SetGridEnabled(bool enabled)
    """
    _f.CAD_SetGridEnabled(enabled)


def CAD_SetDemoLighting(enabled: bool) -> None:
    """C: void CAD_SetDemoLighting(bool enabled)
    """
    _f.CAD_SetDemoLighting(enabled)


def CAD_SetVisualStyle(style: int) -> None:
    """C: void CAD_SetVisualStyle(int style)

    style: 0=Shaded 1=ShadedEdge 2=Wireframe 3=WireframeEdge 4=HiddenLine
    """
    _f.CAD_SetVisualStyle(style)


def CAD_SetSelectionStyle(style: int) -> None:
    """C: void CAD_SetSelectionStyle(int style)

    선택 하이라이트 스타일: 0=Silhouette(JFA 외곽선), 1=Edge(feature edge 노란색, CAD 방식)
    """
    _f.CAD_SetSelectionStyle(style)


def CAD_GetSelectionStyle() -> int:
    """C: int CAD_GetSelectionStyle(void)

    선택 하이라이트 스타일: 0=Silhouette(JFA 외곽선), 1=Edge(feature edge 노란색, CAD 방식)
    """
    return _f.CAD_GetSelectionStyle()


def CAD_SetHoverHighlight(enabled: bool) -> None:
    """C: void CAD_SetHoverHighlight(bool enabled)

    호버 강조 — 마우스가 올라간 객체를 연한 하늘색 엣지로 표시(선택은 노란색).
    기본 켬. 도면 작업 중 시선 분산이 싫거나 초대형 씬에서 부담될 때 끌 수 있다.
    """
    _f.CAD_SetHoverHighlight(enabled)


def CAD_GetHoverHighlight() -> bool:
    """C: bool CAD_GetHoverHighlight(void)

    호버 강조 — 마우스가 올라간 객체를 연한 하늘색 엣지로 표시(선택은 노란색).
    기본 켬. 도면 작업 중 시선 분산이 싫거나 초대형 씬에서 부담될 때 끌 수 있다.
    """
    return _f.CAD_GetHoverHighlight()


def CAD_GetHoveredObject() -> int:
    """C: unsigned int CAD_GetHoveredObject(void)

    현재 커서 아래 객체 id (없으면 0). 호스트가 상태바·툴팁에 이름을 띄우는 용도.
    """
    return _f.CAD_GetHoveredObject()


def CAD_SetHoverStyle(r: float, g: float, b: float, width: float) -> None:
    """C: void CAD_SetHoverStyle(float r, float g, float b, float width)

    호버 표시 스타일 — 색(0~1) + 선 두께(px, 0.5~10 로 클램프).
    ⚠️ 두께는 GPU 가 wide line 을 지원할 때만 반영된다(미지원 기기는 1px 고정).
    """
    _f.CAD_SetHoverStyle(r, g, b, width)


def CAD_SetSelectionLineWidth(width: float) -> None:
    """C: void CAD_SetSelectionLineWidth(float width)

    선택 표시 두께 (색은 노란색 고정 — CAD 관례).
    """
    _f.CAD_SetSelectionLineWidth(width)


def CAD_SetCollisionEnabled(enabled: bool) -> None:
    """C: void CAD_SetCollisionEnabled(bool enabled)

    벽 충돌 (Walk / 캐릭터 모드). 끄면 벽을 통과한다.
    ⚠️ 정적 지오메트리 대상의 캐릭터 충돌이지 물리엔진이 아니다 — 물체는 떨어지지 않는다.
    """
    _f.CAD_SetCollisionEnabled(enabled)


def CAD_GetCollisionEnabled() -> bool:
    """C: bool CAD_GetCollisionEnabled(void)

    벽 충돌 (Walk / 캐릭터 모드). 끄면 벽을 통과한다.
    ⚠️ 정적 지오메트리 대상의 캐릭터 충돌이지 물리엔진이 아니다 — 물체는 떨어지지 않는다.
    """
    return _f.CAD_GetCollisionEnabled()


def CAD_CaptureViewport(pathUtf8: str | None, clean: bool) -> bool:
    """C: bool CAD_CaptureViewport(const char* pathUtf8, bool clean)

    화면 캡처 → PNG(창 전체). clean = 그리드·뷰큐브 없이. 한 프레임 그려 파일이 생겼는지까지 확인하고 돌아온다
    (엔진 틱 안 — 플러그인 콜백 등 — 에서 불리면 요청만 남기고 다음 프레임에 찍는다, true = 요청됨). AI 가 결과를 눈으로 볼 때.
    """
    return _f.CAD_CaptureViewport(_n.text(pathUtf8), clean)


def CAD_OrbitCamera(ax: float, ay: float, az: float, angleDeg: float) -> None:
    """C: void CAD_OrbitCamera(float ax, float ay, float az, float angleDeg)

    카메라 — 지금 궤도 중심 둘레로 (ax,ay,az) 축 angleDeg 만큼 돌리기. 턴테이블 = (0,0,1).
    """
    _f.CAD_OrbitCamera(ax, ay, az, angleDeg)
