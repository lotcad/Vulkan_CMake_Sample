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
        public static extern uint CAD_CreateBox(float x, float y, float z, float sx, float sy, float sz);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_PushPullSelectedFace(float distance);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_InsetSelectedFace(float distance);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateExtrude(uint sourceId, float height);

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
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_Loft();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_Shell(float thickness);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_EdgeFillet(float distance);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_EdgeChamfer(float distance);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_BooleanUnion([MarshalAs(UnmanagedType.I1)] bool keepOriginals);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_BooleanIntersection([MarshalAs(UnmanagedType.I1)] bool keepOriginals);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_BooleanDifference(uint[] baseIds, uint baseCount, uint[] subtractIds, uint subtractCount, [MarshalAs(UnmanagedType.I1)] bool keepOriginals);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_BooleanUnionIds(uint[] ids, uint count, [MarshalAs(UnmanagedType.I1)] bool keepOriginals);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_BooleanIntersectionIds(uint[] ids, uint count, [MarshalAs(UnmanagedType.I1)] bool keepOriginals);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_BooleanSubtract(uint[] baseIds, uint baseCount, uint[] cutIds, uint cutCount, [MarshalAs(UnmanagedType.I1)] bool keepOriginals, [MarshalAs(UnmanagedType.I1)] bool perBase, uint[] outIds, uint cap);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CheckInterference(uint[] ids, uint count, [MarshalAs(UnmanagedType.I1)] bool createObjects, [Out] CAD_InterferenceInfo[] @out, uint cap);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_AddEdgeBevel(uint id, [MarshalAs(UnmanagedType.I1)] bool fillet, float distance, [MarshalAs(UnmanagedType.I1)] bool allEdges, uint brepEdge);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_GetEdgeBevelCount(uint id);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateWedge(float x, float y, float z, float sx, float sy, float sz);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreatePyramid(float x, float y, float z, float radius, float height, int sides, float topRadius);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateSphere(float x, float y, float z, float radius);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateCylinder(float x, float y, float z, float radius, float height);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateCone(float x, float y, float z, float radius, float height);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateTorus(float x, float y, float z, float majorRadius, float minorRadius);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ExplodeView([MarshalAs(UnmanagedType.LPUTF8Str)] string argsJson, byte[] outUtf8, int cap);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateTube(float x, float y, float z, float outerRadius, float innerRadius, float height);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_SetFeatureDimensionsVisible([MarshalAs(UnmanagedType.I1)] bool visible);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_GetFeatureDimensionsVisible();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_GetFeatureDimensionCount(uint id);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_GetFeatureDimension(uint id, uint index, out int outKind, out float outValue, out uint outSketchId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_SetFeatureDimension(uint id, uint index, float value);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_Sweep(uint profileId, uint pathId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_Revolve(uint profileId, float x1, float y1, float z1, float x2, float y2, float z2, int segments);
    }
}
