# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Edit 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_BeginTransaction', 'CAD_EndTransaction', 'CAD_RollbackTransaction', 'CAD_TransactionDepth', 'CAD_Loft', 'CAD_Shell', 'CAD_Explode', 'CAD_EdgeFillet', 'CAD_EdgeChamfer', 'CAD_ArrayRect', 'CAD_ArrayPolar', 'CAD_Undo', 'CAD_Redo', 'CAD_CanUndo', 'CAD_CanRedo']

_f = _n.native

_n.bind("CAD_BeginTransaction", None, [_c.c_char_p])
_n.bind("CAD_EndTransaction", _c.c_bool, [])
_n.bind("CAD_RollbackTransaction", _c.c_bool, [])
_n.bind("CAD_TransactionDepth", _c.c_int, [])
_n.bind("CAD_Loft", _c.c_bool, [])
_n.bind("CAD_Shell", _c.c_bool, [_c.c_float])
_n.bind("CAD_Explode", _c.c_bool, [_c.c_bool])
_n.bind("CAD_EdgeFillet", _c.c_bool, [_c.c_float])
_n.bind("CAD_EdgeChamfer", _c.c_bool, [_c.c_float])
_n.bind("CAD_ArrayRect", _c.c_bool, [_c.c_int, _c.c_int, _c.c_float, _c.c_float])
_n.bind("CAD_ArrayPolar", _c.c_bool, [_c.c_int, _c.c_float, _c.c_float, _c.c_float, _c.c_float, _c.c_bool])
_n.bind("CAD_Undo", None, [])
_n.bind("CAD_Redo", None, [])
_n.bind("CAD_CanUndo", _c.c_bool, [])
_n.bind("CAD_CanRedo", _c.c_bool, [])


def CAD_BeginTransaction(name: str | None) -> None:
    """C: void CAD_BeginTransaction(const char* name)

    트랜잭션 — 여러 편집(생성·속성·삭제·이동…)을 되돌리기 **한 단계** 로 묶는다.
    Begin … End 사이의 CAD_Create·Set·Delete·SetObjectProperty 는 실행은 즉시 되고, End 에서 한 묶음으로
    undo 스택에 오른다(Ctrl+Z 한 번). Rollback 은 묶음을 되돌리고 버린다(미리보기 거절). 중첩 가능(깊이 셈).
    열린 동안 CAD_Undo/Redo 는 false. name 은 UI 의 되돌리기 이름.
    """
    _f.CAD_BeginTransaction(_n.text(name))


def CAD_EndTransaction() -> bool:
    """C: bool CAD_EndTransaction(void)

    트랜잭션 — 여러 편집(생성·속성·삭제·이동…)을 되돌리기 **한 단계** 로 묶는다.
    Begin … End 사이의 CAD_Create·Set·Delete·SetObjectProperty 는 실행은 즉시 되고, End 에서 한 묶음으로
    undo 스택에 오른다(Ctrl+Z 한 번). Rollback 은 묶음을 되돌리고 버린다(미리보기 거절). 중첩 가능(깊이 셈).
    열린 동안 CAD_Undo/Redo 는 false. name 은 UI 의 되돌리기 이름.
    """
    return _f.CAD_EndTransaction()


def CAD_RollbackTransaction() -> bool:
    """C: bool CAD_RollbackTransaction(void)

    트랜잭션 — 여러 편집(생성·속성·삭제·이동…)을 되돌리기 **한 단계** 로 묶는다.
    Begin … End 사이의 CAD_Create·Set·Delete·SetObjectProperty 는 실행은 즉시 되고, End 에서 한 묶음으로
    undo 스택에 오른다(Ctrl+Z 한 번). Rollback 은 묶음을 되돌리고 버린다(미리보기 거절). 중첩 가능(깊이 셈).
    열린 동안 CAD_Undo/Redo 는 false. name 은 UI 의 되돌리기 이름.
    """
    return _f.CAD_RollbackTransaction()


def CAD_TransactionDepth() -> int:
    """C: int CAD_TransactionDepth(void)

    트랜잭션 — 여러 편집(생성·속성·삭제·이동…)을 되돌리기 **한 단계** 로 묶는다.
    Begin … End 사이의 CAD_Create·Set·Delete·SetObjectProperty 는 실행은 즉시 되고, End 에서 한 묶음으로
    undo 스택에 오른다(Ctrl+Z 한 번). Rollback 은 묶음을 되돌리고 버린다(미리보기 거절). 중첩 가능(깊이 셈).
    열린 동안 CAD_Undo/Redo 는 false. name 은 UI 의 되돌리기 이름.
    """
    return _f.CAD_TransactionDepth()


