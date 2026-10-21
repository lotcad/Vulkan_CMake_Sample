# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Input 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_OnKeyDownVK', 'CAD_OnKeyUpVK', 'CAD_GizmoHitTest', 'CAD_SetGizmoTouchMode', 'CAD_SetSnapTouchMode', 'CAD_SetDimensionTextScreenFixed', 'CAD_GetDimensionTextScreenFixed', 'CAD_GetDimensionPointCount', 'CAD_GetPrompt', 'CAD_RequestStartBoxSketch', 'CAD_RequestStartLineSketch', 'CAD_RequestStartRectangleSketch', 'CAD_RequestStartCircleSketch', 'CAD_RequestStartPolygonSketch', 'CAD_RequestCyclePolygonSides']

_f = _n.native

_n.bind("CAD_OnKeyDownVK", None, [_c.c_int])
_n.bind("CAD_OnKeyUpVK", None, [_c.c_int])
_n.bind("CAD_GizmoHitTest", _c.c_int, [_c.c_double, _c.c_double])
_n.bind("CAD_SetGizmoTouchMode", None, [_c.c_bool])
_n.bind("CAD_SetSnapTouchMode", None, [_c.c_bool])
_n.bind("CAD_SetDimensionTextScreenFixed", None, [_c.c_bool])
_n.bind("CAD_GetDimensionTextScreenFixed", _c.c_bool, [])
_n.bind("CAD_GetDimensionPointCount", _c.c_int, [])
_n.bind("CAD_GetPrompt", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_RequestStartBoxSketch", None, [])
_n.bind("CAD_RequestStartLineSketch", None, [])
_n.bind("CAD_RequestStartRectangleSketch", None, [])
_n.bind("CAD_RequestStartCircleSketch", None, [])
_n.bind("CAD_RequestStartPolygonSketch", None, [])
_n.bind("CAD_RequestCyclePolygonSides", None, [])


def CAD_OnKeyDownVK(vkCode: int) -> None:
    """C: void CAD_OnKeyDownVK(int vkCode)
    Windows 전용 — 다른 OS 의 라이브러리엔 없어 부르면 NotImplementedError.
    """
    _f.CAD_OnKeyDownVK(vkCode)


def CAD_OnKeyUpVK(vkCode: int) -> None:
    """C: void CAD_OnKeyUpVK(int vkCode)
    Windows 전용 — 다른 OS 의 라이브러리엔 없어 부르면 NotImplementedError.
    """
    _f.CAD_OnKeyUpVK(vkCode)


def CAD_GizmoHitTest(x: float, y: float) -> int:
    """C: int CAD_GizmoHitTest(double x, double y)

    터치 입력 라우팅: (x,y) 에 Transform Gizmo 핸들이 있으면 1(true), 없으면 0.
    호출자(예: iOS)가 1손가락 드래그 시작 시 호출해 기즈모 조작(left) vs 궤도회전(right) 결정.
    """
    return _f.CAD_GizmoHitTest(x, y)


def CAD_SetGizmoTouchMode(enabled: bool) -> None:
    """C: void CAD_SetGizmoTouchMode(bool enabled)

    기즈모 핸들 hit 허용범위를 터치용으로 확대 (앱 시작 시 한 번 호출).
    """
    _f.CAD_SetGizmoTouchMode(enabled)


def CAD_SetSnapTouchMode(enabled: bool) -> None:
    """C: void CAD_SetSnapTouchMode(bool enabled)

    OSnap(끝점/중점/중심…) 허용범위를 터치용으로 확대 — 12px → 18px (가상 커서 기준).
    **선택 픽 반경도 같이 커진다** — 선·폴리선·치수(치수선/보조선/화살표/값 문자) 탭 10px → 30px.
    선택 탭은 손가락이 직접 짚으므로 3배 레티나 10pt 에 맞춘 값. 앱 시작 시 한 번 호출.
    """
    _f.CAD_SetSnapTouchMode(enabled)


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


def CAD_GetDimensionPointCount() -> int:
    """C: int CAD_GetDimensionPointCount(void)

    진행 중인 치수 도구의 점 개수. 비활성이면 -1.
    모바일 커서 UI 의 [선택] 버튼 문구/종료 판단에 쓴다 — 클라이언트가 클릭을 세면
    엔진이 클릭을 거부하는 경우와 어긋나므로 반드시 엔진 값을 본다.
    """
    return _f.CAD_GetDimensionPointCount()


def CAD_GetPrompt() -> str | None:
    """C: int CAD_GetPrompt(char* buf, int bufLen)

    진행 중인 도구의 안내 문구("첫 번째 점을 지정" 등). 도구가 없으면 빈 문자열.
    모바일 커서 UI 가 **도구 종류와 무관하게** 활성 여부/안내를 알기 위해 매 틱 폴링한다.
    반환: 복사한 길이(널 제외). buf 가 작으면 잘라서 복사한다.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetPrompt(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_RequestStartBoxSketch() -> None:
    """C: void CAD_RequestStartBoxSketch(void)
    """
    _f.CAD_RequestStartBoxSketch()


def CAD_RequestStartLineSketch() -> None:
    """C: void CAD_RequestStartLineSketch(void)
    """
    _f.CAD_RequestStartLineSketch()


def CAD_RequestStartRectangleSketch() -> None:
    """C: void CAD_RequestStartRectangleSketch(void)
    """
    _f.CAD_RequestStartRectangleSketch()


def CAD_RequestStartCircleSketch() -> None:
    """C: void CAD_RequestStartCircleSketch(void)
    """
    _f.CAD_RequestStartCircleSketch()


def CAD_RequestStartPolygonSketch() -> None:
    """C: void CAD_RequestStartPolygonSketch(void)
    """
    _f.CAD_RequestStartPolygonSketch()


def CAD_RequestCyclePolygonSides() -> None:
    """C: void CAD_RequestCyclePolygonSides(void)
    """
    _f.CAD_RequestCyclePolygonSides()
