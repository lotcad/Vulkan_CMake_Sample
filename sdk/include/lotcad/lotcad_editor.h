#pragma once
/* LotCAD C API - editor  [AcEd (editor)]
 * Commands, interactive tools, jig, prompts, picking, selection, object snap.
 * 명령·대화형 도구·지그·안내·점 고르기·선택·객체 스냅.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"
#include "lotcad_objects.h"   /* CAD_OsnapPoint · CAD_OsnapOptions · CAD_OSNAP_* */

#ifdef __cplusplus
extern "C" {
#endif
/* 진행 중인 치수 도구의 점 개수 — 치수 도구가 아니면 CAD_E_NOT_READY.
 * 모바일 커서 UI 의 [선택] 버튼 문구·끝 판단에 쓴다(클릭을 세면 엔진이 거부한 클릭과 어긋나니 엔진 값을 본다). */
CAD_API int32_t    CAD_GetDimensionPointCount(void);
/* 진행 중인 도구·묻기의 안내("첫 번째 점을 지정" 등) — 없으면 ""(길이 0). 모바일 커서 UI 가 도구 종류와 무관하게 매 틱 읽는다.
 * 반환 = 전체 길이(NUL 제외), 칸이 모자라면 글자 경계에서 잘라 담는다. */
CAD_API int32_t    CAD_GetPrompt(char* buf, uint32_t capacity);
/* 한동안 뜨는 안내(몇 초 뒤 스스로 사라짐) — 프롬프트(지금 뭘 할지, 상시)와 다른 값: "방금 왜 안 됐는지".
 *   예: "각도: 선을 클릭하세요". 없거나 지났으면 "". 데스크톱은 상태바가 그리지만 모바일은 이게 유일한 길(안 띄우면 클릭이 씹힌 듯 보인다). */
CAD_API int32_t    CAD_GetTransientMessage(char* buf, uint32_t capacity);

/* ── 명령 실행 ────────────────────────────────────────────────────────────
 *
 * 엔진의 **모든 명령**을 이름으로 실행한다 — 도구 시작(line·circle·rect·arc·polygon·polyline·box·extrude·revolve·light …),
 * 도구 선택지(sides·arcmode), trim·offset·fillet·ocr·navmap … 200개가 넘는다. 새 명령이 생겨도 API 를 늘리지 않는다.
 *
 *   CAD_ExecuteCommand("line");        // 선 도구 시작
 *   CAD_ExecuteCommand("2,3");         // 진행 중인 도구에 좌표·값
 *   CAD_ExecuteCommand(" ");           // 빈 Enter
 *
 * 글은 하단 명령행에 치는 것과 **똑같다**(영문·짧은 별칭·한글, 진행 중인 도구가 있으면 값 입력) — 명령행과 같은 길.
 * 모르는 명령은 AI 로 보내지 않는다(자연어는 CAD_AiSubmit). 반환: CAD_OK · 모르는 명령 CAD_E_NOT_FOUND ·
 * 기다리는 도구가 없는데 빈 Enter CAD_E_NOT_READY.
 */
CAD_API CAD_Status CAD_ExecuteCommand(const char* text);

/* ── 명령 등록 (플러그인) ─────────────────────────────────
 *
 * 플러그인이 **콘솔 명령을 추가**한다. 명령행이 이 엔진의 모든 기능 진입점이라,
 * 이것만 있으면 플러그인이 "기능" 이 된다. ObjectARX 의 acedRegCmds 자리.
 *
 *   등록 후  명령행에 wall → 콜백 호출
 *              CAD_ExecuteCommand("wall") 도 같은 경로
 *
 * name   조회 키. 대소문자를 안 가린다(한글 이름도 된다).
 * title  메뉴·툴바에 들어갈 표시 이름. NULL 이면 name 을 쓴다.
 * fn     콜백. **C 함수 포인터**라 C++/C#/Python 어디서든 같은 모양으로 쓴다.
 * user   그대로 돌려받는다(플러그인 인스턴스 포인터 등).
 * owner  플러그인 ID. 언로드할 때 이 값으로 묶어 한꺼번에 지운다. 0 = 소유자 없음.
 *
 * 실패: 빈 이름·fn NULL = CAD_E_INVALID_ARG · 이미 등록된 이름·엔진 기본 명령(line/circle …)과 같은 이름 = CAD_E_DUPLICATE
 *   (기본 명령이 먼저 조회돼 절대 불리지 않으니 받지 않는다 — 플러그인이 기본 동작을 가로채는 것도 막는다).
 * ⚠️ 콜백은 **엔진과 같은 스레드**에서 불린다 — 안에서 CAD_* 를 부른다. 던진 예외는 엔진이 잡아 삼킨다(프레임 루프가 죽지 않게).
 */
typedef void (*CAD_CommandFn)(void* user);
CAD_API CAD_Status CAD_RegisterCommand(const char* name, const char* title, CAD_CommandFn fn, void* user, uint32_t owner);
CAD_API CAD_Status CAD_UnregisterCommand(const char* name);   /* 없는 이름 CAD_E_NOT_FOUND */
/* 그 플러그인이 등록한 명령을 전부 지운다. 반환 = 지운 개수(owner 0 은 아무것도 안 지움).
 * 언로드 길에서 반드시 부른다 — 안 지우면 사라진 DLL 의 함수를 부르게 된다. */
CAD_API int32_t    CAD_UnregisterCommandsByOwner(uint32_t owner);
/* 등록된 명령 수 · index 번째 이름·표시 이름(메뉴·리본을 그릴 때). index 범위 밖 CAD_E_OUT_OF_RANGE */
CAD_API int32_t    CAD_GetRegisteredCommandCount(void);
CAD_API int32_t    CAD_GetRegisteredCommandName(uint32_t index, char* buf, uint32_t capacity);
CAD_API int32_t    CAD_GetRegisteredCommandTitle(uint32_t index, char* buf, uint32_t capacity);

/* 파일 열기 창(엔진 창이 있는 호스트) · 장면 비우기 · 고른 객체 재질을 다음 것으로 · 고른 객체 재질 떼기 — 다음 틱에 한다(CAD_OK = 맡김).
 * 한 객체에 이름으로 재질을 주는 것은 CAD_ApplyMaterial(id, 이름) */
CAD_API CAD_Status CAD_OpenFileDialog(void);
CAD_API CAD_Status CAD_ClearAll(void);
CAD_API CAD_Status CAD_CycleMaterial(void);
CAD_API CAD_Status CAD_RemoveMaterial(void);

// ── Jig (오토캐드 AcEdJig 스타일) ────────────────────────────────────
// 객체 id 를 물려 시작하면 그 객체가 **커서를 따라다니고**, 좌클릭에 그 자리로 확정된다
// (undo 1스텝). ESC 로 원복. OSnap·직교 트랙킹(F8)·콘솔 값 입력이 그대로 적용된다.
//   mode: 0=이동 1=회전 2=축척 3=복사
//   회전/축척은 (px,py,pz) 가 피벗. 이동/복사는 무시하고 선택 전체의 시각 중심을 기준점으로 잡는다.
// 반환 false = 유효한 객체가 없어 시작 못 함.
CAD_API bool CAD_JigBegin(int mode, const uint32_t* ids, int count,
                          float px, float py, float pz);
CAD_API bool CAD_JigBeginOne(int mode, uint32_t id, float px, float py, float pz);
// 상태 폴링 — 0=비활성 1=끌는 중 2=직전 확정됨 3=직전 취소됨 (2/3 은 1회만 반환).
CAD_API int  CAD_JigState(void);
CAD_API void CAD_JigCancel(void);

// ── 변형(variant) Jig — 끌면서 Tab 으로 **형상 자체를 교체** ──────────
// 후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
// 갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
//   확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
//   취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
// 콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
// 코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
//   MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
//   Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
//   SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
//   GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
CAD_API bool CAD_JigMoveTo(float x, float y, float z);
CAD_API bool CAD_JigCommit(void);
CAD_API bool CAD_JigSetBasePoint(float x, float y, float z);
CAD_API bool CAD_JigGetDelta(float* dx, float* dy, float* dz, float* angleDeg, float* scale);
CAD_API bool CAD_JigBeginVariants(int mode, const uint32_t* ids, int count,
                                  float px, float py, float pz);
CAD_API bool CAD_JigNextVariant(void);   // Tab 과 동일 (호스트 버튼으로 전환할 때)
CAD_API int  CAD_JigVariantIndex(void);  // 현재 후보 번호, -1 = 변형 Jig 아님
CAD_API uint32_t CAD_JigVariantId(void); // 지금 끌고 있는 후보 id (없으면 0)

CAD_API bool     CAD_BeginTextEdit(uint32_t id);
CAD_API bool     CAD_IsTextEditing(void);
CAD_API void     CAD_TextEditInsert(const char* utf8);   // 커서 위치에 삽입(여러 글자 가능)
CAD_API void     CAD_TextEditBackspace(void);
CAD_API void     CAD_TextEditDelete(void);
CAD_API void     CAD_TextEditMoveCaret(int delta);       // -1/+1 등
CAD_API void     CAD_TextEditCommit(void);               // undo 적재 + 종료
CAD_API void     CAD_TextEditCancel(void);               // 원복 + 종료

/* 선택 문맥 JSON — 사람이 화면에서 고른 것. AI 요청마다 자동으로 붙는 것과 같은 문자열.
 * {"mode":"object|face|edge","view":"top|…","count":N,"objects":[CAD_GetObjectJson 과 같은 객체…],"more":n,
 *  "face":{"id","normal","center","area","triangles"},"edge":{"id","a","b","length"}}  반환=길이, 실패 -1. */
CAD_API int32_t    CAD_GetSelectionContext(char* buf, uint32_t capacity);

/* ── 선택 ── (ObjectARX acedSSGet/acedSSSetFirst 자리 — 사람이 고른 것과 같은 선택. 화면에서 묻는 것은 CAD_EdSSGet) */
enum { CAD_SELECT_REPLACE = 0, CAD_SELECT_ADD = 1, CAD_SELECT_REMOVE = 2 };
/* 지금 선택 — 칸만큼 채우고 전체 개수(outIds = NULL 이면 개수만) */
CAD_API int32_t    CAD_GetSelection(uint32_t* outIds, uint32_t capacity);
/* 선택 바꾸기 — mode = CAD_SELECT_*(REPLACE + count 0 = 비우기). 없는 id CAD_E_BAD_HANDLE, 넣을 것이 잠긴 도면층 CAD_E_LOCKED,
 * 숨김·모양 없음(고를 수 없음) CAD_E_NOT_SUPPORTED — 하나라도 그러면 아무것도 안 바꾼다. 보기 상태라 되돌리기에 안 남는다 */
CAD_API CAD_Status CAD_SetSelection(const uint32_t* ids, uint32_t count, int32_t mode);

/* ── 객체 스냅·직교·극좌표 — 상태바 버튼(객체스냅·직교(F8)·극좌표(F10))과 같은 설정. 명령 osnap/ortho/polar [on|off] 과도 같다.
 * 모드 비트: CAD_OSNAP_END 1 · MID 2 · CEN 4 · FACE 8(면 중심) · NODE 16(점) · QUA 32(사분점) · INT 64(교차) · PER 128(수직) · TAN 256(접선) · NEA 512(근처) */
CAD_API CAD_Status CAD_SetOSnapEnabled(bool on);
CAD_API CAD_Status CAD_GetOSnapEnabled(bool* outOn);
CAD_API CAD_Status CAD_SetOSnapModes(uint32_t mask);          /* 모르는 비트 CAD_E_INVALID_ARG */
CAD_API CAD_Status CAD_GetOSnapModes(uint32_t* outMask);
CAD_API CAD_Status CAD_SetOrthoEnabled(bool on);
CAD_API CAD_Status CAD_GetOrthoEnabled(bool* outOn);
/* 극좌표 추적 — increment = 각 증분(rad, 1°~90°, 0 이하 = 지금 값 그대로, 기본 45°). 범위 밖 CAD_E_OUT_OF_RANGE */
CAD_API CAD_Status CAD_SetPolarTracking(bool on, double increment);
CAD_API CAD_Status CAD_GetPolarTracking(bool* outOn, double* outIncrement);   /* 출력은 NULL 가능 */
/* 장면에서 point 의 반경 radius(mm) 안 가장 가까운 스냅점 — 화면·커서 없이(AI·스크립트가 "이 근처 끝점" 을 잡을 때).
 * modes = CAD_OSNAP_* 합(상태바 설정과 무관), 보이는 객체만, 근처(NEA)는 다른 스냅이 없을 때만(오토캐드처럼).
 * opt 의 직전 점은 수직·접선에 쓴다(고른 점은 point). 새 규칙: 찾으면 CAD_OK + outPoint(id = 그 객체),
 * 없으면 CAD_E_NOT_ON_CURVE. 엔진 스레드에서만 */
CAD_API CAD_Status CAD_SnapNearPoint(CAD_GeVec3 point, double radius, uint32_t modes, const CAD_OsnapOptions* opt,
                                     CAD_OsnapPoint* outPoint);


// Static mesh component selection, main thread. Mode: 0 object, 1 face, 2 edge.
// Pick ray is in world coordinates. Face output contains triangle numbers (not corners).
// GetSelectedFaceTriangles returns required count; writes up to capacity if out != NULL.
CAD_API bool CAD_SetSubobjectSelectionMode(int mode);
CAD_API int CAD_GetSubobjectSelectionMode(void);
CAD_API bool CAD_PickSubobject(float ox, float oy, float oz, float dx, float dy, float dz);
CAD_API uint32_t CAD_GetSubobjectSelectionId(void);
CAD_API uint32_t CAD_GetSelectedFaceTriangles(uint32_t* out, uint32_t capacity);
// 현재 선택 면이 B-Rep 면이면 안정적인 face id, 아니면 -1.
CAD_API int32_t CAD_GetSelectedBRepFaceId(void);
// endpoints6 = {ax,ay,az,bx,by,bz}, world coordinates. False if no selected edge.
CAD_API bool CAD_GetSelectedEdge(float* endpoints6);


/* ── 명령행 입력 받기 (CAD_Ed*) — ObjectARX acedGetPoint·GetCorner·GetDist·GetAngle·GetInt·GetReal·GetString·GetKword·
 *    EntSel·SSGet 자리 ───────────────────────────────────────────────────────────────────────────────────
 *
 * 플러그인 명령이나 호스트가 사람에게 "반지름 <10>:" · "[예/아니오]:" · "객체 선택:" 처럼 묻고 답을 받는다.
 * 안내는 명령행에 늘 보이고(값을 치는 동안 3초 뒤 사라지지 않음), 답은 엔진 명령과 같은 길로 들어온다 —
 * 화면 클릭(객체 스냅 그대로), 명령행에 치기, CAD_ExecuteCommand("3,4")(빈 Enter = CAD_ExecuteCommand(" ")), ESC = 취소.
 *
 * 엔진은 한 스레드라 **멈춰 기다리지 않는다**: CAD_EdGetXxx 는 묻기만 하고 바로 CAD_OK 로 돌아온다. 답은
 *   ① 선택 구조체의 onDone 콜백 — 답이 정해진 틱 끝(CAD_Tick 안, 엔진 스레드)에 한 번. 그 안에서 다음 CAD_EdGetXxx 를 불러
 *      질문을 이어 간다(플러그인 명령의 보통 모양), 또는
 *   ② CAD_EdGetInputResult 로 물어보기 — status 가 CAD_ED_RESULT_PENDING 이 아니면 끝.
 * 마지막 답은 다음 답이 정해질 때까지 남는다(글은 CAD_EdGetInputText, 고른 객체는 CAD_EdGetInputIds).
 *
 * 한 번에 하나만 묻는다 — 묻는 중이면 CAD_E_BUSY. 엔진 명령(선·이동 …)이 값을 기다리는 중이어도 CAD_E_BUSY.
 * 점 입력: 클릭 · "x,y[,z]" · "@dx,dy[,dz]"(기준점, 없으면 마지막으로 받은 점에서) · "거리<각도"(XY 평면, 도) ·
 *   기준점이 있으면 접두 없는 "x,y" 도 기준점에서(엔진 명령행 규칙, "#x,y" = 절대) · 숫자 하나 = 기준점에서 커서 쪽으로 그 거리.
 * 키워드(opt.keywords, 띄어 쓴 낱말들 — "Yes No")를 주면 **어느 종류든** 키워드를 받는다 → CAD_ED_RESULT_KEYWORD.
 *   낱말 전체·낱말의 대문자 글자("Yes" → Y)·하나로 정해지는 앞부분(대소문자 무시)이 맞는다.
 * 엔진 스레드에서만 — 아니면 CAD_E_WRONG_THREAD. */

/* 묻는 종류 */
enum {
    CAD_ED_KIND_POINT     = 1,   /* 점 (acedGetPoint) */
    CAD_ED_KIND_CORNER    = 2,   /* 기준점의 반대쪽 구석 — 사각형 미리보기 (acedGetCorner) */
    CAD_ED_KIND_DISTANCE  = 3,   /* 거리 — 숫자 또는 두 점(기준점이 있으면 한 점) (acedGetDist) */
    CAD_ED_KIND_ANGLE     = 4,   /* 각도 — 숫자(도) 또는 두 점, 결과는 rad·XY 평면·+X 에서 반시계 (acedGetAngle) */
    CAD_ED_KIND_INTEGER   = 5,   /* 정수 (acedGetInt) */
    CAD_ED_KIND_REAL      = 6,   /* 실수 (acedGetReal) */
    CAD_ED_KIND_STRING    = 7,   /* 글 (acedGetString) */
    CAD_ED_KIND_KEYWORD   = 8,   /* 키워드만 (acedGetKword) */
    CAD_ED_KIND_ENTITY    = 9,   /* 객체 하나 + 찍은 점 (acedEntSel) */
    CAD_ED_KIND_SELECTION = 10   /* 여러 객체 — 클릭·Ctrl·드래그 창 후 Enter (acedSSGet) */
};

/* 답 (acedGetXxx 의 RTNORM · RTNONE · RTKWORD · RTCAN) */
enum {
    CAD_ED_RESULT_PENDING = 0,   /* 아직 묻는 중 */
    CAD_ED_RESULT_NORMAL  = 1,   /* 값을 받음 */
    CAD_ED_RESULT_NONE    = 2,   /* 빈 Enter — 기본값이 있으면 그 값이 채워져 있다 */
    CAD_ED_RESULT_KEYWORD = 3,   /* 키워드(또는 CAD_ED_ARBITRARY 의 아무 글) — CAD_EdGetInputText */
    CAD_ED_RESULT_CANCEL  = 4    /* ESC · CAD_EdCancelInput · 문서 바꿈 */
};

/* 선택지 비트 (acedInitGet 의 RSG_*) */
enum {
    CAD_ED_NO_NULL      = 1,     /* 빈 Enter 를 받지 않음(기본값이 있으면 기본값) */
    CAD_ED_NO_ZERO      = 2,     /* 0 을 받지 않음 — 정수·실수·거리·각도 */
    CAD_ED_NO_NEGATIVE  = 4,     /* 음수를 받지 않음 — 정수·실수·거리 */
    CAD_ED_ARBITRARY    = 8,     /* 값으로 안 읽히는 글도 받음 → CAD_ED_RESULT_KEYWORD, keywordIndex −1 */
    CAD_ED_ALLOW_SPACES = 16,    /* 글: Space 가 띄어쓰기(끝은 Enter 만) */
    CAD_ED_PICKFIRST    = 32,    /* 여러 객체: 이미 고른 것이 있으면 묻지 않고 그것으로 끝 */
    CAD_ED_SINGLE       = 64     /* 여러 객체: 한 번 고르면 끝(acedSSGet ":S") */
};

typedef struct CAD_EdInputResult {
    uint32_t   size;           /* 부르는 쪽이 sizeof 로 채움 */
    int32_t    kind;           /* CAD_ED_KIND_* */
    int32_t    status;         /* CAD_ED_RESULT_* */
    CAD_GeVec3 point;          /* 점·구석·객체를 찍은 점. 거리·각도는 점으로 답했을 때 둘째 점 */
    double     value;          /* 거리(mm)·각도(rad)·정수·실수 */
    uint32_t   id;             /* 객체 하나(ENTITY) */
    int32_t    keywordIndex;   /* KEYWORD: opt.keywords 의 몇 번째 낱말(0부터), 아무 글이면 −1 */
    int32_t    idCount;        /* SELECTION: 고른 객체 수 → CAD_EdGetInputIds */
    int32_t    textLength;     /* 글·키워드 길이(바이트, NUL 제외) → CAD_EdGetInputText */
} CAD_EdInputResult;

/* 답이 정해진 틱 끝에 엔진 스레드에서 한 번. result 는 콜백 동안만 유효 — 그 안에서 CAD_EdGetInputText·Ids 도 이 답 */
typedef void (*CAD_EdInputFn)(const CAD_EdInputResult* result, void* user);

typedef struct CAD_EdInputOptions {
    uint32_t      size;         /* sizeof(CAD_EdInputOptions) */
    uint32_t      flags;        /* CAD_ED_* 비트 */
    const char*   keywords;     /* "Yes No" — NULL = 키워드 없음(KEYWORD 종류는 꼭 있어야 함) */
    bool          hasBase;      /* 기준점 — 고무줄 선·직교(F8)·"@"·숫자 하나 = 그 거리. 거리·각도는 한 점만 받음 */
    CAD_GeVec3    base;
    bool          hasDefault;   /* 빈 Enter → CAD_ED_RESULT_NONE + 이 값(종류에 맞는 칸) */
    double        defaultValue;
    CAD_GeVec3    defaultPoint;
    const char*   defaultText;  /* 글 기본값(UTF-8), NULL = "" */
    CAD_EdInputFn onDone;       /* NULL = CAD_EdGetInputResult 로 물어보기 */
    void*         user;
} CAD_EdInputOptions;

/* 묻기 함수 공통 — prompt = 명령행 안내(UTF-8, NULL·"" = 종류별 기본 안내), 기본값·키워드도 안내에 직접 쓴다("반지름 <10>:").
 * 묻기만 하고 바로 CAD_OK. 실패: CAD_E_BUSY(다른 입력·명령 진행 중) · CAD_E_INVALID_ARG(opt.size 가 작음, KEYWORD 인데 키워드 없음) */

/* 점 하나(acedGetPoint) — 클릭(객체 스냅) 또는 좌표 글. opt.hasBase 면 기준점에서 고무줄 선·직교 */
CAD_API CAD_Status CAD_EdGetPoint(const char* prompt, const CAD_EdInputOptions* opt);

/* base 의 반대쪽 구석(acedGetCorner) — XY 사각형 미리보기. opt->base 대신 이 base */
CAD_API CAD_Status CAD_EdGetCorner(const char* prompt, CAD_GeVec3 base, const CAD_EdInputOptions* opt);

/* 거리(acedGetDist) — 숫자 또는 두 점(opt.hasBase 면 기준점에서 한 점), 결과 value(mm) */
CAD_API CAD_Status CAD_EdGetDistance(const char* prompt, const CAD_EdInputOptions* opt);

/* 각도(acedGetAngle) — 숫자(도) 또는 두 점, 결과 value = rad, XY 평면에서 +X 부터 반시계 0~2π */
CAD_API CAD_Status CAD_EdGetAngle(const char* prompt, const CAD_EdInputOptions* opt);

/* 정수(acedGetInt) — 결과 value(정수 값), 소수는 거절하고 다시 묻는다 */
CAD_API CAD_Status CAD_EdGetInteger(const char* prompt, const CAD_EdInputOptions* opt);

/* 실수(acedGetReal) — 결과 value */
CAD_API CAD_Status CAD_EdGetReal(const char* prompt, const CAD_EdInputOptions* opt);

/* 글(acedGetString) — 결과는 CAD_EdGetInputText. Space 를 띄어쓰기로 받으려면 CAD_ED_ALLOW_SPACES */
CAD_API CAD_Status CAD_EdGetString(const char* prompt, const CAD_EdInputOptions* opt);

/* 키워드만(acedGetKword) — opt.keywords 필수, 결과 keywordIndex + CAD_EdGetInputText(낱말 그대로) */
CAD_API CAD_Status CAD_EdGetKeyword(const char* prompt, const CAD_EdInputOptions* opt);

/* 객체 하나(acedEntSel) — 빈 곳 클릭은 다시 묻는다, 결과 id + 찍은 점 */
CAD_API CAD_Status CAD_EdEntSel(const char* prompt, const CAD_EdInputOptions* opt);

/* 여러 객체(acedSSGet) — 시작할 때 선택을 비운다(CAD_ED_PICKFIRST 이고 고른 것이 있으면 그것으로 바로 끝). 고르는 동안은 보통 선택
 * 그대로, Enter 는 하나 이상 골라야 끝난다. 끝난 뒤 고른 것은 선택으로 남는다(엔진 명령이 그대로 쓰게). 결과 CAD_EdGetInputIds */
CAD_API CAD_Status CAD_EdSSGet(const char* prompt, const CAD_EdInputOptions* opt);

/* 마지막 답(또는 묻는 중이면 status PENDING). 한 번도 안 물었으면 CAD_E_NOT_READY */
CAD_API CAD_Status CAD_EdGetInputResult(CAD_EdInputResult* out);
/* 마지막 답의 글(글·키워드) — buf 에 NUL 까지 담고(모자라면 잘라서) 전체 길이(NUL 제외) */
CAD_API int32_t    CAD_EdGetInputText(char* buf, uint32_t capacity);
/* 마지막 답의 객체들(SELECTION·ENTITY) — 칸만큼 채우고 전체 개수 */
CAD_API int32_t    CAD_EdGetInputIds(uint32_t* outIds, uint32_t capacity);
/* 묻는 중이면 CAD_ED_RESULT_CANCEL 로 끝낸다(onDone 도 불림). 안 묻는 중이면 아무 일 없이 CAD_OK */
CAD_API CAD_Status CAD_EdCancelInput(void);

typedef struct CAD_EdSelectOptions {
    uint32_t size;       /* sizeof(CAD_EdSelectOptions) */
    bool     crossing;   /* false = 창(안에 다 든 것, acedSSGet "W"), true = 교차(걸친 것도, "C") */
} CAD_EdSelectOptions;

/* 화면 없이 창 선택 — 두 구석(월드)을 지금 보기(활성 칸 카메라)로 화면에 옮겨 사람이 드래그한 것과 같은 판정.
 * 선택은 바꾸지 않는다(필요하면 CAD_SetSelection). 칸만큼 채우고 전체 개수. 구석이 카메라 뒤면 CAD_E_INVALID_ARG,
 * 화면에서 3px 도 안 벌어지면 CAD_E_DEGENERATE */
CAD_API int32_t    CAD_EdSelectWindow(CAD_GeVec3 corner1, CAD_GeVec3 corner2, const CAD_EdSelectOptions* opt,
                                      uint32_t* outIds, uint32_t capacity);

/* 월드 ↔ 화면 좌표(acedCoordFromWorldToPixel · acedCoordFromPixelToWorld) — 활성 칸 카메라, 화면 = 창 안 좌표(CAD_OnMouseXxx 와
 * 같은 단위, 왼쪽 위 0,0). PixelToWorld 는 클릭이 고르는 점과 같은 작업 평면 위 점(스냅 없음). 화면이 아직 없으면 CAD_E_NOT_READY,
 * 점이 카메라 뒤면 CAD_E_INVALID_ARG */
CAD_API CAD_Status CAD_EdWorldToPixel(CAD_GeVec3 point, double* outX, double* outY);

/* 창 안 좌표 → 월드(acedCoordFromPixelToWorld) — 그 자리를 클릭하면 고르는 작업 평면 위 점(스냅 없음) */
CAD_API CAD_Status CAD_EdPixelToWorld(double x, double y, CAD_GeVec3* outPoint);

typedef struct CAD_EdCommandState {
    uint32_t size;          /* 부르는 쪽이 sizeof 로 채움 */
    bool     commandActive; /* 명령이 진행 중(값·점·대상을 기다림) — 시스템 변수 CMDACTIVE */
    int32_t  inputKind;     /* CAD_EdGetXxx 로 묻는 중이면 그 종류, 아니면 0 */
} CAD_EdCommandState;

/* 명령이 진행 중인지·묻는 중인 종류 — out->size 를 sizeof 로 채워 넘긴다 */
CAD_API CAD_Status CAD_EdGetCommandState(CAD_EdCommandState* out);
/* 진행 중인(끝났으면 마지막으로 실행한) 명령 이름 — 명령행에 친 첫 낱말, 소문자(CMDNAMES). 없으면 "" */
CAD_API int32_t    CAD_EdGetCommandName(char* buf, uint32_t capacity);

#ifdef __cplusplus
}
#endif
