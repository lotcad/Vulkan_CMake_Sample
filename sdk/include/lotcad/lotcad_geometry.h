#pragma once
/* LotCAD C API - geometry  [AcGe (vectors, matrices, planes, lines, arcs, curves, intersection)]
 * Pure geometry: no objects, no scene. Compute first, then create objects in one go.
 * 순수 기하 — 객체·장면을 모른다. 계산해 두었다가 객체는 나중에 한꺼번에 만든다.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h.
 *
 * ★ Threads: every function here may be called from ANY thread, several threads at once, even before CAD_Init.
 *   Many threads may read one curve handle at once; editing functions (Reverse/Transform/Extend) swap the handle's
 *   curve atomically, so a reader sees either the old or the new curve, never half of it.
 *   아무 스레드에서나, 여러 스레드가 동시에, CAD_Init 전에도 부를 수 있다. 장면을 바꾸는 함수(다른 헤더)는 엔진 스레드만.
 * Units: length = world mm (values as given), angle = radian, double precision.
 *
 * Return values (lotcad_types.h):
 *   CAD_Status  0 = CAD_OK, negative = CAD_E_* reason code. Results always come through out-parameters (NULL = not wanted).
 *   int32_t     count functions: >= 0 = the FULL count (at most `capacity` items written; NULL/0 = just ask), < 0 = CAD_E_*.
 *               "Nothing found" is 0, not an error. Functions that return new handles in an array create NOTHING when
 *               capacity is short (no leak) — call again with a bigger array.
 *   The human-readable reason is CAD_GetLastError of the CALLING thread (UI language); success clears it.
 *   반환: CAD_Status = 0 성공·음수 이유 코드, 값은 출력 인자로. 개수 함수 = 0 이상 전체 개수·음수 코드(찾은 것 없음 = 0).
 *   새 핸들을 배열로 주는 함수는 칸이 모자라면 아무것도 만들지 않는다. 사람이 읽을 이유는 부른 스레드의 CAD_GetLastError.
 *
 * Curve parameters follow ObjectARX (AcDbCurve): line = distance from the start (0..length), circle/arc = angle
 * (radian, CCW about the normal from refVec), ellipse = parametric angle, NURBS = knot value, polyline/composite =
 * vertex index (piece i spans i..i+1). Split pieces keep the original parameters where the type allows (line, arc, NURBS).
 * 매개변수 = ObjectARX 와 같다: 선 = 시작부터 거리, 원·호 = 각, 타원 = 매개각, NURBS = 매듭값, 폴리선 = 정점 번호.
 */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif

/* 점·벡터 */
typedef struct CAD_GeVec3 { double x, y, z; } CAD_GeVec3;
/* 평면 — 원점 + 법선(길이는 상관없음, 단위로 맞춰 씀) */
typedef struct CAD_GePlane { double ox, oy, oz, nx, ny, nz; } CAD_GePlane;
/* 4×4 아핀 행렬, 열 우선(m[12..14] = 이동) — glm·Vulkan 과 같은 배치. 점 p' = M·(p,1) */
typedef struct CAD_GeMatrix { double m[16]; } CAD_GeMatrix;
/* 원호 — 점 = 중심 + r(cos t·ref + sin t·(n × ref)), t ∈ [startAngle, endAngle]. 원 = 0..2π. ref 는 n 에 수직으로 맞춰 씀 */
typedef struct CAD_GeArc {
    double cx, cy, cz;
    double nx, ny, nz;
    double rx, ry, rz;
    double radius;
    double startAngle, endAngle;
} CAD_GeArc;
/* 타원호 — 점 = 중심 + a·cos t·major + b·sin t·(n × major) (major 는 단위로 맞춰 씀) */
typedef struct CAD_GeEllipse {
    double cx, cy, cz;
    double nx, ny, nz;
    double mx, my, mz;
    double majorRadius, minorRadius;
    double startAngle, endAngle;
} CAD_GeEllipse;
/* 교차 하나 — (x,y,z) 곡선 1 위 점, (x2,y2,z2) 곡선 2 위 점(투영 교차면 다를 수 있다).
 * overlap ≠ 0 이면 (param1,param2) 부터 (endParam1,endParam2) 까지 겹침 구간, 끝점 (endX,endY,endZ) */
