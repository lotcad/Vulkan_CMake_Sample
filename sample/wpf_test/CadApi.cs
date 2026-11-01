using System;
using System.Runtime.InteropServices;

namespace LotCadWpf
{
    // LotCADCore.dll 의 extern "C" CAD_* 함수 P/Invoke 선언.
    // DLL 은 CMake 의 LotCADCoreShared 타겟(OUTPUT_NAME=LotCADCore) 산출물.
    // 빌드 출력 폴더에 LotCADCore.dll + models/ textures/ fonts/ 가 있어야 함.
    internal static class CadApi
    {
        const string DLL = "LotCADCore.dll";

        // ── 생명주기 / 뷰 ──
        // 루프 세 함수(CreateEngine·Tick·ShouldClose)는 bool, 나머지는 결과 코드(0 = CAD_OK, 이유는 CAD_GetLastError)
        // C bool 은 1바이트 — I1 이 없으면 4바이트로 읽어 false 가 true 로 보일 수 있다
        [DllImport(DLL)] [return: MarshalAs(UnmanagedType.I1)] public static extern bool CAD_CreateEngine();
        [DllImport(DLL)] public static extern int CAD_DestroyEngine();
        [DllImport(DLL)] [return: MarshalAs(UnmanagedType.I1)] public static extern bool CAD_Tick();
        [DllImport(DLL)] [return: MarshalAs(UnmanagedType.I1)] public static extern bool CAD_ShouldClose();
        [DllImport(DLL)] public static extern int CAD_SetIgnoreCloseRequest([MarshalAs(UnmanagedType.I1)] bool ignore);
        // CharSet.Ansi 는 한글 경로를 깨뜨린다(엔진은 UTF-8 을 기대). byte[] 로 넘긴다. 0 = CAD_OK
        [DllImport(DLL)] public static extern int CAD_SetRuntimeAssetPath(byte[] pathUtf8);
        [DllImport(DLL)] public static extern int CAD_AttachView(IntPtr nativeHandle, int width, int height);
        [DllImport(DLL)] public static extern int CAD_ResizeView(int width, int height);
        [DllImport(DLL)] public static extern int CAD_DetachView();

        // ── 입력 ──
        [DllImport(DLL)] public static extern void CAD_OnMouseDown(int button, double x, double y, int modifiers);
        [DllImport(DLL)] public static extern void CAD_OnMouseUp(int button, double x, double y, int modifiers);
        [DllImport(DLL)] public static extern void CAD_OnMouseMove(double x, double y);
        [DllImport(DLL)] public static extern void CAD_OnMouseWheel(double x, double y, double deltaX, double deltaY);
        [DllImport(DLL)] public static extern void CAD_OnKeyDownVK(int vkCode);
        [DllImport(DLL)] public static extern void CAD_OnKeyUpVK(int vkCode);

        // ── 툴바 명령 ──
        [StructLayout(LayoutKind.Sequential)] public struct GeVec3 { public double X, Y, Z; public GeVec3(double x, double y, double z) { X = x; Y = y; Z = z; } }
        // 반환 = 결과 코드(0 = 성공), 새 id 는 out — opt 는 IntPtr.Zero(지금 도면층·기본 색)
        [DllImport(DLL)] public static extern int CAD_CreateBox(GeVec3 center, GeVec3 size, IntPtr opt, out uint id);
        // ── 명령 실행 ──
        // 엔진 명령 200여 개를 이름으로 전부 쓸 수 있다 — 도구 시작(line·rect·circle·polyline·cube …)·
        // 전체 선택(selectall)·삭제(delete) 도 이것 하나로 부른다.
        //   CadApi.CAD_ExecuteCommand("trim");
        //   CadApi.CAD_ExecuteCommand("offset");
        // 반환 0 = CAD_OK, 모르는 명령 CAD_E_NOT_FOUND(음수). 글은 UTF-8 로(한글 별칭도 된다).
        [DllImport(DLL)]
        public static extern int CAD_ExecuteCommand([MarshalAs(UnmanagedType.LPUTF8Str)] string text);
        // 진행 중인 명령·도구·묻기를 ESC 처럼 끝낸다(선택은 그대로). 0 = CAD_OK
        [DllImport(DLL)] public static extern int CAD_CancelCommand();
        // 도구 막대 버튼용 — 취소 후 새 명령(오토캐드 ^C^C). ExecuteCommand 만 부르면 선 그리던 중 "rect" 가 값으로 먹힌다.
        public static int StartCommand(string name) { CAD_CancelCommand(); return CAD_ExecuteCommand(name); }

