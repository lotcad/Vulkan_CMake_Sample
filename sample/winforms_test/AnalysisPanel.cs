using System;
using System.Drawing;
using System.Linq;
using System.Text.Json.Nodes;
using System.Windows.Forms;

namespace LotCadWinForms
{
    // 해석 패널 — 바람 터널 · 물 · 구조 해석. 오른쪽에 붙는다(MainForm 의 툴바·메뉴 "해석" 이 연다).
    // 엔진 자체 해석 패널(ImGui)은 호스트 창 안에서 그려지지 않아, 같은 일을 C API(Analysis.cs)로 여기서 한다.
    //
    // 흐름
    //   바람 터널: 솔리드 선택 → 시작(다음 프레임에 켜짐) → 단면·연기·표면 압력으로 보기. 바람은 +X.
    //   물:        닫힌 솔리드(그릇) 선택 → 물 높이 → 시작 → 기울이기·흔들기
    //   구조 해석: 솔리드 선택 → 열기(면 목록이 온다) → 면 골라 고정·하중 → 실행(작업 스레드) → 결과·색 보기
    // 상태는 엔진이 프레임마다 바꾼다(켜짐·풀이 끝) — 보이는 동안 0.3초마다 {"op":"status"} 로 읽는다.
    public sealed class AnalysisPanel : UserControl
    {
        static readonly Color Bg = ColorTranslator.FromHtml("#1E1F22");
        static readonly Color FieldBg = ColorTranslator.FromHtml("#2B2D31");
        static readonly Color Accent = ColorTranslator.FromHtml("#2D6CDF");
        static readonly Color TextMain = ColorTranslator.FromHtml("#E6E6E6");
        static readonly Color TextDim = ColorTranslator.FromHtml("#9AA0AA");
        static readonly Color ErrorColor = ColorTranslator.FromHtml("#FF8A80");

        static readonly (string, string)[] Grids = { ("빠름", "fast"), ("보통", "normal"), ("정밀", "fine") };

        readonly Timer _timer = new Timer { Interval = 300 };
        readonly Label _error = new Label { AutoSize = false, Dock = DockStyle.Bottom, Height = 40, ForeColor = ErrorColor };
        readonly Panel _pages = new Panel { Dock = DockStyle.Fill };
        readonly Button[] _pageButtons = new Button[3];
        readonly Control[] _pageControls = new Control[3];
        JsonObject _wind = new(), _water = new(), _sim = new();

        public AnalysisPanel()
        {
            Width = 330;
            BackColor = Bg;
            ForeColor = TextMain;
            Padding = new Padding(8, 6, 8, 6);

            _pageControls[0] = BuildWind();
            _pageControls[1] = BuildWater();
            _pageControls[2] = BuildSim();
            foreach (var p in _pageControls) { p.Dock = DockStyle.Fill; p.Visible = false; _pages.Controls.Add(p); }

            var header = new FlowLayoutPanel { Dock = DockStyle.Top, Height = 34, WrapContents = false };
            string[] titles = { "바람 터널", "물", "구조 해석" };
            for (int i = 0; i < 3; i++)
            {
                int page = i;
                _pageButtons[i] = Btn(titles[i], () => ShowPage(page));
                header.Controls.Add(_pageButtons[i]);
            }
            header.Controls.Add(Btn("✕", () => Visible = false));

            Controls.Add(_pages);   // 채움을 먼저, 위·아래를 나중에(도킹 순서)
            Controls.Add(_error);
            Controls.Add(header);

            _timer.Tick += (s, e) => RefreshState();
            VisibleChanged += (s, e) => { _timer.Enabled = Visible; if (Visible) RefreshState(); };
            ShowPage(0);
        }

        /// <summary>0 = 바람 터널, 1 = 물, 2 = 구조 해석.</summary>
        public void ShowPage(int page)
        {
            for (int i = 0; i < 3; i++)
            {
                _pageControls[i].Visible = i == page;
                _pageButtons[i].BackColor = i == page ? Accent : FieldBg;
            }
            Visible = true;
        }

        /// <summary>창을 닫을 때 엔진을 헐기 **전에** — 헐린 엔진에 status 를 묻지 않게.</summary>
        public void Shutdown() => _timer.Stop();

