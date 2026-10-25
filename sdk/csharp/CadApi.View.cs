// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;

namespace LotCAD
{
    public static partial class CadApi
    {
        public const int CAD_VIEW_FRONT = 0;
        public const int CAD_VIEW_TOP = 1;
        public const int CAD_VIEW_RIGHT = 2;
        public const int CAD_VIEW_ISOMETRIC = 3;
        public const int CAD_VIEW_LEFT = 4;
        public const int CAD_VIEW_BOTTOM = 5;
        public const int CAD_VIEW_BACK = 6;
        public const int CAD_SECTION_OFF = 0;
        public const int CAD_SECTION_PLANE = 1;
        public const int CAD_SECTION_SLICE = 2;
        public const int CAD_SECTION_BOX = 3;
        public const int CAD_LAYOUT_SINGLE = 0;
        public const int CAD_LAYOUT_DUAL = 1;
        public const int CAD_LAYOUT_TRIPLE = 2;
        public const int CAD_LAYOUT_QUAD = 3;
        public const int CAD_STYLE_SHADED = 0;
        public const int CAD_STYLE_SHADED_EDGE = 1;
        public const int CAD_STYLE_WIREFRAME = 2;
        public const int CAD_STYLE_WIREFRAME_EDGE = 3;
        public const int CAD_STYLE_HIDDEN_LINE = 4;

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ZoomExtents();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_FocusSelected();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetView(int viewType);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetProjection([MarshalAs(UnmanagedType.I1)] bool ortho);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetProjection([MarshalAs(UnmanagedType.I1)] out bool outOrtho);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetViewDirection(CAD_GeVec3 direction);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetViewPivot(CAD_GeVec3 point, int axis);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ClearViewPivot();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetViewPivot(out CAD_GeVec3 outPoint, out int outAxis);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_OrbitCamera(CAD_GeVec3 axis, double angle);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetSection(int mode, int axis, double position, [MarshalAs(UnmanagedType.I1)] bool flip, double thickness);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetSectionBox(CAD_GeVec3 min, CAD_GeVec3 max);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetSectionOptions([MarshalAs(UnmanagedType.I1)] bool showArrows, [MarshalAs(UnmanagedType.I1)] bool selectedOnly);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSectionStateJson(byte[] buf, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_ExtractSectionTo2D([MarshalAs(UnmanagedType.I1)] bool includeBehind, uint[] outIds, uint capacity);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetViewportLayout(int layout);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetViewportLayout();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetActiveViewport(int index);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetActiveViewport();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetGridEnabled([MarshalAs(UnmanagedType.I1)] bool enabled);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetDemoLighting([MarshalAs(UnmanagedType.I1)] bool enabled);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetVisualStyle(int style);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetSelectionStyle(int style);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetSelectionStyle();

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetSelectionLineWidth(double width);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetHoverHighlight([MarshalAs(UnmanagedType.I1)] bool enabled);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetHoverHighlight([MarshalAs(UnmanagedType.I1)] out bool outEnabled);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetHoverStyle(CAD_Color color, double width);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetHoveredObject(out uint outId);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetDimensionTextScreenFixed([MarshalAs(UnmanagedType.I1)] bool enabled);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetDimensionTextScreenFixed([MarshalAs(UnmanagedType.I1)] out bool outEnabled);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_AdjustTextureScale(double delta);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_AdjustLineWidth(double deltaPx);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_SetCollisionEnabled([MarshalAs(UnmanagedType.I1)] bool enabled);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_GetCollisionEnabled([MarshalAs(UnmanagedType.I1)] out bool outEnabled);

        [DllImport(Dll, CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
        public static extern int CAD_CaptureViewport([MarshalAs(UnmanagedType.LPUTF8Str)] string pathUtf8, [MarshalAs(UnmanagedType.I1)] bool clean);
    }
}