        // ── 알림(콜백) ──
        // ⚠️ 델리게이트를 **필드로 붙들어 둬야** 한다. 지역 변수로 넘기면 GC 가 걷어가
        //    엔진이 이미 사라진 함수를 부른다(그 순간 프로세스가 죽는다).
        //    호출은 CAD_Tick 안 = UI 스레드이므로 콜백에서 화면을 바로 고쳐도 된다.
        //    이벤트는 CAD_AddEventListener 하나로 듣는다(kind 로 갈라 처리) — 예전 한 칸짜리
        //    CAD_SetOnSelectionChanged·ObjectCreated·ObjectDeleted·DocumentDirty 는 지워졌다.
        //    kind: 1 객체 생성(id) · 2 객체 삭제(id) · 4 선택 변경(id 0) · 8 문서 변경(id = dirty ? 1 : 0)
        //          16 명령 시작 · 32 명령 끝 · 64 명령 취소(id 0, 이름은 CAD_EdGetCommandName)
        public const uint CAD_EVENT_OBJECT_CREATED    = 1;
        public const uint CAD_EVENT_OBJECT_DELETED    = 2;
        public const uint CAD_EVENT_SELECTION_CHANGED = 4;
        public const uint CAD_EVENT_DOCUMENT_DIRTY    = 8;
        public const uint CAD_EVENT_COMMAND_STARTED   = 16;
        public const uint CAD_EVENT_COMMAND_ENDED     = 32;
        public const uint CAD_EVENT_COMMAND_CANCELLED = 64;
        public delegate void EventCb(int kind, uint id, IntPtr user);
        public delegate void TextCb(IntPtr utf8);

        // 0 = CAD_OK, 핸들은 outHandle. pluginId 는 호스트면 0
        [DllImport(DLL)] public static extern int CAD_AddEventListener(uint kinds, EventCb fn, IntPtr user, uint pluginId, out uint outHandle);
        [DllImport(DLL)] public static extern int CAD_RemoveEventListener(uint handle);
        [DllImport(DLL)] public static extern int CAD_SetOnPrompt(TextCb cb);

        // ── 측정 ── 상태바에 "길이 3,600" / "면적 12.5" 를 띄울 때. 월드 좌표 기준.
        // 반환 = 결과 코드(0 = 성공, 음수 = 이유 코드 — 글은 LastError())
        [DllImport(DLL)] public static extern int CAD_GetLength(uint id, out double outLength);
        [DllImport(DLL)] public static extern int CAD_GetArea(uint id, out double outArea);
        [DllImport(DLL)] public static extern int CAD_GetSelectionLength(out double outLength);
        [DllImport(DLL)] public static extern int CAD_GetSelectionArea(out double outArea);


        [DllImport(DLL)] public static extern int CAD_ClearAll();   // 0 = CAD_OK(다음 틱에 비운다)
        // 보기 — 반환 0 = CAD_OK(카메라는 다음 틱에 움직인다)
        [DllImport(DLL)] public static extern int CAD_ZoomExtents();
        [DllImport(DLL)] public static extern int CAD_SetView(int viewType);   // 0=Front 1=Top 2=Right 3=Iso
        [DllImport(DLL)] public static extern int CAD_SetProjection([MarshalAs(UnmanagedType.I1)] bool ortho);
        [DllImport(DLL)] public static extern int CAD_GetProjection([MarshalAs(UnmanagedType.I1)] out bool ortho);
        public static void ToggleProjection() { if (CAD_GetProjection(out bool ortho) == 0) CAD_SetProjection(!ortho); }
        public static bool IsOrtho() => CAD_GetProjection(out bool ortho) == 0 && ortho;
        [DllImport(DLL)] public static extern int CAD_FocusSelected();   // 고른 것 보기 — 선택이 없으면 CAD_E_NOT_FOUND