        JsonObject Call(string which, object args)
        {
            var r = Analysis.Call(which, args);
            _error.Text = Analysis.Str(r, "error") ?? "";
            if (r.ContainsKey("ok")) RefreshState();
            return r;
        }

        uint[] NeedSelection()
        {
            var ids = Analysis.SelectedIds();
            if (ids.Length == 0) _error.Text = "3D 뷰에서 대상 솔리드를 먼저 선택하세요";
            return ids;
        }

        // ── 바람 터널 ──
        Label _windState, _windSpeedLabel, _windInfo;
        ComboBox _windGrid, _windField, _windPlane;
        TrackBar _windSpeed, _windAt;
        Button _windStart, _windPause;
        Control[] _windRunning;

        Control BuildWind()
        {
            var page = Page();
            _windState = Lbl("", wrap: true);
            _windGrid = Combo(Grids, 0);
            _windSpeed = Track(0.02, 0.10, 0.06);
            _windSpeedLabel = Lbl("");
            _windSpeed.Scroll += (s, e) =>
            {
                ShowWindSpeed();
                if (Analysis.Bool(_wind, "active")) Call(Analysis.Wind, new { op = "wind", value = Real(_windSpeed) });
            };
            _windStart = Btn("시작", () =>
            {
                var ids = NeedSelection();
                if (ids.Length > 0)
                    Call(Analysis.Wind, new { op = "start", ids, grid = Value(_windGrid), wind = Real(_windSpeed) });
            });
            _windPause = Btn("일시정지", () => Call(Analysis.Wind, new { op = Analysis.IsFalse(_wind, "flowing") ? "play" : "pause" }));
            _windRunning = new Control[] { Btn("정지", () => Call(Analysis.Wind, new { op = "stop" })), _windPause,
                                           Btn("초기화", () => Call(Analysis.Wind, new { op = "reset" })) };
            _windField = Combo(new[] { ("속도", "speed"), ("압력", "pressure"), ("소용돌이", "vortex"), ("연기", "smoke") }, 0);
            _windField.SelectionChangeCommitted += (s, e) => Call(Analysis.Wind, new { op = "view", field = Value(_windField) });
            _windPlane = Combo(new[] { ("X", "x"), ("Y", "y"), ("Z", "z") }, 1);
            _windAt = Track(0, 1, 0.5, 100);
            EventHandler plane = (s, e) => Call(Analysis.Wind, new { op = "view", plane = Value(_windPlane), at = Real(_windAt) });
            _windPlane.SelectionChangeCommitted += plane;
            _windAt.Scroll += plane;
            var surface = Check("표면 압력 색", on => Call(Analysis.Wind, new { op = "view", surface = on }));
            var smoke = Check("연기", on => Call(Analysis.Wind, new { op = "view", smoke = on }));
            _windInfo = Lbl("", wrap: true);

            Add(page, _windState, Caption("격자"), _windGrid, _windSpeedLabel, _windSpeed,
                Row(_windStart, _windRunning[0], _windPause, _windRunning[2]),
                Caption("보기"), Caption("색"), _windField, Caption("단면"), _windPlane, Caption("단면 위치"), _windAt,
                surface, smoke, _windInfo);
            ShowWindSpeed();
            return page;
        }

        void ShowWindSpeed() => _windSpeedLabel.Text = $"바람 세기 {Real(_windSpeed):0.000}";

        void ShowWind(JsonObject w)
        {
            bool active = Analysis.Bool(w, "active");
            int n = (w["ids"] as JsonArray)?.Count ?? 0;
            _windState.Text = active ? $"켜짐 — 솔리드 {n}개 둘레, 바람 +X"
                            : Analysis.Bool(w, "starting") ? "켜는 중…" : "꺼짐 — 솔리드를 선택하고 시작";
            _windStart.Enabled = !active;
            foreach (var c in _windRunning) c.Enabled = active;
            _windPause.Text = Analysis.IsFalse(w, "flowing") ? "재생" : "일시정지";
            string info = "";
            if (active)
            {
                info = $"항력 계수 {Analysis.Num(w["drag_coefficient"], "0.000")}";
                if (Analysis.Cells(w["cells"]) is string cells) info += $"   격자 {cells}";
            }
            _windInfo.Text = info;
        }