def CAD_Loft() -> bool:
    """C: bool CAD_Loft(void)

    로프트 — 선택된 **닫힌 단면 2개 이상**을 축 순서로 이어 솔리드 생성.
    단면이 지그재그로 놓여 순서를 직접 주고 싶으면 화면에서 클릭 순서로 지정해야 한다.
    """
    return _f.CAD_Loft()


def CAD_Shell(thickness: float) -> bool:
    """C: bool CAD_Shell(float thickness)

    셸 — 선택 솔리드의 속을 비우고 두께만 남긴다. thickness<=0 이면 크기에 맞춰 자동.
    """
    return _f.CAD_Shell(thickness)


def CAD_Explode(keepOriginal: bool) -> bool:
    """C: bool CAD_Explode(bool keepOriginal)

    분해(EXPLODE) — 선택 객체를 구성 요소로 쪼갠다.
    문자                → 글리프 윤곽선 폴리선
    폴리선/사각형/다각형 → 개별 선분 (닫힌 도형은 마지막↔첫 정점 구간까지)
    선·원·호는 더 쪼갤 수 없어 그대로 남는다. keepOriginal=true 면 원본을 지우지 않는다.
    여러 종류가 섞여 있어도 undo 는 한 번이다. 쪼갤 것이 하나도 없으면 false.
    """
    return _f.CAD_Explode(keepOriginal)


def CAD_EdgeFillet(distance: float) -> bool:
    """C: bool CAD_EdgeFillet(float distance)

    모서리 필렛/챔퍼 — 선택 솔리드의 볼록 모서리를 굴리거나(fillet) 깎는다(chamfer).
    distance<=0 이면 객체 크기에 맞춰 자동.
    """
    return _f.CAD_EdgeFillet(distance)


def CAD_EdgeChamfer(distance: float) -> bool:
    """C: bool CAD_EdgeChamfer(float distance)

    모서리 필렛/챔퍼 — 선택 솔리드의 볼록 모서리를 굴리거나(fillet) 깎는다(chamfer).
    distance<=0 이면 객체 크기에 맞춰 자동.
    """
    return _f.CAD_EdgeChamfer(distance)


def CAD_ArrayRect(cols: int, rows: int, dx: float, dy: float) -> bool:
    """C: bool CAD_ArrayRect(int cols, int rows, float dx, float dy)

    직사각형 배열 — cols(가로 개수) × rows(세로 개수), dx/dy 간격(음수 = 반대 방향).
    원본이 (0,0) 칸을 차지하므로 실제 생성 개수는 cols*rows-1.
    평면은 활성 뷰에서 정해진다 (Top=XY, Front=XZ, Right=YZ).
    """
    return _f.CAD_ArrayRect(cols, rows, dx, dy)


def CAD_ArrayPolar(count: int, angleDeg: float, centerX: float, centerY: float, centerZ: float, rotateItems: bool) -> bool:
    """C: bool CAD_ArrayPolar(int count, float angleDeg, float centerX, float centerY, float centerZ, bool rotateItems)

    원형 배열 — count = **원본 포함** 총 개수, angleDeg = 총 채움 각(360 = 한 바퀴).
    center = 회전 중심(월드), rotateItems=false 면 항목 방향을 유지한 채 위치만 옮긴다.
    회전축은 활성 뷰의 평면 법선이다.
    """
    return _f.CAD_ArrayPolar(count, angleDeg, centerX, centerY, centerZ, rotateItems)


def CAD_Undo() -> None:
    """C: void CAD_Undo(void)
    """
    _f.CAD_Undo()


def CAD_Redo() -> None:
    """C: void CAD_Redo(void)
    """
    _f.CAD_Redo()


def CAD_CanUndo() -> bool:
    """C: bool CAD_CanUndo(void)
    """
    return _f.CAD_CanUndo()


def CAD_CanRedo() -> bool:
    """C: bool CAD_CanRedo(void)
    """
    return _f.CAD_CanRedo()
