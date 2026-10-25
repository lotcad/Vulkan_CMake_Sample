#pragma once
/* LotCAD C API - view  [AcGs (graphics / view)]
 * Camera, standard views, projection, viewports, visual style, live section, capture.
 * 카메라·표준 뷰·투영·분할 화면·표시 방식·실시간 단면·화면 캡처.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h.
 *
 * 보기 상태라 되돌리기에 남지 않는다(단면을 2D 로 꺼내기만 되돌리기 1). 카메라 움직임(전체 보기·뷰 바꾸기·방향·피벗·고른 것 보기)은
 * 다음 틱에 적용된다 — CAD_OK = 맡김. 좌표 = 월드 mm, 각도 = rad. 엔진 스레드에서만. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif

/* ── 카메라·뷰 ── */
CAD_API CAD_Status CAD_ZoomExtents(void);                    /* 전체 보기 */
CAD_API CAD_Status CAD_FocusSelected(void);                  /* 고른 것 보기 — 선택이 없으면 CAD_E_NOT_FOUND */
enum {
    CAD_VIEW_FRONT = 0, CAD_VIEW_TOP = 1, CAD_VIEW_RIGHT = 2, CAD_VIEW_ISOMETRIC = 3,
    CAD_VIEW_LEFT = 4, CAD_VIEW_BOTTOM = 5, CAD_VIEW_BACK = 6
};
CAD_API CAD_Status CAD_SetView(int32_t viewType);           /* CAD_VIEW_*, 범위 밖 CAD_E_OUT_OF_RANGE */
CAD_API CAD_Status CAD_SetProjection(bool ortho);           /* 직교 / 원근 */
CAD_API CAD_Status CAD_GetProjection(bool* outOrtho);       /* 활성 칸이 직교인가(맡긴 SetProjection 은 다음 틱 뒤에 보인다) */
/* 임의 방향 시점 — 뷰큐브의 모서리(2면)·꼭짓점(3면)처럼. direction = 타겟에서 카메라 쪽 월드 방향(길이 무관, 0 = CAD_E_DEGENERATE).
 * 예: (1,-1,1) = 앞·우·위 꼭짓점 */
CAD_API CAD_Status CAD_SetViewDirection(CAD_GeVec3 direction);
/* 화면 회전 피벗(viewucs) — 작업 평면 UCS 와 별개로 화면을 돌릴 때의 중심·축. axis -1 = 축 자유(피벗만), 0·1·2 = X·Y·Z 축 둘레 턴테이블 */
CAD_API CAD_Status CAD_SetViewPivot(CAD_GeVec3 point, int32_t axis);
CAD_API CAD_Status CAD_ClearViewPivot(void);
/* 지금 피벗 — 없으면 CAD_E_NOT_FOUND. 출력은 NULL 가능 */
CAD_API CAD_Status CAD_GetViewPivot(CAD_GeVec3* outPoint, int32_t* outAxis);
/* 지금 궤도 중심 둘레로 axis 축 angle(rad, 오른손) 만큼 — 턴테이블 = (0,0,1). 바로 돈다 */
CAD_API CAD_Status CAD_OrbitCamera(CAD_GeVec3 axis, double angle);

/* ── 실시간 단면 — 셰이더가 잘라 보여 준다. 패널(section 명령)과 같은 상태 ──
 *   mode: CAD_SECTION_* — PLANE = axis 위치 position 보다 큰 쪽을 자름(flip 이면 반대), SLICE = position 가운데 thickness 두께만 남김,
 *   BOX = CAD_SetSectionBox 의 상자. axis 0·1·2 = X·Y·Z. thickness 는 슬라이스에만(0 이하 = 지금 값 그대로). */
enum { CAD_SECTION_OFF = 0, CAD_SECTION_PLANE = 1, CAD_SECTION_SLICE = 2, CAD_SECTION_BOX = 3 };
CAD_API CAD_Status CAD_SetSection(int32_t mode, int32_t axis, double position, bool flip, double thickness);
CAD_API CAD_Status CAD_SetSectionBox(CAD_GeVec3 min, CAD_GeVec3 max);   /* 상자 값만(켜기는 CAD_SetSection(CAD_SECTION_BOX, …)), min < max */
CAD_API CAD_Status CAD_SetSectionOptions(bool showArrows, bool selectedOnly);
/* {"mode","modeName","axis","pos","flip","thickness","box":{"min","max"},"showArrows","selectedOnly","sceneBounds":{"min","max"}} — sceneBounds = 슬라이더 범위 */
CAD_API int32_t    CAD_GetSectionStateJson(char* buf, uint32_t capacity);
/* 지금 평면 단면 → 2D 윤곽(편집 가능한 폴리선, includeBehind 면 뒤쪽 회색 참조선 하나 더)을 모델 오른쪽 XY 평면에. 되돌리기 1.
 * 반환 = 만든 객체 수, outIds = 그 id(outIds = NULL·칸 모자람이면 아무것도 안 만들고 개수만). 평면 단면이 아니면 CAD_E_NOT_READY. */
