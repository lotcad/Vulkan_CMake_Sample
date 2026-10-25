#pragma once
/* LotCAD C API - graph  [(node graph / blueprint)]
 * Build, edit and evaluate the node graph; output nodes make scene objects.
 * 노드 그래프(블루프린트) — 만들기·고치기·계산. 출력 노드가 장면 객체를 만든다.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h.
 *
 * 문서마다 그래프 하나. 노드 = 엔진 연산 하나(종류 목록은 CAD_NodeGraphGetKindsJson), 노드 id = 그래프 안 번호(uint32, 0 = 없음),
 * 포트 = 이름(UTF-8). 출력 노드는 계산할 때 장면 객체를 만들고, 입력이 바뀌면 같은 객체 id 로 다시 만든다(굽기 전엔 그래프가 주인).
 * 그래프를 바꾸는 함수는 되돌리기 한 단계. 바뀐 그래프는 다음 틱에 계산된다 — 바로 결과가 필요하면 CAD_NodeGraphEvaluate.
 * 좌표 값(Point 포트) = 월드 mm. 노드 자리(x, y) = 그래프 칸 좌표(장면과 무관). 엔진 스레드에서만. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif

/* 한 창구 — {"op": …} JSON 을 받아 결과 JSON({"ok": true|false, "error": …, …})을 돌려준다. MCP node_graph·그래프 칸과 같은 연산:
 * status · kinds · evaluate · clear · set{graph} · add_node{kind,x,y,params} · remove_node{id} · move_node{id,x,y} ·
 * connect{from,fromPort,to,toPort} · disconnect{to,toPort} · set_param{id,port,value} · mute{ids,on} · copy{ids} · paste{clip,dx,dy} · bake{ids}.
 * 반환 = 결과 글자 길이(NUL 제외). 같은 인자로 길이를 먼저 묻고 다시 불러도 한 번만 실행한다. "ok": false 여도 반환은 길이(이유는 결과의 error). */
CAD_API int32_t    CAD_NodeGraph(const char* argsJson, char* buf, uint32_t capacity);

/* 상태 JSON — graph(nodes·links, 노드마다 outputs·sceneIds·error) · errors · objects(그래프가 가진 장면 객체) · evaluations · pending · timings(노드 ms). */
CAD_API int32_t    CAD_NodeGraphGetJson(char* buf, uint32_t capacity);
/* 노드 종류 목록 JSON — [{kind, group, inputs:[{name,type,default,min,max}], outputs:[{name,type}]}]. type = number·integer·bool·text·point·objects. */
CAD_API int32_t    CAD_NodeGraphGetKindsJson(char* buf, uint32_t capacity);
/* 그래프 통째로 바꾸기(CAD_NodeGraphGetJson 의 graph 와 같은 모양). 모르는 종류의 노드는 건너뛰고 이유는 CAD_GetLastError 에 남긴다(CAD_OK). */
CAD_API CAD_Status CAD_NodeGraphSetJson(const char* graphJson);
CAD_API CAD_Status CAD_NodeGraphClear(void);
/* 지금 계산 — 반환 = 오류 난 노드 수(0 = 다 됨), 음수 = 오류. 노드마다 이유는 CAD_NodeGraphGetJson 의 errors. */
CAD_API int32_t    CAD_NodeGraphEvaluate(void);

/* 노드 넣기 — 모르는 kind 는 CAD_E_NOT_FOUND. 입력 값은 CAD_NodeGraphSet* 로(안 넣으면 종류의 기본값). */
CAD_API CAD_Status CAD_NodeGraphAddNode(const char* kind, double x, double y, uint32_t* outNodeId);
CAD_API CAD_Status CAD_NodeGraphRemoveNode(uint32_t nodeId);   /* 그 노드의 연결도 같이 */
CAD_API CAD_Status CAD_NodeGraphMoveNode(uint32_t nodeId, double x, double y);
/* 잇기 — from 노드의 출력 포트 → to 노드의 입력 포트(입력 하나엔 연결 하나 — 있던 것은 바뀐다). 없는 노드 CAD_E_BAD_HANDLE, 없는 포트 CAD_E_NOT_FOUND,
 * 형이 안 맞거나 고리가 생기면 CAD_E_CONFLICT(그대로). */
CAD_API CAD_Status CAD_NodeGraphConnect(uint32_t fromNode, const char* fromPort, uint32_t toNode, const char* toPort);
CAD_API CAD_Status CAD_NodeGraphDisconnect(uint32_t toNode, const char* toPort);
/* 입력 값 — 포트 형에 맞는 것으로(number·integer 는 Number, 정수 포트는 반올림). 형이 다르거나 범위 밖이면 CAD_E_INVALID_ARG. */
CAD_API CAD_Status CAD_NodeGraphSetNumber(uint32_t nodeId, const char* port, double value);
CAD_API CAD_Status CAD_NodeGraphSetBool(uint32_t nodeId, const char* port, bool value);
CAD_API CAD_Status CAD_NodeGraphSetText(uint32_t nodeId, const char* port, const char* value);
CAD_API CAD_Status CAD_NodeGraphSetPoint(uint32_t nodeId, const char* port, CAD_GeVec3 value);
/* 끄기·켜기(블렌더 Mute — 끈 노드는 계산하지 않고 입력을 그대로 넘기며, 끈 출력 노드는 장면에 아무것도 두지 않는다). */
CAD_API CAD_Status CAD_NodeGraphSetMuted(const uint32_t* nodeIds, uint32_t count, bool muted);

/* 출력 노드가 만든 장면 객체 id — 반환 = 개수(계산 전·출력 노드가 아니면 0). */
CAD_API int32_t    CAD_NodeGraphGetNodeObjects(uint32_t nodeId, uint32_t* outIds, uint32_t capacity);
/* 굽기 — objectIds(0 개 = 지금 선택)의 출력 객체를 그래프에서 떼어 보통 객체로(그 출력 노드는 지워진다, 객체 id 는 그대로).
 * 반환 = 떼어 낸 객체 수, outIds = 그 id. outIds = NULL·칸 모자람이면 아무것도 안 바꾸고 개수만. 그래프가 만든 객체가 없으면 CAD_E_NOT_FOUND. */
CAD_API int32_t    CAD_NodeGraphBake(const uint32_t* objectIds, uint32_t count, uint32_t* outIds, uint32_t capacity);

#ifdef __cplusplus
}
#endif
