#pragma once
/* LotCAD C API - curves  [AcDbCurve (lines, arcs, polylines, splines)]
 * Curve creation, polyline vertices (world), sketch constraints, curve objects.
 * 곡선 만들기·폴리선 정점·스케치 구동 제약.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"
#include "lotcad_geometry.h"   /* CAD_GeVec3·CAD_GeIntersection — 곡선 객체 함수 */

#ifdef __cplusplus
extern "C" {
#endif
/* ── 곡선 만들기 (AcDbLine · AcDbCircle · AcDbArc · AcDbEllipse · AcDbSpline · AcDbPolyline) ──────────────
 * 규칙(lotcad_types.h): 반환 CAD_Status(0 = CAD_OK, 음수 = CAD_E_*), 새 객체 id 는 outId. 좌표 = 월드 mm(CAD_GeVec3), 각 = rad.
 * 길이 0·반지름 0 = CAD_E_DEGENERATE, 한 줄 위 세 점(호) = CAD_E_PARALLEL, 점이 모자람·NaN = CAD_E_INVALID_ARG.
 * 법선 (0,0,0) = +Z. 만들기 한 번 = 되돌리기 1단계. 엔진 스레드에서만(아니면 CAD_E_WRONG_THREAD). */

/* 만들기 선택 CAD_CreateOptions(도면층·색 이어받기)는 lotcad_types.h — 모든 만들기 함수가 같이 쓴다 */

CAD_API CAD_Status CAD_CreateLine(CAD_GeVec3 start, CAD_GeVec3 end, const CAD_CreateOptions* opt, uint32_t* outId);
/* 원 — normal = 원이 놓인 평면의 법선 */
CAD_API CAD_Status CAD_CreateCircle(CAD_GeVec3 center, double radius, CAD_GeVec3 normal, const CAD_CreateOptions* opt,
                                    uint32_t* outId);
/* 세 점 호 — 시작 → 지나는 점 → 끝 */
CAD_API CAD_Status CAD_CreateArc(CAD_GeVec3 start, CAD_GeVec3 through, CAD_GeVec3 end, const CAD_CreateOptions* opt,
                                 uint32_t* outId);
/* 정다각형(닫힌 폴리선) — 꼭짓점이 중심에서 radius(외접원), sides = 3..1024, firstVertexDir = 첫 꼭짓점 방향(평면 안, (0,0,0) = 평면의 첫 축) */
CAD_API CAD_Status CAD_CreatePolygon(CAD_GeVec3 center, double radius, int32_t sides, CAD_GeVec3 normal, CAD_GeVec3 firstVertexDir,
                                     const CAD_CreateOptions* opt, uint32_t* outId);
/* 사각형(닫힌 폴리선) — 맞모서리 두 점. 두 점이 이루는 축 평면(XY·YZ·XZ)에 놓인다 */
CAD_API CAD_Status CAD_CreateRectangle(CAD_GeVec3 corner0, CAD_GeVec3 corner2, const CAD_CreateOptions* opt, uint32_t* outId);
/* 폴리선 — 점 count 개(2 이상), closed = 마지막 → 첫 점까지 */
CAD_API CAD_Status CAD_CreatePolyline(const CAD_GeVec3* points, uint32_t count, bool closed, const CAD_CreateOptions* opt,
                                      uint32_t* outId);
/* 타원 — 중심, 장축 반벡터(중심 → 장축 끝, 길이 = 장반경, 평면 안), 단축비(0 < ratio ≤ 1), 평면 법선 */
CAD_API CAD_Status CAD_CreateEllipse(CAD_GeVec3 center, CAD_GeVec3 majorAxis, double ratio, CAD_GeVec3 normal,
                                     const CAD_CreateOptions* opt, uint32_t* outId);
/* 맞춤점을 지나는 스플라인 — 열린 것은 2점, 닫힌(주기) 것은 3점 이상(최대 100000) */
CAD_API CAD_Status CAD_CreateSpline(const CAD_GeVec3* fitPoints, uint32_t count, bool closed, const CAD_CreateOptions* opt,
                                    uint32_t* outId);

/* ── 폴리선 정점 목록 (PEDIT · AcDbPolyline getPointAt/setPointAt) ──
 * 닫기·열기·반전·정점 넣기/빼기는 전부 "정점 목록을 바꾸는 일" 이라 목록을 통째로 읽고 쓴다. 좌표 = **월드** mm(객체의 이동·회전·축척이
 * 걸린 화면 자리 — 객체 JSON 의 points 와 같다). 폴리선이 아니면 CAD_E_WRONG_TYPE(선·원·호는 CAD_Curve* 로).
 *
 *   int32_t n = CAD_GetPolylinePoints(id, NULL, 0, NULL);     // 개수
 *   CAD_GeVec3* p = malloc(sizeof(CAD_GeVec3) * n);
 *   bool closed = false;
 *   CAD_GetPolylinePoints(id, p, (uint32_t)n, &closed);
 *   ... 고친 뒤 ...
 *   CAD_SetPolylinePoints(id, p, (uint32_t)n, closed);        // 되돌리기 1
 *
 * Get 반환 = 정점 수(capacity 만큼만 채움). Set 은 2점 이상, 잠긴 도면층 = CAD_E_LOCKED. */
CAD_API int32_t    CAD_GetPolylinePoints(uint32_t id, CAD_GeVec3* outPoints, uint32_t capacity, bool* outClosed);
CAD_API CAD_Status CAD_SetPolylinePoints(uint32_t id, const CAD_GeVec3* points, uint32_t count, bool closed);

/* ── 2D 스케치 구동 제약 ─────────────────────────────────────────────
 * 화면에 그리는 CAD_CreateDimension(측정/주석)과 별개로 실제 선·원을 움직인다(대상은 선·원만 — 다른 종류 = CAD_E_WRONG_TYPE).
 * point: 선 0=시작, 1=끝(거리류는 2 = 중점) / 원 0=중심. value = 월드 mm, 각도(CAD_SKETCH_ANGLE) = rad.
 * 단항 제약(수평/수직/반지름/직경/고정)은 entityB=0, pointB=0.
 * 더하기·값 바꾸기가 다른 제약과 부딪쳐 풀 수 없으면 CAD_E_CONFLICT — 아무것도 바뀌지 않고, 부딪친 제약 id 는 CAD_GetLastSketchConflict.
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
    CAD_SKETCH_ANGLE         = 11,  /* 선 A 에서 B 로 재는 부호 있는 각, value 단위 rad */
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
/* 제약 하나 — 출력 구조체: 부르는 쪽이 size = sizeof(CAD_SketchConstraintInfo) 를 채운다(엔진은 그 크기까지만 쓴다) */
typedef struct CAD_SketchConstraintInfo {
    uint32_t size;
    uint32_t id;
    int32_t type;          /* CAD_SKETCH_* */
    uint32_t entityA;
    int32_t pointA;
    uint32_t entityB;
    int32_t pointB;
    double value;          /* mm, 각도 = rad */
    bool driving;
    bool enabled;
} CAD_SketchConstraintInfo;
/* 제약 더하기 — 바로 풀어 형상을 맞춘다, 되돌리기 1. 같은 제약이 이미 있으면 그 id(CAD_OK).
 * 없는 객체 = CAD_E_BAD_HANDLE, 잠김 = CAD_E_LOCKED, 선·원 아님 = CAD_E_WRONG_TYPE, 그 종류에 안 맞는 점·값 = CAD_E_INVALID_ARG */
CAD_API CAD_Status CAD_AddSketchConstraint(int32_t type, uint32_t entityA, int32_t pointA, uint32_t entityB, int32_t pointB,
                                           double value, uint32_t* outId);
/* 값 바꾸기(거리·반지름·직경 > 0, 각도·가로·세로 거리는 부호 있음) — 값 없는 제약 = CAD_E_WRONG_TYPE, 없는 id = CAD_E_BAD_HANDLE */
CAD_API CAD_Status CAD_SetSketchConstraintValue(uint32_t constraintId, double value);
CAD_API CAD_Status CAD_RemoveSketchConstraint(uint32_t constraintId);
/* 장면의 제약 전부를 다시 푼다 — 풀 수 없으면 CAD_E_CONFLICT(형상은 그대로) */
CAD_API CAD_Status CAD_SolveSketchConstraints(void);
CAD_API int32_t    CAD_GetSketchConstraintCount(void);
CAD_API int32_t    CAD_GetSketchConstraintIds(uint32_t* outIds, uint32_t capacity);
CAD_API CAD_Status CAD_GetSketchConstraintInfo(uint32_t constraintId, CAD_SketchConstraintInfo* outInfo);
/* 이 선·원과 제약으로 이어진 묶음의 자유도·구속 상태(CAD_SKETCH_UNDER …). 형상은 바꾸지 않는다.
 * 반환 = 문제가 된 제약 수(충돌·잘못된 참조·중복 — 상태에 따라), outProblemIds 에 capacity 만큼 */
CAD_API int32_t    CAD_GetSketchDiagnosis(uint32_t entityId, int32_t* outDof, int32_t* outStatus, uint32_t* outProblemIds,
                                          uint32_t capacity);
/* 마지막 더하기·값 바꾸기·풀기가 CAD_E_CONFLICT 였을 때 부딪친 제약 id 들 — 반환 = 전체 개수 */
CAD_API int32_t    CAD_GetLastSketchConflict(uint32_t* outIds, uint32_t capacity);

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

/* 기하 곡선으로 새 객체 — 직선 = 선, 원호 = 원·호, 타원호 = 타원, NURBS = 스플라인, 합성 곡선 = 폴리선
 * (엔진 폴리선은 직선 조각만이라 합성 곡선 안 호·타원·NURBS 조각은 원 분할 규칙으로 꺾은선이 된다). 되돌리기 1 */
CAD_API CAD_Status CAD_CreateCurveFromGe(uint64_t curve, const CAD_CreateOptions* opt, uint32_t* outId);

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
