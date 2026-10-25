# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Effects 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_PARTICLE_FIRE', 'CAD_PARTICLE_SMOKE', 'CAD_PARTICLE_SPARKS', 'CAD_PARTICLE_PAUSE', 'CAD_PARTICLE_PLAY', 'CAD_PARTICLE_RESET', 'CAD_CreateParticleEmitter', 'CAD_CreateParticleEmitterFromPreset', 'CAD_CreateExternalEffect', 'CAD_SetParticlePlayback', 'CAD_GetParticleSettingsJson', 'CAD_SetParticleSettingsJson', 'CAD_GetParticleLiveCount', 'CAD_GetParticlePresetCount', 'CAD_GetParticlePresetName', 'CAD_GetParticlePresetPath', 'CAD_SaveParticlePreset']

_f = _n.native

CAD_PARTICLE_FIRE = 0
CAD_PARTICLE_SMOKE = 1
CAD_PARTICLE_SPARKS = 2
CAD_PARTICLE_PAUSE = 0
CAD_PARTICLE_PLAY = 1
CAD_PARTICLE_RESET = 2

_n.bind("CAD_CreateParticleEmitter", _c.c_int32, [_c.c_int32, CAD_GeVec3, _c.c_double, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateParticleEmitterFromPreset", _c.c_int32, [_c.c_char_p, CAD_GeVec3, _c.c_double, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_CreateExternalEffect", _c.c_int32, [_c.c_char_p, CAD_GeVec3, _c.c_double, _c.POINTER(CAD_CreateOptions), _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetParticlePlayback", _c.c_int32, [_c.c_uint32, _c.c_int32])
_n.bind("CAD_GetParticleSettingsJson", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_SetParticleSettingsJson", _c.c_int32, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_GetParticleLiveCount", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_GetParticlePresetCount", _c.c_int32, [])
_n.bind("CAD_GetParticlePresetName", _c.c_int32, [_c.c_int32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_GetParticlePresetPath", _c.c_int32, [_c.c_int32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_SaveParticlePreset", _c.c_int32, [_c.c_uint32, _c.c_char_p])


def CAD_CreateParticleEmitter(preset: int, position: CAD_GeVec3, unitsPerMeter: float, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateParticleEmitter(int32_t preset, CAD_GeVec3 position, double unitsPerMeter, const CAD_CreateOptions* opt, uint32_t* outId)
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateParticleEmitter(preset, position, unitsPerMeter, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateParticleEmitterFromPreset(path: str | None, position: CAD_GeVec3, unitsPerMeter: float, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateParticleEmitterFromPreset(const char* path, CAD_GeVec3 position, double unitsPerMeter, const CAD_CreateOptions* opt, uint32_t* outId)

    LotCAD v1 JSON 프리셋(Unity·Unreal·Effekseer 아님)으로. UTF-8 경로, 원본 파일은 안 바꾼다.
    파일 없음 = CAD_E_NOT_FOUND, 못 읽음 = CAD_E_FAILED
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateParticleEmitterFromPreset(_n.text(path), position, unitsPerMeter, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_CreateExternalEffect(path: str | None, position: CAD_GeVec3, unitsPerMeter: float, opt: CAD_CreateOptions | None = None, **fields) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateExternalEffect(const char* path, CAD_GeVec3 position, double unitsPerMeter, const CAD_CreateOptions* opt, uint32_t* outId)

    Effekseer .efkefc/.efk(참조 자원 포함). CAD_SetParticlePlayback 으로 같이 다룬다. 파일은 .lot 에 담긴다.
    Effekseer 없는 빌드·못 읽음 = CAD_E_FAILED + 이유
    """
    if opt is None and fields:
        opt = CAD_CreateOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_CreateOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    outId = _c.c_uint32()
    _r = _f.CAD_CreateExternalEffect(_n.text(path), position, unitsPerMeter, _p_opt, _c.byref(outId))
    return (_r, outId.value)


def CAD_SetParticlePlayback(id: int, state: int) -> int:
    """C: CAD_Status CAD_SetParticlePlayback(uint32_t id, int32_t state)

    CAD_PARTICLE_PAUSE·PLAY·RESET

    묶음 주석: Effekseer .efkefc/.efk(참조 자원 포함). CAD_SetParticlePlayback 으로 같이 다룬다. 파일은 .lot 에 담긴다.
    Effekseer 없는 빌드·못 읽음 = CAD_E_FAILED + 이유
    """
    return _f.CAD_SetParticlePlayback(id, state)


def CAD_GetParticleSettingsJson(id: int) -> str | None:
    """C: int32_t CAD_GetParticleSettingsJson(uint32_t id, char* buf, uint32_t capacity)

    설정 — particle_preset_io.h 의 JSON v1(version, unit, style, rate, lifetime, speed, radius, spread, size, acceleration,
    start_color, end_color, capacity, seed). Get 은 unit "m". Set 은 준 키만 바꾼다(unit "mm" 면 준 길이 키를 바꿔 읽음), 되돌리기 1.
    틀린 JSON·값 = CAD_E_INVALID_ARG + 이유
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


def CAD_SetParticleSettingsJson(id: int, json: str | None) -> int:
    """C: CAD_Status CAD_SetParticleSettingsJson(uint32_t id, const char* json)

    설정 — particle_preset_io.h 의 JSON v1(version, unit, style, rate, lifetime, speed, radius, spread, size, acceleration,
    start_color, end_color, capacity, seed). Get 은 unit "m". Set 은 준 키만 바꾼다(unit "mm" 면 준 길이 키를 바꿔 읽음), 되돌리기 1.
    틀린 JSON·값 = CAD_E_INVALID_ARG + 이유
    """
    return _f.CAD_SetParticleSettingsJson(id, _n.text(json))


def CAD_GetParticleLiveCount(id: int) -> int:
    """C: int32_t CAD_GetParticleLiveCount(uint32_t id)

    지금 살아 있는 입자 수

    묶음 주석: 설정 — particle_preset_io.h 의 JSON v1(version, unit, style, rate, lifetime, speed, radius, spread, size, acceleration,
    start_color, end_color, capacity, seed). Get 은 unit "m". Set 은 준 키만 바꾼다(unit "mm" 면 준 길이 키를 바꿔 읽음), 되돌리기 1.
    틀린 JSON·값 = CAD_E_INVALID_ARG + 이유
    """
    return _f.CAD_GetParticleLiveCount(id)


def CAD_GetParticlePresetCount() -> int:
    """C: int32_t CAD_GetParticlePresetCount(void)

    프리셋 목록 — effects/*.json 이름 순, 처음 쓸 때 읽는다(패널 불필요, iOS 도). 경로 = 절대 UTF-8(CreateParticleEmitterFromPreset 에 그대로).
    Effekseer 파일은 안 나온다. 번호 범위 밖 = CAD_E_OUT_OF_RANGE
    """
    return _f.CAD_GetParticlePresetCount()


def CAD_GetParticlePresetName(index: int) -> str | None:
    """C: int32_t CAD_GetParticlePresetName(int32_t index, char* buf, uint32_t capacity)

    프리셋 목록 — effects/*.json 이름 순, 처음 쓸 때 읽는다(패널 불필요, iOS 도). 경로 = 절대 UTF-8(CreateParticleEmitterFromPreset 에 그대로).
    Effekseer 파일은 안 나온다. 번호 범위 밖 = CAD_E_OUT_OF_RANGE
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
    """C: int32_t CAD_GetParticlePresetPath(int32_t index, char* buf, uint32_t capacity)

    프리셋 목록 — effects/*.json 이름 순, 처음 쓸 때 읽는다(패널 불필요, iOS 도). 경로 = 절대 UTF-8(CreateParticleEmitterFromPreset 에 그대로).
    Effekseer 파일은 안 나온다. 번호 범위 밖 = CAD_E_OUT_OF_RANGE
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


def CAD_SaveParticlePreset(id: int, path: str | None) -> int:
    """C: CAD_Status CAD_SaveParticlePreset(uint32_t id, const char* path)

    방출기 설정을 v1 프리셋으로 저장(UTF-8 경로, 폴더 만듦). effects/ 에 저장하면 목록도 다시
    """
    return _f.CAD_SaveParticlePreset(id, _n.text(path))
