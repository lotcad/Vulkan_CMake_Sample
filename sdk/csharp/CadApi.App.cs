// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate void CAD_PostFn(IntPtr user);

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_OverlayFrameInfo
    {
        public uint structSize;
        public ulong physicalDevice;
        public ulong device;
        public ulong graphicsQueue;
        public ulong renderPass;
        public ulong commandBuffer;
        public uint graphicsQueueFamily;
        public uint frameIndex;
        public uint frameCount;
        public uint framebufferWidth;
        public uint framebufferHeight;
        public int windowWidth;
        public int windowHeight;
        public float dpiScale;
        public double pointerX;
        public double pointerY;
        public uint pointerButtons;
        public int modifiers;
        public uint sampleCount;
    }

    [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate uint CAD_OverlayRenderFn(IntPtr frame, IntPtr user);

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_OverlayPointerInfo
    {
        public uint structSize;
        public int windowWidth;
        public int windowHeight;
        public double x;
        public double y;
        public uint buttons;
        public int modifiers;
    }

    [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate uint CAD_OverlayInputFn(IntPtr pointer, IntPtr user);

    [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate void CAD_SetOnCopyText_cb(IntPtr utf8);

    public static partial class CadApi
    {
        public const uint CAD_OVERLAY_CAPTURE_POINTER = 1;
        public const uint CAD_OVERLAY_CAPTURE_KEYBOARD = 2;

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetVersion(byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetUserDataPath([MarshalAs(UnmanagedType.LPUTF8Str)] string pathUtf8);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetUserDataPath(byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_CreateEngine();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_DestroyEngine();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_Tick();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_Post(CAD_PostFn fn, IntPtr user);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_IsEngineThread([MarshalAs(UnmanagedType.I1)] out bool outIsEngine);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_ShouldClose();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetIgnoreCloseRequest([MarshalAs(UnmanagedType.I1)] bool ignore);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetRuntimeAssetPath([MarshalAs(UnmanagedType.LPUTF8Str)] string path);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_AttachView(IntPtr nativeHandle, int width, int height);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ResizeView(int width, int height);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_DetachView();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_OnMouseDown(int button, double x, double y, int modifiers);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_OnMouseUp(int button, double x, double y, int modifiers);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_OnMouseMove(double x, double y);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_OnMouseWheel(double x, double y, double deltaX, double deltaY);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_OnKeyDown(int key, int modifiers);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_OnKeyUp(int key, int modifiers);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetOverlayRenderCallback(CAD_OverlayRenderFn callback, IntPtr user);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetOverlayInputCallback(CAD_OverlayInputFn callback, IntPtr user);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_OnKeyDownVK(int vkCode);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_OnKeyUpVK(int vkCode);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GizmoHitTest(double x, double y, [MarshalAs(UnmanagedType.I1)] out bool outHit);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetGizmoTouchMode([MarshalAs(UnmanagedType.I1)] bool enabled);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetSnapTouchMode([MarshalAs(UnmanagedType.I1)] bool enabled);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetOnCopyText(CAD_SetOnCopyText_cb cb);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_PasteText([MarshalAs(UnmanagedType.LPUTF8Str)] string utf8);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ShowMessage([MarshalAs(UnmanagedType.LPUTF8Str)] string textUtf8, double seconds);
    }
}
