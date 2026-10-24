#pragma once
/* LotCAD C API - view  [AcGs (graphics / view)]
 * Camera, standard views, projection, viewports, visual style, live section, capture.
 * 카메라·표준 뷰·투영·분할 화면·표시 방식·실시간 단면·화면 캡처.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif
// 치수 **문자**를 줌과 무관하게 화면상 같은 크기로 그릴지 (기본 false).
// 모바일에서 치수는 도면 요소보다 "측정 도구" 에 가깝다 — 줌아웃하면 글자가 같이 작아져
// 값을 못 읽는 게 문제였다. 켜면 글자가 항상 읽히는 크기로 남는다(선·화살표는 그대로).
// 데스크톱은 끄는 게 맞다 — 도면 출력에선 월드 크기여야 한다.
// 매 프레임 비용은 없다(플래그를 정점에 굽는다). 전환 시 기존 치수를 한 번 다시 만든다.
CAD_API void CAD_SetDimensionTextScreenFixed(bool enabled);
CAD_API bool CAD_GetDimensionTextScreenFixed(void);

CAD_API void CAD_RequestZoomExtents(void);

CAD_API void CAD_RequestFocusSelected(void);
CAD_API void CAD_RequestToggleProjection(void);
CAD_API void CAD_RequestToggleDemoLighting(void);

CAD_API void CAD_RequestAdjustTextureScale(float delta);
CAD_API void CAD_RequestAdjustLineWidth(float deltaPx);
// viewType: 0=Front 1=Top 2=Right 3=Isometric 4=Left 5=Bottom 6=Back
CAD_API void CAD_RequestSetView(int viewType);
CAD_API void CAD_RequestSetProjection(bool ortho);

// 임의 방향 시점 — 뷰큐브의 모서리(2면)/꼭짓점(3면)처럼 표준 6뷰가 아닌 방향에서 보기.
// dir = 타겟에서 카메라를 향하는 월드 방향(정규화 불필요). 예: (1,-1,1)=앞·우·위 꼭짓점.
CAD_API void CAD_RequestSetViewDirection(float dirX, float dirY, float dirZ);

// 뷰 회전 피벗 (viewucs) — 작업평면 UCS 와 별개로, 화면을 돌릴 때의 중심/축을 지정한다.
//   axis: -1=축 자유(피벗만 고정), 0=X 축 고정, 1=Y, 2=Z (축 고정 시 그 축 기준 턴테이블 회전)
CAD_API void CAD_RequestSetViewPivot(float x, float y, float z, int axis);
CAD_API void CAD_RequestClearViewPivot(void);
// 현재 피벗 조회 — 설정돼 있으면 true. out 인자는 null 허용.
CAD_API bool CAD_GetViewPivot(float* x, float* y, float* z, int* axis);

// ── 실시간 단면 — 셰이더가 잘라 보여 준다(보기 상태, undo 없음). 패널(section 명령)과 같은 상태라 둘이 같이 움직인다.
//   mode 0 끄기 1 평면(axis 위치 pos 보다 큰 쪽을 자름, flip 이면 반대) 2 슬라이스(pos 중심 thickness 두께만 남김) 3 상자(SetSectionBox).
//   axis 0 X 1 Y 2 Z. thickness 는 슬라이스에만(0 이하면 지금 값 유지). 틀린 값 false.
CAD_API bool CAD_SetSection(int mode, int axis, float pos, bool flip, float thickness);
CAD_API bool CAD_SetSectionBox(float minX, float minY, float minZ, float maxX, float maxY, float maxZ);   // 상자 값만(켜기는 SetSection(3,…))
CAD_API void CAD_SetSectionOptions(bool showArrows, bool selectedOnly);
// {"mode","modeName","axis","pos","flip","thickness","box":{"min","max"},"showArrows","selectedOnly","sceneBounds":{"min","max"}} — sceneBounds = 슬라이더 범위
CAD_API int  CAD_GetSectionStateJson(char* out, int cap);
// 지금 평면 단면 → 2D 윤곽(편집 가능한 폴리선, includeBehind 면 뒤쪽 회색 참조선 1개 더)을 모델 오른쪽 XY 평면에. 반환 = 만든 객체 수, undo 1.
CAD_API uint32_t CAD_ExtractSectionTo2D(bool includeBehind);

// ── 멀티뷰포트 (화면 분할) ──
// layout: 0=Single(단일) 1=Dual(좌우) 2=Triple 3=Quad(2x2)
CAD_API void CAD_SetViewportLayout(int layout);
CAD_API int  CAD_GetViewportLayout(void);
// 활성(클릭) 뷰포트 칸 인덱스 0~3.
CAD_API void CAD_SetActiveViewport(int index);
CAD_API int  CAD_GetActiveViewport(void);

// ── 뷰/표시 상태 토글 ──
CAD_API void CAD_SetGridEnabled(bool enabled);
CAD_API void CAD_SetDemoLighting(bool enabled);
// style: 0=Shaded 1=ShadedEdge 2=Wireframe 3=WireframeEdge 4=HiddenLine
CAD_API void CAD_SetVisualStyle(int style);

// 선택 하이라이트 스타일: 0=Silhouette(JFA 외곽선), 1=Edge(feature edge 노란색, CAD 방식)
CAD_API void CAD_SetSelectionStyle(int style);
CAD_API int  CAD_GetSelectionStyle(void);

// 호버 강조 — 마우스가 올라간 객체를 연한 하늘색 엣지로 표시(선택은 노란색).
// 기본 켬. 도면 작업 중 시선 분산이 싫거나 초대형 씬에서 부담될 때 끌 수 있다.
CAD_API void CAD_SetHoverHighlight(bool enabled);
CAD_API bool CAD_GetHoverHighlight(void);
// 현재 커서 아래 객체 id (없으면 0). 호스트가 상태바·툴팁에 이름을 띄우는 용도.
CAD_API unsigned int CAD_GetHoveredObject(void);

// 호버 표시 스타일 — 색(0~1) + 선 두께(px, 0.5~10 로 클램프).
// ⚠️ 두께는 GPU 가 wide line 을 지원할 때만 반영된다(미지원 기기는 1px 고정).
CAD_API void CAD_SetHoverStyle(float r, float g, float b, float width);
// 선택 표시 두께 (색은 노란색 고정 — CAD 관례).
CAD_API void CAD_SetSelectionLineWidth(float width);

// 벽 충돌 (Walk / 캐릭터 모드). 끄면 벽을 통과한다.
// ⚠️ 정적 지오메트리 대상의 캐릭터 충돌이지 물리엔진이 아니다 — 물체는 떨어지지 않는다.
CAD_API void CAD_SetCollisionEnabled(bool enabled);
CAD_API bool CAD_GetCollisionEnabled(void);

/* 화면 캡처 → PNG(창 전체). clean = 그리드·뷰큐브 없이. 한 프레임 그려 파일이 생겼는지까지 확인하고 돌아온다
 * (엔진 틱 안 — 플러그인 콜백 등 — 에서 불리면 요청만 남기고 다음 프레임에 찍는다, true = 요청됨). AI 가 결과를 눈으로 볼 때. */
CAD_API bool     CAD_CaptureViewport(const char* pathUtf8, bool clean);
/* 카메라 — 지금 궤도 중심 둘레로 (ax,ay,az) 축 angleDeg 만큼 돌리기. 턴테이블 = (0,0,1). */
CAD_API void     CAD_OrbitCamera(float ax, float ay, float az, float angleDeg);

#ifdef __cplusplus
}
#endif
