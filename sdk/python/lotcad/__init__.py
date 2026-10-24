# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API 파이썬 바인딩 — 헤더(LotCAD_API.h)의 함수 전부.

    import lotcad
    lotcad.CAD_SetRuntimeAssetPath(lotcad.SDK_DIR)   # models·fonts·textures 위치
    lotcad.CAD_CreateEngine()
    box = lotcad.CAD_CreateBox(0, 0, 0.5, 1, 1, 1)
    st, p = lotcad.CAD_GetPosition(box)                # 결과 코드 + 출력 인자(CAD_GeVec3) — st == 0 이면 p.x, p.y, p.z
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
from .analysis import *  # noqa: F401,F403
from .app import *  # noqa: F401,F403
from .arch import *  # noqa: F401,F403
from .curves import *  # noqa: F401,F403
from .document import *  # noqa: F401,F403
from .drawing import *  # noqa: F401,F403
from .editor import *  # noqa: F401,F403
from .effects import *  # noqa: F401,F403
from .events import *  # noqa: F401,F403
from .geometry import *  # noqa: F401,F403
from .mesh import *  # noqa: F401,F403
from .modify import *  # noqa: F401,F403
from .nav import *  # noqa: F401,F403
from .objects import *  # noqa: F401,F403
from .plugin import *  # noqa: F401,F403
from .robot import *  # noqa: F401,F403
from .solids import *  # noqa: F401,F403
from .types import *  # noqa: F401,F403
from .view import *  # noqa: F401,F403
