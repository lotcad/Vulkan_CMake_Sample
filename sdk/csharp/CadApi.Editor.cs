// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate void CAD_CommandFn(IntPtr user);

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_EdInputResult
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_EdInputResult Create() { return new CAD_EdInputResult { size = (uint)Marshal.SizeOf(typeof(CAD_EdInputResult)) }; }
        public uint size;
        public int kind;
        public int status;
        public CAD_GeVec3 point;
        public double value;
        public uint id;
        public int keywordIndex;
        public int idCount;
        public int textLength;
    }

    [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate void CAD_EdInputFn(IntPtr result, IntPtr user);

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_EdInputOptions
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_EdInputOptions Create() { return new CAD_EdInputOptions { size = (uint)Marshal.SizeOf(typeof(CAD_EdInputOptions)) }; }
        public uint size;
        public uint flags;
        [MarshalAs(UnmanagedType.LPUTF8Str)] public string keywords;
        [MarshalAs(UnmanagedType.I1)] public bool hasBase;
        public CAD_GeVec3 @base;
        [MarshalAs(UnmanagedType.I1)] public bool hasDefault;
        public double defaultValue;
        public CAD_GeVec3 defaultPoint;
        [MarshalAs(UnmanagedType.LPUTF8Str)] public string defaultText;
        public CAD_EdInputFn onDone;
        public IntPtr user;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_EdSelectOptions
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_EdSelectOptions Create() { return new CAD_EdSelectOptions { size = (uint)Marshal.SizeOf(typeof(CAD_EdSelectOptions)) }; }
        public uint size;
        [MarshalAs(UnmanagedType.I1)] public bool crossing;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_EdCommandState
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_EdCommandState Create() { return new CAD_EdCommandState { size = (uint)Marshal.SizeOf(typeof(CAD_EdCommandState)) }; }
        public uint size;
        [MarshalAs(UnmanagedType.I1)] public bool commandActive;
        public int inputKind;
    }

    public static partial class CadApi
    {
        public const int CAD_SELECT_REPLACE = 0;
        public const int CAD_SELECT_ADD = 1;
        public const int CAD_SELECT_REMOVE = 2;
        public const int CAD_ED_KIND_POINT = 1;
        public const int CAD_ED_KIND_CORNER = 2;
        public const int CAD_ED_KIND_DISTANCE = 3;
        public const int CAD_ED_KIND_ANGLE = 4;
        public const int CAD_ED_KIND_INTEGER = 5;
        public const int CAD_ED_KIND_REAL = 6;
        public const int CAD_ED_KIND_STRING = 7;
        public const int CAD_ED_KIND_KEYWORD = 8;
        public const int CAD_ED_KIND_ENTITY = 9;
        public const int CAD_ED_KIND_SELECTION = 10;
        public const int CAD_ED_RESULT_PENDING = 0;
        public const int CAD_ED_RESULT_NORMAL = 1;
        public const int CAD_ED_RESULT_NONE = 2;
        public const int CAD_ED_RESULT_KEYWORD = 3;
        public const int CAD_ED_RESULT_CANCEL = 4;
        public const int CAD_ED_NO_NULL = 1;
        public const int CAD_ED_NO_ZERO = 2;
        public const int CAD_ED_NO_NEGATIVE = 4;
        public const int CAD_ED_ARBITRARY = 8;
        public const int CAD_ED_ALLOW_SPACES = 16;
        public const int CAD_ED_PICKFIRST = 32;
        public const int CAD_ED_SINGLE = 64;

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetDimensionPointCount();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetPrompt(byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetTransientMessage(byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ExecuteCommand([MarshalAs(UnmanagedType.LPUTF8Str)] string text);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_RegisterCommand([MarshalAs(UnmanagedType.LPUTF8Str)] string name, [MarshalAs(UnmanagedType.LPUTF8Str)] string title, CAD_CommandFn fn, IntPtr user, uint owner);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_UnregisterCommand([MarshalAs(UnmanagedType.LPUTF8Str)] string name);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_UnregisterCommandsByOwner(uint owner);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetRegisteredCommandCount();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetRegisteredCommandName(uint index, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetRegisteredCommandTitle(uint index, byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_OpenFileDialog();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClearAll();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CycleMaterial();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_RemoveMaterial();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_JigBegin(int mode, uint[] ids, int count, float px, float py, float pz);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_JigBeginOne(int mode, uint id, float px, float py, float pz);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_JigState();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_JigCancel();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_JigMoveTo(float x, float y, float z);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_JigCommit();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_JigSetBasePoint(float x, float y, float z);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_JigGetDelta(out float dx, out float dy, out float dz, out float angleDeg, out float scale);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_JigBeginVariants(int mode, uint[] ids, int count, float px, float py, float pz);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_JigNextVariant();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_JigVariantIndex();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_JigVariantId();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_BeginTextEdit(uint id);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_IsTextEditing();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_TextEditInsert([MarshalAs(UnmanagedType.LPUTF8Str)] string utf8);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_TextEditBackspace();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_TextEditDelete();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_TextEditMoveCaret(int delta);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_TextEditCommit();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern void CAD_TextEditCancel();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSelectionContext(byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSelection(uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetSelection(uint[] ids, uint count, int mode);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetOSnapEnabled([MarshalAs(UnmanagedType.I1)] bool on);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetOSnapEnabled([MarshalAs(UnmanagedType.I1)] out bool outOn);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetOSnapModes(uint mask);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetOSnapModes(out uint outMask);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetOrthoEnabled([MarshalAs(UnmanagedType.I1)] bool on);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetOrthoEnabled([MarshalAs(UnmanagedType.I1)] out bool outOn);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetPolarTracking([MarshalAs(UnmanagedType.I1)] bool on, double increment);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetPolarTracking([MarshalAs(UnmanagedType.I1)] out bool outOn, out double outIncrement);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SnapNearPoint(CAD_GeVec3 point, double radius, uint modes, CAD_OsnapOptions[] opt, out CAD_OsnapPoint outPoint);

        /// <summary>CAD_SnapNearPoint — 선택 없이(전부 기본값).</summary>
        public static int CAD_SnapNearPoint(CAD_GeVec3 point, double radius, uint modes, out CAD_OsnapPoint outPoint)
        {
            return CAD_SnapNearPoint(point, radius, modes, null, out outPoint);
        }
        /// <summary>CAD_SnapNearPoint — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_SnapNearPoint(CAD_GeVec3 point, double radius, uint modes, CAD_OsnapOptions opt, out CAD_OsnapPoint outPoint)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_OsnapOptions));
            return CAD_SnapNearPoint(point, radius, modes, new[] { opt }, out outPoint);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_SetSubobjectSelectionMode(int mode);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSubobjectSelectionMode();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_PickSubobject(float ox, float oy, float oz, float dx, float dy, float dz);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_GetSubobjectSelectionId();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern uint CAD_GetSelectedFaceTriangles(uint[] @out, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSelectedBRepFaceId();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        [return: MarshalAs(UnmanagedType.I1)]
        public static extern bool CAD_GetSelectedEdge(float[] endpoints6);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdGetPoint([MarshalAs(UnmanagedType.LPUTF8Str)] string prompt, CAD_EdInputOptions[] opt);

        /// <summary>CAD_EdGetPoint — 선택 없이(전부 기본값).</summary>
        public static int CAD_EdGetPoint(string prompt)
        {
            return CAD_EdGetPoint(prompt, null);
        }
        /// <summary>CAD_EdGetPoint — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_EdGetPoint(string prompt, CAD_EdInputOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_EdInputOptions));
            return CAD_EdGetPoint(prompt, new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdGetCorner([MarshalAs(UnmanagedType.LPUTF8Str)] string prompt, CAD_GeVec3 @base, CAD_EdInputOptions[] opt);

        /// <summary>CAD_EdGetCorner — 선택 없이(전부 기본값).</summary>
        public static int CAD_EdGetCorner(string prompt, CAD_GeVec3 @base)
        {
            return CAD_EdGetCorner(prompt, @base, null);
        }
        /// <summary>CAD_EdGetCorner — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_EdGetCorner(string prompt, CAD_GeVec3 @base, CAD_EdInputOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_EdInputOptions));
            return CAD_EdGetCorner(prompt, @base, new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdGetDistance([MarshalAs(UnmanagedType.LPUTF8Str)] string prompt, CAD_EdInputOptions[] opt);

        /// <summary>CAD_EdGetDistance — 선택 없이(전부 기본값).</summary>
        public static int CAD_EdGetDistance(string prompt)
        {
            return CAD_EdGetDistance(prompt, null);
        }
        /// <summary>CAD_EdGetDistance — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_EdGetDistance(string prompt, CAD_EdInputOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_EdInputOptions));
            return CAD_EdGetDistance(prompt, new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdGetAngle([MarshalAs(UnmanagedType.LPUTF8Str)] string prompt, CAD_EdInputOptions[] opt);

        /// <summary>CAD_EdGetAngle — 선택 없이(전부 기본값).</summary>
        public static int CAD_EdGetAngle(string prompt)
        {
            return CAD_EdGetAngle(prompt, null);
        }
        /// <summary>CAD_EdGetAngle — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_EdGetAngle(string prompt, CAD_EdInputOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_EdInputOptions));
            return CAD_EdGetAngle(prompt, new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdGetInteger([MarshalAs(UnmanagedType.LPUTF8Str)] string prompt, CAD_EdInputOptions[] opt);

        /// <summary>CAD_EdGetInteger — 선택 없이(전부 기본값).</summary>
        public static int CAD_EdGetInteger(string prompt)
        {
            return CAD_EdGetInteger(prompt, null);
        }
        /// <summary>CAD_EdGetInteger — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_EdGetInteger(string prompt, CAD_EdInputOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_EdInputOptions));
            return CAD_EdGetInteger(prompt, new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdGetReal([MarshalAs(UnmanagedType.LPUTF8Str)] string prompt, CAD_EdInputOptions[] opt);

        /// <summary>CAD_EdGetReal — 선택 없이(전부 기본값).</summary>
        public static int CAD_EdGetReal(string prompt)
        {
            return CAD_EdGetReal(prompt, null);
        }
        /// <summary>CAD_EdGetReal — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_EdGetReal(string prompt, CAD_EdInputOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_EdInputOptions));
            return CAD_EdGetReal(prompt, new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdGetString([MarshalAs(UnmanagedType.LPUTF8Str)] string prompt, CAD_EdInputOptions[] opt);

        /// <summary>CAD_EdGetString — 선택 없이(전부 기본값).</summary>
        public static int CAD_EdGetString(string prompt)
        {
            return CAD_EdGetString(prompt, null);
        }
        /// <summary>CAD_EdGetString — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_EdGetString(string prompt, CAD_EdInputOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_EdInputOptions));
            return CAD_EdGetString(prompt, new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdGetKeyword([MarshalAs(UnmanagedType.LPUTF8Str)] string prompt, CAD_EdInputOptions[] opt);

        /// <summary>CAD_EdGetKeyword — 선택 없이(전부 기본값).</summary>
        public static int CAD_EdGetKeyword(string prompt)
        {
            return CAD_EdGetKeyword(prompt, null);
        }
        /// <summary>CAD_EdGetKeyword — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_EdGetKeyword(string prompt, CAD_EdInputOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_EdInputOptions));
            return CAD_EdGetKeyword(prompt, new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdEntSel([MarshalAs(UnmanagedType.LPUTF8Str)] string prompt, CAD_EdInputOptions[] opt);

        /// <summary>CAD_EdEntSel — 선택 없이(전부 기본값).</summary>
        public static int CAD_EdEntSel(string prompt)
        {
            return CAD_EdEntSel(prompt, null);
        }
        /// <summary>CAD_EdEntSel — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_EdEntSel(string prompt, CAD_EdInputOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_EdInputOptions));
            return CAD_EdEntSel(prompt, new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdSSGet([MarshalAs(UnmanagedType.LPUTF8Str)] string prompt, CAD_EdInputOptions[] opt);

        /// <summary>CAD_EdSSGet — 선택 없이(전부 기본값).</summary>
        public static int CAD_EdSSGet(string prompt)
        {
            return CAD_EdSSGet(prompt, null);
        }
        /// <summary>CAD_EdSSGet — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_EdSSGet(string prompt, CAD_EdInputOptions opt)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_EdInputOptions));
            return CAD_EdSSGet(prompt, new[] { opt });
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdGetInputResult(ref CAD_EdInputResult @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdGetInputText(byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdGetInputIds(uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdCancelInput();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdSelectWindow(CAD_GeVec3 corner1, CAD_GeVec3 corner2, CAD_EdSelectOptions[] opt, uint[] outIds, uint capacity);

        /// <summary>CAD_EdSelectWindow — 선택 없이(전부 기본값).</summary>
        public static int CAD_EdSelectWindow(CAD_GeVec3 corner1, CAD_GeVec3 corner2, uint[] outIds, uint capacity)
        {
            return CAD_EdSelectWindow(corner1, corner2, null, outIds, capacity);
        }
        /// <summary>CAD_EdSelectWindow — 선택 구조체 하나로(size 가 0 이면 sizeof 로 채움).</summary>
        public static int CAD_EdSelectWindow(CAD_GeVec3 corner1, CAD_GeVec3 corner2, CAD_EdSelectOptions opt, uint[] outIds, uint capacity)
        {
            if (opt.size == 0) opt.size = (uint)Marshal.SizeOf(typeof(CAD_EdSelectOptions));
            return CAD_EdSelectWindow(corner1, corner2, new[] { opt }, outIds, capacity);
        }

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdWorldToPixel(CAD_GeVec3 point, out double outX, out double outY);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdPixelToWorld(double x, double y, out CAD_GeVec3 outPoint);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdGetCommandState(ref CAD_EdCommandState @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_EdGetCommandName(byte[] buf, uint capacity);
    }
}
