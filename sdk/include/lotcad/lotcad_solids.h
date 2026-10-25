#pragma once
/* LotCAD C API - solids  [AcDb3dSolid / AcBr (B-Rep)]
 * Primitives (create), shell/fillet, booleans, interference, exploded view, feature dimensions, B-Rep features and faces.
 * 기본 도형·B-Rep 피처와 면·불리언·필렛·간섭·분해도.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"
#include "lotcad_geometry.h"   /* CAD_GeVec3 */

#ifdef __cplusplus
extern "C" {
#endif
/* ── 솔리드 만들기 (AcDb3dSolid createBox · createWedge · createSphere … · extrude · sweep · revolve · loft) ─────────────
 * 규칙(lotcad_types.h): 반환 CAD_Status, 새 객체 id 는 outId, 좌표 = 월드 mm(CAD_GeVec3), opt = CAD_CreateOptions(NULL = 지금 도면층·기본 색).
 * 크기 0·음수 = CAD_E_INVALID_ARG, 없는 단면·경로 = CAD_E_BAD_HANDLE, 그 종류가 아님 = CAD_E_WRONG_TYPE. 만들기 한 번 = 되돌리기 1. 엔진 스레드에서만. */
/* 상자 — center = 상자 가운데, size = 가로·세로·높이(월드 X·Y·Z) */
CAD_API CAD_Status CAD_CreateBox(CAD_GeVec3 center, CAD_GeVec3 size, const CAD_CreateOptions* opt, uint32_t* outId);
/* 아래는 base = 밑면 가운데(구·토러스는 바닥에 닿는 점), 축 = +Z.
 *   쐐기 size = 밑면 가로·세로·높이 / 피라미드 외접 반지름·높이·변 수(3~64)·윗면 반지름(0 = 뾰족) / 관 바깥·안 반지름(안 < 바깥)·높이 */
CAD_API CAD_Status CAD_CreateWedge(CAD_GeVec3 base, CAD_GeVec3 size, const CAD_CreateOptions* opt, uint32_t* outId);
CAD_API CAD_Status CAD_CreatePyramid(CAD_GeVec3 base, double radius, double height, int32_t sides, double topRadius,
                                     const CAD_CreateOptions* opt, uint32_t* outId);
CAD_API CAD_Status CAD_CreateSphere(CAD_GeVec3 base, double radius, const CAD_CreateOptions* opt, uint32_t* outId);
CAD_API CAD_Status CAD_CreateCylinder(CAD_GeVec3 base, double radius, double height, const CAD_CreateOptions* opt, uint32_t* outId);
CAD_API CAD_Status CAD_CreateCone(CAD_GeVec3 base, double radius, double height, const CAD_CreateOptions* opt, uint32_t* outId);
CAD_API CAD_Status CAD_CreateTorus(CAD_GeVec3 base, double majorRadius, double minorRadius, const CAD_CreateOptions* opt, uint32_t* outId);   /* minor < major */
CAD_API CAD_Status CAD_CreateTube(CAD_GeVec3 base, double outerRadius, double innerRadius, double height, const CAD_CreateOptions* opt,
                                  uint32_t* outId);
/* 돌출 — 닫힌 단면(사각형·원·닫힌 폴리선) id 를 그 평면 법선 쪽으로 height. B-Rep 피처라 단면을 고치면 다시 만들어진다 */
CAD_API CAD_Status CAD_CreateExtrude(uint32_t profileId, double height, const CAD_CreateOptions* opt, uint32_t* outId);
/* 스윕 — 닫힌 단면 id 를 열린 경로(폴리선·선) id 를 따라 쓸어 솔리드. 단면은 경로 시작점으로 옮겨지고 경로 방향에 맞게 돌려진다 */
CAD_API CAD_Status CAD_Sweep(uint32_t profileId, uint32_t pathId, const CAD_CreateOptions* opt, uint32_t* outId);
/* 회전체 — 단면 스케치 id 를 axisStart → axisEnd 둘레로 360°, segments 분할(0 = 32). 스윕처럼 피처 기록이 남아 단면을 고치면 다시 만든다 */
CAD_API CAD_Status CAD_Revolve(uint32_t profileId, CAD_GeVec3 axisStart, CAD_GeVec3 axisEnd, int32_t segments, const CAD_CreateOptions* opt,
                               uint32_t* outId);
/* 로프트 — 닫힌 단면 id 들(2개 이상)을 **준 차례대로** 이어 솔리드. 닫히지 않은 단면 = CAD_E_NOT_CLOSED */
CAD_API CAD_Status CAD_Loft(const uint32_t* sectionIds, uint32_t count, const CAD_CreateOptions* opt, uint32_t* outId);

/* ── 고른 면 하나 (하위 객체 선택 — CAD_SetSubobjectSelectionMode 로 면 모드에서 고른 면) ──
 * PushPull = 법선 방향으로 distance(mm, 양수 = 바깥) 밀기, Inset = 평면 볼록 면 안쪽에 distance 폭 링(0 = 자동).
 * 고른 면이 없거나 안 되는 면이면 CAD_E_FAILED + 이유. 되돌리기 1 */
CAD_API CAD_Status CAD_PushPullSelectedFace(double distance);
CAD_API CAD_Status CAD_InsetSelectedFace(double distance);

/* ── B-Rep 솔리드 — 정보·면·돌출 컷·보스 (AcDb3dSolid · AcBr) ─────────────────────────────
 * 상자·원기둥·돌출·구·원뿔·토러스·회전체·스윕은 B-Rep 정의를 들고 있다(가져온 메시·불리언 결과는 아님 = CAD_E_WRONG_TYPE).
 * 크기를 읽고 고치는 것은 피처 치수(CAD_Get/SetFeatureDimension — 월드 mm). 좌표·길이는 늘 **월드** mm(객체의 이동·회전·축척이 걸린 자리) —
 * 엔진이 객체 로컬로 옮겨 넣는다. 바꾸는 함수는 되돌리기 1, 모양을 못 만들면(외곽에 닿는 컷 …) CAD_E_FAILED 이고 아무것도 안 바뀐다.
 * 컷·보스는 돌출(featureType 2) 솔리드에만. 번호(cutIndex·bossIndex) 밖 = CAD_E_OUT_OF_RANGE. */
enum { CAD_MAX_BREP_PROFILE_POINTS = 2048 };   /* 컷·보스 단면 점 수 상한 */
/* featureType: 0=상자 1=원기둥 2=돌출 3=구 4=원뿔 5=토러스 6=회전체 7=스윕 8=본체만(STEP). 부피·넓이 = 월드(mm³·mm²).
 * 출력 구조체 — 부르는 쪽이 size = sizeof 를 채운다(엔진은 그 크기까지만 쓴다) */
typedef struct CAD_BRepInfo {
    uint32_t size;
    int32_t featureType;
    uint32_t vertexCount;
    uint32_t edgeCount;
    uint32_t faceCount;
    double volume;
    double surfaceArea;
} CAD_BRepInfo;
CAD_API CAD_Status CAD_GetBRepInfo(uint32_t id, CAD_BRepInfo* outInfo);
/* 면 하나(안정된 면 번호 — 밀어도 번호가 그대로). surfaceType 0 = 평면, 1 = 원통. origin·normal = 월드. 출력 구조체(첫 칸 size) */
typedef struct CAD_BRepFaceInfo {
    uint32_t size;
    uint32_t faceId;
    int32_t surfaceType;
    CAD_GeVec3 origin;
    CAD_GeVec3 normal;
} CAD_BRepFaceInfo;
CAD_API CAD_Status CAD_GetBRepFaceInfo(uint32_t id, uint32_t faceId, CAD_BRepFaceInfo* outInfo);
/* 면 밀기 — distance(mm) 만큼 바깥으로. 상자 평면은 반대편 고정, 원통 옆면은 반지름, 돌출 옆면은 단면 변 평행 이동 */
CAD_API CAD_Status CAD_PushPullBRepFace(uint32_t id, uint32_t faceId, double distance);
/* 돌출 컷 — 닫힌 단면 점(월드, 3..CAD_MAX_BREP_PROFILE_POINTS)을 캡과 나란한 평면에 둔다(엔진이 아래 기준면으로 투영). throughAll = 관통(depth 무시).
 * FromSketch = 닫힌 스케치(사각형·원·닫힌 폴리선) id 로 — 피처 기록이 남아 스케치를 고치면 컷도 다시 만든다 */
CAD_API CAD_Status CAD_CutExtrudeBRep(uint32_t id, const CAD_GeVec3* profile, uint32_t count, double depth, bool throughAll);
CAD_API CAD_Status CAD_CutExtrudeFromSketch(uint32_t id, uint32_t sketchId, double depth, bool throughAll);
/* 보스(더하는 돌출) — height > 0 = 위 캡에서 위로, < 0 = 아래 캡에서 아래로(월드 mm). 발자국이 외곽에 닿거나 같은 쪽 보스와 겹치면 CAD_E_FAILED.
 * FromSketch = 스케치가 가까운 캡 쪽으로 height(양수) */
CAD_API CAD_Status CAD_BossExtrudeBRep(uint32_t id, const CAD_GeVec3* profile, uint32_t count, double height);
CAD_API CAD_Status CAD_BossExtrudeFromSketch(uint32_t id, uint32_t sketchId, double height);
CAD_API int32_t    CAD_GetBRepBossCount(uint32_t id);
CAD_API CAD_Status CAD_GetBRepBossHeight(uint32_t id, uint32_t bossIndex, double* outHeight);   /* 부호 = 위/아래 */
CAD_API CAD_Status CAD_SetBRepBossHeight(uint32_t id, uint32_t bossIndex, double height);
/* 컷 하나 — depth = 월드 mm(관통이면 의미 없음), pointCount = 단면 점 수. 출력 구조체(첫 칸 size) */
typedef struct CAD_BRepCutInfo {
    uint32_t size;
    uint32_t cutIndex;
    uint32_t pointCount;
    double depth;
    bool throughAll;
} CAD_BRepCutInfo;
CAD_API int32_t    CAD_GetBRepCutCount(uint32_t id);
CAD_API CAD_Status CAD_GetBRepCutInfo(uint32_t id, uint32_t cutIndex, CAD_BRepCutInfo* outInfo);
/* 컷 단면 점(월드) — 반환 = 점 수, capacity 만큼 채운다 */
CAD_API int32_t    CAD_GetBRepCutProfile(uint32_t id, uint32_t cutIndex, CAD_GeVec3* outPoints, uint32_t capacity);
/* 컷 바꾸기 — 단면(월드)·깊이·관통을 통째로, 또는 닫힌 스케치로 */
CAD_API CAD_Status CAD_SetBRepCut(uint32_t id, uint32_t cutIndex, const CAD_GeVec3* profile, uint32_t count, double depth, bool throughAll);
CAD_API CAD_Status CAD_SetBRepCutFromSketch(uint32_t id, uint32_t cutIndex, uint32_t sketchId, double depth, bool throughAll);
/* 컷·보스 지우기(솔리드웍스 피처 삭제처럼) — 여러 개를 한 번에 빼고 남은 것으로 한 번 다시 만든다. 그 피처만 쓰던 스케치도 지운다.
 * 번호는 지우기 전 번호(지운 뒤엔 뒤쪽이 당겨진다). 되돌리기 1. 남은 것으로 모양을 못 만들면(보스를 지워 그 안 컷이 허공에 남음 …) CAD_E_FAILED */
CAD_API CAD_Status CAD_RemoveBRepFeatures(uint32_t id, const uint32_t* cutIndices, uint32_t cutCount, const uint32_t* bossIndices,
                                          uint32_t bossCount);
CAD_API CAD_Status CAD_RemoveBRepCut(uint32_t id, uint32_t cutIndex);     /* 하나만 — CAD_RemoveBRepFeatures 와 같다 */
CAD_API CAD_Status CAD_RemoveBRepBoss(uint32_t id, uint32_t bossIndex);
/* 원통 타공 기록 — B-Rep 기준체에서 원통 커터를 뺀 차집합 결과가 남긴 구멍. center·axis = 월드, radius·height = 월드 mm.
 * 축에 수직한 두 방향 축척이 다른 객체의 Set = CAD_E_NOT_SUPPORTED(반지름이 하나로 안 정해짐). 출력 구조체(첫 칸 size) */
typedef struct CAD_BooleanCylinderCutInfo {
    uint32_t size;
    uint32_t cutIndex;
    CAD_GeVec3 center;
    CAD_GeVec3 axis;
    double radius;
    double height;
} CAD_BooleanCylinderCutInfo;
CAD_API int32_t    CAD_GetBooleanCylinderCutCount(uint32_t id);
CAD_API CAD_Status CAD_GetBooleanCylinderCutInfo(uint32_t id, uint32_t cutIndex, CAD_BooleanCylinderCutInfo* outInfo);
CAD_API CAD_Status CAD_SetBooleanCylinderCut(uint32_t id, uint32_t cutIndex, CAD_GeVec3 center, CAD_GeVec3 axis, double radius, double height);
/* 화면 메시를 B-Rep 정의로 다시 — 곡면 분할 3..512(밖이면 그 끝으로) */
CAD_API CAD_Status CAD_RebuildBRepMesh(uint32_t id, uint32_t curvedSegments);

/* ── 솔리드 가공 — 대상 id 배열(AcDb3dSolid shell · filletEdges · chamferEdges) ──
 * 입력을 먼저 전부 본다 — 없는 id·잠긴 도면층·솔리드(메시) 아님·같은 id 두 번이 하나라도 있으면, 또 하나라도 가공이 안 먹으면 **아무것도 바꾸지 않는다**.
 * 반환 = 결과 객체 수, outIds 에 capacity 만큼. outIds = NULL(칸 0)이거나 칸이 모자라면 해 본 뒤 물려 개수만(아무것도 안 남김). 되돌리기 1. */
/* 셸 — 속을 비워 두께만 남긴다(닫힌 셸). thickness <= 0 = 자동(바운딩박스 최소변의 5%). 결과는 새 객체(원본은 지움) */
CAD_API int32_t    CAD_Shell(const uint32_t* ids, uint32_t count, double thickness, uint32_t* outIds, uint32_t capacity);
/* 볼록 모서리 전부 필렛·모따기 — distance(mm) <= 0 = 자동(최소변의 12%). B-Rep 솔리드는 **같은 id** 에 가공 기록(스케치를 고쳐도 다시 적용),
 * 그 밖의 메시는 새 객체(원본은 지움). 모서리 하나만은 CAD_AddEdgeBevel */
CAD_API int32_t    CAD_EdgeFillet(const uint32_t* ids, uint32_t count, double distance, uint32_t* outIds, uint32_t capacity);
CAD_API int32_t    CAD_EdgeChamfer(const uint32_t* ids, uint32_t count, double distance, uint32_t* outIds, uint32_t capacity);
/* 모서리 가공 기록 — B-Rep 솔리드에 필렛/모따기 하나를 더한다(스케치가 바뀌어도 다시 적용). allEdges = 볼록 모서리 전부,
 * 아니면 brepEdge(B-Rep 선 모서리 id). distance = 월드 mm. B-Rep 이 아님 = CAD_E_WRONG_TYPE, 안 먹으면 CAD_E_FAILED(변화 없음) */
CAD_API CAD_Status CAD_AddEdgeBevel(uint32_t id, bool fillet, double distance, bool allEdges, uint32_t brepEdge);
CAD_API int32_t    CAD_GetEdgeBevelCount(uint32_t id);

/* ── 3D 불리언 (CSG — AcDb3dSolid booleanOper) ──
 * 부르면 그 자리에서 계산한다. 입력을 먼저 전부 검사 — 없는 id·메시 아님·잠긴 도면층·닫히지 않은 메시·중복이 하나라도 있으면 아무것도 안 바꾼다.
 * 결과 추가 + 원본 삭제(keepOriginals = false) = 되돌리기 1, 결과만 선택. 결과는 첫 원본의 이름·도면층·색·금속·불투명도를 이어받는다.
 * 여러 개는 한 번에 계산(Manifold BatchBoolean) — 순서 무관. 계산이 안 되면(교집합이 비었음 …) CAD_E_FAILED + 이유 */
/* 합집합 — ids 2개 이상 → 한 객체(떨어져 있어도 한 객체에 덩어리 여럿) */
CAD_API CAD_Status CAD_BooleanUnion(const uint32_t* ids, uint32_t count, bool keepOriginals, uint32_t* outId);
/* 교집합 — ids 2개 이상 **모두의** 공통 부분 */
CAD_API CAD_Status CAD_BooleanIntersection(const uint32_t* ids, uint32_t count, bool keepOriginals, uint32_t* outId);
/* 차집합 — 기준 baseIds 에서 cutIds 전부를 뺀다. perBase = false: union(기준) − union(빼는 것) → 결과 1개(오토캐드 SUBTRACT),
 * true: 기준마다 따로(판 3장에 같은 구멍 → 판 3장, 통째로 깎인 기준은 결과 없음). 반환 = 결과 수(outIds = NULL 이면 해 본 뒤 물려 개수만) */
CAD_API int32_t    CAD_BooleanSubtract(const uint32_t* baseIds, uint32_t baseCount, const uint32_t* cutIds, uint32_t cutCount,
                                       bool keepOriginals, bool perBase, uint32_t* outIds, uint32_t capacity);

/* 간섭 검사 — ids 가 NULL·1개 이하면 보이는 솔리드 전부. createObjects = 겹친 덩어리를 "간섭" 층에 만든다(되돌리기 1).
 * 반환 = 전체 간섭 쌍 수(부피 큰 순), out 에 capacity 만큼. createObjects 인데 out = NULL(칸 0)이거나 칸이 모자라면 해 본 뒤 물려 개수만 */
typedef struct CAD_InterferenceInfo {
    uint32_t objectA, objectB;
    double volume;          /* 겹친 부피(mm³) */
    uint32_t resultId;      /* createObjects 일 때 만든 덩어리 id, 아니면 0 */
} CAD_InterferenceInfo;
CAD_API int32_t    CAD_CheckInterference(const uint32_t* ids, uint32_t count, bool createObjects, CAD_InterferenceInfo* out,
                                         uint32_t capacity);

/* 분해도·조립 설명서 — AI 액션 explode·MCP 도구 explode_view 와 같은 창구. argsJson = {"op":"status|solve|auto|clear|amount|play|back|
 * part|spin|balloons|bom|manual", ids, id, t, seconds, turns, dir[3], distance, step, show, path, paper}. 결과 JSON(ok·error·t·steps·parts·items…).
 * 글자 출력 규칙(int32_t 전체 길이, buf = NULL 이면 길이만) — 2회 호출(길이 → 버퍼)은 첫 호출에서 한 번만 실행한다.
 * argsJson NULL·빈 글 = {} (status), JSON 객체가 아니면 CAD_E_INVALID_ARG. op 의 성공·실패는 결과 JSON 의 ok·error. manual 은 여러 프레임 작업 — status 의 manual_busy 로 끝을 본다 */
CAD_API int32_t    CAD_ExplodeView(const char* argsJson, char* buf, uint32_t capacity);

/* ── 피처 치수 (솔리드웍스 Instant3D 식) ──
 * 솔리드를 만든 치수. 상자: 가로·세로·높이 / 원기둥: 지름·높이 / 돌출: 높이 + 단면·컷 스케치의 원 지름, 직사각형 가로·세로. 값은 월드 mm.
 * 일반 폴리선 단면(12꼭짓점까지)은 변마다 길이 — 바꾸면 그 변 끝 너머 꼭짓점을 같이 민다(STRETCH, 직각 유지).
 * kind: 0=가로 1=세로 2=높이 3=지름 4=변 5=위치(원 컷·원 보스 중심 — 바닥 단면 모서리에서 거리, 바꾸면 그 원 스케치를 옮긴다).
 * sketchId = 값이 사는 스케치(0 = 솔리드 자체). 위치 치수는 크기 치수 뒤에 붙는다(기존 번호는 그대로).
 * Set 은 다시 만들기, 되돌리기 1 — 모양을 못 만드는 값이면 CAD_E_FAILED + 이유(바꾸지 않음), 번호 밖 = CAD_E_OUT_OF_RANGE.
 * Visible = 선택한 솔리드 위에 파란 치수 표시(명령 fdim, 상태바 "치수") — 더블클릭하면 그 자리에서 고친다 */
CAD_API CAD_Status CAD_SetFeatureDimensionsVisible(bool visible);
CAD_API CAD_Status CAD_GetFeatureDimensionsVisible(bool* outVisible);
CAD_API int32_t    CAD_GetFeatureDimensionCount(uint32_t id);
CAD_API CAD_Status CAD_GetFeatureDimension(uint32_t id, uint32_t index, int32_t* outKind, double* outValue, uint32_t* outSketchId);
CAD_API CAD_Status CAD_SetFeatureDimension(uint32_t id, uint32_t index, double value);

#ifdef __cplusplus
}
#endif
