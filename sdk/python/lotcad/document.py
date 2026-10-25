# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Document 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_LINETYPE_BYLAYER', 'CAD_GetDocumentCount', 'CAD_GetActiveDocument', 'CAD_GetDocumentTitle', 'CAD_GetDocumentPath', 'CAD_IsDocumentDirty', 'CAD_NewDocument', 'CAD_OpenDocument', 'CAD_ActivateDocument', 'CAD_CloseDocument', 'CAD_BeginTransaction', 'CAD_EndTransaction', 'CAD_RollbackTransaction', 'CAD_TransactionDepth', 'CAD_GetSceneRevision', 'CAD_GetSceneTreeJson', 'CAD_GetLayersJson', 'CAD_GetBlocksJson', 'CAD_CreateBlock', 'CAD_GetInsertAttributesJson', 'CAD_SetInsertAttributesJson', 'CAD_XrefReload', 'CAD_XrefSetPath', 'CAD_XrefBind', 'CAD_XrefDetach', 'CAD_CreateLayer', 'CAD_SetLayerColor', 'CAD_GetLayerColor', 'CAD_SetLayerOpacity', 'CAD_GetLayerOpacity', 'CAD_GetLayerIds', 'CAD_GetLayerName', 'CAD_RenameLayer', 'CAD_SetLayerVisible', 'CAD_IsLayerVisible', 'CAD_SetLayerLocked', 'CAD_IsLayerLocked', 'CAD_CreateLinetype', 'CAD_GetLinetypeIds', 'CAD_GetLinetypeName', 'CAD_GetLinetypePattern', 'CAD_SetObjectLinetype', 'CAD_GetObjectLinetype', 'CAD_SetObjectLinetypeScale', 'CAD_GetObjectLinetypeScale', 'CAD_SetLayerLinetype', 'CAD_GetLayerLinetype', 'CAD_SetLinetypeScale', 'CAD_GetLinetypeScale', 'CAD_SaveAs', 'CAD_OpenFile', 'CAD_Undo', 'CAD_Redo', 'CAD_CanUndo', 'CAD_CanRedo']

_f = _n.native

CAD_LINETYPE_BYLAYER = 0xFFFFFFFF

_n.bind("CAD_GetDocumentCount", _c.c_int32, [])
_n.bind("CAD_GetActiveDocument", _c.c_int32, [])
_n.bind("CAD_GetDocumentTitle", _c.c_int32, [_c.c_int32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_GetDocumentPath", _c.c_int32, [_c.c_int32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_IsDocumentDirty", _c.c_int32, [_c.c_int32, _c.POINTER(_c.c_bool)])
_n.bind("CAD_NewDocument", _c.c_int32, [_c.c_char_p, _c.POINTER(_c.c_int32)])
_n.bind("CAD_OpenDocument", _c.c_int32, [_c.c_char_p, _c.POINTER(_c.c_int32)])
_n.bind("CAD_ActivateDocument", _c.c_int32, [_c.c_int32])
_n.bind("CAD_CloseDocument", _c.c_int32, [_c.c_int32])
_n.bind("CAD_BeginTransaction", _c.c_int32, [_c.c_char_p])
_n.bind("CAD_EndTransaction", _c.c_int32, [])
_n.bind("CAD_RollbackTransaction", _c.c_int32, [])
_n.bind("CAD_TransactionDepth", _c.c_int32, [])
_n.bind("CAD_GetSceneRevision", _c.c_int32, [_c.POINTER(_c.c_uint64)])
_n.bind("CAD_GetSceneTreeJson", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_GetLayersJson", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_GetBlocksJson", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_CreateBlock", _c.c_int32, [_c.c_char_p, _c.POINTER(_c.c_uint32), _c.c_uint32, CAD_GeVec3, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_GetInsertAttributesJson", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_SetInsertAttributesJson", _c.c_int32, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_XrefReload", _c.c_int32, [_c.c_char_p])
_n.bind("CAD_XrefSetPath", _c.c_int32, [_c.c_char_p, _c.c_char_p])
_n.bind("CAD_XrefBind", _c.c_int32, [_c.c_char_p])
_n.bind("CAD_XrefDetach", _c.c_int32, [_c.c_char_p])
_n.bind("CAD_CreateLayer", _c.c_int32, [_c.c_char_p, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetLayerColor", _c.c_int32, [_c.c_uint32, CAD_Color])
_n.bind("CAD_GetLayerColor", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_Color)])
_n.bind("CAD_SetLayerOpacity", _c.c_int32, [_c.c_uint32, _c.c_double])
_n.bind("CAD_GetLayerOpacity", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_double)])
_n.bind("CAD_GetLayerIds", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_GetLayerName", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_RenameLayer", _c.c_int32, [_c.c_uint32, _c.c_char_p])
_n.bind("CAD_SetLayerVisible", _c.c_int32, [_c.c_uint32, _c.c_bool])
_n.bind("CAD_IsLayerVisible", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_bool)])
_n.bind("CAD_SetLayerLocked", _c.c_int32, [_c.c_uint32, _c.c_bool])
_n.bind("CAD_IsLayerLocked", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_bool)])
_n.bind("CAD_CreateLinetype", _c.c_int32, [_c.c_char_p, _c.POINTER(_c.c_double), _c.c_uint32, _c.c_char_p, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_GetLinetypeIds", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_GetLinetypeName", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_GetLinetypePattern", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_double), _c.c_uint32])
_n.bind("CAD_SetObjectLinetype", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_uint32, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_GetObjectLinetype", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetObjectLinetypeScale", _c.c_int32, [_c.c_uint32, _c.c_double])
_n.bind("CAD_GetObjectLinetypeScale", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_double)])
_n.bind("CAD_SetLayerLinetype", _c.c_int32, [_c.c_uint32, _c.c_uint32])
_n.bind("CAD_GetLayerLinetype", _c.c_int32, [_c.c_uint32, _c.POINTER(_c.c_uint32)])
_n.bind("CAD_SetLinetypeScale", _c.c_int32, [_c.c_double])
_n.bind("CAD_GetLinetypeScale", _c.c_int32, [_c.POINTER(_c.c_double)])
_n.bind("CAD_SaveAs", _c.c_int32, [_c.c_char_p, _c.c_bool])
_n.bind("CAD_OpenFile", _c.c_int32, [_c.c_char_p])
_n.bind("CAD_Undo", _c.c_int32, [])
_n.bind("CAD_Redo", _c.c_int32, [])
_n.bind("CAD_CanUndo", _c.c_int32, [_c.POINTER(_c.c_bool)])
_n.bind("CAD_CanRedo", _c.c_int32, [_c.POINTER(_c.c_bool)])


