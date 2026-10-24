# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Objects 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_OSNAP_END', 'CAD_OSNAP_MID', 'CAD_OSNAP_CEN', 'CAD_OSNAP_FACE', 'CAD_OSNAP_NODE', 'CAD_OSNAP_QUA', 'CAD_OSNAP_INT', 'CAD_OSNAP_PER', 'CAD_OSNAP_TAN', 'CAD_OSNAP_NEA', 'CAD_OSNAP_ALL', 'CAD_GetObjectJson', 'CAD_GetObjectProperty', 'CAD_SetObjectProperty', 'CAD_GetLastError', 'CAD_QueryObjects', 'CAD_SelectByQuery', 'CAD_GetSceneJson', 'CAD_DeleteObject', 'CAD_GetObjectCount', 'CAD_GetObjectIds', 'CAD_GetObjectKind', 'CAD_ObjectExists', 'CAD_GetPosition', 'CAD_SetPosition', 'CAD_GetScale', 'CAD_SetScale', 'CAD_GetRotationAxisAngle', 'CAD_SetRotationAxisAngle', 'CAD_GetTransform', 'CAD_SetTransform', 'CAD_SetObjectName', 'CAD_GetObjectName', 'CAD_FindObjectByName', 'CAD_SetObjectVisible', 'CAD_IsObjectVisible', 'CAD_GetColor', 'CAD_SetColor', 'CAD_GetObjectEffectiveColor', 'CAD_SetObjectColorByLayer', 'CAD_GetObjectColorByLayer', 'CAD_SetSelectedColorByLayer', 'CAD_SetObjectOpacity', 'CAD_GetObjectOpacity', 'CAD_SetSelectedOpacity', 'CAD_SetObjectLayer', 'CAD_GetObjectLayer', 'CAD_AssignSelectedToLayer', 'CAD_GetBoundsWorld', 'CAD_GetCenterWorld', 'CAD_GetLength', 'CAD_GetArea', 'CAD_GetSelectionLength', 'CAD_GetSelectionArea', 'CAD_ApplyMaterial', 'CAD_GetMaterialCount', 'CAD_GetMaterialName', 'CAD_EntityTransform', 'CAD_EntityMove', 'CAD_EntityRotate', 'CAD_EntityScale', 'CAD_EntityCopy', 'CAD_EntityErase', 'CAD_EntityExplode', 'CAD_EntityArrayRect', 'CAD_EntityArrayPolar', 'CAD_EntityMirror', 'CAD_EntityGetExtents', 'CAD_EntityGetOsnapPoints', 'CAD_EntityGetGripPoints', 'CAD_EntityMoveGripPoints']

_f = _n.native

CAD_OSNAP_END = 1
CAD_OSNAP_MID = 2
CAD_OSNAP_CEN = 4
CAD_OSNAP_FACE = 8
CAD_OSNAP_NODE = 16
CAD_OSNAP_QUA = 32
CAD_OSNAP_INT = 64
CAD_OSNAP_PER = 128
CAD_OSNAP_TAN = 256
CAD_OSNAP_NEA = 512
CAD_OSNAP_ALL = 1023

_n.bind("CAD_GetObjectJson", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_GetObjectProperty", _c.c_int32, [_c.c_uint32, _c.c_char_p, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_SetObjectProperty", _c.c_int32, [_c.c_uint32, _c.c_char_p, _c.c_char_p])
_n.bind("CAD_GetLastError", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_QueryObjects", _c.c_int32, [_c.c_char_p, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_SelectByQuery", _c.c_int32, [_c.c_char_p, _c.c_bool, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_GetSceneJson", _c.c_int32, [_c.c_int32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_DeleteObject", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_GetObjectCount", _c.c_int32, [])
_n.bind("CAD_GetObjectIds", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_GetObjectKind", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_int32)])
_n.bind("CAD_ObjectExists", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_bool)])
_n.bind("CAD_GetPosition", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_SetPosition", _c.c_int32, [_c.c_uint32, CAD_GeVec3])
_n.bind("CAD_GetScale", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_SetScale", _c.c_int32, [_c.c_uint32, CAD_GeVec3])
_n.bind("CAD_GetRotationAxisAngle", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_GeVec3), _c.POINTER(_c.c_double)])
_n.bind("CAD_SetRotationAxisAngle", _c.c_int32, [_c.c_uint32, CAD_GeVec3, _c.c_double])
_n.bind("CAD_GetTransform", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_GeMatrix)])
_n.bind("CAD_SetTransform", _c.c_int32, [_c.c_uint32, CAD_GeMatrix])
_n.bind("CAD_SetObjectName", _c.c_int32, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_GetObjectName", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_FindObjectByName", _c.c_int32, [_c.c_char_p, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetObjectVisible", _c.c_int32, [_c.c_uint32, _c.c_bool])
_n.bind("CAD_IsObjectVisible", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_bool)])
_n.bind("CAD_GetColor", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_Color)])
_n.bind("CAD_SetColor", _c.c_int32, [_c.c_uint32, CAD_Color])
_n.bind("CAD_GetObjectEffectiveColor", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_Color)])
_n.bind("CAD_SetObjectColorByLayer", _c.c_int32, [_c.c_uint32, _c.c_bool])
_n.bind("CAD_GetObjectColorByLayer", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_bool)])
_n.bind("CAD_SetSelectedColorByLayer", _c.c_int32, [_c.c_bool, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetObjectOpacity", _c.c_int32, [_c.c_uint32, _c.c_double])
_n.bind("CAD_GetObjectOpacity", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_double)])
_n.bind("CAD_SetSelectedOpacity", _c.c_int32, [_c.c_double, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetObjectLayer", _c.c_int32, [_c.c_uint32, _c.c_uint32])
_n.bind("CAD_GetObjectLayer", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_AssignSelectedToLayer", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_GetBoundsWorld", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_GeVec3), _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_GetCenterWorld", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_GetLength", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_double)])
_n.bind("CAD_GetArea", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_double)])
_n.bind("CAD_GetSelectionLength", _c.c_int32, [_c.POINTER(_c.c_double)])
_n.bind("CAD_GetSelectionArea", _c.c_int32, [_c.POINTER(_c.c_double)])
_n.bind("CAD_ApplyMaterial", _c.c_int32, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_GetMaterialCount", _c.c_int32, [])
_n.bind("CAD_GetMaterialName", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_EntityTransform", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, CAD_GeMatrix])
_n.bind("CAD_EntityMove", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, CAD_GeVec3])
_n.bind("CAD_EntityRotate", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, CAD_GeVec3, CAD_GeVec3, _c.c_double])
_n.bind("CAD_EntityScale", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, CAD_GeVec3, _c.c_double])
_n.bind("CAD_EntityCopy", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, CAD_GeMatrix, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_EntityErase", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_EntityExplode", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_EntityArrayRect", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_uint32, _c.c_uint32, _c.c_uint32, CAD_GeVec3, CAD_GeVec3, CAD_GeVec3, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_EntityArrayPolar", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_uint32, _c.c_double, CAD_GeVec3, CAD_GeVec3, _c.c_bool, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_EntityMirror", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, CAD_GePlane, _c.c_bool, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_EntityGetExtents", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_GeVec3), _c.POINTER(CAD_GeVec3)])
_n.bind("CAD_EntityGetOsnapPoints", _c.c_int32, [_c.c_uint32, _c.c_uint32, _c.POINTER(CAD_OsnapOptions), _c.POINTER(CAD_OsnapPoint), _c.c_uint32])
_n.bind("CAD_EntityGetGripPoints", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_GeVec3), _c.c_uint32])
_n.bind("CAD_EntityMoveGripPoints", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_uint32), _c.c_uint32, CAD_GeVec3])


