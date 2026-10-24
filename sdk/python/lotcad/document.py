# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Document 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_LINETYPE_BYLAYER', 'CAD_GetDocumentCount', 'CAD_GetActiveDocument', 'CAD_GetDocumentTitle', 'CAD_GetDocumentPath', 'CAD_IsDocumentDirty', 'CAD_NewDocument', 'CAD_OpenDocument', 'CAD_ActivateDocument', 'CAD_CloseDocument', 'CAD_BeginTransaction', 'CAD_EndTransaction', 'CAD_RollbackTransaction', 'CAD_TransactionDepth', 'CAD_GetSceneRevision', 'CAD_GetSceneTreeJson', 'CAD_GetLayersJson', 'CAD_GetBlocksJson', 'CAD_CreateBlock', 'CAD_GetInsertAttributesJson', 'CAD_SetInsertAttributesJson', 'CAD_XrefReload', 'CAD_XrefSetPath', 'CAD_XrefBind', 'CAD_XrefDetach', 'CAD_CreateLayer', 'CAD_SetLayerColor', 'CAD_GetLayerColor', 'CAD_SetLayerOpacity', 'CAD_GetLayerOpacity', 'CAD_GetLayerIds', 'CAD_GetLayerName', 'CAD_RenameLayer', 'CAD_SetLayerVisible', 'CAD_IsLayerVisible', 'CAD_SetLayerLocked', 'CAD_IsLayerLocked', 'CAD_CreateLinetype', 'CAD_GetLinetypeIds', 'CAD_GetLinetypeName', 'CAD_GetLinetypePattern', 'CAD_SetObjectLinetype', 'CAD_GetObjectLinetype', 'CAD_SetObjectLinetypeScale', 'CAD_GetObjectLinetypeScale', 'CAD_SetSelectedLinetype', 'CAD_SetLayerLinetype', 'CAD_GetLayerLinetype', 'CAD_SetLinetypeScale', 'CAD_GetLinetypeScale', 'CAD_ExportFile', 'CAD_ExportObj', 'CAD_SaveAs', 'CAD_OpenFile', 'CAD_Undo', 'CAD_Redo', 'CAD_CanUndo', 'CAD_CanRedo']

_f = _n.native

CAD_LINETYPE_BYLAYER = 0xFFFFFFFF

