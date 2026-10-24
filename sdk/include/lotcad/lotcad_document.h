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
// 여러 파일을 동시에 열고 탭으로 전환한다. 호스트(WPF/Qt)가 **자기 탭 UI** 를 그릴 수 있도록
// 목록 조회 + 전환/열기/닫기를 모두 노출한다. 전환은 상태 swap 이라 비용이 거의 없다.
CAD_API int  CAD_GetDocumentCount(void);
CAD_API int  CAD_GetActiveDocument(void);
// 탭 라벨용 — 표시 이름(파일명 또는 "제목 없음"). 길이 반환, -1=실패. buf 는 null 허용(길이만 조회).
CAD_API int  CAD_GetDocumentTitle(int index, char* outUtf8, int cap);
CAD_API int  CAD_GetDocumentPath (int index, char* outUtf8, int cap);
// 저장되지 않은 변경이 있는지 — 탭에 * 표시하거나 닫기 확인에 사용.
CAD_API bool CAD_IsDocumentDirty(int index);
// 새 빈 문서 추가 후 활성화. 반환 = 새 문서 인덱스.
CAD_API int  CAD_NewDocument(const char* titleUtf8);
// 파일을 새 탭으로 열기. 반환 = 문서 인덱스, 실패 -1.
CAD_API int  CAD_OpenDocument(const char* pathUtf8);
CAD_API bool CAD_ActivateDocument(int index);
// 닫기 — 마지막 문서는 닫지 않고 내용을 비운다(항상 문서 1개 유지).
CAD_API bool CAD_CloseDocument(int index);

/* 트랜잭션 — 여러 편집(생성·속성·삭제·이동…)을 되돌리기 **한 단계** 로 묶는다.
 * Begin … End 사이의 CAD_Create·Set·Delete·SetObjectProperty 는 실행은 즉시 되고, End 에서 한 묶음으로
 * undo 스택에 오른다(Ctrl+Z 한 번). Rollback 은 묶음을 되돌리고 버린다(미리보기 거절). 중첩 가능(깊이 셈).
 * 열린 동안 CAD_Undo/Redo 는 false. name 은 UI 의 되돌리기 이름. */
CAD_API void     CAD_BeginTransaction(const char* name);
CAD_API bool     CAD_EndTransaction(void);
CAD_API bool     CAD_RollbackTransaction(void);
CAD_API int      CAD_TransactionDepth(void);

// ── 노드 트리·도면층 창 — ImGui 패널이 안 뜨는 호스트(WinForms·WPF·Qt·모바일)가 자기 트리·목록을 그릴 때 ──
// 장면이 바뀔 때마다(객체 추가·삭제·이름·보이기·도면층 …) 커지는 번호 — 같으면 다시 안 읽어도 된다(폴링용).
CAD_API uint64_t CAD_GetSceneRevision(void);
// 노드 트리 — 엔진 패널과 같은 구성(파일 → glTF/FBX 노드 계층 → 객체 → 피처·가공 기록). 평평한 배열 + 부모 번호:
// {"revision","nodes":[{"index","key","kind":"scene|file|node|object|feature","label","parent"(-1 = 뿌리),"depth","children":[…],
//   "total","shown"(아래 객체 수·보이는 수),  객체 줄만: "objectId"(1 이상),"objectKind","visible","selected","locked"(bool),"layerId","layer"}]}
//   objectKind = 문자열, CAD_GetObjectJson 의 "kind" 와 같다: "mesh" "line" "polyline" "circle" "arc" "text" "dimension"
//   "pointcloud" "particle" "effect" "hatch" "insert"(블록 참조) (모르는 종류 "unknown"). 객체 id 는 늘 1 이상(0 = 없음/실패).
// 클릭·보이기·이름 바꾸기는 기존 함수로: CAD_SelectObject · CAD_SetObjectVisible · CAD_SetObjectName(묶음 줄은 children 의 objectId 들).
CAD_API int      CAD_GetSceneTreeJson(char* out, int cap);
// 도면층 창 — 한 번에: {"revision","layers":[{"id","name","visible","locked","color":[r,g,b],"opacity","linetypeId","linetype",
//   "objectCount","selectedCount"(,"fixed":true — 도면층 0)}]}. 바꾸기는 기존 CAD_SetLayer*·CAD_RenameLayer·CAD_CreateLayer·CAD_AssignSelectedToLayer.
CAD_API int      CAD_GetLayersJson(char* out, int cap);
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

// Document layers. 0 is the always-visible, unlocked default layer.
CAD_API uint32_t CAD_CreateLayer(const char* name);
// RGB in [0,1]. Layer 0 has fixed white ByLayer color.
CAD_API bool CAD_SetLayerColor(uint32_t id,float r,float g,float b);
CAD_API bool CAD_GetLayerColor(uint32_t id,float* r,float* g,float* b);

CAD_API bool  CAD_SetLayerOpacity(uint32_t id, float opacity);
CAD_API float CAD_GetLayerOpacity(uint32_t id);

