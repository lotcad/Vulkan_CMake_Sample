#pragma once
/* LotCAD C API - mesh  [(meshes / point clouds / volumes)]
 * Mesh creation and repair, point clouds, CT/MR volume meshes.
 * 메시 만들기·수리, 점군, CT/MR 볼륨 메시.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif
/* 메시 객체 만들기·형상 바꿔 끼우기 — 플러그인 객체(lotcad_plugin.h 의 딱지)의 형상도 이것으로.
 * xyz = 3*vertexCount, indices = 3*triangleCount. normals 는 NULL 가능(삼각형별 flat). */
CAD_API uint32_t CAD_CreateMesh(const float* xyz, unsigned int vertexCount,
                                const unsigned int* indices, unsigned int indexCount,
                                const float* normals);
CAD_API bool CAD_ReplaceMesh(uint32_t id, const float* xyz, unsigned int vertexCount,
                             const unsigned int* indices, unsigned int indexCount,
                             const float* normals);

/* 볼륨(CT/MR: .nrrd/.nhdr/.nii/.nii.gz) → 등가면 메시 객체. iso 는 값 문턱(NaN 이면 범위 중간, CT 뼈 ≈ 300, 피부 ≈ -300),
 * step 은 복셀 건너뛰기(1=전부, 2=삼각형 1/4). 보통 mesh 객체(이름 "파일@iso")를 만들고 선택까지. 반환 id, 실패 0 + CAD_GetLastError. */
CAD_API uint32_t CAD_CreateVolumeMesh(const char* path, float iso, int step);
/* 의료 분할(라벨 볼륨: 정수 라벨 0..N 의 .nii/.nrrd, TotalSegmentator 등) → 라벨마다 색 메시 객체(해부 이름, 도면층 "분할:<파일>").
 * step 0=자동. 반환 = 만든 객체 수, 실패 0 + CAD_GetLastError. 트랜잭션 한 단계. */
CAD_API uint32_t CAD_CreateLabelMeshes(const char* path, int step);

// ── 점군 (라이다 / 스캐너) ──
// 생성과 갱신이 분리돼 있다. 센서는 초당 수십 번 갱신하는데, 그때마다 객체를 지웠다
// 만들면 ID 가 바뀌어 선택·트랜스폼이 매번 풀린다. 한 번 만들고 계속 Update 한다.
//
//   uint32_t pc = CAD_CreatePointCloud();
//   // 매 스캔마다
//   CAD_UpdatePointCloud(pc, xyz, rgba, count);
//
// xyz  : 3 × count 개의 float (x,y,z 반복). 객체 로컬 좌표 — 센서 위치/자세는
//        CAD_SetTransform 으로 따로 준다(점을 미리 변환하지 말 것. 그러면 매 프레임
//        count 개를 CPU 에서 곱해야 한다).
// rgba : 4 × count 개의 uint8. NULL 이면 객체 색으로 단색 표시(LaserScan 처럼 색이 없는 소스).
// count: 점 개수. 0 이면 비운다.
//
// ⚠️ 규모 전제: **수만~수십만 점**. 수백만 점(측량 스캔)은 옥트리 LOD 가 있어야 하고,
//    그건 이 API 위에 얹을 별도 레이어다 — 함수 모양은 그때도 바뀌지 않는다.
// 갱신은 GPU 스톨 없이 host-visible 버퍼 memcpy 로 처리된다(매 프레임 호출해도 안전).
CAD_API uint32_t CAD_CreatePointCloud(void);

CAD_API bool     CAD_UpdatePointCloud(uint32_t id,
                                      const float* xyz,
                                      const unsigned char* rgba,
                                      uint32_t count);
// 화면 픽셀 크기 (1~64 로 클램프). 기본 2.
CAD_API bool     CAD_SetPointCloudSize(uint32_t id, float pointSizePx);
CAD_API uint32_t CAD_GetPointCloudCount(uint32_t id);

/* 메시 검사 — 모델 로컬 단위. ok = 닫힘·바깥향·결함 없음. 메시가 아니면 false. */
typedef struct CAD_MeshCheckInfo {
    uint32_t triangles, vertices, degenerate, duplicates;
    uint32_t openEdges, nonManifoldEdges, flippedEdges, holes, components;
    bool closed, ok;
    double volume, area;
} CAD_MeshCheckInfo;
CAD_API bool     CAD_CheckMesh(uint32_t id, CAD_MeshCheckInfo* out);
/* 메시 수리 — ids 의 메시(null 이면 보이는 메시 전부)를 붙이기·퇴화/중복 제거·방향 통일·구멍 메움. 반환 = 고친 객체 수. */
CAD_API uint32_t CAD_RepairMeshes(const uint32_t* ids, uint32_t count, bool fillHoles);
// 구멍 메우기 방식 지정판 — curvedFill: 둘레 곡면을 따라 둥글게(CAD_RepairMeshes 기본) / false = 평평하게.
CAD_API uint32_t CAD_RepairMeshesEx(const uint32_t* ids, uint32_t count, bool fillHoles, bool curvedFill);
// 메시 매끈하게(토빈 — 부피가 거의 안 준다, 모서리는 둥글어진다). ids 가 비면 선택 메시(없으면 보이는 메시 전부). undo 1. 반환: 바꾼 개수.
CAD_API uint32_t CAD_SmoothMeshes(const uint32_t* ids, uint32_t count, int iterations);
// 삼각형 줄이기(QEM) — ratio = 남길 비율(0~1 사이). 경계 윤곽은 거의 그대로. undo 1. 반환: 바꾼 개수(0 = 대상 없음/범위 밖).
CAD_API uint32_t CAD_DecimateMeshes(const uint32_t* ids, uint32_t count, double ratio);
// 틈 꿰매기 — tolerance(모델 로컬 단위) 안의 경계 점을 붙이고 T 이음을 쪼개 잇는다. 0 = 자동(대각선의 0.1%). 이미 닫힌 메시는 건너뜀.
CAD_API uint32_t CAD_StitchMeshes(const uint32_t* ids, uint32_t count, float tolerance);
// 두께 주기 — 열린 메시를 법선 방향으로 thickness 만큼 두껍게 해 닫힌 솔리드로(음수 = 반대쪽, 0 은 거부). 닫힌 메시는 건너뜀.
CAD_API uint32_t CAD_ThickenMeshes(const uint32_t* ids, uint32_t count, double thickness);
// 다시 나누기(등방 리메시) — edgeLength = 목표 모서리 길이(0 = 지금 평균). 경계·날카로운 모서리(45°↑)는 그대로.
CAD_API uint32_t CAD_RemeshMeshes(const uint32_t* ids, uint32_t count, double edgeLength);

#ifdef __cplusplus
}
#endif
