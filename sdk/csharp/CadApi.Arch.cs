// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_FloorplanOpeningDesc
    {
        public int type;
        public uint roomAIndex;
        public int roomBIndex;
        public int side;
        public double width;
        public double height;
        public double sillHeight;
        public int alignment;
        public double offset;
    }

    public static partial class CadApi
    {
        public const int CAD_OPENING_DOOR = 0;
        public const int CAD_OPENING_WINDOW = 1;
        public const int CAD_WALL_SOUTH = 0;
        public const int CAD_WALL_NORTH = 1;
        public const int CAD_WALL_WEST = 2;
        public const int CAD_WALL_EAST = 3;
        public const int CAD_OPENING_CENTER = 0;
        public const int CAD_OPENING_START = 1;
        public const int CAD_OPENING_END = 2;

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateRoom(CAD_GeVec3 floorCenter, double width, double depth, double height, double wallThickness, CAD_CreateOptions[] opt, uint[] outWallIds);

        /// <summary>CAD_CreateRoom — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateRoom(CAD_GeVec3 floorCenter, double width, double depth, double height, double wallThickness, uint[] outWallIds)
        {
            return CAD_CreateRoom(floorCenter, width, depth, height, wallThickness, null, outWallIds);
        }
        /// <summary>CAD_CreateRoom — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateRoom(CAD_GeVec3 floorCenter, double width, double depth, double height, double wallThickness, CAD_CreateOptions opt, uint[] outWallIds)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateRoom(floorCenter, width, depth, height, wallThickness, new[] { opt }, outWallIds);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateFloorplan(double baseZ, double[] rectBounds, uint spaceCount, double height, double wallThickness, CAD_FloorplanOpeningDesc[] openings, uint openingCount, CAD_CreateOptions[] opt, uint[] outWallIds, uint capacity);

        /// <summary>CAD_CreateFloorplan — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateFloorplan(double baseZ, double[] rectBounds, uint spaceCount, double height, double wallThickness, CAD_FloorplanOpeningDesc[] openings, uint openingCount, uint[] outWallIds, uint capacity)
        {
            return CAD_CreateFloorplan(baseZ, rectBounds, spaceCount, height, wallThickness, openings, openingCount, null, outWallIds, capacity);
        }
        /// <summary>CAD_CreateFloorplan — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateFloorplan(double baseZ, double[] rectBounds, uint spaceCount, double height, double wallThickness, CAD_FloorplanOpeningDesc[] openings, uint openingCount, CAD_CreateOptions opt, uint[] outWallIds, uint capacity)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateFloorplan(baseZ, rectBounds, spaceCount, height, wallThickness, openings, openingCount, new[] { opt }, outWallIds, capacity);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_FloorplanExtractFromImage([MarshalAs(UnmanagedType.LPUTF8Str)] string path, double widthMm, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_FloorplanExtractFromRgba(byte[] rgba, int width, int height, double widthMm, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateWallGraph(double baseZ, double[] segments, uint count, double height, double defaultThickness, CAD_CreateOptions[] opt, uint[] outIds, uint capacity);

        /// <summary>CAD_CreateWallGraph — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateWallGraph(double baseZ, double[] segments, uint count, double height, double defaultThickness, uint[] outIds, uint capacity)
        {
            return CAD_CreateWallGraph(baseZ, segments, count, height, defaultThickness, null, outIds, capacity);
        }
        /// <summary>CAD_CreateWallGraph — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateWallGraph(double baseZ, double[] segments, uint count, double height, double defaultThickness, CAD_CreateOptions opt, uint[] outIds, uint capacity)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateWallGraph(baseZ, segments, count, height, defaultThickness, new[] { opt }, outIds, capacity);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateFloorplanFromImage([MarshalAs(UnmanagedType.LPUTF8Str)] string path, double widthMm, double height, [MarshalAs(UnmanagedType.I1)] bool underlayImage, CAD_CreateOptions[] opt, uint[] outIds, uint capacity);

        /// <summary>CAD_CreateFloorplanFromImage — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateFloorplanFromImage(string path, double widthMm, double height, bool underlayImage, uint[] outIds, uint capacity)
        {
            return CAD_CreateFloorplanFromImage(path, widthMm, height, underlayImage, null, outIds, capacity);
        }
        /// <summary>CAD_CreateFloorplanFromImage — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateFloorplanFromImage(string path, double widthMm, double height, bool underlayImage, CAD_CreateOptions opt, uint[] outIds, uint capacity)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateFloorplanFromImage(path, widthMm, height, underlayImage, new[] { opt }, outIds, capacity);
        }
    }
}
