#pragma once
/* LotCAD C API - events  [AcDb / AcEd reactors]
 * Callbacks and event listeners (engine -> host).
 * 알림 콜백·이벤트 구독(엔진 → 호스트).
 * Include LotCAD_API.h (all areas) or this file alone. Rules: lotcad_types.h. */
#include "lotcad_types.h"

#ifdef __cplusplus
extern "C" {
#endif
/* ── 엔진 이벤트 구독 ──────────────────────────────────────────────────
 *
 * 호스트·플러그인 모두 이것 하나로 구독한다(목록 — 여럿이 같이 들어도 서로 덮지 않는다. 예전 한 칸짜리 CAD_SetOnSelectionChanged·
 * ObjectCreated·ObjectDeleted·DocumentDirty 는 플러그인이 걸면 호스트 것을 덮어써서 2e-1 에서 지웠다).
 *
 * kinds 는 비트 OR: 1=객체생성 2=객체삭제 4=선택변경 8=문서변경 16=명령시작 32=명령끝 64=명령취소
 *   생성/삭제 → id = 그 객체. 선택변경 → id = 0. 문서변경 → id = dirty ? 1 : 0.
 *   명령 시작·끝·취소(ObjectARX commandWillStart · commandEnded · commandCancelled) → id = 0, 이름은 CAD_EdGetCommandName.
 *   "끝" = 명령이 더는 값·점·대상을 기다리지 않음(바로 끝나는 명령은 시작과 같은 틱), "취소" = 기다리던 중 ESC.
 *
 * 성공하면 *outHandle = 핸들(CAD_RemoveEventListener 에). fn·outHandle NULL·kinds 0·모르는 비트 = CAD_E_INVALID_ARG.
 * pluginId = 그 플러그인 ID(0 = 호스트) — 언로드 때 엔진이 그 ID 로 묶어 알아서 지운다.
 * 콜백은 엔진과 같은 스레드에서 프레임 끝에 불린다 — 안에서 CAD_* 를 불러도 된다.
 */
enum {
    CAD_EVENT_OBJECT_CREATED    = 1,
    CAD_EVENT_OBJECT_DELETED    = 2,
    CAD_EVENT_SELECTION_CHANGED = 4,
    CAD_EVENT_DOCUMENT_DIRTY    = 8,
    CAD_EVENT_COMMAND_STARTED   = 16,
    CAD_EVENT_COMMAND_ENDED     = 32,
    CAD_EVENT_COMMAND_CANCELLED = 64
};
typedef void (*CAD_EventFn)(int kind, uint32_t id, void* user);
CAD_API CAD_Status CAD_AddEventListener(uint32_t kinds, CAD_EventFn fn, void* user, uint32_t pluginId, uint32_t* outHandle);
CAD_API CAD_Status CAD_RemoveEventListener(uint32_t handle);   /* 없는 핸들 CAD_E_NOT_FOUND */

/* 하단 안내문(명령 프롬프트/임시 메시지)이 바뀔 때 — 글을 넘겨 주는 알림이라 한 칸 콜백으로 남겼다. 호스트 상태바에 그대로 띄우면 된다.
 * CAD_Tick 안(프레임 끝, 엔진 스레드)에서 바뀐 때만. NULL = 해제 */
CAD_API CAD_Status CAD_SetOnPrompt(void (*cb)(const char* text));

#ifdef __cplusplus
}
#endif
