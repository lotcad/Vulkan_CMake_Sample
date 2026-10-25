#pragma once
/* LotCAD C API - plugin  [(LotCAD plugins)]
 * Plugin loading, UI items, plugin entities (tags), entity properties, plugin panels.
 * 플러그인 올리기·UI 등록·플러그인 객체(딱지)·특성창 속성·플러그인 패널.
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif
/* ── UI 등록 (플러그인) ───────────────────────────────────
 *
 * 플러그인은 UI 를 **직접 그리지 않는다.** (이름, 위치, 명령) 만 올리면 엔진이 그린다.
 * 그래서 ImGui 버전에 묶이지 않고, C#/Python 플러그인도 같은 방식을 쓰며,
 * **호스트 임베드(MFC/WPF)에서도 산다** — 호스트가 이 목록을 읽어 자기 메뉴로 그리면 된다.
 *
 * kind: 0=메뉴항목 1=구분선 2=툴바버튼 3=리본버튼 4=패널
 * path: 위치. 구분자는 '/'.
 *         메뉴 "건축" · "건축/가져오기"   툴바/리본 "건축/벽체"
 *         패널은 도킹 위치를 여기 넣는다("left"/"right"/"bottom").
 * command: 누르면 실행할 명령 이름. 명령행과 **같은 입구**로 들어간다.
 *          구분선·패널은 NULL 가능. 그 외엔 title·command 가 비면 CAD_E_INVALID_ARG —
 *          눌러도 아무 일이 안 생기는 항목은 등록 단계에서 막는다.
 * icon: 짧은 글자/이모지. 지금은 글자로 보여주고 나중에 아이콘으로 바꾼다. NULL 가능.
 * owner: 플러그인 ID. 언로드 시 이 값으로 묶어 한꺼번에 지운다.
 *
 * 성공하면 *outItemId = 항목 id(NULL 가능) — 이 id 로 개별 제거한다. kind 범위 밖 CAD_E_OUT_OF_RANGE(5·6 = CAD_AddUiControl).
 * ⚠️ 패널은 **존재만** 등록된다 — 내용은 플러그인이 ImGui 후크로 그려야 하고,
 *    그건 단독 실행 전용이다(호스트 임베드엔 ImGui 컨텍스트가 없다).
 */
CAD_API CAD_Status CAD_AddUiItem(int32_t kind, const char* path, const char* title,
                                 const char* command, const char* icon, uint32_t owner, uint32_t* outItemId);
CAD_API CAD_Status CAD_RemoveUiItem(uint32_t id);                  /* 없는 id CAD_E_NOT_FOUND */
CAD_API int32_t    CAD_RemoveUiItemsByOwner(uint32_t owner);       /* 지운 개수 */
/* 호스트가 메뉴·툴바를 직접 그릴 때 읽는다. index 는 등록 순서 = 화면 나열 순서(0 ~ 개수 − 1, 범위 밖 CAD_E_OUT_OF_RANGE). */
CAD_API int32_t    CAD_GetUiItemCount(void);
/* 양수 높이 = 바깥 오버레이용으로 기본 리본 자리를 비워 둔다(논리 픽셀). 0 = 원래 ImGui 리본·플러그인 리본으로 */
CAD_API CAD_Status CAD_SetOverlayRibbonHeight(double logicalHeight);
/* 호스트 메뉴줄 바로 아래 논리 Y(ImGui 가 없으면 0) */
CAD_API CAD_Status CAD_GetOverlayRibbonTop(double* outTop);
CAD_API CAD_Status CAD_GetUiItemId(uint32_t index, uint32_t* outItemId);
CAD_API CAD_Status CAD_GetUiItemKind(uint32_t index, int32_t* outKind);
CAD_API int32_t    CAD_GetUiItemPath(uint32_t index, char* buf, uint32_t capacity);
CAD_API int32_t    CAD_GetUiItemTitle(uint32_t index, char* buf, uint32_t capacity);
CAD_API int32_t    CAD_GetUiItemCommand(uint32_t index, char* buf, uint32_t capacity);
CAD_API int32_t    CAD_GetUiItemIcon(uint32_t index, char* buf, uint32_t capacity);

/* 리본 조작 항목 — kind 5 = 체크 상자(값 0/1, 범위 무시), 6 = 슬라이더(유한한 minimum < maximum, 값은 그 안으로).
 * path = "탭/그룹". 사용자가 바꾸면 command 가 불리고, 그 명령이 CAD_GetUiControlValue(id) 로 새 값을 읽는다.
 * 잘못된 값·범위 CAD_E_INVALID_ARG, 없는 id CAD_E_NOT_FOUND. 플러그인은 언로드 때 엔진이 owner 로 지운다. */
