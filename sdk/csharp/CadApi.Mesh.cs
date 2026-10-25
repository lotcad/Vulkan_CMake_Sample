// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_MeshCheckInfo
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_MeshCheckInfo Create() { return new CAD_MeshCheckInfo { size = (uint)Marshal.SizeOf(typeof(CAD_MeshCheckInfo)) }; }
        public uint size;
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

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_MeshRepairOptions
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_MeshRepairOptions Create() { return new CAD_MeshRepairOptions { size = (uint)Marshal.SizeOf(typeof(CAD_MeshRepairOptions)) }; }
        public uint size;
        [MarshalAs(UnmanagedType.I1)] public bool noFill;
        [MarshalAs(UnmanagedType.I1)] public bool flatFill;
    }

    public static partial class CadApi
    {
        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateMesh(CAD_GeVec3[] points, uint pointCount, uint[] indices, uint indexCount, CAD_GeVec3[] normals, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateMesh — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateMesh(CAD_GeVec3[] points, uint pointCount, uint[] indices, uint indexCount, CAD_GeVec3[] normals, out uint outId)
        {
            return CAD_CreateMesh(points, pointCount, indices, indexCount, normals, null, out outId);
        }
        /// <summary>CAD_CreateMesh — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateMesh(CAD_GeVec3[] points, uint pointCount, uint[] indices, uint indexCount, CAD_GeVec3[] normals, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateMesh(points, pointCount, indices, indexCount, normals, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ReplaceMesh(uint id, CAD_GeVec3[] points, uint pointCount, uint[] indices, uint indexCount, CAD_GeVec3[] normals);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateVolumeMesh([MarshalAs(UnmanagedType.LPUTF8Str)] string path, double iso, int step, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateVolumeMesh — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateVolumeMesh(string path, double iso, int step, out uint outId)
        {
            return CAD_CreateVolumeMesh(path, iso, step, null, out outId);
        }
        /// <summary>CAD_CreateVolumeMesh — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateVolumeMesh(string path, double iso, int step, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateVolumeMesh(path, iso, step, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateLabelMeshes([MarshalAs(UnmanagedType.LPUTF8Str)] string path, int step, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreatePointCloud(CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreatePointCloud — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreatePointCloud(out uint outId)
        {
            return CAD_CreatePointCloud(null, out outId);
        }
        /// <summary>CAD_CreatePointCloud — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreatePointCloud(CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreatePointCloud(new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_UpdatePointCloud(uint id, float[] xyz, byte[] rgba, uint count);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetPointCloudSize(uint id, double pointSizePx);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetPointCloudCount(uint id);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CheckMesh(uint id, ref CAD_MeshCheckInfo @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_RepairMeshes(uint[] ids, uint count, CAD_MeshRepairOptions[] opt);

        /// <summary>CAD_RepairMeshes — 선택 없이(전부 기본값).</summary>
        public static int CAD_RepairMeshes(uint[] ids, uint count)
        {
            return CAD_RepairMeshes(ids, count, null);
        }
        /// <summary>CAD_RepairMeshes — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_RepairMeshes(uint[] ids, uint count, CAD_MeshRepairOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_MeshRepairOptions));
            return CAD_RepairMeshes(ids, count, new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SmoothMeshes(uint[] ids, uint count, int iterations);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_DecimateMeshes(uint[] ids, uint count, double ratio);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_StitchMeshes(uint[] ids, uint count, double tolerance);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ThickenMeshes(uint[] ids, uint count, double thickness);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_RemeshMeshes(uint[] ids, uint count, double edgeLength);
    }
}
