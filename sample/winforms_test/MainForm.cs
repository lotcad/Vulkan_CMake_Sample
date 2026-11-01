using System;
using System.Drawing;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace LotCadWinForms
{
    // WPF 샘플(MainWindow.xaml)과 같은 화면 — 메뉴 · 툴바(그리기/편집/뷰) · 왼쪽 정보 · 렌더 영역 · 상태바.
    // 디자이너 파일 없이 코드로만 만든다(한 파일에서 전체가 보이게).
    public sealed class MainForm : Form
    {
        static readonly Color Bg        = ColorTranslator.FromHtml("#1E1F22");
        static readonly Color BarBg     = ColorTranslator.FromHtml("#232529");
        static readonly Color BtnBg     = ColorTranslator.FromHtml("#2B2D31");
        static readonly Color BtnHover  = ColorTranslator.FromHtml("#3A3E44");
        static readonly Color Accent    = ColorTranslator.FromHtml("#2D6CDF");
        static readonly Color TextMain  = ColorTranslator.FromHtml("#E6E6E6");
        static readonly Color TextDim   = ColorTranslator.FromHtml("#7C818B");
        static readonly Color TextBody  = ColorTranslator.FromHtml("#B8BCC4");
        static readonly Color TextInfo  = ColorTranslator.FromHtml("#8CB4FF");
        static readonly Color Line      = ColorTranslator.FromHtml("#2E3136");

        readonly VulkanPanel _render = new VulkanPanel { Dock = DockStyle.Fill, BackColor = Color.Black };
        readonly AnalysisPanel _analysis = new AnalysisPanel { Dock = DockStyle.Right, Visible = false };   // 해석 — 툴바·메뉴가 연다
        readonly LayerPanel _layers = new LayerPanel();   // 도면층·선종류·블록 — 메뉴 "도면"
        readonly ToolsPanel _tools = new ToolsPanel();    // 분해도·메시 수리 — 메뉴 "도구"
        // 엔진에 읽는 함수가 없는 상태 — 호스트가 들고 있는다(처음 값 = 엔진 기본값)
        bool _dynInput = true, _graphOn;
        ToolStripMenuItem _dynItem, _graphItem;
        // 이벤트 — 델리게이트를 필드로 붙들어 둔다(GC 가 걷어가면 엔진이 사라진 함수를 부른다)
        CadApi.EventCb _onEvent;
        uint _eventHandle;
        string _eventCommand = "";
        int _eventCreated, _eventDeleted;
        readonly Label _status = new Label { Text = "준비", AutoSize = true, ForeColor = TextBody, Dock = DockStyle.Left };
        readonly Label _info = new Label { Text = "", AutoSize = true, ForeColor = TextInfo, Dock = DockStyle.Right };
        readonly Label _sceneInfo = new Label { Text = "객체 0 · 선택 0", AutoSize = true, ForeColor = TextInfo };
        string _lastSceneInfo = "";

        public MainForm()
        {
            Text = "LotCAD — WinForms 호스트";
            ClientSize = new Size(1120, 740);
            BackColor = Bg;
            Font = new Font("맑은 고딕", 9.5f);
            StartPosition = FormStartPosition.CenterScreen;

            // 런타임 에셋(models/textures/fonts) 경로 지정 — exe 폴더 기준.
            // 셰이더는 라이브러리에 SPIR-V 로 내장돼 폴더가 아예 없다. CWD 는 실행 방식마다
            // 달라지므로(F5 / Ctrl+F5 / 더블클릭) 조건 없이 항상 설정한다. 엔진 생성(= 렌더 영역 핸들 생성) 전이어야 함.
            bool assetsOk = CadApi.CAD_SetRuntimeAssetPath(CadApi.Utf8(AppDomain.CurrentDomain.BaseDirectory)) == 0;   // 0 = CAD_OK

            // 도킹은 나중에 넣은 것부터 자리를 잡는다 → 채움(렌더)을 먼저, 메뉴를 마지막에.
            Controls.Add(_render);
            Controls.Add(_analysis);
            Controls.Add(_layers);
            Controls.Add(_tools);
            Controls.Add(BuildSidePanel());
            Controls.Add(BuildStatusBar());
            Controls.Add(BuildToolbar());
            var menu = BuildMenu();
            Controls.Add(menu);
            MainMenuStrip = menu;

            Shown += (s, e) =>
            {
                _status.Text = !_render.EngineReady ? "엔진 생성 실패 — DLL/에셋 확인"
                             : assetsOk             ? "엔진 준비됨"
                                                    : "엔진 준비됨 (에셋 경로 실패 — 치수/문자 미동작)";
                _info.Text = _render.EngineReady ? "● 렌더링" : "";
                if (_render.EngineReady) StartEvents();
                _render.Focus();
            };

            // 매 프레임 Tick — 메시지가 없을 때마다 돈다(유휴 루프). 스왑체인이 V-Sync 라 CAD_Tick 이
            // 화면 주기에 맞춰 기다려 주므로 CPU 를 헛돌리지 않는다.
            Application.Idle += OnIdle;
            FormClosed += (s, e) => Application.Idle -= OnIdle;
            // 해석 상태 폴링을 엔진 정리(렌더 영역 핸들 파괴)보다 **먼저** 멈춘다 — 헐린 엔진에 묻지 않게
            FormClosing += (s, e) =>
            {
                _analysis.Shutdown();
                _layers.Shutdown();
                _tools.Shutdown();
                if (_eventHandle != 0) CadApi.CAD_RemoveEventListener(_eventHandle);
                _eventHandle = 0;
            };
        }

        // 오른쪽 패널은 하나씩 — 다른 것을 닫고 연다
        void ShowSide(Control panel, Action show)
        {
            foreach (var p in new Control[] { _analysis, _layers, _tools }) if (p != panel) p.Visible = false;
            show();
        }

        // ── 이벤트 ── 콜백은 CAD_Tick 안(= UI 스레드)에서 프레임 끝에 불린다.
        // 바로 끝나는 명령(cube 등)은 한 틱에 시작 → 끝 → 만들기 순으로 온다(만들기가 끝보다 늦다) —
        // 그래서 '끝' 에선 BeginInvoke 로 미뤄, 그 틱의 이벤트가 다 온 뒤 상태바에 만든·지운 수를 적는다.
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
                    BeginInvoke(new Action(() =>
                    {
                        if (cancelled) _status.Text = $"[이벤트] {_eventCommand} 취소";
                        else if (_eventCreated + _eventDeleted > 0)
                            _status.Text = $"[이벤트] {_eventCommand} 끝 — 만든 객체 {_eventCreated} · 지운 객체 {_eventDeleted}";
                        _eventCreated = _eventDeleted = 0;
                    }));
                    break;
            }
        }

        // F12 = 동적 입력 — 렌더 영역이 키를 엔진에 넘기기 전에 여기서 받아 메뉴 체크와 맞춘다
        protected override bool ProcessCmdKey(ref Message msg, Keys keyData)
        {
            if (keyData == Keys.F12) { ToggleDynInput(); return true; }
            return base.ProcessCmdKey(ref msg, keyData);
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
            _dynItem.Checked = _dynInput;
        }

        // 노드 그래프 칸 — 엔진이 Vulkan 으로 3D 뷰 오른쪽 칸에 그린다(호스트 창 안에서도 보인다). 읽는 함수가 없어 호스트가 상태를.
        void ToggleGraph()
        {
            _graphOn = !_graphOn;
            CadApi.StartCommand(_graphOn ? "graph on" : "graph off");
            _graphItem.Checked = _graphOn;
            _render.Focus();
        }

        // ── 파일 — 고르기는 호스트(대화상자), 엔진에는 경로만. 포맷은 확장자로 엔진이 정한다 ──
        void OpenFile(string filter)
        {
            using var dlg = new OpenFileDialog { Filter = filter };
            if (dlg.ShowDialog(this) != DialogResult.OK) return;
            if (CadApi.CAD_OpenFile(CadApi.Utf8(dlg.FileName)) == 0) CadApi.CAD_ZoomExtents();   // 연 것이 화면 밖일 수 있다
            else MessageBox.Show(this, CadApi.LastError() is { Length: > 0 } e ? e : "열기 실패", "LotCAD");
        }

        // 확장자가 없으면 DefaultExt(필터의 첫 확장자)가 붙는다 — 모르는 확장자는 엔진이 OBJ 로 저장하니 꼭 붙인다
        void SaveFile(string filter, string what)
        {
            using var dlg = new SaveFileDialog { Filter = filter, AddExtension = true };
            if (dlg.ShowDialog(this) != DialogResult.OK) return;
            if (CadApi.CAD_SaveAs(CadApi.Utf8(dlg.FileName), false) != 0)
                MessageBox.Show(this, CadApi.LastError() is { Length: > 0 } e ? e : what + " 실패", "LotCAD");
        }

        // 이미지 붙이기 — 원점에 긴 변 10 단위로 놓고 골라 둔다(이어서 회전·뒤집기·배경 지우기가 그 이미지에 먹는다)
        void AttachImage()
        {
            using var dlg = new OpenFileDialog { Filter = "이미지 (*.png;*.jpg;*.jpeg;*.bmp)|*.png;*.jpg;*.jpeg;*.bmp|모든 파일 (*.*)|*.*" };
            if (dlg.ShowDialog(this) != DialogResult.OK) return;
            if (CadApi.CAD_AttachImageFromFile(CadApi.Utf8(dlg.FileName), 0, new CadApi.GeVec3(0, 0, 0), IntPtr.Zero, out uint id) != 0)
            {
                MessageBox.Show(this, CadApi.LastError(), "LotCAD");
                return;
            }
            CadApi.CAD_SetSelection(new[] { id }, 1, 0);
            CadApi.CAD_ZoomExtents();
        }

        void OnIdle(object sender, EventArgs e)
        {
            while (!IsDisposed && !PeekMessage(out _, IntPtr.Zero, 0, 0, 0))
            {
                _render.Tick();
                string info = $"객체 {CadApi.CAD_GetObjectCount()} · 선택 {CadApi.SelectedCount()}";
                if (info != _lastSceneInfo) { _sceneInfo.Text = info; _lastSceneInfo = info; }
                if (!_render.EngineReady) break;   // 엔진이 없으면 돌 것이 없다
            }
        }

        // ── 메뉴 ──
        MenuStrip BuildMenu()
        {
            var menu = new MenuStrip { BackColor = Bg, ForeColor = TextMain, Padding = new Padding(4, 2, 0, 2) };
            menu.Items.Add(Menu("파일(&F)",
                Item("열기...", (s, e) => OpenFile(
                    "CAD 파일|*.lot;*.step;*.stp;*.dwg;*.dxf;*.obj;*.stl;*.fbx;*.ply;*.gltf;*.glb|STEP (*.step;*.stp)|*.step;*.stp|" +
                    "도면 (*.dwg;*.dxf)|*.dwg;*.dxf|모든 파일 (*.*)|*.*")),
                Item("다른 이름으로 저장...", (s, e) => SaveFile("프로젝트 (*.lot)|*.lot", "저장")),
                Item("내보내기...", (s, e) => SaveFile(
                    "STEP AP242 (*.step)|*.step|DWG R2018 (*.dwg)|*.dwg|DXF (*.dxf)|*.dxf|STL (*.stl)|*.stl|OBJ (*.obj)|*.obj|glTF (*.glb)|*.glb", "내보내기")),
                null,
                Item("모두 지움", (s, e) => CadApi.CAD_ClearAll()),
                null,
                Item("종료", (s, e) => Close())));
            menu.Items.Add(Menu("편집(&E)",
                Item("실행 취소 (Undo)", (s, e) => CadApi.CAD_Undo()),
                Item("다시 실행 (Redo)", (s, e) => CadApi.CAD_Redo()),
                null,
                Item("전체 선택", (s, e) => CadApi.StartCommand("selectall")),
                Item("선택 삭제", (s, e) => CadApi.StartCommand("delete"))));
            menu.Items.Add(Menu("뷰(&V)",
                Item("정면", (s, e) => CadApi.CAD_SetView(0)),
                Item("평면", (s, e) => CadApi.CAD_SetView(1)),
                Item("Isometric", (s, e) => CadApi.CAD_SetView(3)),
                null,
                Item("줌 맞춤", (s, e) => CadApi.CAD_ZoomExtents()),
                Item("투영 전환 (Ortho/Persp)", (s, e) => CadApi.ToggleProjection())));
            // 도면 — 엔진에선 ImGui 창이 여는 것들. 블록 만들기·편집은 명령행이 이름·기준점을 묻는 엔진 명령
            menu.Items.Add(Menu("도면(&D)",
                Item("도면층", (s, e) => ShowSide(_layers, () => _layers.ShowPage(0))),
                Item("선종류", (s, e) => ShowSide(_layers, () => _layers.ShowPage(1))),
                null,
                Item("블록 만들기 (선택한 객체로)", (s, e) => { CadApi.StartCommand("block"); _render.Focus(); }),
                Item("블록 편집 (선택한 블록 참조)", (s, e) => { CadApi.StartCommand("bedit"); _render.Focus(); }),
                Item("블록·외부 참조", (s, e) => ShowSide(_layers, () => _layers.ShowPage(2)))));
            _graphItem = Item("노드 그래프", (s, e) => ToggleGraph());
            _dynItem = Item("동적 입력\tF12", (s, e) => ToggleDynInput());
            _dynItem.Checked = _dynInput;
            // 이미지 편집은 선택한 이미지에 먹는 엔진 명령 — 붙이기만 호스트 파일 창
            menu.Items.Add(Menu("도구(&T)",
                _graphItem,
                Item("분해도", (s, e) => ShowSide(_tools, () => _tools.ShowPage(0))),
                Item("메시 수리", (s, e) => ShowSide(_tools, () => _tools.ShowPage(1))),
                null,
                Menu("이미지",
                    Item("붙이기...", (s, e) => AttachImage()),
                    Item("90° 회전", (s, e) => CadApi.StartCommand("imagerotate 90")),
                    Item("좌우 뒤집기", (s, e) => CadApi.StartCommand("imageflip h")),
                    Item("배경 지우기 (클릭)", (s, e) => { CadApi.StartCommand("imagebg"); _render.Focus(); }),
                    Item("자르기 (두 구석)", (s, e) => { CadApi.StartCommand("imagecrop"); _render.Focus(); })),
                null,
                _dynItem));
            menu.Items.Add(Menu("해석(&A)",
                Item("바람 터널", (s, e) => ShowSide(_analysis, () => _analysis.ShowPage(0))),
                Item("물", (s, e) => ShowSide(_analysis, () => _analysis.ShowPage(1))),
                Item("구조 해석", (s, e) => ShowSide(_analysis, () => _analysis.ShowPage(2)))));
            return menu;
        }

        static ToolStripMenuItem Menu(string text, params ToolStripItem[] items)
        {
            var m = new ToolStripMenuItem(text) { ForeColor = TextMain };
            foreach (var it in items) m.DropDownItems.Add(it ?? new ToolStripSeparator());
            return m;
        }

        static ToolStripMenuItem Item(string text, EventHandler onClick) =>
            new ToolStripMenuItem(text, null, onClick) { ForeColor = ColorTranslator.FromHtml("#1B1B1B") };

        // ── 툴바 ──
        Control BuildToolbar()
        {
            var bar = new FlowLayoutPanel
            {
                Dock = DockStyle.Top, Height = 44, BackColor = BarBg, WrapContents = false,
                Padding = new Padding(8, 7, 8, 0),
            };
            // 명령 버튼은 CadApi.StartCommand = 진행 중인 도구를 먼저 끝내고 시작(선 그리던 중 사각형 버튼도 바로 바뀜)
            bar.Controls.Add(GroupLabel("그리기"));
            bar.Controls.Add(ToolButton("큐브", (s, e) => CadApi.CAD_CreateBox(new CadApi.GeVec3(0, 0, 0), new CadApi.GeVec3(1, 1, 1), IntPtr.Zero, out _), accent: true));
            bar.Controls.Add(ToolButton("선", (s, e) => CadApi.StartCommand("line")));
            bar.Controls.Add(ToolButton("사각형", (s, e) => CadApi.StartCommand("rect")));
            bar.Controls.Add(ToolButton("원", (s, e) => CadApi.StartCommand("circle")));
            bar.Controls.Add(ToolButton("폴리라인", (s, e) => CadApi.StartCommand("polyline")));

            bar.Controls.Add(Separator());
            bar.Controls.Add(GroupLabel("편집"));
            bar.Controls.Add(ToolButton("전체선택", (s, e) => CadApi.StartCommand("selectall")));
            bar.Controls.Add(ToolButton("삭제", (s, e) => CadApi.StartCommand("delete")));
            bar.Controls.Add(ToolButton("↶ Undo", (s, e) => CadApi.CAD_Undo()));
            bar.Controls.Add(ToolButton("↷ Redo", (s, e) => CadApi.CAD_Redo()));

            bar.Controls.Add(Separator());
            bar.Controls.Add(GroupLabel("뷰"));
            bar.Controls.Add(ToolButton("정면", (s, e) => CadApi.CAD_SetView(0)));
            bar.Controls.Add(ToolButton("평면", (s, e) => CadApi.CAD_SetView(1)));
            bar.Controls.Add(ToolButton("Iso", (s, e) => CadApi.CAD_SetView(3)));
            bar.Controls.Add(ToolButton("줌맞춤", (s, e) => CadApi.CAD_ZoomExtents()));
            bar.Controls.Add(ToolButton("투영", (s, e) => CadApi.ToggleProjection()));

            bar.Controls.Add(Separator());
            bar.Controls.Add(GroupLabel("해석"));
            bar.Controls.Add(ToolButton("바람 터널", (s, e) => ShowSide(_analysis, () => _analysis.ShowPage(0))));
            bar.Controls.Add(ToolButton("물", (s, e) => ShowSide(_analysis, () => _analysis.ShowPage(1))));
            bar.Controls.Add(ToolButton("구조 해석", (s, e) => ShowSide(_analysis, () => _analysis.ShowPage(2))));
            return bar;
        }

        Button ToolButton(string text, EventHandler onClick, bool accent = false)
        {
            var b = new Button
            {
                // GrowAndShrink: 기본(GrowOnly)은 너비 75 아래로 안 줄어 툴바가 창 밖으로 넘친다
                Text = text, AutoSize = true, AutoSizeMode = AutoSizeMode.GrowAndShrink, MinimumSize = new Size(0, 30),
                Margin = new Padding(2, 0, 2, 0),
                Padding = new Padding(4, 0, 4, 0), FlatStyle = FlatStyle.Flat, Cursor = Cursors.Hand,
                BackColor = accent ? Accent : BtnBg, ForeColor = accent ? Color.White : TextMain,
                Font = accent ? new Font(Font, FontStyle.Bold) : Font,
                TabStop = false,   // 버튼이 포커스를 가져가면 키 입력이 렌더 영역(엔진)으로 안 간다
            };
            b.FlatAppearance.BorderSize = 0;
            b.FlatAppearance.MouseOverBackColor = accent ? Accent : BtnHover;
            b.FlatAppearance.MouseDownBackColor = Accent;
            b.Click += onClick;
            b.Click += (s, e) => _render.Focus();   // 누른 뒤 키보드는 다시 엔진으로(명령행 입력·ESC)
            return b;
        }

        static Label GroupLabel(string text) => new Label
        {
            Text = text, AutoSize = true, ForeColor = TextDim, Font = new Font("맑은 고딕", 8f),
            Margin = new Padding(10, 8, 6, 0),
        };

        static Control Separator() => new Panel
        {
            Width = 1, Height = 22, BackColor = BtnHover, Margin = new Padding(8, 4, 8, 0),
        };

        // ── 상태바 ──
        Control BuildStatusBar()
        {
            var bar = new Panel { Dock = DockStyle.Bottom, Height = 28, BackColor = BarBg, Padding = new Padding(12, 6, 12, 0) };
            bar.Controls.Add(_status);
            bar.Controls.Add(_info);
            return bar;
        }

        // ── 왼쪽 정보 ──
        Control BuildSidePanel()
        {
            var side = new FlowLayoutPanel
            {
                Dock = DockStyle.Left, Width = 230, BackColor = Bg, FlowDirection = FlowDirection.TopDown,
                WrapContents = false, Padding = new Padding(14),
            };
            side.Controls.Add(new Label { Text = "LotCAD", AutoSize = true, ForeColor = ColorTranslator.FromHtml("#F0F0F0"),
                                          Font = new Font("맑은 고딕", 12f, FontStyle.Bold) });
            side.Controls.Add(new Label { Text = "WinForms 호스트 샘플", AutoSize = true, ForeColor = TextDim,
                                          Font = new Font("맑은 고딕", 8.25f), Margin = new Padding(3, 1, 3, 0) });
            side.Controls.Add(Rule());
            side.Controls.Add(new Label { Text = "조작", AutoSize = true, ForeColor = ColorTranslator.FromHtml("#9AA0AA"),
                                          Font = new Font("맑은 고딕", 8.25f, FontStyle.Bold) });
            side.Controls.Add(new Label { Text = "우클릭 드래그 — 회전\n중클릭 드래그 — 팬\n휠 — 줌\n좌클릭 — 선택", AutoSize = true,
                                          ForeColor = TextBody, Margin = new Padding(3, 4, 3, 0) });
            side.Controls.Add(Rule());
            side.Controls.Add(new Label { Text = "씬", AutoSize = true, ForeColor = ColorTranslator.FromHtml("#9AA0AA"),
                                          Font = new Font("맑은 고딕", 8.25f, FontStyle.Bold) });
            _sceneInfo.Margin = new Padding(3, 4, 3, 0);
            side.Controls.Add(_sceneInfo);
            return side;
        }

        static Control Rule() => new Panel { Height = 1, Width = 200, BackColor = Line, Margin = new Padding(3, 12, 3, 12) };

        // ── Win32 ──
        [StructLayout(LayoutKind.Sequential)]
        struct MSG { public IntPtr hwnd; public uint message; public IntPtr wParam, lParam; public uint time; public int x, y; }

        [DllImport("user32.dll")]
        static extern bool PeekMessage(out MSG msg, IntPtr hWnd, uint filterMin, uint filterMax, uint remove);
    }
}