def CAD_GetDocumentCount() -> int:
    """C: int32_t CAD_GetDocumentCount(void)

    여러 파일을 동시에 열고 탭으로 전환한다(ObjectARX AcApDocManager 자리). 호스트(WPF/Qt)가 **자기 탭 UI** 를 그릴 수 있도록
    목록 조회 + 전환/열기/닫기를 모두 노출한다. 전환은 상태 swap 이라 비용이 거의 없다. 문서는 번호(0 ~ 개수 − 1)로 —
    닫으면 뒤 번호가 하나씩 당겨진다. 범위 밖 번호 CAD_E_OUT_OF_RANGE. 엔진 스레드에서만.
    """
    return _f.CAD_GetDocumentCount()


def CAD_GetActiveDocument() -> int:
    """C: int32_t CAD_GetActiveDocument(void)

    지금 문서 번호

    묶음 주석: 여러 파일을 동시에 열고 탭으로 전환한다(ObjectARX AcApDocManager 자리). 호스트(WPF/Qt)가 **자기 탭 UI** 를 그릴 수 있도록
    목록 조회 + 전환/열기/닫기를 모두 노출한다. 전환은 상태 swap 이라 비용이 거의 없다. 문서는 번호(0 ~ 개수 − 1)로 —
    닫으면 뒤 번호가 하나씩 당겨진다. 범위 밖 번호 CAD_E_OUT_OF_RANGE. 엔진 스레드에서만.
    """
    return _f.CAD_GetActiveDocument()


