// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_SketchConstraintInfo
    {
        public uint id;
        public int type;
        public uint entityA;
        public int pointA;
        public uint entityB;
        public int pointB;
        public float value;
        [MarshalAs(UnmanagedType.I1)] public bool driving;
        [MarshalAs(UnmanagedType.I1)] public bool enabled;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_CurveCreateOptions
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_CurveCreateOptions Create() { return new CAD_CurveCreateOptions { size = (uint)Marshal.SizeOf(typeof(CAD_CurveCreateOptions)) }; }
        public uint size;
        public uint propsFrom;
    }

    public static partial class CadApi
    {
        public const int CAD_SKETCH_WHOLE_ENTITY = 255;
        public const int CAD_SKETCH_COINCIDENT = 0;
        public const int CAD_SKETCH_HORIZONTAL = 1;
        public const int CAD_SKETCH_VERTICAL = 2;
        public const int CAD_SKETCH_CONCENTRIC = 3;
        public const int CAD_SKETCH_DISTANCE = 4;
        public const int CAD_SKETCH_RADIUS = 5;
        public const int CAD_SKETCH_DIAMETER = 6;
        public const int CAD_SKETCH_PARALLEL = 7;
        public const int CAD_SKETCH_PERPENDICULAR = 8;
        public const int CAD_SKETCH_EQUAL = 9;
        public const int CAD_SKETCH_FIXED = 10;
        public const int CAD_SKETCH_ANGLE = 11;
        public const int CAD_SKETCH_TANGENT = 12;
        public const int CAD_SKETCH_DISTANCE_X = 13;
        public const int CAD_SKETCH_DISTANCE_Y = 14;
        public const int CAD_SKETCH_UNDER = 0;
        public const int CAD_SKETCH_WELL = 1;
        public const int CAD_SKETCH_REDUNDANT = 2;
        public const int CAD_SKETCH_CONFLICT = 3;
        public const int CAD_SKETCH_INVALID = 4;

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateLine(float x1, float y1, float z1, float x2, float y2, float z2);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateCircle(float cx, float cy, float cz, float radius, float normalX, float normalY, float normalZ);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_AddSketchConstraint(int type, uint entityA, int pointA, uint entityB, int pointB, float value);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_SetSketchConstraintValue(uint constraintId, float value);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_RemoveSketchConstraint(uint constraintId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_SolveSketchConstraints();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_GetSketchConstraintCount();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_GetSketchConstraintIds(uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_GetSketchConstraintInfo(uint constraintId, out CAD_SketchConstraintInfo outInfo);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSketchDiagnosis(uint entityId, out int outDof, out int outStatus, uint[] outProblemIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_GetLastSketchConflict(uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreatePolygon(float cx, float cy, float cz, float radius, int sides, float normalX, float normalY, float normalZ, float firstVertexDirX, float firstVertexDirY, float firstVertexDirZ);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateArc(float startX, float startY, float startZ, float throughX, float throughY, float throughZ, float endX, float endY, float endZ);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreatePolyline(float[] xyz, uint pointCount, [MarshalAs(UnmanagedType.I1)] bool closed);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateRectangle(float x0, float y0, float z0, float x2, float y2, float z2);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_GetPolylinePoints(uint id, float[] outXyz, uint cap, [MarshalAs(UnmanagedType.I1)] out bool outClosed);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_SetPolylinePoints(uint id, float[] xyz, uint count, [MarshalAs(UnmanagedType.I1)] bool closed);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateEllipse(float cx, float cy, float cz, float majorX, float majorY, float majorZ, float ratio, float normalX, float normalY, float normalZ);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_CreateSpline(float[] fitXYZ, uint count, [MarshalAs(UnmanagedType.I1)] bool closed);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CurveGetGeCurve(uint id, out ulong outCurve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CurveSetFromGeCurve(uint id, ulong curve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateCurveFromGe(ulong curve, CAD_CurveCreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateCurveFromGe — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateCurveFromGe(ulong curve, out uint outId)
        {
            return CAD_CreateCurveFromGe(curve, null, out outId);
        }
        /// <summary>CAD_CreateCurveFromGe — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateCurveFromGe(ulong curve, CAD_CurveCreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CurveCreateOptions));
            return CAD_CreateCurveFromGe(curve, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CurveGetInterval(uint id, out double outStartParam, out double outEndParam);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CurveIsClosed(uint id, [MarshalAs(UnmanagedType.I1)] out bool outClosed);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CurveEvaluate(uint id, double param, out CAD_GeVec3 outPoint, out CAD_GeVec3 outFirstDeriv, out CAD_GeVec3 outSecondDeriv);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CurveParamAtPoint(uint id, CAD_GeVec3 p, out double outParam);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CurveLength(uint id, double fromParam, double toParam, out double outLength);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CurveParamAtLength(uint id, double fromParam, double length, out double outParam);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CurveClosestPoint(uint id, CAD_GeVec3 p, [MarshalAs(UnmanagedType.I1)] bool extend, out double outParam, out CAD_GeVec3 outPoint, out double outDistance);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CurveArea(uint id, out double outArea);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CurveIntersect(uint id1, uint id2, int extendMode, CAD_GeVec3 viewDir, [Out] CAD_GeIntersection[] outHits, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CurveOffset(uint id, double distance, CAD_GeVec3 planeNormal, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CurveSplit(uint id, double[] @params, uint count, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CurveReverse(uint id);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CurveExtendToPoint(uint id, [MarshalAs(UnmanagedType.I1)] bool atStart, CAD_GeVec3 toPoint);
    }
}