def CAD_GetObjectJson(id: int) -> str | None:
    """C: int32_t CAD_GetObjectJson(uint32_t id, char* buf, uint32_t capacity)

    객체 하나를 JSON 한 줄로 — 종류·이름·레이어·색·변환·경계 + 종류별 기하.
    (line: start/end/length, polyline: points/closed, circle: center/radius/normal, arc: +startDeg/endDeg,
     text: text/height/font, dimension: dimType/p1/p2/value, mesh: vertices/triangles/light)
    단위 mm, 좌표 월드. 키 이름은 lot_object_json.h 한 곳에서 정하며 AI 선택 문맥·씬 요약과 같다.
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
    """C: int32_t CAD_GetObjectProperty(uint32_t id, const char* key, char* buf, uint32_t capacity)

    이름으로 속성 하나 읽기·쓰기 — 키는 CAD_GetObjectJson 의 키와 같다.
      공통    name, color, colorByLayer, visible, layer(이름|id), linetype(이름|id|"bylayer"), linetypeScale,
              position, rotation[x,y,z,w], scale, opacity, metallic, group
      line    start, end          polyline  points, closed        circle  center, radius
      arc     center, radius, startDeg, endDeg                     text    text, height, font
      dimension p1, p2, p3, dimLinePoint, precision                mesh    intensity(조명)
    Get: 값의 JSON 텍스트(예: 50.0 / [1,2,3] / "이름"). 없는 키 = CAD_E_NOT_FOUND.
    Set: valueJson 은 JSON(따옴표 없는 글자는 문자열로 받음). 좌표·길이는 월드 mm. 딸린 모델을 다시 만든다.
         없는 키·형식 오류 = CAD_E_INVALID_ARG(이유 글에 무엇이 틀렸는지).
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


def CAD_SetObjectProperty(id: int, key: str | None, valueJson: str | None) -> int:
    """C: CAD_Status CAD_SetObjectProperty(uint32_t id, const char* key, const char* valueJson)

    이름으로 속성 하나 읽기·쓰기 — 키는 CAD_GetObjectJson 의 키와 같다.
      공통    name, color, colorByLayer, visible, layer(이름|id), linetype(이름|id|"bylayer"), linetypeScale,
              position, rotation[x,y,z,w], scale, opacity, metallic, group
      line    start, end          polyline  points, closed        circle  center, radius
      arc     center, radius, startDeg, endDeg                     text    text, height, font
      dimension p1, p2, p3, dimLinePoint, precision                mesh    intensity(조명)
    Get: 값의 JSON 텍스트(예: 50.0 / [1,2,3] / "이름"). 없는 키 = CAD_E_NOT_FOUND.
    Set: valueJson 은 JSON(따옴표 없는 글자는 문자열로 받음). 좌표·길이는 월드 mm. 딸린 모델을 다시 만든다.
         없는 키·형식 오류 = CAD_E_INVALID_ARG(이유 글에 무엇이 틀렸는지).
    """
    return _f.CAD_SetObjectProperty(id, _n.text(key), _n.text(valueJson))


def CAD_GetLastError() -> str | None:
    """C: int32_t CAD_GetLastError(char* buf, uint32_t capacity)

    이 스레드에서 직전에 실패한 함수의 이유(UTF-8, 화면 언어) — 스레드마다 따로, 아무 스레드에서나. CAD_Status·개수를 돌려주는 함수는
    성공하면 비운다(아직 옛 규칙인 영역의 함수 일부는 실패 때만 쓴다). 프로그램은 글이 아니라 결과 코드(CAD_E_*)로 가를 것.
    이 함수는 글을 비우지 않는다.
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


def CAD_QueryObjects(filterJson: str | None, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_QueryObjects(const char* filterJson, uint32_t* outIds, uint32_t capacity)

    질의 — 필터 JSON 으로 객체 id 목록. 키는 전부 선택(AND):
      {"kind":"circle"|["circle","arc"], "layer":"이름"|id, "name":"기둥*"(글롭), "selected":true, "visible":true,
       "within":{"min":[x,y,z],"max":[x,y,z]}(상자 안), "intersects":{min,max}(겹침), "near":{"point":[x,y,z],"radius":r},
       "pick":"largest"|"smallest"(통과한 것 중 하나), "limit":N}
    반환 = 전체 개수. 틀린 필터 = CAD_E_INVALID_ARG.
    """
    return _f.CAD_QueryObjects(_n.text(filterJson), outIds, capacity)


