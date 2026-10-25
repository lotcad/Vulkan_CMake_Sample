#pragma once
/* LotCAD C API - document  [AcDbDatabase / AcApDocManager / symbol tables]
 * Documents, open/save, transactions, undo, layers, linetypes, blocks, xrefs, scene tree.
 * 문서·열기/저장·트랜잭션·되돌리기·도면층·선종류·블록·외부 참조·노드 트리.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif
// ── 문서 탭 (멀티 문서) ──────────────────────────────────────────────
// 여러 파일을 동시에 열고 탭으로 전환한다(ObjectARX AcApDocManager 자리). 호스트(WPF/Qt)가 **자기 탭 UI** 를 그릴 수 있도록
// 목록 조회 + 전환/열기/닫기를 모두 노출한다. 전환은 상태 swap 이라 비용이 거의 없다. 문서는 번호(0 ~ 개수 − 1)로 —
// 닫으면 뒤 번호가 하나씩 당겨진다. 범위 밖 번호 CAD_E_OUT_OF_RANGE. 엔진 스레드에서만.
CAD_API int32_t    CAD_GetDocumentCount(void);
CAD_API int32_t    CAD_GetActiveDocument(void);   /* 지금 문서 번호 */
// 탭 라벨용 — 표시 이름(파일명 또는 "제목 없음") · 파일 경로(저장 전이면 ""). 반환 = 전체 길이, 칸이 모자라면 글자 경계에서 자름
CAD_API int32_t    CAD_GetDocumentTitle(int32_t index, char* buf, uint32_t capacity);
CAD_API int32_t    CAD_GetDocumentPath(int32_t index, char* buf, uint32_t capacity);
// 저장되지 않은 변경이 있는지 — 탭에 * 표시하거나 닫기 확인에 사용.
CAD_API CAD_Status CAD_IsDocumentDirty(int32_t index, bool* outDirty);
// 새 빈 문서 추가 후 활성화(title NULL = "제목 없음"). *outIndex = 새 문서 번호(NULL 가능)
CAD_API CAD_Status CAD_NewDocument(const char* titleUtf8, int32_t* outIndex);
// 파일을 새 탭으로 열기(현재 문서에 더하려면 CAD_OpenFile). 없는 파일 CAD_E_NOT_FOUND · 못 읽음 CAD_E_FAILED(+ 이유)
CAD_API CAD_Status CAD_OpenDocument(const char* pathUtf8, int32_t* outIndex);
// 전환(이미 그 문서면 그냥 CAD_OK). 블록 편집 탭이 열린 동안 원래 도면은 CAD_E_LOCKED. 진행 중인 명령은 끝낸다(CAD_CancelCommand 와 같다)
CAD_API CAD_Status CAD_ActivateDocument(int32_t index);
// 닫기 — 마지막 문서는 닫지 않고 내용을 비운다(항상 문서 1개 유지). 저장 안 한 변경은 묻지 않고 버린다(먼저 CAD_IsDocumentDirty)
CAD_API CAD_Status CAD_CloseDocument(int32_t index);

/* 트랜잭션 — 여러 편집(생성·속성·삭제·이동…)을 되돌리기 **한 단계** 로 묶는다.
 * Begin … End 사이의 CAD_Create·Set·Delete·SetObjectProperty 는 실행은 즉시 되고, End 에서 한 묶음으로
 * undo 스택에 오른다(Ctrl+Z 한 번). Rollback 은 묶음을 되돌리고 버린다(미리보기 거절). 중첩 가능(깊이 셈).
 * 열린 동안 CAD_Undo/Redo 는 CAD_E_BUSY. name 은 UI 의 되돌리기 이름(NULL·"" = "묶음 편집"). 열린 묶음이 없는데 End·Rollback = CAD_E_NOT_READY */
CAD_API CAD_Status CAD_BeginTransaction(const char* name);
CAD_API CAD_Status CAD_EndTransaction(void);
CAD_API CAD_Status CAD_RollbackTransaction(void);
CAD_API int32_t    CAD_TransactionDepth(void);   /* 열린 묶음 깊이(0 = 없음) */

