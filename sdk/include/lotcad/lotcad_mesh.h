#pragma once
/* LotCAD C API - mesh  [(meshes / point clouds / volumes)]
 * Mesh creation and repair, point clouds, CT/MR volume meshes.
 * 메시 만들기·수리, 점군, CT/MR 볼륨 메시.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h.
 *
 * 좌표·길이 = 월드 mm. 예외 둘 — 객체가 통째로 들고 다니는 모양 데이터는 **객체 자기 좌표**이고 객체 변환이 그 위에 얹힌다:
 * CAD_ReplaceMesh 의 정점(플러그인이 자기 정의로 다시 만들어 끼움 — 사용자가 옮긴 자리는 그대로) · CAD_UpdatePointCloud 의 점(센서 좌표 —
 * 센서 자세는 객체 변환). 메시 대상 ids 가 NULL/0 개면 선택한 메시, 선택이 없으면 보이는 메시 전부. 고친 것은 되돌리기 한 단계. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif

/* 메시 객체 만들기 — points = 월드 좌표(pointCount ≥ 3), indices = 삼각형 세 개씩(indexCount 는 3 의 배수, 값 < pointCount),
 * normals = 점마다 법선(NULL = 삼각형마다 평평한 음영). 되돌리기 1. 플러그인 객체(lotcad_plugin.h 의 딱지)의 형상도 이것으로. */
CAD_API CAD_Status CAD_CreateMesh(const CAD_GeVec3* points, uint32_t pointCount, const uint32_t* indices, uint32_t indexCount,
                                  const CAD_GeVec3* normals, const CAD_CreateOptions* opt, uint32_t* outId);
/* 메시 형상 바꿔 끼우기 — points 는 **객체 자기 좌표**(지금 변환이 그 위에 얹힘 — 처음 CAD_CreateMesh 로 만든 객체는 만들 때 월드 = 자기 좌표).
 * 메시가 아니면 CAD_E_WRONG_TYPE, 잠긴 도면층 CAD_E_LOCKED. 피처 기록(B-Rep)은 사라진다. 되돌리기에 남기지 않는다(플러그인이 값을 바꿀 때마다
 * 다시 만드므로 — 정의 편집의 되돌리기는 플러그인 몫). */
CAD_API CAD_Status CAD_ReplaceMesh(uint32_t id, const CAD_GeVec3* points, uint32_t pointCount, const uint32_t* indices, uint32_t indexCount,
                                   const CAD_GeVec3* normals);

/* 볼륨(CT/MR: .nrrd/.nhdr/.nii/.nii.gz, 경로 UTF-8) → 등가면 메시 객체(이름 "파일@iso", 선택됨, 되돌리기 1).
 * iso = 값 문턱(NaN = 자동: CT 뼈 300, 그 밖은 값 범위 하위 15 %; CT 피부 ≈ -300), step = 복셀 건너뛰기 0(자동 — 600만 복셀↑ 2)·1~16.
 * 파일이 없으면 CAD_E_NOT_FOUND, 못 읽으면 CAD_E_FAILED + CAD_GetLastError. */
CAD_API CAD_Status CAD_CreateVolumeMesh(const char* path, double iso, int32_t step, const CAD_CreateOptions* opt, uint32_t* outId);
/* 의료 분할(라벨 볼륨: 정수 라벨 0..N 의 .nii/.nrrd, TotalSegmentator 등) → 라벨마다 색 메시 객체(해부 이름, 도면층 "분할:<파일>"), 되돌리기 1.
 * step 0 = 자동. 반환 = 만든 객체 수(라벨 수), outIds 에 그 id. outIds = NULL 이거나 칸이 모자라면 아무것도 안 만들고 개수만 —
 * 읽기·계산을 한 번 더 하게 되니(큰 볼륨은 수 초) 칸을 넉넉히(라벨 수 ≤ 255 가 보통) 주는 게 좋다. */
CAD_API int32_t CAD_CreateLabelMeshes(const char* path, int32_t step, uint32_t* outIds, uint32_t capacity);

/* ── 점군 (라이다 / 스캐너) ──
 * 만들기와 갱신이 나뉘어 있다. 센서는 초당 수십 번 갱신하는데, 그때마다 지웠다 만들면 id 가 바뀌어 선택·변환이 매번 풀린다.
 * 한 번 만들고 계속 Update 한다:
 *
 *   uint32_t pc = 0; CAD_CreatePointCloud(NULL, &pc);
 *   // 매 스캔마다
 *   CAD_UpdatePointCloud(pc, xyz, rgba, count);
 *
 * xyz  : 3 × count 개의 float(x,y,z 반복) — **객체 자기 좌표**(센서 좌표). 센서 위치·자세는 객체 변환으로 따로(CAD_SetTransform).
 *        점을 미리 월드로 바꾸지 말 것(그러면 매 프레임 count 개를 CPU 에서 곱한다). 대량 흐름이라 double 이 아니라 float.
 * rgba : 4 × count 개의 uint8. NULL 이면 객체 색으로 단색(LaserScan 처럼 색이 없는 소스).
 * count: 점 개수. 0 이면 비운다.
 * ⚠️ 규모 전제: 수만~수십만 점. 수백만 점(측량 스캔)은 옥트리 LOD 가 있어야 하고 그건 이 위에 얹을 층이다 — 함수 모양은 그대로.
 * 갱신은 GPU 대기 없이 호스트 보이는 버퍼에 복사(매 프레임 불러도 된다), 되돌리기에 남기지 않는다. */
