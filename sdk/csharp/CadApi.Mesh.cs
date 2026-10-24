// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_MeshCheckInfo
    {
        public uint triangles;
        public uint vertices;
        public uint degenerate;
        public uint duplicates;
        public uint openEdges;
        public uint nonManifoldEdges;
        public uint flippedEdges;
        public uint holes;
        public uint components;
        [MarshalAs(UnmanagedType.I1)] public bool closed;
        [MarshalAs(UnmanagedType.I1)] public bool ok;
        public double volume;
        public double area;
    }

    public static partial class CadApi
    {
        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateMesh(float[] xyz, uint vertexCount, uint[] indices, uint indexCount, float[] normals);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_ReplaceMesh(uint id, float[] xyz, uint vertexCount, uint[] indices, uint indexCount, float[] normals);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateVolumeMesh([MarshalAs(UnmanagedType.LPUTF8Str)] string path, float iso, int step);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateLabelMeshes([MarshalAs(UnmanagedType.LPUTF8Str)] string path, int step);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreatePointCloud();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_UpdatePointCloud(uint id, float[] xyz, byte[] rgba, uint count);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_SetPointCloudSize(uint id, float pointSizePx);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_GetPointCloudCount(uint id);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_CheckMesh(uint id, out CAD_MeshCheckInfo @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_RepairMeshes(uint[] ids, uint count, [MarshalAs(UnmanagedType.I1)] bool fillHoles);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_RepairMeshesEx(uint[] ids, uint count, [MarshalAs(UnmanagedType.I1)] bool fillHoles, [MarshalAs(UnmanagedType.I1)] bool curvedFill);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_SmoothMeshes(uint[] ids, uint count, int iterations);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_DecimateMeshes(uint[] ids, uint count, double ratio);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_StitchMeshes(uint[] ids, uint count, float tolerance);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_ThickenMeshes(uint[] ids, uint count, double thickness);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_RemeshMeshes(uint[] ids, uint count, double edgeLength);
    }
}
