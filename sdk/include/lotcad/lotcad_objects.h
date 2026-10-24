#pragma once
/* LotCAD C API - objects  [AcDbEntity / AcDbObject]
 * Object ids, properties, JSON, query, transform, color, layer, bounds, measure, material.
 * 객체 id·속성·JSON·질의·변환·색·도면층·경계·측정·재질.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"
#include "lotcad_geometry.h"   /* CAD_GeVec3 · CAD_GeMatrix · CAD_GePlane — 객체 편집(CAD_Entity*) */

#ifdef __cplusplus
extern "C" {
#endif
/* ── 객체 기본 (AcDbObject · AcDbEntity 의 속성) ─────────────────────────────────
 * 규칙(lotcad_types.h): 반환 CAD_Status(0 = CAD_OK, 음수 = CAD_E_*), 값은 출력 인자. 없는 id = CAD_E_BAD_HANDLE, 잠긴 도면층의 객체를
 * 바꾸면 CAD_E_LOCKED, 틀린 값 = CAD_E_INVALID_ARG. 실패 이유 글은 CAD_GetLastError, 성공하면 비운다.
 * 글자 출력: int32_t f(…, char* buf, uint32_t capacity) — 반환 = 널을 뺀 전체 길이(UTF-8 바이트), 음수 = CAD_E_*.
 *   buf = NULL(칸 0)이면 길이만. 칸이 모자라면 앞부분만(글자 가운데에서 자르지 않고) 담고 그래도 전체 길이를 돌려준다.
 * 개수 출력: int32_t f(…, uint32_t* outIds, uint32_t capacity) — 반환 = 전체 개수, capacity 만큼만 채운다.
 * 좌표·길이 = 월드 mm(double), 각 = rad. 바꾸는 함수는 한 번 = 되돌리기 1단계. 엔진 스레드에서만(아니면 CAD_E_WRONG_THREAD,
 * CAD_GetLastError 만 아무 스레드). */

/* 객체 하나를 JSON 한 줄로 — 종류·이름·레이어·색·변환·경계 + 종류별 기하.
 * (line: start/end/length, polyline: points/closed, circle: center/radius/normal, arc: +startDeg/endDeg,
 *  text: text/height/font, dimension: dimType/p1/p2/value, mesh: vertices/triangles/light)
 * 단위 mm, 좌표 월드. 키 이름은 lot_object_json.h 한 곳에서 정하며 AI 선택 문맥·씬 요약과 같다. */
CAD_API int32_t    CAD_GetObjectJson(uint32_t id, char* buf, uint32_t capacity);

/* 이름으로 속성 하나 읽기·쓰기 — 키는 CAD_GetObjectJson 의 키와 같다.
 *   공통    name, color, colorByLayer, visible, layer(이름|id), linetype(이름|id|"bylayer"), linetypeScale,
 *           position, rotation[x,y,z,w], scale, opacity, metallic, group
 *   line    start, end          polyline  points, closed        circle  center, radius
 *   arc     center, radius, startDeg, endDeg                     text    text, height, font
 *   dimension p1, p2, p3, dimLinePoint, precision                mesh    intensity(조명)
 * Get: 값의 JSON 텍스트(예: 50.0 / [1,2,3] / "이름"). 없는 키 = CAD_E_NOT_FOUND.
 * Set: valueJson 은 JSON(따옴표 없는 글자는 문자열로 받음). 좌표·길이는 월드 mm. 딸린 모델을 다시 만든다.
 *      없는 키·형식 오류 = CAD_E_INVALID_ARG(이유 글에 무엇이 틀렸는지). */
CAD_API int32_t    CAD_GetObjectProperty(uint32_t id, const char* key, char* buf, uint32_t capacity);
CAD_API CAD_Status CAD_SetObjectProperty(uint32_t id, const char* key, const char* valueJson);
/* 이 스레드에서 직전에 실패한 함수의 이유(UTF-8, 화면 언어) — 스레드마다 따로, 아무 스레드에서나. CAD_Status·개수를 돌려주는 함수는
 * 성공하면 비운다(아직 옛 규칙인 영역의 함수 일부는 실패 때만 쓴다). 프로그램은 글이 아니라 결과 코드(CAD_E_*)로 가를 것.
 * 이 함수는 글을 비우지 않는다. */
CAD_API int32_t    CAD_GetLastError(char* buf, uint32_t capacity);

/* 질의 — 필터 JSON 으로 객체 id 목록. 키는 전부 선택(AND):
 *   {"kind":"circle"|["circle","arc"], "layer":"이름"|id, "name":"기둥*"(글롭), "selected":true, "visible":true,
 *    "within":{"min":[x,y,z],"max":[x,y,z]}(상자 안), "intersects":{min,max}(겹침), "near":{"point":[x,y,z],"radius":r},
 *    "pick":"largest"|"smallest"(통과한 것 중 하나), "limit":N}
 * 반환 = 전체 개수. 틀린 필터 = CAD_E_INVALID_ARG. */
CAD_API int32_t    CAD_QueryObjects(const char* filterJson, uint32_t* outIds, uint32_t capacity);
/* 질의 결과를 선택으로 — 같은 필터 문법. additive = false 면 기존 선택을 비운다. outSelected = 고른 수(NULL 이면 안 받음).
 * AI 의 edit_selected op="select" 와 같은 통로. */
CAD_API CAD_Status CAD_SelectByQuery(const char* filterJson, bool additive, uint32_t* outSelected);
/* 씬 요약 JSON — {"count","selected","units":"mm","bounds","kinds":{종류:수},"layers":[…],"objects":[요약…],"more"}.
 * objects 는 앞에서 maxObjects 개(0 이면 50). 객체 상세는 CAD_GetObjectJson. */
CAD_API int32_t    CAD_GetSceneJson(int32_t maxObjects, char* buf, uint32_t capacity);

/* 지우기 — 여러 개는 CAD_EntityErase */
CAD_API CAD_Status CAD_DeleteObject(uint32_t id);

CAD_API int32_t    CAD_GetObjectCount(void);   /* 장면의 객체 수 */
/* 전체 객체 id — 반환 = 전체 개수 */
CAD_API int32_t    CAD_GetObjectIds(uint32_t* outIds, uint32_t capacity);
/* 종류: 0=Mesh 1=Line 2=Polyline 3=Circle 4=Arc 5=Text 6=Dimension 7=PointCloud 8=ParticleEmitter … (PrimitiveKind 번호) */
CAD_API CAD_Status CAD_GetObjectKind(uint32_t id, int32_t* outKind);
/* 있는가 — 없는 id 도 CAD_OK(outExists = false). 엔진이 없거나 다른 스레드면 그 코드 */
CAD_API CAD_Status CAD_ObjectExists(uint32_t id, bool* outExists);

/* 변환 — 객체 = 위치·회전·축척(T·R·S). 위치 = 객체 기준점의 월드 자리, 축척 = 축마다(0 이나 음수는 CAD_E_INVALID_ARG) */
CAD_API CAD_Status CAD_GetPosition(uint32_t id, CAD_GeVec3* outPosition);
CAD_API CAD_Status CAD_SetPosition(uint32_t id, CAD_GeVec3 position);
CAD_API CAD_Status CAD_GetScale(uint32_t id, CAD_GeVec3* outScale);
CAD_API CAD_Status CAD_SetScale(uint32_t id, CAD_GeVec3 scale);
/* 회전 = axis 둘레로 angle(rad, 오른손). Get 은 회전이 없으면 축 (0,0,1)·각 0. Set 의 axis 길이 0 = CAD_E_DEGENERATE */
CAD_API CAD_Status CAD_GetRotationAxisAngle(uint32_t id, CAD_GeVec3* outAxis, double* outAngle);
CAD_API CAD_Status CAD_SetRotationAxisAngle(uint32_t id, CAD_GeVec3 axis, double angle);
/* 위치·회전·축척을 행렬 하나로(m = T·R·S, 열 우선 — CAD_GeMatrix). 한 번에 대입하니 "옮겼지만 아직 안 돌아간" 프레임이 없다
 * (로봇 관절·모션 캡처·시뮬레이터가 매 프레임 자세를 밀어 넣는 길). Set 은 비틀림(열이 서로 수직 아님)·대칭(행렬식 < 0)이면
 * CAD_E_NOT_SUPPORTED, 축척 0 = CAD_E_DEGENERATE. 회전 행렬은 CAD_GeMatrixRotation·CAD_GeMatrixCoordSys 로 만든다.
 * 엔진은 ROS(REP-103)와 같은 Z-up 오른손 좌표계 — 전방만 다르다(ROS +X, 엔진 +Y). */
CAD_API CAD_Status CAD_GetTransform(uint32_t id, CAD_GeMatrix* outMatrix);
CAD_API CAD_Status CAD_SetTransform(uint32_t id, CAD_GeMatrix m);

/* 이름 — 장면 안에서 **하나**여야 한다(이름은 사람과 외부 API 가 부품을 가리키는 수단이라). 이미 쓰는 이름 = CAD_E_DUPLICATE.
 * 앞뒤 공백은 뗀다, 빈 이름(이름 없음)은 몇 개든 된다. FindObjectByName 은 없으면 CAD_E_NOT_FOUND */
CAD_API CAD_Status CAD_SetObjectName(uint32_t id, const char* name);
CAD_API int32_t    CAD_GetObjectName(uint32_t id, char* buf, uint32_t capacity);
CAD_API CAD_Status CAD_FindObjectByName(const char* name, uint32_t* outId);

/* 보이기 — 숨긴 객체는 문서에 남지만 고르기·스냅이 안 된다. IsObjectVisible = 객체·도면층이 다 보일 때 참 */
CAD_API CAD_Status CAD_SetObjectVisible(uint32_t id, bool visible);
CAD_API CAD_Status CAD_IsObjectVisible(uint32_t id, bool* outVisible);

/* 색 — Get/SetColor = 객체 자기 색, EffectiveColor = 화면에 쓰는 색(도면층 색을 따르면 도면층 색).
 * ColorByLayer = 도면층 색 따르기. 선택 전부에 하는 함수의 outChanged = 바뀐 수(NULL 이면 안 받음, 잠긴 도면층 것은 건너뜀) */
CAD_API CAD_Status CAD_GetColor(uint32_t id, CAD_Color* outColor);
CAD_API CAD_Status CAD_SetColor(uint32_t id, CAD_Color color);
CAD_API CAD_Status CAD_GetObjectEffectiveColor(uint32_t id, CAD_Color* outColor);
CAD_API CAD_Status CAD_SetObjectColorByLayer(uint32_t id, bool byLayer);
CAD_API CAD_Status CAD_GetObjectColorByLayer(uint32_t id, bool* outByLayer);
CAD_API CAD_Status CAD_SetSelectedColorByLayer(bool byLayer, uint32_t* outChanged);

/* 불투명도 0..1 (1 = 불투명). 객체 것 × 도면층 것이 화면에 쓰인다 — 메시(채움)에만, 선·문자는 그대로.
 * 이름 기반 속성 "opacity" 와 같은 값 */
CAD_API CAD_Status CAD_SetObjectOpacity(uint32_t id, double opacity);
CAD_API CAD_Status CAD_GetObjectOpacity(uint32_t id, double* outOpacity);
CAD_API CAD_Status CAD_SetSelectedOpacity(double opacity, uint32_t* outChanged);

/* 도면층 — 0 = 도면층 "0". 없는 도면층 id = CAD_E_BAD_HANDLE. 그립을 끄는 중이면 CAD_E_BUSY */
CAD_API CAD_Status CAD_SetObjectLayer(uint32_t objectId, uint32_t layerId);
CAD_API CAD_Status CAD_GetObjectLayer(uint32_t objectId, uint32_t* outLayerId);
CAD_API CAD_Status CAD_AssignSelectedToLayer(uint32_t layerId, uint32_t* outChanged);

/* 월드 경계 상자(min/max), 가운데 = 0.5·(min + max). 큰 가져온 메시도 상자로 */
CAD_API CAD_Status CAD_GetBoundsWorld(uint32_t id, CAD_GeVec3* outMin, CAD_GeVec3* outMax);
CAD_API CAD_Status CAD_GetCenterWorld(uint32_t id, CAD_GeVec3* outCenter);

/* ── 측정 ─────────────────────────────────────────────────────────────────
 * **월드 좌표로** 잰다 — 축척이 걸린 객체도 화면에 보이는 값과 맞는다.
 * 길이: 선/폴리선 = 변의 합(닫혀 있으면 마지막→첫 변 포함), 원 = 2πr, 호 = rθ.
 * 넓이: 닫힌 폴리선 = 신발끈 공식(3D 평면판), 원 = πr², 호 = 부채꼴.
 * 메시·문자·점군은 CAD_E_WRONG_TYPE(그 종류엔 정의되지 않는다).
 * 선택 합: 잴 수 없는 종류는 건너뛴다(선택이 비었거나 잴 게 없으면 0, CAD_OK). */
CAD_API CAD_Status CAD_GetLength(uint32_t id, double* outLength);
CAD_API CAD_Status CAD_GetArea(uint32_t id, double* outArea);
CAD_API CAD_Status CAD_GetSelectionLength(double* outLength);
CAD_API CAD_Status CAD_GetSelectionArea(double* outArea);

/* 재질 — textures/ 의 파일 이름(확장자 없이, 예 "wood_oak_veneer"). 이름에 metal·steel 이 들면 금속 셰이딩.
 * name 이 NULL/"" 이면 재질 빼기. 재질 패널 클릭과 같다(앱과 같이 되돌리기 없음). 없는 재질 = CAD_E_NOT_FOUND.
 * GetMaterialName: index = 0 .. CAD_GetMaterialCount() − 1(밖 = CAD_E_OUT_OF_RANGE) */
CAD_API CAD_Status CAD_ApplyMaterial(uint32_t id, const char* name);
CAD_API int32_t    CAD_GetMaterialCount(void);
CAD_API int32_t    CAD_GetMaterialName(uint32_t index, char* buf, uint32_t capacity);

/* ── 객체 편집 (AcDbEntity) ─────────────────────────────────────────────
 * 객체 여러 개를 id 배열로 고친다. 새 규칙: CAD_Status(0 = CAD_OK, 음수 = CAD_E_*) 또는 개수(int32_t), 좌표 = 월드 mm(double), 각 = rad.
 * 입력을 먼저 전부 본다 — 없는 id(CAD_E_BAD_HANDLE)·잠긴 도면층(CAD_E_LOCKED)·같은 id 두 번·빈 배열(CAD_E_INVALID_ARG)·
 * 안 되는 종류(CAD_E_NOT_SUPPORTED)가 하나라도 있으면 **아무것도 바꾸지 않는다**. 바꾸는 함수는 한 번 = 되돌리기 1단계.
 * 새 객체를 만드는 함수의 반환 = 만든(만들) 개수: outIds = NULL(칸 0)이면 개수만 알려 주고 아무것도 안 만들며,
 * 칸이 모자라도 아무것도 안 만든다(개수만 돌려줌). 솔리드를 옮기면 그 피처 스케치도 같이 옮긴다.
 * 엔진 스레드에서만 — 다른 스레드면 CAD_E_WRONG_THREAD(CAD_Post 로 넘길 것). */

/* 변환 — transformBy. m 은 닮음 변환(회전·균일 축척·이동, 행렬식 > 0)만: 객체 변환이 이동·회전·축척이라.
 * 대칭·찌그러뜨림은 CAD_E_NOT_SUPPORTED(대칭은 CAD_EntityMirror) */
CAD_API CAD_Status CAD_EntityTransform(const uint32_t* ids, uint32_t count, CAD_GeMatrix m);
CAD_API CAD_Status CAD_EntityMove(const uint32_t* ids, uint32_t count, CAD_GeVec3 offset);   /* offset(mm)만큼 옮기기 */
/* basePoint 를 지나는 axis 둘레로 angle(rad, 오른손 — axis 끝에서 볼 때 반시계) */
CAD_API CAD_Status CAD_EntityRotate(const uint32_t* ids, uint32_t count, CAD_GeVec3 basePoint, CAD_GeVec3 axis, double angle);
/* basePoint 기준 균일 축척 — factor > 0 */
CAD_API CAD_Status CAD_EntityScale(const uint32_t* ids, uint32_t count, CAD_GeVec3 basePoint, double factor);
/* 변환한 사본 — getTransformedCopy. 사본은 원본의 도면층·색·이름을 이어받는다(잠긴 도면층 객체도 복사는 된다) */
CAD_API int32_t    CAD_EntityCopy(const uint32_t* ids, uint32_t count, CAD_GeMatrix m, uint32_t* outIds, uint32_t capacity);
/* 지우기 — erase */
CAD_API CAD_Status CAD_EntityErase(const uint32_t* ids, uint32_t count);
/* 분해 — explode. 블록 참조 → 안 객체(한 단계), 폴리선·사각형·다각형 → 선, 문자 → 윤곽선 폴리선.
 * 쪼갤 수 없는 객체(선·원·호·메시 …)는 그대로 두고, 하나도 못 쪼개면 CAD_E_NOT_SUPPORTED. 외부 참조는 결합(xref bind) 먼저 */
CAD_API int32_t    CAD_EntityExplode(const uint32_t* ids, uint32_t count, bool keepOriginal, uint32_t* outIds, uint32_t capacity);
/* 격자 배열 — 칸 (i, j, k)(i < cols, j < rows, k < levels)에 i·colStep + j·rowStep + k·levelStep 만큼 옮긴 사본. (0,0,0) = 원본 자리라
 * 사본 = (cols·rows·levels − 1) × count */
CAD_API int32_t    CAD_EntityArrayRect(const uint32_t* ids, uint32_t count, uint32_t cols, uint32_t rows, uint32_t levels,
                                       CAD_GeVec3 colStep, CAD_GeVec3 rowStep, CAD_GeVec3 levelStep, uint32_t* outIds, uint32_t capacity);
/* 원형 배열 — itemCount = 원본 포함 개수(2 이상), fillAngle(rad) = 채울 각: 2π(한 바퀴)면 itemCount 등분, 아니면 양 끝을 포함해
 * itemCount − 1 등분(오토캐드와 같다). axisPoint 를 지나는 axisDir 둘레. rotateItems = false 면 방향은 두고 자리만 옮긴다 */
CAD_API int32_t    CAD_EntityArrayPolar(const uint32_t* ids, uint32_t count, uint32_t itemCount, double fillAngle, CAD_GeVec3 axisPoint,
                                        CAD_GeVec3 axisDir, bool rotateItems, uint32_t* outIds, uint32_t capacity);
/* 평면 대칭 사본 — mirror. 곡선(선·원·호·타원·스플라인·폴리선)은 정확히, 메시는 정점을 뒤집어. 문자·치수·블록 = CAD_E_NOT_SUPPORTED.
 * eraseSource = 원본 지움(그때는 잠긴 도면층 객체 = CAD_E_LOCKED) */
CAD_API int32_t    CAD_EntityMirror(const uint32_t* ids, uint32_t count, CAD_GePlane plane, bool eraseSource, uint32_t* outIds, uint32_t capacity);
/* 월드 경계 상자 — getGeomExtents */
CAD_API CAD_Status CAD_EntityGetExtents(uint32_t id, CAD_GeVec3* outMin, CAD_GeVec3* outMax);

/* ── 객체 스냅·그립 (AcDbEntity getOsnapPoints · getGripPoints · moveGripPointsAt) ── */
/* 스냅 모드 비트 — CAD_SetOSnapModes(상태바 객체 스냅)와 같은 값 */
enum {
    CAD_OSNAP_END  = 1,     /* 끝점(메시는 꼭짓점·상자 구석) */
    CAD_OSNAP_MID  = 2,     /* 중점(메시는 상자 모서리 가운데) */
    CAD_OSNAP_CEN  = 4,     /* 중심 */
    CAD_OSNAP_FACE = 8,     /* 면 중심(메시 상자) */
    CAD_OSNAP_NODE = 16,    /* 점(치수 정의점·블록 삽입점) */
    CAD_OSNAP_QUA  = 32,    /* 사분점 */
    CAD_OSNAP_INT  = 64,    /* 교차 — 두 객체가 있어야 해 CAD_CurveIntersect 로 */
    CAD_OSNAP_PER  = 128,   /* 수직 — 직전 점(lastPoint)에서 곡선에 내린 수선의 발 */
    CAD_OSNAP_TAN  = 256,   /* 접선 — 직전 점에서 그은 접선이 곡선에 닿는 곳 */
    CAD_OSNAP_NEA  = 512,   /* 근처 — 고른 점(pickPoint)에 가장 가까운 곡선 위 점 */
    CAD_OSNAP_ALL  = 1023
};
/* 스냅점 하나 — mode = 한 비트(CAD_OSNAP_*), id = 그 점을 낸 객체 */
typedef struct CAD_OsnapPoint {
    double x, y, z;
    uint32_t mode;
    uint32_t id;
} CAD_OsnapPoint;
/* 스냅 선택 — NULL = 고른 점·직전 점 없음. 맨 앞 size = sizeof(CAD_OsnapOptions), 새 칸은 끝에만 붙는다 */
typedef struct CAD_OsnapOptions {
    uint32_t size;
    bool hasPickPoint;            /* 근처(NEA)에 쓸 고른 점 */
    bool hasLastPoint;            /* 수직(PER)·접선(TAN)에 쓸 직전 점(선 도구의 첫 점 같은 것) */
    double pickX, pickY, pickZ;
    double lastX, lastY, lastZ;
} CAD_OsnapOptions;
/* 객체 하나의 스냅점 — getOsnapPoints. modes = CAD_OSNAP_* 합. 같은 종류·같은 자리는 하나만. 반환 = 전체 개수.
 * 점군은 후보 없음(0), 근처·수직·접선은 곡선 객체만 */
CAD_API int32_t    CAD_EntityGetOsnapPoints(uint32_t id, uint32_t modes, const CAD_OsnapOptions* opt, CAD_OsnapPoint* outPoints,
                                            uint32_t capacity);
/* 그립 점(월드) — getGripPoints. 번호는 화면 그립과 같다: 선 0·1 끝 · 원 0 중심·1~4 사분점 · 호 0 중심·1 시작·2 끝·3 가운데 ·
 * 폴리선 = 정점 · 타원 0 중심·1/3 장축 끝·2/4 단축 끝 · 스플라인 = 맞춤점(없으면 제어점) · 치수 0·1 측정점·2 치수선 · 문자·블록 0 삽입점 ·
 * 메시 = 겹치지 않는 꼭짓점. 반환 = 전체 개수(해치·점군 = 0) */
CAD_API int32_t    CAD_EntityGetGripPoints(uint32_t id, CAD_GeVec3* outPoints, uint32_t capacity);
/* 그립들을 offset 만큼 — moveGripPointsAt. 고른 그립을 모두 옮기면 객체 이동과 같다(선의 0·1). 되돌리기 1.
 * 번호 범위 밖 = CAD_E_OUT_OF_RANGE, B-Rep 솔리드 = CAD_E_NOT_SUPPORTED(모양은 CAD_SetFeatureDimension 으로) */
CAD_API CAD_Status CAD_EntityMoveGripPoints(uint32_t id, const uint32_t* indices, uint32_t count, CAD_GeVec3 offset);

#ifdef __cplusplus
}
#endif
