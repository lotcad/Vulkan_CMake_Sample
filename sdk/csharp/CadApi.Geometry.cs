// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_GeVec3
    {
        public double x;
        public double y;
        public double z;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_GePlane
    {
        public double ox;
        public double oy;
        public double oz;
        public double nx;
        public double ny;
        public double nz;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_GeMatrix
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 16)] public double[] m;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_GeArc
    {
        public double cx;
        public double cy;
        public double cz;
        public double nx;
        public double ny;
        public double nz;
        public double rx;
        public double ry;
        public double rz;
        public double radius;
        public double startAngle;
        public double endAngle;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_GeEllipse
    {
        public double cx;
        public double cy;
        public double cz;
        public double nx;
        public double ny;
        public double nz;
        public double mx;
        public double my;
        public double mz;
        public double majorRadius;
        public double minorRadius;
        public double startAngle;
        public double endAngle;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_GeIntersection
    {
        public double x;
        public double y;
        public double z;
        public double x2;
        public double y2;
        public double z2;
        public double param1;
        public double param2;
        public int overlap;
        public double endX;
        public double endY;
        public double endZ;
        public double endParam1;
        public double endParam2;
    }

    public static partial class CadApi
    {
        public const int CAD_GECURVE_LINE = 1;
        public const int CAD_GECURVE_ARC = 2;
        public const int CAD_GECURVE_ELLIPSE = 3;
        public const int CAD_GECURVE_NURBS = 4;
        public const int CAD_GECURVE_COMPOSITE = 5;
        public const int CAD_GE_EXTEND_NONE = 0;
        public const int CAD_GE_EXTEND_THIS = 1;
        public const int CAD_GE_EXTEND_ARG = 2;
        public const int CAD_GE_EXTEND_BOTH = 3;
        public const int CAD_GEVEC_NONE = 0;
        public const int CAD_GEVEC_CODIRECTIONAL = 1;
        public const int CAD_GEVEC_OPPOSITE = 2;
        public const int CAD_GEVEC_PERPENDICULAR = 3;
        public const int CAD_GEPOS_OUTSIDE = 0;
        public const int CAD_GEPOS_ON = 1;
        public const int CAD_GEPOS_INSIDE = 2;

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeSetTolerance(double equalPoint, double equalVector);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeGetTolerance(out double outEqualPoint, out double outEqualVector);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeVectorAngle(CAD_GeVec3 a, CAD_GeVec3 b, CAD_GeVec3 refAxis, out double outAngle);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeVectorRotate(CAD_GeVec3 v, double angle, CAD_GeVec3 axis, out CAD_GeVec3 outVector);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeVectorPerp(CAD_GeVec3 v, out CAD_GeVec3 outVector);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeVectorRelation(CAD_GeVec3 a, CAD_GeVec3 b, out int outRelation);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GePointRotate(CAD_GeVec3 p, double angle, CAD_GeVec3 axisPoint, CAD_GeVec3 axisDir, out CAD_GeVec3 outPoint);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GePointMirror(CAD_GeVec3 p, CAD_GePlane plane, out CAD_GeVec3 outPoint);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GePointProject(CAD_GeVec3 p, CAD_GePlane plane, CAD_GeVec3 dir, out CAD_GeVec3 outPoint);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GePlaneFrom3Points(CAD_GeVec3 a, CAD_GeVec3 b, CAD_GeVec3 c, out CAD_GePlane outPlane);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GePlaneDistance(CAD_GePlane plane, CAD_GeVec3 p, out double outSignedDistance);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GePlaneAxes(CAD_GePlane plane, out CAD_GeVec3 outXAxis, out CAD_GeVec3 outYAxis);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GePlaneIntersectLine(CAD_GePlane plane, CAD_GeVec3 linePoint, CAD_GeVec3 lineDir, out double outParam, out CAD_GeVec3 outPoint);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GePlaneIntersectPlane(CAD_GePlane a, CAD_GePlane b, out CAD_GeVec3 outPoint, out CAD_GeVec3 outDir);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeLineClosest(CAD_GeVec3 a0, CAD_GeVec3 a1, [MarshalAs(UnmanagedType.I1)] bool segmentA, CAD_GeVec3 b0, CAD_GeVec3 b1, [MarshalAs(UnmanagedType.I1)] bool segmentB, out double outParamA, out double outParamB, out CAD_GeVec3 outPointA, out CAD_GeVec3 outPointB, [MarshalAs(UnmanagedType.I1)] out bool outParallel);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeMatrixIdentity(out CAD_GeMatrix outMatrix);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeMatrixTranslation(CAD_GeVec3 v, out CAD_GeMatrix outMatrix);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeMatrixRotation(double angle, CAD_GeVec3 axis, CAD_GeVec3 center, out CAD_GeMatrix outMatrix);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeMatrixScaling(double scale, CAD_GeVec3 center, out CAD_GeMatrix outMatrix);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeMatrixMirroring(CAD_GePlane plane, out CAD_GeMatrix outMatrix);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeMatrixCoordSys(CAD_GeVec3 origin, CAD_GeVec3 xAxis, CAD_GeVec3 yAxis, CAD_GeVec3 zAxis, out CAD_GeMatrix outMatrix);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeMatrixAlignCoordSys(CAD_GeVec3 fromOrigin, CAD_GeVec3 fromX, CAD_GeVec3 fromY, CAD_GeVec3 fromZ, CAD_GeVec3 toOrigin, CAD_GeVec3 toX, CAD_GeVec3 toY, CAD_GeVec3 toZ, out CAD_GeMatrix outMatrix);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeMatrixPlaneToWorld(CAD_GePlane plane, out CAD_GeMatrix outMatrix);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeMatrixWorldToPlane(CAD_GePlane plane, out CAD_GeMatrix outMatrix);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeMatrixInverse(CAD_GeMatrix m, out CAD_GeMatrix outMatrix);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeMatrixMultiply(CAD_GeMatrix a, CAD_GeMatrix b, out CAD_GeMatrix outMatrix);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeTransformPoints(CAD_GeMatrix m, double[] xyz, uint count, double[] outXyz, uint outCapacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeTransformVectors(CAD_GeMatrix m, double[] xyz, uint count, double[] outXyz, uint outCapacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveCreateLine(CAD_GeVec3 start, CAD_GeVec3 end, out ulong outCurve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveCreateArc(CAD_GeArc arc, out ulong outCurve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveCreateCircle(CAD_GeVec3 center, CAD_GeVec3 normal, double radius, out ulong outCurve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveCreateArc3Points(CAD_GeVec3 start, CAD_GeVec3 through, CAD_GeVec3 end, out ulong outCurve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveCreateArcBulge(CAD_GeVec3 start, CAD_GeVec3 end, double bulge, CAD_GeVec3 normal, out ulong outCurve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveCreateFillet(CAD_GeVec3 pointA, CAD_GeVec3 dirA, CAD_GeVec3 pointB, CAD_GeVec3 dirB, double radius, out ulong outCurve, out double outParamA, out double outParamB);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveCreateEllipse(CAD_GeEllipse ellipse, out ulong outCurve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveCreatePolyline(double[] xyz, uint count, [MarshalAs(UnmanagedType.I1)] bool closed, out ulong outCurve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveCreatePolylineBulge(double[] xyz, uint count, double[] bulges, uint bulgeCount, [MarshalAs(UnmanagedType.I1)] bool closed, CAD_GeVec3 normal, out ulong outCurve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveCreateNurbs(int degree, double[] knots, uint knotCount, double[] controlXyz, uint controlCount, double[] weights, uint weightCount, out ulong outCurve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveCreateInterpolated(double[] xyz, uint count, int degree, out ulong outCurve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveCreateComposite(ulong[] curves, uint count, out ulong outCurve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveCopy(ulong curve, out ulong outCurve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveFree(ulong curve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveLiveCount();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveGetType(ulong curve, out int outType);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveGetInterval(ulong curve, out double outStartParam, out double outEndParam);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveIsClosed(ulong curve, [MarshalAs(UnmanagedType.I1)] out bool outClosed);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveIsPlanar(ulong curve, [MarshalAs(UnmanagedType.I1)] out bool outPlanar, out CAD_GeVec3 outNormal);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveEvaluate(ulong curve, double param, out CAD_GeVec3 outPoint, out CAD_GeVec3 outFirstDeriv, out CAD_GeVec3 outSecondDeriv);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveEvaluateMany(ulong curve, double[] @params, uint count, double[] outXyz, uint outCapacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveParamAtPoint(ulong curve, CAD_GeVec3 p, out double outParam);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveClosestPoint(ulong curve, CAD_GeVec3 p, [MarshalAs(UnmanagedType.I1)] bool extend, out double outParam, out CAD_GeVec3 outPoint, out double outDistance);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveClosestPointAlong(ulong curve, CAD_GeVec3 p, CAD_GeVec3 viewDir, [MarshalAs(UnmanagedType.I1)] bool extend, out double outParam, out CAD_GeVec3 outPoint);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurvePerpendicularPoints(ulong curve, CAD_GeVec3 p, [MarshalAs(UnmanagedType.I1)] bool extend, double[] outParams, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveTangentPoints(ulong curve, CAD_GeVec3 p, CAD_GeVec3 planeNormal, double[] outParams, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveClosestToCurve(ulong curve1, ulong curve2, out double outParamA, out double outParamB, out double outDistance);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveLength(ulong curve, double fromParam, double toParam, out double outLength);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveParamAtLength(ulong curve, double fromParam, double length, out double outParam);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveSampleParams(ulong curve, double chordTolerance, double[] outParams, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveGetBox(ulong curve, out CAD_GeVec3 outMin, out CAD_GeVec3 outMax);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveArea(ulong curve, out double outArea);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveContainsPoint(ulong curve, CAD_GeVec3 p, out int outPosition);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveGetLine(ulong curve, out CAD_GeVec3 outStart, out CAD_GeVec3 outEnd);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveGetArc(ulong curve, out CAD_GeArc outArc);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveGetEllipse(ulong curve, out CAD_GeEllipse outEllipse);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveGetPieceCount(ulong curve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveGetPiece(ulong curve, uint index, out ulong outPiece);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveGetNurbsInfo(ulong curve, out int outDegree, out uint outControlCount, out uint outKnotCount, [MarshalAs(UnmanagedType.I1)] out bool outRational);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveGetNurbsData(ulong curve, double[] outControlXyz, uint controlCapacity, double[] outKnots, uint knotCapacity, double[] outWeights, uint weightCapacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveToNurbs(ulong curve, out ulong outCurve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveReverse(ulong curve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveTransform(ulong curve, CAD_GeMatrix m);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveExtendToPoint(ulong curve, [MarshalAs(UnmanagedType.I1)] bool atStart, CAD_GeVec3 toPoint);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveExtendToParam(ulong curve, double newParam);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveSubCurve(ulong curve, double fromParam, double toParam, out ulong outCurve);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveSplit(ulong curve, double[] @params, uint count, ulong[] outCurves, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveOffset(ulong curve, double distance, CAD_GeVec3 planeNormal, ulong[] outCurves, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveIntersect(ulong curve1, ulong curve2, int extendMode, CAD_GeVec3 viewDir, [Out] CAD_GeIntersection[] outHits, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GeCurveIntersectPlane(ulong curve, CAD_GePlane plane, double[] outParams, uint capacity);
    }
}
