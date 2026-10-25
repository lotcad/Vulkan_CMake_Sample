#pragma once
/* LotCAD C API - ai  [(AI / MCP)]
 * AI endpoint, requests, action JSON, MCP tools.
 * AI 연결·요청·액션 JSON·MCP 도구.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif
/* 새 규칙: CAD_Status(실패 이유 = CAD_GetLastError) · 글 함수 = int32_t 전체 길이(실패면 음수 CAD_E_*), 칸은 uint32_t.
 * 엔진 스레드에서만(아니면 CAD_E_WRONG_THREAD) — CAD_GetMcpToolsJson 만 엔진 없이도 된다. */

// ── AI ─────────────────────────────────────────────────────────────
enum {   /* CAD_AiGetStatus — 끝남·오류는 한 번만 알린다(읽으면 IDLE 로) */
    CAD_AI_IDLE  = 0,
    CAD_AI_BUSY  = 1,
    CAD_AI_DONE  = 2,
    CAD_AI_ERROR = 3
};
/* 엔드포인트 — 모바일은 원격 서버. url 예 "http://192.168.0.10:8080"(OpenAI 호환 /v1/chat/completions), model = 서버가 쓰는 이름(NULL = 안 보냄).
 * 설정 뒤 서버 확인에 1초쯤 — 준비 전 Submit 은 CAD_E_NOT_READY. 빈 url = CAD_E_INVALID_ARG */
CAD_API CAD_Status CAD_AiSetEndpoint(const char* url, const char* model);
/* 데스크톱 전용(helperAI llama-server) — 모바일 = CAD_E_NOT_SUPPORTED, 못 띄움 = CAD_E_FAILED + 이유 */
CAD_API CAD_Status CAD_AiStartLocalServer(void);
/* 비동기 요청 — 결과 액션은 다음 틱들에서 트랜잭션 하나로 적용(AI 창과 같음). 처리 중이거나 준비 전 = CAD_E_NOT_READY + 이유,
 * 빈 프롬프트 = CAD_E_INVALID_ARG, 이미지 파일이 없음 = CAD_E_NOT_FOUND */
CAD_API CAD_Status CAD_AiSubmit(const char* prompt);
CAD_API CAD_Status CAD_AiSubmitWithImage(const char* prompt, const char* imagePath);
CAD_API CAD_Status CAD_AiGetStatus(int32_t* outState);                    /* CAD_AI_* */
CAD_API int32_t    CAD_AiGetLastAnswer(char* buf, uint32_t capacity);      /* 모델의 답 문장(질문엔 액션 없이 이것만) — 반환 = 전체 길이 */
CAD_API int32_t    CAD_AiGetNotes(char* buf, uint32_t capacity);           /* 액션별 결과 줄(\n 구분) — 반환 = 전체 길이 */
CAD_API CAD_Status CAD_AiCancel(void);                                     /* 진행 중 답을 버리고 대기 액션도 지움 */
/* 동기 — 호스트가 자기 LLM(Claude API 등)으로 받은 액션 JSON(배열 또는 {"actions":[…]}, lot_ai_prompt.h 계약)을 바로.
 * MCP ai_actions 와 같은 처리 + 되돌리기 한 단계. 반환 = notes 전체 길이. 2회 호출(buf NULL 로 길이 → 버퍼)은 첫 호출에서 한 번만 실행하고,
 * 같은 프레임 같은 인자의 다음 호출엔 그 결과를 준다. JSON·액션이 틀림 = CAD_E_INVALID_ARG + 이유 */
CAD_API int32_t    CAD_RunAiActionsJson(const char* actionsJson, char* outNotes, uint32_t capacity);
/* MCP 도구를 TCP 없이 직접 — CAD_GetMcpToolsJson 짝. 결과 = MCP content JSON, 반환 = 전체 길이. 모르는 도구·틀린 인자 = CAD_E_INVALID_ARG.
 * 2회 호출은 한 번만 실행(위와 같음) */
CAD_API int32_t    CAD_McpCall(const char* toolName, const char* argsJson, char* buf, uint32_t capacity);

/* MCP 도구 목록(JSON 배열) — 엔진을 만들지 않아도 된다. LotCAD --mcp 브리지가 앱이 꺼져 있을 때 목록을 보여 주는 데 쓴다.
 * 반환 = 전체 길이 */
CAD_API int32_t    CAD_GetMcpToolsJson(char* buf, uint32_t capacity);

#ifdef __cplusplus
}
#endif
