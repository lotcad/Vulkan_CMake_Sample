#pragma once
/* LotCAD C API - robot  [(robotics)]
 * URDF robots, joints, runtime rigging.
 * URDF 로봇·관절·런타임 리깅.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"
#include "lotcad_geometry.h"   /* CAD_GeVec3 */

#ifdef __cplusplus
extern "C" {
#endif
/* 새 규칙: CAD_Status(실패 이유 = CAD_GetLastError) · 개수·글 함수 = int32_t 전체 개수·길이(실패면 음수 CAD_E_*), 칸은 uint32_t.
 * 좌표 = 월드(관절 축의 자리·방향도 월드 — 엔진 안은 부모 링크 기준이라 API 가 바꿔 준다). 엔진 스레드에서만.
 * 로봇 핸들은 1부터(없는 핸들 = CAD_E_BAD_HANDLE), 관절 번호는 0부터(범위 밖 = CAD_E_OUT_OF_RANGE). */

// ── 관절 로봇 (URDF) ──
// URDF 는 ROS 의 로봇 정의 포맷이지만 파일 자체는 XML 이라 **ROS 없이도** 읽고 그린다.
// 좌표계도 맞는다 — URDF 와 이 엔진 둘 다 Z-up 우수좌표계·미터라 축 변환이 없다.
//
//   uint32_t r = 0; int32_t elbow = -1;
//   CAD_LoadUrdf("models/demo_arm.urdf", &r);
//   CAD_FindJoint(r, "joint_elbow", &elbow);
//   CAD_SetJointValue(r, elbow, 0.7, NULL);   // 라디안
//
// 조인트는 1자유도다 — URDF <axis> 가 축이고 값은 그 축의 회전각(revolute, 라디안)
// 또는 이동거리(prismatic, 장면 단위 = URDF 의 미터). 한계가 있으면 엔진이 잘라 넣는다.
// 지원 형상: box / cylinder / sphere. mesh(STL/DAE) 링크는 아직 건너뛴다.
enum {   /* 관절 종류 */
    CAD_JOINT_FIXED      = 0,
    CAD_JOINT_REVOLUTE   = 1,
    CAD_JOINT_CONTINUOUS = 2,
    CAD_JOINT_PRISMATIC  = 3
};
/* 파일 없음 = CAD_E_NOT_FOUND, 못 읽음 = CAD_E_FAILED + 이유 */
CAD_API CAD_Status CAD_LoadUrdf(const char* path, uint32_t* outRobot);
CAD_API int32_t    CAD_GetRobotCount(void);
CAD_API int32_t    CAD_GetJointCount(uint32_t robot);
/* 조인트 이름 → 번호(ROS 는 이름으로 온다). 없음 = CAD_E_NOT_FOUND(*outJoint = -1) */
CAD_API CAD_Status CAD_FindJoint(uint32_t robot, const char* jointName, int32_t* outJoint);
CAD_API int32_t    CAD_GetJointName(uint32_t robot, int32_t joint, char* buf, uint32_t capacity);
/* 값 대입/조회 — outApplied = 한계로 잘린 **실제 적용값**(NULL 가능) */
CAD_API CAD_Status CAD_SetJointValue(uint32_t robot, int32_t joint, double value, double* outApplied);
CAD_API CAD_Status CAD_GetJointValue(uint32_t robot, int32_t joint, double* outValue);
// ── 여러 관절을 한 번에 ──
// ROS 의 sensor_msgs/JointState 는 관절 전부를 한 메시지에 담아 초당 수십 번 보낸다.
// 하나씩 넣으면 관절 수만큼 계층 트리를 다시 푸느라 헛일을 한다 — 여기선 **마지막에 한 번만** 푼다.
// 반환: 실제로 적용된 개수(범위 밖·고정 조인트는 건너뜀).
CAD_API int32_t    CAD_SetJointValues(uint32_t robot, const int32_t* joints, const double* values, uint32_t count);
// 이름으로 받는 판 — JointState 콜백에 그대로 꽂힌다(position 은 double 이라 복사 없이).
//   CAD_SetJointValuesByName(r, names, msg.position.data(), count);
CAD_API int32_t    CAD_SetJointValuesByName(uint32_t robot, const char* const* names, const double* values, uint32_t count);
/* 관절 정보 — 부르는 쪽이 out->size = sizeof(CAD_JointInfo). 새 칸은 끝에만 */
typedef struct CAD_JointInfo {
    uint32_t   size;
    int32_t    type;       /* CAD_JOINT_* */
    bool       hasLimit;   /* 거짓이면 lower·upper 무의미 */
    double     lower, upper;
    double     value;      /* 지금 값 */
    CAD_GeVec3 origin;     /* 축의 자리(월드, 관절 값 0 일 때 — 회전 관절은 늘 같은 자리) */
    CAD_GeVec3 axis;       /* 축 방향(월드, 단위) */
} CAD_JointInfo;
CAD_API CAD_Status CAD_GetJointInfo(uint32_t robot, int32_t joint, CAD_JointInfo* out);
/* 축 방향(월드) — 엔진 안에서 리깅(URDF 로 읽은 값을 바꿔 보기). 길이 0 = CAD_E_DEGENERATE. 내부에서 정규화 */
CAD_API CAD_Status CAD_SetJointAxis(uint32_t robot, int32_t joint, CAD_GeVec3 axis);
/* 종류 — CAD_JOINT_*. 종류가 바뀌면 한계는 버린다(각도와 길이는 단위가 달라 그대로 쓰면 위험) */
CAD_API CAD_Status CAD_SetJointType(uint32_t robot, int32_t joint, int32_t type);
/* 축의 **자리**(피벗, 월드 — 관절 값 0 기준). 방향만으로는 어디를 중심으로 도는지 못 정한다. 부품은 제자리 */
CAD_API CAD_Status CAD_SetJointOrigin(uint32_t robot, int32_t joint, CAD_GeVec3 position);
/* 링크 이름 → 그 링크의 씬 객체 id(형상 없는 링크는 0). 없는 이름 = CAD_E_NOT_FOUND */
CAD_API CAD_Status CAD_GetLinkObject(uint32_t robot, const char* linkName, uint32_t* outId);
CAD_API CAD_Status CAD_ClearRobots(void);   /* 씬에서 로봇 전부 제거 */

// ── 런타임 리깅 — URDF 없이 씬 객체를 부모-자식으로 붙이기 ──
// "큐브 9개로 로봇 만들기". 붙여도 부품은 제자리에 그대로 있는다(월드 변환을 계층으로 옮김).
// type = CAD_JOINT_*, axis = 붙일 때의 축 방향(월드, 고정이 아니면 길이 0 = CAD_E_DEGENERATE).
// pivot(월드) = 축의 **자리**, NULL 이면 자식이 있는 자리 — 회전 중심이 부품 중심이라는 법이 없다(문 경첩은 모서리에 있다).
// 이미 다른 로봇에 붙어 있음·고리가 생김 = CAD_E_FAILED + 이유
CAD_API CAD_Status CAD_RigAttach(uint32_t parentObj, uint32_t childObj, CAD_GeVec3 axis, int32_t type, const CAD_GeVec3* pivot);
/* 이 부품과 그 **아래 가지 전체**를 떼어낸다(각자 보이는 자리 유지). 안 붙어 있음 = CAD_E_NOT_FOUND */
CAD_API CAD_Status CAD_RigDetach(uint32_t obj);
/* 이 객체가 속한 로봇 핸들(안 붙어 있으면 0, CAD_OK) */
CAD_API CAD_Status CAD_GetObjectRobot(uint32_t obj, uint32_t* outRobot);

#ifdef __cplusplus
}
#endif
