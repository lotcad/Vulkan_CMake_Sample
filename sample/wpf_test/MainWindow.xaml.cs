using System;
using System.Runtime.InteropServices;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Threading;
using Microsoft.Win32;

namespace LotCadWpf
{
    // 메뉴 · 리본(MainWindow.Ribbon.cs) · 왼쪽 정보 · 렌더 영역 · 오른쪽 패널 · 상태바.
    public partial class MainWindow : Window
    {
        readonly VulkanHost _host = new VulkanHost();
        // 엔진에 읽는 함수가 없는 상태 — 호스트가 들고 있는다(처음 값 = 엔진 기본값)
        bool _dynInput = true, _graphOn;
        // 이벤트 — 델리게이트를 필드로 붙들어 둔다(GC 가 걷어가면 엔진이 사라진 함수를 부른다)
        CadApi.EventCb _onEvent;
        uint _eventHandle;
        string _eventCommand = "";
        int _eventCreated, _eventDeleted;

        public MainWindow()
        {
            InitializeComponent();
            BuildRibbon();
            Loaded += OnLoaded;
            // 패널 폴링·이벤트를 엔진 정리(Closed 의 _host.Dispose)보다 **먼저** 멈춘다 — 헐린 엔진에 묻지 않게
            Closing += (s, e) =>
            {
                Analysis.Shutdown();
                Layers.Shutdown();
                Tools.Shutdown();
                if (_eventHandle != 0) CadApi.CAD_RemoveEventListener(_eventHandle);
                _eventHandle = 0;
            };
            Closed += OnClosed;
            // F12 = 동적 입력 — 렌더 영역에 포커스가 있으면 VulkanHost 가, WPF 컨트롤에 있으면 여기서 받는다
            _host.F12Pressed += ToggleDynInput;
            PreviewKeyDown += (s, e) => { if (e.Key == Key.F12) { ToggleDynInput(); e.Handled = true; } };
        }

        void OnLoaded(object sender, RoutedEventArgs e)
        {
            // 런타임 에셋(models/textures/fonts) 경로 지정 — exe 폴더 기준.
            // 셰이더는 라이브러리에 SPIR-V 로 내장돼 폴더가 아예 없다. CWD 는 실행 방식마다
            // 달라지므로(F5 / Ctrl+F5 / 더블클릭) 조건 없이 항상 설정한다. 엔진 생성 전이어야 함.
            string assets = AppDomain.CurrentDomain.BaseDirectory;
            bool assetsOk = CadApi.CAD_SetRuntimeAssetPath(CadApi.Utf8(assets)) == 0;   // 0 = CAD_OK

            // HwndHost 를 렌더 영역에 얹음 → BuildWindowCore 에서 엔진 생성.
            // 크기 동기화는 host.Tick() 안의 SyncSize() 가 실제 HWND 픽셀로 매 프레임 처리.
            RenderHost.Child = _host;

            StatusText.Text = !_host.EngineReady ? "엔진 생성 실패 — DLL/에셋 확인"
                            : assetsOk           ? "엔진 준비됨"
                                                 : "엔진 준비됨 (에셋 경로 실패 — 치수/문자 미동작)";
            InfoText.Text = _host.EngineReady ? "● 렌더링" : "";
            if (_host.EngineReady) StartEvents();

            // 매 프레임 Tick (WPF 합성 타이밍)
            CompositionTarget.Rendering += (s, ev) =>
            {
                _host.Tick();
                SceneInfo.Text = $"객체 {CadApi.CAD_GetObjectCount()} · 선택 {CadApi.SelectedCount()}";
            };
        }

        void OnClosed(object sender, EventArgs e) => _host.Dispose();

        void OnExit(object s, RoutedEventArgs e) => Close();

        // ── 이벤트 ── 콜백은 CAD_Tick 안(= UI 스레드)에서 프레임 끝에 불린다.
        // 바로 끝나는 명령(cube 등)은 한 틱에 시작 → 끝 → 만들기 순으로 온다(만들기가 끝보다 늦다) —
        // 그래서 '끝' 에선 Dispatcher.BeginInvoke 로 미뤄, 그 틱의 이벤트가 다 온 뒤 상태바에 만든·지운 수를 적는다.
        void StartEvents()
        {
            _onEvent = OnEngineEvent;
            uint kinds = CadApi.CAD_EVENT_OBJECT_CREATED | CadApi.CAD_EVENT_OBJECT_DELETED |
                         CadApi.CAD_EVENT_COMMAND_STARTED | CadApi.CAD_EVENT_COMMAND_ENDED | CadApi.CAD_EVENT_COMMAND_CANCELLED;
            if (CadApi.CAD_AddEventListener(kinds, _onEvent, IntPtr.Zero, 0, out _eventHandle) != 0) _eventHandle = 0;   // 0 = 호스트
        }