CAD_API CAD_Status CAD_AddUiControl(int32_t kind, const char* path,
    const char* title, const char* command, double minimum, double maximum,
    double value, uint32_t owner, uint32_t* outItemId);
CAD_API CAD_Status CAD_SetUiControlValue(uint32_t id, double value);
CAD_API CAD_Status CAD_GetUiControlValue(uint32_t id, double* value,
    double* minimum, double* maximum);   /* 출력은 NULL 가능 */

/* ── 플러그인 로더 ────────────────────────────────────────
 *
 * 엔진은 시작할 때 플러그인을 붙이지 않는다(2026-10-11부터). 필요하면 호스트가 CAD_LoadPlugins("plugins") 처럼 부르고,
 * 앱 사용자는 명령 `pload all`(실행 폴더·사용자 설정 폴더의 plugins/) · `punload all` 로 붙이고 내린다.
 *
 * 플러그인은 plugin/lot_plugin_sdk.h 의 심볼 셋을 내보내야 한다:
 *   CAD_PluginAbiVersion / CAD_PluginLoad / CAD_PluginUnload
 * ABI 번호가 다르면 아예 올리지 않는다 — 엔진과 같은 컴파일러·런타임으로 빌드해야 한다.
 *
 * 언로드하면 그 플러그인이 올린 명령과 UI 항목이 **엔진이 알아서** 같이 지워진다.
 */
/* dir 의 플러그인을 붙인다(이미 붙은 것은 건너뜀). 반환 = 새로 붙인 개수(0 이면 이유 — ABI 다름 등 — 가 CAD_GetLastError 에 있을 수 있다).
 * 폴더가 아님 CAD_E_NOT_FOUND */
CAD_API int32_t    CAD_LoadPlugins(const char* dir);
CAD_API CAD_Status CAD_UnloadPlugin(uint32_t id);                       /* 없는 id CAD_E_NOT_FOUND */
CAD_API int32_t    CAD_GetPluginCount(void);
CAD_API CAD_Status CAD_GetPluginId(uint32_t index, uint32_t* outPluginId);
CAD_API int32_t    CAD_GetPluginName(uint32_t index, char* buf, uint32_t capacity);

/* ── 플러그인 엔티티 ───────────────────────────────────────────────────
 *
 * 새 객체 종류를 만들지 않는다. 플러그인이 **형상(메시)을 공급**하고, 객체에 **딱지**를 붙인다.
 * 객체는 평범한 메시라 그리기·픽킹·저장이 전부 그대로 동작하고, 플러그인이 없는 곳에서
 * 열어도 형상은 보인다. 딱지는 보존돼 나중에 플러그인이 있으면 도로 살아난다.
 *
 *   CAD_CreateMesh(pts, nv, idx, ni, NULL, NULL, &id);    // 형상(월드 = 처음 자기 좌표)
 *   CAD_SetPluginTag(id, "ArchBuilder", "wall", json);   // 딱지
 *   ... 값이 바뀌면 → CAD_ReplaceMesh(id, pts, ...)       // 재생성(자기 좌표 — 사용자가 옮긴 자리는 그대로)
 *
 * .lot 을 열어 딱지 붙은 객체가 복원되면 CAD_SetOnPluginEntityLoaded 콜백으로 알려준다.
 * 플러그인은 owner 가 자기 이름이면 data 를 읽어 살아 있는 엔티티로 넘겨받는다.
 *
 * 사용자가 그립·불리언·밀당·분해로 메시를 직접 고치면 정의와 형상이 어긋나므로 엔진이
 * 먼저 묻고, "계속" 이면 딱지를 뗀다(그냥 메시가 된다). 호스트 임베드는 ImGui 가 없어
 * CAD_SetOnConfirm 으로 대신 물어야 한다 — 안 달면 안전한 쪽(취소)으로 간다.
 *
 * CAD_CreateMesh / CAD_ReplaceMesh 는 lotcad_mesh.h.
 */
/* 없는 객체 CAD_E_BAD_HANDLE · owner 빈 글 CAD_E_INVALID_ARG · 딱지 없는 객체의 Get* = CAD_E_NOT_FOUND */
CAD_API CAD_Status CAD_SetPluginTag(uint32_t id, const char* owner, const char* type, const char* data);
CAD_API CAD_Status CAD_ClearPluginTag(uint32_t id);
CAD_API CAD_Status CAD_HasPluginTag(uint32_t id, bool* outHas);
CAD_API int32_t    CAD_GetPluginTagOwner(uint32_t id, char* buf, uint32_t capacity);
CAD_API int32_t    CAD_GetPluginTagType(uint32_t id, char* buf, uint32_t capacity);
CAD_API int32_t    CAD_GetPluginTagData(uint32_t id, char* buf, uint32_t capacity);
CAD_API CAD_Status CAD_SetOnPluginEntityLoaded(void (*cb)(uint32_t id, const char* owner,
                                                           const char* type, const char* data));