// ── 노드 트리·도면층 창 — ImGui 패널이 안 뜨는 호스트(WinForms·WPF·Qt·모바일)가 자기 트리·목록을 그릴 때 ──
// 장면이 바뀔 때마다(객체 추가·삭제·이름·보이기·도면층 …) 커지는 번호 — 같으면 다시 안 읽어도 된다(폴링용).
CAD_API CAD_Status CAD_GetSceneRevision(uint64_t* outRevision);
// 노드 트리 — 엔진 패널과 같은 구성(파일 → glTF/FBX 노드 계층 → 객체 → 피처·가공 기록). 평평한 배열 + 부모 번호:
// {"revision","nodes":[{"index","key","kind":"scene|file|node|object|feature","label","parent"(-1 = 뿌리),"depth","children":[…],
//   "total","shown"(아래 객체 수·보이는 수),  객체 줄만: "objectId"(1 이상),"objectKind","visible","selected","locked"(bool),"layerId","layer"}]}
//   objectKind = 문자열, CAD_GetObjectJson 의 "kind" 와 같다: "mesh" "line" "polyline" "circle" "arc" "text" "dimension"
//   "pointcloud" "particle" "effect" "hatch" "insert"(블록 참조) (모르는 종류 "unknown"). 객체 id 는 늘 1 이상(0 = 없음/실패).
// 클릭·보이기·이름 바꾸기는 기존 함수로: CAD_SetSelection · CAD_SetObjectVisible · CAD_SetObjectName(묶음 줄은 children 의 objectId 들).
CAD_API int32_t    CAD_GetSceneTreeJson(char* buf, uint32_t capacity);
// 도면층 창 — 한 번에: {"revision","layers":[{"id","name","visible","locked","color":[r,g,b],"opacity","linetypeId","linetype",
//   "objectCount","selectedCount"(,"fixed":true — 도면층 0)}]}. 바꾸기는 CAD_SetLayer*·CAD_RenameLayer·CAD_CreateLayer·CAD_SetObjectLayer.
CAD_API int32_t    CAD_GetLayersJson(char* buf, uint32_t capacity);
// 블록(블록 참조 — docs/BLOCKS_2026-10-12.md). 정의 표 한 번에: {"blocks":[{"name","objects","references"(장면에 넣은 수),
//   "base":[x,y,z],"bounds":{"min","max"}(있으면),"xref"(외부 참조 경로, 있으면)}]}. 블록 편집은 명령으로: CAD_ExecuteCommand("bedit 이름") ·
//   "bsave" · "bclose save|discard" · "bbase x,y" (탭을 여닫으므로 다음 CAD_Tick 에 처리된다).
CAD_API int      CAD_GetBlocksJson(char* out, int cap);
// 객체들로 새 블록 정의 + 그 자리(층 "0")에 INSERT 하나 — 명령 block 과 같다, 되돌리기 1. 반환 = 새 INSERT id(0 = 실패, 이유는 CAD_GetLastError)
CAD_API uint32_t CAD_CreateBlock(const char* nameUtf8, const uint32_t* ids, int count, float baseX, float baseY, float baseZ);
// 블록 참조의 속성 글 값 — JSON 문자열 배열(속성 글 id 순). Get: 반환 = 길이, 블록 참조가 아니면 -1.
// Set: 같은 개수의 배열 — 그 INSERT 만 바뀐다(복사한 INSERT 와 같이 쓰던 묶음은 사본으로), 되돌리기 1. 실패면 false + CAD_GetLastError
CAD_API int      CAD_GetInsertAttributesJson(uint32_t id, char* out, int cap);
CAD_API bool     CAD_SetInsertAttributesJson(uint32_t id, const char* jsonArray);
// 외부 참조(XREF — 정의 표에서 "xref" 가 있는 블록, ObjectARX acedXrefReload·acedXrefBind·acedXrefDetach·setPathName). 목록·경로·찾음 여부는
// CAD_GetBlocksJson 의 "xref"(적힌 경로)·"xrefFound"(읽은 파일)·"xrefLoaded". 명령 xref 와 같고 전부 되돌리기 1, 실패 false + CAD_GetLastError.
//   Reload : 그 파일을 다시 읽어 정의를 바꾼다(그 INSERT 들이 따라 바뀜)
//   SetPath: pathOrKind = "absolute" | "relative" | "none"(파일 이름만) 이면 경로 모양만(상대는 도면을 저장한 뒤),
//            그 밖은 새 경로 — 적고 그 파일로 다시 읽는다(옮긴 파일 다시 찾기)
//   Bind   : 보통 블록으로 굳힘 — 딸린 이름 "SITE|문" → "SITE$0$문"(블록·도면층·선종류)
//   Detach : 그 INSERT·정의를 지움(다른 블록 안에 들어 있으면 거부)
// 저장(.lot·DXF·DWG)엔 경로만 쓰고 열 때 다시 읽는다 — 상대 경로는 저장 자리 기준으로 다시 맞춘다.
CAD_API bool     CAD_XrefReload(const char* nameUtf8);
CAD_API bool     CAD_XrefSetPath(const char* nameUtf8, const char* pathOrKindUtf8);
CAD_API bool     CAD_XrefBind(const char* nameUtf8);
CAD_API bool     CAD_XrefDetach(const char* nameUtf8);