        void OnEngineEvent(int kind, uint id, IntPtr user)
        {
            switch ((uint)kind)
            {
                case CadApi.CAD_EVENT_OBJECT_CREATED: _eventCreated++; break;
                case CadApi.CAD_EVENT_OBJECT_DELETED: _eventDeleted++; break;
                case CadApi.CAD_EVENT_COMMAND_STARTED:
                    _eventCommand = CadApi.ReadText(CadApi.CAD_EdGetCommandName);   // 명령행에 친 첫 낱말(소문자)
                    _eventCreated = _eventDeleted = 0;   // 명령 밖(C API 로 만든 것 등)에서 센 것은 버린다
                    break;
                case CadApi.CAD_EVENT_COMMAND_ENDED:
                case CadApi.CAD_EVENT_COMMAND_CANCELLED:
                    bool cancelled = kind == (int)CadApi.CAD_EVENT_COMMAND_CANCELLED;
                    Dispatcher.BeginInvoke(new Action(() =>
                    {
                        if (cancelled) StatusText.Text = $"[이벤트] {_eventCommand} 취소";
                        else if (_eventCreated + _eventDeleted > 0)
                            StatusText.Text = $"[이벤트] {_eventCommand} 끝 — 만든 객체 {_eventCreated} · 지운 객체 {_eventDeleted}";
                        _eventCreated = _eventDeleted = 0;
                    }));
                    break;
            }
        }

        // 동적 입력은 읽는 함수가 없어 호스트가 상태를 들고 있는다. 명령이 없을 땐 dyn on|off 로 정확히 맞추고,
        // 그리는 중엔 명령행에 글을 넣으면 값으로 먹히므로 엔진에 F12 키를 보낸다(엔진의 F12 = 동적 입력 뒤집기.
        // 단 자르기·연장 중의 F12 는 EDGE 모드라 그때는 체크가 어긋날 수 있다).
        void ToggleDynInput()
        {
            _dynInput = !_dynInput;
            var state = new CadApi.EdCommandState { Size = (uint)Marshal.SizeOf<CadApi.EdCommandState>() };
            if (CadApi.CAD_EdGetCommandState(ref state) == 0 && state.CommandActive)
            {
                CadApi.CAD_OnKeyDownVK(0x7B);   // VK_F12
                CadApi.CAD_OnKeyUpVK(0x7B);
            }
            else CadApi.CAD_ExecuteCommand(_dynInput ? "dyn on" : "dyn off");
            DynItem.IsChecked = _dynInput;
        }

        // 노드 그래프 칸 — 엔진이 Vulkan 으로 3D 뷰 오른쪽 칸에 그린다(호스트 창 안에서도 보인다). 읽는 함수가 없어 호스트가 상태를.
        void ToggleGraph()
        {
            _graphOn = !_graphOn;
            CadApi.StartCommand(_graphOn ? "graph on" : "graph off");
            GraphItem.IsChecked = _graphOn;
        }

        // 키보드를 렌더 창(엔진)으로 — 메뉴·리본으로 시작한 명령이 묻는 값(블록 이름 등)을 바로 치게.
        // 메뉴가 닫히며 포커스를 되돌린 **뒤에** 옮겨야 해서 Dispatcher 로 미룬다.
        void FocusViewLater() => Dispatcher.BeginInvoke(new Action(_host.FocusView), DispatcherPriority.Input);

        // 메뉴로 시작하는 엔진 명령
        void Command(string text)
        {
            CadApi.StartCommand(text);
            FocusViewLater();
        }

        // 오른쪽 패널은 하나씩 — 다른 것을 닫고 연다
        void ShowSide(UserControl panel, Action show)
        {
            foreach (var p in new UserControl[] { Analysis, Layers, Tools }) if (p != panel) p.Visibility = Visibility.Collapsed;
            show();
        }

        // ── 파일 — 고르기는 호스트(대화상자), 엔진에는 경로만. 포맷은 확장자로 엔진이 정한다 ──
        void OpenFile(string filter)
        {
            var dlg = new OpenFileDialog { Filter = filter };
            if (dlg.ShowDialog(this) != true) return;
            if (CadApi.CAD_OpenFile(CadApi.Utf8(dlg.FileName)) == 0) CadApi.CAD_ZoomExtents();   // 연 것이 화면 밖일 수 있다
            else MessageBox.Show(this, CadApi.LastError() is { Length: > 0 } m ? m : "열기 실패", "LotCAD");
        }

        // 확장자가 없으면 고른 형식의 확장자가 붙는다 — 모르는 확장자는 엔진이 OBJ 로 저장하니 꼭 붙인다
        void SaveFile(string filter, string what)
        {
            var dlg = new SaveFileDialog { Filter = filter, AddExtension = true };
            if (dlg.ShowDialog(this) != true) return;
            if (CadApi.CAD_SaveAs(CadApi.Utf8(dlg.FileName), false) != 0)
                MessageBox.Show(this, CadApi.LastError() is { Length: > 0 } m ? m : what + " 실패", "LotCAD");
        }