/* 콜백 반환 true = 계속. 호스트 임베드(MFC/WPF)는 반드시 달 것 — 없으면 취소로 간다. */
CAD_API CAD_Status CAD_SetOnConfirm(bool (*cb)(const char* text));

/* ── 엔티티 속성 (특성창) ──────────────────────────────────────────────
 *
 * 플러그인은 특성창을 직접 그리지 않는다. "두께는 0.05~2.0 실수" 라고 **말만** 하고
 * 엔진이 슬라이더를 그린다. ImGui 버전에 안 묶이고, 호스트 임베드에서도 산다.
 *
 *   CAD_AddEntityProperty("HelloPlugin", "wall", "thick", "두께", 0, 0.05f, 2.0f, id);
 *
 * ⭐ 값은 딱지 data 에 **JSON 오브젝트**로 들어 있어야 한다. 엔진이 그 JSON 을 읽고 쓴다.
 *    그래서 플러그인이 없어도 값이 보인다(그때는 읽기 전용 — 형상을 다시 만들 코드가 없다).
 *
 * kind: 0=실수 1=정수 2=참거짓 3=문자(읽기전용)
 * minV/maxV: min>=max 면 범위 없음. 실패: owner·type·key 빈 글 CAD_E_INVALID_ARG · kind 범위 밖 CAD_E_OUT_OF_RANGE ·
 *   같은 (owner,type,key) CAD_E_DUPLICATE.
 *
 * 사용자가 값을 바꾸면 엔진이 딱지 JSON 을 갱신하고 CAD_SetOnPluginEntityChanged 를 부른다.
 * 플러그인은 거기서 CAD_ReplaceMesh 로 형상을 다시 만든다.
 */
CAD_API CAD_Status CAD_AddEntityProperty(const char* owner, const char* type, const char* key,
                                         const char* label, int32_t kind, double minV, double maxV,
                                         uint32_t pluginId);
CAD_API int32_t    CAD_RemoveEntityPropertiesByOwner(uint32_t pluginId);   /* 지운 개수 */
CAD_API CAD_Status CAD_SetOnPluginEntityChanged(void (*cb)(uint32_t id, const char* owner,
                                                            const char* type, const char* data));

/* ── 플러그인 패널 (ImGui 직접 그리기) ─────────────────────────────────
 *
 * 패널은 CAD_AddUiItem(kind 4) 로 등록하면 엔진이 창을 만들고, 그 **안을 플러그인이**
 * ImGui 로 그린다. 메뉴·툴바·리본과 달리 이것만 플러그인이 ImGui 를 직접 부른다.
 *
 * ⚠️ 그래서 제약이 붙는다:
 *    · 플러그인이 엔진과 **같은 ImGui 버전**을 컴파일해 넣어야 한다
 *    · 아래 두 함수로 컨텍스트와 할당자를 받아 ImGui::SetCurrentContext /
 *      ImGui::SetAllocatorFunctions 를 먼저 불러야 한다 — DLL 경계를 넘으면
 *      ImGui 전역과 힙이 공유되지 않는다(ImGui 문서의 그 항목)
 *    · **호스트 임베드(MFC/WPF)에선 안 뜬다** — 거기엔 ImGui 컨텍스트가 없다
 *      (CAD_GetImGuiContext 가 CAD_E_NOT_SUPPORTED)
 *
 * 값 편집만 필요하면 CAD_AddEntityProperty(특성창) 가 이 제약을 전부 피한다.
 * 그래서 패널은 "그래프·미리보기처럼 정말 직접 그려야 하는 것" 에만 쓰는 게 좋다.
 *
 *   void drawPanel(unsigned id, const char* title) { ImGui::Text("..."); }
 *   void* ctx = NULL; if (CAD_GetImGuiContext(&ctx) == CAD_OK) ImGui::SetCurrentContext((ImGuiContext*)ctx);
 *   CAD_GetImGuiAllocators(&a, &f, &u); ImGui::SetAllocatorFunctions(a, f, u);
 *   CAD_SetOnDrawPanel(&drawPanel);
 */
CAD_API CAD_Status CAD_GetImGuiContext(void** outContext);   /* *outContext = ImGuiContext* — ImGui 가 없으면 CAD_E_NOT_SUPPORTED + NULL */
CAD_API CAD_Status CAD_GetImGuiAllocators(void** allocFn, void** freeFn, void** userData);
CAD_API CAD_Status CAD_SetOnDrawPanel(void (*cb)(unsigned int panelId, const char* title));

#ifdef __cplusplus
}
#endif