typedef struct CAD_GeIntersection {
    double x, y, z;
    double x2, y2, z2;
    double param1, param2;
    int overlap;
    double endX, endY, endZ;
    double endParam1, endParam2;
} CAD_GeIntersection;

/* 곡선 종류 — CAD_GeCurveGetType */
enum {
    CAD_GECURVE_LINE      = 1,
    CAD_GECURVE_ARC       = 2,   /* 원 = 한 바퀴 호 */
    CAD_GECURVE_ELLIPSE   = 3,
    CAD_GECURVE_NURBS     = 4,
    CAD_GECURVE_COMPOSITE = 5    /* 폴리선·이어 붙인 곡선 */
};
/* 교차 연장 — AcDb::Intersect 와 같다. 연장 = 선은 무한 직선, 원·호·타원은 한 바퀴, 폴리선은 첫·끝 조각(선·호), NURBS 는 연장 안 함 */
enum {
    CAD_GE_EXTEND_NONE = 0,   /* kOnBothOperands */
    CAD_GE_EXTEND_THIS = 1,   /* 곡선 1 만 */
    CAD_GE_EXTEND_ARG  = 2,   /* 곡선 2 만 */
    CAD_GE_EXTEND_BOTH = 3
};
/* 두 벡터 관계 — CAD_GeVectorRelation */
enum {
    CAD_GEVEC_NONE          = 0,
    CAD_GEVEC_CODIRECTIONAL = 1,    /* 나란하고 같은 방향 */
    CAD_GEVEC_OPPOSITE      = 2,    /* 나란하고 반대 방향 */
    CAD_GEVEC_PERPENDICULAR = 3
};
/* 점과 닫힌 곡선 — CAD_GeCurveContainsPoint */
enum {
    CAD_GEPOS_OUTSIDE = 0,
    CAD_GEPOS_ON      = 1,   /* 경계 위(허용치 안) */
    CAD_GEPOS_INSIDE  = 2
};

/* ── 허용치(AcGeContext::gTol) — 프로세스 전체(모든 스레드) 한 벌. 기본 점 1e-5 mm, 벡터 1e-10(1 − cos) ── */
CAD_API CAD_Status CAD_GeSetTolerance(double equalPoint, double equalVector);      /* 둘 다 > 0(아니면 CAD_E_INVALID_ARG) */
CAD_API CAD_Status CAD_GeGetTolerance(double* outEqualPoint, double* outEqualVector);  /* 지금 허용치 */

/* ── 벡터·점 (AcGeVector3d·AcGePoint3d) ── */
/* a → b 각. refAxis 가 0 이면 0..π, 아니면 refAxis 둘레 오른손 방향으로 잰 0..2π. 길이 0 = CAD_E_DEGENERATE */
CAD_API CAD_Status CAD_GeVectorAngle(CAD_GeVec3 a, CAD_GeVec3 b, CAD_GeVec3 refAxis, double* outAngle);
CAD_API CAD_Status CAD_GeVectorRotate(CAD_GeVec3 v, double angle, CAD_GeVec3 axis, CAD_GeVec3* outVector);   /* axis 둘레 오른손 방향 angle(rad) */
CAD_API CAD_Status CAD_GeVectorPerp(CAD_GeVec3 v, CAD_GeVec3* outVector);            /* 수직인 단위 벡터(늘 같은 규칙) */
CAD_API CAD_Status CAD_GeVectorRelation(CAD_GeVec3 a, CAD_GeVec3 b, int* outRelation);  /* CAD_GEVEC_* (허용치 = 벡터 허용치) */
/* 점 p 를 축(axisPoint 를 지나는 axisDir) 둘레로 오른손 방향 angle(rad) 돌린 점 */
CAD_API CAD_Status CAD_GePointRotate(CAD_GeVec3 p, double angle, CAD_GeVec3 axisPoint, CAD_GeVec3 axisDir, CAD_GeVec3* outPoint);
CAD_API CAD_Status CAD_GePointMirror(CAD_GeVec3 p, CAD_GePlane plane, CAD_GeVec3* outPoint);   /* 평면에 비친 점 */
/* 평면에 투영 — dir 이 0 이면 수직, 아니면 dir 방향으로(dir 이 평면과 나란하면 CAD_E_PARALLEL) */
CAD_API CAD_Status CAD_GePointProject(CAD_GeVec3 p, CAD_GePlane plane, CAD_GeVec3 dir, CAD_GeVec3* outPoint);

