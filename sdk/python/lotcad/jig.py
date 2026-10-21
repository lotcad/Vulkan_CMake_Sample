# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Jig 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_JigBegin', 'CAD_JigBeginOne', 'CAD_JigState', 'CAD_JigCancel', 'CAD_JigMoveTo', 'CAD_JigCommit', 'CAD_JigSetBasePoint', 'CAD_JigGetDelta', 'CAD_JigBeginVariants', 'CAD_JigNextVariant', 'CAD_JigVariantIndex', 'CAD_JigVariantId', 'CAD_RequestMoveSelected', 'CAD_RequestRotateSelected', 'CAD_RequestScaleSelected', 'CAD_RequestCopySelected', 'CAD_RequestColorSelected', 'CAD_CreateBox']

_f = _n.native

_n.bind("CAD_JigBegin", _c.c_bool, [_c.c_int, _c.POINTER(_c.c_uint32), _c.c_int, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_JigBeginOne", _c.c_bool, [_c.c_int, _c.c_uint32, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_JigState", _c.c_int, [])
_n.bind("CAD_JigCancel", None, [])
_n.bind("CAD_JigMoveTo", _c.c_bool, [_c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_JigCommit", _c.c_bool, [])
_n.bind("CAD_JigSetBasePoint", _c.c_bool, [_c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_JigGetDelta", _c.c_bool, [_c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float)])
_n.bind("CAD_JigBeginVariants", _c.c_bool, [_c.c_int, _c.POINTER(_c.c_uint32), _c.c_int, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_JigNextVariant", _c.c_bool, [])
_n.bind("CAD_JigVariantIndex", _c.c_int, [])
_n.bind("CAD_JigVariantId", _c.c_uint32, [])
_n.bind("CAD_RequestMoveSelected", None, [_c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_RequestRotateSelected", None, [_c.c_float, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_RequestScaleSelected", None, [_c.c_float])
_n.bind("CAD_RequestCopySelected", None, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_int])
_n.bind("CAD_RequestColorSelected", None, [_c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_CreateBox", _c.c_uint32, [_c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_float])


def CAD_JigBegin(mode: int, ids: Sequence | None, count: int, px: float, py: float, pz: float) -> bool:
    """C: bool CAD_JigBegin(int mode, const uint32_t* ids, int count, float px, float py, float pz)

    객체 id 를 물려 시작하면 그 객체가 **커서를 따라다니고**, 좌클릭에 그 자리로 확정된다
    (undo 1스텝). ESC 로 원복. OSnap·직교 트랙킹(F8)·콘솔 값 입력이 그대로 적용된다.
    mode: 0=이동 1=회전 2=축척 3=복사
    회전/축척은 (px,py,pz) 가 피벗. 이동/복사는 무시하고 선택 전체의 시각 중심을 기준점으로 잡는다.
    반환 false = 유효한 객체가 없어 시작 못 함.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_JigBegin(mode, _a_ids, count, px, py, pz)


def CAD_JigBeginOne(mode: int, id: int, px: float, py: float, pz: float) -> bool:
    """C: bool CAD_JigBeginOne(int mode, uint32_t id, float px, float py, float pz)

    객체 id 를 물려 시작하면 그 객체가 **커서를 따라다니고**, 좌클릭에 그 자리로 확정된다
    (undo 1스텝). ESC 로 원복. OSnap·직교 트랙킹(F8)·콘솔 값 입력이 그대로 적용된다.
    mode: 0=이동 1=회전 2=축척 3=복사
    회전/축척은 (px,py,pz) 가 피벗. 이동/복사는 무시하고 선택 전체의 시각 중심을 기준점으로 잡는다.
    반환 false = 유효한 객체가 없어 시작 못 함.
    """
    return _f.CAD_JigBeginOne(mode, id, px, py, pz)


def CAD_JigState() -> int:
    """C: int CAD_JigState(void)

    상태 폴링 — 0=비활성 1=끌는 중 2=직전 확정됨 3=직전 취소됨 (2/3 은 1회만 반환).
    """
    return _f.CAD_JigState()


def CAD_JigCancel() -> None:
    """C: void CAD_JigCancel(void)

    상태 폴링 — 0=비활성 1=끌는 중 2=직전 확정됨 3=직전 취소됨 (2/3 은 1회만 반환).
    """
    _f.CAD_JigCancel()


def CAD_JigMoveTo(x: float, y: float, z: float) -> bool:
    """C: bool CAD_JigMoveTo(float x, float y, float z)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    return _f.CAD_JigMoveTo(x, y, z)


def CAD_JigCommit() -> bool:
    """C: bool CAD_JigCommit(void)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    return _f.CAD_JigCommit()


def CAD_JigSetBasePoint(x: float, y: float, z: float) -> bool:
    """C: bool CAD_JigSetBasePoint(float x, float y, float z)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    return _f.CAD_JigSetBasePoint(x, y, z)


def CAD_JigGetDelta() -> tuple[float, float, float, float, float] | None:
    """C: bool CAD_JigGetDelta(float* dx, float* dy, float* dz, float* angleDeg, float* scale)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    dx = _c.c_float()
    dy = _c.c_float()
    dz = _c.c_float()
    angleDeg = _c.c_float()
    scale = _c.c_float()
    if not _f.CAD_JigGetDelta(_c.byref(dx), _c.byref(dy), _c.byref(dz), _c.byref(angleDeg), _c.byref(scale)):
        return None
    return (dx.value, dy.value, dz.value, angleDeg.value, scale.value)


def CAD_JigBeginVariants(mode: int, ids: Sequence | None, count: int, px: float, py: float, pz: float) -> bool:
    """C: bool CAD_JigBeginVariants(int mode, const uint32_t* ids, int count, float px, float py, float pz)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_JigBeginVariants(mode, _a_ids, count, px, py, pz)


def CAD_JigNextVariant() -> bool:
    """C: bool CAD_JigNextVariant(void)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    Tab 과 동일 (호스트 버튼으로 전환할 때)
    """
    return _f.CAD_JigNextVariant()


def CAD_JigVariantIndex() -> int:
    """C: int CAD_JigVariantIndex(void)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    현재 후보 번호, -1 = 변형 Jig 아님
    """
    return _f.CAD_JigVariantIndex()


def CAD_JigVariantId() -> int:
    """C: uint32_t CAD_JigVariantId(void)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    지금 끌고 있는 후보 id (없으면 0)
    """
    return _f.CAD_JigVariantId()


def CAD_RequestMoveSelected(dirX: float, dirY: float, dirZ: float, distance: float) -> None:
    """C: void CAD_RequestMoveSelected(float dirX, float dirY, float dirZ, float distance)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    _f.CAD_RequestMoveSelected(dirX, dirY, dirZ, distance)


def CAD_RequestRotateSelected(axisX: float, axisY: float, axisZ: float, angleDeg: float) -> None:
    """C: void CAD_RequestRotateSelected(float axisX, float axisY, float axisZ, float angleDeg)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    _f.CAD_RequestRotateSelected(axisX, axisY, axisZ, angleDeg)


def CAD_RequestScaleSelected(factor: float) -> None:
    """C: void CAD_RequestScaleSelected(float factor)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    _f.CAD_RequestScaleSelected(factor)


def CAD_RequestCopySelected(dirX: float, dirY: float, dirZ: float, distance: float, count: int) -> None:
    """C: void CAD_RequestCopySelected(float dirX, float dirY, float dirZ, float distance, int count)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    _f.CAD_RequestCopySelected(dirX, dirY, dirZ, distance, count)


def CAD_RequestColorSelected(r: float, g: float, b: float) -> None:
    """C: void CAD_RequestColorSelected(float r, float g, float b)

    후보 객체들을 미리 만들어 id 배열로 넘기면, 첫 후보가 커서를 따라오고 **Tab** 마다 다음 후보로
    갈아끼워진다(문 좌/우열림, 볼트 규격 등). 비활성 후보는 씬에서 잠시 빠져 보이지 않는다.
    확정 → 선택된 후보만 남고 나머지는 삭제 (AcEdJig 의 "성공 시에만 남긴다" 규약)
    취소 → 후보 전부 삭제 (임시 형상이라 씬에 남기지 않음)
    콜백이 필요 없어 C#/Qt 어디서든 그대로 쓸 수 있다.
    코드로 끌기 — 모바일(가상 커서 없이 버튼으로)·자동 시연. Jig 중이 아니면 false.
    MoveTo: 지그를 월드 점으로(OSnap 미적용). 이후 실제 마우스가 움직이면 다시 마우스를 따른다.
    Commit: 좌클릭과 같은 확정(undo 1). CAD_JigState 는 다음 폴링에 2.
    SetBasePoint: 이동·복사의 기준점(기본 = 선택 경계 상자 중심), 회전·축척은 피벗.
    GetDelta: 지금 미리보기 — 이동량(이동·복사, 직교 반영), 회전각(도), 배율. 인자는 NULL 가능.
    """
    _f.CAD_RequestColorSelected(r, g, b)


def CAD_CreateBox(x: float, y: float, z: float, sx: float, sy: float, sz: float) -> int:
    """C: uint32_t CAD_CreateBox(float x, float y, float z, float sx, float sy, float sz)
    """
    return _f.CAD_CreateBox(x, y, z, sx, sy, sz)
