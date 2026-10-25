# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Graph 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_NodeGraph', 'CAD_NodeGraphGetJson', 'CAD_NodeGraphGetKindsJson', 'CAD_NodeGraphSetJson', 'CAD_NodeGraphClear', 'CAD_NodeGraphEvaluate', 'CAD_NodeGraphAddNode', 'CAD_NodeGraphRemoveNode', 'CAD_NodeGraphMoveNode', 'CAD_NodeGraphConnect', 'CAD_NodeGraphDisconnect', 'CAD_NodeGraphSetNumber', 'CAD_NodeGraphSetBool', 'CAD_NodeGraphSetText', 'CAD_NodeGraphSetPoint', 'CAD_NodeGraphSetMuted', 'CAD_NodeGraphGetNodeObjects', 'CAD_NodeGraphBake']

_f = _n.native

_n.bind("CAD_NodeGraph", _c.c_int32, [_c.c_char_p, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_NodeGraphGetJson", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_NodeGraphGetKindsJson", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_NodeGraphSetJson", _c.c_int32, [_c.c_char_p])
_n.bind("CAD_NodeGraphClear", _c.c_int32, [])
_n.bind("CAD_NodeGraphEvaluate", _c.c_int32, [])
_n.bind("CAD_NodeGraphAddNode", _c.c_int32, [_c.c_char_p, _c.c_double, _c.c_double, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_NodeGraphRemoveNode", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_NodeGraphMoveNode", _c.c_int32, [_c.c_uint32, _c.c_double, _c.c_double])
_n.bind("CAD_NodeGraphConnect", _c.c_int32, [_c.c_uint32, _c.c_char_p, _c.c_uint32, _c.c_char_p])
_n.bind("CAD_NodeGraphDisconnect", _c.c_int32, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_NodeGraphSetNumber", _c.c_int32, [_c.c_uint32, _c.c_char_p, _c.c_double])
_n.bind("CAD_NodeGraphSetBool", _c.c_int32, [_c.c_uint32, _c.c_char_p, _c.c_bool])
_n.bind("CAD_NodeGraphSetText", _c.c_int32, [_c.c_uint32, _c.c_char_p, _c.c_char_p])
_n.bind("CAD_NodeGraphSetPoint", _c.c_int32, [_c.c_uint32, _c.c_char_p, CAD_GeVec3])
_n.bind("CAD_NodeGraphSetMuted", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool])
_n.bind("CAD_NodeGraphGetNodeObjects", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_NodeGraphBake", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.POINTER(_c.c_uint32), _c.c_uint32])


def CAD_NodeGraph(argsJson: str | None) -> str | None:
    """C: int32_t CAD_NodeGraph(const char* argsJson, char* buf, uint32_t capacity)

    한 창구 — {"op": …} JSON 을 받아 결과 JSON({"ok": true|false, "error": …, …})을 돌려준다. MCP node_graph·그래프 칸과 같은 연산:
    status · kinds · evaluate · clear · set{graph} · add_node{kind,x,y,params} · remove_node{id} · move_node{id,x,y} ·
    connect{from,fromPort,to,toPort} · disconnect{to,toPort} · set_param{id,port,value} · mute{ids,on} · copy{ids} · paste{clip,dx,dy} · bake{ids}.
    반환 = 결과 글자 길이(NUL 제외). 같은 인자로 길이를 먼저 묻고 다시 불러도 한 번만 실행한다. "ok": false 여도 반환은 길이(이유는 결과의 error).
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_NodeGraph(_n.text(argsJson), _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_NodeGraphGetJson() -> str | None:
    """C: int32_t CAD_NodeGraphGetJson(char* buf, uint32_t capacity)

    상태 JSON — graph(nodes·links, 노드마다 outputs·sceneIds·error) · errors · objects(그래프가 가진 장면 객체) · evaluations · pending · timings(노드 ms).
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_NodeGraphGetJson(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_NodeGraphGetKindsJson() -> str | None:
    """C: int32_t CAD_NodeGraphGetKindsJson(char* buf, uint32_t capacity)

    노드 종류 목록 JSON — [{kind, group, inputs:[{name,type,default,min,max}], outputs:[{name,type}]}]. type = number·integer·bool·text·point·objects.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_NodeGraphGetKindsJson(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_NodeGraphSetJson(graphJson: str | None) -> int:
    """C: CAD_Status CAD_NodeGraphSetJson(const char* graphJson)

    그래프 통째로 바꾸기(CAD_NodeGraphGetJson 의 graph 와 같은 모양). 모르는 종류의 노드는 건너뛰고 이유는 CAD_GetLastError 에 남긴다(CAD_OK).
    """
    return _f.CAD_NodeGraphSetJson(_n.text(graphJson))


def CAD_NodeGraphClear() -> int:
    """C: CAD_Status CAD_NodeGraphClear(void)

    그래프 통째로 바꾸기(CAD_NodeGraphGetJson 의 graph 와 같은 모양). 모르는 종류의 노드는 건너뛰고 이유는 CAD_GetLastError 에 남긴다(CAD_OK).
    """
    return _f.CAD_NodeGraphClear()


def CAD_NodeGraphEvaluate() -> int:
    """C: int32_t CAD_NodeGraphEvaluate(void)

    지금 계산 — 반환 = 오류 난 노드 수(0 = 다 됨), 음수 = 오류. 노드마다 이유는 CAD_NodeGraphGetJson 의 errors.
    """
    return _f.CAD_NodeGraphEvaluate()


def CAD_NodeGraphAddNode(kind: str | None, x: float, y: float) -> tuple[int, int]:
    """C: CAD_Status CAD_NodeGraphAddNode(const char* kind, double x, double y, uint32_t* outNodeId)

    노드 넣기 — 모르는 kind 는 CAD_E_NOT_FOUND. 입력 값은 CAD_NodeGraphSet* 로(안 넣으면 종류의 기본값).
    """
    outNodeId = _c.c_uint32()
    _r = _f.CAD_NodeGraphAddNode(_n.text(kind), x, y, _c.byref(outNodeId))
    return (_r, outNodeId.value)


def CAD_NodeGraphRemoveNode(nodeId: int) -> int:
    """C: CAD_Status CAD_NodeGraphRemoveNode(uint32_t nodeId)

    그 노드의 연결도 같이

    묶음 주석: 노드 넣기 — 모르는 kind 는 CAD_E_NOT_FOUND. 입력 값은 CAD_NodeGraphSet* 로(안 넣으면 종류의 기본값).
    """
    return _f.CAD_NodeGraphRemoveNode(nodeId)


def CAD_NodeGraphMoveNode(nodeId: int, x: float, y: float) -> int:
    """C: CAD_Status CAD_NodeGraphMoveNode(uint32_t nodeId, double x, double y)

    노드 넣기 — 모르는 kind 는 CAD_E_NOT_FOUND. 입력 값은 CAD_NodeGraphSet* 로(안 넣으면 종류의 기본값).
    """
    return _f.CAD_NodeGraphMoveNode(nodeId, x, y)


def CAD_NodeGraphConnect(fromNode: int, fromPort: str | None, toNode: int, toPort: str | None) -> int:
    """C: CAD_Status CAD_NodeGraphConnect(uint32_t fromNode, const char* fromPort, uint32_t toNode, const char* toPort)

    잇기 — from 노드의 출력 포트 → to 노드의 입력 포트(입력 하나엔 연결 하나 — 있던 것은 바뀐다). 없는 노드 CAD_E_BAD_HANDLE, 없는 포트 CAD_E_NOT_FOUND,
    형이 안 맞거나 고리가 생기면 CAD_E_CONFLICT(그대로).
    """
    return _f.CAD_NodeGraphConnect(fromNode, _n.text(fromPort), toNode, _n.text(toPort))


def CAD_NodeGraphDisconnect(toNode: int, toPort: str | None) -> int:
    """C: CAD_Status CAD_NodeGraphDisconnect(uint32_t toNode, const char* toPort)

    잇기 — from 노드의 출력 포트 → to 노드의 입력 포트(입력 하나엔 연결 하나 — 있던 것은 바뀐다). 없는 노드 CAD_E_BAD_HANDLE, 없는 포트 CAD_E_NOT_FOUND,
    형이 안 맞거나 고리가 생기면 CAD_E_CONFLICT(그대로).
    """
    return _f.CAD_NodeGraphDisconnect(toNode, _n.text(toPort))


def CAD_NodeGraphSetNumber(nodeId: int, port: str | None, value: float) -> int:
    """C: CAD_Status CAD_NodeGraphSetNumber(uint32_t nodeId, const char* port, double value)

    입력 값 — 포트 형에 맞는 것으로(number·integer 는 Number, 정수 포트는 반올림). 형이 다르거나 범위 밖이면 CAD_E_INVALID_ARG.
    """
    return _f.CAD_NodeGraphSetNumber(nodeId, _n.text(port), value)


def CAD_NodeGraphSetBool(nodeId: int, port: str | None, value: bool) -> int:
    """C: CAD_Status CAD_NodeGraphSetBool(uint32_t nodeId, const char* port, bool value)

    입력 값 — 포트 형에 맞는 것으로(number·integer 는 Number, 정수 포트는 반올림). 형이 다르거나 범위 밖이면 CAD_E_INVALID_ARG.
    """
    return _f.CAD_NodeGraphSetBool(nodeId, _n.text(port), value)


def CAD_NodeGraphSetText(nodeId: int, port: str | None, value: str | None) -> int:
    """C: CAD_Status CAD_NodeGraphSetText(uint32_t nodeId, const char* port, const char* value)

    입력 값 — 포트 형에 맞는 것으로(number·integer 는 Number, 정수 포트는 반올림). 형이 다르거나 범위 밖이면 CAD_E_INVALID_ARG.
    """
    return _f.CAD_NodeGraphSetText(nodeId, _n.text(port), _n.text(value))


def CAD_NodeGraphSetPoint(nodeId: int, port: str | None, value: CAD_GeVec3) -> int:
    """C: CAD_Status CAD_NodeGraphSetPoint(uint32_t nodeId, const char* port, CAD_GeVec3 value)

    입력 값 — 포트 형에 맞는 것으로(number·integer 는 Number, 정수 포트는 반올림). 형이 다르거나 범위 밖이면 CAD_E_INVALID_ARG.
    """
    return _f.CAD_NodeGraphSetPoint(nodeId, _n.text(port), value)


def CAD_NodeGraphSetMuted(nodeIds: Sequence | None, count: int, muted: bool) -> int:
    """C: CAD_Status CAD_NodeGraphSetMuted(const uint32_t* nodeIds, uint32_t count, bool muted)

    끄기·켜기(블렌더 Mute — 끈 노드는 계산하지 않고 입력을 그대로 넘기며, 끈 출력 노드는 장면에 아무것도 두지 않는다).
    """
    _a_nodeIds = _n.array(_c.c_uint32, nodeIds)
    return _f.CAD_NodeGraphSetMuted(_a_nodeIds, count, muted)


def CAD_NodeGraphGetNodeObjects(nodeId: int, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_NodeGraphGetNodeObjects(uint32_t nodeId, uint32_t* outIds, uint32_t capacity)

    출력 노드가 만든 장면 객체 id — 반환 = 개수(계산 전·출력 노드가 아니면 0).
    """
    return _f.CAD_NodeGraphGetNodeObjects(nodeId, outIds, capacity)


def CAD_NodeGraphBake(objectIds: Sequence | None, count: int, outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_NodeGraphBake(const uint32_t* objectIds, uint32_t count, uint32_t* outIds, uint32_t capacity)

    굽기 — objectIds(0 개 = 지금 선택)의 출력 객체를 그래프에서 떼어 보통 객체로(그 출력 노드는 지워진다, 객체 id 는 그대로).
    반환 = 떼어 낸 객체 수, outIds = 그 id. outIds = NULL·칸 모자람이면 아무것도 안 바꾸고 개수만. 그래프가 만든 객체가 없으면 CAD_E_NOT_FOUND.
    """
    _a_objectIds = _n.array(_c.c_uint32, objectIds)
    return _f.CAD_NodeGraphBake(_a_objectIds, count, outIds, capacity)