/* ── 평면 (AcGePlane) ── */
CAD_API CAD_Status CAD_GePlaneFrom3Points(CAD_GeVec3 a, CAD_GeVec3 b, CAD_GeVec3 c, CAD_GePlane* outPlane);   /* 한 줄 = CAD_E_PARALLEL */
CAD_API CAD_Status CAD_GePlaneDistance(CAD_GePlane plane, CAD_GeVec3 p, double* outSignedDistance);        /* 법선 쪽 + */
/* 평면 안 두 축(법선에 수직, 오른손) — 오토캐드 임의 축 규칙(DXF OCS 와 같다) */
CAD_API CAD_Status CAD_GePlaneAxes(CAD_GePlane plane, CAD_GeVec3* outXAxis, CAD_GeVec3* outYAxis);
/* 무한 직선(점 + 방향) ∩ 평면 — outParam = 방향 1 당 매개변수. 나란하면 CAD_E_PARALLEL */
CAD_API CAD_Status CAD_GePlaneIntersectLine(CAD_GePlane plane, CAD_GeVec3 linePoint, CAD_GeVec3 lineDir,
                                            double* outParam, CAD_GeVec3* outPoint);
/* 평면 ∩ 평면 = 직선(점 + 단위 방향). 나란하면 CAD_E_PARALLEL */
CAD_API CAD_Status CAD_GePlaneIntersectPlane(CAD_GePlane a, CAD_GePlane b, CAD_GeVec3* outPoint, CAD_GeVec3* outDir);

/* ── 직선 (AcGeLinearEnt3d) ── */
/* 두 선의 가장 가까운 두 점 — a0→a1 이 매개변수 0→1. segmentA/B = 선분(0..1 안으로). 두 점이 같으면 교점.
 * outParallel = 나란함(그때는 가까운 점 한 쌍을 골라 줌). 길이 0 인 선 = CAD_E_DEGENERATE */
CAD_API CAD_Status CAD_GeLineClosest(CAD_GeVec3 a0, CAD_GeVec3 a1, bool segmentA, CAD_GeVec3 b0, CAD_GeVec3 b1, bool segmentB,
                                     double* outParamA, double* outParamB, CAD_GeVec3* outPointA, CAD_GeVec3* outPointB,
                                     bool* outParallel);

/* ── 행렬 (AcGeMatrix3d) ── */
CAD_API CAD_Status CAD_GeMatrixIdentity(CAD_GeMatrix* outMatrix);                       /* 단위 행렬 */
CAD_API CAD_Status CAD_GeMatrixTranslation(CAD_GeVec3 v, CAD_GeMatrix* outMatrix);       /* v 만큼 옮기기 */
/* center 를 지나는 axis 둘레 오른손 방향 angle(rad) 회전 */
CAD_API CAD_Status CAD_GeMatrixRotation(double angle, CAD_GeVec3 axis, CAD_GeVec3 center, CAD_GeMatrix* outMatrix);
CAD_API CAD_Status CAD_GeMatrixScaling(double scale, CAD_GeVec3 center, CAD_GeMatrix* outMatrix);   /* center 기준 고른 배율 */
CAD_API CAD_Status CAD_GeMatrixMirroring(CAD_GePlane plane, CAD_GeMatrix* outMatrix);              /* 평면 대칭 */
/* 좌표계 → 월드(AcGeMatrix3d::setCoordSystem). 축이 한 평면 = CAD_E_DEGENERATE */
CAD_API CAD_Status CAD_GeMatrixCoordSys(CAD_GeVec3 origin, CAD_GeVec3 xAxis, CAD_GeVec3 yAxis, CAD_GeVec3 zAxis, CAD_GeMatrix* outMatrix);
/* 좌표계 from 에 놓인 것을 좌표계 to 로(alignCoordSys) */
CAD_API CAD_Status CAD_GeMatrixAlignCoordSys(CAD_GeVec3 fromOrigin, CAD_GeVec3 fromX, CAD_GeVec3 fromY, CAD_GeVec3 fromZ,
                                             CAD_GeVec3 toOrigin, CAD_GeVec3 toX, CAD_GeVec3 toY, CAD_GeVec3 toZ, CAD_GeMatrix* outMatrix);
