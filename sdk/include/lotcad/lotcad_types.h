#pragma once
/* LotCAD C API - common types and rules (every lotcad_*.h includes this).
 *
 * Boundary rules (C ABI — usable from C, C++, C#, Python, Swift, Kotlin):
 * - Only C-friendly types: bool, int, uint32_t, float, double, const char* (UTF-8), void* handles, plain structs.
 * - No C++/STL/GLM/GLFW/Vulkan types, no internal object pointers. Objects are uint32_t ids (0 = none / failure).
 * - Mutating functions run on the engine thread (the thread that calls CAD_Tick).
 *
 * C API 경계 규칙: C 친화 타입만(UTF-8 문자열, id = uint32_t, 0 = 없음/실패), 엔진 내부 형식·포인터는 내보내지 않는다.
 * 장면을 바꾸는 함수는 엔진 스레드(CAD_Tick 을 부르는 스레드)에서만.
 */

#include <stdint.h>

#ifndef __cplusplus
#include <stdbool.h>
#endif

/* Result code — functions return this (areas still on the old rule are being moved over, see docs/API_RULES.md). 0 = success, negative = why it failed.
 * The human text is in CAD_GetLastError, translated to the UI language, so programs branch on the CODE, never the text.
 * Functions that return a count use int32_t: >= 0 = the full count, < 0 = one of these codes.
 * 결과 코드 — 0 = 성공, 음수 = 실패 이유. 사람이 읽을 글(CAD_GetLastError)은 화면 언어로 번역되니 프로그램은 코드로 가른다.
 * 개수를 돌려주는 함수는 int32_t: 0 이상 = 전체 개수, 음수 = 이 코드. 값은 늘 출력 인자로(필요 없는 출력은 NULL). */
typedef int32_t CAD_Status;
enum {
    CAD_OK                  = 0,
    CAD_E_INVALID_ARG       = -1,    /* 값이 맞지 않음(NULL 입력, 숫자 아님, 범위 밖 설정값 …) */
    CAD_E_BAD_HANDLE        = -2,    /* 없는 핸들·id(만들지 않았거나 이미 지움) */
    CAD_E_NO_ENGINE         = -3,    /* 엔진이 없음(CAD_Init 전) — 장면 함수 */
    CAD_E_WRONG_TYPE        = -4,    /* 그 종류가 아님(호가 아닌 곡선에 호 읽기 …) */
    CAD_E_DEGENERATE        = -5,    /* 길이·넓이가 0 인 입력 */
    CAD_E_PARALLEL          = -6,    /* 나란해서(한 줄이라서) 하나로 정해지지 않음 */
    CAD_E_NOT_PLANAR        = -7,    /* 평면 곡선이 아님 / 그 평면에 있지 않음 */
    CAD_E_NOT_CLOSED        = -8,    /* 닫힌 곡선이어야 함 */
    CAD_E_NOT_ON_CURVE      = -9,    /* 점이 곡선(또는 그 연장) 위가 아님 */
    CAD_E_OUT_OF_RANGE      = -10,   /* 매개변수·번호가 범위 밖 */
    CAD_E_NOT_SUPPORTED     = -11,   /* 이 종류는 아직 안 됨 */
    CAD_E_FAILED            = -12,   /* 계산이 맞지 않음(수렴 안 함 …) */
    CAD_E_BUFFER_TOO_SMALL  = -13,   /* 한꺼번에 채워야 하는 출력의 칸이 모자람(개수 함수는 이 코드 대신 개수를 돌려준다) */
    CAD_E_NOT_CONNECTED     = -14,   /* 이어 붙일 곡선들이 끝 → 시작으로 이어지지 않음 */
    CAD_E_WRONG_THREAD      = -15,   /* 엔진 스레드에서만 부르는 함수를 다른 스레드에서 부름 */
    CAD_E_LOCKED            = -16,   /* 잠긴 도면층의 객체라 바꿀 수 없음 */
    CAD_E_BUSY              = -17,   /* 일이 도는 중이라 지금은 못 바꿈(해석 풀이 중 …) — 끝나거나 멈춘 뒤 다시 */
    CAD_E_NOT_READY         = -18,   /* 아직 준비되지 않음(해석 대상을 안 열었음·결과가 아직 없음 …) */
    CAD_E_NOT_FOUND         = -19,   /* 찾는 것이 없음(그 이름의 객체·재질 …) — 없는 id 는 CAD_E_BAD_HANDLE */
    CAD_E_DUPLICATE         = -20,   /* 이미 있는 이름(객체 이름은 장면 안에서 하나 …) */
    CAD_E_CONFLICT          = -21    /* 조건끼리 부딪쳐 풀 수 없음(스케치 제약 …) — 아무것도 안 바뀜, 부딪친 것은 함수 설명의 읽기 함수로 */
};

/* 색 — r, g, b 는 0..1(1 = 가장 밝음) */
typedef struct CAD_Color { double r, g, b; } CAD_Color;

#if defined(_WIN32)
    #if defined(LOTCAD_API_STATIC)
        #define CAD_API
    #elif defined(LOTCAD_API_EXPORTS)
        #define CAD_API __declspec(dllexport)
    #else
        #define CAD_API __declspec(dllimport)
    #endif
#else
    #define CAD_API __attribute__((visibility("default")))
#endif
