#pragma once
/* LotCAD C API - arch  [(architecture)]
 * Rooms, floorplans, walls from images.
 * 방·평면도·이미지에서 벽.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif
// origin = floor center; width/depth = interior clear size; all values are metres.
// outWallIds must point to storage for 4 ids. Order: south, north, west, east.
CAD_API bool CAD_CreateRoom(float originX, float originY, float originZ,
                            float width, float depth, float height,
                            float wallThickness, uint32_t* outWallIds);

// rectBounds contains spaceCount groups of [minX,minY,maxX,maxY], local to origin.
// Returns the total number of unique walls created and copies up to outCapacity ids.
CAD_API uint32_t CAD_CreateFloorplan(float originX, float originY, float originZ,
                                     const float* rectBounds, uint32_t spaceCount,
                                     float height, float wallThickness,
                                     uint32_t* outWallIds, uint32_t outCapacity);

// type: 0=door, 1=window. roomBIndex >= 0 targets a shared wall;
// roomBIndex < 0 uses side (0=south, 1=north, 2=west, 3=east).
// alignment: 0=center, 1=start(west/south), 2=end(east/north).
typedef struct CAD_FloorplanOpeningDesc {
    int type;
    uint32_t roomAIndex;
    int32_t roomBIndex;
    int side;
    float width;
    float height;
    float sillHeight;
    int alignment;
    float offset;
} CAD_FloorplanOpeningDesc;

// Returns the number of solid wall pieces after openings are removed.
CAD_API uint32_t CAD_CreateFloorplanWithOpenings(
    float originX, float originY, float originZ,
    const float* rectBounds, uint32_t spaceCount,
    float height, float wallThickness,
    const CAD_FloorplanOpeningDesc* openings, uint32_t openingCount,
    uint32_t* outWallIds, uint32_t outCapacity);

// ── 평면도 이미지 → 벽 (AI 없이) ───────────────────────────────────────
// 추출은 장면을 바꾸지 않는다. widthMm = 도면 전체 폭(벽 중심선, mm), 0 이면 문 폭 900mm 로 축척 추정.
// 출력 JSON(mm, 좌하단 원점·Y 위): {"widthMm","depthMm","walls":[{"x1","y1","x2","y2","thicknessMm","exterior"}],
//   "outerThicknessMm","innerThicknessMm","scaleEstimated","doorCount","imageWidthMm","imageOrigin":[x,y],"summary"}
//   — imageWidthMm/imageOrigin = 이미지 **전체**의 실폭·좌하단(바닥에 깔 때). 실패 -1 + CAD_GetLastError. 2회 호출 규약.
CAD_API int  CAD_FloorplanExtractFromImage(const char* path, float widthMm, char* outJson, int cap);
// rgba = 4바이트 × w × h(행 우선, 위에서 아래) — 모바일 카메라·사진 선택기용.
CAD_API int  CAD_FloorplanExtractFromRgba(const unsigned char* rgba, int w, int h, float widthMm, char* outJson, int cap);
// 벽 그래프 → 3D 벽. segs = [x1,y1,x2,y2,thickness] × count, **단위 m**(CAD_CreateFloorplan 과 같음), 축에 나란한 벽만.
// thickness <= 0 이면 defaultThickness. 반환 = 만든 벽 수, outIds 에 최대 cap 개. undo 1.
CAD_API uint32_t CAD_CreateWallGraph(float ox, float oy, float oz, const float* segs, uint32_t count,
                                     float height, float defaultThickness, uint32_t* outIds, uint32_t cap);
// 편의 — 이미지에서 벽을 찾아 m 로 세우고, underlayImage 면 원본을 같은 축척으로 바닥에(AI create_wall_graph 와 같음).
CAD_API uint32_t CAD_CreateFloorplanFromImage(const char* path, float widthMm, float height, bool underlayImage,
                                              uint32_t* outIds, uint32_t cap);

#ifdef __cplusplus
}
#endif
