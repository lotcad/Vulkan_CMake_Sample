# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Files 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_ExportFile', 'CAD_ExportObj', 'CAD_SaveAs', 'CAD_OpenFile']

_f = _n.native

_n.bind("CAD_ExportFile", _c.c_bool, [_c.c_char_p, _c.c_bool])
_n.bind("CAD_ExportObj", _c.c_bool, [_c.c_char_p, _c.c_bool])
_n.bind("CAD_SaveAs", _c.c_bool, [_c.c_char_p, _c.c_bool])
_n.bind("CAD_OpenFile", _c.c_bool, [_c.c_char_p])


def CAD_ExportFile(path: str | None, selectedOnly: bool) -> bool:
    """C: bool CAD_ExportFile(const char* path, bool selectedOnly)

    내보내기

    **확장자로 포맷이 정해진다** — .stl .dxf .glb .obj .lot
    전에는 CAD_ExportObj 하나뿐이라 나머지 포맷을 호스트에서 쓸 수가 없었다.
    selectedOnly=true 면 선택된 것만(선택이 비었으면 실패).
    대화상자를 띄우지 않으므로 경로는 호스트가 정한다.
    """
    return _f.CAD_ExportFile(_n.text(path), selectedOnly)


def CAD_ExportObj(path: str | None, selectedOnly: bool) -> bool:
    """C: bool CAD_ExportObj(const char* path, bool selectedOnly)

    selectedOnly=false → 씬 전체, true → 선택 객체만. 월드 좌표로 baking. 성공 시 true.
    """
    return _f.CAD_ExportObj(_n.text(path), selectedOnly)


def CAD_SaveAs(pathUtf8: str | None, selectedOnly: bool) -> bool:
    """C: bool CAD_SaveAs(const char* pathUtf8, bool selectedOnly)

    확장자로 갈린다. 엔진 안의 분기(saveByExtension / loadModelFromPath)를 그대로 쓴다 —
    호스트가 포맷을 판별해 다른 함수를 고를 필요가 없고, 새 포맷이 붙어도 API 는 그대로다.

    CAD_SaveAs  : .lot(프로젝트) · .stl · .dxf · .obj · .glb/.gltf
    .lot 은 씬 전체(선·솔리드·로봇·문서 상태)를 담는 네이티브 형식이고,
    나머지는 내보내기다. selectedOnly=true 면 선택 객체만.
    점군도 .lot 에 담긴다(2026-09 부터). 다만 파일이 커진다 — 점당 21.3B.
    CAD_OpenFile: .lot · .obj · .stl · .dxf · .ply(점군) · .gltf/.glb · .fbx (static meshes)
    **현재 문서에 추가**한다(새 탭을 만들지 않음). 새 탭으로 열려면
    CAD_OpenDocument 를 쓴다.

    둘 다 실패 시 false 를 반환하고 사유는 CAD_GetStatusMessage 로 읽는다.
    """
    return _f.CAD_SaveAs(_n.text(pathUtf8), selectedOnly)


def CAD_OpenFile(pathUtf8: str | None) -> bool:
    """C: bool CAD_OpenFile(const char* pathUtf8)

    확장자로 갈린다. 엔진 안의 분기(saveByExtension / loadModelFromPath)를 그대로 쓴다 —
    호스트가 포맷을 판별해 다른 함수를 고를 필요가 없고, 새 포맷이 붙어도 API 는 그대로다.

    CAD_SaveAs  : .lot(프로젝트) · .stl · .dxf · .obj · .glb/.gltf
    .lot 은 씬 전체(선·솔리드·로봇·문서 상태)를 담는 네이티브 형식이고,
    나머지는 내보내기다. selectedOnly=true 면 선택 객체만.
    점군도 .lot 에 담긴다(2026-09 부터). 다만 파일이 커진다 — 점당 21.3B.
    CAD_OpenFile: .lot · .obj · .stl · .dxf · .ply(점군) · .gltf/.glb · .fbx (static meshes)
    **현재 문서에 추가**한다(새 탭을 만들지 않음). 새 탭으로 열려면
    CAD_OpenDocument 를 쓴다.

    둘 다 실패 시 false 를 반환하고 사유는 CAD_GetStatusMessage 로 읽는다.
    """
    return _f.CAD_OpenFile(_n.text(pathUtf8))
