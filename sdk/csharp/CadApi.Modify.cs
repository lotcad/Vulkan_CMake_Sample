// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    public static partial class CadApi
    {
        public const int CAD_LENGTHEN_DELTA = 0;
        public const int CAD_LENGTHEN_PERCENT = 1;
        public const int CAD_LENGTHEN_TOTAL = 2;

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_StretchWindowXY(CAD_GeVec3 corner1, CAD_GeVec3 corner2, CAD_GeVec3 offset);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_Lengthen(uint id, int mode, double value, [MarshalAs(UnmanagedType.I1)] bool atStart);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_BreakObject(uint id, CAD_GeVec3 point1, CAD_GeVec3 point2, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_Align3D(uint[] ids, uint count, CAD_GeVec3[] source, CAD_GeVec3[] target, uint pairs);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_Offset(uint[] ids, uint count, double distance, CAD_GeVec3 sidePoint, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_Trim(uint id, CAD_GeVec3 pickPoint, uint[] boundaryIds, uint boundaryCount, CAD_GeVec3 planeNormal, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_Extend(uint id, CAD_GeVec3 pickPoint, uint[] boundaryIds, uint boundaryCount, CAD_GeVec3 planeNormal, uint[] outIds, uint capacity);
    }
}