CAD_API CAD_Status CAD_GeMatrixPlaneToWorld(CAD_GePlane plane, CAD_GeMatrix* outMatrix);   /* 평면 좌표(CAD_GePlaneAxes, z = 법선) → 월드 */
CAD_API CAD_Status CAD_GeMatrixWorldToPlane(CAD_GePlane plane, CAD_GeMatrix* outMatrix);   /* PlaneToWorld 의 역 */
CAD_API CAD_Status CAD_GeMatrixInverse(CAD_GeMatrix m, CAD_GeMatrix* outMatrix);              /* 특이 = CAD_E_DEGENERATE */
CAD_API CAD_Status CAD_GeMatrixMultiply(CAD_GeMatrix a, CAD_GeMatrix b, CAD_GeMatrix* outMatrix); /* a·b (b 를 먼저 적용) */
/* 점 여러 개를 한 번에 — xyz = 3 × count, outXyz 도(같은 배열을 줘도 됨). 반환 = count */
CAD_API int32_t CAD_GeTransformPoints(CAD_GeMatrix m, const double* xyz, uint32_t count, double* outXyz, uint32_t outCapacity);
/* 벡터 여러 개 — 점과 같되 이동은 빼고 돌리기·배율만 */
CAD_API int32_t CAD_GeTransformVectors(CAD_GeMatrix m, const double* xyz, uint32_t count, double* outXyz, uint32_t outCapacity);

/* ── 곡선 핸들 (AcGeCurve3d) — 만들기. 다 쓰면 CAD_GeCurveFree ── */
CAD_API CAD_Status CAD_GeCurveCreateLine(CAD_GeVec3 start, CAD_GeVec3 end, uint64_t* outCurve);   /* 매개변수 = 시작부터 거리 */
CAD_API CAD_Status CAD_GeCurveCreateArc(CAD_GeArc arc, uint64_t* outCurve);                        /* radius > 0, start < end ≤ start + 2π */
/* 원(한 바퀴 호, 매개변수 0..2π — 시작 방향은 CAD_GePlaneAxes 의 X 축) */
CAD_API CAD_Status CAD_GeCurveCreateCircle(CAD_GeVec3 center, CAD_GeVec3 normal, double radius, uint64_t* outCurve);
/* start → through → end 를 지나는 호. 세 점이 한 줄 = CAD_E_PARALLEL */
CAD_API CAD_Status CAD_GeCurveCreateArc3Points(CAD_GeVec3 start, CAD_GeVec3 through, CAD_GeVec3 end, uint64_t* outCurve);
/* 두 점 + bulge(LWPOLYLINE 42: tan(포함각/4), + = normal 둘레 반시계) */
CAD_API CAD_Status CAD_GeCurveCreateArcBulge(CAD_GeVec3 start, CAD_GeVec3 end, double bulge, CAD_GeVec3 normal, uint64_t* outCurve);
/* 두 무한 직선(점 + 방향)에 접하는 반지름 r 호 — 두 방향이 가리키는 쪽 사이 칸에. outParamA/B = 접점의 직선 매개변수(방향 1 당) */
CAD_API CAD_Status CAD_GeCurveCreateFillet(CAD_GeVec3 pointA, CAD_GeVec3 dirA, CAD_GeVec3 pointB, CAD_GeVec3 dirB, double radius,
                                           uint64_t* outCurve, double* outParamA, double* outParamB);
