// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    public static partial class CadApi
    {
        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraph([MarshalAs(UnmanagedType.LPUTF8Str)] string argsJson, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphGetJson(byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphGetKindsJson(byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphSetJson([MarshalAs(UnmanagedType.LPUTF8Str)] string graphJson);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphClear();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphEvaluate();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphAddNode([MarshalAs(UnmanagedType.LPUTF8Str)] string kind, double x, double y, out uint outNodeId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphRemoveNode(uint nodeId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphMoveNode(uint nodeId, double x, double y);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphConnect(uint fromNode, [MarshalAs(UnmanagedType.LPUTF8Str)] string fromPort, uint toNode, [MarshalAs(UnmanagedType.LPUTF8Str)] string toPort);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphDisconnect(uint toNode, [MarshalAs(UnmanagedType.LPUTF8Str)] string toPort);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphSetNumber(uint nodeId, [MarshalAs(UnmanagedType.LPUTF8Str)] string port, double value);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphSetBool(uint nodeId, [MarshalAs(UnmanagedType.LPUTF8Str)] string port, [MarshalAs(UnmanagedType.I1)] bool value);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphSetText(uint nodeId, [MarshalAs(UnmanagedType.LPUTF8Str)] string port, [MarshalAs(UnmanagedType.LPUTF8Str)] string value);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphSetPoint(uint nodeId, [MarshalAs(UnmanagedType.LPUTF8Str)] string port, CAD_GeVec3 value);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphSetMuted(uint[] nodeIds, uint count, [MarshalAs(UnmanagedType.I1)] bool muted);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphGetNodeObjects(uint nodeId, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_NodeGraphBake(uint[] objectIds, uint count, uint[] outIds, uint capacity);
    }
}
