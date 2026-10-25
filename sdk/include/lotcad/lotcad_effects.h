#pragma once
/* LotCAD C API - effects  [(effects)]
 * Particle emitters and external effects.
 * 파티클 방출기·외부 효과.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"
#include "lotcad_geometry.h"   /* CAD_GeVec3 */

#ifdef __cplusplus
extern "C" {
#endif
/* 새 규칙: CAD_Status(실패 이유 = CAD_GetLastError) · 개수·글 함수 = int32_t 전체 개수·길이(실패면 음수 CAD_E_*), 칸은 uint32_t.
 * 좌표 = 월드. 엔진 스레드에서만, CAD_Tick 밖에서(CAD_CreateBox 와 같은 규칙). 만드는 함수는 되돌리기 1, 멈춘 채로 넣는다.
 * unitsPerMeter = 장면 1 m 가 몇 단위인가 — m 도면 1, mm 도면 1000(0 이하 = 1). 방출기가 아닌 id = CAD_E_WRONG_TYPE. */

enum {   /* 내장 프리셋 */
    CAD_PARTICLE_FIRE   = 0,
    CAD_PARTICLE_SMOKE  = 1,
    CAD_PARTICLE_SPARKS = 2
};
enum {   /* CAD_SetParticlePlayback */
    CAD_PARTICLE_PAUSE = 0,   /* 멈춤(입자 그대로) */
    CAD_PARTICLE_PLAY  = 1,   /* 재생·이어서 */
    CAD_PARTICLE_RESET = 2    /* 처음으로·멈춤 */
};
CAD_API CAD_Status CAD_CreateParticleEmitter(int32_t preset, CAD_GeVec3 position, double unitsPerMeter,
                                             const CAD_CreateOptions* opt, uint32_t* outId);
/* LotCAD v1 JSON 프리셋(Unity·Unreal·Effekseer 아님)으로. UTF-8 경로, 원본 파일은 안 바꾼다.
 * 파일 없음 = CAD_E_NOT_FOUND, 못 읽음 = CAD_E_FAILED */
CAD_API CAD_Status CAD_CreateParticleEmitterFromPreset(const char* path, CAD_GeVec3 position, double unitsPerMeter,
                                                       const CAD_CreateOptions* opt, uint32_t* outId);
/* Effekseer .efkefc/.efk(참조 자원 포함). CAD_SetParticlePlayback 으로 같이 다룬다. 파일은 .lot 에 담긴다.
 * Effekseer 없는 빌드·못 읽음 = CAD_E_FAILED + 이유 */
CAD_API CAD_Status CAD_CreateExternalEffect(const char* path, CAD_GeVec3 position, double unitsPerMeter,
                                            const CAD_CreateOptions* opt, uint32_t* outId);
CAD_API CAD_Status CAD_SetParticlePlayback(uint32_t id, int32_t state);   /* CAD_PARTICLE_PAUSE·PLAY·RESET */
/* 설정 — particle_preset_io.h 의 JSON v1(version, unit, style, rate, lifetime, speed, radius, spread, size, acceleration,
 * start_color, end_color, capacity, seed). Get 은 unit "m". Set 은 준 키만 바꾼다(unit "mm" 면 준 길이 키를 바꿔 읽음), 되돌리기 1.
 * 틀린 JSON·값 = CAD_E_INVALID_ARG + 이유 */
CAD_API int32_t    CAD_GetParticleSettingsJson(uint32_t id, char* buf, uint32_t capacity);
CAD_API CAD_Status CAD_SetParticleSettingsJson(uint32_t id, const char* json);
CAD_API int32_t    CAD_GetParticleLiveCount(uint32_t id);   /* 지금 살아 있는 입자 수 */
/* 프리셋 목록 — effects/*.json 이름 순, 처음 쓸 때 읽는다(패널 불필요, iOS 도). 경로 = 절대 UTF-8(CreateParticleEmitterFromPreset 에 그대로).
 * Effekseer 파일은 안 나온다. 번호 범위 밖 = CAD_E_OUT_OF_RANGE */
CAD_API int32_t    CAD_GetParticlePresetCount(void);
CAD_API int32_t    CAD_GetParticlePresetName(int32_t index, char* buf, uint32_t capacity);
CAD_API int32_t    CAD_GetParticlePresetPath(int32_t index, char* buf, uint32_t capacity);
/* 방출기 설정을 v1 프리셋으로 저장(UTF-8 경로, 폴더 만듦). effects/ 에 저장하면 목록도 다시 */
CAD_API CAD_Status CAD_SaveParticlePreset(uint32_t id, const char* path);

#ifdef __cplusplus
}
#endif