CAD_API CAD_Status CAD_GeCurveCreateEllipse(CAD_GeEllipse ellipse, uint64_t* outCurve);   /* 타원·타원호(CAD_GeEllipse) */
/* 폴리선 — xyz = 3 × count. closed 면 끝 → 처음 조각까지(조각 수 = 정점 수) */
CAD_API CAD_Status CAD_GeCurveCreatePolyline(const double* xyz, uint32_t count, bool closed, uint64_t* outCurve);
/* bulge 있는 폴리선(LWPOLYLINE) — bulges[i] = 정점 i → i+1 조각(0 = 직선). bulgeCount = 조각 수(열린 것 count−1, 닫힌 것 count) 또는 0 */
CAD_API CAD_Status CAD_GeCurveCreatePolylineBulge(const double* xyz, uint32_t count, const double* bulges, uint32_t bulgeCount,
                                                  bool closed, CAD_GeVec3 normal, uint64_t* outCurve);
/* NURBS — 매듭 = 제어점 + 차수 + 1, weights 는 비우거나(0 개 = 다항) 제어점 수만큼 */
CAD_API CAD_Status CAD_GeCurveCreateNurbs(int degree, const double* knots, uint32_t knotCount, const double* controlXyz,
                                          uint32_t controlCount, const double* weights, uint32_t weightCount, uint64_t* outCurve);
/* 점들을 지나는 곡선(전역 보간, 현 길이 매개변수) — 차수는 점 수에 맞춰 낮춘다 */
CAD_API CAD_Status CAD_GeCurveCreateInterpolated(const double* xyz, uint32_t count, int degree, uint64_t* outCurve);
/* 곡선들을 끝 → 시작으로 이어(복사) — 이음매가 떨어지면 CAD_E_NOT_CONNECTED. 합성 곡선은 펼쳐 넣는다 */
CAD_API CAD_Status CAD_GeCurveCreateComposite(const uint64_t* curves, uint32_t count, uint64_t* outCurve);
CAD_API CAD_Status CAD_GeCurveCopy(uint64_t curve, uint64_t* outCurve);   /* 같은 곡선의 새 핸들 */
CAD_API CAD_Status CAD_GeCurveFree(uint64_t curve);                      /* 핸들 풀기(이미 푼 것·0 = CAD_E_BAD_HANDLE) */
CAD_API int32_t    CAD_GeCurveLiveCount(void);   /* 살아 있는 핸들 수(새는지 볼 때) */

/* ── 곡선 읽기 ── */
CAD_API CAD_Status CAD_GeCurveGetType(uint64_t curve, int* outType);                       /* CAD_GECURVE_* */
CAD_API CAD_Status CAD_GeCurveGetInterval(uint64_t curve, double* outStartParam, double* outEndParam);   /* 매개변수 구간 */
CAD_API CAD_Status CAD_GeCurveIsClosed(uint64_t curve, bool* outClosed);   /* 끝 = 시작(허용치 안). 선은 늘 열림 */
/* 평면 곡선인가 + 법선(닫힌 곡선은 반시계로 보이는 쪽). 직선은 평면(그에 수직인 아무 법선) */
CAD_API CAD_Status CAD_GeCurveIsPlanar(uint64_t curve, bool* outPlanar, CAD_GeVec3* outNormal);
/* 점·1차·2차 도함수(매개변수 1 당) — AcDbCurve::getPointAtParam·getFirstDeriv·getSecondDeriv */
CAD_API CAD_Status CAD_GeCurveEvaluate(uint64_t curve, double param, CAD_GeVec3* outPoint, CAD_GeVec3* outFirstDeriv,
                                       CAD_GeVec3* outSecondDeriv);
/* 여러 매개변수의 점 — outXyz = 3 × count. 반환 = count */
CAD_API int32_t    CAD_GeCurveEvaluateMany(uint64_t curve, const double* params, uint32_t count, double* outXyz, uint32_t outCapacity);
/* 곡선 위 점의 매개변수(허용치 밖 = CAD_E_NOT_ON_CURVE) — getParamAtPoint */
CAD_API CAD_Status CAD_GeCurveParamAtPoint(uint64_t curve, CAD_GeVec3 p, double* outParam);
/* 가장 가까운 점 — extend = 연장한 경로에서(getClosestPointTo(pt, extend)). outDistance = 그 거리 */
CAD_API CAD_Status CAD_GeCurveClosestPoint(uint64_t curve, CAD_GeVec3 p, bool extend, double* outParam, CAD_GeVec3* outPoint,
                                           double* outDistance);
