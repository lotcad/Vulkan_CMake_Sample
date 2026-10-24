// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate void CAD_EventFn(int kind, uint id, IntPtr user);

    [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate void CAD_SetOnSelectionChanged_cb();

    [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate void CAD_SetOnObjectCreated_cb(uint id);

    [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate void CAD_SetOnObjectDeleted_cb(uint id);

    [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate void CAD_SetOnDocumentDirty_cb([MarshalAs(UnmanagedType.I1)] bool dirty);

    [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate void CAD_SetOnPrompt_cb(IntPtr text);

    public static partial class CadApi
    {
        public const int CAD_EVENT_OBJECT_CREATED = 1;
        public const int CAD_EVENT_OBJECT_DELETED = 2;
        public const int CAD_EVENT_SELECTION_CHANGED = 4;
        public const int CAD_EVENT_DOCUMENT_DIRTY = 8;
        public const int CAD_EVENT_COMMAND_STARTED = 16;
        public const int CAD_EVENT_COMMAND_ENDED = 32;
        public const int CAD_EVENT_COMMAND_CANCELLED = 64;

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_AddEventListener(int kinds, CAD_EventFn fn, IntPtr user, uint pluginId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_RemoveEventListener(uint handle);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_SetOnSelectionChanged(CAD_SetOnSelectionChanged_cb cb);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_SetOnObjectCreated(CAD_SetOnObjectCreated_cb cb);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_SetOnObjectDeleted(CAD_SetOnObjectDeleted_cb cb);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_SetOnDocumentDirty(CAD_SetOnDocumentDirty_cb cb);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_SetOnPrompt(CAD_SetOnPrompt_cb cb);
    }
}
