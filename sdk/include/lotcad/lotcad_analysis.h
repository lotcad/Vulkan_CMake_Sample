#pragma once
/* LotCAD C API - analysis  [(simulation)]
 * Wind tunnel, water, cloth, structural/thermal/modal/buckling analysis.
 * 바람 터널·물·천·구조/열/모드/좌굴 해석.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"
#include "lotcad_geometry.h"   /* CAD_GeVec3 */

#ifdef __cplusplus
extern "C" {
#endif
/* 해석 — MCP 도구 wind_tunnel · water · structural_analysis 와 같은 창구(엔진 windTunnelOp·waterOp·simOp). argsJson = {"op": …, …}
 * (없으면 status), 결과 JSON(ok·error·message·상태)을 outUtf8 에(cap 바이트, null 이면 길이만). 반환 = 길이, 실패 -1.
 * 켜기(start)는 다음 프레임에, 구조 해석 풀이(run·converge)는 작업 스레드에서 — status 로 끝을 본다.
 * 2회 호출(outUtf8 null 로 길이 → 버퍼)은 첫 호출에서 한 번만 실행하고, 같은 인자의 다음 호출엔 그 결과를 준다.
 *  바람 터널: status · start {ids|id, grid fast|normal|fine, wind 0.02~0.10} · stop · reset · pause · play ·
 *             view {field speed|pressure|vortex|smoke, plane x|y|z, at 0~1, smoke, surface} · wind {value}      — 바람은 +X
 *  물:        status · start {id(그릇), level 0~1, grid} · stop · reset · pause · play · tilt {x, y 도} · shake {amplitude 0~1, period}
 *  구조 해석: status(faces = 면 번호·넓이·가운데·법선) · open {id} · close · clear · run · cancel · converge(요소 × 0.7 로 한 번 더) ·
 *             set {type stress|heat|modal|buckling, material, size, units mm|m, modes, thermal, ref_temp, wind, wind_speed, show, scale, animate} ·
 *             fix|free {face} · force {face, force[3] N} · pressure {face, value MPa} · temp {face, value °C} · flux {face, value W} · convect {face, h, ambient}
 *             face = 번호 또는 그 면 가까운 점 [x,y,z]. 결과는 status 의 result(응력·변위·안전율·온도·진동수·좌굴 배수·convergence). */

CAD_API int      CAD_WindTunnel(const char* argsJson, char* outUtf8, int cap);
CAD_API int      CAD_Water(const char* argsJson, char* outUtf8, int cap);
CAD_API int      CAD_StructuralAnalysis(const char* argsJson, char* outUtf8, int cap);

/* ── 구조 해석 — 값 함수 (CAD_Sim*) ──────────────────────────────────────
 * 닫힌 솔리드 하나를 2차 사면체(tet10)로 나눠 선형 탄성·열전도·모드(고유진동)·좌굴을 푼다. 위 JSON 창구(CAD_StructuralAnalysis · MCP
 * structural_analysis)와 같은 해석이라 어느 쪽으로 바꿔도 같은 상태다(패널에도 그대로 보인다).
 * 흐름: CAD_SimOpen(id) → CAD_SimSetOptions → CAD_SimGetFaces 로 면 번호 → CAD_SimSetCondition(고정·하중) → CAD_SimRun →
 *       CAD_SimWait(풀이는 작업 스레드 — CAD_Tick 을 돌리지 않아도 기다릴 수 있다) → CAD_SimGetSummary · CAD_SimGetNodes · CAD_SimGetNodeField …
 * 단위: 길이·좌표·변위 = 장면 단위(월드, double — 해석은 mm 로 하고 돌려줄 때 장면 단위로, 설정 units 가 m 이면 장면 1 = 1 m),
 *       응력 MPa · 힘 N · 온도 °C · 열 W · 열유속 W/m² · 진동수 Hz. 넓이 = 장면 단위².
 * 새 규칙: CAD_Status / 개수 함수 = int32_t 전체 개수(값 배열은 값 개수 — 함수마다 적음), 실패 이유 = CAD_GetLastError.
 * 대상을 안 열었음·결과 없음 = CAD_E_NOT_READY, 풀이 중에 설정·조건·대상을 바꾸면 CAD_E_BUSY. 엔진 스레드에서만(아니면 CAD_E_WRONG_THREAD).
 * 결과는 설정·조건을 바꾸거나 대상 솔리드를 옮기면 지워진다. 출력 구조체(CAD_SimState·CAD_SimSummary)는 부르는 쪽이 size = sizeof 를
 * 채워 넘긴다(엔진은 그 크기까지만 쓴다 — 새 칸은 끝에만 붙는다). */

enum {   /* 해석 종류 */
    CAD_SIM_STRESS   = 0,   /* 정적 구조(응력·변위·안전율) */
    CAD_SIM_HEAT     = 1,   /* 정상 열전도(온도·열유속) */
    CAD_SIM_MODAL    = 2,   /* 고유진동(진동수·모드 모양) — 고정 조건만 씀 */
    CAD_SIM_BUCKLING = 3    /* 선형 좌굴(하중 배수·모양) — 고정 + 하중 */
};
enum {   /* 재료 — CUSTOM 이면 CAD_SimOptions 의 값 여섯 개 */
    CAD_SIM_MAT_STEEL     = 0,     /* 강철 S275 */
    CAD_SIM_MAT_ALUMINUM  = 1,     /* 알루미늄 6061-T6 */
    CAD_SIM_MAT_STAINLESS = 2,     /* 스테인리스 304 */
    CAD_SIM_MAT_TITANIUM  = 3,     /* 티타늄 Ti-6Al-4V */
    CAD_SIM_MAT_ABS       = 4,     /* ABS 수지 */
    CAD_SIM_MAT_CUSTOM    = 100
};
enum {   /* 메시 크기 — elementSize 가 0 일 때 */
    CAD_SIM_MESH_NORMAL = 0,   /* 사면체 약 5만 */
    CAD_SIM_MESH_FAST   = 1,   /* 약 1.5만 */
    CAD_SIM_MESH_FINE   = 2    /* 약 15만 */
};
enum {   /* 장면 길이 단위 */
    CAD_SIM_UNITS_AUTO = 0,    /* 대상 대각선이 200 넘으면 mm, 아니면 m */
    CAD_SIM_UNITS_MM   = 1,
    CAD_SIM_UNITS_M    = 2
};
/* 해석 설정 — CAD_SimGetOptions 로 읽어 고친 뒤 CAD_SimSetOptions 로(NULL = 전부 기본값). 맨 앞 size = sizeof, 새 칸은 끝에만.
 * 기본: 구조 · 강철 · 보통 메시 · 단위 자동 · 모드 6개 · 열 하중 끔(기준 20 °C) · 바람 하중 끔(30 m/s) */
typedef struct CAD_SimOptions {
    uint32_t size;
    int32_t  type;                    /* CAD_SIM_STRESS·HEAT·MODAL·BUCKLING */
    int32_t  material;                /* CAD_SIM_MAT_* */
    double   youngsModulus;           /* CUSTOM: 탄성 계수 E (MPa) */
    double   poissonRatio;            /* CUSTOM: 푸아송 비 0 ≤ ν < 0.5 */
    double   yieldStrength;           /* CUSTOM: 항복 응력 (MPa) — 안전율 */
    double   density;                 /* CUSTOM: 밀도 (kg/m³) — 모드 질량 */
    double   conductivity;            /* CUSTOM: 열전도율 W/(m·K) */
    double   expansion;               /* CUSTOM: 열팽창 계수 (1/K) — 열 하중 */
    int32_t  meshQuality;             /* CAD_SIM_MESH_* */
    double   elementSize;             /* 요소 크기 mm(해석 길이) — 0 = meshQuality 로 */
    int32_t  units;                   /* CAD_SIM_UNITS_* (읽을 땐 정해진 MM 또는 M) */
    int32_t  modeCount;               /* 모드·좌굴 모양 수 1~30 — 0 = 6 */
    bool     thermalLoad;             /* 구조 해석에 열 조건(TEMPERATURE·HEAT_FLOW·CONVECTION)으로 먼저 푼 온도를 하중으로(열응력) */
    double   referenceTemperature;    /* 열 하중 — 응력 없는 온도 °C(이 칸은 0 도 그 값) */
    bool     windLoad;                /* 구조·좌굴 해석에 바람 터널(같은 솔리드로 켜 둔)의 표면 압력을 하중으로 */
    double   windSpeed;               /* 바람 하중 m/s — 0 = 30 */
} CAD_SimOptions;

enum {   /* 조건 종류 — 1~3 은 구조(STRESS·MODAL·BUCKLING), 4~6 은 열(HEAT, 열 하중) */
    CAD_SIM_FIX         = 1,   /* 고정 — fixAxes 의 축만(0 = 세 축 모두) */
    CAD_SIM_FORCE       = 2,   /* 면 전체에 넓이 비례로 나눈 힘 (fx, fy, fz) N */
    CAD_SIM_PRESSURE    = 3,   /* 압력 value MPa(+ = 면을 누름) */
    CAD_SIM_TEMPERATURE = 4,   /* 온도 고정 value °C */
    CAD_SIM_HEAT_FLOW   = 5,   /* 들어오는 열 value W(넓이 비례, 음수 = 빠져나감) */
    CAD_SIM_CONVECTION  = 6    /* 대류 h = value W/(m²·K), 바깥 온도 ambient °C */
};
enum { CAD_SIM_AXIS_X = 1, CAD_SIM_AXIS_Y = 2, CAD_SIM_AXIS_Z = 4 };
/* 면 조건 하나 — 한 면엔 구조 조건 하나와 열 조건 하나까지(같은 쪽을 다시 주면 바꿈) */
typedef struct CAD_SimCondition {
    int32_t  face;         /* CAD_SimGetFaces 의 번호 */
    int32_t  kind;         /* CAD_SIM_FIX … CAD_SIM_CONVECTION */
    uint32_t fixAxes;      /* FIX: CAD_SIM_AXIS_* 합(0 = 세 축) */
    double   fx, fy, fz;   /* FORCE: N(월드 방향) */
    double   value;        /* PRESSURE MPa · TEMPERATURE °C · HEAT_FLOW W · CONVECTION W/(m²·K) */
    double   ambient;      /* CONVECTION 바깥 온도 °C */
} CAD_SimCondition;
/* 면 하나 — 30° 넘게 꺾인 곳에서 나눈 면(번호 = 배열 자리). 넓이 장면 단위², 가운데·바깥 법선은 월드 */
typedef struct CAD_SimFace {
    double area;
    double cx, cy, cz;
    double nx, ny, nz;
} CAD_SimFace;

enum {   /* 진행 단계(CAD_SimState::stage) */
    CAD_SIM_STAGE_IDLE = -1, CAD_SIM_STAGE_MESH = 0, CAD_SIM_STAGE_CURVE = 1, CAD_SIM_STAGE_ASSEMBLE = 2, CAD_SIM_STAGE_SOLVE = 3
};
/* 지금 상태 — 부르는 쪽이 size = sizeof(CAD_SimState) */
typedef struct CAD_SimState {
    uint32_t size;
    bool     open;             /* 해석 대상이 열려 있음 */
    uint32_t target;           /* 대상 객체 id(없으면 0) */
    int32_t  faceCount;
    int32_t  conditionCount;   /* 구조 + 열 조건 */
    bool     busy;             /* 풀이 중(작업 스레드) */
    int32_t  stage;            /* CAD_SIM_STAGE_* */
    double   fraction;         /* 그 단계 진행 0~1, 모르면 −1 */
    bool     hasResult;
    int32_t  resultType;       /* 결과의 CAD_SIM_* (없으면 −1) */
    bool     lastRunFailed;    /* 마지막 풀이가 실패함 — 이유는 CAD_SimWait 가 돌려준다 */
} CAD_SimState;

/* 결과 요약 — 부르는 쪽이 size = sizeof(CAD_SimSummary). 그 종류에 없는 값은 NaN(번호 −1, 개수 0) */
typedef struct CAD_SimSummary {
    uint32_t size;
    int32_t  type;                       /* CAD_SIM_* */
    int32_t  nodeCount, elementCount, boundaryTriangleCount;
    double   elementSize;                /* 쓴 요소 크기 mm(해석 길이) */
    double   minDihedralDeg;             /* 가장 납작한 사면체의 이면각 ° */
    double   meshSeconds, solveSeconds;
    /* 구조 */
    double   maxVonMises;                /* MPa */
    double   maxDisplacement;            /* 장면 단위 */
    double   safetyFactor;               /* 항복 ÷ 최대 von Mises */
    int32_t  maxVonMisesNode, maxDisplacementNode;
    double   appliedX, appliedY, appliedZ;     /* 준 하중 합 N */
    double   reactionX, reactionY, reactionZ;  /* 고정 면 반력 합 N */
    double   strainEnergy;               /* N·mm */
    /* 열(열 하중 구조 해석이면 그 온도) */
    double   minTemperature, maxTemperature;   /* °C */
    double   maxHeatFlux;                /* W/m² */
    double   heatIn, heatFixed, heatConvection;   /* W — 넣은 열·온도 고정 면·대류 면으로 들어온 열(합 ≈ 0) */
    /* 모드·좌굴 */
    int32_t  modeCount;                  /* CAD_SimGetModes 개수 */
    /* 바람 하중 */
    double   windForceX, windForceY, windForceZ;   /* N */
    double   windCpMin, windCpMax;
    /* 수렴 확인(CAD_SimRunOptions::checkConvergence) */
    int32_t  convergenceCount;           /* CAD_SimGetConvergence 개수 */
    double   coarseElementSize;          /* 처음 메시 요소 크기 mm(결과는 × 0.7 로 잘게 푼 쪽) */
    int32_t  coarseElementCount;
} CAD_SimSummary;

enum {   /* 절점 값(CAD_SimGetNodeField) — 절점마다 값 개수 */
    CAD_SIM_FIELD_DISPLACEMENT = 1,   /* 3 — 장면 단위 */
    CAD_SIM_FIELD_VON_MISES    = 2,   /* 1 — MPa */
    CAD_SIM_FIELD_STRESS       = 3,   /* 6 — MPa, xx yy zz xy yz zx */
    CAD_SIM_FIELD_SAFETY       = 4,   /* 1 — 항복 ÷ von Mises(응력 0 이면 무한대) */
    CAD_SIM_FIELD_TEMPERATURE  = 5,   /* 1 — °C(열 해석 또는 열 하중 구조 해석) */
    CAD_SIM_FIELD_HEAT_FLUX    = 6    /* 3 — W/m²(열 해석) */
};
enum {   /* 수렴 확인에서 견준 값 */
    CAD_SIM_METRIC_MAX_VON_MISES = 1, CAD_SIM_METRIC_MAX_DISPLACEMENT = 2, CAD_SIM_METRIC_MAX_TEMPERATURE = 3,
    CAD_SIM_METRIC_MIN_TEMPERATURE = 4, CAD_SIM_METRIC_MAX_HEAT_FLUX = 5, CAD_SIM_METRIC_FREQUENCY = 6, CAD_SIM_METRIC_LOAD_FACTOR = 7
};
/* 수렴 확인 하나 — 처음 메시(coarse)와 요소 × 0.7(fine)의 값, change = fine ÷ coarse − 1 (변위는 장면 단위) */
typedef struct CAD_SimConvergence {
    int32_t metric;   /* CAD_SIM_METRIC_* */
    double  coarse, fine, change;
} CAD_SimConvergence;
/* CAD_SimRun 의 선택 — NULL = 한 번 풀기. 맨 앞 size = sizeof, 새 칸은 끝에만 */
typedef struct CAD_SimRunOptions {
    uint32_t size;
    bool     checkConvergence;   /* 같은 조건을 요소 크기 × 0.7 로 한 번 더 풀어 대표 값이 얼마나 바뀌는지(결과는 잘게 푼 쪽) */
} CAD_SimRunOptions;

/* 닫힌 메시 솔리드 id 를 해석 대상으로 연다(패널도 켬). 열린 동안 선택이 바뀌어도 대상은 그대로.
 * 없는 id = CAD_E_BAD_HANDLE, 메시가 아님 = CAD_E_WRONG_TYPE, 닫히지 않음 = CAD_E_NOT_CLOSED(meshfix 로 먼저),
 * 다른 대상에 조건·결과가 있음 = CAD_E_BUSY(CAD_SimClear 먼저). 같은 id 를 다시 열면 그대로(조건 유지) */
CAD_API CAD_Status CAD_SimOpen(uint32_t id);

CAD_API CAD_Status CAD_SimClose(void);     /* 해석을 닫는다(조건·결과·패널) — 풀이 중이면 멈추고 닫음 */
CAD_API CAD_Status CAD_SimClear(void);     /* 조건과 결과를 지운다(대상·설정은 그대로) */
CAD_API CAD_Status CAD_SimGetOptions(CAD_SimOptions* out);   /* 지금 설정 — 부르는 쪽이 out->size = sizeof */
/* 설정을 통째로 바꾼다(NULL = 기본값) — 바뀌면 결과를 지운다. 범위 밖 값 = CAD_E_INVALID_ARG(아무것도 안 바꿈). 대상 없이도 된다 */
CAD_API CAD_Status CAD_SimSetOptions(const CAD_SimOptions* opt);
/* 대상의 면 — 반환 = 면 개수 */
CAD_API int32_t    CAD_SimGetFaces(CAD_SimFace* outFaces, uint32_t capacity);
/* 점(월드)에서 가장 가까운 면의 번호 */
CAD_API CAD_Status CAD_SimFindFace(CAD_GeVec3 point, int32_t* outFace);
/* 면 조건 주기·바꾸기 — 결과를 지운다. 면 번호 범위 밖 = CAD_E_OUT_OF_RANGE, 종류·값이 맞지 않음 = CAD_E_INVALID_ARG */
CAD_API CAD_Status CAD_SimSetCondition(CAD_SimCondition condition);
/* 면 조건 지우기 — kind 의 쪽(구조 1~3 · 열 4~6)만, 0 = 둘 다. 조건이 없던 면이면 그대로 CAD_OK */
CAD_API CAD_Status CAD_SimClearCondition(int32_t face, int32_t kind);
/* 지금 조건 — 구조 조건(면 순) 다음 열 조건(면 순). 반환 = 개수 */
CAD_API int32_t    CAD_SimGetConditions(CAD_SimCondition* outConditions, uint32_t capacity);
/* 풀이 시작(작업 스레드 — 바로 돌아온다). 고정이 없음·하중이 없음 등 = CAD_E_INVALID_ARG, 해석 모듈 없음 = CAD_E_NOT_SUPPORTED */
CAD_API CAD_Status CAD_SimRun(const CAD_SimRunOptions* opt);

CAD_API CAD_Status CAD_SimCancel(void);    /* 풀이 멈춤(멈춘 뒤 CAD_SimWait 는 CAD_E_FAILED "멈춤") — 풀이 중이 아니면 그대로 CAD_OK */
/* 풀이가 끝나기를 기다린다 — timeoutSeconds < 0 = 끝날 때까지, 0 = 기다리지 않고 보기만. 끝났으면 결과를 바로 받는다(CAD_Tick 불필요).
 * CAD_OK + *outDone: 참 = 결과 있음, 거짓 = 아직 도는 중(시간 다 됨). 마지막 풀이 실패 = CAD_E_FAILED + 이유, 푼 적 없음 = CAD_E_NOT_READY */
CAD_API CAD_Status CAD_SimWait(double timeoutSeconds, bool* outDone);

CAD_API CAD_Status CAD_SimGetState(CAD_SimState* out);       /* 부르는 쪽이 out->size = sizeof */
CAD_API CAD_Status CAD_SimGetSummary(CAD_SimSummary* out);   /* 결과 요약 — 부르는 쪽이 out->size = sizeof. 결과 없음 = CAD_E_NOT_READY */
/* 절점 자리(월드, 장면 단위) — 앞쪽이 사면체 꼭짓점, 뒤쪽이 변 가운데 절점. 반환 = 절점 개수 */
CAD_API int32_t    CAD_SimGetNodes(CAD_GeVec3* outNodes, uint32_t capacity);
/* 사면체 — 사면체마다 절점 번호 10개(VTK 2차 사면체 순서: 꼭짓점 0~3, 가운데 4 (0,1)·5 (1,2)·6 (0,2)·7 (0,3)·8 (1,3)·9 (2,3)).
 * 반환 = 값 개수(사면체 × 10) */
CAD_API int32_t    CAD_SimGetElements(uint32_t* outNodeIndices, uint32_t capacity);
/* 표면 2차 삼각형 — 삼각형마다 절점 번호 6개(꼭짓점 0~2, 가운데 (0,1)·(1,2)·(2,0)). 반환 = 값 개수(삼각형 × 6) */
CAD_API int32_t    CAD_SimGetBoundary(uint32_t* outNodeIndices, uint32_t capacity);
/* 표면 삼각형마다 면 번호(CAD_SimGetBoundary 와 같은 차례). 반환 = 삼각형 개수 */
CAD_API int32_t    CAD_SimGetBoundaryFaces(int32_t* outFaces, uint32_t capacity);
/* 절점 값 — field = CAD_SIM_FIELD_*(절점마다 값 개수는 그 enum 에, 절점 순서 = CAD_SimGetNodes). 반환 = 값 개수(절점 × 개수).
 * 그 결과에 없는 값(열 해석의 응력 …) = CAD_E_NOT_READY */
CAD_API int32_t    CAD_SimGetNodeField(int32_t field, double* outValues, uint32_t capacity);
/* 모드 해석 = 진동수 Hz(작은 것부터), 좌굴 = 하중 배수(준 하중의 몇 배에서 꺾이나, 작은 것부터). 반환 = 개수 */
CAD_API int32_t    CAD_SimGetModes(double* outValues, uint32_t capacity);
/* 모드(좌굴) 모양 mode(0부터) — 절점마다 방향(가장 큰 크기 1, 단위 없음). 반환 = 절점 개수 */
CAD_API int32_t    CAD_SimGetModeShape(int32_t mode, CAD_GeVec3* outShape, uint32_t capacity);
/* 열 해석에서 그 면으로 들어온 열 W(조건 없는 면 = 단열이라 0) */
CAD_API CAD_Status CAD_SimGetFaceHeat(int32_t face, double* outWatts);
/* 수렴 확인 결과 — 반환 = 개수(수렴 확인을 안 했으면 0) */
CAD_API int32_t    CAD_SimGetConvergence(CAD_SimConvergence* outItems, uint32_t capacity);

/* ── 바람 터널 — 값 함수 (CAD_Wind*) ─────────────────────────────────────
 * 고른 솔리드 둘레(또는 관 안)의 공기를 GPU 격자 볼츠만으로 흘린다. 바람은 +X 로 분다. 위 JSON 창구(CAD_WindTunnel · MCP wind_tunnel)·
 * 명령 cfd·패널과 같은 세션이라 어느 쪽으로 바꿔도 같은 상태다.
 * 흐름: CAD_WindOpen(ids) → CAD_Tick 을 돌리거나 CAD_WindAdvance(걸음) → CAD_WindGetState(Cd·힘 계수) · CAD_WindSample · CAD_WindGetCellField …
 * 단위: 좌표·칸 크기 = 장면 단위(월드). 흐름은 격자 단위로 계산해 물리 단위가 없다 — 바람 세기 = 격자 단위 입구 속도(0.01~0.12, 기본 0.06),
 *       속도 결과 = 바람 대비(1 = 입구 바람), 압력 = 압력 계수 Cp = (p − p∞) ÷ ½ρU², 힘 = 앞면 넓이 기준 힘 계수.
 *       레이놀즈 수는 격자 값(100 안팎)이라 실제 크기 물체와 박리 자리가 다를 수 있다(둔한 물체의 압력·항력 어림에 알맞다).
 * 새 규칙: CAD_Status / 개수 함수 = int32_t 전체 개수. 꺼져 있음 = CAD_E_NOT_READY, 유체 해석 모듈(LotCADCfd)이 없음 = CAD_E_NOT_SUPPORTED.
 * 엔진 스레드에서만. 솔리드를 옮기면 고체 칸을 다시 맞추고(흐름은 이어짐), 격자를 벗어나면 격자를 새로 만든다(흐름은 처음부터). */

enum {   /* 격자 크기 */
    CAD_WIND_GRID_NORMAL = 0,   /* 약 100만 칸 */
    CAD_WIND_GRID_FAST   = 1,   /* 약 25만 칸 */
    CAD_WIND_GRID_FINE   = 2    /* 약 250만 칸 */
};
/* 바람 터널 설정 — 맨 앞 size = sizeof, 새 칸은 끝에만. NULL = 기본값(보통 격자 · 바람 0.06 · 바깥 흐름) */
typedef struct CAD_WindOptions {
    uint32_t size;
    int32_t  grid;    /* CAD_WIND_GRID_* — 도는 중에 바꾸면 같은 솔리드로 처음부터 */
    double   wind;    /* 격자 단위 입구 속도 0.01~0.12, 0 = 0.06 — 도는 중에도 바로 바뀐다 */
    bool     pipe;    /* 관 안 흐름: 관 끝(평평한 고리 면 안의 구멍) 중 가장 −X 쪽이 입구, 나머지가 출구, 관 안만 흐른다. 바꾸면 처음부터 */
} CAD_WindOptions;

/* 지금 상태 — 부르는 쪽이 size = sizeof(CAD_WindState). 꺼져 있어도 CAD_OK(active 거짓) */
typedef struct CAD_WindState {
    uint32_t   size;
    bool       active;            /* 흐름 세션이 있음 */
    bool       starting;          /* 켜기를 받아 다음 CAD_Tick 에 켜짐(그리는 중에 부른 CAD_WindOpen) */
    bool       running;           /* 걸음이 나아감(CAD_WindSetRunning 거짓 = 멈춤 — CAD_WindAdvance 는 멈춤에도 된다) */
    bool       failed;            /* 계산이 멈춤(발산·장치 오류) 또는 켜기 실패 — 이유는 CAD_WindAdvance 가 CAD_E_FAILED 로 */
    bool       pipe;              /* 관 안 흐름 */
    int64_t    steps;             /* 흘린 걸음 */
    double     stepsPerSecond;    /* 틱으로 돌 때의 초당 걸음 */
    int32_t    nx, ny, nz;        /* 격자 칸 수 */
    double     cellSize;          /* 칸 한 변(장면 단위) */
    CAD_GeVec3 origin;            /* 격자 구석(월드) — 칸 (i,j,k) 가운데 = origin + (i+½, j+½, k+½) × cellSize */
    double     wind;              /* 격자 단위 입구 속도 */
    double     reynolds;          /* 격자 레이놀즈 수(바람 방향 길이 기준, 관 안이면 입구 지름) */
    double     dragCoefficient;   /* 앞면 넓이 기준 항력 계수 Cd — 걸음마다 부드럽게 맞춘 값, 아직 없거나 관 안이면 NaN(수천 걸음 뒤 자리 잡음) */
    CAD_GeVec3 forceCoefficient;  /* 마지막 걸음의 힘 계수 (Cx 항력, Cy 옆, Cz 들림) — 앞면 넓이 기준, 관 안이면 NaN */
    double     frontalArea;       /* 앞면 넓이(장면 단위², 바람 쪽으로 비친 고체 칸) */
    int32_t    objectCount;       /* 바람을 맞는 솔리드 수 */
    int32_t    pipeOpenings;      /* 관 안: 관 끝 수(입구 1 + 출구) */
    int64_t    fluidCells;        /* 관 안: 유체 칸 수 */
    int32_t    regrids;           /* 솔리드가 격자를 벗어나 격자를 새로 만든 횟수(켠 뒤 모두) */
} CAD_WindState;

enum {   /* 단면 판 색(CAD_WindView::field) */
    CAD_WIND_FIELD_SPEED     = 0,   /* 빠르기 */
    CAD_WIND_FIELD_PRESSURE  = 1,   /* 압력 계수 */
    CAD_WIND_FIELD_VORTICITY = 2,   /* 소용돌이 세기 */
    CAD_WIND_FIELD_SMOKE     = 3    /* 단면 판 없이 연기만(빠르기 색) */
};
/* 화면 표시 — CAD_WindGetView 로 읽어 고친 뒤 CAD_WindSetView(NULL = 켠 때의 보기). 맨 앞 size = sizeof, 새 칸은 끝에만 */
typedef struct CAD_WindViewOptions {
    uint32_t size;
    int32_t  field;            /* CAD_WIND_FIELD_* */
    int32_t  planeAxis;        /* 단면 판의 법선 — 0 X(정면) · 1 Y(옆) · 2 Z(위) */
    double   planeAt;          /* 그 축 안 자리 0~1(격자 처음 ~ 끝) */
    bool     planeShown;       /* 단면 판 보이기 */
    bool     smoke;            /* 연기 */
    bool     surfacePressure;  /* 솔리드 표면을 압력 계수 색으로 */
    double   isoSpeed;         /* 등속도면 — 바람 대비 빠르기 0~1(안쪽 = 느린 곳), 0 = 끔 */
    bool     trajectories;     /* 흐름 궤적(물체 앞에서 출발한 흐름선 + 흐르는 화살촉) */
} CAD_WindViewOptions;

enum {   /* 칸 값(CAD_WindGetCellField) — 칸마다 값 개수. 칸 순서 = i + nx·(j + ny·k) */
    CAD_WIND_CELL_VELOCITY = 1,   /* 3 — 바람 대비 속도(고체 칸 0) */
    CAD_WIND_CELL_PRESSURE = 2,   /* 1 — 압력 계수 Cp(고체 칸 NaN) */
    CAD_WIND_CELL_SOLID    = 3    /* 1 — 1 고체, 0 유체 */
};
/* 점 하나의 흐름 값(CAD_WindSample) */
typedef struct CAD_WindPointValue {
    CAD_GeVec3 velocity;   /* 바람 대비 속도 */
    double     speed;      /* |velocity| */
    double     pressure;   /* 압력 계수 Cp(둘레 유체 칸만으로 보간) */
    bool       inFluid;    /* 격자 안 유체 칸 — 거짓이면 고체 속이거나 격자 밖(값은 가장 가까운 칸 쪽으로 잘림) */
} CAD_WindPointValue;
/* 표면 점 하나(CAD_WindSurfacePressure) — 월드 자리와 바깥 법선 */
typedef struct CAD_WindSurfacePoint {
    CAD_GeVec3 point;
    CAD_GeVec3 normal;   /* 바깥쪽(길이 0 이 아니면 단위가 아니어도 된다) */
} CAD_WindSurfacePoint;

/* 닫힌 메시 솔리드들(ids, count ≥ 1)에 바람을 맞힌다(패널도 켬). 이미 같은 솔리드로 켜져 있으면 설정만 바꾼다(CAD_WindSetOptions 처럼),
 * 다른 솔리드면 그것으로 처음부터. 없는 id = CAD_E_BAD_HANDLE, 메시가 아님 = CAD_E_WRONG_TYPE, 모듈 없음 = CAD_E_NOT_SUPPORTED,
 * 격자·셰이더를 못 만듦 = CAD_E_FAILED. 그리는 중(플러그인 명령 안)에 부르면 다음 CAD_Tick 에 켠다(state.starting) */
CAD_API CAD_Status CAD_WindOpen(const uint32_t* ids, uint32_t count, const CAD_WindOptions* opt);
CAD_API CAD_Status CAD_WindClose(void);   /* 끈다(패널도) — 꺼져 있으면 그대로 CAD_OK */
CAD_API CAD_Status CAD_WindGetOptions(CAD_WindOptions* out);   /* 지금 설정(꺼져 있으면 다음에 켤 설정) — 부르는 쪽이 out->size = sizeof */
/* 설정 바꾸기(NULL = 기본값). 범위 밖 = CAD_E_INVALID_ARG(아무것도 안 바꿈). 꺼져 있으면 다음에 켤 설정으로 */
CAD_API CAD_Status CAD_WindSetOptions(const CAD_WindOptions* opt);
CAD_API CAD_Status CAD_WindReset(void);                 /* 흐름을 처음부터(같은 격자) */
CAD_API CAD_Status CAD_WindSetRunning(bool running);    /* 거짓 = 멈춤, 참 = 계속 */
/* steps 걸음(1~1000000)을 흘릴 때까지 기다린다 — 틱 없이 흐름을 나아가게(스크립트·AI). 그동안 엔진은 멈춘다(그래픽 큐를 같이 씀).
 * 옮긴 솔리드는 먼저 다시 맞춘다. 그리는 중 = CAD_E_BUSY(CAD_Post 로 틱 밖에서), 계산이 깨짐 = CAD_E_FAILED + 이유 */
CAD_API CAD_Status CAD_WindAdvance(int32_t steps);
CAD_API CAD_Status CAD_WindGetState(CAD_WindState* out);   /* 부르는 쪽이 out->size = sizeof */
CAD_API CAD_Status CAD_WindGetView(CAD_WindViewOptions* out);   /* 꺼져 있음 = CAD_E_NOT_READY. 부르는 쪽이 out->size = sizeof */
/* 화면 표시 바꾸기 — NULL = 켠 때의 보기(빠르기·처음 단면·판 보임·연기 켬·나머지 끔), 모르는 칸도 그 값.
 * field 가 SMOKE 면 smoke 는 켜진다. 범위 밖 = CAD_E_INVALID_ARG(아무것도 안 바꿈) */
CAD_API CAD_Status CAD_WindSetView(const CAD_WindViewOptions* opt);
/* 칸 값 — field = CAD_WIND_CELL_*(칸마다 값 개수는 그 enum 에). 반환 = 값 개수(칸 × 개수) */
CAD_API int32_t    CAD_WindGetCellField(int32_t field, double* outValues, uint32_t capacity);
/* 월드 점들(count 개)의 흐름 값 — 칸 사이는 세 방향 선형 보간. 반환 = 점 개수(outValues 엔 capacity 까지 차례대로).
 * 아직 한 걸음도 안 흘렀음 = CAD_E_NOT_READY */
CAD_API int32_t    CAD_WindSample(const CAD_GeVec3* points, uint32_t count, CAD_WindPointValue* outValues, uint32_t capacity);
/* 표면 압력 계수 — 표면 점(자리 + 바깥 법선)마다 법선 쪽 1.5칸의 Cp(화면 표면 압력 색·구조 해석 바람 하중과 같은 계산).
 * 반환 = 점 개수(outCp 엔 capacity 까지). 법선 길이 0 = CAD_E_INVALID_ARG */
CAD_API int32_t    CAD_WindSurfacePressure(const CAD_WindSurfacePoint* points, uint32_t count, double* outCp, uint32_t capacity);
/* seed(월드)에서 흐름을 따라간 흐름선(반 칸 간격 점, 월드) — 고체·흡수층·느린 곳(바람의 3 %)에 닿으면 끝. 반환 = 점 개수(씨앗이 고체 속이면 0) */
CAD_API int32_t    CAD_WindGetStreamline(CAD_GeVec3 seed, CAD_GeVec3* outPoints, uint32_t capacity);

/* ── 물 — 값 함수 (CAD_Water*) ───────────────────────────────────────────
 * 닫힌 솔리드(그릇) 안의 물을 GPU 자유 표면 격자 볼츠만으로 출렁이게 한다 — 기울이기·흔들기·띄우기. JSON 창구(CAD_Water · MCP water)·
 * 명령 water·패널과 같은 세션이다. 시간은 계산 걸음(물리 초가 아님 — 첫 출렁임 공명 주기가 걸음으로 state 에).
 * 단위: 좌표·칸 크기 = 장면 단위, 속도 = 장면 단위/걸음, 각 = rad. 그릇을 옮기거나 모양을 바꾸면 같은 그릇으로 다시 채운다.
 * 새 규칙: 꺼져 있음 = CAD_E_NOT_READY, 모듈 없음 = CAD_E_NOT_SUPPORTED, 엔진 스레드에서만. */

enum {   /* 격자 크기 */
    CAD_WATER_GRID_NORMAL = 0,   /* 약 30만 칸 */
    CAD_WATER_GRID_FAST   = 1,   /* 약 10만 칸 */
    CAD_WATER_GRID_FINE   = 2    /* 약 80만 칸 */
};
/* 물 설정 — 맨 앞 size = sizeof, 새 칸은 끝에만. NULL = 기본값(보통 격자 · 반 채움 · 닫힌 그릇 · 속도 1) */
typedef struct CAD_WaterOptions {
    uint32_t size;
    int32_t  grid;      /* CAD_WATER_GRID_* — 도는 중에 바꾸면 다시 채움 */
    double   level;     /* 그릇 높이에 대한 물 높이 0.05~0.95, 0 = 0.5 — 바꾸면 다시 채움 */
    bool     openTop;   /* 위가 열린 그릇(벽·바닥만 고체 — 넘친 물이 그릇 밑면 높이 바닥에 고인다) — 바꾸면 다시 채움 */
    double   speed;     /* 계산 속도 1~4(프레임당 GPU 계산을 그 배만큼), 0 = 1 — 도는 중에도 */
} CAD_WaterOptions;

/* 지금 상태 — 부르는 쪽이 size = sizeof(CAD_WaterState). 꺼져 있어도 CAD_OK(active 거짓) */
typedef struct CAD_WaterState {
    uint32_t   size;
    bool       active;
    bool       starting;          /* 다음 CAD_Tick 에 켜짐 */
    bool       running;
    bool       failed;            /* 계산이 멈춤(숫자가 아닌 칸 — 처음부터 필요) 또는 켜기 실패 — 이유는 CAD_WaterAdvance 가 */
    bool       openTop;
    uint32_t   container;         /* 그릇 id */
    int64_t    steps;
    double     stepsPerSecond;
    int32_t    nx, ny, nz;
    double     cellSize;          /* 장면 단위 */
    CAD_GeVec3 origin;            /* 격자 구석(월드) */
    double     tiltX, tiltY;      /* 그릇 기울기 rad — X 축·Y 축 둘레 */
    double     shake;             /* 흔들기 세기(중력의 몇 배, 0 = 안 흔듦) */
    double     shakePeriod;       /* 흔들기 주기(걸음) */
    double     resonancePeriod;   /* 이 그릇의 첫 출렁임 공명 주기(걸음) */
    double     massDrift;         /* 처음 대비 물 질량 변화(비율) — GPU 에서 내려받아 셈(자주 부르면 느림) */
    double     spilledFraction;   /* 열린 그릇: 물 가운데 그릇 밖에 있는 비율(닫힌 그릇 0) */
    int32_t    surfaceTriangleCount;
    int32_t    floaterCount;
    int32_t    restarts;          /* 그릇이 바뀌어 다시 채운 횟수(켠 뒤 모두) */
} CAD_WaterState;

/* 띄운 강체 하나 */
typedef struct CAD_WaterFloater {
    uint32_t   id;
    double     density;        /* 물 대비 */
    CAD_GeVec3 center;         /* 질량 중심(월드) */
    CAD_GeVec3 velocity;       /* 장면 단위/걸음 */
    double     submerged;      /* 잠긴 부피 비율 0~1 */
    double     tilt;           /* 띄운 때 대비 위쪽(+Z) 기울기 rad */
    int32_t    wallContacts;   /* 마지막 걸음 묶음에서 그릇 벽에 닿은 표본 수 */
} CAD_WaterFloater;

enum {   /* 칸 값(CAD_WaterGetCellField) — 칸마다 값 개수. 칸 순서 = i + nx·(j + ny·k) */
    CAD_WATER_CELL_FILL     = 1,   /* 1 — 채움 0(빈칸)~1(물), 고체 칸 0 */
    CAD_WATER_CELL_VELOCITY = 2,   /* 3 — 장면 단위/걸음 */
    CAD_WATER_CELL_SOLID    = 3    /* 1 — 1 고체(그릇·바닥·격자 테두리), 0 그 밖 */
};
/* 점 하나의 물 값(CAD_WaterSample) */
typedef struct CAD_WaterPointValue {
    double     fill;       /* 채움 0~1 */
    CAD_GeVec3 velocity;   /* 장면 단위/걸음 */
} CAD_WaterPointValue;

/* 닫힌 메시 솔리드(그릇) container 에 물을 채워 켠다(패널도). 같은 그릇으로 켜져 있으면 설정만 바꾼다(CAD_WaterSetOptions 처럼).
 * 없는 id = CAD_E_BAD_HANDLE, 메시가 아님 = CAD_E_WRONG_TYPE, 모듈 없음 = CAD_E_NOT_SUPPORTED, 그릇 안이 너무 작음·닫히지 않음 = CAD_E_FAILED.
 * 그리는 중에 부르면 다음 CAD_Tick 에 켠다(state.starting) */
CAD_API CAD_Status CAD_WaterOpen(uint32_t container, const CAD_WaterOptions* opt);
CAD_API CAD_Status CAD_WaterClose(void);   /* 끈다(띄운 것은 띄운 때 자세로) — 꺼져 있으면 그대로 CAD_OK */
CAD_API CAD_Status CAD_WaterGetOptions(CAD_WaterOptions* out);   /* 부르는 쪽이 out->size = sizeof */
CAD_API CAD_Status CAD_WaterSetOptions(const CAD_WaterOptions* opt);   /* NULL = 기본값, 범위 밖 = CAD_E_INVALID_ARG */
CAD_API CAD_Status CAD_WaterReset(void);   /* 처음 채운 때로(기울기·흔들기 0, 띄운 것은 띄운 때 자세로) */
CAD_API CAD_Status CAD_WaterSetRunning(bool running);
/* steps 걸음(1~1000000)을 흘릴 때까지 기다린다(기울기·흔들기·띄운 것 그대로, 끝나면 표면도 다시). 그리는 중 = CAD_E_BUSY, 계산이 깨짐 = CAD_E_FAILED */
CAD_API CAD_Status CAD_WaterAdvance(int32_t steps);
/* 그릇 기울이기 — X 축·Y 축 둘레 rad(각 ±0.698 = ±40° 안, 밖이면 CAD_E_INVALID_ARG). 중력을 반대로 돌린다 */
CAD_API CAD_Status CAD_WaterSetTilt(double xRadians, double yRadians);
/* 흔들기 — 세기 0~1(중력의 몇 배, 0 = 멈춤), 주기 걸음(0 = 이 그릇의 공명 주기, 그 밖엔 10 이상) */
CAD_API CAD_Status CAD_WaterSetShake(double amplitude, double periodSteps);
/* 닫힌 메시 솔리드들을 물에 띄운다(강체 — 부력·물 끌림·벽 닿음). density = 물 대비 0.1~0.95. 그릇·메시 아님은 건너뜀. 반환 = 띄운 개수(0 = 하나도 못 띄움 + 이유) */
CAD_API int32_t    CAD_WaterAddFloaters(const uint32_t* ids, uint32_t count, double density);
CAD_API CAD_Status CAD_WaterClearFloaters(bool restore);   /* 띄운 것 내리기 — restore 참 = 띄운 때 자세로 */
CAD_API CAD_Status CAD_WaterGetState(CAD_WaterState* out);   /* 부르는 쪽이 out->size = sizeof */
CAD_API int32_t    CAD_WaterGetFloaters(CAD_WaterFloater* outFloaters, uint32_t capacity);   /* 반환 = 개수 */
/* 물 표면 메시(채움 0.5 면, 월드) — 정점. 반환 = 정점 개수(아직 표면이 없으면 0) */
CAD_API int32_t    CAD_WaterGetSurfaceVertices(CAD_GeVec3* outVertices, uint32_t capacity);
/* 물 표면 메시 — 삼각형마다 정점 번호 3개. 반환 = 값 개수(삼각형 × 3) */
CAD_API int32_t    CAD_WaterGetSurfaceTriangles(uint32_t* outIndices, uint32_t capacity);
/* 칸 값 — field = CAD_WATER_CELL_*. 반환 = 값 개수(칸 × 개수) */
CAD_API int32_t    CAD_WaterGetCellField(int32_t field, double* outValues, uint32_t capacity);
/* 월드 점들(count 개)의 채움·속도(세 방향 선형 보간, 고체·격자 밖 칸은 0). 반환 = 점 개수(outValues 엔 capacity 까지) */
CAD_API int32_t    CAD_WaterSample(const CAD_GeVec3* points, uint32_t count, CAD_WaterPointValue* outValues, uint32_t capacity);

/* ── 천 — 값 함수 (CAD_Cloth*) ───────────────────────────────────────────
 * 메시 솔리드 위에 천을 떨어뜨려 덮거나(덮기), 가로 선에 커튼을 걸어 바람에 흔든다(XPBD 작은 걸음). 명령 cloth·패널과 같은 세션이다.
 * 계산은 작업 스레드가 실시간으로(1/60 초 걸음) 돌린다 — CAD_Tick 을 돌리면 화면 천이 따라오고, CAD_ClothAdvance 는 정한 시간만큼 흘릴 때까지 기다린다.
 * 단위: 천은 실제 물리로 계산한다 — 시간 = 초, 바람 = m/s, 늘어남 = 비율. 좌표·두께 = 장면 단위(장면 → m 는 대상 크기로 정함: 대각선이
 *       20 넘으면 mm — state.unitToMeter). 장애물은 켤 때 모양 그대로(옮겨도 따라가지 않음 — 다시 켜기).
 *       저장·되돌리기에 들어가지 않는다(굽기만 들어감). 뻣뻣한 천(데님·가죽)은 실제보다 무르게 처진다(XPBD 의 한계).
 * 새 규칙: 꺼져 있음 = CAD_E_NOT_READY, 엔진 스레드에서만. 그리는 중(플러그인 명령 안)에 켜기·끄기를 받으면 다음 틱에(state.starting). */

enum {   /* 모양 */
    CAD_CLOTH_DRAPE   = 0,   /* 덮기 — 장애물 위 가운데 조금 위에서 네모 천을 떨어뜨림(대상이 놓인 높이가 바닥) */
    CAD_CLOTH_CURTAIN = 1    /* 커튼 — 막대(선)에 위 줄을 고정하고 늘어뜨림(주름 잡아), 바람은 커튼 면에 수직 */
};
enum {   /* 천 종류 — 넓이당 질량·굽힘 강성(Kawabata 측정 범위) */
    CAD_CLOTH_FABRIC_COTTON  = 0,   /* 면 0.15 kg/m² */
    CAD_CLOTH_FABRIC_SILK    = 1,   /* 실크 0.05 kg/m² */
    CAD_CLOTH_FABRIC_DENIM   = 2,   /* 데님 0.35 kg/m² */
    CAD_CLOTH_FABRIC_LEATHER = 3    /* 가죽 0.9 kg/m² */
};
enum {   /* 점 수 */
    CAD_CLOTH_RES_NORMAL = 0,   /* 48 × 48 */
    CAD_CLOTH_RES_FAST   = 1,   /* 32 × 32 */
    CAD_CLOTH_RES_FINE   = 2    /* 64 × 64 */
};
/* 천 설정 — 맨 앞 size = sizeof, 새 칸은 끝에만. NULL = 기본값(덮기 · 면 · 보통 · 1.6배 · 바람 0 · 돌풍 0 · 실시간) */
typedef struct CAD_ClothOptions {
    uint32_t size;
    int32_t  mode;         /* CAD_CLOTH_DRAPE · CAD_CLOTH_CURTAIN — 도는 중에 바꾸면 같은 대상으로 처음부터 */
    int32_t  fabric;       /* CAD_CLOTH_FABRIC_* — 도는 중에도 바로(자리·속도는 그대로) */
    int32_t  resolution;   /* CAD_CLOTH_RES_* — 바꾸면 처음부터 */
    double   sizeFactor;   /* 덮기 = 대상 폭(가로·세로 중 큰 것)의 배수, 커튼 = 막대 길이의 배수(늘어뜨린 길이) 0.5~4, 0 = 1.6 — 바꾸면 처음부터 */
    double   windSpeed;    /* 바람 m/s 0~30 — 덮기 +X, 커튼 = 면에 수직. 도는 중에도 */
    double   gust;         /* 돌풍 세기 0~1(바람 크기에 대한 변동) — 도는 중에도 */
    bool     fast;         /* 틱으로 돌 때 실시간에 맞추지 않고 최대 속도로 — 도는 중에도 */
} CAD_ClothOptions;

/* 지금 상태 — 부르는 쪽이 size = sizeof(CAD_ClothState). 꺼져 있어도 CAD_OK(active 거짓) */
typedef struct CAD_ClothState {
    uint32_t size;
    bool     active;          /* 천 세션이 있음 */
    bool     starting;        /* 다음 CAD_Tick 에 켜짐(그리는 중에 부른 CAD_ClothOpen·처음부터 다시 도는 설정) */
    bool     running;         /* 작업 스레드가 나아감(거짓 = 멈춤 — CAD_ClothAdvance 는 멈춤에도 된다) */
    bool     failed;          /* 계산이 깨짐(숫자가 아닌 자리 — CAD_ClothReset 필요) 또는 켜기 실패 — 이유는 CAD_ClothAdvance 가 */
    int32_t  mode;            /* CAD_CLOTH_DRAPE · CAD_CLOTH_CURTAIN */
    int32_t  fabric;          /* CAD_CLOTH_FABRIC_* */
    int32_t  pointCount;      /* 천 점 수 */
    int32_t  triangleCount;   /* 천 삼각형 수(한 장) */
    int32_t  obstacleCount;   /* 장애물 솔리드 수 */
    bool     rodGiven;        /* 커튼: 준 선에 걸었음(거짓 = 원점 위 2 m 높이에 1 m 막대) */
    double   time;            /* 흐른 시간(초) */
    double   stepMs;          /* 1/60 초 한 걸음의 계산 시간(ms, 부드럽게 맞춘 값) */
    double   realtime;        /* 틱으로 돌 때 실시간 대비 빠르기(1 = 실시간) */
    double   meanStretch;     /* 변 길이 늘어남 평균(비율, 0.01 = 1 %) */
    double   maxStretch;      /* 가장 많이 늘어난 변(받침 모서리 한두 곳에 몰린다) */
    double   maxSpeed;        /* 가장 빠른 점(m/s) — 0 가까우면 자리 잡음 */
    double   thickness;       /* 충돌 두께(장면 단위) */
    double   unitToMeter;     /* 장면 단위 1 = 몇 m(0.001 = mm) */
} CAD_ClothState;

/* 천을 켠다(패널도). 덮기: ids 에 메시 솔리드가 하나 이상(전부 장애물). 커튼: ids 안의 선(LINE·열린 폴리선) 하나가 막대, 나머지 솔리드는 장애물
 * — ids 가 없으면(count 0) 원점 위 2 m 높이 1 m 막대. 같은 대상으로 켜져 있으면 설정만 바꾼다(CAD_ClothSetOptions 처럼), 다른 대상이면 처음부터.
 * 없는 id = CAD_E_BAD_HANDLE, 솔리드·선이 아님(덮기에 선) = CAD_E_WRONG_TYPE, 덮기에 솔리드 없음·선 둘 이상·범위 밖 설정 = CAD_E_INVALID_ARG,
 * 막대가 세로이거나 너무 짧음 = CAD_E_FAILED. 그리는 중에 부르면 다음 CAD_Tick 에 켠다(state.starting) */
CAD_API CAD_Status CAD_ClothOpen(const uint32_t* ids, uint32_t count, const CAD_ClothOptions* opt);
CAD_API CAD_Status CAD_ClothClose(void);   /* 끈다(패널도) — 꺼져 있으면 그대로 CAD_OK */
CAD_API CAD_Status CAD_ClothGetOptions(CAD_ClothOptions* out);   /* 지금 설정(꺼져 있으면 다음에 켤 설정) — 부르는 쪽이 out->size = sizeof */
/* 설정 바꾸기(NULL = 기본값). 범위 밖 = CAD_E_INVALID_ARG(아무것도 안 바꿈). 꺼져 있으면 다음에 켤 설정으로.
 * 모양·점 수·크기가 바뀌면 같은 대상으로 처음부터(멈춤은 그대로) — 못 만들면 CAD_E_FAILED + 이유(천은 꺼짐) */
CAD_API CAD_Status CAD_ClothSetOptions(const CAD_ClothOptions* opt);
/* 재질(무늬) — textures 폴더의 재질 이름(확장자 빼고), "none" = 무늬 없이 천 종류 색만, NULL·"" = 천 종류 따라(실크는 색만).
 * 없는 재질 = CAD_E_INVALID_ARG. 도는 중에도 바로, 꺼져 있으면 다음에 켤 때. 굽기에도 쓴다 */
CAD_API CAD_Status CAD_ClothSetMaterial(const char* name);
/* 재질 설정 — buf 에 NUL 까지 담고(모자라면 잘라서) 전체 길이(NUL 제외). "" = 천 종류 따라, "none" = 색만 */
CAD_API int32_t    CAD_ClothGetMaterial(char* buf, uint32_t capacity);
CAD_API CAD_Status CAD_ClothReset(void);                 /* 처음 자리·속도 0 으로, 시간 0(설정 그대로) — 깨진 계산도 이걸로 */
CAD_API CAD_Status CAD_ClothSetRunning(bool running);    /* 거짓 = 멈춤(돌아오면 더 나아가지 않음), 참 = 계속 */
/* seconds 초(1/60 초 걸음으로 반올림, 적어도 한 걸음 · 600 초 이하)를 흘릴 때까지 기다린다 — 틱 없이 천을 나아가게(스크립트·AI).
 * 작업 스레드는 그동안 비켜 서고, 끝나면 이어서 돈다(멈춤이면 그대로). GPU 를 쓰지 않아 그리는 중에도 된다(화면 천은 다음 틱에).
 * 계산이 깨짐 = CAD_E_FAILED + 이유 */
CAD_API CAD_Status CAD_ClothAdvance(double seconds);
CAD_API CAD_Status CAD_ClothGetState(CAD_ClothState* out);   /* 부르는 쪽이 out->size = sizeof */
/* 지금 천 점(월드, 장면 단위) — 칸만큼 채우고 전체 개수. 점 번호는 CAD_ClothGetTriangles 의 번호 */
CAD_API int32_t    CAD_ClothGetPoints(CAD_GeVec3* outPoints, uint32_t capacity);
/* 점마다 법선(단위, 이웃 삼각형 넓이 가중) — 칸만큼 채우고 전체 개수 */
CAD_API int32_t    CAD_ClothGetNormals(CAD_GeVec3* outNormals, uint32_t capacity);
/* 천 삼각형 — 삼각형마다 점 번호 3개(한 장, 감김은 쉴 때 그대로). 반환 = 값 개수(삼각형 × 3) */
CAD_API int32_t    CAD_ClothGetTriangles(uint32_t* outIndices, uint32_t capacity);
/* 지금 모양에 두께(충돌 두께의 0.6배)를 줘 닫힌 메시 객체로 만든다(재질 그대로, 되돌리기 1) — 천은 끈다(그리는 중이면 다음 틱에).
 * outId = 새 객체 id. 꺼져 있음 = CAD_E_NOT_READY, 못 만듦 = CAD_E_FAILED */
CAD_API CAD_Status CAD_ClothBake(uint32_t* outId);

#ifdef __cplusplus
}
#endif