/* viewDir 방향으로 본 가장 가까운 점(돌려주는 점은 곡선 위 3D) — getClosestPointTo(pt, normal, extend) */
CAD_API CAD_Status CAD_GeCurveClosestPointAlong(uint64_t curve, CAD_GeVec3 p, CAD_GeVec3 viewDir, bool extend,
                                                double* outParam, CAD_GeVec3* outPoint);
/* 수직점 — 점 p 에서 곡선에 내린 수선의 발 전부(가까운 것부터) — getNormalPoint · OSNAP 수직. 끝점은 수직일 때만 */
CAD_API int32_t    CAD_GeCurvePerpendicularPoints(uint64_t curve, CAD_GeVec3 p, bool extend, double* outParams, uint32_t capacity);
/* 접점 — 점 p 에서 그은 접선이 곡선에 닿는 곳(평면 법선 planeNormal, 0 이면 곡선 평면) — OSNAP 접점 */
CAD_API int32_t    CAD_GeCurveTangentPoints(uint64_t curve, CAD_GeVec3 p, CAD_GeVec3 planeNormal, double* outParams, uint32_t capacity);
/* 두 곡선의 가장 가까운 두 점(만나면 거리 0) — getClosestPointTo(curve) */
CAD_API CAD_Status CAD_GeCurveClosestToCurve(uint64_t curve1, uint64_t curve2, double* outParamA, double* outParamB,
                                             double* outDistance);
/* 두 매개변수 사이 길이(getDistAtParam 은 fromParam = 시작). 구간 밖 = CAD_E_OUT_OF_RANGE */
CAD_API CAD_Status CAD_GeCurveLength(uint64_t curve, double fromParam, double toParam, double* outLength);
/* fromParam 에서 곡선을 따라 length(음수 = 거꾸로) 간 곳 — getParamAtDist. 끝을 넘으면 끝에서 멈춤 */
CAD_API CAD_Status CAD_GeCurveParamAtLength(uint64_t curve, double fromParam, double length, double* outParam);
/* 곡선 ↔ 현 거리 ≤ chordTolerance 가 되게 나눈 매개변수(양 끝 포함) — 그리기·다른 계산용 표본 */
CAD_API int32_t    CAD_GeCurveSampleParams(uint64_t curve, double chordTolerance, double* outParams, uint32_t capacity);
CAD_API CAD_Status CAD_GeCurveGetBox(uint64_t curve, CAD_GeVec3* outMin, CAD_GeVec3* outMax);   /* 꼭 맞는 상자 */
/* 닫힌 평면 곡선 넓이 — getArea. 열림 = CAD_E_NOT_CLOSED, 비평면 = CAD_E_NOT_PLANAR */
CAD_API CAD_Status CAD_GeCurveArea(uint64_t curve, double* outArea);
/* 점이 닫힌 평면 곡선 안인가(곡선 평면에 투영해서) — CAD_GEPOS_* */
CAD_API CAD_Status CAD_GeCurveContainsPoint(uint64_t curve, CAD_GeVec3 p, int* outPosition);
CAD_API CAD_Status CAD_GeCurveGetLine(uint64_t curve, CAD_GeVec3* outStart, CAD_GeVec3* outEnd);   /* 선이 아니면 CAD_E_WRONG_TYPE */
CAD_API CAD_Status CAD_GeCurveGetArc(uint64_t curve, CAD_GeArc* outArc);              /* 원·호가 아니면 CAD_E_WRONG_TYPE */
CAD_API CAD_Status CAD_GeCurveGetEllipse(uint64_t curve, CAD_GeEllipse* outEllipse);  /* 타원이 아니면 CAD_E_WRONG_TYPE */
CAD_API int32_t    CAD_GeCurveGetPieceCount(uint64_t curve);                               /* 합성 곡선 조각 수(그 밖은 1) */
CAD_API CAD_Status CAD_GeCurveGetPiece(uint64_t curve, uint32_t index, uint64_t* outPiece);  /* 조각 사본(새 핸들) */
CAD_API CAD_Status CAD_GeCurveGetNurbsInfo(uint64_t curve, int* outDegree, uint32_t* outControlCount, uint32_t* outKnotCount,
                                           bool* outRational);   /* NURBS 핸들만 */
