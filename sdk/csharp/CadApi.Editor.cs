// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    [UnmanagedFunctionPointer(CallingConvention.Cdecl)]
    public delegate void CAD_CommandFn(IntPtr user);

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_JigDelta
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_JigDelta Create() { return new CAD_JigDelta { size = (uint)Marshal.SizeOf(typeof(CAD_JigDelta)) }; }
        public uint size;
        public int mode;
        public CAD_GeVec3 move;
        public double angle;
        public double scale;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct CAD_SubobjectSelection
    {
        /// <summary>size 를 sizeof 로 채운 새 값(나머지 0).</summary>
        public static CAD_SubobjectSelection Create() { return new CAD_SubobjectSelection { size = (uint)Marshal.SizeOf(typeof(CAD_SubobjectSelection)) }; }
        public uint size;
        public int mode;
        public uint id;
        public int brepFaceId;
        public uint triangleCount;
        public CAD_GeVec3 normal;
        public CAD_GeVec3 center;
        public double area;
        public CAD_GeVec3 edgeStart;
        public CAD_GeVec3 edgeEnd;
    }

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
        public const int CAD_JIG_MOVE = 0;
        public const int CAD_JIG_ROTATE = 1;
        public const int CAD_JIG_SCALE = 2;
        public const int CAD_JIG_COPY = 3;
        public const int CAD_JIG_IDLE = 0;
        public const int CAD_JIG_DRAGGING = 1;
        public const int CAD_JIG_COMMITTED = 2;
        public const int CAD_JIG_CANCELLED = 3;
        public const int CAD_SELECT_REPLACE = 0;
        public const int CAD_SELECT_ADD = 1;
        public const int CAD_SELECT_REMOVE = 2;
        public const int CAD_SUBOBJECT_OBJECT = 0;
        public const int CAD_SUBOBJECT_FACE = 1;
        public const int CAD_SUBOBJECT_EDGE = 2;
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
        public static extern int CAD_JigBegin(int mode, uint[] ids, uint count, CAD_GeVec3 pivot);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_JigBeginOne(int mode, uint id, CAD_GeVec3 pivot);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_JigGetState(out int outState);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_JigCancel();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_JigMoveTo(CAD_GeVec3 point);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_JigCommit();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_JigSetBasePoint(CAD_GeVec3 point);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_JigGetDelta(ref CAD_JigDelta @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_JigBeginVariants(int mode, uint[] ids, uint count, CAD_GeVec3 pivot);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_JigNextVariant();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_JigGetVariant(out int outIndex, out uint outId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_BeginTextEdit(uint id);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetTextEditId(out uint outId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_TextEditInsert([MarshalAs(UnmanagedType.LPUTF8Str)] string utf8);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_TextEditBackspace();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_TextEditDelete();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_TextEditMoveCaret(int delta);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_TextEditCommit();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_TextEditCancel();

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
        public static extern int CAD_SetSubobjectSelectionMode(int mode);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSubobjectSelectionMode(out int outMode);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_PickSubobject(CAD_GeVec3 origin, CAD_GeVec3 direction);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSubobjectSelection(ref CAD_SubobjectSelection @out);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSelectedFaceTriangles(uint[] outTriangles, uint capacity);

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