_n.bind("CAD_GetDocumentCount", _c.c_int, [])
_n.bind("CAD_GetActiveDocument", _c.c_int, [])
_n.bind("CAD_GetDocumentTitle", _c.c_int, [_c.c_int, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetDocumentPath", _c.c_int, [_c.c_int, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_IsDocumentDirty", _c.c_bool, [_c.c_int])
_n.bind("CAD_NewDocument", _c.c_int, [_c.c_char_p])
_n.bind("CAD_OpenDocument", _c.c_int, [_c.c_char_p])
_n.bind("CAD_ActivateDocument", _c.c_bool, [_c.c_int])
_n.bind("CAD_CloseDocument", _c.c_bool, [_c.c_int])
_n.bind("CAD_BeginTransaction", None, [_c.c_char_p])
_n.bind("CAD_EndTransaction", _c.c_bool, [])
_n.bind("CAD_RollbackTransaction", _c.c_bool, [])
_n.bind("CAD_TransactionDepth", _c.c_int, [])
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
_n.bind("CAD_CreateLayer", _c.c_uint32, [_c.c_char_p])
_n.bind("CAD_SetLayerColor", _c.c_bool, [_c.c_uint32, _c.c_float, _c.c_float, _c.c_float])
_n.bind("CAD_GetLayerColor", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float), _c.POINTER(_c.c_float), _c.POINTER(_c.c_float)])
_n.bind("CAD_SetLayerOpacity", _c.c_bool, [_c.c_uint32, _c.c_float])
_n.bind("CAD_GetLayerOpacity", _c.c_float, [_c.c_uint32])
_n.bind("CAD_GetLayerIds", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_GetLayerName", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_RenameLayer", _c.c_bool, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_SetLayerVisible", _c.c_bool, [_c.c_uint32, _c.c_bool])
_n.bind("CAD_IsLayerVisible", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_SetLayerLocked", _c.c_bool, [_c.c_uint32, _c.c_bool])
_n.bind("CAD_IsLayerLocked", _c.c_bool, [_c.c_uint32])
_n.bind("CAD_CreateLinetype", _c.c_uint32, [_c.c_char_p, _c.POINTER(_c.c_float), _c.c_int, _c.c_char_p])
_n.bind("CAD_GetLinetypeIds", _c.c_uint32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_GetLinetypeName", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_GetLinetypePattern", _c.c_int, [_c.c_uint32, _c.POINTER(_c.c_float), _c.c_int])
_n.bind("CAD_SetObjectLinetype", _c.c_bool, [_c.c_uint32, _c.c_uint32])
_n.bind("CAD_GetObjectLinetype", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetObjectLinetypeScale", _c.c_bool, [_c.c_uint32, _c.c_float])
_n.bind("CAD_GetObjectLinetypeScale", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_float)])
_n.bind("CAD_SetSelectedLinetype", _c.c_uint32, [_c.c_uint32])
_n.bind("CAD_SetLayerLinetype", _c.c_bool, [_c.c_uint32, _c.c_uint32])
_n.bind("CAD_GetLayerLinetype", _c.c_bool, [_c.c_uint32, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetLinetypeScale", _c.c_bool, [_c.c_float])
_n.bind("CAD_GetLinetypeScale", _c.c_float, [])
_n.bind("CAD_ExportFile", _c.c_bool, [_c.c_char_p, _c.c_bool])
_n.bind("CAD_ExportObj", _c.c_bool, [_c.c_char_p, _c.c_bool])
_n.bind("CAD_SaveAs", _c.c_bool, [_c.c_char_p, _c.c_bool])
_n.bind("CAD_OpenFile", _c.c_bool, [_c.c_char_p])
_n.bind("CAD_Undo", None, [])
_n.bind("CAD_Redo", None, [])
_n.bind("CAD_CanUndo", _c.c_bool, [])
_n.bind("CAD_CanRedo", _c.c_bool, [])


def CAD_GetDocumentCount() -> int:
    """C: int CAD_GetDocumentCount(void)

    여러 파일을 동시에 열고 탭으로 전환한다. 호스트(WPF/Qt)가 **자기 탭 UI** 를 그릴 수 있도록
    목록 조회 + 전환/열기/닫기를 모두 노출한다. 전환은 상태 swap 이라 비용이 거의 없다.
    """
    return _f.CAD_GetDocumentCount()


def CAD_GetActiveDocument() -> int:
    """C: int CAD_GetActiveDocument(void)

    여러 파일을 동시에 열고 탭으로 전환한다. 호스트(WPF/Qt)가 **자기 탭 UI** 를 그릴 수 있도록
    목록 조회 + 전환/열기/닫기를 모두 노출한다. 전환은 상태 swap 이라 비용이 거의 없다.
    """
    return _f.CAD_GetActiveDocument()


def CAD_GetDocumentTitle(index: int) -> str | None:
    """C: int CAD_GetDocumentTitle(int index, char* outUtf8, int cap)

    탭 라벨용 — 표시 이름(파일명 또는 "제목 없음"). 길이 반환, -1=실패. buf 는 null 허용(길이만 조회).
    """
    _need = _f.CAD_GetDocumentTitle(index, None, 0)   # 2회 호출 규약: 길이를 물으며 한 번 실행
    if _need < 0:
        return None
    _cap = _need + 1
    _buf = _c.create_string_buffer(_cap)
    if _f.CAD_GetDocumentTitle(index, _buf, _cap) < 0:   # 같은 인자 → 다시 실행하지 않고 결과만
        return None
    return _n.decode(_buf.value)


def CAD_GetDocumentPath(index: int) -> str | None:
    """C: int CAD_GetDocumentPath (int index, char* outUtf8, int cap)

    탭 라벨용 — 표시 이름(파일명 또는 "제목 없음"). 길이 반환, -1=실패. buf 는 null 허용(길이만 조회).
    """
    _need = _f.CAD_GetDocumentPath(index, None, 0)   # 2회 호출 규약: 길이를 물으며 한 번 실행
    if _need < 0:
        return None
    _cap = _need + 1
    _buf = _c.create_string_buffer(_cap)
    if _f.CAD_GetDocumentPath(index, _buf, _cap) < 0:   # 같은 인자 → 다시 실행하지 않고 결과만
        return None
    return _n.decode(_buf.value)


def CAD_IsDocumentDirty(index: int) -> bool:
    """C: bool CAD_IsDocumentDirty(int index)

    저장되지 않은 변경이 있는지 — 탭에 * 표시하거나 닫기 확인에 사용.
    """
    return _f.CAD_IsDocumentDirty(index)


def CAD_NewDocument(titleUtf8: str | None) -> int:
    """C: int CAD_NewDocument(const char* titleUtf8)

    새 빈 문서 추가 후 활성화. 반환 = 새 문서 인덱스.
    """
    return _f.CAD_NewDocument(_n.text(titleUtf8))


def CAD_OpenDocument(pathUtf8: str | None) -> int:
    """C: int CAD_OpenDocument(const char* pathUtf8)

    파일을 새 탭으로 열기. 반환 = 문서 인덱스, 실패 -1.
    """
    return _f.CAD_OpenDocument(_n.text(pathUtf8))


def CAD_ActivateDocument(index: int) -> bool:
    """C: bool CAD_ActivateDocument(int index)

    파일을 새 탭으로 열기. 반환 = 문서 인덱스, 실패 -1.
    """
    return _f.CAD_ActivateDocument(index)


def CAD_CloseDocument(index: int) -> bool:
    """C: bool CAD_CloseDocument(int index)

    닫기 — 마지막 문서는 닫지 않고 내용을 비운다(항상 문서 1개 유지).
    """
    return _f.CAD_CloseDocument(index)


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


def CAD_CreateLayer(name: str | None) -> int:
    """C: uint32_t CAD_CreateLayer(const char* name)

    Document layers. 0 is the always-visible, unlocked default layer.
    """
    return _f.CAD_CreateLayer(_n.text(name))


def CAD_SetLayerColor(id: int, r: float, g: float, b: float) -> bool:
    """C: bool CAD_SetLayerColor(uint32_t id,float r,float g,float b)

    RGB in [0,1]. Layer 0 has fixed white ByLayer color.
    """
    return _f.CAD_SetLayerColor(id, r, g, b)


def CAD_GetLayerColor(id: int) -> tuple[float, float, float] | None:
    """C: bool CAD_GetLayerColor(uint32_t id,float* r,float* g,float* b)

    RGB in [0,1]. Layer 0 has fixed white ByLayer color.
    """
    r = _c.c_float()
    g = _c.c_float()
    b = _c.c_float()
    if not _f.CAD_GetLayerColor(id, _c.byref(r), _c.byref(g), _c.byref(b)):
        return None
    return (r.value, g.value, b.value)


def CAD_SetLayerOpacity(id: int, opacity: float) -> bool:
    """C: bool CAD_SetLayerOpacity(uint32_t id, float opacity)
    """
    return _f.CAD_SetLayerOpacity(id, opacity)


def CAD_GetLayerOpacity(id: int) -> float:
    """C: float CAD_GetLayerOpacity(uint32_t id)
    """
    return _f.CAD_GetLayerOpacity(id)


def CAD_GetLayerIds(out: Any, capacity: int) -> int:
    """C: uint32_t CAD_GetLayerIds(uint32_t* out, uint32_t capacity)

    required count, includes 0
    """
    return _f.CAD_GetLayerIds(out, capacity)


def CAD_GetLayerName(id: int) -> str | None:
    """C: int CAD_GetLayerName(uint32_t id, char* out, int capacity)
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetLayerName(id, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_RenameLayer(id: int, name: str | None) -> bool:
    """C: bool CAD_RenameLayer(uint32_t id, const char* name)
    """
    return _f.CAD_RenameLayer(id, _n.text(name))


def CAD_SetLayerVisible(id: int, visible: bool) -> bool:
    """C: bool CAD_SetLayerVisible(uint32_t id, bool visible)
    """
    return _f.CAD_SetLayerVisible(id, visible)


def CAD_IsLayerVisible(id: int) -> bool:
    """C: bool CAD_IsLayerVisible(uint32_t id)
    """
    return _f.CAD_IsLayerVisible(id)


def CAD_SetLayerLocked(id: int, locked: bool) -> bool:
    """C: bool CAD_SetLayerLocked(uint32_t id, bool locked)
    """
    return _f.CAD_SetLayerLocked(id, locked)


def CAD_IsLayerLocked(id: int) -> bool:
    """C: bool CAD_IsLayerLocked(uint32_t id)
    """
    return _f.CAD_IsLayerLocked(id)


def CAD_CreateLinetype(name: str | None, pattern: Sequence | None, count: int, description: str | None) -> int:
    """C: uint32_t CAD_CreateLinetype(const char* name, const float* pattern, int count, const char* description)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    _a_pattern = _n.array(_c.c_float, pattern)
    return _f.CAD_CreateLinetype(_n.text(name), _a_pattern, count, _n.text(description))


def CAD_GetLinetypeIds(out: Any, capacity: int) -> int:
    """C: uint32_t CAD_GetLinetypeIds(uint32_t* out, uint32_t capacity)

    필요한 개수, 0(Continuous) 포함

    묶음 주석: 사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    return _f.CAD_GetLinetypeIds(out, capacity)


def CAD_GetLinetypeName(id: int) -> str | None:
    """C: int CAD_GetLinetypeName(uint32_t id, char* out, int capacity)

    이름 길이, 없으면 -1

    묶음 주석: 사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetLinetypeName(id, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetLinetypePattern(id: int, out: Any, capacity: int) -> int:
    """C: int CAD_GetLinetypePattern(uint32_t id, float* out, int capacity)

    요소 수, 없으면 -1

    묶음 주석: 사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    return _f.CAD_GetLinetypePattern(id, out, capacity)


def CAD_SetObjectLinetype(objectId: int, linetypeId: int) -> bool:
    """C: bool CAD_SetObjectLinetype(uint32_t objectId, uint32_t linetypeId)

    CAD_LINETYPE_BYLAYER 허용

    묶음 주석: 사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    return _f.CAD_SetObjectLinetype(objectId, linetypeId)


def CAD_GetObjectLinetype(objectId: int) -> int | None:
    """C: bool CAD_GetObjectLinetype(uint32_t objectId, uint32_t* out)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    out = _c.c_uint32()
    if not _f.CAD_GetObjectLinetype(objectId, _c.byref(out)):
        return None
    return out.value


def CAD_SetObjectLinetypeScale(objectId: int, scale: float) -> bool:
    """C: bool CAD_SetObjectLinetypeScale(uint32_t objectId, float scale)

    객체별 축척(CELTSCALE)

    묶음 주석: 사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    return _f.CAD_SetObjectLinetypeScale(objectId, scale)


def CAD_GetObjectLinetypeScale(objectId: int) -> float | None:
    """C: bool CAD_GetObjectLinetypeScale(uint32_t objectId, float* out)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    out = _c.c_float()
    if not _f.CAD_GetObjectLinetypeScale(objectId, _c.byref(out)):
        return None
    return out.value


def CAD_SetSelectedLinetype(linetypeId: int) -> int:
    """C: uint32_t CAD_SetSelectedLinetype(uint32_t linetypeId)

    바뀐 객체 수

    묶음 주석: 사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    return _f.CAD_SetSelectedLinetype(linetypeId)


def CAD_SetLayerLinetype(layerId: int, linetypeId: int) -> bool:
    """C: bool CAD_SetLayerLinetype(uint32_t layerId, uint32_t linetypeId)

    도면층 0 은 실선 고정

    묶음 주석: 사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    return _f.CAD_SetLayerLinetype(layerId, linetypeId)


def CAD_GetLayerLinetype(layerId: int) -> int | None:
    """C: bool CAD_GetLayerLinetype(uint32_t layerId, uint32_t* out)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    out = _c.c_uint32()
    if not _f.CAD_GetLayerLinetype(layerId, _c.byref(out)):
        return None
    return out.value


def CAD_SetLinetypeScale(scale: float) -> bool:
    """C: bool CAD_SetLinetypeScale(float scale)

    전역 LTSCALE

    묶음 주석: 사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    return _f.CAD_SetLinetypeScale(scale)


def CAD_GetLinetypeScale() -> float:
    """C: float CAD_GetLinetypeScale(void)

    사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
    """
    return _f.CAD_GetLinetypeScale()


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
