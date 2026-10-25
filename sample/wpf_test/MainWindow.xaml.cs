using System;
using System.Windows;
using System.Windows.Media;

namespace LotCadWpf
{
    public partial class MainWindow : Window
    {
        readonly VulkanHost _host = new VulkanHost();

        public MainWindow()
        {
            InitializeComponent();
            Loaded += OnLoaded;
            // 해석 상태 폴링을 엔진 정리(Closed 의 _host.Dispose)보다 **먼저** 멈춘다 — 헐린 엔진에 묻지 않게
            Closing += (s, e) => Analysis.Shutdown();
            Closed += OnClosed;
        }

        void OnLoaded(object sender, RoutedEventArgs e)
        {
            // 런타임 에셋(models/textures/fonts) 경로 지정 — exe 폴더 기준.
            // 셰이더는 라이브러리에 SPIR-V 로 내장돼 폴더가 아예 없다. CWD 는 실행 방식마다
            // 달라지므로(F5 / Ctrl+F5 / 더블클릭) 조건 없이 항상 설정한다. 엔진 생성 전이어야 함.
            string assets = AppDomain.CurrentDomain.BaseDirectory;
            bool assetsOk = CadApi.CAD_SetRuntimeAssetPath(CadApi.Utf8(assets));

            // HwndHost 를 렌더 영역에 얹음 → BuildWindowCore 에서 엔진 생성.
            // 크기 동기화는 host.Tick() 안의 SyncSize() 가 실제 HWND 픽셀로 매 프레임 처리.
            RenderHost.Child = _host;

            StatusText.Text = !_host.EngineReady ? "엔진 생성 실패 — DLL/에셋 확인"
                            : assetsOk           ? "엔진 준비됨"
                                                 : "엔진 준비됨 (에셋 경로 실패 — 치수/문자 미동작)";
            InfoText.Text = _host.EngineReady ? "● 렌더링" : "";

            // 매 프레임 Tick (WPF 합성 타이밍)
            CompositionTarget.Rendering += (s, ev) =>
            {
                _host.Tick();
                SceneInfo.Text = $"객체 {CadApi.CAD_GetObjectCount()} · 선택 {CadApi.SelectedCount()}";
            };
        }

        void OnClosed(object sender, EventArgs e) => _host.Dispose();

        void OnExit(object s, RoutedEventArgs e) => Close();

        // ── 툴바 핸들러 ──
        void OnAddCube(object s, RoutedEventArgs e)   => CadApi.CAD_CreateBox(new CadApi.GeVec3(0, 0, 0), new CadApi.GeVec3(1, 1, 1), IntPtr.Zero, out _);
        void OnLine(object s, RoutedEventArgs e)       => CadApi.CAD_ExecuteCommand("line");
        void OnRect(object s, RoutedEventArgs e)       => CadApi.CAD_ExecuteCommand("rect");
        void OnCircle(object s, RoutedEventArgs e)     => CadApi.CAD_ExecuteCommand("circle");
        void OnPolyline(object s, RoutedEventArgs e)   => CadApi.CAD_ExecuteCommand("polyline");
        void OnSelectAll(object s, RoutedEventArgs e)  => CadApi.CAD_ExecuteCommand("selectall");
        void OnDelete(object s, RoutedEventArgs e)     => CadApi.CAD_ExecuteCommand("delete");
        void OnClearAll(object s, RoutedEventArgs e)   => CadApi.CAD_ClearAll();
        void OnUndo(object s, RoutedEventArgs e)       => CadApi.CAD_Undo();
        void OnRedo(object s, RoutedEventArgs e)       => CadApi.CAD_Redo();
        void OnViewFront(object s, RoutedEventArgs e)  => CadApi.CAD_SetView(0);
        void OnViewTop(object s, RoutedEventArgs e)    => CadApi.CAD_SetView(1);
        void OnViewIso(object s, RoutedEventArgs e)    => CadApi.CAD_SetView(3);
        void OnZoom(object s, RoutedEventArgs e)       => CadApi.CAD_ZoomExtents();
        void OnToggleProj(object s, RoutedEventArgs e) => CadApi.ToggleProjection();

        // ── 해석 — 오른쪽 패널의 그 페이지를 연다 ──
        void OnWindTunnel(object s, RoutedEventArgs e) => Analysis.ShowPage(0);
        void OnWater(object s, RoutedEventArgs e)      => Analysis.ShowPage(1);
        void OnStructural(object s, RoutedEventArgs e) => Analysis.ShowPage(2);
    }
}
