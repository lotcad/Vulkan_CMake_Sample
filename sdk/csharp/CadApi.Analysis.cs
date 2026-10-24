// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_SimOptions
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_SimOptions Create() { return new CAD_SimOptions { size = (uint)Marshal.SizeOf(typeof(CAD_SimOptions)) }; }
        public uint size;
        public int type;
        public int material;
        public double youngsModulus;
        public double poissonRatio;
        public double yieldStrength;
        public double density;
        public double conductivity;
        public double expansion;
        public int meshQuality;
        public double elementSize;
        public int units;
        public int modeCount;
        [MarshalAs(UnmanagedType.I1)] public bool thermalLoad;
        public double referenceTemperature;
        [MarshalAs(UnmanagedType.I1)] public bool windLoad;
        public double windSpeed;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_SimCondition
    {
        public int face;
        public int kind;
        public uint fixAxes;
        public double fx;
        public double fy;
        public double fz;
        public double value;
        public double ambient;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_SimFace
    {
        public double area;
        public double cx;
        public double cy;
        public double cz;
        public double nx;
        public double ny;
        public double nz;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_SimState
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_SimState Create() { return new CAD_SimState { size = (uint)Marshal.SizeOf(typeof(CAD_SimState)) }; }
        public uint size;
        [MarshalAs(UnmanagedType.I1)] public bool open;
        public uint target;
        public int faceCount;
        public int conditionCount;
        [MarshalAs(UnmanagedType.I1)] public bool busy;
        public int stage;
        public double fraction;
        [MarshalAs(UnmanagedType.I1)] public bool hasResult;
        public int resultType;
        [MarshalAs(UnmanagedType.I1)] public bool lastRunFailed;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_SimSummary
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_SimSummary Create() { return new CAD_SimSummary { size = (uint)Marshal.SizeOf(typeof(CAD_SimSummary)) }; }
        public uint size;
        public int type;
        public int nodeCount;
        public int elementCount;
        public int boundaryTriangleCount;
        public double elementSize;
        public double minDihedralDeg;
        public double meshSeconds;
        public double solveSeconds;
        public double maxVonMises;
        public double maxDisplacement;
        public double safetyFactor;
        public int maxVonMisesNode;
        public int maxDisplacementNode;
        public double appliedX;
        public double appliedY;
        public double appliedZ;
        public double reactionX;
        public double reactionY;
        public double reactionZ;
        public double strainEnergy;
        public double minTemperature;
        public double maxTemperature;
        public double maxHeatFlux;
        public double heatIn;
        public double heatFixed;
        public double heatConvection;
        public int modeCount;
        public double windForceX;
        public double windForceY;
        public double windForceZ;
        public double windCpMin;
        public double windCpMax;
        public int convergenceCount;
        public double coarseElementSize;
        public int coarseElementCount;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_SimConvergence
    {
        public int metric;
        public double coarse;
        public double fine;
        public double change;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_SimRunOptions
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_SimRunOptions Create() { return new CAD_SimRunOptions { size = (uint)Marshal.SizeOf(typeof(CAD_SimRunOptions)) }; }
        public uint size;
        [MarshalAs(UnmanagedType.I1)] public bool checkConvergence;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_WindOptions
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_WindOptions Create() { return new CAD_WindOptions { size = (uint)Marshal.SizeOf(typeof(CAD_WindOptions)) }; }
        public uint size;
        public int grid;
        public double wind;
        [MarshalAs(UnmanagedType.I1)] public bool pipe;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_WindState
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_WindState Create() { return new CAD_WindState { size = (uint)Marshal.SizeOf(typeof(CAD_WindState)) }; }
        public uint size;
        [MarshalAs(UnmanagedType.I1)] public bool active;
        [MarshalAs(UnmanagedType.I1)] public bool starting;
        [MarshalAs(UnmanagedType.I1)] public bool running;
        [MarshalAs(UnmanagedType.I1)] public bool failed;
        [MarshalAs(UnmanagedType.I1)] public bool pipe;
        public long steps;
        public double stepsPerSecond;
        public int nx;
        public int ny;
        public int nz;
        public double cellSize;
        public CAD_GeVec3 origin;
        public double wind;
        public double reynolds;
        public double dragCoefficient;
        public CAD_GeVec3 forceCoefficient;
        public double frontalArea;
        public int objectCount;
        public int pipeOpenings;
        public long fluidCells;
        public int regrids;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_WindViewOptions
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_WindViewOptions Create() { return new CAD_WindViewOptions { size = (uint)Marshal.SizeOf(typeof(CAD_WindViewOptions)) }; }
        public uint size;
        public int field;
        public int planeAxis;
        public double planeAt;
        [MarshalAs(UnmanagedType.I1)] public bool planeShown;
        [MarshalAs(UnmanagedType.I1)] public bool smoke;
        [MarshalAs(UnmanagedType.I1)] public bool surfacePressure;
        public double isoSpeed;
        [MarshalAs(UnmanagedType.I1)] public bool trajectories;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_WindPointValue
    {
        public CAD_GeVec3 velocity;
        public double speed;
        public double pressure;
        [MarshalAs(UnmanagedType.I1)] public bool inFluid;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_WindSurfacePoint
    {
        public CAD_GeVec3 point;
        public CAD_GeVec3 normal;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_WaterOptions
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_WaterOptions Create() { return new CAD_WaterOptions { size = (uint)Marshal.SizeOf(typeof(CAD_WaterOptions)) }; }
        public uint size;
        public int grid;
        public double level;
        [MarshalAs(UnmanagedType.I1)] public bool openTop;
        public double speed;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_WaterState
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_WaterState Create() { return new CAD_WaterState { size = (uint)Marshal.SizeOf(typeof(CAD_WaterState)) }; }
        public uint size;
        [MarshalAs(UnmanagedType.I1)] public bool active;
        [MarshalAs(UnmanagedType.I1)] public bool starting;
        [MarshalAs(UnmanagedType.I1)] public bool running;
        [MarshalAs(UnmanagedType.I1)] public bool failed;
        [MarshalAs(UnmanagedType.I1)] public bool openTop;
        public uint container;
        public long steps;
        public double stepsPerSecond;
        public int nx;
        public int ny;
        public int nz;
        public double cellSize;
        public CAD_GeVec3 origin;
        public double tiltX;
        public double tiltY;
        public double shake;
        public double shakePeriod;
        public double resonancePeriod;
        public double massDrift;
        public double spilledFraction;
        public int surfaceTriangleCount;
        public int floaterCount;
        public int restarts;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_WaterFloater
    {
        public uint id;
        public double density;
        public CAD_GeVec3 center;
        public CAD_GeVec3 velocity;
        public double submerged;
        public double tilt;
        public int wallContacts;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_WaterPointValue
    {
        public double fill;
        public CAD_GeVec3 velocity;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_ClothOptions
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_ClothOptions Create() { return new CAD_ClothOptions { size = (uint)Marshal.SizeOf(typeof(CAD_ClothOptions)) }; }
        public uint size;
        public int mode;
        public int fabric;
        public int resolution;
        public double sizeFactor;
        public double windSpeed;
        public double gust;
        [MarshalAs(UnmanagedType.I1)] public bool fast;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_ClothState
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_ClothState Create() { return new CAD_ClothState { size = (uint)Marshal.SizeOf(typeof(CAD_ClothState)) }; }
        public uint size;
        [MarshalAs(UnmanagedType.I1)] public bool active;
        [MarshalAs(UnmanagedType.I1)] public bool starting;
        [MarshalAs(UnmanagedType.I1)] public bool running;
        [MarshalAs(UnmanagedType.I1)] public bool failed;
        public int mode;
        public int fabric;
        public int pointCount;
        public int triangleCount;
        public int obstacleCount;
        [MarshalAs(UnmanagedType.I1)] public bool rodGiven;
        public double time;
        public double stepMs;
        public double realtime;
        public double meanStretch;
        public double maxStretch;
        public double maxSpeed;
        public double thickness;
        public double unitToMeter;
    }

    public static partial class CadApi
    {
        public const int CAD_SIM_STRESS = 0;
        public const int CAD_SIM_HEAT = 1;
        public const int CAD_SIM_MODAL = 2;
        public const int CAD_SIM_BUCKLING = 3;
        public const int CAD_SIM_MAT_STEEL = 0;
        public const int CAD_SIM_MAT_ALUMINUM = 1;
        public const int CAD_SIM_MAT_STAINLESS = 2;
        public const int CAD_SIM_MAT_TITANIUM = 3;
        public const int CAD_SIM_MAT_ABS = 4;
        public const int CAD_SIM_MAT_CUSTOM = 100;
        public const int CAD_SIM_MESH_NORMAL = 0;
        public const int CAD_SIM_MESH_FAST = 1;
        public const int CAD_SIM_MESH_FINE = 2;
        public const int CAD_SIM_UNITS_AUTO = 0;
        public const int CAD_SIM_UNITS_MM = 1;
        public const int CAD_SIM_UNITS_M = 2;
        public const int CAD_SIM_FIX = 1;
        public const int CAD_SIM_FORCE = 2;
        public const int CAD_SIM_PRESSURE = 3;
        public const int CAD_SIM_TEMPERATURE = 4;
        public const int CAD_SIM_HEAT_FLOW = 5;
        public const int CAD_SIM_CONVECTION = 6;
        public const int CAD_SIM_AXIS_X = 1;
        public const int CAD_SIM_AXIS_Y = 2;
        public const int CAD_SIM_AXIS_Z = 4;
        public const int CAD_SIM_STAGE_IDLE = -1;
        public const int CAD_SIM_STAGE_MESH = 0;
        public const int CAD_SIM_STAGE_CURVE = 1;
        public const int CAD_SIM_STAGE_ASSEMBLE = 2;
        public const int CAD_SIM_STAGE_SOLVE = 3;
        public const int CAD_SIM_FIELD_DISPLACEMENT = 1;
        public const int CAD_SIM_FIELD_VON_MISES = 2;
        public const int CAD_SIM_FIELD_STRESS = 3;
        public const int CAD_SIM_FIELD_SAFETY = 4;
        public const int CAD_SIM_FIELD_TEMPERATURE = 5;
        public const int CAD_SIM_FIELD_HEAT_FLUX = 6;
        public const int CAD_SIM_METRIC_MAX_VON_MISES = 1;
        public const int CAD_SIM_METRIC_MAX_DISPLACEMENT = 2;
        public const int CAD_SIM_METRIC_MAX_TEMPERATURE = 3;
        public const int CAD_SIM_METRIC_MIN_TEMPERATURE = 4;
        public const int CAD_SIM_METRIC_MAX_HEAT_FLUX = 5;
        public const int CAD_SIM_METRIC_FREQUENCY = 6;
        public const int CAD_SIM_METRIC_LOAD_FACTOR = 7;
        public const int CAD_WIND_GRID_NORMAL = 0;
        public const int CAD_WIND_GRID_FAST = 1;
        public const int CAD_WIND_GRID_FINE = 2;
        public const int CAD_WIND_FIELD_SPEED = 0;
        public const int CAD_WIND_FIELD_PRESSURE = 1;
        public const int CAD_WIND_FIELD_VORTICITY = 2;
        public const int CAD_WIND_FIELD_SMOKE = 3;
        public const int CAD_WIND_CELL_VELOCITY = 1;
        public const int CAD_WIND_CELL_PRESSURE = 2;
        public const int CAD_WIND_CELL_SOLID = 3;
        public const int CAD_WATER_GRID_NORMAL = 0;
        public const int CAD_WATER_GRID_FAST = 1;
        public const int CAD_WATER_GRID_FINE = 2;
        public const int CAD_WATER_CELL_FILL = 1;
        public const int CAD_WATER_CELL_VELOCITY = 2;
        public const int CAD_WATER_CELL_SOLID = 3;
        public const int CAD_CLOTH_DRAPE = 0;
        public const int CAD_CLOTH_CURTAIN = 1;
        public const int CAD_CLOTH_FABRIC_COTTON = 0;
        public const int CAD_CLOTH_FABRIC_SILK = 1;
        public const int CAD_CLOTH_FABRIC_DENIM = 2;
        public const int CAD_CLOTH_FABRIC_LEATHER = 3;
        public const int CAD_CLOTH_RES_NORMAL = 0;
        public const int CAD_CLOTH_RES_FAST = 1;
        public const int CAD_CLOTH_RES_FINE = 2;

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WindTunnel([MarshalAs(UnmanagedType.LPUTF8Str)] string argsJson, byte[] outUtf8, int cap);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_Water([MarshalAs(UnmanagedType.LPUTF8Str)] string argsJson, byte[] outUtf8, int cap);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_StructuralAnalysis([MarshalAs(UnmanagedType.LPUTF8Str)] string argsJson, byte[] outUtf8, int cap);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimOpen(uint id);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimClose();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimClear();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimGetOptions(ref CAD_SimOptions @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimSetOptions(CAD_SimOptions[] opt);

        /// <summary>CAD_SimSetOptions — 선택 없이(전부 기본값).</summary>
        public static int CAD_SimSetOptions()
        {
            return CAD_SimSetOptions(null);
        }
        /// <summary>CAD_SimSetOptions — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_SimSetOptions(CAD_SimOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_SimOptions));
            return CAD_SimSetOptions(new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimGetFaces([Out] CAD_SimFace[] outFaces, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimFindFace(CAD_GeVec3 point, out int outFace);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimSetCondition(CAD_SimCondition condition);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimClearCondition(int face, int kind);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimGetConditions([Out] CAD_SimCondition[] outConditions, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimRun(CAD_SimRunOptions[] opt);

        /// <summary>CAD_SimRun — 선택 없이(전부 기본값).</summary>
        public static int CAD_SimRun()
        {
            return CAD_SimRun(null);
        }
        /// <summary>CAD_SimRun — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_SimRun(CAD_SimRunOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_SimRunOptions));
            return CAD_SimRun(new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimCancel();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimWait(double timeoutSeconds, [MarshalAs(UnmanagedType.I1)] out bool outDone);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimGetState(ref CAD_SimState @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimGetSummary(ref CAD_SimSummary @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimGetNodes([Out] CAD_GeVec3[] outNodes, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimGetElements(uint[] outNodeIndices, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimGetBoundary(uint[] outNodeIndices, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimGetBoundaryFaces(int[] outFaces, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimGetNodeField(int field, double[] outValues, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimGetModes(double[] outValues, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimGetModeShape(int mode, [Out] CAD_GeVec3[] outShape, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimGetFaceHeat(int face, out double outWatts);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SimGetConvergence([Out] CAD_SimConvergence[] outItems, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WindOpen(uint[] ids, uint count, CAD_WindOptions[] opt);

        /// <summary>CAD_WindOpen — 선택 없이(전부 기본값).</summary>
        public static int CAD_WindOpen(uint[] ids, uint count)
        {
            return CAD_WindOpen(ids, count, null);
        }
        /// <summary>CAD_WindOpen — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_WindOpen(uint[] ids, uint count, CAD_WindOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_WindOptions));
            return CAD_WindOpen(ids, count, new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WindClose();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WindGetOptions(ref CAD_WindOptions @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WindSetOptions(CAD_WindOptions[] opt);

        /// <summary>CAD_WindSetOptions — 선택 없이(전부 기본값).</summary>
        public static int CAD_WindSetOptions()
        {
            return CAD_WindSetOptions(null);
        }
        /// <summary>CAD_WindSetOptions — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_WindSetOptions(CAD_WindOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_WindOptions));
            return CAD_WindSetOptions(new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WindReset();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WindSetRunning([MarshalAs(UnmanagedType.I1)] bool running);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WindAdvance(int steps);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WindGetState(ref CAD_WindState @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WindGetView(ref CAD_WindViewOptions @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WindSetView(CAD_WindViewOptions[] opt);

        /// <summary>CAD_WindSetView — 선택 없이(전부 기본값).</summary>
        public static int CAD_WindSetView()
        {
            return CAD_WindSetView(null);
        }
        /// <summary>CAD_WindSetView — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_WindSetView(CAD_WindViewOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_WindViewOptions));
            return CAD_WindSetView(new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WindGetCellField(int field, double[] outValues, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WindSample(CAD_GeVec3[] points, uint count, [Out] CAD_WindPointValue[] outValues, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WindSurfacePressure(CAD_WindSurfacePoint[] points, uint count, double[] outCp, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WindGetStreamline(CAD_GeVec3 seed, [Out] CAD_GeVec3[] outPoints, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterOpen(uint container, CAD_WaterOptions[] opt);

        /// <summary>CAD_WaterOpen — 선택 없이(전부 기본값).</summary>
        public static int CAD_WaterOpen(uint container)
        {
            return CAD_WaterOpen(container, null);
        }
        /// <summary>CAD_WaterOpen — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_WaterOpen(uint container, CAD_WaterOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_WaterOptions));
            return CAD_WaterOpen(container, new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterClose();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterGetOptions(ref CAD_WaterOptions @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterSetOptions(CAD_WaterOptions[] opt);

        /// <summary>CAD_WaterSetOptions — 선택 없이(전부 기본값).</summary>
        public static int CAD_WaterSetOptions()
        {
            return CAD_WaterSetOptions(null);
        }
        /// <summary>CAD_WaterSetOptions — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_WaterSetOptions(CAD_WaterOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_WaterOptions));
            return CAD_WaterSetOptions(new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterReset();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterSetRunning([MarshalAs(UnmanagedType.I1)] bool running);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterAdvance(int steps);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterSetTilt(double xRadians, double yRadians);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterSetShake(double amplitude, double periodSteps);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterAddFloaters(uint[] ids, uint count, double density);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterClearFloaters([MarshalAs(UnmanagedType.I1)] bool restore);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterGetState(ref CAD_WaterState @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterGetFloaters([Out] CAD_WaterFloater[] outFloaters, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterGetSurfaceVertices([Out] CAD_GeVec3[] outVertices, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterGetSurfaceTriangles(uint[] outIndices, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterGetCellField(int field, double[] outValues, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_WaterSample(CAD_GeVec3[] points, uint count, [Out] CAD_WaterPointValue[] outValues, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClothOpen(uint[] ids, uint count, CAD_ClothOptions[] opt);

        /// <summary>CAD_ClothOpen — 선택 없이(전부 기본값).</summary>
        public static int CAD_ClothOpen(uint[] ids, uint count)
        {
            return CAD_ClothOpen(ids, count, null);
        }
        /// <summary>CAD_ClothOpen — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_ClothOpen(uint[] ids, uint count, CAD_ClothOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_ClothOptions));
            return CAD_ClothOpen(ids, count, new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClothClose();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClothGetOptions(ref CAD_ClothOptions @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClothSetOptions(CAD_ClothOptions[] opt);

        /// <summary>CAD_ClothSetOptions — 선택 없이(전부 기본값).</summary>
        public static int CAD_ClothSetOptions()
        {
            return CAD_ClothSetOptions(null);
        }
        /// <summary>CAD_ClothSetOptions — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_ClothSetOptions(CAD_ClothOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_ClothOptions));
            return CAD_ClothSetOptions(new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClothSetMaterial([MarshalAs(UnmanagedType.LPUTF8Str)] string name);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClothGetMaterial(byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClothReset();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClothSetRunning([MarshalAs(UnmanagedType.I1)] bool running);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClothAdvance(double seconds);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClothGetState(ref CAD_ClothState @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClothGetPoints([Out] CAD_GeVec3[] outPoints, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClothGetNormals([Out] CAD_GeVec3[] outNormals, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClothGetTriangles(uint[] outIndices, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClothBake(out uint outId);
    }
}
