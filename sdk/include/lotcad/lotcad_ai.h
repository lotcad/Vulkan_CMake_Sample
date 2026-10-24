#pragma once
/* LotCAD C API - ai  [(AI / MCP)]
 * AI endpoint, requests, action JSON, MCP tools.
 * AI 연결·요청·액션 JSON·MCP 도구.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif
// ── AI ─────────────────────────────────────────────────────────────
// 엔드포인트 — 모바일은 원격 서버. url 예 "http://192.168.0.10:8080"(OpenAI 호환 /v1/chat/completions), model = 서버가 쓰는 이름(NULL = 안 보냄).
//   설정 뒤 서버 확인에 1초쯤 — 준비 전 Submit 은 false + CAD_GetLastError.
CAD_API bool CAD_AiSetEndpoint(const char* url, const char* model);
CAD_API bool CAD_AiStartLocalServer(void);        // 데스크톱 전용(helperAI llama-server), 모바일 false + GetLastError
// 비동기 요청 — 결과 액션은 다음 틱들에서 트랜잭션 하나로 적용(AI 창과 같음). 처리 중이거나 준비 전이면 false.
CAD_API bool CAD_AiSubmit(const char* prompt);
CAD_API bool CAD_AiSubmitWithImage(const char* prompt, const char* imagePath);
CAD_API int  CAD_AiGetStatus(void);               // 0 idle 1 busy 2 done 3 error (2·3 은 한 번만)
CAD_API int  CAD_AiGetLastAnswer(char* out, int cap);   // 모델의 답 문장(질문엔 액션 없이 이것만)
CAD_API int  CAD_AiGetNotes(char* out, int cap);        // 액션별 결과 줄(\n 구분)
CAD_API void CAD_AiCancel(void);                  // 진행 중 답을 버리고 대기 액션도 지움
// 동기 — 호스트가 자기 LLM(Claude API 등)으로 받은 액션 JSON(배열 또는 {"actions":[…]}, lot_ai_prompt.h 계약)을 바로.
//   MCP ai_actions 와 같은 처리 + 되돌리기 한 단계. 반환 = notes 길이(2회 호출 — 길이만 묻는 첫 호출에서 한 번 실행, 같은 프레임 같은 인자의 다음 호출은 그 결과), 실패 -1 + GetLastError.
CAD_API int  CAD_RunAiActionsJson(const char* actionsJson, char* outNotes, int cap);
// MCP 도구를 TCP 없이 직접 — CAD_GetMcpToolsJson 짝. 결과 = MCP content JSON. 실패 -1. 2회 호출은 한 번만 실행(위와 같음).
CAD_API int  CAD_McpCall(const char* toolName, const char* argsJson, char* out, int cap);

/* MCP 도구 목록(JSON 배열) — 엔진을 만들지 않아도 된다. LotCAD --mcp 브리지가 앱이 꺼져 있을 때 목록을 보여 주는 데 쓴다.
 * 반환 = 길이, 실패 -1. */
CAD_API int      CAD_GetMcpToolsJson(char* outUtf8, int cap);

#ifdef __cplusplus
}
#endif
