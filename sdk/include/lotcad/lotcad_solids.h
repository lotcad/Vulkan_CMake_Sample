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

// 자체 Mini B-Rep 정보. featureType: 0=Box, 1=Cylinder, 2=Extrude, 3=Sphere, 4=Cone, 5=Torus.
// 파라미터(CAD_GetBRepParameters/Set…): Sphere = radius · Cone = radius(밑면)·height · Torus = radius(큰)·height 자리에 관 반지름.
// volume/surfaceArea는 객체의 현재 축척·회전을 반영한 월드 값이다.
// 임포트 메시나 아직 B-Rep으로 복원하지 않은 Boolean 결과는 false.
// 원통 차집합 결과의 타공 편집 가능 여부는 CAD_GetBooleanCylinderCutCount로 조회한다.
typedef struct CAD_BRepInfo {
    int32_t featureType;
    uint32_t vertexCount;
    uint32_t edgeCount;
    uint32_t faceCount;
    double volume;
    double surfaceArea;
} CAD_BRepInfo;
CAD_API bool     CAD_GetBRepInfo(uint32_t id, CAD_BRepInfo* outInfo);

// B-Rep 생성 파라미터. 사용하지 않는 필드는 0이다.
// dimensions는 객체 transform.scale과 별개인 로컬 원본 치수다.
typedef struct CAD_BRepParameters {
    int32_t featureType;
    float dimensionsX;
    float dimensionsY;
    float dimensionsZ;
    float radius;
    float height;
    float directionX;
    float directionY;
    float directionZ;
} CAD_BRepParameters;
CAD_API bool     CAD_GetBRepParameters(uint32_t id, CAD_BRepParameters* outParams);
CAD_API bool     CAD_SetBRepBoxDimensions(uint32_t id, float x, float y, float z);
CAD_API bool     CAD_SetBRepCylinderDimensions(uint32_t id, float radius, float height);
CAD_API bool     CAD_SetBRepExtrudeHeight(uint32_t id, float height);
// 안정적인 B-Rep face id 조회. surfaceType: 0=Plane, 1=Cylinder. 원점/법선은 월드 좌표.
typedef struct CAD_BRepFaceInfo {
    uint32_t faceId;
    int32_t surfaceType;
    float originX, originY, originZ;
    float normalX, normalY, normalZ;
} CAD_BRepFaceInfo;
CAD_API bool     CAD_GetBRepFaceInfo(uint32_t id, uint32_t faceId, CAD_BRepFaceInfo* outInfo);
// 지정 면을 바깥쪽으로 이동한다. 박스 평면은 반대편 면을 고정하고,
// 원통 옆면(surfaceType=1)은 반지름을 변경하며, 돌출체 옆면은 프로파일 변을 평행 이동한다.
// distance는 월드 단위다.
CAD_API bool     CAD_PushPullBRepFace(uint32_t id, uint32_t faceId, float distance);
// Extrude 솔리드에 편집 가능한 포켓/관통 컷을 추가한다.
// profileXYZ는 객체 로컬 좌표의 폐프로파일(pointCount*3)이며 캡과 평행한 평면에 둔다.
// 엔진이 아래 기준면으로 투영한다. throughAll=true이면 depth를 무시한다.
// 외곽에 닿거나 다른 컷과 겹치는 프로파일은 false를 반환한다.
enum { CAD_MAX_BREP_PROFILE_POINTS = 2048 };
CAD_API bool     CAD_CutExtrudeBRep(uint32_t id,
                                    const float* profileXYZ,
                                    uint32_t pointCount,
                                    float depth,
                                    bool throughAll);
// 기존 닫힌 2D 스케치를 프로파일로 사용한다. 스케치의 월드 변환을 대상 솔리드의
// 로컬 좌표로 자동 변환하므로 화면에서 그린 사각형·원·폴리선을 바로 사용할 수 있다.
CAD_API bool     CAD_CutExtrudeFromSketch(uint32_t id,
                                          uint32_t sketchId,
                                          float depth,
                                          bool throughAll);
// 보스(더하는 돌출) — Extrude 솔리드의 캡 안쪽에 폐프로파일을 쌓는다(피처 기록에 남아 치수·재생성이 된다).
// height > 0 = 위 캡에서 위로, < 0 = 아래 캡에서 아래로. 발자국이 외곽에 닿거나 같은 쪽 보스와 겹치거나
// 기존 컷 테두리를 가로지르면 false. 이미 있던 관통 컷은 보스까지 관통한다.
CAD_API bool     CAD_BossExtrudeBRep(uint32_t id,
                                     const float* profileXYZ,
                                     uint32_t pointCount,
                                     float height);