CAD_API uint32_t CAD_GetLayerIds(uint32_t* out, uint32_t capacity); // required count, includes 0
CAD_API int CAD_GetLayerName(uint32_t id, char* out, int capacity);
CAD_API bool CAD_RenameLayer(uint32_t id, const char* name);
CAD_API bool CAD_SetLayerVisible(uint32_t id, bool visible);
CAD_API bool CAD_IsLayerVisible(uint32_t id);
CAD_API bool CAD_SetLayerLocked(uint32_t id, bool locked);
CAD_API bool CAD_IsLayerLocked(uint32_t id);

// ── 선종류 (파선·숨은선·중심선…) ──
// AutoCAD .lin 규칙: 무늬 요소 양수=선, 음수=빈칸, 0=점. 단위는 도면 단위(m).
// id 0 = Continuous(실선, 항상 있음). 표준 8종은 id 1..8 로 고정:
//   1 Dashed  2 Hidden  3 Center  4 Phantom  5 Dot  6 DashDot  7 Divide  8 Border
// 사용자 정의는 100 부터. 객체 값 CAD_LINETYPE_BYLAYER = 도면층 것을 따른다(기본).
// 선·폴리선·원·호에만 보인다 — 메시·문자·치수는 항상 실선.
#define CAD_LINETYPE_BYLAYER 0xFFFFFFFFu
// 사용자 선종류 추가. 요소 1..8개, 선(양수 또는 점)이 하나는 있어야 한다. 실패 0.
CAD_API uint32_t CAD_CreateLinetype(const char* name, const float* pattern, int count, const char* description);
CAD_API uint32_t CAD_GetLinetypeIds(uint32_t* out, uint32_t capacity);        // 필요한 개수, 0(Continuous) 포함
CAD_API int      CAD_GetLinetypeName(uint32_t id, char* out, int capacity);   // 이름 길이, 없으면 -1
CAD_API int      CAD_GetLinetypePattern(uint32_t id, float* out, int capacity); // 요소 수, 없으면 -1
CAD_API bool     CAD_SetObjectLinetype(uint32_t objectId, uint32_t linetypeId);  // CAD_LINETYPE_BYLAYER 허용
CAD_API bool     CAD_GetObjectLinetype(uint32_t objectId, uint32_t* out);
CAD_API bool     CAD_SetObjectLinetypeScale(uint32_t objectId, float scale);     // 객체별 축척(CELTSCALE)
CAD_API bool     CAD_GetObjectLinetypeScale(uint32_t objectId, float* out);
CAD_API uint32_t CAD_SetSelectedLinetype(uint32_t linetypeId);                  // 바뀐 객체 수
CAD_API bool     CAD_SetLayerLinetype(uint32_t layerId, uint32_t linetypeId);   // 도면층 0 은 실선 고정
CAD_API bool     CAD_GetLayerLinetype(uint32_t layerId, uint32_t* out);
CAD_API bool     CAD_SetLinetypeScale(float scale);                              // 전역 LTSCALE
CAD_API float    CAD_GetLinetypeScale(void);

/* ── 내보내기 ─────────────────────────────────────────────────────────────
 *
 * **확장자로 포맷이 정해진다** — .stl .dxf .glb .obj .lot
 * 전에는 CAD_ExportObj 하나뿐이라 나머지 포맷을 호스트에서 쓸 수가 없었다.
 * selectedOnly=true 면 선택된 것만(선택이 비었으면 실패).
 * 대화상자를 띄우지 않으므로 경로는 호스트가 정한다.
 */
CAD_API bool     CAD_ExportFile(const char* path, bool selectedOnly);

// ── 내보내기 (Export) ──
// selectedOnly=false → 씬 전체, true → 선택 객체만. 월드 좌표로 baking. 성공 시 true.
CAD_API bool CAD_ExportObj(const char* path, bool selectedOnly);

// ── 저장 / 내보내기 / 가져오기 ──────────────────────────────────────────
// 확장자로 갈린다. 엔진 안의 분기(saveByExtension / loadModelFromPath)를 그대로 쓴다 —
// 호스트가 포맷을 판별해 다른 함수를 고를 필요가 없고, 새 포맷이 붙어도 API 는 그대로다.
//
// CAD_SaveAs  : .lot(프로젝트) · .stl · .dxf · .obj · .glb/.gltf
//               .lot 은 씬 전체(선·솔리드·로봇·문서 상태)를 담는 네이티브 형식이고,
//               나머지는 내보내기다. selectedOnly=true 면 선택 객체만.
//               점군도 .lot 에 담긴다(2026-09 부터). 다만 파일이 커진다 — 점당 21.3B.
// CAD_OpenFile: .lot · .obj · .stl · .dxf · .ply(점군) · .gltf/.glb · .fbx (static meshes)
//               **현재 문서에 추가**한다(새 탭을 만들지 않음). 새 탭으로 열려면
//               CAD_OpenDocument 를 쓴다.
//
// 둘 다 실패 시 false 를 반환하고 사유는 CAD_GetStatusMessage 로 읽는다.
CAD_API bool CAD_SaveAs(const char* pathUtf8, bool selectedOnly);
CAD_API bool CAD_OpenFile(const char* pathUtf8);

// ── Undo / Redo ──
CAD_API void CAD_Undo(void);
CAD_API void CAD_Redo(void);
CAD_API bool CAD_CanUndo(void);
CAD_API bool CAD_CanRedo(void);

#ifdef __cplusplus
}
#endif
