// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_OsnapPoint
    {
        public double x;
        public double y;
        public double z;
        public uint mode;
        public uint id;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_OsnapOptions
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_OsnapOptions Create() { return new CAD_OsnapOptions { size = (uint)Marshal.SizeOf(typeof(CAD_OsnapOptions)) }; }
        public uint size;
        [MarshalAs(UnmanagedType.I1)] public bool hasPickPoint;
        [MarshalAs(UnmanagedType.I1)] public bool hasLastPoint;
        public double pickX;
        public double pickY;
        public double pickZ;
        public double lastX;
        public double lastY;
        public double lastZ;
    }

    public static partial class CadApi
    {
        public const int CAD_OSNAP_END = 1;
        public const int CAD_OSNAP_MID = 2;
        public const int CAD_OSNAP_CEN = 4;
        public const int CAD_OSNAP_FACE = 8;
        public const int CAD_OSNAP_NODE = 16;
        public const int CAD_OSNAP_QUA = 32;
        public const int CAD_OSNAP_INT = 64;
        public const int CAD_OSNAP_PER = 128;
        public const int CAD_OSNAP_TAN = 256;
        public const int CAD_OSNAP_NEA = 512;
        public const int CAD_OSNAP_ALL = 1023;

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetObjectJson(uint id, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetObjectProperty(uint id, [MarshalAs(UnmanagedType.LPUTF8Str)] string key, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetObjectProperty(uint id, [MarshalAs(UnmanagedType.LPUTF8Str)] string key, [MarshalAs(UnmanagedType.LPUTF8Str)] string valueJson);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetLastError(byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_QueryObjects([MarshalAs(UnmanagedType.LPUTF8Str)] string filterJson, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SelectByQuery([MarshalAs(UnmanagedType.LPUTF8Str)] string filterJson, [MarshalAs(UnmanagedType.I1)] bool additive, out uint outSelected);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSceneJson(int maxObjects, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_DeleteObject(uint id);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetObjectCount();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetObjectIds(uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetObjectKind(uint id, out int outKind);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ObjectExists(uint id, [MarshalAs(UnmanagedType.I1)] out bool outExists);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetPosition(uint id, out CAD_GeVec3 outPosition);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetPosition(uint id, CAD_GeVec3 position);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetScale(uint id, out CAD_GeVec3 outScale);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetScale(uint id, CAD_GeVec3 scale);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetRotationAxisAngle(uint id, out CAD_GeVec3 outAxis, out double outAngle);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetRotationAxisAngle(uint id, CAD_GeVec3 axis, double angle);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetTransform(uint id, out CAD_GeMatrix outMatrix);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetTransform(uint id, CAD_GeMatrix m);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetObjectName(uint id, [MarshalAs(UnmanagedType.LPUTF8Str)] string name);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetObjectName(uint id, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_FindObjectByName([MarshalAs(UnmanagedType.LPUTF8Str)] string name, out uint outId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetObjectVisible(uint id, [MarshalAs(UnmanagedType.I1)] bool visible);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_IsObjectVisible(uint id, [MarshalAs(UnmanagedType.I1)] out bool outVisible);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetColor(uint id, out CAD_Color outColor);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetColor(uint id, CAD_Color color);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetObjectEffectiveColor(uint id, out CAD_Color outColor);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetObjectColorByLayer(uint id, [MarshalAs(UnmanagedType.I1)] bool byLayer);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetObjectColorByLayer(uint id, [MarshalAs(UnmanagedType.I1)] out bool outByLayer);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetSelectedColorByLayer([MarshalAs(UnmanagedType.I1)] bool byLayer, out uint outChanged);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetObjectOpacity(uint id, double opacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetObjectOpacity(uint id, out double outOpacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetSelectedOpacity(double opacity, out uint outChanged);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetObjectLayer(uint objectId, uint layerId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetObjectLayer(uint objectId, out uint outLayerId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_AssignSelectedToLayer(uint layerId, out uint outChanged);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetBoundsWorld(uint id, out CAD_GeVec3 outMin, out CAD_GeVec3 outMax);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetCenterWorld(uint id, out CAD_GeVec3 outCenter);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetLength(uint id, out double outLength);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetArea(uint id, out double outArea);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSelectionLength(out double outLength);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSelectionArea(out double outArea);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ApplyMaterial(uint id, [MarshalAs(UnmanagedType.LPUTF8Str)] string name);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetMaterialCount();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetMaterialName(uint index, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EntityTransform(uint[] ids, uint count, CAD_GeMatrix m);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EntityMove(uint[] ids, uint count, CAD_GeVec3 offset);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EntityRotate(uint[] ids, uint count, CAD_GeVec3 basePoint, CAD_GeVec3 axis, double angle);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EntityScale(uint[] ids, uint count, CAD_GeVec3 basePoint, double factor);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EntityCopy(uint[] ids, uint count, CAD_GeMatrix m, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EntityErase(uint[] ids, uint count);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EntityExplode(uint[] ids, uint count, [MarshalAs(UnmanagedType.I1)] bool keepOriginal, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EntityArrayRect(uint[] ids, uint count, uint cols, uint rows, uint levels, CAD_GeVec3 colStep, CAD_GeVec3 rowStep, CAD_GeVec3 levelStep, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EntityArrayPolar(uint[] ids, uint count, uint itemCount, double fillAngle, CAD_GeVec3 axisPoint, CAD_GeVec3 axisDir, [MarshalAs(UnmanagedType.I1)] bool rotateItems, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EntityMirror(uint[] ids, uint count, CAD_GePlane plane, [MarshalAs(UnmanagedType.I1)] bool eraseSource, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EntityGetExtents(uint id, out CAD_GeVec3 outMin, out CAD_GeVec3 outMax);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EntityGetOsnapPoints(uint id, uint modes, CAD_OsnapOptions[] opt, [Out] CAD_OsnapPoint[] outPoints, uint capacity);

        /// <summary>CAD_EntityGetOsnapPoints — 선택 없이(전부 기본값).</summary>
        public static int CAD_EntityGetOsnapPoints(uint id, uint modes, CAD_OsnapPoint[] outPoints, uint capacity)
        {
            return CAD_EntityGetOsnapPoints(id, modes, null, outPoints, capacity);
        }
        /// <summary>CAD_EntityGetOsnapPoints — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_EntityGetOsnapPoints(uint id, uint modes, CAD_OsnapOptions opt, CAD_OsnapPoint[] outPoints, uint capacity)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_OsnapOptions));
            return CAD_EntityGetOsnapPoints(id, modes, new[] { opt }, outPoints, capacity);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EntityGetGripPoints(uint id, [Out] CAD_GeVec3[] outPoints, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EntityMoveGripPoints(uint id, uint[] indices, uint count, CAD_GeVec3 offset);
    }
}