        // ── 물 ──
        Label _waterState, _waterInfo;
        ComboBox _waterGrid;
        TrackBar _waterLevel, _tiltX, _tiltY, _shakeAmp;
        Button _waterStart, _waterPause;
        Control[] _waterRunning;

        Control BuildWater()
        {
            var page = Page();
            _waterState = Lbl("", wrap: true);
            _waterGrid = Combo(Grids, 1);
            _waterLevel = Track(0.05, 0.95, 0.5, 90);
            _waterStart = Btn("시작", () =>
            {
                var ids = NeedSelection();
                if (ids.Length > 0)
                    Call(Analysis.Water, new { op = "start", id = ids[0], level = Real(_waterLevel), grid = Value(_waterGrid) });
            });
            _waterPause = Btn("일시정지", () => Call(Analysis.Water, new { op = Analysis.IsFalse(_water, "flowing") ? "play" : "pause" }));
            _tiltX = Track(-40, 40, 0, 80);
            _tiltY = Track(-40, 40, 0, 80);
            EventHandler tilt = (s, e) => Call(Analysis.Water, new { op = "tilt", x = Real(_tiltX), y = Real(_tiltY) });
            _tiltX.Scroll += tilt;
            _tiltY.Scroll += tilt;
            _shakeAmp = Track(0.05, 1.0, 0.3, 95);
            // 주기를 비우면 엔진이 첫 출렁임 공진 주기로 흔든다
            var shake = Btn("흔들기(공진)", () => Call(Analysis.Water, new { op = "shake", amplitude = Real(_shakeAmp) }));
            var unshake = Btn("멈춤", () => Call(Analysis.Water, new { op = "shake", amplitude = 0 }));
            var stop = Btn("정지", () => Call(Analysis.Water, new { op = "stop" }));
            var reset = Btn("초기화", () => Call(Analysis.Water, new { op = "reset" }));
            _waterRunning = new Control[] { stop, _waterPause, reset, _tiltX, _tiltY, shake, unshake };
            _waterInfo = Lbl("", wrap: true);

            Add(page, _waterState, Caption("격자"), _waterGrid, Caption("물 높이"), _waterLevel,
                Row(_waterStart, stop, _waterPause, reset),
                Caption("기울이기 X"), _tiltX, Caption("기울이기 Y"), _tiltY,
                Caption("흔들기 세기"), _shakeAmp, Row(shake, unshake), _waterInfo);
            return page;
        }

        void ShowWater(JsonObject w)
        {
            bool active = Analysis.Bool(w, "active");
            _waterState.Text = active ? $"켜짐 — 그릇 #{w["container"]}"
                             : Analysis.Bool(w, "starting") ? "켜는 중…" : "꺼짐 — 닫힌 솔리드(그릇)를 선택하고 시작";
            _waterStart.Enabled = !active;
            foreach (var c in _waterRunning) c.Enabled = active;
            _waterPause.Text = Analysis.IsFalse(w, "flowing") ? "재생" : "일시정지";
            string info = "";
            if (active)
            {
                if (Analysis.Cells(w["cells"]) is string cells) info = $"격자 {cells}   ";
                double? drift = Analysis.Number(w["mass_drift"]);
                info += "질량 오차 " + (drift is double d ? $"{d * 100:0.0000}%" : "-");
            }
            _waterInfo.Text = info;
        }

        // ── 구조 해석 ──
        ComboBox _simType, _simMaterial, _simSize, _simShow;
        ListBox _faces;
        Control _loadBox, _heatBox, _runRow, _showRow, _facesCaption;
        NumericUpDown _fx, _fy, _fz, _pressure, _temp, _flux, _convH, _convAmb;
        Button _simClose, _simRun, _simCancel, _simConverge, _simClear;
        Label _simResult;
        int _face = -1;            // 고른 면
        string _facesKey, _showKind;
        bool _filling;             // 면 목록을 다시 채우는 동안 선택 이벤트 무시

