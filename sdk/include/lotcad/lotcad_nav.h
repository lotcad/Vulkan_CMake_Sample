#pragma once
/* LotCAD C API - nav  [(navigation / external link)]
 * Path driving agents, TCP link, external poses.
 * 경로 주행·외부 연결(TCP)·외부 자세.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif
/* ── 외부 연결(link) — 태그 추적 스크립트·로봇·머리 추적 같은 바깥 프로세스가 붙는 TCP 문 ───────────────────
 * 127.0.0.1:port 에서 듣고, 줄 하나 = JSON 객체 하나("\n" 구분). 처리는 엔진 메인 스레드(다음 tick)에서.
 *   {"type":"pose","id":"기둥A"|12,"x":..,"y":..,"yaw":90,"mode":"clamp"|"twin"}
 *       id 는 객체 이름 또는 번호. (x,y) = 객체의 **월드 경계 중심**(원점 아님), 단위 = 도면 단위(mm). z 는 그대로.
 *       yaw 는 도, 0 = +Y, 시계 방향 양수(내비 규약). 생략하면 향 유지.
 *       mode 생략 시 CAD_LinkStart 의 clamp. clamp = 벽(다른 메시)에 막히면 벽 앞에 선다(도면이 진실),
 *       twin = 그대로 비춘다(현실이 진실). 직전 위치와의 속도가 몸 크기의 0.3배/초를 넘으면 걷기 애니가 켜지고,
 *       0.5초 동안 소식이 없으면 꺼진다.
 *   {"type":"ping"}  →  엔진이 {"type":"pong"} 을 되돌린다.
 * 명령행 `link [on|off|port N|clamp|twin]` 과 같은 것. 파이썬 예: tools/tag_tracker.py(AprilTag), tools/fake_pose.py.
 * 로컬 전용 — 원격·토큰은 없다. */
CAD_API bool     CAD_LinkStart(int port, bool clamp);       /* port 0 = 빈 포트를 고름(CAD_LinkPort 로 확인). 실패 false + CAD_GetLastError */
CAD_API void     CAD_LinkStop(void);
CAD_API int      CAD_LinkPort(void);                         /* 0 = 닫힘 */
CAD_API bool     CAD_LinkSend(const char* jsonLine);         /* 붙은 클라이언트 전부에 한 줄(끝에 "\n" 붙임). 접속 없으면 false */
/* 소켓 없이 호스트가 직접 위치를 넣는다(iOS ARKit·자체 추적기). pose 메시지와 같은 규약. yawDeg 에 NaN 을 주면 향 유지.
 * 반환 = 적용됨. outBlocked 는 clamp 로 벽에 막혔는가(NULL 가능). */
CAD_API bool     CAD_ApplyExternalPose(uint32_t id, float x, float y, float yawDeg, bool clamp, bool* outBlocked);

// ── 내비(경로 주행) — 패널·마우스 없이. 패널과 같은 규약: agentId 0 = 체크된 것 전부(없으면 고른 줄).
//   agentId = 대상의 대표 객체 id(차체·바퀴처럼 조각 모델은 가장 큰 조각). 단위 = 장면 단위(m 장면이면 m, mm 도면이면 mm).
// 지도 — paramsJson: {"cellSize","agentRadius","minZ","maxZ","margin","maxCells"} 중 준 키만 자동값 위에 덮음. NULL/"" = 자동.
CAD_API bool     CAD_NavBuildMap(const char* paramsJson);
CAD_API void     CAD_NavShowGrid(bool on);
// 대상 — 장면 객체를 주행 대상으로. 반환 agentId(0 실패). 자동 수집(뼈·바퀴 클립)된 대상도 Remove/Clear 하면 다시 안 들어온다.
CAD_API uint32_t CAD_NavAddAgent(uint32_t objectId, bool isVehicle);
CAD_API uint32_t CAD_NavAddSelected(void);                 // 반환 = 추가된 수
CAD_API bool     CAD_NavRemoveAgent(uint32_t agentId);
CAD_API void     CAD_NavClearAgents(void);
// {"speed","scanRange","radius"(0=자동),"showRays","checked","isVehicle"} 중 준 키만.
CAD_API bool     CAD_NavSetAgentParams(uint32_t agentId, const char* json);
// 목적지 — 경로 계획까지(출발은 Start). 길이 없으면 false + CAD_GetLastError.
CAD_API bool     CAD_NavSetGoal(uint32_t agentId, float x, float y, float z);
CAD_API bool     CAD_NavStart(uint32_t agentId);
CAD_API bool     CAD_NavStop(uint32_t agentId);
CAD_API bool     CAD_NavReset(uint32_t agentId);          // 정지·경로 삭제·출발 자리로
// {"grid":{"ready","showing","w","h","cellSize","origin","blockedCells","totalCells"},"activeAgent",
//  "agents":[{"agentId","name","isVehicle","checked","active","hasGoal","goal","driving","pathPoints","pathIndex","pathLength",
//             "position"(몸통 중심),"yaw"(도, 0=+Y 시계 — CAD_ApplyExternalPose 와 같음),"arrived","speed","scanRange","radius","showRays"}]}
CAD_API int      CAD_NavGetStateJson(char* out, int cap);
// 경로 점 [x,y] × n — 반환 = 점 수(outXY NULL/cap 0 이면 개수만, 2회 호출). cap = 점 개수 단위(배열은 float cap×2 칸).
CAD_API uint32_t CAD_NavGetPath(uint32_t agentId, float* outXY, uint32_t cap);

#ifdef __cplusplus
}
#endif