        // ── 솔리드 차집합 (리본 3D > 차집합) ── 기준 baseIds 에서 cutIds 전부를 뺀다. perBase = false: 결과 1개(오토캐드 SUBTRACT).
        // 반환 = 결과 수(음수 = 이유 코드 — 실패면 아무것도 안 바꾼다). outIds 를 꼭 준다: null 이면 해 본 뒤 되돌려 개수만 센다
        [DllImport(DLL)]
        public static extern int CAD_BooleanSubtract(uint[] baseIds, uint baseCount, uint[] cutIds, uint cutCount,
            [MarshalAs(UnmanagedType.I1)] bool keepOriginals, [MarshalAs(UnmanagedType.I1)] bool perBase, uint[] outIds, uint capacity);
        // 되돌리기 — 0 = CAD_OK, 되돌릴 것이 없으면 CAD_E_NOT_READY(음수)
        [DllImport(DLL)] public static extern int CAD_Undo();
        [DllImport(DLL)] public static extern int CAD_Redo();

        // ── 파일 ──
        // 경로는 UTF-8 로 넘긴다. C# 의 기본 문자열 마샬링(Ansi)은 한글 경로에서 깨지므로
        // CharSet 을 쓰지 않고 byte[] 로 직접 넘긴다 (Utf8 헬퍼 참고).
        // 반환 0 = CAD_OK, 음수 = 이유 코드(글은 LastError()). 확장자로 포맷이 정해진다(.lot .step .dwg .dxf .stl .obj .glb) —
        // 예전 CAD_ExportFile 은 CAD_SaveAs(path, selectedOnly) 와 같은 길이라 지워졌다.
        [DllImport(DLL)] public static extern int CAD_SaveAs(byte[] pathUtf8, [MarshalAs(UnmanagedType.I1)] bool selectedOnly);
        [DllImport(DLL)] public static extern int CAD_OpenFile(byte[] pathUtf8);

        // ── 편집 명령 — 분해·배열·대칭은 대상 id 를 받는 CAD_EntityExplode·CAD_EntityArrayRect/Polar·CAD_EntityMirror(sdk/csharp 바인딩) ──

        // ── 조회 ──
        [DllImport(DLL)] public static extern int CAD_GetObjectCount();        // 음수 = 이유 코드
        // 지금 선택 — 칸만큼 채우고 전체 개수(outIds = null 이면 개수만)
        [DllImport(DLL)] public static extern int CAD_GetSelection(uint[] outIds, uint capacity);
        public static int SelectedCount() => Math.Max(0, CAD_GetSelection(null, 0));
        public static uint[] SelectedIds()
        {
            int n = CAD_GetSelection(null, 0);
            if (n <= 0) return Array.Empty<uint>();
            var ids = new uint[n];
            int got = CAD_GetSelection(ids, (uint)n);
            if (got < 0) return Array.Empty<uint>();
            if (got < n) Array.Resize(ref ids, got);
            return ids;
        }
        [DllImport(DLL)] public static extern int CAD_GetLastError(byte[] outUtf8, uint capacity);   // 직전 실패 이유
        // 선택 바꾸기 — mode 0 = 바꿔 고르기
        [DllImport(DLL)] public static extern int CAD_SetSelection(uint[] ids, uint count, int mode);
        // 장면이 바뀔 때마다 커지는 번호 — 같으면 목록을 다시 읽지 않아도 된다(폴링용)
        [DllImport(DLL)] public static extern int CAD_GetSceneRevision(out ulong outRevision);

        // ── 명령 상태 — 동적 입력 토글이 쓴다 ──
        [StructLayout(LayoutKind.Sequential)]
        public struct EdCommandState { public uint Size; [MarshalAs(UnmanagedType.I1)] public bool CommandActive; public int InputKind; }
        [DllImport(DLL)] public static extern int CAD_EdGetCommandState(ref EdCommandState state);   // Size 를 채워 넘긴다
        [DllImport(DLL)] public static extern int CAD_EdGetCommandName(byte[] buf, uint capacity);   // 진행 중(또는 마지막) 명령 이름

