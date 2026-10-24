#pragma once
/* LotCAD C API - robot  [(robotics)]
 * URDF robots, joints, runtime rigging.
 * URDF 로봇·관절·런타임 리깅.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif
// ── 관절 로봇 (URDF) ──
// URDF 는 ROS 의 로봇 정의 포맷이지만 파일 자체는 XML 이라 **ROS 없이도** 읽고 그린다.
// 좌표계도 맞는다 — URDF 와 이 엔진 둘 다 Z-up 우수좌표계·미터라 축 변환이 없다.
//
//   uint32_t r = CAD_LoadUrdf("models/demo_arm.urdf");   // 0 = 실패, 아니면 로봇 인덱스+1
//   CAD_SetJointValue(r, CAD_FindJoint(r, "joint_elbow"), 0.7f);   // 라디안
//
// 조인트는 1자유도다 — URDF <axis> 가 축이고 값은 그 축의 회전각(revolute, 라디안)
// 또는 이동거리(prismatic, 미터). 한계가 있으면 엔진이 잘라 넣는다.
//
// 로봇 핸들은 **1부터** — 0 을 실패로 쓰기 위해서다. 내부 인덱스 = handle-1.
// 지원 형상: box / cylinder / sphere. mesh(STL/DAE) 링크는 아직 건너뛴다.
CAD_API uint32_t CAD_LoadUrdf(const char* path);
CAD_API uint32_t CAD_GetRobotCount(void);
CAD_API uint32_t CAD_GetJointCount(uint32_t robot);
// 조인트 이름 → 인덱스. 없으면 -1. (ROS 는 이름으로 오므로 필요)
CAD_API int      CAD_FindJoint(uint32_t robot, const char* jointName);
CAD_API int      CAD_GetJointName(uint32_t robot, int jointIdx, char* outUtf8, int cap);
// 값 대입/조회. 반환은 한계로 잘린 **실제 적용값**.
CAD_API float    CAD_SetJointValue(uint32_t robot, int jointIdx, float value);
CAD_API float    CAD_GetJointValue(uint32_t robot, int jointIdx);
// ── 여러 관절을 한 번에 ──
// ROS 의 sensor_msgs/JointState 는 관절 전부를 한 메시지에 담아 초당 수십 번 보낸다.
// 하나씩 넣으면 관절 수만큼 계층 트리를 다시 푸느라 헛일을 한다 — 여기선 **마지막에 한 번만** 푼다.
// 반환: 실제로 적용된 개수(범위 밖·고정 조인트는 건너뜀).
CAD_API uint32_t CAD_SetJointValues(uint32_t robot, const int* jointIdx,
                                    const float* values, uint32_t count);
// 이름으로 받는 판 — ROS 는 인덱스가 아니라 이름으로 온다. JointState 콜백에 그대로 꽂힌다.
//   CAD_SetJointValuesByName(r, msg.name.data(), msg.position.data(), msg.name.size());
CAD_API uint32_t CAD_SetJointValuesByName(uint32_t robot, const char* const* names,
                                          const float* values, uint32_t count);
// 한계와 종류(0=fixed 1=revolute 2=continuous 3=prismatic). hasLimit=false 면 lower/upper 무의미.
CAD_API bool     CAD_GetJointInfo(uint32_t robot, int jointIdx,
                                  int* outType, float* outLower, float* outUpper, bool* outHasLimit);
// 축/종류 지정 — 엔진 안에서 리깅 (URDF 로 읽은 값을 바꿔 보기).
// 축은 길이 0 이면 무시하고 false. 내부에서 정규화한다.
CAD_API bool     CAD_SetJointAxis(uint32_t robot, int jointIdx, float x, float y, float z);
CAD_API bool     CAD_GetJointAxis(uint32_t robot, int jointIdx, float* x, float* y, float* z);
// type: 0=fixed 1=revolute 2=continuous 3=prismatic.
// 종류가 바뀌면 한계는 버린다 — 각도(라디안)와 길이(미터)는 단위가 달라 그대로 쓰면 위험하다.
CAD_API bool     CAD_SetJointType(uint32_t robot, int jointIdx, int type);
// 축의 **위치**(피벗). 부모 링크 좌표 기준. 방향만으로는 어디를 중심으로 도는지 못 정한다.
CAD_API bool     CAD_SetJointOrigin(uint32_t robot, int jointIdx, float x, float y, float z);
CAD_API bool     CAD_GetJointOrigin(uint32_t robot, int jointIdx, float* x, float* y, float* z);
// 링크 이름 → 그 링크의 씬 객체 ID (형상 없는 링크는 0). 색/재질 변경 등에 사용.
CAD_API uint32_t CAD_GetLinkObject(uint32_t robot, const char* linkName);
// 씬에서 로봇 전부 제거.
CAD_API void     CAD_ClearRobots(void);

// ── 런타임 리깅 — URDF 없이 씬 객체를 부모-자식으로 붙이기 ──
// "큐브 9개로 로봇 만들기". 붙여도 부품은 제자리에 그대로 있는다(월드 변환을 계층으로 옮김).
// type: 0=고정 1=회전 2=연속회전 3=직선. axis 는 붙일 때의 축 방향.
// pivot(월드) = 축의 **위치**. usePivot=false 면 자식이 있는 자리를 쓴다.
// 회전 중심이 부품 중심이라는 법이 없다 — 문 경첩은 모서리에 있다.
CAD_API bool     CAD_RigAttach(uint32_t parentObj, uint32_t childObj,
                               float axisX, float axisY, float axisZ, int type,
                               float pivotX, float pivotY, float pivotZ, bool usePivot);
// 이 부품과 그 **아래 가지 전체**를 떼어낸다. 각자 보이는 자리를 유지한다.
CAD_API bool     CAD_RigDetach(uint32_t obj);
// 이 객체가 속한 로봇 핸들 (0 = 안 붙어 있음).
CAD_API uint32_t CAD_GetObjectRobot(uint32_t obj);

#ifdef __cplusplus
}
#endif
