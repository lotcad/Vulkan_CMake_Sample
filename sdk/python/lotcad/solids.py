# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Solids 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_RequestStartRevolve', 'CAD_BooleanUnion', 'CAD_BooleanIntersection', 'CAD_BooleanDifference', 'CAD_BooleanUnionIds', 'CAD_BooleanIntersectionIds', 'CAD_BooleanSubtract']

_f = _n.native

_n.bind("CAD_RequestStartRevolve", None, [])
_n.bind("CAD_BooleanUnion", None, [_c.c_bool])
_n.bind("CAD_BooleanIntersection", None, [_c.c_bool])
_n.bind("CAD_BooleanDifference", None, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool])
_n.bind("CAD_BooleanUnionIds", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool])
_n.bind("CAD_BooleanIntersectionIds", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool])
_n.bind("CAD_BooleanSubtract", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_bool, _c.c_bool, _c.POINTER(_c.c_uint32), _c.c_uint32])


def CAD_RequestStartRevolve() -> None:
    """C: void CAD_RequestStartRevolve(void)
    """
    _f.CAD_RequestStartRevolve()


def CAD_BooleanUnion(keepOriginals: bool) -> None:
    """C: void CAD_BooleanUnion(bool keepOriginals)

    **요청형**(예전부터 있던 셋) — 반환값 없음, 다음 프레임에 실행. 결과 id·실패를 알 수 없다.
    Union/Intersection 은 **부른 순간의 선택**(메시만)이 대상. keepOriginals=false 면 원본 삭제(되돌리기 한 단계).
    결과가 필요하거나 여러 번 이어 부를 땐 아래 바로 실행형(CAD_BooleanUnionIds …)을 쓴다.
    """
    _f.CAD_BooleanUnion(keepOriginals)


def CAD_BooleanIntersection(keepOriginals: bool) -> None:
    """C: void CAD_BooleanIntersection(bool keepOriginals)
    """
    _f.CAD_BooleanIntersection(keepOriginals)


def CAD_BooleanDifference(baseIds: Sequence | None, baseCount: int, subtractIds: Sequence | None, subtractCount: int, keepOriginals: bool) -> None:
    """C: void CAD_BooleanDifference(const uint32_t* baseIds, uint32_t baseCount, const uint32_t* subtractIds, uint32_t subtractCount, bool keepOriginals)

    Difference: union(baseIds) − union(subtractIds). id 배열 + 개수 전달.
    """
    _a_baseIds = _n.array(_c.c_uint32, baseIds)
    _a_subtractIds = _n.array(_c.c_uint32, subtractIds)
    _f.CAD_BooleanDifference(_a_baseIds, baseCount, _a_subtractIds, subtractCount, keepOriginals)


def CAD_BooleanUnionIds(ids: Sequence | None, count: int, keepOriginals: bool) -> int:
    """C: uint32_t CAD_BooleanUnionIds(const uint32_t* ids, uint32_t count, bool keepOriginals)

    **바로 실행형**(2026-10-04) — 부르면 그 자리에서 계산하고 결과를 돌려준다. 선택과 무관(넘긴 id 만),
    한 프레임에 여러 번 이어 불러도 된다. 공통 규칙:
    · 입력을 먼저 전부 검사 — 없는 id·메시 아님·잠긴 도면층·닫히지 않은 메시·중복(기준과 빼는 쪽 사이 포함)이
    하나라도 있으면 **아무것도 바꾸지 않고** 0, 이유는 CAD_GetLastError.
    · 결과(들) 추가 + 원본 삭제(keepOriginals=false) = 되돌리기 한 단계. 끝나면 결과만 선택된다.
    · 결과는 첫 원본(기준)의 이름·도면층·색·금속·불투명도를 이어받는다(텍스처는 안 이어받음 — UV 없음).
    · 여러 개는 한 번에 계산(Manifold BatchBoolean) — 순서 무관.
    합집합 — ids 2개 이상 → 한 객체(떨어져 있어도 한 객체에 덩어리 여럿). 결과 id, 실패 0.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_BooleanUnionIds(_a_ids, count, keepOriginals)


def CAD_BooleanIntersectionIds(ids: Sequence | None, count: int, keepOriginals: bool) -> int:
    """C: uint32_t CAD_BooleanIntersectionIds(const uint32_t* ids, uint32_t count, bool keepOriginals)

    교집합 — ids 2개 이상 **모두의** 공통 부분(A∩B∩C). 공통 부분이 없으면 0. 결과 id, 실패 0.
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_BooleanIntersectionIds(_a_ids, count, keepOriginals)


def CAD_BooleanSubtract(baseIds: Sequence | None, baseCount: int, cutIds: Sequence | None, cutCount: int, keepOriginals: bool, perBase: bool, outIds: Any, cap: int) -> int:
    """C: uint32_t CAD_BooleanSubtract(const uint32_t* baseIds, uint32_t baseCount, const uint32_t* cutIds, uint32_t cutCount, bool keepOriginals, bool perBase, uint32_t* outIds, uint32_t cap)

    차집합 — 기준 baseIds 에서 cutIds 전부를 뺀다.
    perBase=false: union(기준) − union(빼는 것) → 결과 1개(기준들이 한 덩어리로 합쳐짐, 오토캐드 SUBTRACT 와 같음)
    perBase=true : 기준마다 따로(판 3장에 같은 구멍 → 판 3장). 통째로 깎여 사라진 기준은 결과가 없다.
    반환 = 결과 개수(실패 0), outIds 에 cap 개까지 결과 id. outIds=NULL 이면 **빼기는 하고** 개수만 — 같은 프레임에 같은 인자로
    버퍼를 들고 다시 부르면 다시 빼지 않고 그 결과 id 를 준다(2회 호출 규약). CAD_Offset·CAD_Mirror·CAD_CheckInterference 도 같다.
    """
    _a_baseIds = _n.array(_c.c_uint32, baseIds)
    _a_cutIds = _n.array(_c.c_uint32, cutIds)
    return _f.CAD_BooleanSubtract(_a_baseIds, baseCount, _a_cutIds, cutCount, keepOriginals, perBase, outIds, cap)
