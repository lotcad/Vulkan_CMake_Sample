# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Callbacks 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_SetOnSelectionChanged', 'CAD_SetOnSelectionChanged_cb', 'CAD_SetOnObjectCreated', 'CAD_SetOnObjectCreated_cb', 'CAD_SetOnObjectDeleted', 'CAD_SetOnObjectDeleted_cb', 'CAD_SetOnDocumentDirty', 'CAD_SetOnDocumentDirty_cb', 'CAD_SetOnPrompt', 'CAD_SetOnPrompt_cb', 'CAD_RequestStartExtrude', 'CAD_RequestStartArcSketch', 'CAD_RequestCycleArcMode', 'CAD_RequestStartPolylineSketch', 'CAD_RequestOpenFileDialog', 'CAD_RequestZoomExtents', 'CAD_RequestSelectAll', 'CAD_RequestDeleteSelected', 'CAD_RequestClearAll', 'CAD_RequestAddCube', 'CAD_RequestStartLightPlacement', 'CAD_RequestFocusSelected', 'CAD_RequestToggleProjection', 'CAD_RequestToggleDemoLighting', 'CAD_RequestCycleMaterial', 'CAD_RequestRemoveMaterial', 'CAD_RequestAdjustTextureScale', 'CAD_RequestAdjustLineWidth', 'CAD_RequestSetView', 'CAD_RequestSetProjection', 'CAD_RequestSetViewDirection', 'CAD_RequestSetViewPivot', 'CAD_RequestClearViewPivot', 'CAD_GetViewPivot']

_f = _n.native

CAD_SetOnSelectionChanged_cb = _c.CFUNCTYPE(None)
CAD_SetOnObjectCreated_cb = _c.CFUNCTYPE(None, _c.c_uint32)
CAD_SetOnObjectDeleted_cb = _c.CFUNCTYPE(None, _c.c_uint32)
CAD_SetOnDocumentDirty_cb = _c.CFUNCTYPE(None, _c.c_bool)
CAD_SetOnPrompt_cb = _c.CFUNCTYPE(None, _c.c_char_p)

_n.bind("CAD_SetOnSelectionChanged", None, [CAD_SetOnSelectionChanged_cb])
_n.bind("CAD_SetOnObjectCreated", None, [CAD_SetOnObjectCreated_cb])
_n.bind("CAD_SetOnObjectDeleted", None, [CAD_SetOnObjectDeleted_cb])
_n.bind("CAD_SetOnDocumentDirty", None, [CAD_SetOnDocumentDirty_cb])
_n.bind("CAD_SetOnPrompt", None, [CAD_SetOnPrompt_cb])
_n.bind("CAD_RequestStartExtrude", None, [])
_n.bind("CAD_RequestStartArcSketch", None, [])
_n.bind("CAD_RequestCycleArcMode", None, [])
_n.bind("CAD_RequestStartPolylineSketch", None, [])
_n.bind("CAD_RequestOpenFileDialog", None, [])
_n.bind("CAD_RequestZoomExtents", None, [])
_n.bind("CAD_RequestSelectAll", None, [])
_n.bind("CAD_RequestDeleteSelected", None, [])
_n.bind("CAD_RequestClearAll", None, [])
_n.bind("CAD_RequestAddCube", None, [])
_n.bind("CAD_RequestStartLightPlacement", None, [])
_n.bind("CAD_RequestFocusSelected", None, [])
_n.bind("CAD_RequestToggleProjection", None, [])
_n.bind("CAD_RequestToggleDemoLighting", None, [])
_n.bind("CAD_RequestCycleMaterial", None, [])
_n.bind("CAD_RequestRemoveMaterial", None, [])
_n.bind("CAD_RequestAdjustTextureScale", None, [_c.c_float])
_n.bind("CAD_RequestAdjustLineWidth", None, [_c.c_float])
_n.bind("CAD_RequestSetView", None, [_c.c_int])
_n.bind("CAD_RequestSetProjection", None, [_c.c_bool])
_n.bind("CAD_RequestSetViewDirection", None, [_c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_RequestSetViewPivot", None, [_c.c_float, _c.c_float, _c.c_float, _c.c_int])
_n.bind("CAD_RequestClearViewPivot", None, [])
_n.bind("CAD_GetViewPivot", _c.c_bool, [_c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_int)])


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


def CAD_RequestStartExtrude() -> None:
    """C: void CAD_RequestStartExtrude(void)
    """
    _f.CAD_RequestStartExtrude()


def CAD_RequestStartArcSketch() -> None:
    """C: void CAD_RequestStartArcSketch(void)
    """
    _f.CAD_RequestStartArcSketch()


def CAD_RequestCycleArcMode() -> None:
    """C: void CAD_RequestCycleArcMode(void)
    """
    _f.CAD_RequestCycleArcMode()


def CAD_RequestStartPolylineSketch() -> None:
    """C: void CAD_RequestStartPolylineSketch(void)
    """
    _f.CAD_RequestStartPolylineSketch()


def CAD_RequestOpenFileDialog() -> None:
    """C: void CAD_RequestOpenFileDialog(void)
    """
    _f.CAD_RequestOpenFileDialog()


def CAD_RequestZoomExtents() -> None:
    """C: void CAD_RequestZoomExtents(void)
    """
    _f.CAD_RequestZoomExtents()


def CAD_RequestSelectAll() -> None:
    """C: void CAD_RequestSelectAll(void)
    """
    _f.CAD_RequestSelectAll()


def CAD_RequestDeleteSelected() -> None:
    """C: void CAD_RequestDeleteSelected(void)
    """
    _f.CAD_RequestDeleteSelected()


def CAD_RequestClearAll() -> None:
    """C: void CAD_RequestClearAll(void)
    """
    _f.CAD_RequestClearAll()


def CAD_RequestAddCube() -> None:
    """C: void CAD_RequestAddCube(void)
    """
    _f.CAD_RequestAddCube()


def CAD_RequestStartLightPlacement() -> None:
    """C: void CAD_RequestStartLightPlacement(void)
    """
    _f.CAD_RequestStartLightPlacement()


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


def CAD_RequestCycleMaterial() -> None:
    """C: void CAD_RequestCycleMaterial(void)
    """
    _f.CAD_RequestCycleMaterial()


def CAD_RequestRemoveMaterial() -> None:
    """C: void CAD_RequestRemoveMaterial(void)
    """
    _f.CAD_RequestRemoveMaterial()


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