        // 이미지 붙이기 — 원점에 긴 변 10 단위로 놓고 골라 둔다(이어서 회전·뒤집기·배경 지우기가 그 이미지에 먹는다)
        void AttachImage()
        {
            var dlg = new OpenFileDialog { Filter = "이미지 (*.png;*.jpg;*.jpeg;*.bmp)|*.png;*.jpg;*.jpeg;*.bmp|모든 파일 (*.*)|*.*" };
            if (dlg.ShowDialog(this) != true) return;
            if (CadApi.CAD_AttachImageFromFile(CadApi.Utf8(dlg.FileName), 0, new CadApi.GeVec3(0, 0, 0), IntPtr.Zero, out uint id) != 0)
            {
                MessageBox.Show(this, CadApi.LastError(), "LotCAD");
                return;
            }
            CadApi.CAD_SetSelection(new[] { id }, 1, 0);
            CadApi.CAD_ZoomExtents();
        }

        // ── 메뉴 ──
        void OnOpen(object s, RoutedEventArgs e) => OpenFile(
            "CAD 파일|*.lot;*.step;*.stp;*.dwg;*.dxf;*.obj;*.stl;*.fbx;*.ply;*.gltf;*.glb|STEP (*.step;*.stp)|*.step;*.stp|" +
            "도면 (*.dwg;*.dxf)|*.dwg;*.dxf|모든 파일 (*.*)|*.*");
        void OnSaveAs(object s, RoutedEventArgs e) => SaveFile("프로젝트 (*.lot)|*.lot", "저장");
        void OnExport(object s, RoutedEventArgs e) => SaveFile(
            "STEP AP242 (*.step)|*.step|DWG R2018 (*.dwg)|*.dwg|DXF (*.dxf)|*.dxf|STL (*.stl)|*.stl|OBJ (*.obj)|*.obj|glTF (*.glb)|*.glb", "내보내기");
        void OnClearAll(object s, RoutedEventArgs e)   => CadApi.CAD_ClearAll();

        void OnUndo(object s, RoutedEventArgs e)       => CadApi.CAD_Undo();
        void OnRedo(object s, RoutedEventArgs e)       => CadApi.CAD_Redo();
        void OnSelectAll(object s, RoutedEventArgs e)  => CadApi.StartCommand("selectall");
        void OnDelete(object s, RoutedEventArgs e)     => CadApi.StartCommand("delete");

        void OnViewFront(object s, RoutedEventArgs e)  => CadApi.CAD_SetView(0);
        void OnViewTop(object s, RoutedEventArgs e)    => CadApi.CAD_SetView(1);
        void OnViewIso(object s, RoutedEventArgs e)    => CadApi.CAD_SetView(3);
        void OnZoom(object s, RoutedEventArgs e)       => CadApi.CAD_ZoomExtents();
        void OnToggleProj(object s, RoutedEventArgs e) => CadApi.ToggleProjection();

        // 도면 — 오른쪽 도면 패널, 블록 만들기·편집은 엔진 명령(이름·기준점을 3D 뷰가 묻는다)
        void OnLayers(object s, RoutedEventArgs e)      => ShowSide(Layers, () => Layers.ShowPage(0));
        void OnLinetypes(object s, RoutedEventArgs e)   => ShowSide(Layers, () => Layers.ShowPage(1));
        void OnBlocks(object s, RoutedEventArgs e)      => ShowSide(Layers, () => Layers.ShowPage(2));
        void OnBlockCreate(object s, RoutedEventArgs e) => Command("block");
        void OnBlockEdit(object s, RoutedEventArgs e)   => Command("bedit");

        // 도구
        void OnGraph(object s, RoutedEventArgs e)    => ToggleGraph();
        void OnExplode(object s, RoutedEventArgs e)  => ShowSide(Tools, () => Tools.ShowPage(0));
        void OnMesh(object s, RoutedEventArgs e)     => ShowSide(Tools, () => Tools.ShowPage(1));
        void OnDynInput(object s, RoutedEventArgs e) => ToggleDynInput();
        void OnImageAttach(object s, RoutedEventArgs e)     => AttachImage();
        void OnImageRotate(object s, RoutedEventArgs e)     => CadApi.StartCommand("imagerotate 90");
        void OnImageFlip(object s, RoutedEventArgs e)       => CadApi.StartCommand("imageflip h");
        void OnImageBackground(object s, RoutedEventArgs e) => Command("imagebg");
        void OnImageCrop(object s, RoutedEventArgs e)       => Command("imagecrop");

        // 해석 — 오른쪽 패널의 그 페이지를 연다
        void OnWindTunnel(object s, RoutedEventArgs e) => ShowSide(Analysis, () => Analysis.ShowPage(0));
        void OnWater(object s, RoutedEventArgs e)      => ShowSide(Analysis, () => Analysis.ShowPage(1));
        void OnStructural(object s, RoutedEventArgs e) => ShowSide(Analysis, () => Analysis.ShowPage(2));
    }
}
