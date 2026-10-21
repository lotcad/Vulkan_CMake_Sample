# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Objects 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_GetObjectJson', 'CAD_GetObjectProperty', 'CAD_SetObjectProperty', 'CAD_GetLastError', 'CAD_QueryObjects', 'CAD_SelectByQuery', 'CAD_GetSceneJson', 'CAD_GetSelectionContext', 'CAD_GetPolylinePoints', 'CAD_SetPolylinePoints', 'CAD_GetObjectIds', 'CAD_GetObjectKind', 'CAD_ObjectExists', 'CAD_SetObjectName', 'CAD_SetObjectVisible', 'CAD_IsObjectVisible', 'CAD_CreateLayer', 'CAD_SetLayerColor', 'CAD_GetLayerColor', 'CAD_SetObjectColorByLayer', 'CAD_GetObjectColorByLayer', 'CAD_SetSelectedColorByLayer', 'CAD_GetObjectEffectiveColor', 'CAD_SetObjectOpacity', 'CAD_GetObjectOpacity', 'CAD_SetLayerOpacity', 'CAD_GetLayerOpacity', 'CAD_SetSelectedOpacity', 'CAD_GetLayerIds', 'CAD_GetLayerName', 'CAD_RenameLayer', 'CAD_SetLayerVisible', 'CAD_IsLayerVisible', 'CAD_SetLayerLocked', 'CAD_IsLayerLocked']

_f = _n.native

