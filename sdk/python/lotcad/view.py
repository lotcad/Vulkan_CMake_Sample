# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — View 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_SetViewportLayout', 'CAD_GetViewportLayout', 'CAD_SetActiveViewport', 'CAD_GetActiveViewport', 'CAD_SetGridEnabled', 'CAD_SetDemoLighting', 'CAD_SetVisualStyle', 'CAD_SetSelectionStyle', 'CAD_GetSelectionStyle', 'CAD_SetHoverHighlight', 'CAD_GetHoverHighlight', 'CAD_GetHoveredObject', 'CAD_SetHoverStyle', 'CAD_SetSelectionLineWidth', 'CAD_SetCollisionEnabled', 'CAD_GetCollisionEnabled', 'CAD_GetStatusMessage', 'CAD_GetTransientMessage']

_f = _n.native

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
_n.bind("CAD_GetStatusMessage", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetTransientMessage", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])


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


def CAD_GetStatusMessage() -> str | None:
    """C: int CAD_GetStatusMessage(char* buf, int bufLen)

    명령 프롬프트(현재 대화형 도구 안내). buf 에 UTF-8 로 복사, 반환=문자열 길이(널 제외).
    호스트가 자기 상태바에 표시하려고 매 프레임 폴링. buf/bufLen 0 이면 길이만 반환.
    """
    _need = _f.CAD_GetStatusMessage(None, 0)   # 2회 호출 규약: 길이를 물으며 한 번 실행
    if _need < 0:
        return None
    _cap = _need + 1
    _buf = _c.create_string_buffer(_cap)
    if _f.CAD_GetStatusMessage(_buf, _cap) < 0:   # 같은 인자 → 다시 실행하지 않고 결과만
        return None
    return _n.decode(_buf.value)


def CAD_GetTransientMessage() -> str | None:
    """C: int CAD_GetTransientMessage(char* buf, int bufLen)

    일회성 안내 (몇 초 뒤 스스로 사라짐). 프롬프트와 **다른 값**이다 —
    프롬프트는 "지금 뭘 해야 하는지"(상시), 이쪽은 "방금 왜 안 됐는지"(일시).
    예: "각도: 선을 클릭하세요", "선: 커서를 방향으로 옮긴 뒤 거리를 입력하세요"
    없거나 만료됐으면 빈 문자열(길이 0). 데스크톱은 ImGui 상태바가 그리지만 모바일은
    표시할 곳이 없어 이게 유일한 경로다 — 안 띄우면 클릭이 씹힌 것처럼 보인다.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetTransientMessage(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)
