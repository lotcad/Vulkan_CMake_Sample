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
 * ⚠️ 위 CAD_SetOnXxx 계열은 **한 칸짜리**다 — 플러그인이 걸면 호스트 것을 덮어쓴다.
 *    플러그인은 여러 개가 동시에 올라오므로 이쪽(목록)으로 구독한다. 둘 다 발화한다.
 *
 * kinds 는 비트 OR: 1=객체생성 2=객체삭제 4=선택변경 8=문서변경 16=명령시작 32=명령끝 64=명령취소
 *   생성/삭제 → id = 그 객체. 선택변경 → id = 0. 문서변경 → id = dirty ? 1 : 0.
 *   명령 시작·끝·취소(ObjectARX commandWillStart · commandEnded · commandCancelled) → id = 0, 이름은 CAD_EdGetCommandName.
 *   "끝" = 명령이 더는 값·점·대상을 기다리지 않음(바로 끝나는 명령은 시작과 같은 틱), "취소" = 기다리던 중 ESC.
 *
 * 반환 = 핸들(0 이면 실패). 언로드 때는 엔진이 pluginId 로 묶어 알아서 지운다.
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
CAD_API unsigned int CAD_AddEventListener(int kinds, CAD_EventFn fn, void* user, unsigned int pluginId);
CAD_API bool CAD_RemoveEventListener(unsigned int handle);

/* ── 알림(콜백) ───────────────────────────────────────────────────────────
 *
 * 엔진 → 호스트 UI 방향의 알림. 이게 없으면 호스트는 **매 프레임 물어보는 수밖에**
 * 없다(선택이 바뀌었는지 알려고 GetSelectedCount 를 계속 호출하는 식).
 * 속성 패널·씬 트리·제목표시줄의 * 표시 같은 걸 붙이려면 사실상 필수다.
 * ObjectARX 의 리액터(AcDbDatabaseReactor)와 같은 역할.
 *
 * ⚠️ 호출 시점은 **CAD_Tick 안**이다 — 프레임당 한 번, 엔진과 같은 스레드.
 *    그래서 콜백 안에서 다른 CAD_* 를 불러도 안전하다.
 *    변화가 **한 프레임에 여러 번** 나도 한 번으로 합쳐 알린다(UI 갱신엔 충분).
 * nullptr 를 주면 해제된다.
 */
CAD_API void CAD_SetOnSelectionChanged(void (*cb)(void));
CAD_API void CAD_SetOnObjectCreated  (void (*cb)(uint32_t id));
CAD_API void CAD_SetOnObjectDeleted  (void (*cb)(uint32_t id));
CAD_API void CAD_SetOnDocumentDirty  (void (*cb)(bool dirty));
/* 하단 안내문(명령 프롬프트/임시 메시지)이 바뀔 때. 호스트 상태바에 그대로 띄우면 된다. */
CAD_API void CAD_SetOnPrompt         (void (*cb)(const char* text));

#ifdef __cplusplus
}
#endif
