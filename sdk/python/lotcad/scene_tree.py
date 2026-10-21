# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — SceneTree 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_GetSceneRevision', 'CAD_GetSceneTreeJson', 'CAD_GetLayersJson', 'CAD_GetBlocksJson', 'CAD_CreateBlock', 'CAD_GetInsertAttributesJson', 'CAD_SetInsertAttributesJson', 'CAD_XrefReload', 'CAD_XrefSetPath', 'CAD_XrefBind', 'CAD_XrefDetach']

_f = _n.native

_n.bind("CAD_GetSceneRevision", _c.c_uint64, [])
_n.bind("CAD_GetSceneTreeJson", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetLayersJson", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetBlocksJson", _c.c_int, [_c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_CreateBlock", _c.c_uint32, [_c.c_char_p, _c.POINTER(_c.c_uint32), _c.c_int, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_GetInsertAttributesJson", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_SetInsertAttributesJson", _c.c_bool, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_XrefReload", _c.c_bool, [_c.c_char_p])
_n.bind("CAD_XrefSetPath", _c.c_bool, [_c.c_char_p, _c.c_char_p])
_n.bind("CAD_XrefBind", _c.c_bool, [_c.c_char_p])
_n.bind("CAD_XrefDetach", _c.c_bool, [_c.c_char_p])


def CAD_GetSceneRevision() -> int:
    """C: uint64_t CAD_GetSceneRevision(void)

    장면이 바뀔 때마다(객체 추가·삭제·이름·보이기·도면층 …) 커지는 번호 — 같으면 다시 안 읽어도 된다(폴링용).
    """
    return _f.CAD_GetSceneRevision()


def CAD_GetSceneTreeJson() -> str | None:
    """C: int CAD_GetSceneTreeJson(char* out, int cap)

    노드 트리 — 엔진 패널과 같은 구성(파일 → glTF/FBX 노드 계층 → 객체 → 피처·가공 기록). 평평한 배열 + 부모 번호:
    {"revision","nodes":[{"index","key","kind":"scene|file|node|object|feature","label","parent"(-1 = 뿌리),"depth","children":[…],
    "total","shown"(아래 객체 수·보이는 수),  객체 줄만: "objectId"(1 이상),"objectKind","visible","selected","locked"(bool),"layerId","layer"}]}
    objectKind = 문자열, CAD_GetObjectJson 의 "kind" 와 같다: "mesh" "line" "polyline" "circle" "arc" "text" "dimension"
    "pointcloud" "particle" "effect" "hatch" "insert"(블록 참조) (모르는 종류 "unknown"). 객체 id 는 늘 1 이상(0 = 없음/실패).
    클릭·보이기·이름 바꾸기는 기존 함수로: CAD_SelectObject · CAD_SetObjectVisible · CAD_SetObjectName(묶음 줄은 children 의 objectId 들).
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetSceneTreeJson(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetLayersJson() -> str | None:
    """C: int CAD_GetLayersJson(char* out, int cap)

    도면층 창 — 한 번에: {"revision","layers":[{"id","name","visible","locked","color":[r,g,b],"opacity","linetypeId","linetype",
    "objectCount","selectedCount"(,"fixed":true — 도면층 0)}]}. 바꾸기는 기존 CAD_SetLayer*·CAD_RenameLayer·CAD_CreateLayer·CAD_AssignSelectedToLayer.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetLayersJson(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetBlocksJson() -> str | None:
    """C: int CAD_GetBlocksJson(char* out, int cap)

    블록(블록 참조 — docs/BLOCKS_2026-10-12.md). 정의 표 한 번에: {"blocks":[{"name","objects","references"(장면에 넣은 수),
    "base":[x,y,z],"bounds":{"min","max"}(있으면),"xref"(외부 참조 경로, 있으면)}]}. 블록 편집은 명령으로: CAD_ExecuteCommand("bedit 이름") ·
    "bsave" · "bclose save|discard" · "bbase x,y" (탭을 여닫으므로 다음 CAD_Tick 에 처리된다).
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetBlocksJson(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_CreateBlock(nameUtf8: str | None, ids: Sequence | None, count: int, baseX: float, baseY: float, baseZ: float) -> int:
    """C: uint32_t CAD_CreateBlock(const char* nameUtf8, const uint32_t* ids, int count, float baseX, float baseY, float baseZ)

    객체들로 새 블록 정의 + 그 자리(층 "0")에 INSERT 하나 — 명령 block 과 같다, 되돌리기 1. 반환 = 새 INSERT id(0 = 실패, 이유는 CAD_GetLastError)
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_CreateBlock(_n.text(nameUtf8), _a_ids, count, baseX, baseY, baseZ)


def CAD_GetInsertAttributesJson(id: int) -> str | None:
    """C: int CAD_GetInsertAttributesJson(uint32_t id, char* out, int cap)

    블록 참조의 속성 글 값 — JSON 문자열 배열(속성 글 id 순). Get: 반환 = 길이, 블록 참조가 아니면 -1.
    Set: 같은 개수의 배열 — 그 INSERT 만 바뀐다(복사한 INSERT 와 같이 쓰던 묶음은 사본으로), 되돌리기 1. 실패면 false + CAD_GetLastError
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetInsertAttributesJson(id, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_SetInsertAttributesJson(id: int, jsonArray: str | None) -> bool:
    """C: bool CAD_SetInsertAttributesJson(uint32_t id, const char* jsonArray)

    블록 참조의 속성 글 값 — JSON 문자열 배열(속성 글 id 순). Get: 반환 = 길이, 블록 참조가 아니면 -1.
    Set: 같은 개수의 배열 — 그 INSERT 만 바뀐다(복사한 INSERT 와 같이 쓰던 묶음은 사본으로), 되돌리기 1. 실패면 false + CAD_GetLastError
    """
    return _f.CAD_SetInsertAttributesJson(id, _n.text(jsonArray))


def CAD_XrefReload(nameUtf8: str | None) -> bool:
    """C: bool CAD_XrefReload(const char* nameUtf8)

    외부 참조(XREF — 정의 표에서 "xref" 가 있는 블록, ObjectARX acedXrefReload·acedXrefBind·acedXrefDetach·setPathName). 목록·경로·찾음 여부는
    CAD_GetBlocksJson 의 "xref"(적힌 경로)·"xrefFound"(읽은 파일)·"xrefLoaded". 명령 xref 와 같고 전부 되돌리기 1, 실패 false + CAD_GetLastError.
    Reload : 그 파일을 다시 읽어 정의를 바꾼다(그 INSERT 들이 따라 바뀜)
    SetPath: pathOrKind = "absolute" | "relative" | "none"(파일 이름만) 이면 경로 모양만(상대는 도면을 저장한 뒤),
    그 밖은 새 경로 — 적고 그 파일로 다시 읽는다(옮긴 파일 다시 찾기)
    Bind   : 보통 블록으로 굳힘 — 딸린 이름 "SITE|문" → "SITE$0$문"(블록·도면층·선종류)
    Detach : 그 INSERT·정의를 지움(다른 블록 안에 들어 있으면 거부)
    저장(.lot·DXF·DWG)엔 경로만 쓰고 열 때 다시 읽는다 — 상대 경로는 저장 자리 기준으로 다시 맞춘다.
    """
    return _f.CAD_XrefReload(_n.text(nameUtf8))


def CAD_XrefSetPath(nameUtf8: str | None, pathOrKindUtf8: str | None) -> bool:
    """C: bool CAD_XrefSetPath(const char* nameUtf8, const char* pathOrKindUtf8)

    외부 참조(XREF — 정의 표에서 "xref" 가 있는 블록, ObjectARX acedXrefReload·acedXrefBind·acedXrefDetach·setPathName). 목록·경로·찾음 여부는
    CAD_GetBlocksJson 의 "xref"(적힌 경로)·"xrefFound"(읽은 파일)·"xrefLoaded". 명령 xref 와 같고 전부 되돌리기 1, 실패 false + CAD_GetLastError.
    Reload : 그 파일을 다시 읽어 정의를 바꾼다(그 INSERT 들이 따라 바뀜)
    SetPath: pathOrKind = "absolute" | "relative" | "none"(파일 이름만) 이면 경로 모양만(상대는 도면을 저장한 뒤),
    그 밖은 새 경로 — 적고 그 파일로 다시 읽는다(옮긴 파일 다시 찾기)
    Bind   : 보통 블록으로 굳힘 — 딸린 이름 "SITE|문" → "SITE$0$문"(블록·도면층·선종류)
    Detach : 그 INSERT·정의를 지움(다른 블록 안에 들어 있으면 거부)
    저장(.lot·DXF·DWG)엔 경로만 쓰고 열 때 다시 읽는다 — 상대 경로는 저장 자리 기준으로 다시 맞춘다.
    """
    return _f.CAD_XrefSetPath(_n.text(nameUtf8), _n.text(pathOrKindUtf8))


def CAD_XrefBind(nameUtf8: str | None) -> bool:
    """C: bool CAD_XrefBind(const char* nameUtf8)

    외부 참조(XREF — 정의 표에서 "xref" 가 있는 블록, ObjectARX acedXrefReload·acedXrefBind·acedXrefDetach·setPathName). 목록·경로·찾음 여부는
    CAD_GetBlocksJson 의 "xref"(적힌 경로)·"xrefFound"(읽은 파일)·"xrefLoaded". 명령 xref 와 같고 전부 되돌리기 1, 실패 false + CAD_GetLastError.
    Reload : 그 파일을 다시 읽어 정의를 바꾼다(그 INSERT 들이 따라 바뀜)
    SetPath: pathOrKind = "absolute" | "relative" | "none"(파일 이름만) 이면 경로 모양만(상대는 도면을 저장한 뒤),
    그 밖은 새 경로 — 적고 그 파일로 다시 읽는다(옮긴 파일 다시 찾기)
    Bind   : 보통 블록으로 굳힘 — 딸린 이름 "SITE|문" → "SITE$0$문"(블록·도면층·선종류)
    Detach : 그 INSERT·정의를 지움(다른 블록 안에 들어 있으면 거부)
    저장(.lot·DXF·DWG)엔 경로만 쓰고 열 때 다시 읽는다 — 상대 경로는 저장 자리 기준으로 다시 맞춘다.
    """
    return _f.CAD_XrefBind(_n.text(nameUtf8))


def CAD_XrefDetach(nameUtf8: str | None) -> bool:
    """C: bool CAD_XrefDetach(const char* nameUtf8)

    외부 참조(XREF — 정의 표에서 "xref" 가 있는 블록, ObjectARX acedXrefReload·acedXrefBind·acedXrefDetach·setPathName). 목록·경로·찾음 여부는
    CAD_GetBlocksJson 의 "xref"(적힌 경로)·"xrefFound"(읽은 파일)·"xrefLoaded". 명령 xref 와 같고 전부 되돌리기 1, 실패 false + CAD_GetLastError.
    Reload : 그 파일을 다시 읽어 정의를 바꾼다(그 INSERT 들이 따라 바뀜)
    SetPath: pathOrKind = "absolute" | "relative" | "none"(파일 이름만) 이면 경로 모양만(상대는 도면을 저장한 뒤),
    그 밖은 새 경로 — 적고 그 파일로 다시 읽는다(옮긴 파일 다시 찾기)
    Bind   : 보통 블록으로 굳힘 — 딸린 이름 "SITE|문" → "SITE$0$문"(블록·도면층·선종류)
    Detach : 그 INSERT·정의를 지움(다른 블록 안에 들어 있으면 거부)
    저장(.lot·DXF·DWG)엔 경로만 쓰고 열 때 다시 읽는다 — 상대 경로는 저장 자리 기준으로 다시 맞춘다.
    """
    return _f.CAD_XrefDetach(_n.text(nameUtf8))
