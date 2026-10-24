// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    public static partial class CadApi
    {
        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateText(float x, float y, float z, [MarshalAs(UnmanagedType.LPUTF8Str)] string utf8, float heightMM);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateDimension(float p1x, float p1y, float p1z, float p2x, float p2y, float p2z, float dlx, float dly, float dlz, float nx, float ny, float nz);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_SetTextContent(uint id, [MarshalAs(UnmanagedType.LPUTF8Str)] string utf8);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetTextContent(uint id, byte[] outUtf8, int cap);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateDrawingViews(uint[] ids, uint count, float scale);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateSectionView(float ax, float ay, float bx, float by);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateDetailView(float cx, float cy, float radius, float factor);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_MoveDrawingView(uint viewId, float dx, float dy);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_ClearDrawingViews();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetDrawingViewsJson(byte[] @out, int cap);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_AttachImageFromFile([MarshalAs(UnmanagedType.LPUTF8Str)] string pathUtf8, float widthWorld, float originX, float originY, float originZ);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_AttachImageFromMemory(byte[] rgba, int width, int height, [MarshalAs(UnmanagedType.LPUTF8Str)] string displayName, float widthWorld, float originX, float originY, float originZ);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_BeginOcrLines(uint imageId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_AddOcrLine([MarshalAs(UnmanagedType.LPUTF8Str)] string utf8, int x0, int y0, int x1, int y1);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_EndOcrLines();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateLeader(float tipX, float tipY, float tipZ, float bendX, float bendY, float bendZ, [MarshalAs(UnmanagedType.LPUTF8Str)] string textUtf8, float textHeight);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateHatch(uint[] ids, uint count, [MarshalAs(UnmanagedType.LPUTF8Str)] string pattern, float scale, float angleDeg);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_Plot([MarshalAs(UnmanagedType.LPUTF8Str)] string path, [MarshalAs(UnmanagedType.I1)] bool selectedOnly, [MarshalAs(UnmanagedType.I1)] bool monochrome, float paperW, float paperH, int pngLongSidePx);
    }
}
