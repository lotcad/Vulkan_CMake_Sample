#pragma once
/* LotCAD C API - modify  [(modify commands)]
 * Stretch/lengthen/break/align/offset/trim/extend.
 * 늘이기·길이조정·끊기·3D 정렬·오프셋·자르기·연장. 옮기기·돌리기·축척·복사·분해·배열·대칭은 lotcad_objects.h 의 CAD_Entity*.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h.
 *
 * 클릭 대신 점을 값으로 — 대화형 도구와 같은 계산, 전부 되돌리기 한 단계. 좌표·길이 = 월드 mm.
 * 새 객체를 주는 함수(끊기·오프셋·자르기·연장)는 반환 = 만든(만들) 개수: outIds = NULL(칸 0)이면 개수만 알려 주고 아무것도 안 바꾸며,
 * 칸이 모자라도 아무것도 안 바꾼다(개수만 돌려줌). 엔진 스레드에서만 — 다른 스레드면 CAD_E_WRONG_THREAD. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif

/* 늘이기(STRETCH) — 교차 창(corner1·corner2 의 월드 x·y, z 는 안 봄 — 평면도용) 안에 든 편집점만 offset 만큼.
 * 반환 = 걸린 객체 수(0 = 창에 걸린 것 없음 — 오류 아님). 고를 수 없는 객체(숨김·잠긴 도면층)는 건너뛴다. */
CAD_API int32_t    CAD_StretchWindowXY(CAD_GeVec3 corner1, CAD_GeVec3 corner2, CAD_GeVec3 offset);

/* 길이조정(LENGTHEN) — 선·열린 폴리선·호의 한 끝(atStart = 시작 쪽)을. */
enum {
    CAD_LENGTHEN_DELTA   = 0,   /* value = 늘릴 길이(mm, 음수 = 줄임) */
    CAD_LENGTHEN_PERCENT = 1,   /* value = 지금 길이의 % (50 = 절반) */
    CAD_LENGTHEN_TOTAL   = 2    /* value = 새 전체 길이(mm) */
};
/* 그 밖의 종류 CAD_E_WRONG_TYPE, 길이가 0 이하가 되거나 호가 한 바퀴를 넘으면 CAD_E_OUT_OF_RANGE. */
CAD_API CAD_Status CAD_Lengthen(uint32_t id, int32_t mode, double value, bool atStart);

/* 끊기(BREAK) — 두 점(곡선 위로 투영) 사이를 지운다. 같은 점이면 그 자리에서 둘로 나눈다(원·닫힌 폴리선은 두 점이어야).
 * 선·폴리선·원·호. 반환 = 남은 조각 수, outIds = 그 id(원본은 지워진다). */
CAD_API int32_t    CAD_BreakObject(uint32_t id, CAD_GeVec3 point1, CAD_GeVec3 point2, uint32_t* outIds, uint32_t capacity);

/* 3D 정렬(3DALIGN) — ids 를 점 쌍 pairs 개(1~3)로: 1 = 옮기기, 2 = 방향 맞추기(최단 회전), 3 = 방향까지(틀 맞춤).
 * source·target = pairs 개씩. 반환 = 옮긴 객체 수. 하나라도 없거나 잠겼으면 아무것도 안 옮긴다. */
CAD_API int32_t    CAD_Align3D(const uint32_t* ids, uint32_t count, const CAD_GeVec3* source, const CAD_GeVec3* target, uint32_t pairs);

/* 오프셋(OFFSET) — 선·원·호·폴리선을 distance(> 0) 만큼 sidePoint 쪽으로 평행 복제. 반환 = 새로 만든 개수. */
CAD_API int32_t    CAD_Offset(const uint32_t* ids, uint32_t count, double distance, CAD_GeVec3 sidePoint, uint32_t* outIds, uint32_t capacity);

/* 자르기(TRIM)·연장(EXTEND) — 대상 하나. pickPoint = 지울 부분 / 늘릴 끝 가까운 점. 경계 = boundaryIds(0 개 = 장면의 선·폴리선 전부).
 * 원·호는 제 평면에서, 선·폴리선은 planeNormal(0,0,0 = 지금 작업 평면)에 투영해 교차. 원본은 지워지고 결과 조각이 새 id 로.
 * 반환 = 결과 조각 수(자르기는 0 = 통째로 지움), 교차가 없어 못 하면 CAD_E_FAILED(아무것도 안 바뀜). */
CAD_API int32_t    CAD_Trim(uint32_t id, CAD_GeVec3 pickPoint, const uint32_t* boundaryIds, uint32_t boundaryCount, CAD_GeVec3 planeNormal,
                            uint32_t* outIds, uint32_t capacity);
CAD_API int32_t    CAD_Extend(uint32_t id, CAD_GeVec3 pickPoint, const uint32_t* boundaryIds, uint32_t boundaryCount, CAD_GeVec3 planeNormal,
                              uint32_t* outIds, uint32_t capacity);

#ifdef __cplusplus
}
#endif
