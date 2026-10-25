// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_Color
    {
        public double r;
        public double g;
        public double b;
    }

    public static partial class CadApi
    {
        public const int CAD_OK = 0;
        public const int CAD_E_INVALID_ARG = -1;
        public const int CAD_E_BAD_HANDLE = -2;
        public const int CAD_E_NO_ENGINE = -3;
        public const int CAD_E_WRONG_TYPE = -4;
        public const int CAD_E_DEGENERATE = -5;
        public const int CAD_E_PARALLEL = -6;
        public const int CAD_E_NOT_PLANAR = -7;
        public const int CAD_E_NOT_CLOSED = -8;
        public const int CAD_E_NOT_ON_CURVE = -9;
        public const int CAD_E_OUT_OF_RANGE = -10;
        public const int CAD_E_NOT_SUPPORTED = -11;
        public const int CAD_E_FAILED = -12;
        public const int CAD_E_BUFFER_TOO_SMALL = -13;
        public const int CAD_E_NOT_CONNECTED = -14;
        public const int CAD_E_WRONG_THREAD = -15;
        public const int CAD_E_LOCKED = -16;
        public const int CAD_E_BUSY = -17;
        public const int CAD_E_NOT_READY = -18;
        public const int CAD_E_NOT_FOUND = -19;
        public const int CAD_E_DUPLICATE = -20;
        public const int CAD_E_CONFLICT = -21;
    }
}