/* NURBS 데이터 — 칸은 점 수·매듭 수·무게 수 단위. 하나라도 모자라면 CAD_E_BUFFER_TOO_SMALL(아무것도 안 씀). 다항이면 무게는 전부 1 */
CAD_API CAD_Status CAD_GeCurveGetNurbsData(uint64_t curve, double* outControlXyz, uint32_t controlCapacity, double* outKnots,
                                           uint32_t knotCapacity, double* outWeights, uint32_t weightCapacity);
CAD_API CAD_Status CAD_GeCurveToNurbs(uint64_t curve, uint64_t* outCurve);   /* 같은 곡선의 NURBS(새 핸들, 선·원·타원은 정확) */

/* ── 곡선 바꾸기(그 핸들의 곡선을 바꿔 끼움) ── */
CAD_API CAD_Status CAD_GeCurveReverse(uint64_t curve);   /* 방향 뒤집기(시작 ↔ 끝) — reverseCurve */
/* 닮음 변환이면 원·호·타원 그대로, 아니면 그 부분은 NURBS 가 된다(정확, 매개변수 바뀜) */
CAD_API CAD_Status CAD_GeCurveTransform(uint64_t curve, CAD_GeMatrix m);
/* 끝을 경로 위 점까지 늘인다 — 선·원호·타원·폴리선(첫·끝 조각이 선·호) — extend(start, pt).
 * 경로 밖 = CAD_E_NOT_ON_CURVE, 지금 곡선 위 = CAD_E_INVALID_ARG, NURBS = CAD_E_NOT_SUPPORTED */
CAD_API CAD_Status CAD_GeCurveExtendToPoint(uint64_t curve, bool atStart, CAD_GeVec3 toPoint);
CAD_API CAD_Status CAD_GeCurveExtendToParam(uint64_t curve, double newParam);   /* 구간 밖 매개변수까지 — extend(param) */

/* ── 새 곡선 ── */
/* fromParam < toParam 부분의 새 곡선(매개변수 그대로). 선·호·타원은 구간 밖까지(연장), NURBS·폴리선은 구간 안만(밖 = CAD_E_OUT_OF_RANGE) */
CAD_API CAD_Status CAD_GeCurveSubCurve(uint64_t curve, double fromParam, double toParam, uint64_t* outCurve);
/* 나누기 — 열린 곡선: 시작→p1→…→끝, 닫힌 곡선: p1→…→pn→(이음매를 지나)p1. 끝·같은 값은 버린다 — getSplitCurves */
CAD_API int32_t CAD_GeCurveSplit(uint64_t curve, const double* params, uint32_t count, uint64_t* outCurves, uint32_t capacity);
/* 오프셋 — planeNormal 평면 안에서(0 이면 곡선 평면), distance > 0 = 진행 방향 오른쪽(반시계 닫힌 곡선이면 바깥, 호는 반지름 + d).
 * 선·호 정확, 타원·NURBS 는 NURBS 근사(허용치 안), 폴리선은 이음매를 교점까지 늘이거나 자르고 안 만나면 둥글게 — getOffsetCurvesGivenPlaneNormal */
CAD_API int32_t CAD_GeCurveOffset(uint64_t curve, double distance, CAD_GeVec3 planeNormal, uint64_t* outCurves, uint32_t capacity);
/* 교차점 — extendMode = CAD_GE_EXTEND_*, viewDir ≠ 0 이면 그 방향으로 본 교차(높이가 달라도 만남). 결과는 곡선 1 매개변수 순 */
CAD_API int32_t CAD_GeCurveIntersect(uint64_t curve1, uint64_t curve2, int extendMode, CAD_GeVec3 viewDir,
                                     CAD_GeIntersection* outHits, uint32_t capacity);
/* 곡선 ∩ 평면 — 지나는 점과 닿는 점의 매개변수(곡선이 평면 안에 누우면 0 개) */
CAD_API int32_t CAD_GeCurveIntersectPlane(uint64_t curve, CAD_GePlane plane, double* outParams, uint32_t capacity);

#ifdef __cplusplus
}
#endif
