// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_CurveCreateOptions
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_CurveCreateOptions Create() { return new CAD_CurveCreateOptions { size = (uint)Marshal.SizeOf(typeof(CAD_CurveCreateOptions)) }; }
        public uint size;
        public uint propsFrom;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_SketchConstraintInfo
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_SketchConstraintInfo Create() { return new CAD_SketchConstraintInfo { size = (uint)Marshal.SizeOf(typeof(CAD_SketchConstraintInfo)) }; }
        public uint size;
        public uint id;
        public int type;
        public uint entityA;
        public int pointA;
        public uint entityB;
        public int pointB;
        public double value;
        [MarshalAs(UnmanagedType.I1)] public bool driving;
        [MarshalAs(UnmanagedType.I1)] public bool enabled;
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
        public static extern int CAD_CreateLine(CAD_GeVec3 start, CAD_GeVec3 end, CAD_CurveCreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateLine — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateLine(CAD_GeVec3 start, CAD_GeVec3 end, out uint outId)
        {
            return CAD_CreateLine(start, end, null, out outId);
        }
        /// <summary>CAD_CreateLine — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateLine(CAD_GeVec3 start, CAD_GeVec3 end, CAD_CurveCreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CurveCreateOptions));
            return CAD_CreateLine(start, end, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateCircle(CAD_GeVec3 center, double radius, CAD_GeVec3 normal, CAD_CurveCreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateCircle — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateCircle(CAD_GeVec3 center, double radius, CAD_GeVec3 normal, out uint outId)
        {
            return CAD_CreateCircle(center, radius, normal, null, out outId);
        }
        /// <summary>CAD_CreateCircle — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateCircle(CAD_GeVec3 center, double radius, CAD_GeVec3 normal, CAD_CurveCreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CurveCreateOptions));
            return CAD_CreateCircle(center, radius, normal, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateArc(CAD_GeVec3 start, CAD_GeVec3 through, CAD_GeVec3 end, CAD_CurveCreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateArc — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateArc(CAD_GeVec3 start, CAD_GeVec3 through, CAD_GeVec3 end, out uint outId)
        {
            return CAD_CreateArc(start, through, end, null, out outId);
        }
        /// <summary>CAD_CreateArc — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateArc(CAD_GeVec3 start, CAD_GeVec3 through, CAD_GeVec3 end, CAD_CurveCreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CurveCreateOptions));
            return CAD_CreateArc(start, through, end, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreatePolygon(CAD_GeVec3 center, double radius, int sides, CAD_GeVec3 normal, CAD_GeVec3 firstVertexDir, CAD_CurveCreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreatePolygon — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreatePolygon(CAD_GeVec3 center, double radius, int sides, CAD_GeVec3 normal, CAD_GeVec3 firstVertexDir, out uint outId)
        {
            return CAD_CreatePolygon(center, radius, sides, normal, firstVertexDir, null, out outId);
        }
        /// <summary>CAD_CreatePolygon — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreatePolygon(CAD_GeVec3 center, double radius, int sides, CAD_GeVec3 normal, CAD_GeVec3 firstVertexDir, CAD_CurveCreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CurveCreateOptions));
            return CAD_CreatePolygon(center, radius, sides, normal, firstVertexDir, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateRectangle(CAD_GeVec3 corner0, CAD_GeVec3 corner2, CAD_CurveCreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateRectangle — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateRectangle(CAD_GeVec3 corner0, CAD_GeVec3 corner2, out uint outId)
        {
            return CAD_CreateRectangle(corner0, corner2, null, out outId);
        }
        /// <summary>CAD_CreateRectangle — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateRectangle(CAD_GeVec3 corner0, CAD_GeVec3 corner2, CAD_CurveCreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CurveCreateOptions));
            return CAD_CreateRectangle(corner0, corner2, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreatePolyline(CAD_GeVec3[] points, uint count, [MarshalAs(UnmanagedType.I1)] bool closed, CAD_CurveCreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreatePolyline — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreatePolyline(CAD_GeVec3[] points, uint count, bool closed, out uint outId)
        {
            return CAD_CreatePolyline(points, count, closed, null, out outId);
        }
        /// <summary>CAD_CreatePolyline — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreatePolyline(CAD_GeVec3[] points, uint count, bool closed, CAD_CurveCreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CurveCreateOptions));
            return CAD_CreatePolyline(points, count, closed, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateEllipse(CAD_GeVec3 center, CAD_GeVec3 majorAxis, double ratio, CAD_GeVec3 normal, CAD_CurveCreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateEllipse — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateEllipse(CAD_GeVec3 center, CAD_GeVec3 majorAxis, double ratio, CAD_GeVec3 normal, out uint outId)
        {
            return CAD_CreateEllipse(center, majorAxis, ratio, normal, null, out outId);
        }
        /// <summary>CAD_CreateEllipse — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateEllipse(CAD_GeVec3 center, CAD_GeVec3 majorAxis, double ratio, CAD_GeVec3 normal, CAD_CurveCreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CurveCreateOptions));
            return CAD_CreateEllipse(center, majorAxis, ratio, normal, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CreateSpline(CAD_GeVec3[] fitPoints, uint count, [MarshalAs(UnmanagedType.I1)] bool closed, CAD_CurveCreateOptions[] opt, out uint outId);

        /// <summary>CAD_CreateSpline — 선택 없이(전부 기본값).</summary>
        public static int CAD_CreateSpline(CAD_GeVec3[] fitPoints, uint count, bool closed, out uint outId)
        {
            return CAD_CreateSpline(fitPoints, count, closed, null, out outId);
        }
        /// <summary>CAD_CreateSpline — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_CreateSpline(CAD_GeVec3[] fitPoints, uint count, bool closed, CAD_CurveCreateOptions opt, out uint outId)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_CurveCreateOptions));
            return CAD_CreateSpline(fitPoints, count, closed, new[] { opt }, out outId);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetPolylinePoints(uint id, [Out] CAD_GeVec3[] outPoints, uint capacity, [MarshalAs(UnmanagedType.I1)] out bool outClosed);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetPolylinePoints(uint id, CAD_GeVec3[] points, uint count, [MarshalAs(UnmanagedType.I1)] bool closed);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_AddSketchConstraint(int type, uint entityA, int pointA, uint entityB, int pointB, double value, out uint outId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetSketchConstraintValue(uint constraintId, double value);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_RemoveSketchConstraint(uint constraintId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SolveSketchConstraints();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSketchConstraintCount();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSketchConstraintIds(uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSketchConstraintInfo(uint constraintId, ref CAD_SketchConstraintInfo outInfo);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSketchDiagnosis(uint entityId, out int outDof, out int outStatus, uint[] outProblemIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetLastSketchConflict(uint[] outIds, uint capacity);

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
