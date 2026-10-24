#pragma once
/* LotCAD C API - effects  [(effects)]
 * Particle emitters and external effects.
 * 파티클 방출기·외부 효과.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif
// Particle presets: 0 fire, 1 smoke, 2 sparks. Inserted stopped.
// unitsPerMeter = 1 for metre drawings, 1000 for millimetre drawings.
// Call on the engine thread, outside CAD_Tick (same rule as CAD_CreateBox).
CAD_API uint32_t CAD_CreateParticleEmitter(int preset, float x, float y, float z, float unitsPerMeter);
// Load a LotCAD v1 JSON preset (not Unity/Unreal/Effekseer), create stopped.
// UTF-8 path. Invalid/unsupported file returns 0; never modifies the source file.
CAD_API uint32_t CAD_CreateParticleEmitterFromPreset(const char* path, float x, float y, float z, float unitsPerMeter);
// state: 0 pause (preserves particles), 1 play/resume, 2 reset/stop.
CAD_API bool CAD_SetParticlePlayback(uint32_t id, int state);
// Settings — JSON schema v1 of particle_preset_io.h (version, unit, style, rate, lifetime, speed, radius, spread,
// size, acceleration, start_color, end_color, capacity, seed). Get returns unit "m". Set accepts a partial object:
// only the given keys change (unit "mm" converts the given length keys). Undo 1 step. Fail: false + CAD_GetLastError.
CAD_API int      CAD_GetParticleSettingsJson(uint32_t id, char* out, int cap);   // length, -1 = not an emitter
CAD_API bool     CAD_SetParticleSettingsJson(uint32_t id, const char* json);
CAD_API uint32_t CAD_GetParticleLiveCount(uint32_t id);                          // 0 = none / not an emitter
// Preset library — effects/*.json sorted by name, loaded on first use (no panel needed, works on iOS).
// Path is absolute UTF-8, ready for CAD_CreateParticleEmitterFromPreset. Effekseer files are not listed.
CAD_API uint32_t CAD_GetParticlePresetCount(void);
CAD_API int      CAD_GetParticlePresetName(uint32_t index, char* out, int cap);  // -1 = out of range
CAD_API int      CAD_GetParticlePresetPath(uint32_t index, char* out, int cap);  // -1 = out of range
// Save an emitter's settings as a v1 preset (UTF-8 path, folders created). Saving into effects/ refreshes the list.
CAD_API bool     CAD_SaveParticlePreset(uint32_t id, const char* path);

// Load an Effekseer .efkefc/.efk with referenced resources. Inserted stopped.
// CAD_SetParticlePlayback also controls these objects. Files embed in .lot.
CAD_API uint32_t CAD_CreateExternalEffect(const char* path,float x,float y,float z,float unitsPerMeter);

#ifdef __cplusplus
}
#endif
