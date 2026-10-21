# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Linetypes 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_LINETYPE_BYLAYER', 'CAD_MAX_BREP_PROFILE_POINTS', 'CAD_CreateLinetype', 'CAD_GetLinetypeIds', 'CAD_GetLinetypeName', 'CAD_GetLinetypePattern', 'CAD_SetObjectLinetype', 'CAD_GetObjectLinetype', 'CAD_SetObjectLinetypeScale', 'CAD_GetObjectLinetypeScale', 'CAD_SetSelectedLinetype', 'CAD_SetLayerLinetype', 'CAD_GetLayerLinetype', 'CAD_SetLinetypeScale', 'CAD_GetLinetypeScale', 'CAD_SetObjectLayer', 'CAD_GetObjectLayer', 'CAD_AssignSelectedToLayer', 'CAD_GetObjectName', 'CAD_FindObjectByName', 'CAD_GetColor', 'CAD_SetColor', 'CAD_GetBoundsWorld', 'CAD_GetCenterWorld', 'CAD_CutExtrudeFromSketch', 'CAD_BossExtrudeFromSketch']

_f = _n.native

CAD_LINETYPE_BYLAYER = 0xFFFFFFFF
CAD_MAX_BREP_PROFILE_POINTS = 2048

_n.bind("CAD_CreateLinetype", _c.c_uint32, [_c.c_char_p, _c.POINTER(_c.c_float), _c.c_int, _c.c_char_p])
_n.bind("CAD_GetLinetypeIds", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_GetLinetypeName", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetLinetypePattern", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_float), _c.c_int])
_n.bind("CAD_SetObjectLinetype", _c.c_bool, [_c.c_uint32, _c.c_uint32])
_n.bind("CAD_GetObjectLinetype", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetObjectLinetypeScale", _c.c_bool, [_c.c_uint32, _c.c_float])
_n.bind("CAD_GetObjectLinetypeScale", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float)])
_n.bind("CAD_SetSelectedLinetype", _c.c_uint32, [_c.c_uint32])
_n.bind("CAD_SetLayerLinetype", _c.c_bool, [_c.c_uint32, _c.c_uint32])
_n.bind("CAD_GetLayerLinetype", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetLinetypeScale", _c.c_bool, [_c.c_float])
_n.bind("CAD_GetLinetypeScale", _c.c_float, [])
_n.bind("CAD_SetObjectLayer", _c.c_bool, [_c.c_uint32, _c.c_uint32])
_n.bind("CAD_GetObjectLayer", _c.c_int, [_c.c_uint32])
_n.bind("CAD_AssignSelectedToLayer", _c.c_uint32, [_c.c_uint32])
_n.bind("CAD_GetObjectName", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_FindObjectByName", _c.c_uint32, [_c.c_char_p])
_n.bind("CAD_GetColor", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float)])
_n.bind("CAD_SetColor", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_GetBoundsWorld", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float)])
_n.bind("CAD_GetCenterWorld", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float)])
_n.bind("CAD_CutExtrudeFromSketch", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.c_float, _c.c_bool])
_n.bind("CAD_BossExtrudeFromSketch", _c.c_bool, [_c.c_uint32, _c.c_uint32, _c.c_float])