def CAD_GetDocumentTitle(index: int) -> str | None:
    """C: int32_t CAD_GetDocumentTitle(int32_t index, char* buf, uint32_t capacity)

    탭 라벨용 — 표시 이름(파일명 또는 "제목 없음") · 파일 경로(저장 전이면 ""). 반환 = 전체 길이, 칸이 모자라면 글자 경계에서 자름
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetDocumentTitle(index, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_GetDocumentPath(index: int) -> str | None:
    """C: int32_t CAD_GetDocumentPath(int32_t index, char* buf, uint32_t capacity)

    탭 라벨용 — 표시 이름(파일명 또는 "제목 없음") · 파일 경로(저장 전이면 ""). 반환 = 전체 길이, 칸이 모자라면 글자 경계에서 자름
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_GetDocumentPath(index, _buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_IsDocumentDirty(index: int) -> tuple[int, bool]:
    """C: CAD_Status CAD_IsDocumentDirty(int32_t index, bool* outDirty)

    저장되지 않은 변경이 있는지 — 탭에 * 표시하거나 닫기 확인에 사용.
    """
    outDirty = _c.c_bool()
    _r = _f.CAD_IsDocumentDirty(index, _c.byref(outDirty))
    return (_r, outDirty.value)


def CAD_NewDocument(titleUtf8: str | None) -> tuple[int, int]:
    """C: CAD_Status CAD_NewDocument(const char* titleUtf8, int32_t* outIndex)

    새 빈 문서 추가 후 활성화(title NULL = "제목 없음"). *outIndex = 새 문서 번호(NULL 가능)
    """
    outIndex = _c.c_int32()
    _r = _f.CAD_NewDocument(_n.text(titleUtf8), _c.byref(outIndex))
    return (_r, outIndex.value)


def CAD_OpenDocument(pathUtf8: str | None) -> tuple[int, int]:
    """C: CAD_Status CAD_OpenDocument(const char* pathUtf8, int32_t* outIndex)

    파일을 새 탭으로 열기(현재 문서에 더하려면 CAD_OpenFile). 없는 파일 CAD_E_NOT_FOUND · 못 읽음 CAD_E_FAILED(+ 이유)
    """
    outIndex = _c.c_int32()
    _r = _f.CAD_OpenDocument(_n.text(pathUtf8), _c.byref(outIndex))
    return (_r, outIndex.value)


def CAD_ActivateDocument(index: int) -> int:
    """C: CAD_Status CAD_ActivateDocument(int32_t index)

    전환(이미 그 문서면 그냥 CAD_OK). 블록 편집 탭이 열린 동안 원래 도면은 CAD_E_LOCKED. 진행 중인 명령은 끝낸다(CAD_CancelCommand 와 같다)
    """
    return _f.CAD_ActivateDocument(index)


def CAD_CloseDocument(index: int) -> int:
    """C: CAD_Status CAD_CloseDocument(int32_t index)

    닫기 — 마지막 문서는 닫지 않고 내용을 비운다(항상 문서 1개 유지). 저장 안 한 변경은 묻지 않고 버린다(먼저 CAD_IsDocumentDirty)
    """
    return _f.CAD_CloseDocument(index)


def CAD_BeginTransaction(name: str | None) -> int:
    """C: CAD_Status CAD_BeginTransaction(const char* name)

    트랜잭션 — 여러 편집(생성·속성·삭제·이동…)을 되돌리기 **한 단계** 로 묶는다.
    Begin … End 사이의 CAD_Create·Set·Delete·SetObjectProperty 는 실행은 즉시 되고, End 에서 한 묶음으로
    undo 스택에 오른다(Ctrl+Z 한 번). Rollback 은 묶음을 되돌리고 버린다(미리보기 거절). 중첩 가능(깊이 셈).
    열린 동안 CAD_Undo/Redo 는 CAD_E_BUSY. name 은 UI 의 되돌리기 이름(NULL·"" = "묶음 편집"). 열린 묶음이 없는데 End·Rollback = CAD_E_NOT_READY
    """
    return _f.CAD_BeginTransaction(_n.text(name))


def CAD_EndTransaction() -> int:
    """C: CAD_Status CAD_EndTransaction(void)

    트랜잭션 — 여러 편집(생성·속성·삭제·이동…)을 되돌리기 **한 단계** 로 묶는다.
    Begin … End 사이의 CAD_Create·Set·Delete·SetObjectProperty 는 실행은 즉시 되고, End 에서 한 묶음으로
    undo 스택에 오른다(Ctrl+Z 한 번). Rollback 은 묶음을 되돌리고 버린다(미리보기 거절). 중첩 가능(깊이 셈).
    열린 동안 CAD_Undo/Redo 는 CAD_E_BUSY. name 은 UI 의 되돌리기 이름(NULL·"" = "묶음 편집"). 열린 묶음이 없는데 End·Rollback = CAD_E_NOT_READY
    """
    return _f.CAD_EndTransaction()


def CAD_RollbackTransaction() -> int:
    """C: CAD_Status CAD_RollbackTransaction(void)

    트랜잭션 — 여러 편집(생성·속성·삭제·이동…)을 되돌리기 **한 단계** 로 묶는다.
    Begin … End 사이의 CAD_Create·Set·Delete·SetObjectProperty 는 실행은 즉시 되고, End 에서 한 묶음으로
    undo 스택에 오른다(Ctrl+Z 한 번). Rollback 은 묶음을 되돌리고 버린다(미리보기 거절). 중첩 가능(깊이 셈).
    열린 동안 CAD_Undo/Redo 는 CAD_E_BUSY. name 은 UI 의 되돌리기 이름(NULL·"" = "묶음 편집"). 열린 묶음이 없는데 End·Rollback = CAD_E_NOT_READY
    """
    return _f.CAD_RollbackTransaction()


def CAD_TransactionDepth() -> int:
    """C: int32_t CAD_TransactionDepth(void)

    열린 묶음 깊이(0 = 없음)

    묶음 주석: 트랜잭션 — 여러 편집(생성·속성·삭제·이동…)을 되돌리기 **한 단계** 로 묶는다.
    Begin … End 사이의 CAD_Create·Set·Delete·SetObjectProperty 는 실행은 즉시 되고, End 에서 한 묶음으로
    undo 스택에 오른다(Ctrl+Z 한 번). Rollback 은 묶음을 되돌리고 버린다(미리보기 거절). 중첩 가능(깊이 셈).
    열린 동안 CAD_Undo/Redo 는 CAD_E_BUSY. name 은 UI 의 되돌리기 이름(NULL·"" = "묶음 편집"). 열린 묶음이 없는데 End·Rollback = CAD_E_NOT_READY
    """
    return _f.CAD_TransactionDepth()


def CAD_GetSceneRevision() -> tuple[int, int]:
    """C: CAD_Status CAD_GetSceneRevision(uint64_t* outRevision)

    장면이 바뀔 때마다(객체 추가·삭제·이름·보이기·도면층 …) 커지는 번호 — 같으면 다시 안 읽어도 된다(폴링용).
    """
    outRevision = _c.c_uint64()
    _r = _f.CAD_GetSceneRevision(_c.byref(outRevision))
    return (_r, outRevision.value)


def CAD_GetSceneTreeJson() -> str | None:
    """C: int32_t CAD_GetSceneTreeJson(char* buf, uint32_t capacity)

    노드 트리 — 엔진 패널과 같은 구성(파일 → glTF/FBX 노드 계층 → 객체 → 피처·가공 기록). 평평한 배열 + 부모 번호:
    {"revision","nodes":[{"index","key","kind":"scene|file|node|object|feature","label","parent"(-1 = 뿌리),"depth","children":[…],
    "total","shown"(아래 객체 수·보이는 수),  객체 줄만: "objectId"(1 이상),"objectKind","visible","selected","locked"(bool),"layerId","layer"}]}
    objectKind = 문자열, CAD_GetObjectJson 의 "kind" 와 같다: "mesh" "line" "polyline" "circle" "arc" "text" "dimension"
    "pointcloud" "particle" "effect" "hatch" "insert"(블록 참조) (모르는 종류 "unknown"). 객체 id 는 늘 1 이상(0 = 없음/실패).
    클릭·보이기·이름 바꾸기는 기존 함수로: CAD_SetSelection · CAD_SetObjectVisible · CAD_SetObjectName(묶음 줄은 children 의 objectId 들).
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
    """C: int32_t CAD_GetLayersJson(char* buf, uint32_t capacity)

    도면층 창 — 한 번에: {"revision","layers":[{"id","name","visible","locked","color":[r,g,b],"opacity","linetypeId","linetype",
    "objectCount","selectedCount"(,"fixed":true — 도면층 0)}]}. 바꾸기는 CAD_SetLayer*·CAD_RenameLayer·CAD_CreateLayer·CAD_SetObjectLayer.
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
    """C: int32_t CAD_GetBlocksJson(char* buf, uint32_t capacity)

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


def CAD_CreateBlock(nameUtf8: str | None, ids: Sequence | None, count: int, base: CAD_GeVec3) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateBlock(const char* nameUtf8, const uint32_t* ids, uint32_t count, CAD_GeVec3 base, uint32_t* outInsertId)

    객체들로 새 블록 정의 + 그 자리(층 "0")에 INSERT 하나 — 명령 block 과 같다, 되돌리기 1. base = 기준점(월드). *outInsertId = 새 INSERT id.
    없는 id CAD_E_BAD_HANDLE · 못 만듦(쓰는 이름·잠김 …) CAD_E_FAILED + 이유
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    outInsertId = _c.c_uint32()
    _r = _f.CAD_CreateBlock(_n.text(nameUtf8), _a_ids, count, base, _c.byref(outInsertId))
    return (_r, outInsertId.value)


def CAD_GetInsertAttributesJson(id: int) -> str | None:
    """C: int32_t CAD_GetInsertAttributesJson(uint32_t id, char* buf, uint32_t capacity)

    블록 참조의 속성 글 값 — JSON 문자열 배열(속성 글 id 순). 블록 참조가 아니면 CAD_E_NOT_SUPPORTED.
    Set: 같은 개수의 배열 — 그 INSERT 만 바뀐다(복사한 INSERT 와 같이 쓰던 묶음은 사본으로), 되돌리기 1. 모양이 틀리면 CAD_E_INVALID_ARG + 이유
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


def CAD_SetInsertAttributesJson(id: int, jsonArray: str | None) -> int:
    """C: CAD_Status CAD_SetInsertAttributesJson(uint32_t id, const char* jsonArray)

    블록 참조의 속성 글 값 — JSON 문자열 배열(속성 글 id 순). 블록 참조가 아니면 CAD_E_NOT_SUPPORTED.
    Set: 같은 개수의 배열 — 그 INSERT 만 바뀐다(복사한 INSERT 와 같이 쓰던 묶음은 사본으로), 되돌리기 1. 모양이 틀리면 CAD_E_INVALID_ARG + 이유
    """
    return _f.CAD_SetInsertAttributesJson(id, _n.text(jsonArray))


def CAD_XrefReload(nameUtf8: str | None) -> int:
    """C: CAD_Status CAD_XrefReload(const char* nameUtf8)

    외부 참조(XREF — 정의 표에서 "xref" 가 있는 블록, ObjectARX acedXrefReload·acedXrefBind·acedXrefDetach·setPathName). 목록·경로·찾음 여부는
    CAD_GetBlocksJson 의 "xref"(적힌 경로)·"xrefFound"(읽은 파일)·"xrefLoaded". 명령 xref 와 같고 전부 되돌리기 1, 실패 CAD_E_FAILED + 이유(CAD_GetLastError).
    Reload : 그 파일을 다시 읽어 정의를 바꾼다(그 INSERT 들이 따라 바뀜)
    SetPath: pathOrKind = "absolute" | "relative" | "none"(파일 이름만) 이면 경로 모양만(상대는 도면을 저장한 뒤),
    그 밖은 새 경로 — 적고 그 파일로 다시 읽는다(옮긴 파일 다시 찾기)
    Bind   : 보통 블록으로 굳힘 — 딸린 이름 "SITE|문" → "SITE$0$문"(블록·도면층·선종류)
    Detach : 그 INSERT·정의를 지움(다른 블록 안에 들어 있으면 거부)
    저장(.lot·DXF·DWG)엔 경로만 쓰고 열 때 다시 읽는다 — 상대 경로는 저장 자리 기준으로 다시 맞춘다.
    """
    return _f.CAD_XrefReload(_n.text(nameUtf8))


def CAD_XrefSetPath(nameUtf8: str | None, pathOrKindUtf8: str | None) -> int:
    """C: CAD_Status CAD_XrefSetPath(const char* nameUtf8, const char* pathOrKindUtf8)

    외부 참조(XREF — 정의 표에서 "xref" 가 있는 블록, ObjectARX acedXrefReload·acedXrefBind·acedXrefDetach·setPathName). 목록·경로·찾음 여부는
    CAD_GetBlocksJson 의 "xref"(적힌 경로)·"xrefFound"(읽은 파일)·"xrefLoaded". 명령 xref 와 같고 전부 되돌리기 1, 실패 CAD_E_FAILED + 이유(CAD_GetLastError).
    Reload : 그 파일을 다시 읽어 정의를 바꾼다(그 INSERT 들이 따라 바뀜)
    SetPath: pathOrKind = "absolute" | "relative" | "none"(파일 이름만) 이면 경로 모양만(상대는 도면을 저장한 뒤),
    그 밖은 새 경로 — 적고 그 파일로 다시 읽는다(옮긴 파일 다시 찾기)
    Bind   : 보통 블록으로 굳힘 — 딸린 이름 "SITE|문" → "SITE$0$문"(블록·도면층·선종류)
    Detach : 그 INSERT·정의를 지움(다른 블록 안에 들어 있으면 거부)
    저장(.lot·DXF·DWG)엔 경로만 쓰고 열 때 다시 읽는다 — 상대 경로는 저장 자리 기준으로 다시 맞춘다.
    """
    return _f.CAD_XrefSetPath(_n.text(nameUtf8), _n.text(pathOrKindUtf8))


def CAD_XrefBind(nameUtf8: str | None) -> int:
    """C: CAD_Status CAD_XrefBind(const char* nameUtf8)

    외부 참조(XREF — 정의 표에서 "xref" 가 있는 블록, ObjectARX acedXrefReload·acedXrefBind·acedXrefDetach·setPathName). 목록·경로·찾음 여부는
    CAD_GetBlocksJson 의 "xref"(적힌 경로)·"xrefFound"(읽은 파일)·"xrefLoaded". 명령 xref 와 같고 전부 되돌리기 1, 실패 CAD_E_FAILED + 이유(CAD_GetLastError).
    Reload : 그 파일을 다시 읽어 정의를 바꾼다(그 INSERT 들이 따라 바뀜)
    SetPath: pathOrKind = "absolute" | "relative" | "none"(파일 이름만) 이면 경로 모양만(상대는 도면을 저장한 뒤),
    그 밖은 새 경로 — 적고 그 파일로 다시 읽는다(옮긴 파일 다시 찾기)
    Bind   : 보통 블록으로 굳힘 — 딸린 이름 "SITE|문" → "SITE$0$문"(블록·도면층·선종류)
    Detach : 그 INSERT·정의를 지움(다른 블록 안에 들어 있으면 거부)
    저장(.lot·DXF·DWG)엔 경로만 쓰고 열 때 다시 읽는다 — 상대 경로는 저장 자리 기준으로 다시 맞춘다.
    """
    return _f.CAD_XrefBind(_n.text(nameUtf8))


def CAD_XrefDetach(nameUtf8: str | None) -> int:
    """C: CAD_Status CAD_XrefDetach(const char* nameUtf8)

    외부 참조(XREF — 정의 표에서 "xref" 가 있는 블록, ObjectARX acedXrefReload·acedXrefBind·acedXrefDetach·setPathName). 목록·경로·찾음 여부는
    CAD_GetBlocksJson 의 "xref"(적힌 경로)·"xrefFound"(읽은 파일)·"xrefLoaded". 명령 xref 와 같고 전부 되돌리기 1, 실패 CAD_E_FAILED + 이유(CAD_GetLastError).
    Reload : 그 파일을 다시 읽어 정의를 바꾼다(그 INSERT 들이 따라 바뀜)
    SetPath: pathOrKind = "absolute" | "relative" | "none"(파일 이름만) 이면 경로 모양만(상대는 도면을 저장한 뒤),
    그 밖은 새 경로 — 적고 그 파일로 다시 읽는다(옮긴 파일 다시 찾기)
    Bind   : 보통 블록으로 굳힘 — 딸린 이름 "SITE|문" → "SITE$0$문"(블록·도면층·선종류)
    Detach : 그 INSERT·정의를 지움(다른 블록 안에 들어 있으면 거부)
    저장(.lot·DXF·DWG)엔 경로만 쓰고 열 때 다시 읽는다 — 상대 경로는 저장 자리 기준으로 다시 맞춘다.
    """
    return _f.CAD_XrefDetach(_n.text(nameUtf8))


def CAD_CreateLayer(name: str | None) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateLayer(const char* name, uint32_t* outLayerId)

    도면층 (ObjectARX AcDbLayerTable 자리) — 지금 문서의 표
    id 0 = 도면층 "0"(늘 있음, 늘 보이고 안 잠김, 흰색·실선·불투명 고정 — 바꾸려 하면 CAD_E_NOT_SUPPORTED). 없는 id CAD_E_BAD_HANDLE.
    이름은 대소문자까지 그대로, 같은 이름 둘은 안 됨(CAD_E_DUPLICATE). 도면층 표 바꾸기는 되돌리기에 안 남는다(오토캐드 도면층 관리자처럼).
    빈 이름 CAD_E_INVALID_ARG
    """
    outLayerId = _c.c_uint32()
    _r = _f.CAD_CreateLayer(_n.text(name), _c.byref(outLayerId))
    return (_r, outLayerId.value)


def CAD_SetLayerColor(id: int, color: CAD_Color) -> int:
    """C: CAD_Status CAD_SetLayerColor(uint32_t id, CAD_Color color)

    색 0~1(범위 밖 CAD_E_OUT_OF_RANGE) — 색을 '도면층을 따름' 인 객체가 이 색으로 그려진다
    """
    return _f.CAD_SetLayerColor(id, color)


def CAD_GetLayerColor(id: int) -> tuple[int, CAD_Color]:
    """C: CAD_Status CAD_GetLayerColor(uint32_t id, CAD_Color* outColor)

    색 0~1(범위 밖 CAD_E_OUT_OF_RANGE) — 색을 '도면층을 따름' 인 객체가 이 색으로 그려진다
    """
    outColor = CAD_Color()
    _r = _f.CAD_GetLayerColor(id, _c.byref(outColor))
    return (_r, outColor)


def CAD_SetLayerOpacity(id: int, opacity: float) -> int:
    """C: CAD_Status CAD_SetLayerOpacity(uint32_t id, double opacity)

    불투명도 0~1 — 객체 불투명도와 곱해진다
    """
    return _f.CAD_SetLayerOpacity(id, opacity)


def CAD_GetLayerOpacity(id: int) -> tuple[int, float]:
    """C: CAD_Status CAD_GetLayerOpacity(uint32_t id, double* outOpacity)

    불투명도 0~1 — 객체 불투명도와 곱해진다
    """
    outOpacity = _c.c_double()
    _r = _f.CAD_GetLayerOpacity(id, _c.byref(outOpacity))
    return (_r, outOpacity.value)


def CAD_GetLayerIds(outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_GetLayerIds(uint32_t* outIds, uint32_t capacity)

    도면층 id 들(0 이 맨 앞) — 칸만큼 채우고 전체 개수
    """
    return _f.CAD_GetLayerIds(outIds, capacity)


def CAD_GetLayerName(id: int) -> str | None:
    """C: int32_t CAD_GetLayerName(uint32_t id, char* buf, uint32_t capacity)

    도면층 id 들(0 이 맨 앞) — 칸만큼 채우고 전체 개수
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


def CAD_RenameLayer(id: int, name: str | None) -> int:
    """C: CAD_Status CAD_RenameLayer(uint32_t id, const char* name)

    도면층 id 들(0 이 맨 앞) — 칸만큼 채우고 전체 개수
    """
    return _f.CAD_RenameLayer(id, _n.text(name))


def CAD_SetLayerVisible(id: int, visible: bool) -> int:
    """C: CAD_Status CAD_SetLayerVisible(uint32_t id, bool visible)

    끄면 그 도면층 객체가 안 보이고 고를 수 없다 · 잠그면 보이지만 못 고친다(고를 수도 없다). 그립을 끄는 중 CAD_E_BUSY
    """
    return _f.CAD_SetLayerVisible(id, visible)


def CAD_IsLayerVisible(id: int) -> tuple[int, bool]:
    """C: CAD_Status CAD_IsLayerVisible(uint32_t id, bool* outVisible)

    끄면 그 도면층 객체가 안 보이고 고를 수 없다 · 잠그면 보이지만 못 고친다(고를 수도 없다). 그립을 끄는 중 CAD_E_BUSY
    """
    outVisible = _c.c_bool()
    _r = _f.CAD_IsLayerVisible(id, _c.byref(outVisible))
    return (_r, outVisible.value)


def CAD_SetLayerLocked(id: int, locked: bool) -> int:
    """C: CAD_Status CAD_SetLayerLocked(uint32_t id, bool locked)

    끄면 그 도면층 객체가 안 보이고 고를 수 없다 · 잠그면 보이지만 못 고친다(고를 수도 없다). 그립을 끄는 중 CAD_E_BUSY
    """
    return _f.CAD_SetLayerLocked(id, locked)


def CAD_IsLayerLocked(id: int) -> tuple[int, bool]:
    """C: CAD_Status CAD_IsLayerLocked(uint32_t id, bool* outLocked)

    끄면 그 도면층 객체가 안 보이고 고를 수 없다 · 잠그면 보이지만 못 고친다(고를 수도 없다). 그립을 끄는 중 CAD_E_BUSY
    """
    outLocked = _c.c_bool()
    _r = _f.CAD_IsLayerLocked(id, _c.byref(outLocked))
    return (_r, outLocked.value)


def CAD_CreateLinetype(name: str | None, pattern: Sequence | None, count: int, description: str | None) -> tuple[int, int]:
    """C: CAD_Status CAD_CreateLinetype(const char* name, const double* pattern, uint32_t count, const char* description, uint32_t* outLinetypeId)

    사용자 선종류 추가 — 요소 1~8개(범위 밖 CAD_E_OUT_OF_RANGE), 선(양수 또는 0 = 점)이 하나는 있어야 한다(CAD_E_INVALID_ARG),
    같은 이름 CAD_E_DUPLICATE. 문자·도형이 든 복합 선종류는 명령 ltnew·ltload(.lin 문법).
    """
    _a_pattern = _n.array(_c.c_double, pattern)
    outLinetypeId = _c.c_uint32()
    _r = _f.CAD_CreateLinetype(_n.text(name), _a_pattern, count, _n.text(description), _c.byref(outLinetypeId))
    return (_r, outLinetypeId.value)


def CAD_GetLinetypeIds(outIds: Any, capacity: int) -> int:
    """C: int32_t CAD_GetLinetypeIds(uint32_t* outIds, uint32_t capacity)

    칸만큼 채우고 전체 개수, 0(Continuous) 포함

    묶음 주석: 사용자 선종류 추가 — 요소 1~8개(범위 밖 CAD_E_OUT_OF_RANGE), 선(양수 또는 0 = 점)이 하나는 있어야 한다(CAD_E_INVALID_ARG),
    같은 이름 CAD_E_DUPLICATE. 문자·도형이 든 복합 선종류는 명령 ltnew·ltload(.lin 문법).
    """
    return _f.CAD_GetLinetypeIds(outIds, capacity)


def CAD_GetLinetypeName(id: int) -> str | None:
    """C: int32_t CAD_GetLinetypeName(uint32_t id, char* buf, uint32_t capacity)

    없는 id CAD_E_BAD_HANDLE

    묶음 주석: 사용자 선종류 추가 — 요소 1~8개(범위 밖 CAD_E_OUT_OF_RANGE), 선(양수 또는 0 = 점)이 하나는 있어야 한다(CAD_E_INVALID_ARG),
    같은 이름 CAD_E_DUPLICATE. 문자·도형이 든 복합 선종류는 명령 ltnew·ltload(.lin 문법).
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


def CAD_GetLinetypePattern(id: int, outPattern: Any, capacity: int) -> int:
    """C: int32_t CAD_GetLinetypePattern(uint32_t id, double* outPattern, uint32_t capacity)

    요소 수(실선 0)

    묶음 주석: 사용자 선종류 추가 — 요소 1~8개(범위 밖 CAD_E_OUT_OF_RANGE), 선(양수 또는 0 = 점)이 하나는 있어야 한다(CAD_E_INVALID_ARG),
    같은 이름 CAD_E_DUPLICATE. 문자·도형이 든 복합 선종류는 명령 ltnew·ltload(.lin 문법).
    """
    return _f.CAD_GetLinetypePattern(id, outPattern, capacity)


def CAD_SetObjectLinetype(ids: Sequence | None, count: int, linetypeId: int) -> tuple[int, int]:
    """C: CAD_Status CAD_SetObjectLinetype(const uint32_t* ids, uint32_t count, uint32_t linetypeId, uint32_t* outChanged)

    객체 선종류 — 여럿 한 번에(되돌리기 1, 하나라도 없음·잠김이면 아무것도 안 바꿈), linetypeId = CAD_LINETYPE_BYLAYER·0(실선)·표에 있는 id
    (없는 선종류 CAD_E_BAD_HANDLE). *outChanged = 실제로 바뀐 수(NULL 가능). 메시·문자·치수엔 안 보인다
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    outChanged = _c.c_uint32()
    _r = _f.CAD_SetObjectLinetype(_a_ids, count, linetypeId, _c.byref(outChanged))
    return (_r, outChanged.value)


def CAD_GetObjectLinetype(objectId: int) -> tuple[int, int]:
    """C: CAD_Status CAD_GetObjectLinetype(uint32_t objectId, uint32_t* outLinetypeId)

    객체 선종류 — 여럿 한 번에(되돌리기 1, 하나라도 없음·잠김이면 아무것도 안 바꿈), linetypeId = CAD_LINETYPE_BYLAYER·0(실선)·표에 있는 id
    (없는 선종류 CAD_E_BAD_HANDLE). *outChanged = 실제로 바뀐 수(NULL 가능). 메시·문자·치수엔 안 보인다
    """
    outLinetypeId = _c.c_uint32()
    _r = _f.CAD_GetObjectLinetype(objectId, _c.byref(outLinetypeId))
    return (_r, outLinetypeId.value)


def CAD_SetObjectLinetypeScale(objectId: int, scale: float) -> int:
    """C: CAD_Status CAD_SetObjectLinetypeScale(uint32_t objectId, double scale)

    객체별 축척(CELTSCALE, > 0) — 되돌리기 1

    묶음 주석: 객체 선종류 — 여럿 한 번에(되돌리기 1, 하나라도 없음·잠김이면 아무것도 안 바꿈), linetypeId = CAD_LINETYPE_BYLAYER·0(실선)·표에 있는 id
    (없는 선종류 CAD_E_BAD_HANDLE). *outChanged = 실제로 바뀐 수(NULL 가능). 메시·문자·치수엔 안 보인다
    """
    return _f.CAD_SetObjectLinetypeScale(objectId, scale)


def CAD_GetObjectLinetypeScale(objectId: int) -> tuple[int, float]:
    """C: CAD_Status CAD_GetObjectLinetypeScale(uint32_t objectId, double* outScale)

    객체 선종류 — 여럿 한 번에(되돌리기 1, 하나라도 없음·잠김이면 아무것도 안 바꿈), linetypeId = CAD_LINETYPE_BYLAYER·0(실선)·표에 있는 id
    (없는 선종류 CAD_E_BAD_HANDLE). *outChanged = 실제로 바뀐 수(NULL 가능). 메시·문자·치수엔 안 보인다
    """
    outScale = _c.c_double()
    _r = _f.CAD_GetObjectLinetypeScale(objectId, _c.byref(outScale))
    return (_r, outScale.value)


def CAD_SetLayerLinetype(layerId: int, linetypeId: int) -> int:
    """C: CAD_Status CAD_SetLayerLinetype(uint32_t layerId, uint32_t linetypeId)

    ByLayer 는 안 됨, 도면층 0 은 실선 고정

    묶음 주석: 객체 선종류 — 여럿 한 번에(되돌리기 1, 하나라도 없음·잠김이면 아무것도 안 바꿈), linetypeId = CAD_LINETYPE_BYLAYER·0(실선)·표에 있는 id
    (없는 선종류 CAD_E_BAD_HANDLE). *outChanged = 실제로 바뀐 수(NULL 가능). 메시·문자·치수엔 안 보인다
    """
    return _f.CAD_SetLayerLinetype(layerId, linetypeId)


def CAD_GetLayerLinetype(layerId: int) -> tuple[int, int]:
    """C: CAD_Status CAD_GetLayerLinetype(uint32_t layerId, uint32_t* outLinetypeId)

    객체 선종류 — 여럿 한 번에(되돌리기 1, 하나라도 없음·잠김이면 아무것도 안 바꿈), linetypeId = CAD_LINETYPE_BYLAYER·0(실선)·표에 있는 id
    (없는 선종류 CAD_E_BAD_HANDLE). *outChanged = 실제로 바뀐 수(NULL 가능). 메시·문자·치수엔 안 보인다
    """
    outLinetypeId = _c.c_uint32()
    _r = _f.CAD_GetLayerLinetype(layerId, _c.byref(outLinetypeId))
    return (_r, outLinetypeId.value)


def CAD_SetLinetypeScale(scale: float) -> int:
    """C: CAD_Status CAD_SetLinetypeScale(double scale)

    전역 LTSCALE(> 0)

    묶음 주석: 객체 선종류 — 여럿 한 번에(되돌리기 1, 하나라도 없음·잠김이면 아무것도 안 바꿈), linetypeId = CAD_LINETYPE_BYLAYER·0(실선)·표에 있는 id
    (없는 선종류 CAD_E_BAD_HANDLE). *outChanged = 실제로 바뀐 수(NULL 가능). 메시·문자·치수엔 안 보인다
    """
    return _f.CAD_SetLinetypeScale(scale)


def CAD_GetLinetypeScale() -> tuple[int, float]:
    """C: CAD_Status CAD_GetLinetypeScale(double* outScale)

    객체 선종류 — 여럿 한 번에(되돌리기 1, 하나라도 없음·잠김이면 아무것도 안 바꿈), linetypeId = CAD_LINETYPE_BYLAYER·0(실선)·표에 있는 id
    (없는 선종류 CAD_E_BAD_HANDLE). *outChanged = 실제로 바뀐 수(NULL 가능). 메시·문자·치수엔 안 보인다
    """
    outScale = _c.c_double()
    _r = _f.CAD_GetLinetypeScale(_c.byref(outScale))
    return (_r, outScale.value)


def CAD_SaveAs(pathUtf8: str | None, selectedOnly: bool) -> int:
    """C: CAD_Status CAD_SaveAs(const char* pathUtf8, bool selectedOnly)

    저장 / 내보내기 / 가져오기
    확장자로 갈린다 — 엔진 안의 분기(saveByExtension / loadModelFromPath) 그대로라 호스트가 포맷을 판별할 필요가 없고,
    새 포맷이 붙어도 API 는 그대로다. 대화상자를 띄우지 않으므로 경로는 호스트가 정한다(UTF-8). 파일 창은 CAD_OpenFileDialog.

    CAD_SaveAs  : .lot(프로젝트 — 씬 전체: 선·솔리드·로봇·점군·문서 상태) · .dxf · .dwg(2018) · .stl · .obj · .glb/.gltf(내보내기).
                  selectedOnly = 선택한 것만(선택이 비었으면 CAD_E_NOT_FOUND). 모르는 확장자·못 씀 = CAD_E_FAILED + 이유
    CAD_OpenFile: .lot · .dxf · .dwg · .obj · .stl · .ply(점군) · .gltf/.glb · .fbx(정적 메시) · .nrrd/.nii(볼륨) …
                  **현재 문서에 더한다**(새 탭으로 열려면 CAD_OpenDocument). 없는 파일 CAD_E_NOT_FOUND · 못 읽음 CAD_E_FAILED + 이유.
    이유 글은 CAD_GetLastError (예전엔 bool + CAD_GetTransientMessage). 예전 CAD_ExportFile·CAD_ExportObj 는 이것과 같은 길이라 지웠다.
    """
    return _f.CAD_SaveAs(_n.text(pathUtf8), selectedOnly)


def CAD_OpenFile(pathUtf8: str | None) -> int:
    """C: CAD_Status CAD_OpenFile(const char* pathUtf8)

    저장 / 내보내기 / 가져오기
    확장자로 갈린다 — 엔진 안의 분기(saveByExtension / loadModelFromPath) 그대로라 호스트가 포맷을 판별할 필요가 없고,
    새 포맷이 붙어도 API 는 그대로다. 대화상자를 띄우지 않으므로 경로는 호스트가 정한다(UTF-8). 파일 창은 CAD_OpenFileDialog.

    CAD_SaveAs  : .lot(프로젝트 — 씬 전체: 선·솔리드·로봇·점군·문서 상태) · .dxf · .dwg(2018) · .stl · .obj · .glb/.gltf(내보내기).
                  selectedOnly = 선택한 것만(선택이 비었으면 CAD_E_NOT_FOUND). 모르는 확장자·못 씀 = CAD_E_FAILED + 이유
    CAD_OpenFile: .lot · .dxf · .dwg · .obj · .stl · .ply(점군) · .gltf/.glb · .fbx(정적 메시) · .nrrd/.nii(볼륨) …
                  **현재 문서에 더한다**(새 탭으로 열려면 CAD_OpenDocument). 없는 파일 CAD_E_NOT_FOUND · 못 읽음 CAD_E_FAILED + 이유.
    이유 글은 CAD_GetLastError (예전엔 bool + CAD_GetTransientMessage). 예전 CAD_ExportFile·CAD_ExportObj 는 이것과 같은 길이라 지웠다.
    """
    return _f.CAD_OpenFile(_n.text(pathUtf8))


def CAD_Undo() -> int:
    """C: CAD_Status CAD_Undo(void)

    되돌리기 ── 되돌릴(다시 할) 것이 없으면 CAD_E_NOT_READY · 트랜잭션이 열려 있으면 CAD_E_BUSY
    """
    return _f.CAD_Undo()


def CAD_Redo() -> int:
    """C: CAD_Status CAD_Redo(void)

    되돌리기 ── 되돌릴(다시 할) 것이 없으면 CAD_E_NOT_READY · 트랜잭션이 열려 있으면 CAD_E_BUSY
    """
    return _f.CAD_Redo()


def CAD_CanUndo() -> tuple[int, bool]:
    """C: CAD_Status CAD_CanUndo(bool* outCan)

    되돌리기 ── 되돌릴(다시 할) 것이 없으면 CAD_E_NOT_READY · 트랜잭션이 열려 있으면 CAD_E_BUSY
    """
    outCan = _c.c_bool()
    _r = _f.CAD_CanUndo(_c.byref(outCan))
    return (_r, outCan.value)


def CAD_CanRedo() -> tuple[int, bool]:
    """C: CAD_Status CAD_CanRedo(bool* outCan)

    되돌리기 ── 되돌릴(다시 할) 것이 없으면 CAD_E_NOT_READY · 트랜잭션이 열려 있으면 CAD_E_BUSY
    """
    outCan = _c.c_bool()
    _r = _f.CAD_CanRedo(_c.byref(outCan))
    return (_r, outCan.value)
