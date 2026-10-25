#pragma once
/* LotCAD C API - drawing  [(annotation / drafting)]
 * Text, dimensions, leaders, hatches, drawing views, plot, raster images, OCR.
 * 문자·치수·지시선·해치·도면 뷰·출력·이미지·OCR.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"
#include "lotcad_geometry.h"   /* CAD_GeVec3 */

#ifdef __cplusplus
extern "C" {
#endif
/* 새 규칙: CAD_Status(실패 이유 = CAD_GetLastError) · 개수·글 함수 = int32_t 전체 길이(실패면 음수 CAD_E_*), 칸은 uint32_t.
 * 좌표·길이 = 월드 mm(double), 각 = rad. 엔진 스레드에서만(아니면 CAD_E_WRONG_THREAD).
 * 만드는 함수는 되돌리기 한 단계, opt = NULL 이면 지금 도면층·색(CAD_CreateOptions.propsFrom 을 주면 그 객체의 도면층·색·선종류), 새 id 는 *outId. */

// ── 문자(Text) + 편집(textedit) — 모든 프론트엔드 공통 진입점 ──
/* 문자 — position = 기준점, height > 0(mm). 빈 글 "" 도 된다 */
CAD_API CAD_Status CAD_CreateText(CAD_GeVec3 position, const char* utf8, double height, const CAD_CreateOptions* opt, uint32_t* outId);
/* 선형 치수 — 측정점 p1/p2 + 치수선 위치점 + 작업평면 법선. p1 = p2 · 법선 0 = CAD_E_DEGENERATE */
CAD_API CAD_Status CAD_CreateDimension(CAD_GeVec3 p1, CAD_GeVec3 p2, CAD_GeVec3 dimLinePoint, CAD_GeVec3 normal,
                                       const CAD_CreateOptions* opt, uint32_t* outId);
/* 글 바꾸기(되돌리기 1). 문자가 아님 = CAD_E_WRONG_TYPE, 잠김 = CAD_E_LOCKED */
CAD_API CAD_Status CAD_SetTextContent(uint32_t id, const char* utf8);
/* 글 읽기 — buf 에 NUL 까지(모자라면 글자 경계에서 자름), 반환 = 전체 길이(NUL 제외). 문자가 아님 = CAD_E_WRONG_TYPE */
CAD_API int32_t    CAD_GetTextContent(uint32_t id, char* buf, uint32_t capacity);

// ── 도면 뷰(3D → 2D, 솔리드웍스 Drawing 식) — 뷰는 장면 객체가 아니라 CAD_GetObjectIds 에 안 나온다. 좌표 = 도면 평면(월드 XY, mm, z 는 안 씀).
// 3D 를 고치면 따라온다(연관). 만들기·지우기·옮기기는 되돌리기 1.
/* 정면·평면·우측면(3각법) + 등각(0.6배), 모델 치수 자동. 반환 = 만든 뷰 수(4). ids 없으면(count 0) 보이는 솔리드 전부. scale 0 = 1 */
CAD_API int32_t    CAD_CreateDrawingViews(const uint32_t* ids, uint32_t count, double scale);
/* 단면도 A-A — 정투상 뷰를 가로지르는 선(첫 점 → 둘째 점), 보는 쪽 = 선의 왼쪽. *outViewId = 뷰 id */
CAD_API CAD_Status CAD_CreateSectionView(CAD_GeVec3 a, CAD_GeVec3 b, uint32_t* outViewId);
/* 상세도 — 정투상 뷰 위 원(중심·반지름 > 0)을 factor 배(0 = 2)로 도면 오른쪽에 */
CAD_API CAD_Status CAD_CreateDetailView(CAD_GeVec3 center, double radius, double factor, uint32_t* outViewId);
/* 뷰 옮기기(offset 의 x·y) — 3각법 정렬 유지(평면도는 위아래, 우측면도는 좌우, 정면도는 매달린 뷰·단면도와 함께).
 * 그 뷰가 없거나 정렬 때문에 못 움직임 = CAD_E_NOT_FOUND */
CAD_API CAD_Status CAD_MoveDrawingView(uint32_t viewId, CAD_GeVec3 offset);
CAD_API CAD_Status CAD_ClearDrawingViews(void);
/* 뷰 목록 JSON — [{"id","name","kind":"base|section|detail","dir","up","origin","scale","hidden","dims","sources",
 * "parent","label"(단면·상세),"bounds":{"min":[x,y],"max":[x,y]}}] — bounds = 뷰가 차지하는 자리(선 + 모델 치수 + 이름). 반환 = 전체 길이 */
CAD_API int32_t    CAD_GetDrawingViewsJson(char* buf, uint32_t capacity);

/* ── 이미지 붙이기 ────────────────────────────────────────────────────────
 *
 * 도면 밑에 깔 이미지(평면도 사진 등)를 XY 평면에 붙인다.
 * 엔진의 imageattach 명령은 **파일 대화상자를 띄우므로 모바일에서 못 쓴다** —
 * 호스트가 사진 앱(PHPicker / Intent)에서 고른 뒤 여기로 넘긴다.
 *
 *   FromFile   : 경로로. 데스크톱·모바일 공통. 파일이 없음 = CAD_E_NOT_FOUND, 못 읽음 = CAD_E_FAILED.
 *   FromMemory : RGBA8 픽셀(width × height × 4 바이트)을 직접. 사진 앱이 경로 대신 데이터를 주는 경우
 *                (iOS PHPicker 가 그렇다) 파일로 떨구지 않고 바로 넘길 수 있다. displayName NULL = "이미지".
 *
 * widthWorld = 0 이면 긴 변이 10 단위가 되게 자동. 종횡비는 항상 보존한다. origin = 왼쪽 아래.
 */
CAD_API CAD_Status CAD_AttachImageFromFile(const char* pathUtf8, double widthWorld, CAD_GeVec3 origin,
                                           const CAD_CreateOptions* opt, uint32_t* outId);
CAD_API CAD_Status CAD_AttachImageFromMemory(const unsigned char* rgba, int32_t width, int32_t height, const char* displayName,
                                             double widthWorld, CAD_GeVec3 origin, const CAD_CreateOptions* opt, uint32_t* outId);

/* ── OCR 결과 주입 (모바일용) ─────────────────────────────────────────────
 *
 * 모바일은 **OS 내장 OCR 을 쓴다** — iOS Vision, 안드로이드 ML Kit.
 * Tesseract(45MB)를 올릴 이유가 없고, 내장 쪽이 한글·혼합 글자에서 더 정확하다.
 * 다만 둘 다 Swift/Kotlin API 라 C++ 에서 부르기 번거로우므로, **호스트가 인식하고
 * 결과만 넘긴다.** 그 뒤 흐름(네모 표시 → 드래그로 줄 고르기 → 커서 배치)은
 * 데스크톱과 완전히 같다.
 *
 * imageId : CAD_AttachImage* 로 붙인 이미지(없으면 CAD_E_BAD_HANDLE)
 * 사각형  : 그 **이미지의 픽셀 좌표**(좌상단 원점). Vision 의 정규화 좌표를 쓰면
 *           호스트에서 픽셀로 바꿔 넘겨야 한다.
 * 호출 순서대로 = 읽는 순서. "시작~끝 사이 전부" 선택이 이 순서를 따른다.
 * Begin 없이 Add·End = CAD_E_NOT_READY, 빈 글 = CAD_E_INVALID_ARG.
 *
 *   CAD_BeginOcrLines(imageId);
 *   CAD_AddOcrLine("거실 3600", 29, 29, 192, 64);
 *   CAD_EndOcrLines();          // 여기서 화면에 네모가 뜬다
 */
CAD_API CAD_Status CAD_BeginOcrLines(uint32_t imageId);
CAD_API CAD_Status CAD_AddOcrLine(const char* utf8, int32_t x0, int32_t y0, int32_t x1, int32_t y1);
CAD_API CAD_Status CAD_EndOcrLines(void);

/* 지시선 — 화살촉 → 꺾임 점 + 글(UTF-8, 여러 줄은 \n, NULL = 글 없음). textHeight <= 0 이면 2.5. 평면은 XY */
CAD_API CAD_Status CAD_CreateLeader(CAD_GeVec3 tip, CAD_GeVec3 bend, const char* textUtf8, double textHeight,
                                    const CAD_CreateOptions* opt, uint32_t* outId);

/* 해치 — 닫힌 폴리선·사각형·원 ids(같은 평면이면 한 객체, 안쪽 루프 = 구멍). pattern: SOLID ANSI31~38 NET LINE DOTS BRICK STEEL CROSS
 * (NULL/빈 = ANSI31), scale > 0, angle rad. 선택이 새 해치로 바뀐다. 경계가 맞지 않음 = CAD_E_FAILED + 이유 */
CAD_API CAD_Status CAD_CreateHatch(const uint32_t* ids, uint32_t count, const char* pattern, double scale, double angle,
                                   const CAD_CreateOptions* opt, uint32_t* outId);
/* 도면 출력 — path 확장자로 .pdf(벡터)/.png(래스터). 지금 뷰 방향, 흰 종이. paperW/H mm(0 = A3 가로 420×297), pngLongSidePx(0 = 4000).
 * selectedOnly = 선택만(선택 없음 = CAD_E_NOT_FOUND), monochrome = 흑백. 3D 메시·이미지는 아직 안 나온다 */
CAD_API CAD_Status CAD_Plot(const char* path, bool selectedOnly, bool monochrome, double paperW, double paperH, int32_t pngLongSidePx);

#ifdef __cplusplus
}
#endif