def CAD_CreateLinetype(name: str | None, pattern: Sequence | None, count: int, description: str | None) -> int:
    """C: uint32_t CAD_CreateLinetype(const char* name, const float* pattern, int count, const char* description)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    _a_pattern = _n.array(_c.c_float, pattern)
    return _f.CAD_CreateLinetype(_n.text(name), _a_pattern, count, _n.text(description))


def CAD_GetLinetypeIds(out: Any, capacity: int) -> int:
    """C: uint32_t CAD_GetLinetypeIds(uint32_t* out, uint32_t capacity)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    필요한 개수, 0(Continuous) 포함
    """
    return _f.CAD_GetLinetypeIds(out, capacity)


def CAD_GetLinetypeName(id: int) -> str | None:
    """C: int CAD_GetLinetypeName(uint32_t id, char* out, int capacity)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    이름 길이, 없으면 -1
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetLinetypeName(id, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetLinetypePattern(id: int, out: Any, capacity: int) -> int:
    """C: int CAD_GetLinetypePattern(uint32_t id, float* out, int capacity)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    요소 수, 없으면 -1
    """
    return _f.CAD_GetLinetypePattern(id, out, capacity)


def CAD_SetObjectLinetype(objectId: int, linetypeId: int) -> bool:
    """C: bool CAD_SetObjectLinetype(uint32_t objectId, uint32_t linetypeId)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    CAD_LINETYPE_BYLAYER 허용
    """
    return _f.CAD_SetObjectLinetype(objectId, linetypeId)


def CAD_GetObjectLinetype(objectId: int) -> int | None:
    """C: bool CAD_GetObjectLinetype(uint32_t objectId, uint32_t* out)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    out = _c.c_uint32()
    if not _f.CAD_GetObjectLinetype(objectId, _c.byref(out)):
        return None
    return out.value


def CAD_SetObjectLinetypeScale(objectId: int, scale: float) -> bool:
    """C: bool CAD_SetObjectLinetypeScale(uint32_t objectId, float scale)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    객체별 축척(CELTSCALE)
    """
    return _f.CAD_SetObjectLinetypeScale(objectId, scale)


def CAD_GetObjectLinetypeScale(objectId: int) -> float | None:
    """C: bool CAD_GetObjectLinetypeScale(uint32_t objectId, float* out)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    out = _c.c_float()
    if not _f.CAD_GetObjectLinetypeScale(objectId, _c.byref(out)):
        return None
    return out.value


def CAD_SetSelectedLinetype(linetypeId: int) -> int:
    """C: uint32_t CAD_SetSelectedLinetype(uint32_t linetypeId)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    바뀐 객체 수
    """
    return _f.CAD_SetSelectedLinetype(linetypeId)


def CAD_SetLayerLinetype(layerId: int, linetypeId: int) -> bool:
    """C: bool CAD_SetLayerLinetype(uint32_t layerId, uint32_t linetypeId)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    도면층 0 은 실선 고정
    """
    return _f.CAD_SetLayerLinetype(layerId, linetypeId)


def CAD_GetLayerLinetype(layerId: int) -> int | None:
    """C: bool CAD_GetLayerLinetype(uint32_t layerId, uint32_t* out)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    out = _c.c_uint32()
    if not _f.CAD_GetLayerLinetype(layerId, _c.byref(out)):
        return None
    return out.value


def CAD_SetLinetypeScale(scale: float) -> bool:
    """C: bool CAD_SetLinetypeScale(float scale)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    전역 LTSCALE
    """
    return _f.CAD_SetLinetypeScale(scale)


def CAD_GetLinetypeScale() -> float:
    """C: float CAD_GetLinetypeScale(void)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    return _f.CAD_GetLinetypeScale()


def CAD_SetObjectLayer(objectId: int, layerId: int) -> bool:
    """C: bool CAD_SetObjectLayer(uint32_t objectId, uint32_t layerId)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    return _f.CAD_SetObjectLayer(objectId, layerId)


def CAD_GetObjectLayer(objectId: int) -> int:
    """C: int CAD_GetObjectLayer(uint32_t objectId)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    -1 for missing objects
    """
    return _f.CAD_GetObjectLayer(objectId)


def CAD_AssignSelectedToLayer(layerId: int) -> int:
    """C: uint32_t CAD_AssignSelectedToLayer(uint32_t layerId)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    return _f.CAD_AssignSelectedToLayer(layerId)


def CAD_GetObjectName(id: int) -> str | None:
    """C: int CAD_GetObjectName(uint32_t id, char* outUtf8, int cap)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    길이 반환, -1=실패
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetObjectName(id, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_FindObjectByName(utf8: str | None) -> int:
    """C: uint32_t CAD_FindObjectByName(const char* utf8)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    0 = 없음
    """
    return _f.CAD_FindObjectByName(_n.text(utf8))


def CAD_GetColor(id: int) -> tuple[float, float, float] | None:
    """C: bool CAD_GetColor(uint32_t id, float* r, float* g, float* b)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    r = _c.c_float()
    g = _c.c_float()
    b = _c.c_float()
    if not _f.CAD_GetColor(id, _c.byref(r), _c.byref(g), _c.byref(b)):
        return None
    return (r.value, g.value, b.value)


def CAD_SetColor(id: int, r: float, g: float, b: float) -> bool:
    """C: bool CAD_SetColor(uint32_t id, float r, float g, float b)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    return _f.CAD_SetColor(id, r, g, b)


def CAD_GetBoundsWorld(id: int) -> tuple[float, float, float, float, float, float] | None:
    """C: bool CAD_GetBoundsWorld(uint32_t id, float* minX, float* minY, float* minZ, float* maxX, float* maxY, float* maxZ)

    월드 AABB (min/max). GetCenter = 0.5*(min+max). 대형 임포트 메시는 AABB 폴백으로 유효.
    """
    minX = _c.c_float()
    minY = _c.c_float()
    minZ = _c.c_float()
    maxX = _c.c_float()
    maxY = _c.c_float()
    maxZ = _c.c_float()
    if not _f.CAD_GetBoundsWorld(id, _c.byref(minX), _c.byref(minY), _c.byref(minZ), _c.byref(maxX), _c.byref(maxY), _c.byref(maxZ)):
        return None
    return (minX.value, minY.value, minZ.value, maxX.value, maxY.value, maxZ.value)


def CAD_GetCenterWorld(id: int) -> tuple[float, float, float] | None:
    """C: bool CAD_GetCenterWorld(uint32_t id, float* x, float* y, float* z)

    월드 AABB (min/max). GetCenter = 0.5*(min+max). 대형 임포트 메시는 AABB 폴백으로 유효.
    """
    x = _c.c_float()
    y = _c.c_float()
    z = _c.c_float()
    if not _f.CAD_GetCenterWorld(id, _c.byref(x), _c.byref(y), _c.byref(z)):
        return None
    return (x.value, y.value, z.value)


def CAD_CutExtrudeFromSketch(id: int, sketchId: int, depth: float, throughAll: bool) -> bool:
    """C: bool CAD_CutExtrudeFromSketch(uint32_t id, uint32_t sketchId, float depth, bool throughAll)

    기존 닫힌 2D 스케치를 프로파일로 사용한다. 스케치의 월드 변환을 대상 솔리드의
    로컬 좌표로 자동 변환하므로 화면에서 그린 사각형·원·폴리선을 바로 사용할 수 있다.
    """
    return _f.CAD_CutExtrudeFromSketch(id, sketchId, depth, throughAll)


def CAD_BossExtrudeFromSketch(id: int, sketchId: int, height: float) -> bool:
    """C: bool CAD_BossExtrudeFromSketch(uint32_t id, uint32_t sketchId, float height)

    닫힌 스케치로 — 스케치가 가까운 캡(위/아래) 쪽으로 height(양수) 만큼. 스케치가 바뀌면 다시 만든다.
    """
    return _f.CAD_BossExtrudeFromSketch(id, sketchId, height)