_n.bind("CAD_GetObjectJson", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetObjectProperty", _c.c_int, [_c.c_uint32, _c.c_char_p, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_SetObjectProperty", _c.c_bool, [_c.c_uint32, _c.c_char_p, _c.c_char_p])
_n.bind("CAD_GetLastError", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_QueryObjects", _c.c_uint32, [_c.c_char_p, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_SelectByQuery", _c.c_uint32, [_c.c_char_p, _c.c_bool])
_n.bind("CAD_GetSceneJson", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int, _c.c_int])
_n.bind("CAD_GetSelectionContext", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetPolylinePoints", _c.c_uint32, [_c.c_uint32, _c.POINTER(_c.c_float), _c.c_uint32, _c.POINTER(_c.c_bool)])
_n.bind("CAD_SetPolylinePoints", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.c_uint32, _c.c_bool])
_n.bind("CAD_GetObjectIds", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_GetObjectKind", _c.c_int, [_c.c_uint32])
_n.bind("CAD_ObjectExists", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_SetObjectName", _c.c_bool, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_SetObjectVisible", _c.c_bool, [_c.c_uint32, _c.c_bool])
_n.bind("CAD_IsObjectVisible", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_CreateLayer", _c.c_uint32, [_c.c_char_p])
_n.bind("CAD_SetLayerColor", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_GetLayerColor", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float)])
_n.bind("CAD_SetObjectColorByLayer", _c.c_bool, [_c.c_uint32, _c.c_bool])
_n.bind("CAD_GetObjectColorByLayer", _c.c_int, [_c.c_uint32])
_n.bind("CAD_SetSelectedColorByLayer", _c.c_uint32, [_c.c_bool])
_n.bind("CAD_GetObjectEffectiveColor", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float)])
_n.bind("CAD_SetObjectOpacity", _c.c_bool, [_c.c_uint32, _c.c_float])
_n.bind("CAD_GetObjectOpacity", _c.c_float, [_c.c_uint32])
_n.bind("CAD_SetLayerOpacity", _c.c_bool, [_c.c_uint32, _c.c_float])
_n.bind("CAD_GetLayerOpacity", _c.c_float, [_c.c_uint32])
_n.bind("CAD_SetSelectedOpacity", _c.c_uint32, [_c.c_float])
_n.bind("CAD_GetLayerIds", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_GetLayerName", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_RenameLayer", _c.c_bool, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_SetLayerVisible", _c.c_bool, [_c.c_uint32, _c.c_bool])
_n.bind("CAD_IsLayerVisible", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_SetLayerLocked", _c.c_bool, [_c.c_uint32, _c.c_bool])
_n.bind("CAD_IsLayerLocked", _c.c_bool, [_c.c_uint32])


def CAD_GetObjectJson(id: int) -> str | None:
    """C: int CAD_GetObjectJson(uint32_t id, char* outUtf8, int cap)

    객체 하나를 JSON 한 줄로 — 종류·이름·레이어·색·변환·경계 + 종류별 기하.
    (line: start/end/length, polyline: points/closed, circle: center/radius/normal, arc: +startDeg/endDeg,
     text: text/height/font, dimension: dimType/p1/p2/value, mesh: vertices/triangles/light)
    단위 mm, 좌표 월드. 키 이름은 lot_object_json.h 한 곳에서 정하며 AI 선택 문맥·씬 요약과 같다.
    반환 = 길이(널 제외), 없는 id/실패 = -1. outUtf8=NULL 이면 길이만(2회 호출 규약).
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetObjectJson(id, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetObjectProperty(id: int, key: str | None) -> str | None:
    """C: int CAD_GetObjectProperty(uint32_t id, const char* key, char* outUtf8, int cap)

    이름으로 속성 하나 읽기·쓰기 — 키는 CAD_GetObjectJson 의 키와 같다.
      공통    name, color, colorByLayer, visible, layer(이름|id), linetype(이름|id|"bylayer"), linetypeScale,
              position, rotation[x,y,z,w], scale
      line    start, end          polyline  points, closed        circle  center, radius
      arc     center, radius, startDeg, endDeg                     text    text, height, font
      dimension p1, p2, p3, dimLinePoint, precision                mesh    intensity(조명)
    Get: 값의 JSON 텍스트(예: 50.0 / [1,2,3] / "이름"), 반환=길이, 없으면 -1.
    Set: valueJson 은 JSON(따옴표 없는 글자는 문자열로 받음). 좌표·길이는 월드 mm. 딸린 모델을 다시 만들고
         undo 한 단계로 남긴다. 실패(없는 키·형식 오류·잠긴 도면층) 면 false — 이유는 CAD_GetStatusMessage 가 아니라
         CAD_GetLastError 로.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetObjectProperty(id, _n.text(key), _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_SetObjectProperty(id: int, key: str | None, valueJson: str | None) -> bool:
    """C: bool CAD_SetObjectProperty(uint32_t id, const char* key, const char* valueJson)
    """
    return _f.CAD_SetObjectProperty(id, _n.text(key), _n.text(valueJson))


def CAD_GetLastError() -> str | None:
    """C: int CAD_GetLastError(char* outUtf8, int cap)

    직전 CAD_SetObjectProperty 실패 이유(UTF-8). 성공 뒤엔 빈 문자열.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetLastError(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_QueryObjects(filterJson: str | None, outIds: Any, cap: int) -> int:
    """C: uint32_t CAD_QueryObjects(const char* filterJson, uint32_t* outIds, uint32_t cap)

    질의 — 필터 JSON 으로 객체 id 목록. 키는 전부 선택(AND):
      {"kind":"circle"|["circle","arc"], "layer":"이름"|id, "name":"기둥*"(글롭), "selected":true, "visible":true,
       "within":{"min":[x,y,z],"max":[x,y,z]}(상자 안), "intersects":{min,max}(겹침), "near":{"point":[x,y,z],"radius":r},
       "pick":"largest"|"smallest"(통과한 것 중 하나), "limit":N}
    반환 = 전체 개수(outIds=NULL/cap=0 이면 개수만 — 2회 호출 규약). 틀린 필터면 0 + CAD_GetLastError.
    """
    return _f.CAD_QueryObjects(_n.text(filterJson), outIds, cap)


def CAD_SelectByQuery(filterJson: str | None, additive: bool) -> int:
    """C: uint32_t CAD_SelectByQuery(const char* filterJson, bool additive)

    질의 결과를 선택으로 — 같은 필터 문법. additive=false 면 기존 선택을 비운다. 반환=고른 수, 틀린 필터면 0 + CAD_GetLastError.
    AI 의 edit_selected op="select" 와 같은 통로.
    """
    return _f.CAD_SelectByQuery(_n.text(filterJson), additive)


def CAD_GetSceneJson(maxObjects: int) -> str | None:
    """C: int CAD_GetSceneJson(char* outUtf8, int cap, int maxObjects)

    씬 요약 JSON — {"count","selected","units":"mm","bounds","kinds":{종류:수},"layers":[…],"objects":[요약…],"more"}.
    objects 는 앞에서 maxObjects 개(0 이면 50). 객체 상세는 CAD_GetObjectJson. 반환=길이, 실패 -1.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetSceneJson(_buf, _cap, maxObjects)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetSelectionContext() -> str | None:
    """C: int CAD_GetSelectionContext(char* outUtf8, int cap)

    선택 문맥 JSON — 사람이 화면에서 고른 것. AI 요청마다 자동으로 붙는 것과 같은 문자열.
    {"mode":"object|face|edge","view":"top|…","count":N,"objects":[CAD_GetObjectJson 과 같은 객체…],"more":n,
     "face":{"id","normal","center","area","triangles"},"edge":{"id","a","b","length"}}  반환=길이, 실패 -1.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetSelectionContext(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetPolylinePoints(id: int, outXyz: Any, cap: int) -> tuple[int, bool]:
    """C: uint32_t CAD_GetPolylinePoints(uint32_t id, float* outXyz, uint32_t cap, bool* outClosed)

    닫기·열기·반전·정점 삽입/삭제는 전부 "정점 목록을 바꾸는 일" 이라, 하위 명령마다
    함수를 늘리는 대신 목록을 통째로 읽고 쓰게 한다. 호스트가 받아서 고쳐 되돌려주면 된다.

    uint32_t n = CAD_GetPolylinePoints(id, NULL, 0, NULL);   // 개수 질의
    float* buf = malloc(n * 3 * sizeof(float));
    bool closed = false;
    CAD_GetPolylinePoints(id, buf, n, &closed);
    ... 고친 뒤 ...
    CAD_SetPolylinePoints(id, buf, n, closed);               // undo 1스텝으로 적재

    xyz 는 3 × count 개 float. 좌표는 객체 로컬 (그립/스케치와 같은 공간).
    Set 은 정점이 2개 미만이면 실패. Polyline 이 아닌 객체는 0 / false.
    """
    outClosed = _c.c_bool()
    _r = _f.CAD_GetPolylinePoints(id, outXyz, cap, _c.byref(outClosed))
    return (_r, outClosed.value)


def CAD_SetPolylinePoints(id: int, xyz: Sequence | None, count: int, closed: bool) -> bool:
    """C: bool CAD_SetPolylinePoints(uint32_t id, const float* xyz, uint32_t count, bool closed)
    """
    _a_xyz = _n.array(_c.c_float, xyz)
    return _f.CAD_SetPolylinePoints(id, _a_xyz, count, closed)


def CAD_GetObjectIds(outIds: Any, cap: int) -> int:
    """C: uint32_t CAD_GetObjectIds(uint32_t* outIds, uint32_t cap)

    전체 객체 ID 열거 — outIds 에 최대 cap 개 채우고 총 개수 반환. cap=0/outIds=NULL → 개수만 질의.
    (2단계: 먼저 개수 질의 → 버퍼 할당 → 다시 호출)
    """
    return _f.CAD_GetObjectIds(outIds, cap)


def CAD_GetObjectKind(id: int) -> int:
    """C: int CAD_GetObjectKind(uint32_t id)

    종류: 0=Mesh 1=Line 2=Polyline 3=Circle 4=Arc 5=Text 6=Dimension
    7=PointCloud 8=ParticleEmitter, 없으면 -1.
    """
    return _f.CAD_GetObjectKind(id)


def CAD_ObjectExists(id: int) -> bool:
    """C: bool CAD_ObjectExists(uint32_t id)
    """
    return _f.CAD_ObjectExists(id)


def CAD_SetObjectName(id: int, utf8: str | None) -> bool:
    """C: bool CAD_SetObjectName(uint32_t id, const char* utf8)

    이름 — 씬 안에서 **유일**해야 한다. 중복이면 false (이름은 사람과 외부 API 가
    부품을 가리키는 유일한 수단이라, 겹치면 어느 쪽인지 알 수 없다). 빈 이름은 허용.
    """
    return _f.CAD_SetObjectName(id, _n.text(utf8))


def CAD_SetObjectVisible(id: int, visible: bool) -> bool:
    """C: bool CAD_SetObjectVisible(uint32_t id, bool visible)

    Viewport visibility; hidden objects remain in the document but cannot be picked/snapped.
    """
    return _f.CAD_SetObjectVisible(id, visible)


def CAD_IsObjectVisible(id: int) -> bool:
    """C: bool CAD_IsObjectVisible(uint32_t id)

    false for missing IDs
    """
    return _f.CAD_IsObjectVisible(id)


def CAD_CreateLayer(name: str | None) -> int:
    """C: uint32_t CAD_CreateLayer(const char* name)

    Document layers. 0 is the always-visible, unlocked default layer.
    """
    return _f.CAD_CreateLayer(_n.text(name))


def CAD_SetLayerColor(id: int, r: float, g: float, b: float) -> bool:
    """C: bool CAD_SetLayerColor(uint32_t id,float r,float g,float b)

    RGB in [0,1]. Layer 0 has fixed white ByLayer color.
    """
    return _f.CAD_SetLayerColor(id, r, g, b)


def CAD_GetLayerColor(id: int) -> tuple[float, float, float] | None:
    """C: bool CAD_GetLayerColor(uint32_t id,float* r,float* g,float* b)
    """
    r = _c.c_float()
    g = _c.c_float()
    b = _c.c_float()
    if not _f.CAD_GetLayerColor(id, _c.byref(r), _c.byref(g), _c.byref(b)):
        return None
    return (r.value, g.value, b.value)


def CAD_SetObjectColorByLayer(id: int, enabled: bool) -> bool:
    """C: bool CAD_SetObjectColorByLayer(uint32_t id,bool enabled)
    """
    return _f.CAD_SetObjectColorByLayer(id, enabled)


def CAD_GetObjectColorByLayer(id: int) -> int:
    """C: int CAD_GetObjectColorByLayer(uint32_t id)

    0=individual, 1=ByLayer, -1=missing
    """
    return _f.CAD_GetObjectColorByLayer(id)


def CAD_SetSelectedColorByLayer(enabled: bool) -> int:
    """C: uint32_t CAD_SetSelectedColorByLayer(bool enabled)
    """
    return _f.CAD_SetSelectedColorByLayer(enabled)


def CAD_GetObjectEffectiveColor(id: int) -> tuple[float, float, float] | None:
    """C: bool CAD_GetObjectEffectiveColor(uint32_t id,float* r,float* g,float* b)
    """
    r = _c.c_float()
    g = _c.c_float()
    b = _c.c_float()
    if not _f.CAD_GetObjectEffectiveColor(id, _c.byref(r), _c.byref(g), _c.byref(b)):
        return None
    return (r.value, g.value, b.value)


def CAD_SetObjectOpacity(id: int, opacity: float) -> bool:
    """C: bool CAD_SetObjectOpacity(uint32_t id, float opacity)

    불투명도 0..1 (1 = 불투명). 객체 것 × 도면층 것이 화면에 쓰인다 — 메시(채움)에만, 선·문자는 그대로.
       객체 것은 되돌리기 1단계. 이름 기반 속성 "opacity" 와 같은 값. Get 은 없으면 -1.
    """
    return _f.CAD_SetObjectOpacity(id, opacity)


def CAD_GetObjectOpacity(id: int) -> float:
    """C: float CAD_GetObjectOpacity(uint32_t id)
    """
    return _f.CAD_GetObjectOpacity(id)


def CAD_SetLayerOpacity(id: int, opacity: float) -> bool:
    """C: bool CAD_SetLayerOpacity(uint32_t id, float opacity)
    """
    return _f.CAD_SetLayerOpacity(id, opacity)


def CAD_GetLayerOpacity(id: int) -> float:
    """C: float CAD_GetLayerOpacity(uint32_t id)
    """
    return _f.CAD_GetLayerOpacity(id)


def CAD_SetSelectedOpacity(opacity: float) -> int:
    """C: uint32_t CAD_SetSelectedOpacity(float opacity)
    """
    return _f.CAD_SetSelectedOpacity(opacity)


def CAD_GetLayerIds(out: Any, capacity: int) -> int:
    """C: uint32_t CAD_GetLayerIds(uint32_t* out, uint32_t capacity)

    CAD_API uint32_t CAD_SetSelectedOpacity(float opacity);   /* 선택 전부, 되돌리기 1단계 → 바뀐 수
    required count, includes 0
    """
    return _f.CAD_GetLayerIds(out, capacity)


def CAD_GetLayerName(id: int) -> str | None:
    """C: int CAD_GetLayerName(uint32_t id, char* out, int capacity)
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetLayerName(id, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_RenameLayer(id: int, name: str | None) -> bool:
    """C: bool CAD_RenameLayer(uint32_t id, const char* name)
    """
    return _f.CAD_RenameLayer(id, _n.text(name))


def CAD_SetLayerVisible(id: int, visible: bool) -> bool:
    """C: bool CAD_SetLayerVisible(uint32_t id, bool visible)
    """
    return _f.CAD_SetLayerVisible(id, visible)


def CAD_IsLayerVisible(id: int) -> bool:
    """C: bool CAD_IsLayerVisible(uint32_t id)
    """
    return _f.CAD_IsLayerVisible(id)


def CAD_SetLayerLocked(id: int, locked: bool) -> bool:
    """C: bool CAD_SetLayerLocked(uint32_t id, bool locked)
    """
    return _f.CAD_SetLayerLocked(id, locked)


def CAD_IsLayerLocked(id: int) -> bool:
    """C: bool CAD_IsLayerLocked(uint32_t id)
    """
    return _f.CAD_IsLayerLocked(id)