        // ── 도면층·선종류 (LayerPanel.cs) ── 도면층 표 바꾸기는 되돌리기에 안 남는다. 도면층 0 은 고정(바꾸면 CAD_E_NOT_SUPPORTED)
        [StructLayout(LayoutKind.Sequential)] public struct CadColor { public double R, G, B; public CadColor(double r, double g, double b) { R = r; G = g; B = b; } }
        [DllImport(DLL)] public static extern int CAD_GetLayersJson(byte[] buf, uint capacity);   // {"layers":[{id,name,visible,locked,color,linetypeId,linetype,objectCount,selectedCount,fixed?}]}
        [DllImport(DLL)] public static extern int CAD_CreateLayer(byte[] nameUtf8, out uint outLayerId);
        [DllImport(DLL)] public static extern int CAD_RenameLayer(uint id, byte[] nameUtf8);
        [DllImport(DLL)] public static extern int CAD_SetLayerColor(uint id, CadColor color);   // 0~1
        [DllImport(DLL)] public static extern int CAD_SetLayerVisible(uint id, [MarshalAs(UnmanagedType.I1)] bool visible);
        [DllImport(DLL)] public static extern int CAD_SetLayerLocked(uint id, [MarshalAs(UnmanagedType.I1)] bool locked);
        [DllImport(DLL)] public static extern int CAD_SetLayerLinetype(uint layerId, uint linetypeId);
        [DllImport(DLL)] public static extern int CAD_AssignSelectedToLayer(uint layerId, out uint outChanged);   // 잠긴 층 것은 건너뜀
        [DllImport(DLL)] public static extern int CAD_SetSelectedColorByLayer([MarshalAs(UnmanagedType.I1)] bool byLayer, out uint outChanged);
        public const uint CAD_LINETYPE_BYLAYER = 0xFFFFFFFF;   // 객체 선종류 = 도면층 따름
        [DllImport(DLL)] public static extern int CAD_GetLinetypeIds(uint[] outIds, uint capacity);   // 0(Continuous) 포함 전체 개수
        [DllImport(DLL)] public static extern int CAD_GetLinetypeName(uint id, byte[] buf, uint capacity);
        [DllImport(DLL)] public static extern int CAD_GetLinetypePattern(uint id, double[] outPattern, uint capacity);   // 요소 수(실선 0)
        // 무늬: 양수 = 선, 음수 = 빈칸, 0 = 점(.lin 규칙), 요소 1~8개
        [DllImport(DLL)] public static extern int CAD_CreateLinetype(byte[] nameUtf8, double[] pattern, uint count, byte[] description, out uint outId);
        [DllImport(DLL)] public static extern int CAD_SetObjectLinetype(uint[] ids, uint count, uint linetypeId, out uint outChanged);
        [DllImport(DLL)] public static extern int CAD_SetObjectLinetypeScale(uint objectId, double scale);
        [DllImport(DLL)] public static extern int CAD_SetLinetypeScale(double scale);   // 전역 LTSCALE

        // ── 블록·외부 참조 (LayerPanel.cs) ── 만들기·편집은 명령(block · bedit 이름 · bclose save|discard · bbase)
        [DllImport(DLL)] public static extern int CAD_GetBlocksJson(byte[] buf, uint capacity);   // {"blocks":[{name,objects,references,base,xref?,xrefFound?}]}
        [DllImport(DLL)] public static extern int CAD_XrefReload(byte[] nameUtf8);
        [DllImport(DLL)] public static extern int CAD_XrefBind(byte[] nameUtf8);
        [DllImport(DLL)] public static extern int CAD_XrefDetach(byte[] nameUtf8);
        [DllImport(DLL)] public static extern int CAD_XrefSetPath(byte[] nameUtf8, byte[] pathOrKindUtf8);   // "relative" | "absolute" | "none" | 새 경로

        // ── 분해도 (ToolsPanel.cs) ── {"op": status|solve|auto|clear|amount|play|back|balloons|bom, …} → 결과 JSON. 2회 호출 규약(CallOnce)
        [DllImport(DLL)] public static extern int CAD_ExplodeView(byte[] argsJson, byte[] outUtf8, uint capacity);

