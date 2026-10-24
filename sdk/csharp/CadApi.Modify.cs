// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    public static partial class CadApi
    {
        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_RequestMoveSelected(float dirX, float dirY, float dirZ, float distance);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_RequestRotateSelected(float axisX, float axisY, float axisZ, float angleDeg);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_RequestScaleSelected(float factor);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_RequestCopySelected(float dirX, float dirY, float dirZ, float distance, int count);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_RequestColorSelected(float r, float g, float b);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_Explode([MarshalAs(UnmanagedType.I1)] bool keepOriginal);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_ArrayRect(int cols, int rows, float dx, float dy);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_ArrayPolar(int count, float angleDeg, float centerX, float centerY, float centerZ, [MarshalAs(UnmanagedType.I1)] bool rotateItems);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_StretchWindowXY(float minX, float minY, float maxX, float maxY, float dx, float dy, float dz);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_Lengthen(uint id, int mode, float value, [MarshalAs(UnmanagedType.I1)] bool atStart);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_BreakObject(uint id, float x1, float y1, float z1, float x2, float y2, float z2);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_Array3DRect(int cols, int rows, int levels, float dx, float dy, float dz);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_Array3DPolar(int count, float angleDeg, float ax, float ay, float az, float bx, float by, float bz, [MarshalAs(UnmanagedType.I1)] bool rotateItems);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_Align3D(uint[] ids, uint count, float[] srcXYZ, float[] dstXYZ, int pairs);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_Offset(uint[] ids, uint count, float distance, float sx, float sy, float sz, uint[] outIds, uint outCapacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_Mirror(uint[] ids, uint count, float x1, float y1, float z1, float x2, float y2, float z2, float nx, float ny, float nz, [MarshalAs(UnmanagedType.I1)] bool deleteOriginals, uint[] outIds, uint outCapacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_Trim(uint id, float px, float py, float pz, uint[] boundaryIds, uint boundaryCount, float nx, float ny, float nz);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_Extend(uint id, float px, float py, float pz, uint[] boundaryIds, uint boundaryCount, float nx, float ny, float nz);
    }
}