// 닫힌 스케치로 — 스케치가 가까운 캡(위/아래) 쪽으로 height(양수) 만큼. 스케치가 바뀌면 다시 만든다.
CAD_API bool     CAD_BossExtrudeFromSketch(uint32_t id,
                                           uint32_t sketchId,
                                           float height);
CAD_API uint32_t CAD_GetBRepBossCount(uint32_t id);
// 보스 높이 읽기·바꾸기(부호 = 위/아래). 바꾸기는 undo 1.
CAD_API bool     CAD_GetBRepBossHeight(uint32_t id, uint32_t bossIndex, float* outHeight);
CAD_API bool     CAD_SetBRepBossHeight(uint32_t id, uint32_t bossIndex, float height);
typedef struct CAD_BRepCutInfo {
    uint32_t cutIndex;
    uint32_t pointCount;
    float depth;
    bool throughAll;
} CAD_BRepCutInfo;
CAD_API uint32_t CAD_GetBRepCutCount(uint32_t id);
CAD_API bool     CAD_GetBRepCutInfo(uint32_t id, uint32_t cutIndex, CAD_BRepCutInfo* outInfo);
// 필요한 점 개수를 반환한다. outXYZ가 null이거나 capacity가 작으면 복사하지 않는다.
CAD_API uint32_t CAD_GetBRepCutProfile(uint32_t id, uint32_t cutIndex,
                                       float* outXYZ, uint32_t capacity);
// 기존 컷의 프로파일과 관통/포켓 깊이를 교체한다. cutIndex는 GetBRepCutInfo의 값이다.
// profileXYZ는 대상 솔리드의 객체 로컬 좌표이며, 임포트한 폐폴리라인 좌표도 사용할 수 있다.
CAD_API bool     CAD_SetBRepCut(uint32_t id, uint32_t cutIndex,
                                const float* profileXYZ, uint32_t pointCount,
                                float depth, bool throughAll);
// 닫힌 엔진 스케치(직접 그린 형상 또는 DXF 등에서 변환한 형상)로 기존 컷을 교체한다.
CAD_API bool     CAD_SetBRepCutFromSketch(uint32_t id, uint32_t cutIndex,
                                          uint32_t sketchId,
                                          float depth, bool throughAll);
// 컷·보스 지우기(솔리드웍스 피처 삭제처럼) — 여러 개를 한 번에 빼고 남은 것으로 한 번 다시 만든다. 그 피처만 쓰던 스케치도 지운다.
// 번호는 CAD_GetBRepCutInfo / 보스 순서(지우기 전 번호 — 지운 뒤엔 뒤쪽 번호가 당겨진다). 되돌리기 한 단계.
// 남은 것으로 모양을 못 만들면(보스를 지워 그 안 컷이 허공에 남음 등) 아무것도 안 바꾸고 false + CAD_GetLastError.
CAD_API bool     CAD_RemoveBRepFeatures(uint32_t id, const uint32_t* cutIndices, uint32_t cutCount,
                                        const uint32_t* bossIndices, uint32_t bossCount);
CAD_API bool     CAD_RemoveBRepCut(uint32_t id, uint32_t cutIndex);     // 하나만 — CAD_RemoveBRepFeatures 와 같다
CAD_API bool     CAD_RemoveBRepBoss(uint32_t id, uint32_t bossIndex);
// 일반 Boolean 차집합이 B-Rep 기준체와 원통 커터로 만들어졌으면 타공 기록을 보존한다.
// 중심·방향은 결과 객체 로컬 좌표, radius/height는 같은 좌표계의 수치다.
typedef struct CAD_BooleanCylinderCutInfo {
    uint32_t cutIndex;
    float centerX, centerY, centerZ;
    float axisX, axisY, axisZ;
    float radius;
    float height;
} CAD_BooleanCylinderCutInfo;
CAD_API uint32_t CAD_GetBooleanCylinderCutCount(uint32_t id);
CAD_API bool     CAD_GetBooleanCylinderCutInfo(uint32_t id, uint32_t cutIndex,
                                               CAD_BooleanCylinderCutInfo* outInfo);
CAD_API bool     CAD_SetBooleanCylinderCut(uint32_t id, uint32_t cutIndex,
                                           float centerX, float centerY, float centerZ,
                                           float axisX, float axisY, float axisZ,
                                           float radius, float height);
// B-Rep 정의로 렌더 메시 캐시를 강제 재생성한다. 곡면 분할은 3~512로 제한된다.
CAD_API bool     CAD_RebuildBRepMesh(uint32_t id, uint32_t curvedSegments);

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
