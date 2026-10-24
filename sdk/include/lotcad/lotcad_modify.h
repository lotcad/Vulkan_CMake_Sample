#pragma once
/* LotCAD C API - modify  [(modify commands)]
 * Move/copy/array/explode/stretch/lengthen/break/offset/mirror/trim/extend/align.
 * 이동·복사·배열·분해·늘이기·길이조정·끊기·오프셋·대칭·자르기·연장·정렬.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif
CAD_API void CAD_RequestMoveSelected(float dirX, float dirY, float dirZ, float distance);
CAD_API void CAD_RequestRotateSelected(float axisX, float axisY, float axisZ, float angleDeg);
CAD_API void CAD_RequestScaleSelected(float factor);
CAD_API void CAD_RequestCopySelected(float dirX, float dirY, float dirZ,
                                     float distance, int count);
CAD_API void CAD_RequestColorSelected(float r, float g, float b);

// ── 편집 명령 ───────────────────────────────────────────────────────────
// 전부 **현재 선택**에 적용되고 각각 undo 1스텝으로 들어간다. 화면 클릭이 필요 없는
// (인자만으로 결정되는) 명령들만 여기 노출한다 — 트림/연장/오프셋 방향처럼 커서가 있어야
// 뜻이 정해지는 것들은 대화형이라 별도 픽 API(CAD_BeginGetPoint 등)를 거쳐야 한다.

// 분해(EXPLODE) — 선택 객체를 구성 요소로 쪼갠다.
//   문자                → 글리프 윤곽선 폴리선
//   폴리선/사각형/다각형 → 개별 선분 (닫힌 도형은 마지막↔첫 정점 구간까지)
// 선·원·호는 더 쪼갤 수 없어 그대로 남는다. keepOriginal=true 면 원본을 지우지 않는다.
// 여러 종류가 섞여 있어도 undo 는 한 번이다. 쪼갤 것이 하나도 없으면 false.
CAD_API bool CAD_Explode(bool keepOriginal);

// 직사각형 배열 — cols(가로 개수) × rows(세로 개수), dx/dy 간격(음수 = 반대 방향).
// 원본이 (0,0) 칸을 차지하므로 실제 생성 개수는 cols*rows-1.
// 평면은 활성 뷰에서 정해진다 (Top=XY, Front=XZ, Right=YZ).
CAD_API bool CAD_ArrayRect(int cols, int rows, float dx, float dy);

// 원형 배열 — count = **원본 포함** 총 개수, angleDeg = 총 채움 각(360 = 한 바퀴).
// center = 회전 중심(월드), rotateItems=false 면 항목 방향을 유지한 채 위치만 옮긴다.
// 회전축은 활성 뷰의 평면 법선이다.
CAD_API bool CAD_ArrayPolar(int count, float angleDeg,
                            float centerX, float centerY, float centerZ,
                            bool rotateItems);

/* 늘이기 — XY 교차 창(월드) 안의 편집점을 (dx,dy,dz) 만큼. 창 판정은 z 를 보지 않는다. 반환 = 걸린 객체 수. */
CAD_API uint32_t CAD_StretchWindowXY(float minX, float minY, float maxX, float maxY, float dx, float dy, float dz);
/* 길이조정 — mode 0 = 증분, 1 = 퍼센트, 2 = 전체 길이. atStart = 시작 쪽 끝. 선·열린 폴리선·호. */
CAD_API bool     CAD_Lengthen(uint32_t id, int mode, float value, bool atStart);
/* 끊기 — 두 점(객체 위로 투영) 사이를 지운다. 같은 점이면 둘로 나눈다. 결과는 새 객체들(원본 삭제). */
CAD_API bool     CAD_BreakObject(uint32_t id, float x1, float y1, float z1, float x2, float y2, float z2);

/* 3D 배열 — 현재 선택을 월드 X(열)·Y(행)·Z(층) 격자로. 생성 = cols*rows*levels - 1. */
CAD_API bool     CAD_Array3DRect(int cols, int rows, int levels, float dx, float dy, float dz);
/* 3D 원형 배열 — 현재 선택을 두 점(a→b) 축 둘레로. count = 원본 포함 총 개수. */
CAD_API bool     CAD_Array3DPolar(int count, float angleDeg,
                                  float ax, float ay, float az, float bx, float by, float bz, bool rotateItems);
/* 3D 정렬 — ids 를 점 pairs 쌍(1~3)으로. src/dst = pairs*3. 1 = 이동, 2 = 방향, 3 = 방향까지. 반환 = 옮긴 객체 수. */
CAD_API uint32_t CAD_Align3D(const uint32_t* ids, uint32_t count, const float* srcXYZ, const float* dstXYZ, int pairs);

/* 오프셋·대칭·자르기·연장 — 클릭 대신 점을 값으로(도구와 같은 계산, 전부 undo 1). 좌표는 월드.
 * outIds/outCapacity 는 새 객체 id 받을 곳(null 이면 안 받음). 반환 = 새로 만든 개수.
 *   CAD_Offset : 선·원·호·폴리선을 distance(>0) 만큼 (sx,sy,sz) 쪽으로 평행 복제.
 *   CAD_Mirror : 미러선 (x1..z1)→(x2..z2) 과 작업 평면 법선 (nx,ny,nz)(0,0,0 = 지금 작업 평면)이 이루는 면으로 반사 복제.
 *                선·원·호·폴리선·메시. deleteOriginals = 원본 지움.
 *   CAD_Trim / CAD_Extend : 대상 하나, (px,py,pz) = 지울 부분 / 늘릴 끝 가까운 점. 경계 ids(0개 = 씬의 선·폴리선 전부).
 *                원·호는 제 평면, 선·폴리선은 (nx,ny,nz)(0 = 지금 작업 평면)에 투영해 교차. 못 하면 false(변화 없음). */
CAD_API uint32_t CAD_Offset(const uint32_t* ids, uint32_t count, float distance, float sx, float sy, float sz,
                            uint32_t* outIds, uint32_t outCapacity);
CAD_API uint32_t CAD_Mirror(const uint32_t* ids, uint32_t count, float x1, float y1, float z1, float x2, float y2, float z2,
                            float nx, float ny, float nz, bool deleteOriginals, uint32_t* outIds, uint32_t outCapacity);
CAD_API bool     CAD_Trim(uint32_t id, float px, float py, float pz, const uint32_t* boundaryIds, uint32_t boundaryCount,
                          float nx, float ny, float nz);
CAD_API bool     CAD_Extend(uint32_t id, float px, float py, float pz, const uint32_t* boundaryIds, uint32_t boundaryCount,
                            float nx, float ny, float nz);

#ifdef __cplusplus
}
#endif