CAD_API CAD_Status CAD_CreatePointCloud(const CAD_CreateOptions* opt, uint32_t* outId);
CAD_API CAD_Status CAD_UpdatePointCloud(uint32_t id, const float* xyz, const uint8_t* rgba, uint32_t count);
/* 화면 점 크기(픽셀) 1~64, 기본 2. 범위 밖은 CAD_E_INVALID_ARG. */
CAD_API CAD_Status CAD_SetPointCloudSize(uint32_t id, double pointSizePx);
/* 점 개수(음수 = 오류: 없는 id, 점군이 아님). */
CAD_API int32_t    CAD_GetPointCloudCount(uint32_t id);

/* ── 메시 검사·수리 ── */
/* 메시 검사 — volume·area 는 월드(mm³·mm², 객체 변환을 얹은 모양). ok = 닫힘·바깥향·결함 없음. 메시가 아니면 CAD_E_WRONG_TYPE. */
typedef struct CAD_MeshCheckInfo {
    uint32_t size;                 /* = sizeof(CAD_MeshCheckInfo) */
    uint32_t triangles, vertices;  /* 삼각형 수 · 같은 자리를 붙인 뒤 정점 수 */
    uint32_t degenerate, duplicates;
    uint32_t openEdges, nonManifoldEdges, flippedEdges, holes, components;
    bool     closed, ok;
    double   volume, area;         /* 부호 부피(닫혔을 때만 뜻 — 음수 = 안팎 뒤집힘) · 겉넓이 */
} CAD_MeshCheckInfo;
CAD_API CAD_Status CAD_CheckMesh(uint32_t id, CAD_MeshCheckInfo* out);

/* 수리 선택 — NULL = 구멍 메움(둘레 곡면을 따라 둥글게). */
typedef struct CAD_MeshRepairOptions {
    uint32_t size;       /* = sizeof(CAD_MeshRepairOptions) */
    bool     noFill;     /* true = 구멍은 메우지 않음 */
    bool     flatFill;   /* true = 구멍을 평평하게(기본은 둥글게) */
} CAD_MeshRepairOptions;

/* 아래 여섯은 반환 = 바꾼 메시 수(0 = 고칠 것 없음 — 오류 아님), 음수 = 오류. ids 를 주면 하나라도 없거나(CAD_E_BAD_HANDLE)·잠겼거나(CAD_E_LOCKED)·
 * 메시가 아니면(B-Rep 솔리드 포함, CAD_E_WRONG_TYPE) 아무것도 안 바꾼다. 여럿이어도 되돌리기 1. */
/* 수리 — 같은 자리 정점 붙이기 → 퇴화·중복 제거 → 방향 통일(닫힌 것은 바깥향) → 구멍 메움. 멀쩡한 메시는 건드리지 않는다. */
CAD_API int32_t CAD_RepairMeshes(const uint32_t* ids, uint32_t count, const CAD_MeshRepairOptions* opt);
/* 매끈하게(토빈 — 부피가 거의 안 준다, 열린 가장자리 고정, 모서리는 둥글어진다). iterations 1~500. */
CAD_API int32_t CAD_SmoothMeshes(const uint32_t* ids, uint32_t count, int32_t iterations);
/* 삼각형 줄이기(QEM) — ratio = 남길 비율(0 과 1 사이). 경계 윤곽은 거의 그대로. 더 못 줄이는 메시는 건너뜀. */
CAD_API int32_t CAD_DecimateMeshes(const uint32_t* ids, uint32_t count, double ratio);
/* 틈 꿰매기 — tolerance(월드 mm, 0 = 자동: 대각선의 0.1 %) 안의 경계 점을 붙이고 T 이음을 쪼개 잇는다. 이미 닫힌 메시는 건너뜀.
 * 축마다 축척이 다른 객체에 tolerance > 0 이면 CAD_E_NOT_SUPPORTED(거리가 방향마다 달라져서). */
CAD_API int32_t CAD_StitchMeshes(const uint32_t* ids, uint32_t count, double tolerance);
/* 두께 주기 — 열린 메시를 법선 쪽으로 thickness(월드 mm, 음수 = 반대쪽, 0 은 거부)만큼 → 닫힌 솔리드. 닫힌 메시는 건너뜀(셸은 CAD_Shell).
 * 축마다 축척이 다른 객체는 CAD_E_NOT_SUPPORTED. */
CAD_API int32_t CAD_ThickenMeshes(const uint32_t* ids, uint32_t count, double thickness);
/* 다시 나누기(등방 리메시) — edgeLength = 목표 모서리 길이(월드 mm, 0 = 지금 평균). 경계·날카로운 모서리(45°↑)는 그대로.
 * 축마다 축척이 다른 객체에 edgeLength > 0 이면 CAD_E_NOT_SUPPORTED. */
CAD_API int32_t CAD_RemeshMeshes(const uint32_t* ids, uint32_t count, double edgeLength);

#ifdef __cplusplus
}
#endif