/* ── 도면층 (ObjectARX AcDbLayerTable 자리) — 지금 문서의 표 ──
 * id 0 = 도면층 "0"(늘 있음, 늘 보이고 안 잠김, 흰색·실선·불투명 고정 — 바꾸려 하면 CAD_E_NOT_SUPPORTED). 없는 id CAD_E_BAD_HANDLE.
 * 이름은 대소문자까지 그대로, 같은 이름 둘은 안 됨(CAD_E_DUPLICATE). 도면층 표 바꾸기는 되돌리기에 안 남는다(오토캐드 도면층 관리자처럼). */
CAD_API CAD_Status CAD_CreateLayer(const char* name, uint32_t* outLayerId);   /* 빈 이름 CAD_E_INVALID_ARG */
/* 색 0~1(범위 밖 CAD_E_OUT_OF_RANGE) — 색을 '도면층을 따름' 인 객체가 이 색으로 그려진다 */
CAD_API CAD_Status CAD_SetLayerColor(uint32_t id, CAD_Color color);
CAD_API CAD_Status CAD_GetLayerColor(uint32_t id, CAD_Color* outColor);
/* 불투명도 0~1 — 객체 불투명도와 곱해진다 */
CAD_API CAD_Status CAD_SetLayerOpacity(uint32_t id, double opacity);
CAD_API CAD_Status CAD_GetLayerOpacity(uint32_t id, double* outOpacity);
/* 도면층 id 들(0 이 맨 앞) — 칸만큼 채우고 전체 개수 */
CAD_API int32_t    CAD_GetLayerIds(uint32_t* outIds, uint32_t capacity);
CAD_API int32_t    CAD_GetLayerName(uint32_t id, char* buf, uint32_t capacity);
CAD_API CAD_Status CAD_RenameLayer(uint32_t id, const char* name);
/* 끄면 그 도면층 객체가 안 보이고 고를 수 없다 · 잠그면 보이지만 못 고친다(고를 수도 없다). 그립을 끄는 중 CAD_E_BUSY */
CAD_API CAD_Status CAD_SetLayerVisible(uint32_t id, bool visible);
CAD_API CAD_Status CAD_IsLayerVisible(uint32_t id, bool* outVisible);
CAD_API CAD_Status CAD_SetLayerLocked(uint32_t id, bool locked);
CAD_API CAD_Status CAD_IsLayerLocked(uint32_t id, bool* outLocked);

