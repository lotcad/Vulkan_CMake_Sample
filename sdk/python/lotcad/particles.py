# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Particles 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_CreateParticleEmitter', 'CAD_CreateParticleEmitterFromPreset', 'CAD_SetParticlePlayback', 'CAD_GetParticleSettingsJson', 'CAD_SetParticleSettingsJson', 'CAD_GetParticleLiveCount', 'CAD_GetParticlePresetCount', 'CAD_GetParticlePresetName', 'CAD_GetParticlePresetPath', 'CAD_SaveParticlePreset']

_f = _n.native

_n.bind("CAD_CreateParticleEmitter", _c.c_uint32, [_c.c_int, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateParticleEmitterFromPreset", _c.c_uint32, [_c.c_char_p, _c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_SetParticlePlayback", _c.c_bool, [_c.c_uint32, _c.c_int])
_n.bind("CAD_GetParticleSettingsJson", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_SetParticleSettingsJson", _c.c_bool, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_GetParticleLiveCount", _c.c_uint32, [_c.c_uint32])
_n.bind("CAD_GetParticlePresetCount", _c.c_uint32, [])
_n.bind("CAD_GetParticlePresetName", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetParticlePresetPath", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_SaveParticlePreset", _c.c_bool, [_c.c_uint32, _c.c_char_p])


def CAD_CreateParticleEmitter(preset: int, x: float, y: float, z: float, unitsPerMeter: float) -> int:
    """C: uint32_t CAD_CreateParticleEmitter(int preset, float x, float y, float z, float unitsPerMeter)

    Particle presets: 0 fire, 1 smoke, 2 sparks. Inserted stopped.
    unitsPerMeter = 1 for metre drawings, 1000 for millimetre drawings.
    Call on the engine thread, outside CAD_Tick (same rule as CAD_CreateBox).
    """
    return _f.CAD_CreateParticleEmitter(preset, x, y, z, unitsPerMeter)


def CAD_CreateParticleEmitterFromPreset(path: str | None, x: float, y: float, z: float, unitsPerMeter: float) -> int:
    """C: uint32_t CAD_CreateParticleEmitterFromPreset(const char* path, float x, float y, float z, float unitsPerMeter)

    Load a LotCAD v1 JSON preset (not Unity/Unreal/Effekseer), create stopped.
    UTF-8 path. Invalid/unsupported file returns 0; never modifies the source file.
    """
    return _f.CAD_CreateParticleEmitterFromPreset(_n.text(path), x, y, z, unitsPerMeter)


def CAD_SetParticlePlayback(id: int, state: int) -> bool:
    """C: bool CAD_SetParticlePlayback(uint32_t id, int state)

    state: 0 pause (preserves particles), 1 play/resume, 2 reset/stop.
    """
    return _f.CAD_SetParticlePlayback(id, state)


def CAD_GetParticleSettingsJson(id: int) -> str | None:
    """C: int CAD_GetParticleSettingsJson(uint32_t id, char* out, int cap)

    Settings — JSON schema v1 of particle_preset_io.h (version, unit, style, rate, lifetime, speed, radius, spread,
    size, acceleration, start_color, end_color, capacity, seed). Get returns unit "m". Set accepts a partial object:
    only the given keys change (unit "mm" converts the given length keys). Undo 1 step. Fail: false + CAD_GetLastError.
    length, -1 = not an emitter
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetParticleSettingsJson(id, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_SetParticleSettingsJson(id: int, json: str | None) -> bool:
    """C: bool CAD_SetParticleSettingsJson(uint32_t id, const char* json)
    """
    return _f.CAD_SetParticleSettingsJson(id, _n.text(json))


def CAD_GetParticleLiveCount(id: int) -> int:
    """C: uint32_t CAD_GetParticleLiveCount(uint32_t id)

    0 = none / not an emitter
    """
    return _f.CAD_GetParticleLiveCount(id)


def CAD_GetParticlePresetCount() -> int:
    """C: uint32_t CAD_GetParticlePresetCount(void)

    Preset library — effects/*.json sorted by name, loaded on first use (no panel needed, works on iOS).
    Path is absolute UTF-8, ready for CAD_CreateParticleEmitterFromPreset. Effekseer files are not listed.
    """
    return _f.CAD_GetParticlePresetCount()


def CAD_GetParticlePresetName(index: int) -> str | None:
    """C: int CAD_GetParticlePresetName(uint32_t index, char* out, int cap)

    -1 = out of range
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetParticlePresetName(index, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetParticlePresetPath(index: int) -> str | None:
    """C: int CAD_GetParticlePresetPath(uint32_t index, char* out, int cap)

    -1 = out of range
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetParticlePresetPath(index, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_SaveParticlePreset(id: int, path: str | None) -> bool:
    """C: bool CAD_SaveParticlePreset(uint32_t id, const char* path)

    Save an emitter's settings as a v1 preset (UTF-8 path, folders created). Saving into effects/ refreshes the list.
    """
    return _f.CAD_SaveParticlePreset(id, _n.text(path))
