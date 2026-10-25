#pragma once
/* LotCAD C API - arch  [(architecture)]
 * Rooms, floorplans, walls from images.
 * 방·평면도·이미지에서 벽.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"
#include "lotcad_geometry.h"   /* CAD_GeVec3 */

#ifdef __cplusplus
extern "C" {
#endif
/* 새 규칙: CAD_Status(실패 이유 = CAD_GetLastError) · 개수·글 함수 = int32_t 전체 개수·길이(실패면 음수 CAD_E_*), 칸은 uint32_t.
 * 좌표 = 월드(사각형·선분도 월드 XY, 바닥 높이는 baseZ), 길이 = 장면 단위(m 장면 기준으로 만든 기능 — 문 폭 0.9 등 기본값이 m).
 * 엔진 스레드에서만(이미지 추출만 엔진 없이 아무 스레드). 만드는 함수는 되돌리기 1, CAD_CreateOptions.propsFrom 은 벽마다. */

/* 방 하나 — floorCenter = 바닥 가운데, width·depth = 안쪽 크기, 모두 > 0. outWallIds = 4칸(NULL 가능), 차례 남·북·서·동 */
CAD_API CAD_Status CAD_CreateRoom(CAD_GeVec3 floorCenter, double width, double depth, double height, double wallThickness,
                                  const CAD_CreateOptions* opt, uint32_t* outWallIds);

enum {   /* 개구부 종류 */
    CAD_OPENING_DOOR   = 0,
    CAD_OPENING_WINDOW = 1
};
enum {   /* 방 하나의 벽 쪽(roomBIndex < 0 일 때) */
    CAD_WALL_SOUTH = 0,
    CAD_WALL_NORTH = 1,
    CAD_WALL_WEST  = 2,
    CAD_WALL_EAST  = 3
};
enum {   /* 벽 위 맞춤 */
    CAD_OPENING_CENTER = 0,   /* 가운데 + offset(+X/+Y 쪽 부호) */
    CAD_OPENING_START  = 1,   /* 서·남 끝에서 offset 안쪽 */
    CAD_OPENING_END    = 2    /* 동·북 끝에서 offset 안쪽 */
};
/* 문·창 하나 — roomBIndex >= 0 이면 두 방이 함께 쓰는 벽, < 0 이면 roomAIndex 방의 side 쪽 벽 */
typedef struct CAD_FloorplanOpeningDesc {
    int32_t  type;         /* CAD_OPENING_DOOR·WINDOW */
    uint32_t roomAIndex;
    int32_t  roomBIndex;
    int32_t  side;         /* CAD_WALL_* */
    double   width, height;
    double   sillHeight;   /* 바닥에서 아래턱까지(문 0) */
    int32_t  alignment;    /* CAD_OPENING_CENTER·START·END */
    double   offset;
} CAD_FloorplanOpeningDesc;
/* 평면도 — rectBounds = 방마다 [minX,minY,maxX,maxY](월드 XY) × spaceCount, 맞닿은 벽은 하나로. 문·창은 openings(없으면 NULL, 0).
 * 반환 = 만든 벽 조각 수(개구부를 뺀 뒤), outWallIds 에 capacity 개까지. 방·종류·쪽·맞춤 번호 범위 밖 = CAD_E_OUT_OF_RANGE */
CAD_API int32_t    CAD_CreateFloorplan(double baseZ, const double* rectBounds, uint32_t spaceCount, double height, double wallThickness,
                                       const CAD_FloorplanOpeningDesc* openings, uint32_t openingCount,
                                       const CAD_CreateOptions* opt, uint32_t* outWallIds, uint32_t capacity);

// ── 평면도 이미지 → 벽 (AI 없이) ───────────────────────────────────────
// 추출은 장면을 바꾸지 않는다. widthMm = 도면 전체 폭(벽 중심선, mm), 0 이면 문 폭 900mm 로 축척 추정.
// 출력 JSON(mm, 좌하단 원점·Y 위): {"widthMm","depthMm","walls":[{"x1","y1","x2","y2","thicknessMm","exterior"}],
//   "outerThicknessMm","innerThicknessMm","scaleEstimated","doorCount","imageWidthMm","imageOrigin":[x,y],"summary"}
//   — imageWidthMm/imageOrigin = 이미지 **전체**의 실폭·좌하단(바닥에 깔 때). 반환 = 전체 길이. 벽 없음·못 읽음 = CAD_E_FAILED + 이유
CAD_API int32_t    CAD_FloorplanExtractFromImage(const char* path, double widthMm, char* buf, uint32_t capacity);
// rgba = 4바이트 × width × height(행 우선, 위에서 아래) — 모바일 카메라·사진 선택기용.
CAD_API int32_t    CAD_FloorplanExtractFromRgba(const unsigned char* rgba, int32_t width, int32_t height, double widthMm,
                                                char* buf, uint32_t capacity);
/* 벽 그래프 → 3D 벽. segments = [x1,y1,x2,y2,thickness](월드 XY, m) × count, 축에 나란한 벽만. thickness <= 0 이면 defaultThickness.
 * 반환 = 만든 벽 수, outIds 에 capacity 개까지 */
CAD_API int32_t    CAD_CreateWallGraph(double baseZ, const double* segments, uint32_t count, double height, double defaultThickness,
                                       const CAD_CreateOptions* opt, uint32_t* outIds, uint32_t capacity);
/* 편의 — 이미지에서 벽을 찾아 m 로 세우고, underlayImage 면 원본을 같은 축척으로 바닥에(AI create_wall_graph 와 같음).
 * 반환 = 만든 벽 수(바닥 이미지는 outIds 에 안 들어감 — 되돌리기는 함께) */
CAD_API int32_t    CAD_CreateFloorplanFromImage(const char* path, double widthMm, double height, bool underlayImage,
                                                const CAD_CreateOptions* opt, uint32_t* outIds, uint32_t capacity);

#ifdef __cplusplus
}
#endif