def CAD_SelectByQuery(filterJson: str | None, additive: bool) -> tuple[int, int]:
    """C: CAD_Status CAD_SelectByQuery(const char* filterJson, bool additive, uint32_t* outSelected)

    질의 결과를 선택으로 — 같은 필터 문법. additive = false 면 기존 선택을 비운다. outSelected = 고른 수(NULL 이면 안 받음).
    AI 의 edit_selected op="select" 와 같은 통로.
    """
    outSelected = _c.c_uint32()
    _r = _f.CAD_SelectByQuery(_n.text(filterJson), additive, _c.byref(outSelected))
    return (_r, outSelected.value)


def CAD_GetSceneJson(maxObjects: int) -> str | None:
    """C: int32_t CAD_GetSceneJson(int32_t maxObjects, char* buf, uint32_t capacity)

    씬 요약 JSON — {"count","selected","units":"mm","bounds","kinds":{종류:수},"layers":[…],"objects":[요약…],"more"}.
    objects 는 앞에서 maxObjects 개(0 이면 50). 객체 상세는 CAD_GetObjectJson.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetSceneJson(maxObjects, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_DeleteObject(id: int) -> int:
    """C: CAD_Status CAD_DeleteObject(uint32_t id)

    지우기 — 여러 개는 CAD_EntityErase
    """
    return _f.CAD_DeleteObject(id)


def CAD_GetObjectCount() -> int:
    """C: int32_t CAD_GetObjectCount(void)

    장면의 객체 수
    """
    return _f.CAD_GetObjectCount()


def CAD_GetObjectIds(outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_GetObjectIds(uint32_t* outIds, uint32_t capacity)

    전체 객체 id — 반환 = 전체 개수
    """
    return _f.CAD_GetObjectIds(outIds, capacity)


def CAD_GetObjectKind(id: int) -> tuple[int, int]:
    """C: CAD_Status CAD_GetObjectKind(uint32_t id, int32_t* outKind)

    종류: 0=Mesh 1=Line 2=Polyline 3=Circle 4=Arc 5=Text 6=Dimension 7=PointCloud 8=ParticleEmitter … (PrimitiveKind 번호)
    """
    outKind = _c.c_int32()
    _r = _f.CAD_GetObjectKind(id, _c.byref(outKind))
    return (_r, outKind.value)


def CAD_ObjectExists(id: int) -> tuple[int, bool]:
    """C: CAD_Status CAD_ObjectExists(uint32_t id, bool* outExists)

    있는가 — 없는 id 도 CAD_OK(outExists = false). 엔진이 없거나 다른 스레드면 그 코드
    """
    outExists = _c.c_bool()
    _r = _f.CAD_ObjectExists(id, _c.byref(outExists))
    return (_r, outExists.value)


def CAD_GetPosition(id: int) -> tuple[int, CAD_GeVec3]:
    """C: CAD_Status CAD_GetPosition(uint32_t id, CAD_GeVec3* outPosition)

    변환 — 객체 = 위치·회전·축척(T·R·S). 위치 = 객체 기준점의 월드 자리, 축척 = 축마다(0 이나 음수는 CAD_E_INVALID_ARG)
    """
    outPosition = CAD_GeVec3()
    _r = _f.CAD_GetPosition(id, _c.byref(outPosition))
    return (_r, outPosition)