        Control BuildSim()
        {
            var page = Page();
            var open = Btn("선택한 솔리드로 열기", () =>
            {
                var ids = NeedSelection();
                if (ids.Length > 0) { _face = -1; Call(Analysis.Sim, new { op = "open", id = ids[0] }); }
            });
            _simClose = Btn("닫기", () => { _face = -1; Call(Analysis.Sim, new { op = "close" }); });
            _simType = Combo(new[] { ("응력", "stress"), ("열전도", "heat"), ("진동 모드", "modal"), ("좌굴", "buckling") }, 0);
            _simMaterial = Combo(new[] { ("강철(S275)", "steel"), ("알루미늄(6061-T6)", "aluminum"), ("스테인리스", "stainless"),
                                         ("티타늄", "titanium"), ("ABS", "abs") }, 0);
            _simSize = Combo(Grids, 1);
            _simType.SelectionChangeCommitted += (s, e) => Call(Analysis.Sim, new { op = "set", type = Value(_simType) });
            _simMaterial.SelectionChangeCommitted += (s, e) => Call(Analysis.Sim, new { op = "set", material = Value(_simMaterial) });
            _simSize.SelectionChangeCommitted += (s, e) => Call(Analysis.Sim, new { op = "set", size = Value(_simSize) });

            _faces = new ListBox { Width = 300, Height = 130, BackColor = FieldBg, ForeColor = TextMain, BorderStyle = BorderStyle.None };
            _faces.SelectedIndexChanged += (s, e) =>
            {
                if (_filling) return;
                _face = _faces.SelectedItem is FaceItem f ? f.Index : -1;
                _loadBox.Enabled = _heatBox.Enabled = _face >= 0;
            };

            // 하중 조건 — 응력·진동·좌굴
            _fx = Number(0); _fy = Number(0); _fz = Number(-1000); _pressure = Number(1);
            _loadBox = Box(
                Row(Btn("고정", () => Call(Analysis.Sim, new { op = "fix", face = _face })),
                    Btn("풀기", () => Call(Analysis.Sim, new { op = "free", face = _face }))),
                Caption("힘 N  (x · y · z)"),
                Row(_fx, _fy, _fz, Btn("걸기", () => Call(Analysis.Sim,
                    new { op = "force", face = _face, force = new[] { _fx.Value, _fy.Value, _fz.Value } }))),
                Caption("압력 MPa"),
                Row(_pressure, Btn("걸기", () => Call(Analysis.Sim, new { op = "pressure", face = _face, value = _pressure.Value }))));
            // 열 조건
            _temp = Number(80); _flux = Number(10); _convH = Number(10); _convAmb = Number(20);
            _heatBox = Box(
                Caption("온도 °C"), Row(_temp, Btn("걸기", () => Call(Analysis.Sim, new { op = "temp", face = _face, value = _temp.Value }))),
                Caption("열 W"), Row(_flux, Btn("걸기", () => Call(Analysis.Sim, new { op = "flux", face = _face, value = _flux.Value }))),
                Caption("대류 h · 주변 °C"),
                Row(_convH, _convAmb, Btn("걸기", () => Call(Analysis.Sim,
                    new { op = "convect", face = _face, h = _convH.Value, ambient = _convAmb.Value }))));

            _simRun = Btn("실행", () => Call(Analysis.Sim, new { op = "run" }));
            _simCancel = Btn("취소", () => Call(Analysis.Sim, new { op = "cancel" }));
            _simConverge = Btn("수렴 확인", () => Call(Analysis.Sim, new { op = "converge" }));
            _simClear = Btn("지우기", () => Call(Analysis.Sim, new { op = "clear" }));
            _runRow = Row(_simRun, _simCancel, _simConverge, _simClear);
            _simShow = Combo(Array.Empty<(string, string)>(), -1);
            _simShow.SelectionChangeCommitted += (s, e) => Call(Analysis.Sim, new { op = "set", show = Value(_simShow) });
            _showRow = Row(Caption("색"), _simShow);
            _simResult = Lbl("", wrap: true);
            _facesCaption = Caption("면 — 골라서 조건을 건다");

            Add(page, Row(open, _simClose), Caption("종류"), _simType, Caption("재료"), _simMaterial, Caption("요소"), _simSize,
                _facesCaption, _faces, _loadBox, _heatBox, _runRow, _showRow, _simResult);
            return page;
        }

