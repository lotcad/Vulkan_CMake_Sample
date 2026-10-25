// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    public static partial class CadApi
    {
        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateText(CAD_GeVec3 position, [MarshalAs(UnmanagedType.LPUTF8Str)] string utf8, double height, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateText — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateText(CAD_GeVec3 position, string utf8, double height, out uint outId)
        {
            return CAD_CreateText(position, utf8, height, null, out outId);
        }
        /// <summary>CAD_CreateText — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateText(CAD_GeVec3 position, string utf8, double height, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateText(position, utf8, height, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateDimension(CAD_GeVec3 p1, CAD_GeVec3 p2, CAD_GeVec3 dimLinePoint, CAD_GeVec3 normal, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateDimension — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateDimension(CAD_GeVec3 p1, CAD_GeVec3 p2, CAD_GeVec3 dimLinePoint, CAD_GeVec3 normal, out uint outId)
        {
            return CAD_CreateDimension(p1, p2, dimLinePoint, normal, null, out outId);
        }
        /// <summary>CAD_CreateDimension — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateDimension(CAD_GeVec3 p1, CAD_GeVec3 p2, CAD_GeVec3 dimLinePoint, CAD_GeVec3 normal, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateDimension(p1, p2, dimLinePoint, normal, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetTextContent(uint id, [MarshalAs(UnmanagedType.LPUTF8Str)] string utf8);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetTextContent(uint id, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateDrawingViews(uint[] ids, uint count, double scale);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateSectionView(CAD_GeVec3 a, CAD_GeVec3 b, out uint outViewId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateDetailView(CAD_GeVec3 center, double radius, double factor, out uint outViewId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_MoveDrawingView(uint viewId, CAD_GeVec3 offset);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClearDrawingViews();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetDrawingViewsJson(byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_AttachImageFromFile([MarshalAs(UnmanagedType.LPUTF8Str)] string pathUtf8, double widthWorld, CAD_GeVec3 origin, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_AttachImageFromFile — 선택 없이(전부 기본값).</summary>
        public static int CAD_AttachImageFromFile(string pathUtf8, double widthWorld, CAD_GeVec3 origin, out uint outId)
        {
            return CAD_AttachImageFromFile(pathUtf8, widthWorld, origin, null, out outId);
        }
        /// <summary>CAD_AttachImageFromFile — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_AttachImageFromFile(string pathUtf8, double widthWorld, CAD_GeVec3 origin, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_AttachImageFromFile(pathUtf8, widthWorld, origin, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_AttachImageFromMemory(byte[] rgba, int width, int height, [MarshalAs(UnmanagedType.LPUTF8Str)] string displayName, double widthWorld, CAD_GeVec3 origin, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_AttachImageFromMemory — 선택 없이(전부 기본값).</summary>
        public static int CAD_AttachImageFromMemory(byte[] rgba, int width, int height, string displayName, double widthWorld, CAD_GeVec3 origin, out uint outId)
        {
            return CAD_AttachImageFromMemory(rgba, width, height, displayName, widthWorld, origin, null, out outId);
        }
        /// <summary>CAD_AttachImageFromMemory — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_AttachImageFromMemory(byte[] rgba, int width, int height, string displayName, double widthWorld, CAD_GeVec3 origin, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_AttachImageFromMemory(rgba, width, height, displayName, widthWorld, origin, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_BeginOcrLines(uint imageId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_AddOcrLine([MarshalAs(UnmanagedType.LPUTF8Str)] string utf8, int x0, int y0, int x1, int y1);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EndOcrLines();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateLeader(CAD_GeVec3 tip, CAD_GeVec3 bend, [MarshalAs(UnmanagedType.LPUTF8Str)] string textUtf8, double textHeight, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateLeader — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateLeader(CAD_GeVec3 tip, CAD_GeVec3 bend, string textUtf8, double textHeight, out uint outId)
        {
            return CAD_CreateLeader(tip, bend, textUtf8, textHeight, null, out outId);
        }
        /// <summary>CAD_CreateLeader — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateLeader(CAD_GeVec3 tip, CAD_GeVec3 bend, string textUtf8, double textHeight, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateLeader(tip, bend, textUtf8, textHeight, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateHatch(uint[] ids, uint count, [MarshalAs(UnmanagedType.LPUTF8Str)] string pattern, double scale, double angle, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateHatch — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateHatch(uint[] ids, uint count, string pattern, double scale, double angle, out uint outId)
        {
            return CAD_CreateHatch(ids, count, pattern, scale, angle, null, out outId);
        }
        /// <summary>CAD_CreateHatch — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateHatch(uint[] ids, uint count, string pattern, double scale, double angle, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateHatch(ids, count, pattern, scale, angle, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_Plot([MarshalAs(UnmanagedType.LPUTF8Str)] string path, [MarshalAs(UnmanagedType.I1)] bool selectedOnly, [MarshalAs(UnmanagedType.I1)] bool monochrome, double paperW, double paperH, int pngLongSidePx);
    }
}
