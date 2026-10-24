# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — AI 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_AiSetEndpoint', 'CAD_AiStartLocalServer', 'CAD_AiSubmit', 'CAD_AiSubmitWithImage', 'CAD_AiGetStatus', 'CAD_AiGetLastAnswer', 'CAD_AiGetNotes', 'CAD_AiCancel', 'CAD_RunAiActionsJson', 'CAD_McpCall', 'CAD_GetMcpToolsJson']

_f = _n.native

_n.bind("CAD_AiSetEndpoint", _c.c_bool, [_c.c_char_p, _c.c_char_p])
_n.bind("CAD_AiStartLocalServer", _c.c_bool, [])
_n.bind("CAD_AiSubmit", _c.c_bool, [_c.c_char_p])
_n.bind("CAD_AiSubmitWithImage", _c.c_bool, [_c.c_char_p, _c.c_char_p])
_n.bind("CAD_AiGetStatus", _c.c_int, [])
_n.bind("CAD_AiGetLastAnswer", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_AiGetNotes", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_AiCancel", None, [])
_n.bind("CAD_RunAiActionsJson", _c.c_int, [_c.c_char_p, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_McpCall", _c.c_int, [_c.c_char_p, _c.c_char_p, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetMcpToolsJson", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])


def CAD_AiSetEndpoint(url: str | None, model: str | None) -> bool:
    """C: bool CAD_AiSetEndpoint(const char* url, const char* model)

    엔드포인트 — 모바일은 원격 서버. url 예 "http://192.168.0.10:8080"(OpenAI 호환 /v1/chat/completions), model = 서버가 쓰는 이름(NULL = 안 보냄).
    설정 뒤 서버 확인에 1초쯤 — 준비 전 Submit 은 false + CAD_GetLastError.
    """
    return _f.CAD_AiSetEndpoint(_n.text(url), _n.text(model))


def CAD_AiStartLocalServer() -> bool:
    """C: bool CAD_AiStartLocalServer(void)

    데스크톱 전용(helperAI llama-server), 모바일 false + GetLastError

    묶음 주석: 엔드포인트 — 모바일은 원격 서버. url 예 "http://192.168.0.10:8080"(OpenAI 호환 /v1/chat/completions), model = 서버가 쓰는 이름(NULL = 안 보냄).
    설정 뒤 서버 확인에 1초쯤 — 준비 전 Submit 은 false + CAD_GetLastError.
    """
    return _f.CAD_AiStartLocalServer()


def CAD_AiSubmit(prompt: str | None) -> bool:
    """C: bool CAD_AiSubmit(const char* prompt)

    비동기 요청 — 결과 액션은 다음 틱들에서 트랜잭션 하나로 적용(AI 창과 같음). 처리 중이거나 준비 전이면 false.
    """
    return _f.CAD_AiSubmit(_n.text(prompt))


def CAD_AiSubmitWithImage(prompt: str | None, imagePath: str | None) -> bool:
    """C: bool CAD_AiSubmitWithImage(const char* prompt, const char* imagePath)

    비동기 요청 — 결과 액션은 다음 틱들에서 트랜잭션 하나로 적용(AI 창과 같음). 처리 중이거나 준비 전이면 false.
    """
    return _f.CAD_AiSubmitWithImage(_n.text(prompt), _n.text(imagePath))


def CAD_AiGetStatus() -> int:
    """C: int CAD_AiGetStatus(void)

    0 idle 1 busy 2 done 3 error (2·3 은 한 번만)

    묶음 주석: 비동기 요청 — 결과 액션은 다음 틱들에서 트랜잭션 하나로 적용(AI 창과 같음). 처리 중이거나 준비 전이면 false.
    """
    return _f.CAD_AiGetStatus()


def CAD_AiGetLastAnswer() -> str | None:
    """C: int CAD_AiGetLastAnswer(char* out, int cap)

    모델의 답 문장(질문엔 액션 없이 이것만)

    묶음 주석: 비동기 요청 — 결과 액션은 다음 틱들에서 트랜잭션 하나로 적용(AI 창과 같음). 처리 중이거나 준비 전이면 false.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_AiGetLastAnswer(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_AiGetNotes() -> str | None:
    """C: int CAD_AiGetNotes(char* out, int cap)

    액션별 결과 줄(\\n 구분)

    묶음 주석: 비동기 요청 — 결과 액션은 다음 틱들에서 트랜잭션 하나로 적용(AI 창과 같음). 처리 중이거나 준비 전이면 false.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_AiGetNotes(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_AiCancel() -> None:
    """C: void CAD_AiCancel(void)

    진행 중 답을 버리고 대기 액션도 지움

    묶음 주석: 비동기 요청 — 결과 액션은 다음 틱들에서 트랜잭션 하나로 적용(AI 창과 같음). 처리 중이거나 준비 전이면 false.
    """
    _f.CAD_AiCancel()


def CAD_RunAiActionsJson(actionsJson: str | None) -> str | None:
    """C: int CAD_RunAiActionsJson(const char* actionsJson, char* outNotes, int cap)

    동기 — 호스트가 자기 LLM(Claude API 등)으로 받은 액션 JSON(배열 또는 {"actions":[…]}, lot_ai_prompt.h 계약)을 바로.
    MCP ai_actions 와 같은 처리 + 되돌리기 한 단계. 반환 = notes 길이(2회 호출 — 길이만 묻는 첫 호출에서 한 번 실행, 같은 프레임 같은 인자의 다음 호출은 그 결과), 실패 -1 + GetLastError.
    """
    _need = _f.CAD_RunAiActionsJson(_n.text(actionsJson), None, 0)   # 2회 호출 규약: 길이를 물으며 한 번 실행
    if _need < 0:
        return None
    _cap = _need + 1
    _buf = _c.create_string_buffer(_cap)
    if _f.CAD_RunAiActionsJson(_n.text(actionsJson), _buf, _cap) < 0:   # 같은 인자 → 다시 실행하지 않고 결과만
        return None
    return _n.decode(_buf.value)


def CAD_McpCall(toolName: str | None, argsJson: str | None) -> str | None:
    """C: int CAD_McpCall(const char* toolName, const char* argsJson, char* out, int cap)

    MCP 도구를 TCP 없이 직접 — CAD_GetMcpToolsJson 짝. 결과 = MCP content JSON. 실패 -1. 2회 호출은 한 번만 실행(위와 같음).
    """
    _need = _f.CAD_McpCall(_n.text(toolName), _n.text(argsJson), None, 0)   # 2회 호출 규약: 길이를 물으며 한 번 실행
    if _need < 0:
        return None
    _cap = _need + 1
    _buf = _c.create_string_buffer(_cap)
    if _f.CAD_McpCall(_n.text(toolName), _n.text(argsJson), _buf, _cap) < 0:   # 같은 인자 → 다시 실행하지 않고 결과만
        return None
    return _n.decode(_buf.value)


def CAD_GetMcpToolsJson() -> str | None:
    """C: int CAD_GetMcpToolsJson(char* outUtf8, int cap)

    MCP 도구 목록(JSON 배열) — 엔진을 만들지 않아도 된다. LotCAD --mcp 브리지가 앱이 꺼져 있을 때 목록을 보여 주는 데 쓴다.
    반환 = 길이, 실패 -1.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetMcpToolsJson(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)
