// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_JointInfo
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_JointInfo Create() { return new CAD_JointInfo { size = (uint)Marshal.SizeOf(typeof(CAD_JointInfo)) }; }
        public uint size;
        public int type;
        [MarshalAs(UnmanagedType.I1)] public bool hasLimit;
        public double lower;
        public double upper;
        public double value;
        public CAD_GeVec3 origin;
        public CAD_GeVec3 axis;
    }

    public static partial class CadApi
    {
        public const int CAD_JOINT_FIXED = 0;
        public const int CAD_JOINT_REVOLUTE = 1;
        public const int CAD_JOINT_CONTINUOUS = 2;
        public const int CAD_JOINT_PRISMATIC = 3;

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_LoadUrdf([MarshalAs(UnmanagedType.LPUTF8Str)] string path, out uint outRobot);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetRobotCount();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetJointCount(uint robot);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_FindJoint(uint robot, [MarshalAs(UnmanagedType.LPUTF8Str)] string jointName, out int outJoint);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetJointName(uint robot, int joint, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetJointValue(uint robot, int joint, double value, out double outApplied);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetJointValue(uint robot, int joint, out double outValue);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetJointValues(uint robot, int[] joints, double[] values, uint count);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetJointValuesByName(uint robot, IntPtr[] names, double[] values, uint count);

        /// <summary>CAD_SetJointValuesByName — string[] 를 UTF-8 로 바꿔 넘기는 편의 오버로드.</summary>
        public static int CAD_SetJointValuesByName(uint robot, string[] names, double[] values, uint count)
        {
            using (var names_utf8 = new Utf8StringArray(names))
            {
                return CAD_SetJointValuesByName(robot, names_utf8.Pointers, values, count);
            }
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetJointInfo(uint robot, int joint, ref CAD_JointInfo @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetJointAxis(uint robot, int joint, CAD_GeVec3 axis);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetJointType(uint robot, int joint, int type);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetJointOrigin(uint robot, int joint, CAD_GeVec3 position);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetLinkObject(uint robot, [MarshalAs(UnmanagedType.LPUTF8Str)] string linkName, out uint outId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClearRobots();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_RigAttach(uint parentObj, uint childObj, CAD_GeVec3 axis, int type, CAD_GeVec3[] pivot);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_RigDetach(uint obj);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetObjectRobot(uint obj, out uint outRobot);
    }
}