        // ── 메시 수리 (ToolsPanel.cs) ── 반환 = 바꾼 메시 수(0 = 고칠 것 없음), 음수 = 이유 코드. B-Rep 솔리드는 대상 아님
        [StructLayout(LayoutKind.Sequential)]
        public struct MeshCheckInfo
        {
            public uint Size, Triangles, Vertices, Degenerate, Duplicates, OpenEdges, NonManifoldEdges, FlippedEdges, Holes, Components;
            [MarshalAs(UnmanagedType.I1)] public bool Closed;
            [MarshalAs(UnmanagedType.I1)] public bool Ok;
            public double Volume, Area;
        }
        [StructLayout(LayoutKind.Sequential)]
        public struct MeshRepairOptions { public uint Size; [MarshalAs(UnmanagedType.I1)] public bool NoFill; [MarshalAs(UnmanagedType.I1)] public bool FlatFill; }
        [DllImport(DLL)] public static extern int CAD_CheckMesh(uint id, ref MeshCheckInfo info);   // Size 를 채워 넘긴다
        [DllImport(DLL)] public static extern int CAD_RepairMeshes(uint[] ids, uint count, ref MeshRepairOptions opt);
        [DllImport(DLL)] public static extern int CAD_SmoothMeshes(uint[] ids, uint count, int iterations);
        [DllImport(DLL)] public static extern int CAD_DecimateMeshes(uint[] ids, uint count, double ratio);
        [DllImport(DLL)] public static extern int CAD_StitchMeshes(uint[] ids, uint count, double tolerance);
        [DllImport(DLL)] public static extern int CAD_ThickenMeshes(uint[] ids, uint count, double thickness);
        [DllImport(DLL)] public static extern int CAD_RemeshMeshes(uint[] ids, uint count, double edgeLength);

        // ── 이미지 ── widthWorld 0 = 긴 변 10 단위, origin = 왼쪽 아래, opt = IntPtr.Zero
        [DllImport(DLL)] public static extern int CAD_AttachImageFromFile(byte[] pathUtf8, double widthWorld, GeVec3 origin, IntPtr opt, out uint outId);

        /// <summary>(buf, capacity) 로 글을 주는 함수 — 길이를 먼저 묻고 그만큼 받는다. 실패면 "".</summary>
        public static string ReadText(Func<byte[], uint, int> fn)
        {
            int n = fn(null, 0);
            if (n < 0) return "";
            var buf = new byte[n + 1];
            fn(buf, (uint)buf.Length);
            return FromUtf8(buf);
        }

        // ── 해석 — 바람 터널 · 물 · 구조 해석 ── (Analysis.cs 가 쓴다)
        // argsJson = {"op": …} 를 UTF-8 로, 결과 JSON 이 outUtf8 에(capacity 바이트). 반환 = 전체 길이, 실패 = 음수 CAD_E_*(이유는 CAD_GetLastError).
        // ⚠️ 2회 호출 규약: outUtf8=null 로 길이를 물을 때 **한 번 실행**하고, 같은 인자로 버퍼를 주면 그 결과만 준다.
        //    고정 버퍼로 먼저 불렀다 모자라 다시 부르면 start·run 이 두 번 들어간다 → 아래 CallOnce 로만 읽는다.
        // 해석 모듈 LotCADSim.dll · LotCADCfd.dll 이 LotCADCore.dll 옆에 있어야 한다(csproj 가 같이 복사).
        [DllImport(DLL)] public static extern int CAD_WindTunnel(byte[] argsJson, byte[] outUtf8, uint capacity);
        [DllImport(DLL)] public static extern int CAD_Water(byte[] argsJson, byte[] outUtf8, uint capacity);
        [DllImport(DLL)] public static extern int CAD_StructuralAnalysis(byte[] argsJson, byte[] outUtf8, uint capacity);

        public delegate int JsonFn(byte[] argsJson, byte[] outUtf8, uint capacity);

        /// <summary>2회 호출 규약대로 한 번만 실행하고 결과 글을 받는다. 실패면 null.</summary>
        public static string CallOnce(JsonFn fn, string argsJson)
        {
            byte[] args = Utf8(argsJson);
            int need = fn(args, null, 0);          // 길이를 물으며 실행
            if (need < 0) return null;
            var buf = new byte[need + 1];
            if (fn(args, buf, (uint)buf.Length) < 0) return null;   // 같은 인자 → 다시 실행하지 않고 결과만
            return FromUtf8(buf);
        }

        public static string LastError()
        {
            var buf = new byte[1024];
            CAD_GetLastError(buf, (uint)buf.Length);
            return FromUtf8(buf);
        }

        public static string FromUtf8(byte[] buf)
        {
            int len = Array.IndexOf(buf, (byte)0);
            return System.Text.Encoding.UTF8.GetString(buf, 0, len < 0 ? buf.Length : len);
        }

        // 한글 경로를 위한 UTF-8 변환 — 위 파일 API 에 넘길 때 반드시 이걸 거친다.
        public static byte[] Utf8(string s) =>
            System.Text.Encoding.UTF8.GetBytes((s ?? string.Empty) + "\0");
    }
}