// ── 선종류 (파선·숨은선·중심선…) ──
// AutoCAD .lin 규칙: 무늬 요소 양수=선, 음수=빈칸, 0=점. 단위는 도면 단위(m).
// id 0 = Continuous(실선, 항상 있음). 표준 8종은 id 1..8 로 고정:
//   1 Dashed  2 Hidden  3 Center  4 Phantom  5 Dot  6 DashDot  7 Divide  8 Border
// 사용자 정의는 100 부터. 객체 값 CAD_LINETYPE_BYLAYER = 도면층 것을 따른다(기본).
// 선·폴리선·원·호에만 보인다 — 메시·문자·치수는 항상 실선.
#define CAD_LINETYPE_BYLAYER 0xFFFFFFFFu
// 사용자 선종류 추가 — 요소 1~8개(범위 밖 CAD_E_OUT_OF_RANGE), 선(양수 또는 0 = 점)이 하나는 있어야 한다(CAD_E_INVALID_ARG),
// 같은 이름 CAD_E_DUPLICATE. 문자·도형이 든 복합 선종류는 명령 ltnew·ltload(.lin 문법).
CAD_API CAD_Status CAD_CreateLinetype(const char* name, const double* pattern, uint32_t count, const char* description, uint32_t* outLinetypeId);
CAD_API int32_t    CAD_GetLinetypeIds(uint32_t* outIds, uint32_t capacity);   /* 칸만큼 채우고 전체 개수, 0(Continuous) 포함 */
CAD_API int32_t    CAD_GetLinetypeName(uint32_t id, char* buf, uint32_t capacity);   /* 없는 id CAD_E_BAD_HANDLE */
CAD_API int32_t    CAD_GetLinetypePattern(uint32_t id, double* outPattern, uint32_t capacity);   /* 요소 수(실선 0) */
// 객체 선종류 — 여럿 한 번에(되돌리기 1, 하나라도 없음·잠김이면 아무것도 안 바꿈), linetypeId = CAD_LINETYPE_BYLAYER·0(실선)·표에 있는 id
// (없는 선종류 CAD_E_BAD_HANDLE). *outChanged = 실제로 바뀐 수(NULL 가능). 메시·문자·치수엔 안 보인다
CAD_API CAD_Status CAD_SetObjectLinetype(const uint32_t* ids, uint32_t count, uint32_t linetypeId, uint32_t* outChanged);
CAD_API CAD_Status CAD_GetObjectLinetype(uint32_t objectId, uint32_t* outLinetypeId);
CAD_API CAD_Status CAD_SetObjectLinetypeScale(uint32_t objectId, double scale);   /* 객체별 축척(CELTSCALE, > 0) — 되돌리기 1 */
CAD_API CAD_Status CAD_GetObjectLinetypeScale(uint32_t objectId, double* outScale);
CAD_API CAD_Status CAD_SetLayerLinetype(uint32_t layerId, uint32_t linetypeId);   /* ByLayer 는 안 됨, 도면층 0 은 실선 고정 */
CAD_API CAD_Status CAD_GetLayerLinetype(uint32_t layerId, uint32_t* outLinetypeId);
CAD_API CAD_Status CAD_SetLinetypeScale(double scale);                             /* 전역 LTSCALE(> 0) */
CAD_API CAD_Status CAD_GetLinetypeScale(double* outScale);

/* ── 저장 / 내보내기 / 가져오기 ──────────────────────────────────────────
 * 확장자로 갈린다 — 엔진 안의 분기(saveByExtension / loadModelFromPath) 그대로라 호스트가 포맷을 판별할 필요가 없고,
 * 새 포맷이 붙어도 API 는 그대로다. 대화상자를 띄우지 않으므로 경로는 호스트가 정한다(UTF-8). 파일 창은 CAD_OpenFileDialog.
 *
 * CAD_SaveAs  : .lot(프로젝트 — 씬 전체: 선·솔리드·로봇·점군·문서 상태) · .dxf · .dwg(2018) · .stl · .obj · .glb/.gltf(내보내기).
 *               selectedOnly = 선택한 것만(선택이 비었으면 CAD_E_NOT_FOUND). 모르는 확장자·못 씀 = CAD_E_FAILED + 이유
 * CAD_OpenFile: .lot · .dxf · .dwg · .obj · .stl · .ply(점군) · .gltf/.glb · .fbx(정적 메시) · .nrrd/.nii(볼륨) …
 *               **현재 문서에 더한다**(새 탭으로 열려면 CAD_OpenDocument). 없는 파일 CAD_E_NOT_FOUND · 못 읽음 CAD_E_FAILED + 이유.
 * 이유 글은 CAD_GetLastError (예전엔 bool + CAD_GetTransientMessage). 예전 CAD_ExportFile·CAD_ExportObj 는 이것과 같은 길이라 지웠다. */
CAD_API CAD_Status CAD_SaveAs(const char* pathUtf8, bool selectedOnly);
CAD_API CAD_Status CAD_OpenFile(const char* pathUtf8);

/* ── 되돌리기 ── 되돌릴(다시 할) 것이 없으면 CAD_E_NOT_READY · 트랜잭션이 열려 있으면 CAD_E_BUSY */
CAD_API CAD_Status CAD_Undo(void);
CAD_API CAD_Status CAD_Redo(void);
CAD_API CAD_Status CAD_CanUndo(bool* outCan);
CAD_API CAD_Status CAD_CanRedo(bool* outCan);

#ifdef __cplusplus
}
#endif
