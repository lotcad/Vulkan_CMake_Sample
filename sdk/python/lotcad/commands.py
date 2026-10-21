# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Commands 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_ExecuteCommand']

_f = _n.native

_n.bind("CAD_ExecuteCommand", _c.c_bool, [_c.c_char_p])


def CAD_ExecuteCommand(name: str | None) -> bool:
    """C: bool CAD_ExecuteCommand(const char* name)

    명령 실행

    엔진의 **모든 명령**을 이름으로 실행한다. 아래 CAD_RequestXxx 들은 자주 쓰는 것만
    개별 함수로 뽑아 둔 것이고, 엔진에는 명령이 200개가 넘는다(trim / offset / fillet /
    ocr / navmap / imageattach …). 이 함수 하나면 그 전부가 열리고, 새 명령을 추가할
    때마다 API 를 늘리지 않아도 된다.

      CAD_ExecuteCommand("trim");        // 자르기
      CAD_ExecuteCommand("offset");      // 오프셋
      CAD_ExecuteCommand("2,3");         // 진행 중인 도구에 좌표/값 전달

    이름은 하단 명령행에 치는 것과 **똑같다**(영문·짧은 별칭·한글 모두).
    진행 중인 도구가 있으면 값 입력으로 전달된다 — 명령행과 완전히 같은 경로.
    반환: 알 수 없는 이름이면 false. 값 입력으로 소비된 경우도 true.
    """
    return _f.CAD_ExecuteCommand(_n.text(name))