CAD_API int32_t    CAD_ExtractSectionTo2D(bool includeBehind, uint32_t* outIds, uint32_t capacity);

/* ── 분할 화면 ── */
enum { CAD_LAYOUT_SINGLE = 0, CAD_LAYOUT_DUAL = 1, CAD_LAYOUT_TRIPLE = 2, CAD_LAYOUT_QUAD = 3 };
CAD_API CAD_Status CAD_SetViewportLayout(int32_t layout);   /* CAD_LAYOUT_* */
CAD_API int32_t    CAD_GetViewportLayout(void);             /* CAD_LAYOUT_*, 음수 = 오류 */
CAD_API CAD_Status CAD_SetActiveViewport(int32_t index);    /* 칸 번호 0 ~ (지금 칸 수 − 1) */
CAD_API int32_t    CAD_GetActiveViewport(void);

/* ── 표시 ── */
CAD_API CAD_Status CAD_SetGridEnabled(bool enabled);
CAD_API CAD_Status CAD_SetDemoLighting(bool enabled);
enum { CAD_STYLE_SHADED = 0, CAD_STYLE_SHADED_EDGE = 1, CAD_STYLE_WIREFRAME = 2, CAD_STYLE_WIREFRAME_EDGE = 3, CAD_STYLE_HIDDEN_LINE = 4 };
CAD_API CAD_Status CAD_SetVisualStyle(int32_t style);       /* CAD_STYLE_* */
/* 선택 강조 — 0 = 실루엣(JFA 외곽선), 1 = 모서리(노란 특징선, CAD 식) */
CAD_API CAD_Status CAD_SetSelectionStyle(int32_t style);
CAD_API int32_t    CAD_GetSelectionStyle(void);
/* 선택 표시 두께(px, 색은 노란색 고정 — CAD 관례) */
CAD_API CAD_Status CAD_SetSelectionLineWidth(double width);
/* 호버 강조 — 마우스가 올라간 객체를 연한 하늘색 모서리로(기본 켬) */
CAD_API CAD_Status CAD_SetHoverHighlight(bool enabled);
CAD_API CAD_Status CAD_GetHoverHighlight(bool* outEnabled);
/* 호버 색·두께(px 0.5~10). ⚠️ 두께는 GPU 가 굵은 선을 받을 때만(못 받는 장치는 1px) */
CAD_API CAD_Status CAD_SetHoverStyle(CAD_Color color, double width);
/* 지금 커서 아래 객체(없으면 0 — 오류 아님). 호스트가 상태바·툴팁에 이름을 띄울 때 */
CAD_API CAD_Status CAD_GetHoveredObject(uint32_t* outId);
/* 치수 **글자**를 줌과 무관하게 화면에서 같은 크기로(기본 끔). 모바일 측정 도구용 — 도면 출력은 월드 크기여야 하니 데스크톱은 끔 */
CAD_API CAD_Status CAD_SetDimensionTextScreenFixed(bool enabled);
CAD_API CAD_Status CAD_GetDimensionTextScreenFixed(bool* outEnabled);
/* 고른 객체의 텍스처 축척을 delta 만큼 · 선 두께(px)를 deltaPx 만큼 늘리고 줄이기 */
CAD_API CAD_Status CAD_AdjustTextureScale(double delta);
CAD_API CAD_Status CAD_AdjustLineWidth(double deltaPx);
/* 벽 충돌(걷기·캐릭터 모드) — 끄면 벽을 지나간다. ⚠️ 정적 형상 대상의 캐릭터 충돌이지 물리 엔진이 아니다 */
CAD_API CAD_Status CAD_SetCollisionEnabled(bool enabled);
CAD_API CAD_Status CAD_GetCollisionEnabled(bool* outEnabled);

/* ── 화면 캡처 → PNG(창 전체, 경로 UTF-8). clean = 격자·뷰큐브 없이. 한 프레임 그려 파일이 생겼는지까지 보고 돌아온다
 * (엔진 틱 안 — 플러그인 콜백 등 — 에서 불리면 요청만 남기고 다음 프레임에 찍는다, CAD_OK = 맡김). 못 찍으면 CAD_E_FAILED. */
CAD_API CAD_Status CAD_CaptureViewport(const char* pathUtf8, bool clean);

#ifdef __cplusplus
}
#endif