        sealed class FaceItem
        {
            public int Index;
            public string Text;
            public override string ToString() => Text;
        }

        void ShowSim(JsonObject s)
        {
            var faces = s["faces"] as JsonArray ?? new JsonArray();
            bool isOpen = faces.Count > 0;
            string kind = Analysis.Str(s, "type") ?? "stress";
            bool busy = Analysis.Bool(s, "busy");
            var result = s["result"] as JsonObject;

            Select(_simType, Analysis.Str(s, "type"));
            Select(_simMaterial, Analysis.Str(s, "material"));
            Select(_simSize, Analysis.Str(s, "size"));
            _simClose.Enabled = isOpen;
            _facesCaption.Visible = _faces.Visible = _runRow.Visible = isOpen;
            _loadBox.Visible = isOpen && kind != "heat";
            _heatBox.Visible = isOpen && kind == "heat";
            _loadBox.Enabled = _heatBox.Enabled = _face >= 0;

            // 면 목록 — 면이나 조건이 바뀔 때만 다시 채운다(고른 줄 유지)
            var conds = (s["conditions"] as JsonArray ?? new JsonArray()).Concat(s["heat_conditions"] as JsonArray ?? new JsonArray()).ToList();
            string key = faces.ToJsonString() + string.Join(",", conds.Select(c => c?.ToJsonString()));
            if (key != _facesKey)
            {
                _facesKey = key;
                _filling = true;
                _faces.Items.Clear();
                foreach (var f in faces)
                {
                    int index = (int)(Analysis.Number(f?["index"]) ?? -1);
                    string tags = string.Join("·", conds.Where(c => Analysis.Number(c?["face"]) == index).Select(c => Analysis.Str(c, "kind")));
                    var item = new FaceItem
                    {
                        Index = index,
                        Text = $"면 {index}   {Analysis.AxisName(f?["normal"])}   넓이 {Analysis.Num(f?["area"], "G3")}" +
                               (tags.Length > 0 ? $"   [{tags}]" : ""),
                    };
                    _faces.Items.Add(item);
                    if (index == _face) _faces.SelectedItem = item;
                }
                _filling = false;
                if (!isOpen) _face = -1;
            }

            _simRun.Text = busy ? "푸는 중…" : "실행";
            _simRun.Enabled = !busy;
            _simCancel.Enabled = busy;
            _simConverge.Enabled = !busy && result != null;
            _simClear.Enabled = !busy;

            // 결과 색 — 종류마다 고를 수 있는 것이 다르다
            _showRow.Visible = result != null;
            if (kind != _showKind)
            {
                _showKind = kind;
                _simShow.Items.Clear();
                var items = kind == "heat" ? new[] { ("온도", "temp"), ("열 흐름", "flux") }
                          : kind == "stress" ? new[] { ("응력", "stress"), ("변위", "disp"), ("안전율", "safety") }
                          : Enumerable.Range(1, 6).Select(k => ($"모드 {k}", $"mode {k}")).ToArray();
                foreach (var (text, value) in items) _simShow.Items.Add(new Choice(text, value));
            }
            _simResult.Text = Analysis.ResultText(result);
        }

        // ── 상태 → 화면 ──
        void RefreshState()
        {
            if (!Visible) return;
            var w = Analysis.Call(Analysis.Wind, new { op = "status" });
            var a = Analysis.Call(Analysis.Water, new { op = "status" });
            var s = Analysis.Call(Analysis.Sim, new { op = "status" });
            // status 자체가 실패(엔진 없음 등)면 지난 상태를 그대로 둔다
            if (!Analysis.IsFalse(w, "ok")) _wind = w;
            if (!Analysis.IsFalse(a, "ok")) _water = a;
            if (!Analysis.IsFalse(s, "ok")) _sim = s;
            ShowWind(_wind);
            ShowWater(_water);
            ShowSim(_sim);
        }

        // ── 컨트롤 도우미 (다크) ──
        sealed class Choice
        {
            public readonly string Text, Value;
            public Choice(string text, string value) { Text = text; Value = value; }
            public override string ToString() => Text;
        }

        static string Value(ComboBox box) => (box.SelectedItem as Choice)?.Value;

