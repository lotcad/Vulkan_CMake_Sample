// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate void CAD_EventFn(int kind, uint id, IntPtr user);

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
        public static extern int CAD_AddEventListener(uint kinds, CAD_EventFn fn, IntPtr user, uint pluginId, out uint outHandle);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_RemoveEventListener(uint handle);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetOnPrompt(CAD_SetOnPrompt_cb cb);
    }
}
