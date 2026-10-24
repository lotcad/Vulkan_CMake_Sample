#pragma once
/* LotCAD C API - curves  [AcDbCurve (lines, arcs, polylines, splines)]
 * Curve creation, polyline vertices, sketch constraints.
 * 곡선 만들기·폴리선 정점·스케치 구동 제약.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"
#include "lotcad_geometry.h"   /* CAD_GeVec3·CAD_GeIntersection — 곡선 객체 함수 */

#ifdef __cplusplus
extern "C" {
#endif
CAD_API uint32_t CAD_CreateLine(float x1, float y1, float z1,
                                float x2, float y2, float z2);
CAD_API uint32_t CAD_CreateCircle(float cx, float cy, float cz,
                                  float radius,
                                  float normalX, float normalY, float normalZ);

/* ── 2D 스케치 구동 제약 ─────────────────────────────────────────────
 * 화면에 그리는 CAD_CreateDimension(측정/주석)과 별개로 실제 선·원을 움직인다.
 * point: 선 0=시작, 1=끝 / 원 0=중심. value 단위는 월드 mm.
 * 단항 제약(수평/수직/반지름/직경)은 entityB=0, pointB=0.
 */
enum {
    CAD_SKETCH_COINCIDENT = 0,
    CAD_SKETCH_HORIZONTAL = 1,
    CAD_SKETCH_VERTICAL   = 2,
    CAD_SKETCH_CONCENTRIC = 3,
    CAD_SKETCH_DISTANCE   = 4,
    CAD_SKETCH_RADIUS     = 5,
    CAD_SKETCH_DIAMETER   = 6,
    CAD_SKETCH_PARALLEL      = 7,   /* 선 A·B */
    CAD_SKETCH_PERPENDICULAR = 8,   /* 선 A·B */
    CAD_SKETCH_EQUAL         = 9,   /* 선 두 개 = 같은 길이, 원 두 개 = 같은 반지름 */
    CAD_SKETCH_FIXED         = 10,  /* pointA 0/1 = 그 점만, CAD_SKETCH_WHOLE_ENTITY = 객체 전체 */
    CAD_SKETCH_ANGLE         = 11,  /* 선 A 에서 B 로 재는 부호 있는 각, value 단위 도(°) */
    CAD_SKETCH_TANGENT       = 12,  /* 선–원 또는 원–원(외접/내접은 지금 모양에서 자동) */
    CAD_SKETCH_DISTANCE_X    = 13,  /* 점 A→B 가로 거리(부호 있음, A 평면 right 축). 선 점 2 = 중점 */
    CAD_SKETCH_DISTANCE_Y    = 14   /* 점 A→B 세로 거리(부호 있음, A 평면 up 축) */
};
#define CAD_SKETCH_WHOLE_ENTITY 255
/* 구속 상태 — CAD_GetSketchDiagnosis 의 outStatus */
enum {
    CAD_SKETCH_UNDER     = 0,   /* 과소 구속: 자유도 남음 */
    CAD_SKETCH_WELL      = 1,   /* 완전 구속 */
    CAD_SKETCH_REDUNDANT = 2,   /* 과잉: 풀리지만 같은 조건이 겹침 */
    CAD_SKETCH_CONFLICT  = 3,   /* 충돌: 동시에 만족 불가 */
    CAD_SKETCH_INVALID   = 4    /* 잘못된 참조 */
};
typedef struct CAD_SketchConstraintInfo {
    uint32_t id;
    int type;
    uint32_t entityA;
    int pointA;
    uint32_t entityB;
    int pointB;
    float value;
    bool driving;
    bool enabled;
} CAD_SketchConstraintInfo;
CAD_API uint32_t CAD_AddSketchConstraint(int type,
                                         uint32_t entityA, int pointA,
                                         uint32_t entityB, int pointB,
                                         float value);
CAD_API bool CAD_SetSketchConstraintValue(uint32_t constraintId, float value);
CAD_API bool CAD_RemoveSketchConstraint(uint32_t constraintId);
CAD_API bool CAD_SolveSketchConstraints(void);
CAD_API uint32_t CAD_GetSketchConstraintCount(void);
/* 반환=필요한 전체 개수. outIds/capacity가 작으면 앞부분만 복사한다. */
CAD_API uint32_t CAD_GetSketchConstraintIds(uint32_t* outIds, uint32_t capacity);
CAD_API bool CAD_GetSketchConstraintInfo(uint32_t constraintId, CAD_SketchConstraintInfo* outInfo);
/* 이 선·원과 제약으로 이어진 묶음의 자유도·구속 상태. 형상은 바꾸지 않는다.
 * outProblemIds 에는 충돌(또는 중복) 제약 id — 반환 = 필요한 전체 개수, capacity 만큼만 복사. 실패 시 -1. */
CAD_API int CAD_GetSketchDiagnosis(uint32_t entityId, int* outDof, int* outStatus,
                                   uint32_t* outProblemIds, uint32_t capacity);
/* 마지막 제약 추가·값 편집이 충돌로 실패했을 때 부딪친 제약 id 들. 반환 = 전체 개수. */
CAD_API uint32_t CAD_GetLastSketchConflict(uint32_t* outIds, uint32_t capacity);

CAD_API uint32_t CAD_CreatePolygon(float cx, float cy, float cz,
                                   float radius,
                                   int sides,
                                   float normalX, float normalY, float normalZ,
                                   float firstVertexDirX,
                                   float firstVertexDirY,
                                   float firstVertexDirZ);
CAD_API uint32_t CAD_CreateArc(float startX, float startY, float startZ,
                               float throughX, float throughY, float throughZ,
                               float endX, float endY, float endZ);
CAD_API uint32_t CAD_CreatePolyline(const float* xyz,
                                    uint32_t pointCount,
                                    bool closed);
CAD_API uint32_t CAD_CreateRectangle(float x0, float y0, float z0,
                                     float x2, float y2, float z2);

// ── 폴리선 정점 목록 (PEDIT 대응) ──
// 닫기·열기·반전·정점 삽입/삭제는 전부 "정점 목록을 바꾸는 일" 이라, 하위 명령마다
// 함수를 늘리는 대신 목록을 통째로 읽고 쓰게 한다. 호스트가 받아서 고쳐 되돌려주면 된다.
//
//   uint32_t n = CAD_GetPolylinePoints(id, NULL, 0, NULL);   // 개수 질의
//   float* buf = malloc(n * 3 * sizeof(float));
//   bool closed = false;
//   CAD_GetPolylinePoints(id, buf, n, &closed);
//   ... 고친 뒤 ...
//   CAD_SetPolylinePoints(id, buf, n, closed);               // undo 1스텝으로 적재
//
// xyz 는 3 × count 개 float. 좌표는 객체 로컬 (그립/스케치와 같은 공간).
// Set 은 정점이 2개 미만이면 실패. Polyline 이 아닌 객체는 0 / false.
CAD_API uint32_t CAD_GetPolylinePoints(uint32_t id, float* outXyz, uint32_t cap, bool* outClosed);
CAD_API bool     CAD_SetPolylinePoints(uint32_t id, const float* xyz, uint32_t count, bool closed);

/* 타원 — 중심, 장축 반벡터(중심→장축 끝, 길이 = 장반경), 단축비(0<ratio≤1), 평면 법선(0,0,0 이면 +Z). 실패 0. */
CAD_API uint32_t CAD_CreateEllipse(float cx, float cy, float cz,
                                   float majorX, float majorY, float majorZ,
                                   float ratio,
                                   float normalX, float normalY, float normalZ);
/* 맞춤점을 지나는 스플라인 — fitXYZ = count*3, closed = 닫힌(주기) 스플라인. 열린 것은 2점, 닫힌 것은 3점 이상. 실패 0. */
CAD_API uint32_t CAD_CreateSpline(const float* fitXYZ, uint32_t count, bool closed);

/* ── 곡선 객체 (AcDbCurve) ──────────────────────────────────────────────
 * 선·원·호·폴리선·타원·스플라인 객체를 id 로 다룬다. 새 규칙: CAD_Status(0 = CAD_OK, 음수 = CAD_E_*), 값은 출력 인자, 좌표 = 월드 mm(double).
 * 매개변수는 ObjectARX 와 같다: 선 = 시작부터 거리, 원·호 = 각(rad, 원은 객체의 0° 방향부터), 타원 = 매개각, 스플라인 = 매듭값,
 * 폴리선 = 정점 번호(조각 i = i..i+1). 계산은 CAD_GeCurve* 와 같은 코드 — 결과·실패 코드가 기하 곡선과 같다.
 * 없는 id = CAD_E_BAD_HANDLE, 곡선 객체가 아님 = CAD_E_WRONG_TYPE, 엔진 없음 = CAD_E_NO_ENGINE. 엔진 스레드에서만. */

/* 객체의 곡선을 기하 곡선 핸들로(getAcGeCurve) — 여기서 CAD_GeCurve* 를 다 쓸 수 있다. 다 쓰면 CAD_GeCurveFree */
CAD_API CAD_Status CAD_CurveGetGeCurve(uint32_t id, uint64_t* outCurve);
/* 객체의 모양을 기하 곡선으로 바꾼다(setFromAcGeCurve) — 같은 종류만: 선 ← 직선, 원 ← 한 바퀴 원호, 호 ← 원호, 타원 ← 타원호,
 * 스플라인 ← NURBS, 폴리선 ← 직선 조각 폴리선. 아니면 CAD_E_WRONG_TYPE. id·도면층·색은 그대로, 되돌리기 1. 잠긴 도면층 = CAD_E_LOCKED */
CAD_API CAD_Status CAD_CurveSetFromGeCurve(uint32_t id, uint64_t curve);

/* CAD_CreateCurveFromGe 의 선택 — NULL = 전부 기본. 맨 앞 size = sizeof(CAD_CurveCreateOptions), 새 칸은 끝에만 붙는다 */
typedef struct CAD_CurveCreateOptions {
    uint32_t size;
    uint32_t propsFrom;   /* 이 객체의 도면층·색·선종류·불투명도를 이어받음(0 = 지금 도면층·기본 색) */
} CAD_CurveCreateOptions;
/* 기하 곡선으로 새 객체 — 직선 = 선, 원호 = 원·호, 타원호 = 타원, NURBS = 스플라인, 합성 곡선 = 폴리선
 * (엔진 폴리선은 직선 조각만이라 합성 곡선 안 호·타원·NURBS 조각은 원 분할 규칙으로 꺾은선이 된다). 되돌리기 1 */
CAD_API CAD_Status CAD_CreateCurveFromGe(uint64_t curve, const CAD_CurveCreateOptions* opt, uint32_t* outId);

/* 매개변수 구간 — getStartParam·getEndParam */
CAD_API CAD_Status CAD_CurveGetInterval(uint32_t id, double* outStartParam, double* outEndParam);
CAD_API CAD_Status CAD_CurveIsClosed(uint32_t id, bool* outClosed);   /* isClosed */
/* 점·1차·2차 도함수 — getPointAtParam·getFirstDeriv·getSecondDeriv */
CAD_API CAD_Status CAD_CurveEvaluate(uint32_t id, double param, CAD_GeVec3* outPoint, CAD_GeVec3* outFirstDeriv,
                                     CAD_GeVec3* outSecondDeriv);
/* 곡선 위 점의 매개변수(허용치 밖 = CAD_E_NOT_ON_CURVE) — getParamAtPoint */
CAD_API CAD_Status CAD_CurveParamAtPoint(uint32_t id, CAD_GeVec3 p, double* outParam);
/* 두 매개변수 사이 길이 — getDistAtParam(fromParam = 시작). 구간 밖 = CAD_E_OUT_OF_RANGE */
CAD_API CAD_Status CAD_CurveLength(uint32_t id, double fromParam, double toParam, double* outLength);
/* fromParam 에서 곡선을 따라 length(음수 = 거꾸로) 간 곳 — getParamAtDist. 끝을 넘으면 끝에서 멈춤 */
CAD_API CAD_Status CAD_CurveParamAtLength(uint32_t id, double fromParam, double length, double* outParam);
/* 가장 가까운 점 — getClosestPointTo(pt, extend). outDistance = 그 거리 */
CAD_API CAD_Status CAD_CurveClosestPoint(uint32_t id, CAD_GeVec3 p, bool extend, double* outParam, CAD_GeVec3* outPoint,
                                         double* outDistance);
/* 닫힌 평면 곡선 넓이 — getArea. 열림 = CAD_E_NOT_CLOSED, 비평면 = CAD_E_NOT_PLANAR */
CAD_API CAD_Status CAD_CurveArea(uint32_t id, double* outArea);
/* 두 곡선 객체의 교차 — intersectWith. extendMode = CAD_GE_EXTEND_*, viewDir ≠ 0 이면 그 방향으로 본 교차. 결과는 id1 매개변수 순 */
CAD_API int32_t CAD_CurveIntersect(uint32_t id1, uint32_t id2, int extendMode, CAD_GeVec3 viewDir,
                                   CAD_GeIntersection* outHits, uint32_t capacity);
/* 오프셋 곡선을 새 객체로 — getOffsetCurvesGivenPlaneNormal(CAD_GeCurveOffset 과 같은 규칙: distance > 0 = 진행 방향 오른쪽).
 * 새 객체는 원본의 도면층·색·선종류를 이어받고 원본은 그대로, 전부 되돌리기 1. 반환 = 만든(만들) 개수 — 칸이 모자라면 아무것도 안 만든다 */
CAD_API int32_t CAD_CurveOffset(uint32_t id, double distance, CAD_GeVec3 planeNormal, uint32_t* outIds, uint32_t capacity);
/* 매개변수들에서 나눈 조각을 새 객체로 — getSplitCurves(CAD_GeCurveSplit 과 같은 규칙). 원본은 그대로(지우려면 따로), 되돌리기 1.
 * 반환 = 조각 수 — 칸이 모자라면 아무것도 안 만든다 */
CAD_API int32_t CAD_CurveSplit(uint32_t id, const double* params, uint32_t count, uint32_t* outIds, uint32_t capacity);
CAD_API CAD_Status CAD_CurveReverse(uint32_t id);   /* 방향 뒤집기 — reverseCurve, 되돌리기 1 */
/* 끝을 경로 위 점까지 늘인다 — extend(fromStart, toPoint). 선·호·타원·폴리선(끝 조각이 선), 되돌리기 1 */
CAD_API CAD_Status CAD_CurveExtendToPoint(uint32_t id, bool atStart, CAD_GeVec3 toPoint);

#ifdef __cplusplus
}
#endif