def CAD_SetPosition(id: int, position: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_SetPosition(uint32_t id, CAD_GeVec3 position)

    변환 — 객체 = 위치·회전·축척(T·R·S). 위치 = 객체 기준점의 월드 자리, 축척 = 축마다(0 이나 음수는 CAD_E_INVALID_ARG)
    """
    return _f.CAD_SetPosition(id, position)


def CAD_GetScale(id: int) -> tuple[int, CAD_GeVec3]:
    """C: CAD_Status CAD_GetScale(uint32_t id, CAD_GeVec3* outScale)

    변환 — 객체 = 위치·회전·축척(T·R·S). 위치 = 객체 기준점의 월드 자리, 축척 = 축마다(0 이나 음수는 CAD_E_INVALID_ARG)
    """
    outScale = CAD_GeVec3()
    _r = _f.CAD_GetScale(id, _c.byref(outScale))
    return (_r, outScale)


def CAD_SetScale(id: int, scale: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_SetScale(uint32_t id, CAD_GeVec3 scale)

    변환 — 객체 = 위치·회전·축척(T·R·S). 위치 = 객체 기준점의 월드 자리, 축척 = 축마다(0 이나 음수는 CAD_E_INVALID_ARG)
    """
    return _f.CAD_SetScale(id, scale)


def CAD_GetRotationAxisAngle(id: int) -> tuple[int, CAD_GeVec3, float]:
    """C: CAD_Status CAD_GetRotationAxisAngle(uint32_t id, CAD_GeVec3* outAxis, double* outAngle)

    회전 = axis 둘레로 angle(rad, 오른손). Get 은 회전이 없으면 축 (0,0,1)·각 0. Set 의 axis 길이 0 = CAD_E_DEGENERATE
    """
    outAxis = CAD_GeVec3()
    outAngle = _c.c_double()
    _r = _f.CAD_GetRotationAxisAngle(id, _c.byref(outAxis), _c.byref(outAngle))
    return (_r, outAxis, outAngle.value)


def CAD_SetRotationAxisAngle(id: int, axis: CAD_GeVec3, angle: float) -> int:
    """C: CAD_Status CAD_SetRotationAxisAngle(uint32_t id, CAD_GeVec3 axis, double angle)

    회전 = axis 둘레로 angle(rad, 오른손). Get 은 회전이 없으면 축 (0,0,1)·각 0. Set 의 axis 길이 0 = CAD_E_DEGENERATE
    """
    return _f.CAD_SetRotationAxisAngle(id, axis, angle)


def CAD_GetTransform(id: int) -> tuple[int, CAD_GeMatrix]:
    """C: CAD_Status CAD_GetTransform(uint32_t id, CAD_GeMatrix* outMatrix)

    위치·회전·축척을 행렬 하나로(m = T·R·S, 열 우선 — CAD_GeMatrix). 한 번에 대입하니 "옮겼지만 아직 안 돌아간" 프레임이 없다
    (로봇 관절·모션 캡처·시뮬레이터가 매 프레임 자세를 밀어 넣는 길). Set 은 비틀림(열이 서로 수직 아님)·대칭(행렬식 < 0)이면
    CAD_E_NOT_SUPPORTED, 축척 0 = CAD_E_DEGENERATE. 회전 행렬은 CAD_GeMatrixRotation·CAD_GeMatrixCoordSys 로 만든다.
    엔진은 ROS(REP-103)와 같은 Z-up 오른손 좌표계 — 전방만 다르다(ROS +X, 엔진 +Y).
    """
    outMatrix = CAD_GeMatrix()
    _r = _f.CAD_GetTransform(id, _c.byref(outMatrix))
    return (_r, outMatrix)


def CAD_SetTransform(id: int, m: CAD_GeMatrix) -> int:
    """C: CAD_Status CAD_SetTransform(uint32_t id, CAD_GeMatrix m)

    위치·회전·축척을 행렬 하나로(m = T·R·S, 열 우선 — CAD_GeMatrix). 한 번에 대입하니 "옮겼지만 아직 안 돌아간" 프레임이 없다
    (로봇 관절·모션 캡처·시뮬레이터가 매 프레임 자세를 밀어 넣는 길). Set 은 비틀림(열이 서로 수직 아님)·대칭(행렬식 < 0)이면
    CAD_E_NOT_SUPPORTED, 축척 0 = CAD_E_DEGENERATE. 회전 행렬은 CAD_GeMatrixRotation·CAD_GeMatrixCoordSys 로 만든다.
    엔진은 ROS(REP-103)와 같은 Z-up 오른손 좌표계 — 전방만 다르다(ROS +X, 엔진 +Y).
    """
    return _f.CAD_SetTransform(id, m)


def CAD_SetObjectName(id: int, name: str | None) -> int:
    """C: CAD_Status CAD_SetObjectName(uint32_t id, const char* name)

    이름 — 장면 안에서 **하나**여야 한다(이름은 사람과 외부 API 가 부품을 가리키는 수단이라). 이미 쓰는 이름 = CAD_E_DUPLICATE.
    앞뒤 공백은 뗀다, 빈 이름(이름 없음)은 몇 개든 된다. FindObjectByName 은 없으면 CAD_E_NOT_FOUND
    """
    return _f.CAD_SetObjectName(id, _n.text(name))


def CAD_GetObjectName(id: int) -> str | None:
    """C: int32_t CAD_GetObjectName(uint32_t id, char* buf, uint32_t capacity)

    이름 — 장면 안에서 **하나**여야 한다(이름은 사람과 외부 API 가 부품을 가리키는 수단이라). 이미 쓰는 이름 = CAD_E_DUPLICATE.
    앞뒤 공백은 뗀다, 빈 이름(이름 없음)은 몇 개든 된다. FindObjectByName 은 없으면 CAD_E_NOT_FOUND
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


def CAD_FindObjectByName(name: str | None) -> tuple[int, int]:
    """C: CAD_Status CAD_FindObjectByName(const char* name, uint32_t* outId)

    이름 — 장면 안에서 **하나**여야 한다(이름은 사람과 외부 API 가 부품을 가리키는 수단이라). 이미 쓰는 이름 = CAD_E_DUPLICATE.
    앞뒤 공백은 뗀다, 빈 이름(이름 없음)은 몇 개든 된다. FindObjectByName 은 없으면 CAD_E_NOT_FOUND
    """
    outId = _c.c_uint32()
    _r = _f.CAD_FindObjectByName(_n.text(name), _c.byref(outId))
    return (_r, outId.value)


def CAD_SetObjectVisible(id: int, visible: bool) -> int:
    """C: CAD_Status CAD_SetObjectVisible(uint32_t id, bool visible)

    보이기 — 숨긴 객체는 문서에 남지만 고르기·스냅이 안 된다. IsObjectVisible = 객체·도면층이 다 보일 때 참
    """
    return _f.CAD_SetObjectVisible(id, visible)


def CAD_IsObjectVisible(id: int) -> tuple[int, bool]:
    """C: CAD_Status CAD_IsObjectVisible(uint32_t id, bool* outVisible)

    보이기 — 숨긴 객체는 문서에 남지만 고르기·스냅이 안 된다. IsObjectVisible = 객체·도면층이 다 보일 때 참
    """
    outVisible = _c.c_bool()
    _r = _f.CAD_IsObjectVisible(id, _c.byref(outVisible))
    return (_r, outVisible.value)


def CAD_GetColor(id: int) -> tuple[int, CAD_Color]:
    """C: CAD_Status CAD_GetColor(uint32_t id, CAD_Color* outColor)

    색 — Get/SetColor = 객체 자기 색, EffectiveColor = 화면에 쓰는 색(도면층 색을 따르면 도면층 색).
    ColorByLayer = 도면층 색 따르기. 선택 전부에 하는 함수의 outChanged = 바뀐 수(NULL 이면 안 받음, 잠긴 도면층 것은 건너뜀)
    """
    outColor = CAD_Color()
    _r = _f.CAD_GetColor(id, _c.byref(outColor))
    return (_r, outColor)


def CAD_SetColor(id: int, color: CAD_Color) -> int:
    """C: CAD_Status CAD_SetColor(uint32_t id, CAD_Color color)

    색 — Get/SetColor = 객체 자기 색, EffectiveColor = 화면에 쓰는 색(도면층 색을 따르면 도면층 색).
    ColorByLayer = 도면층 색 따르기. 선택 전부에 하는 함수의 outChanged = 바뀐 수(NULL 이면 안 받음, 잠긴 도면층 것은 건너뜀)
    """
    return _f.CAD_SetColor(id, color)


def CAD_GetObjectEffectiveColor(id: int) -> tuple[int, CAD_Color]:
    """C: CAD_Status CAD_GetObjectEffectiveColor(uint32_t id, CAD_Color* outColor)

    색 — Get/SetColor = 객체 자기 색, EffectiveColor = 화면에 쓰는 색(도면층 색을 따르면 도면층 색).
    ColorByLayer = 도면층 색 따르기. 선택 전부에 하는 함수의 outChanged = 바뀐 수(NULL 이면 안 받음, 잠긴 도면층 것은 건너뜀)
    """
    outColor = CAD_Color()
    _r = _f.CAD_GetObjectEffectiveColor(id, _c.byref(outColor))
    return (_r, outColor)


def CAD_SetObjectColorByLayer(id: int, byLayer: bool) -> int:
    """C: CAD_Status CAD_SetObjectColorByLayer(uint32_t id, bool byLayer)

    색 — Get/SetColor = 객체 자기 색, EffectiveColor = 화면에 쓰는 색(도면층 색을 따르면 도면층 색).
    ColorByLayer = 도면층 색 따르기. 선택 전부에 하는 함수의 outChanged = 바뀐 수(NULL 이면 안 받음, 잠긴 도면층 것은 건너뜀)
    """
    return _f.CAD_SetObjectColorByLayer(id, byLayer)


def CAD_GetObjectColorByLayer(id: int) -> tuple[int, bool]:
    """C: CAD_Status CAD_GetObjectColorByLayer(uint32_t id, bool* outByLayer)

    색 — Get/SetColor = 객체 자기 색, EffectiveColor = 화면에 쓰는 색(도면층 색을 따르면 도면층 색).
    ColorByLayer = 도면층 색 따르기. 선택 전부에 하는 함수의 outChanged = 바뀐 수(NULL 이면 안 받음, 잠긴 도면층 것은 건너뜀)
    """
    outByLayer = _c.c_bool()
    _r = _f.CAD_GetObjectColorByLayer(id, _c.byref(outByLayer))
    return (_r, outByLayer.value)


def CAD_SetSelectedColorByLayer(byLayer: bool) -> tuple[int, int]:
    """C: CAD_Status CAD_SetSelectedColorByLayer(bool byLayer, uint32_t* outChanged)

    색 — Get/SetColor = 객체 자기 색, EffectiveColor = 화면에 쓰는 색(도면층 색을 따르면 도면층 색).
    ColorByLayer = 도면층 색 따르기. 선택 전부에 하는 함수의 outChanged = 바뀐 수(NULL 이면 안 받음, 잠긴 도면층 것은 건너뜀)
    """
    outChanged = _c.c_uint32()
    _r = _f.CAD_SetSelectedColorByLayer(byLayer, _c.byref(outChanged))
    return (_r, outChanged.value)


def CAD_SetObjectOpacity(id: int, opacity: float) -> int:
    """C: CAD_Status CAD_SetObjectOpacity(uint32_t id, double opacity)

    불투명도 0..1 (1 = 불투명). 객체 것 × 도면층 것이 화면에 쓰인다 — 메시(채움)에만, 선·문자는 그대로.
    이름 기반 속성 "opacity" 와 같은 값
    """
    return _f.CAD_SetObjectOpacity(id, opacity)


def CAD_GetObjectOpacity(id: int) -> tuple[int, float]:
    """C: CAD_Status CAD_GetObjectOpacity(uint32_t id, double* outOpacity)

    불투명도 0..1 (1 = 불투명). 객체 것 × 도면층 것이 화면에 쓰인다 — 메시(채움)에만, 선·문자는 그대로.
    이름 기반 속성 "opacity" 와 같은 값
    """
    outOpacity = _c.c_double()
    _r = _f.CAD_GetObjectOpacity(id, _c.byref(outOpacity))
    return (_r, outOpacity.value)


def CAD_SetSelectedOpacity(opacity: float) -> tuple[int, int]:
    """C: CAD_Status CAD_SetSelectedOpacity(double opacity, uint32_t* outChanged)

    불투명도 0..1 (1 = 불투명). 객체 것 × 도면층 것이 화면에 쓰인다 — 메시(채움)에만, 선·문자는 그대로.
    이름 기반 속성 "opacity" 와 같은 값
    """
    outChanged = _c.c_uint32()
    _r = _f.CAD_SetSelectedOpacity(opacity, _c.byref(outChanged))
    return (_r, outChanged.value)


def CAD_SetObjectLayer(objectId: int, layerId: int) -> int:
    """C: CAD_Status CAD_SetObjectLayer(uint32_t objectId, uint32_t layerId)

    도면층 — 0 = 도면층 "0". 없는 도면층 id = CAD_E_BAD_HANDLE. 그립을 끄는 중이면 CAD_E_BUSY
    """
    return _f.CAD_SetObjectLayer(objectId, layerId)


def CAD_GetObjectLayer(objectId: int) -> tuple[int, int]:
    """C: CAD_Status CAD_GetObjectLayer(uint32_t objectId, uint32_t* outLayerId)

    도면층 — 0 = 도면층 "0". 없는 도면층 id = CAD_E_BAD_HANDLE. 그립을 끄는 중이면 CAD_E_BUSY
    """
    outLayerId = _c.c_uint32()
    _r = _f.CAD_GetObjectLayer(objectId, _c.byref(outLayerId))
    return (_r, outLayerId.value)


def CAD_AssignSelectedToLayer(layerId: int) -> tuple[int, int]:
    """C: CAD_Status CAD_AssignSelectedToLayer(uint32_t layerId, uint32_t* outChanged)

    도면층 — 0 = 도면층 "0". 없는 도면층 id = CAD_E_BAD_HANDLE. 그립을 끄는 중이면 CAD_E_BUSY
    """
    outChanged = _c.c_uint32()
    _r = _f.CAD_AssignSelectedToLayer(layerId, _c.byref(outChanged))
    return (_r, outChanged.value)


def CAD_GetBoundsWorld(id: int) -> tuple[int, CAD_GeVec3, CAD_GeVec3]:
    """C: CAD_Status CAD_GetBoundsWorld(uint32_t id, CAD_GeVec3* outMin, CAD_GeVec3* outMax)

    월드 경계 상자(min/max), 가운데 = 0.5·(min + max). 큰 가져온 메시도 상자로
    """
    outMin = CAD_GeVec3()
    outMax = CAD_GeVec3()
    _r = _f.CAD_GetBoundsWorld(id, _c.byref(outMin), _c.byref(outMax))
    return (_r, outMin, outMax)


def CAD_GetCenterWorld(id: int) -> tuple[int, CAD_GeVec3]:
    """C: CAD_Status CAD_GetCenterWorld(uint32_t id, CAD_GeVec3* outCenter)

    월드 경계 상자(min/max), 가운데 = 0.5·(min + max). 큰 가져온 메시도 상자로
    """
    outCenter = CAD_GeVec3()
    _r = _f.CAD_GetCenterWorld(id, _c.byref(outCenter))
    return (_r, outCenter)


def CAD_GetLength(id: int) -> tuple[int, float]:
    """C: CAD_Status CAD_GetLength(uint32_t id, double* outLength)

    측정
    **월드 좌표로** 잰다 — 축척이 걸린 객체도 화면에 보이는 값과 맞는다.
    길이: 선/폴리선 = 변의 합(닫혀 있으면 마지막→첫 변 포함), 원 = 2πr, 호 = rθ.
    넓이: 닫힌 폴리선 = 신발끈 공식(3D 평면판), 원 = πr², 호 = 부채꼴.
    메시·문자·점군은 CAD_E_WRONG_TYPE(그 종류엔 정의되지 않는다).
    선택 합: 잴 수 없는 종류는 건너뛴다(선택이 비었거나 잴 게 없으면 0, CAD_OK).
    """
    outLength = _c.c_double()
    _r = _f.CAD_GetLength(id, _c.byref(outLength))
    return (_r, outLength.value)


def CAD_GetArea(id: int) -> tuple[int, float]:
    """C: CAD_Status CAD_GetArea(uint32_t id, double* outArea)

    측정
    **월드 좌표로** 잰다 — 축척이 걸린 객체도 화면에 보이는 값과 맞는다.
    길이: 선/폴리선 = 변의 합(닫혀 있으면 마지막→첫 변 포함), 원 = 2πr, 호 = rθ.
    넓이: 닫힌 폴리선 = 신발끈 공식(3D 평면판), 원 = πr², 호 = 부채꼴.
    메시·문자·점군은 CAD_E_WRONG_TYPE(그 종류엔 정의되지 않는다).
    선택 합: 잴 수 없는 종류는 건너뛴다(선택이 비었거나 잴 게 없으면 0, CAD_OK).
    """
    outArea = _c.c_double()
    _r = _f.CAD_GetArea(id, _c.byref(outArea))
    return (_r, outArea.value)


def CAD_GetSelectionLength() -> tuple[int, float]:
    """C: CAD_Status CAD_GetSelectionLength(double* outLength)

    측정
    **월드 좌표로** 잰다 — 축척이 걸린 객체도 화면에 보이는 값과 맞는다.
    길이: 선/폴리선 = 변의 합(닫혀 있으면 마지막→첫 변 포함), 원 = 2πr, 호 = rθ.
    넓이: 닫힌 폴리선 = 신발끈 공식(3D 평면판), 원 = πr², 호 = 부채꼴.
    메시·문자·점군은 CAD_E_WRONG_TYPE(그 종류엔 정의되지 않는다).
    선택 합: 잴 수 없는 종류는 건너뛴다(선택이 비었거나 잴 게 없으면 0, CAD_OK).
    """
    outLength = _c.c_double()
    _r = _f.CAD_GetSelectionLength(_c.byref(outLength))
    return (_r, outLength.value)


def CAD_GetSelectionArea() -> tuple[int, float]:
    """C: CAD_Status CAD_GetSelectionArea(double* outArea)

    측정
    **월드 좌표로** 잰다 — 축척이 걸린 객체도 화면에 보이는 값과 맞는다.
    길이: 선/폴리선 = 변의 합(닫혀 있으면 마지막→첫 변 포함), 원 = 2πr, 호 = rθ.
    넓이: 닫힌 폴리선 = 신발끈 공식(3D 평면판), 원 = πr², 호 = 부채꼴.
    메시·문자·점군은 CAD_E_WRONG_TYPE(그 종류엔 정의되지 않는다).
    선택 합: 잴 수 없는 종류는 건너뛴다(선택이 비었거나 잴 게 없으면 0, CAD_OK).
    """
    outArea = _c.c_double()
    _r = _f.CAD_GetSelectionArea(_c.byref(outArea))
    return (_r, outArea.value)


def CAD_ApplyMaterial(id: int, name: str | None) -> int:
    """C: CAD_Status CAD_ApplyMaterial(uint32_t id, const char* name)

    재질 — textures/ 의 파일 이름(확장자 없이, 예 "wood_oak_veneer"). 이름에 metal·steel 이 들면 금속 셰이딩.
    name 이 NULL/"" 이면 재질 빼기. 재질 패널 클릭과 같다(앱과 같이 되돌리기 없음). 없는 재질 = CAD_E_NOT_FOUND.
    GetMaterialName: index = 0 .. CAD_GetMaterialCount() − 1(밖 = CAD_E_OUT_OF_RANGE)
    """
    return _f.CAD_ApplyMaterial(id, _n.text(name))


def CAD_GetMaterialCount() -> int:
    """C: int32_t CAD_GetMaterialCount(void)

    재질 — textures/ 의 파일 이름(확장자 없이, 예 "wood_oak_veneer"). 이름에 metal·steel 이 들면 금속 셰이딩.
    name 이 NULL/"" 이면 재질 빼기. 재질 패널 클릭과 같다(앱과 같이 되돌리기 없음). 없는 재질 = CAD_E_NOT_FOUND.
    GetMaterialName: index = 0 .. CAD_GetMaterialCount() − 1(밖 = CAD_E_OUT_OF_RANGE)
    """
    return _f.CAD_GetMaterialCount()


def CAD_GetMaterialName(index: int) -> str | None:
    """C: int32_t CAD_GetMaterialName(uint32_t index, char* buf, uint32_t capacity)

    재질 — textures/ 의 파일 이름(확장자 없이, 예 "wood_oak_veneer"). 이름에 metal·steel 이 들면 금속 셰이딩.
    name 이 NULL/"" 이면 재질 빼기. 재질 패널 클릭과 같다(앱과 같이 되돌리기 없음). 없는 재질 = CAD_E_NOT_FOUND.
    GetMaterialName: index = 0 .. CAD_GetMaterialCount() − 1(밖 = CAD_E_OUT_OF_RANGE)
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetMaterialName(index, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_EntityTransform(ids: Sequence | None, count: int, m: CAD_GeMatrix) -> int:
    """C: CAD_Status CAD_EntityTransform(const uint32_t* ids, uint32_t count, CAD_GeMatrix m)

    변환 — transformBy. m 은 닮음 변환(회전·균일 축척·이동, 행렬식 > 0)만: 객체 변환이 이동·회전·축척이라.
    대칭·찌그러뜨림은 CAD_E_NOT_SUPPORTED(대칭은 CAD_EntityMirror)
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_EntityTransform(_a_ids, count, m)


def CAD_EntityMove(ids: Sequence | None, count: int, offset: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_EntityMove(const uint32_t* ids, uint32_t count, CAD_GeVec3 offset)

    offset(mm)만큼 옮기기

    묶음 주석: 변환 — transformBy. m 은 닮음 변환(회전·균일 축척·이동, 행렬식 > 0)만: 객체 변환이 이동·회전·축척이라.
    대칭·찌그러뜨림은 CAD_E_NOT_SUPPORTED(대칭은 CAD_EntityMirror)
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_EntityMove(_a_ids, count, offset)


def CAD_EntityRotate(ids: Sequence | None, count: int, basePoint: CAD_GeVec3, axis: CAD_GeVec3, angle: float) -> int:
    """C: CAD_Status CAD_EntityRotate(const uint32_t* ids, uint32_t count, CAD_GeVec3 basePoint, CAD_GeVec3 axis, double angle)

    basePoint 를 지나는 axis 둘레로 angle(rad, 오른손 — axis 끝에서 볼 때 반시계)
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_EntityRotate(_a_ids, count, basePoint, axis, angle)


def CAD_EntityScale(ids: Sequence | None, count: int, basePoint: CAD_GeVec3, factor: float) -> int:
    """C: CAD_Status CAD_EntityScale(const uint32_t* ids, uint32_t count, CAD_GeVec3 basePoint, double factor)

    basePoint 기준 균일 축척 — factor > 0
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_EntityScale(_a_ids, count, basePoint, factor)


def CAD_EntityCopy(ids: Sequence | None, count: int, m: CAD_GeMatrix, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_EntityCopy(const uint32_t* ids, uint32_t count, CAD_GeMatrix m, uint32_t* outIds, uint32_t capacity)

    변환한 사본 — getTransformedCopy. 사본은 원본의 도면층·색·이름을 이어받는다(잠긴 도면층 객체도 복사는 된다)
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_EntityCopy(_a_ids, count, m, outIds, capacity)


def CAD_EntityErase(ids: Sequence | None, count: int) -> int:
    """C: CAD_Status CAD_EntityErase(const uint32_t* ids, uint32_t count)

    지우기 — erase
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_EntityErase(_a_ids, count)


def CAD_EntityExplode(ids: Sequence | None, count: int, keepOriginal: bool, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_EntityExplode(const uint32_t* ids, uint32_t count, bool keepOriginal, uint32_t* outIds, uint32_t capacity)

    분해 — explode. 블록 참조 → 안 객체(한 단계), 폴리선·사각형·다각형 → 선, 문자 → 윤곽선 폴리선.
    쪼갤 수 없는 객체(선·원·호·메시 …)는 그대로 두고, 하나도 못 쪼개면 CAD_E_NOT_SUPPORTED. 외부 참조는 결합(xref bind) 먼저
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_EntityExplode(_a_ids, count, keepOriginal, outIds, capacity)


def CAD_EntityArrayRect(ids: Sequence | None, count: int, cols: int, rows: int, levels: int, colStep: CAD_GeVec3, rowStep: CAD_GeVec3, levelStep: CAD_GeVec3, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_EntityArrayRect(const uint32_t* ids, uint32_t count, uint32_t cols, uint32_t rows, uint32_t levels, CAD_GeVec3 colStep, CAD_GeVec3 rowStep, CAD_GeVec3 levelStep, uint32_t* outIds, uint32_t capacity)

    격자 배열 — 칸 (i, j, k)(i < cols, j < rows, k < levels)에 i·colStep + j·rowStep + k·levelStep 만큼 옮긴 사본. (0,0,0) = 원본 자리라
    사본 = (cols·rows·levels − 1) × count
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_EntityArrayRect(_a_ids, count, cols, rows, levels, colStep, rowStep, levelStep, outIds, capacity)


def CAD_EntityArrayPolar(ids: Sequence | None, count: int, itemCount: int, fillAngle: float, axisPoint: CAD_GeVec3, axisDir: CAD_GeVec3, rotateItems: bool, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_EntityArrayPolar(const uint32_t* ids, uint32_t count, uint32_t itemCount, double fillAngle, CAD_GeVec3 axisPoint, CAD_GeVec3 axisDir, bool rotateItems, uint32_t* outIds, uint32_t capacity)

    원형 배열 — itemCount = 원본 포함 개수(2 이상), fillAngle(rad) = 채울 각: 2π(한 바퀴)면 itemCount 등분, 아니면 양 끝을 포함해
    itemCount − 1 등분(오토캐드와 같다). axisPoint 를 지나는 axisDir 둘레. rotateItems = false 면 방향은 두고 자리만 옮긴다
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_EntityArrayPolar(_a_ids, count, itemCount, fillAngle, axisPoint, axisDir, rotateItems, outIds, capacity)


def CAD_EntityMirror(ids: Sequence | None, count: int, plane: CAD_GePlane, eraseSource: bool, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_EntityMirror(const uint32_t* ids, uint32_t count, CAD_GePlane plane, bool eraseSource, uint32_t* outIds, uint32_t capacity)

    평면 대칭 사본 — mirror. 곡선(선·원·호·타원·스플라인·폴리선)은 정확히, 메시는 정점을 뒤집어. 문자·치수·블록 = CAD_E_NOT_SUPPORTED.
    eraseSource = 원본 지움(그때는 잠긴 도면층 객체 = CAD_E_LOCKED)
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_EntityMirror(_a_ids, count, plane, eraseSource, outIds, capacity)


def CAD_EntityGetExtents(id: int) -> tuple[int, CAD_GeVec3, CAD_GeVec3]:
    """C: CAD_Status CAD_EntityGetExtents(uint32_t id, CAD_GeVec3* outMin, CAD_GeVec3* outMax)

    월드 경계 상자 — getGeomExtents
    """
    outMin = CAD_GeVec3()
    outMax = CAD_GeVec3()
    _r = _f.CAD_EntityGetExtents(id, _c.byref(outMin), _c.byref(outMax))
    return (_r, outMin, outMax)


def CAD_EntityGetOsnapPoints(id: int, modes: int, outPoints: Any, capacity: int, opt: CAD_OsnapOptions | None = None, **fields) -> int:
    """C: int32_t CAD_EntityGetOsnapPoints(uint32_t id, uint32_t modes, const CAD_OsnapOptions* opt, CAD_OsnapPoint* outPoints, uint32_t capacity)

    객체 하나의 스냅점 — getOsnapPoints. modes = CAD_OSNAP_* 합. 같은 종류·같은 자리는 하나만. 반환 = 전체 개수.
    점군은 후보 없음(0), 근처·수직·접선은 곡선 객체만
    """
    if opt is None and fields:
        opt = CAD_OsnapOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_OsnapOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_EntityGetOsnapPoints(id, modes, _p_opt, outPoints, capacity)


def CAD_EntityGetGripPoints(id: int, outPoints: Any, capacity: int) -> int:
    """C: int32_t CAD_EntityGetGripPoints(uint32_t id, CAD_GeVec3* outPoints, uint32_t capacity)

    그립 점(월드) — getGripPoints. 번호는 화면 그립과 같다: 선 0·1 끝 · 원 0 중심·1~4 사분점 · 호 0 중심·1 시작·2 끝·3 가운데 ·
    폴리선 = 정점 · 타원 0 중심·1/3 장축 끝·2/4 단축 끝 · 스플라인 = 맞춤점(없으면 제어점) · 치수 0·1 측정점·2 치수선 · 문자·블록 0 삽입점 ·
    메시 = 겹치지 않는 꼭짓점. 반환 = 전체 개수(해치·점군 = 0)
    """
    return _f.CAD_EntityGetGripPoints(id, outPoints, capacity)


def CAD_EntityMoveGripPoints(id: int, indices: Sequence | None, count: int, offset: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_EntityMoveGripPoints(uint32_t id, const uint32_t* indices, uint32_t count, CAD_GeVec3 offset)

    그립들을 offset 만큼 — moveGripPointsAt. 고른 그립을 모두 옮기면 객체 이동과 같다(선의 0·1). 되돌리기 1.
    번호 범위 밖 = CAD_E_OUT_OF_RANGE, B-Rep 솔리드 = CAD_E_NOT_SUPPORTED(모양은 CAD_SetFeatureDimension 으로)
    """
    _a_indices = _n.array(_c.c_uint32, indices)
    return _f.CAD_EntityMoveGripPoints(id, _a_indices, count, offset)