        static void Select(ComboBox box, string value)
        {
            if (value == null || box.DroppedDown) return;   // 사용자가 고르는 중이면 건드리지 않는다
            for (int i = 0; i < box.Items.Count; i++)
                if (((Choice)box.Items[i]).Value == value && box.SelectedIndex != i) box.SelectedIndex = i;
        }

        static ComboBox Combo((string, string)[] items, int selected)
        {
            var box = new ComboBox { DropDownStyle = ComboBoxStyle.DropDownList, Width = 300, BackColor = FieldBg, ForeColor = TextMain,
                                     FlatStyle = FlatStyle.Flat };
            foreach (var (text, value) in items) box.Items.Add(new Choice(text, value));
            if (selected >= 0 && selected < items.Length) box.SelectedIndex = selected;
            return box;
        }

        // TrackBar 는 정수라 steps 칸으로 나눈다. 실수 범위는 Tag 에.
        static TrackBar Track(double lo, double hi, double value, int steps = 1000)
        {
            var t = new TrackBar { Minimum = 0, Maximum = steps, TickStyle = TickStyle.None, Width = 300, BackColor = Bg,
                                   Tag = (lo, hi), AutoSize = false, Height = 28 };
            t.Value = (int)Math.Round((value - lo) / (hi - lo) * steps);
            return t;
        }

        static double Real(TrackBar t)
        {
            var (lo, hi) = ((double, double))t.Tag;
            return lo + (hi - lo) * t.Value / t.Maximum;
        }

        static NumericUpDown Number(decimal value) => new NumericUpDown
        {
            Minimum = -1000000, Maximum = 1000000, DecimalPlaces = 1, Value = value, Width = 64,
            BackColor = FieldBg, ForeColor = TextMain, BorderStyle = BorderStyle.FixedSingle,
        };

        static Button Btn(string text, Action onClick)
        {
            var b = new Button
            {
                Text = text, AutoSize = true, AutoSizeMode = AutoSizeMode.GrowAndShrink, MinimumSize = new Size(0, 28),
                Margin = new Padding(0, 2, 4, 2), Padding = new Padding(4, 0, 4, 0), FlatStyle = FlatStyle.Flat,
                BackColor = FieldBg, ForeColor = TextMain, Cursor = Cursors.Hand,
            };
            b.FlatAppearance.BorderSize = 0;
            b.Click += (s, e) => onClick();
            return b;
        }

        static CheckBox Check(string text, Action<bool> onChanged)
        {
            var c = new CheckBox { Text = text, AutoSize = true, ForeColor = TextMain, Margin = new Padding(0, 4, 0, 0) };
            c.CheckedChanged += (s, e) => onChanged(c.Checked);
            return c;
        }

        static Label Lbl(string text, bool wrap = false) => new Label
        {
            // 줄바꿈 글은 폭을 300 으로 묶고 높이만 늘어나게(AutoSize + MaximumSize)
            Text = text, ForeColor = TextMain, AutoSize = true,
            MaximumSize = wrap ? new Size(300, 0) : Size.Empty, Margin = new Padding(0, 4, 0, 2),
        };

        static Label Caption(string text) => new Label
        {
            Text = text, AutoSize = true, ForeColor = TextDim, Margin = new Padding(0, 8, 0, 2),
        };

        static FlowLayoutPanel Row(params Control[] items)
        {
            var row = new FlowLayoutPanel { AutoSize = true, WrapContents = false, Margin = new Padding(0, 2, 0, 2) };
            row.Controls.AddRange(items);
            return row;
        }

        static FlowLayoutPanel Box(params Control[] items)
        {
            var box = new FlowLayoutPanel { AutoSize = true, FlowDirection = FlowDirection.TopDown, WrapContents = false,
                                            Margin = new Padding(0) };
            box.Controls.AddRange(items);
            return box;
        }

        static FlowLayoutPanel Page() => new FlowLayoutPanel
        {
            FlowDirection = FlowDirection.TopDown, WrapContents = false, AutoScroll = true, Padding = new Padding(0, 4, 0, 4),
        };

        static void Add(Control page, params Control[] items) => page.Controls.AddRange(items);
    }
}
