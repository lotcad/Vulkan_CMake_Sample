// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_BRepInfo
    {
        public int featureType;
        public uint vertexCount;
        public uint edgeCount;
        public uint faceCount;
        public double volume;
        public double surfaceArea;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_BRepParameters
    {
        public int featureType;
        public float dimensionsX;
        public float dimensionsY;
        public float dimensionsZ;
        public float radius;
        public float height;
        public float directionX;
        public float directionY;
        public float directionZ;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_BRepFaceInfo
    {
        public uint faceId;
        public int surfaceType;
        public float originX;
        public float originY;
        public float originZ;
        public float normalX;
        public float normalY;
        public float normalZ;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_BRepCutInfo
    {
        public uint cutIndex;
        public uint pointCount;
        public float depth;
        [MarshalAs(UnmanagedType.I1)] public bool throughAll;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_BooleanCylinderCutInfo
    {
        public uint cutIndex;
        public float centerX;
        public float centerY;
        public float centerZ;
        public float axisX;
        public float axisY;
        public float axisZ;
        public float radius;
        public float height;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_InterferenceInfo
    {
        public uint objectA;
        public uint objectB;
        public double volume;
        public uint resultId;
    }

    public static partial class CadApi
    {
        public const int CAD_MAX_BREP_PROFILE_POINTS = 2048;

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateBox(CAD_GeVec3 center, CAD_GeVec3 size, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateBox — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateBox(CAD_GeVec3 center, CAD_GeVec3 size, out uint outId)
        {
            return CAD_CreateBox(center, size, null, out outId);
        }
        /// <summary>CAD_CreateBox — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateBox(CAD_GeVec3 center, CAD_GeVec3 size, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateBox(center, size, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateWedge(CAD_GeVec3 @base, CAD_GeVec3 size, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateWedge — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateWedge(CAD_GeVec3 @base, CAD_GeVec3 size, out uint outId)
        {
            return CAD_CreateWedge(@base, size, null, out outId);
        }
        /// <summary>CAD_CreateWedge — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateWedge(CAD_GeVec3 @base, CAD_GeVec3 size, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateWedge(@base, size, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreatePyramid(CAD_GeVec3 @base, double radius, double height, int sides, double topRadius, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreatePyramid — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreatePyramid(CAD_GeVec3 @base, double radius, double height, int sides, double topRadius, out uint outId)
        {
            return CAD_CreatePyramid(@base, radius, height, sides, topRadius, null, out outId);
        }
        /// <summary>CAD_CreatePyramid — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreatePyramid(CAD_GeVec3 @base, double radius, double height, int sides, double topRadius, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreatePyramid(@base, radius, height, sides, topRadius, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateSphere(CAD_GeVec3 @base, double radius, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateSphere — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateSphere(CAD_GeVec3 @base, double radius, out uint outId)
        {
            return CAD_CreateSphere(@base, radius, null, out outId);
        }
        /// <summary>CAD_CreateSphere — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateSphere(CAD_GeVec3 @base, double radius, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateSphere(@base, radius, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateCylinder(CAD_GeVec3 @base, double radius, double height, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateCylinder — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateCylinder(CAD_GeVec3 @base, double radius, double height, out uint outId)
        {
            return CAD_CreateCylinder(@base, radius, height, null, out outId);
        }
        /// <summary>CAD_CreateCylinder — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateCylinder(CAD_GeVec3 @base, double radius, double height, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateCylinder(@base, radius, height, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateCone(CAD_GeVec3 @base, double radius, double height, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateCone — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateCone(CAD_GeVec3 @base, double radius, double height, out uint outId)
        {
            return CAD_CreateCone(@base, radius, height, null, out outId);
        }
        /// <summary>CAD_CreateCone — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateCone(CAD_GeVec3 @base, double radius, double height, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateCone(@base, radius, height, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateTorus(CAD_GeVec3 @base, double majorRadius, double minorRadius, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateTorus — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateTorus(CAD_GeVec3 @base, double majorRadius, double minorRadius, out uint outId)
        {
            return CAD_CreateTorus(@base, majorRadius, minorRadius, null, out outId);
        }
        /// <summary>CAD_CreateTorus — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateTorus(CAD_GeVec3 @base, double majorRadius, double minorRadius, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateTorus(@base, majorRadius, minorRadius, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateTube(CAD_GeVec3 @base, double outerRadius, double innerRadius, double height, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateTube — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateTube(CAD_GeVec3 @base, double outerRadius, double innerRadius, double height, out uint outId)
        {
            return CAD_CreateTube(@base, outerRadius, innerRadius, height, null, out outId);
        }
        /// <summary>CAD_CreateTube — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateTube(CAD_GeVec3 @base, double outerRadius, double innerRadius, double height, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateTube(@base, outerRadius, innerRadius, height, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateExtrude(uint profileId, double height, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateExtrude — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateExtrude(uint profileId, double height, out uint outId)
        {
            return CAD_CreateExtrude(profileId, height, null, out outId);
        }
        /// <summary>CAD_CreateExtrude — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateExtrude(uint profileId, double height, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_CreateExtrude(profileId, height, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_Sweep(uint profileId, uint pathId, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_Sweep — 선택 없이(전부 기본값).</summary>
        public static int CAD_Sweep(uint profileId, uint pathId, out uint outId)
        {
            return CAD_Sweep(profileId, pathId, null, out outId);
        }
        /// <summary>CAD_Sweep — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_Sweep(uint profileId, uint pathId, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_Sweep(profileId, pathId, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_Revolve(uint profileId, CAD_GeVec3 axisStart, CAD_GeVec3 axisEnd, int segments, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_Revolve — 선택 없이(전부 기본값).</summary>
        public static int CAD_Revolve(uint profileId, CAD_GeVec3 axisStart, CAD_GeVec3 axisEnd, int segments, out uint outId)
        {
            return CAD_Revolve(profileId, axisStart, axisEnd, segments, null, out outId);
        }
        /// <summary>CAD_Revolve — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_Revolve(uint profileId, CAD_GeVec3 axisStart, CAD_GeVec3 axisEnd, int segments, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_Revolve(profileId, axisStart, axisEnd, segments, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_Loft(uint[] sectionIds, uint count, CAD_CreateOptions[] opt, out uint outId);

        /// <summary>CAD_Loft — 선택 없이(전부 기본값).</summary>
        public static int CAD_Loft(uint[] sectionIds, uint count, out uint outId)
        {
            return CAD_Loft(sectionIds, count, null, out outId);
        }
        /// <summary>CAD_Loft — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_Loft(uint[] sectionIds, uint count, CAD_CreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CreateOptions));
            return CAD_Loft(sectionIds, count, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_PushPullSelectedFace(double distance);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_InsetSelectedFace(double distance);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_GetBRepInfo(uint id, out CAD_BRepInfo outInfo);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_GetBRepParameters(uint id, out CAD_BRepParameters outParams);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_SetBRepBoxDimensions(uint id, float x, float y, float z);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_SetBRepCylinderDimensions(uint id, float radius, float height);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_SetBRepExtrudeHeight(uint id, float height);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_GetBRepFaceInfo(uint id, uint faceId, out CAD_BRepFaceInfo outInfo);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_PushPullBRepFace(uint id, uint faceId, float distance);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_CutExtrudeBRep(uint id, float[] profileXYZ, uint pointCount, float depth, [MarshalAs(UnmanagedType.I1)] bool throughAll);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_CutExtrudeFromSketch(uint id, uint sketchId, float depth, [MarshalAs(UnmanagedType.I1)] bool throughAll);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_BossExtrudeBRep(uint id, float[] profileXYZ, uint pointCount, float height);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_BossExtrudeFromSketch(uint id, uint sketchId, float height);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_GetBRepBossCount(uint id);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_GetBRepBossHeight(uint id, uint bossIndex, out float outHeight);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_SetBRepBossHeight(uint id, uint bossIndex, float height);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_GetBRepCutCount(uint id);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_GetBRepCutInfo(uint id, uint cutIndex, out CAD_BRepCutInfo outInfo);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_GetBRepCutProfile(uint id, uint cutIndex, float[] outXYZ, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_SetBRepCut(uint id, uint cutIndex, float[] profileXYZ, uint pointCount, float depth, [MarshalAs(UnmanagedType.I1)] bool throughAll);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_SetBRepCutFromSketch(uint id, uint cutIndex, uint sketchId, float depth, [MarshalAs(UnmanagedType.I1)] bool throughAll);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_RemoveBRepFeatures(uint id, uint[] cutIndices, uint cutCount, uint[] bossIndices, uint bossCount);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_RemoveBRepCut(uint id, uint cutIndex);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_RemoveBRepBoss(uint id, uint bossIndex);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_GetBooleanCylinderCutCount(uint id);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_GetBooleanCylinderCutInfo(uint id, uint cutIndex, out CAD_BooleanCylinderCutInfo outInfo);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_SetBooleanCylinderCut(uint id, uint cutIndex, float centerX, float centerY, float centerZ, float axisX, float axisY, float axisZ, float radius, float height);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_RebuildBRepMesh(uint id, uint curvedSegments);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_Shell(uint[] ids, uint count, double thickness, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdgeFillet(uint[] ids, uint count, double distance, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdgeChamfer(uint[] ids, uint count, double distance, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_AddEdgeBevel(uint id, [MarshalAs(UnmanagedType.I1)] bool fillet, double distance, [MarshalAs(UnmanagedType.I1)] bool allEdges, uint brepEdge);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetEdgeBevelCount(uint id);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_BooleanUnion(uint[] ids, uint count, [MarshalAs(UnmanagedType.I1)] bool keepOriginals, out uint outId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_BooleanIntersection(uint[] ids, uint count, [MarshalAs(UnmanagedType.I1)] bool keepOriginals, out uint outId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_BooleanSubtract(uint[] baseIds, uint baseCount, uint[] cutIds, uint cutCount, [MarshalAs(UnmanagedType.I1)] bool keepOriginals, [MarshalAs(UnmanagedType.I1)] bool perBase, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CheckInterference(uint[] ids, uint count, [MarshalAs(UnmanagedType.I1)] bool createObjects, [Out] CAD_InterferenceInfo[] @out, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ExplodeView([MarshalAs(UnmanagedType.LPUTF8Str)] string argsJson, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetFeatureDimensionsVisible([MarshalAs(UnmanagedType.I1)] bool visible);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetFeatureDimensionsVisible([MarshalAs(UnmanagedType.I1)] out bool outVisible);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetFeatureDimensionCount(uint id);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetFeatureDimension(uint id, uint index, out int outKind, out double outValue, out uint outSketchId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetFeatureDimension(uint id, uint index, double value);
    }
}
