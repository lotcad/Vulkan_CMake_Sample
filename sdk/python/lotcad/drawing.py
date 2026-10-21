# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Drawing 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_CreateDrawingViews', 'CAD_CreateSectionView', 'CAD_CreateDetailView', 'CAD_MoveDrawingView', 'CAD_ClearDrawingViews', 'CAD_GetDrawingViewsJson', 'CAD_CreateExternalEffect', 'CAD_GetSelectedCount', 'CAD_GetSelectedObjectId']

_f = _n.native

_n.bind("CAD_CreateDrawingViews", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_float])
_n.bind("CAD_CreateSectionView", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateDetailView", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_MoveDrawingView", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float])
_n.bind("CAD_ClearDrawingViews", None, [])
_n.bind("CAD_GetDrawingViewsJson", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_CreateExternalEffect", _c.c_uint32, [_c.c_char_p, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_GetSelectedCount", _c.c_uint32, [])
_n.bind("CAD_GetSelectedObjectId", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_uint32)])


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
    """
    _f.CAD_ClearDrawingViews()


def CAD_GetDrawingViewsJson() -> str | None:
    """C: int CAD_GetDrawingViewsJson(char* out, int cap)

    뷰 목록 JSON — [{"id","name","kind":"base|section|detail","dir","up","origin","scale","hidden","dims","sources",
    "parent","label"(단면·상세),"bounds":{"min":[x,y],"max":[x,y]}}] — bounds = 뷰가 차지하는 자리(선 + 모델 치수 + 이름). 2회 호출 규약.
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


def CAD_CreateExternalEffect(path: str | None, x: float, y: float, z: float, unitsPerMeter: float) -> int:
    """C: uint32_t CAD_CreateExternalEffect(const char* path,float x,float y,float z,float unitsPerMeter)

    Load an Effekseer .efkefc/.efk with referenced resources. Inserted stopped.
    CAD_SetParticlePlayback also controls these objects. Files embed in .lot.
    """
    return _f.CAD_CreateExternalEffect(_n.text(path), x, y, z, unitsPerMeter)


def CAD_GetSelectedCount() -> int:
    """C: uint32_t CAD_GetSelectedCount(void)
    """
    return _f.CAD_GetSelectedCount()


def CAD_GetSelectedObjectId(index: int) -> int | None:
    """C: bool CAD_GetSelectedObjectId(uint32_t index, uint32_t* id)
    """
    id = _c.c_uint32()
    if not _f.CAD_GetSelectedObjectId(index, _c.byref(id)):
        return None
    return id.value
