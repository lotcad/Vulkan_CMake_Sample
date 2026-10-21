# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API 파이썬 바인딩 — 헤더(LotCAD_API.h)의 함수 전부.

    import lotcad
    lotcad.CAD_SetRuntimeAssetPath(lotcad.SDK_DIR)   # models·fonts·textures 위치
    lotcad.CAD_CreateEngine()
    box = lotcad.CAD_CreateBox(0, 0, 0.5, 1, 1, 1)
    x, y, z = lotcad.CAD_GetPosition(box)              # 출력 인자는 반환값으로
    print(lotcad.CAD_GetObjectJson(box))               # 문자열 버퍼는 str 로
    while not lotcad.CAD_ShouldClose() and lotcad.CAD_Tick():
        pass
    lotcad.CAD_DestroyEngine()

함수 이름·의미는 헤더와 같다 — help(lotcad.CAD_CreateBox) 에 C 선언과 헤더 주석이 있다.
원시 ctypes 함수(헤더와 똑같은 인자)는 lotcad.native.CAD_xxx.
엔진 함수는 엔진을 만든 스레드에서만 부른다(콜백도 CAD_Tick 안, 같은 스레드에서 온다).
"""
from ._native import LIBRARY_PATH, SDK_DIR, buffer, native  # noqa: F401
from ._types import *  # noqa: F401,F403
from .ai import *  # noqa: F401,F403
from .brep import *  # noqa: F401,F403
from .callbacks import *  # noqa: F401,F403
from .commands import *  # noqa: F401,F403
from .documents import *  # noqa: F401,F403
from .drawing import *  # noqa: F401,F403
from .edit import *  # noqa: F401,F403
from .engine import *  # noqa: F401,F403
from .files import *  # noqa: F401,F403
from .floorplan import *  # noqa: F401,F403
from .images import *  # noqa: F401,F403
from .input import *  # noqa: F401,F403
from .jig import *  # noqa: F401,F403
from .linetypes import *  # noqa: F401,F403
from .link import *  # noqa: F401,F403
from .mobile import *  # noqa: F401,F403
from .modeling import *  # noqa: F401,F403
from .navigation import *  # noqa: F401,F403
from .objects import *  # noqa: F401,F403
from .overlay import *  # noqa: F401,F403
from .particles import *  # noqa: F401,F403
from .pick import *  # noqa: F401,F403
from .plugins import *  # noqa: F401,F403
from .point_cloud import *  # noqa: F401,F403
from .robot import *  # noqa: F401,F403
from .scene_tree import *  # noqa: F401,F403
from .section import *  # noqa: F401,F403
from .sketch_constraints import *  # noqa: F401,F403
from .snap import *  # noqa: F401,F403
from .solids import *  # noqa: F401,F403
from .text import *  # noqa: F401,F403
from .transform import *  # noqa: F401,F403
from .view import *  # noqa: F401,F403
