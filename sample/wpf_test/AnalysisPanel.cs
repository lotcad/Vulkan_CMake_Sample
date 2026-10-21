using System;
using System.Linq;
using System.Text.Json.Nodes;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;
using System.Windows.Threading;

namespace LotCadWpf
{
    // 해석 패널 — 바람 터널 · 물 · 구조 해석. 오른쪽에 붙는다(MainWindow 의 툴바·메뉴 "해석" 이 연다).
    // 엔진 자체 해석 패널(ImGui)은 호스트 창 안에서 그려지지 않아, 같은 일을 C API(Analysis.cs)로 여기서 한다.
    // XAML 없이 코드로만 만든다 — WinForms 샘플의 AnalysisPanel.cs 와 같은 구성·같은 이름.
    //
    // 흐름
    //   바람 터널: 솔리드 선택 → 시작(다음 프레임에 켜짐) → 단면·연기·표면 압력으로 보기. 바람은 +X.
    //   물:        닫힌 솔리드(그릇) 선택 → 물 높이 → 시작 → 기울이기·흔들기
    //   구조 해석: 솔리드 선택 → 열기(면 목록이 온다) → 면 골라 고정·하중 → 실행(작업 스레드) → 결과·색 보기
    // 상태는 엔진이 프레임마다 바꾼다(켜짐·풀이 끝) — 보이는 동안 0.3초마다 {"op":"status"} 로 읽는다.
    public sealed class AnalysisPanel : UserControl
    {
        static readonly Brush Bg = Hex("#1E1F22");
        static readonly Brush FieldBg = Hex("#2B2D31");
        static readonly Brush Accent = Hex("#2D6CDF");
        static readonly Brush TextMain = Hex("#E6E6E6");
        static readonly Brush TextDim = Hex("#9AA0AA");
        static readonly Brush ErrorColor = Hex("#FF8A80");

        static readonly (string, string)[] Grids = { ("빠름", "fast"), ("보통", "normal"), ("정밀", "fine") };

        readonly DispatcherTimer _timer = new DispatcherTimer { Interval = TimeSpan.FromMilliseconds(300) };
        readonly TextBlock _error = new TextBlock { Foreground = ErrorColor, TextWrapping = TextWrapping.Wrap, Margin = new Thickness(0, 6, 0, 0) };
        readonly Button[] _pageButtons = new Button[3];
        readonly FrameworkElement[] _pages = new FrameworkElement[3];
        JsonObject _wind = new(), _water = new(), _sim = new();

        public AnalysisPanel()
        {
            Width = 330;
            Background = Bg;
            Foreground = TextMain;

            _pages[0] = Scroll(BuildWind());
            _pages[1] = Scroll(BuildWater());
            _pages[2] = Scroll(BuildSim());

            var header = new StackPanel { Orientation = Orientation.Horizontal, Margin = new Thickness(0, 0, 0, 6) };
            string[] titles = { "바람 터널", "물", "구조 해석" };
            for (int i = 0; i < 3; i++)
            {
                int page = i;
                _pageButtons[i] = Btn(titles[i], () => ShowPage(page));
                header.Children.Add(_pageButtons[i]);
            }
            header.Children.Add(Btn("✕", () => Visibility = Visibility.Collapsed));

            var root = new DockPanel { Margin = new Thickness(8, 6, 8, 6) };
            DockPanel.SetDock(header, Dock.Top);
            DockPanel.SetDock(_error, Dock.Bottom);
            root.Children.Add(header);
            root.Children.Add(_error);
            var pageHost = new Grid();
            foreach (var p in _pages) pageHost.Children.Add(p);
            root.Children.Add(pageHost);
            Content = root;

            _timer.Tick += (s, e) => RefreshState();
            IsVisibleChanged += (s, e) => { if (IsVisible) { _timer.Start(); RefreshState(); } else _timer.Stop(); };
            ShowPage(0);
            Visibility = Visibility.Collapsed;
        }

        /// <summary>0 = 바람 터널, 1 = 물, 2 = 구조 해석.</summary>
        public void ShowPage(int page)
        {
            for (int i = 0; i < 3; i++)
            {
                _pages[i].Visibility = i == page ? Visibility.Visible : Visibility.Collapsed;
                _pageButtons[i].Background = i == page ? Accent : FieldBg;
            }
            Visibility = Visibility.Visible;
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
        TextBlock _windState, _windSpeedLabel, _windInfo;
        ComboBox _windGrid, _windField, _windPlane;
        Slider _windSpeed, _windAt;
        Button _windStart, _windPause;
        UIElement[] _windRunning;

        UIElement BuildWind()
        {
            _windState = Lbl("");
            _windGrid = Combo(Grids, 0);
            _windSpeed = Track(0.02, 0.10, 0.06);
            _windSpeedLabel = Lbl("");
            _windSpeed.ValueChanged += (s, e) =>
            {
                ShowWindSpeed();
                // 끄는 중(사용자 끌기)에만 엔진에 — 프로그램이 값을 바꿀 때는 보내지 않는다
                if (_windSpeed.IsMouseCaptureWithin && Analysis.Bool(_wind, "active"))
                    Call(Analysis.Wind, new { op = "wind", value = _windSpeed.Value });
            };
            _windStart = Btn("시작", () =>
            {
                var ids = NeedSelection();
                if (ids.Length > 0)
                    Call(Analysis.Wind, new { op = "start", ids, grid = Value(_windGrid), wind = _windSpeed.Value });
            });
            _windPause = Btn("일시정지", () => Call(Analysis.Wind, new { op = Analysis.IsFalse(_wind, "flowing") ? "play" : "pause" }));
            _windRunning = new UIElement[] { Btn("정지", () => Call(Analysis.Wind, new { op = "stop" })), _windPause,
                                             Btn("초기화", () => Call(Analysis.Wind, new { op = "reset" })) };
            _windField = Combo(new[] { ("속도", "speed"), ("압력", "pressure"), ("소용돌이", "vortex"), ("연기", "smoke") }, 0);
            _windField.DropDownClosed += (s, e) => Call(Analysis.Wind, new { op = "view", field = Value(_windField) });
            _windPlane = Combo(new[] { ("X", "x"), ("Y", "y"), ("Z", "z") }, 1);
            _windAt = Track(0, 1, 0.5);
            _windPlane.DropDownClosed += (s, e) => SendPlane();
            _windAt.ValueChanged += (s, e) => { if (_windAt.IsMouseCaptureWithin) SendPlane(); };
            var surface = Check("표면 압력 색", on => Call(Analysis.Wind, new { op = "view", surface = on }));
            var smoke = Check("연기", on => Call(Analysis.Wind, new { op = "view", smoke = on }));
            _windInfo = Lbl("");

            ShowWindSpeed();
            return Stack(_windState, Caption("격자"), _windGrid, _windSpeedLabel, _windSpeed,
                         Row(_windStart, _windRunning[0], _windPause, _windRunning[2]),
                         Caption("보기"), Caption("색"), _windField, Caption("단면"), _windPlane, Caption("단면 위치"), _windAt,
                         surface, smoke, _windInfo);
        }

        void SendPlane() => Call(Analysis.Wind, new { op = "view", plane = Value(_windPlane), at = _windAt.Value });

        void ShowWindSpeed() => _windSpeedLabel.Text = $"바람 세기 {_windSpeed.Value:0.000}";

        void ShowWind(JsonObject w)
        {
            bool active = Analysis.Bool(w, "active");
            int n = (w["ids"] as JsonArray)?.Count ?? 0;
            _windState.Text = active ? $"켜짐 — 솔리드 {n}개 둘레, 바람 +X"
                            : Analysis.Bool(w, "starting") ? "켜는 중…" : "꺼짐 — 솔리드를 선택하고 시작";
            _windStart.IsEnabled = !active;
            foreach (var c in _windRunning) c.IsEnabled = active;
            _windPause.Content = Analysis.IsFalse(w, "flowing") ? "재생" : "일시정지";
            string info = "";
            if (active)
            {
                info = $"항력 계수 {Analysis.Num(w["drag_coefficient"], "0.000")}";
                if (Analysis.Cells(w["cells"]) is string cells) info += $"   격자 {cells}";
            }
            _windInfo.Text = info;
        }

        // ── 물 ──
        TextBlock _waterState, _waterInfo;
        ComboBox _waterGrid;
        Slider _waterLevel, _tiltX, _tiltY, _shakeAmp;
        Button _waterStart, _waterPause;
        UIElement[] _waterRunning;

        UIElement BuildWater()
        {
            _waterState = Lbl("");
            _waterGrid = Combo(Grids, 1);
            _waterLevel = Track(0.05, 0.95, 0.5);
            _waterStart = Btn("시작", () =>
            {
                var ids = NeedSelection();
                if (ids.Length > 0)
                    Call(Analysis.Water, new { op = "start", id = ids[0], level = _waterLevel.Value, grid = Value(_waterGrid) });
            });
            _waterPause = Btn("일시정지", () => Call(Analysis.Water, new { op = Analysis.IsFalse(_water, "flowing") ? "play" : "pause" }));
            _tiltX = Track(-40, 40, 0);
            _tiltY = Track(-40, 40, 0);
            RoutedPropertyChangedEventHandler<double> tilt = (s, e) =>
            {
                if (((Slider)s).IsMouseCaptureWithin)
                    Call(Analysis.Water, new { op = "tilt", x = _tiltX.Value, y = _tiltY.Value });
            };
            _tiltX.ValueChanged += tilt;
            _tiltY.ValueChanged += tilt;
            _shakeAmp = Track(0.05, 1.0, 0.3);
            // 주기를 비우면 엔진이 첫 출렁임 공진 주기로 흔든다
            var shake = Btn("흔들기(공진)", () => Call(Analysis.Water, new { op = "shake", amplitude = _shakeAmp.Value }));
            var unshake = Btn("멈춤", () => Call(Analysis.Water, new { op = "shake", amplitude = 0 }));
            var stop = Btn("정지", () => Call(Analysis.Water, new { op = "stop" }));
            var reset = Btn("초기화", () => Call(Analysis.Water, new { op = "reset" }));
            _waterRunning = new UIElement[] { stop, _waterPause, reset, _tiltX, _tiltY, shake, unshake };
            _waterInfo = Lbl("");

            return Stack(_waterState, Caption("격자"), _waterGrid, Caption("물 높이"), _waterLevel,
                         Row(_waterStart, stop, _waterPause, reset),
                         Caption("기울이기 X"), _tiltX, Caption("기울이기 Y"), _tiltY,
                         Caption("흔들기 세기"), _shakeAmp, Row(shake, unshake), _waterInfo);
        }

        void ShowWater(JsonObject w)
        {
            bool active = Analysis.Bool(w, "active");
            _waterState.Text = active ? $"켜짐 — 그릇 #{w["container"]}"
                             : Analysis.Bool(w, "starting") ? "켜는 중…" : "꺼짐 — 닫힌 솔리드(그릇)를 선택하고 시작";
            _waterStart.IsEnabled = !active;
            foreach (var c in _waterRunning) c.IsEnabled = active;
            _waterPause.Content = Analysis.IsFalse(w, "flowing") ? "재생" : "일시정지";
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
        FrameworkElement _loadBox, _heatBox, _runRow, _showRow, _facesCaption;
        TextBox _fx, _fy, _fz, _pressure, _temp, _flux, _convH, _convAmb;
        Button _simClose, _simRun, _simCancel, _simConverge, _simClear;
        TextBlock _simResult;
        int _face = -1;            // 고른 면
        string _facesKey, _showKind;
        bool _filling;             // 면 목록을 다시 채우는 동안 선택 이벤트 무시

        UIElement BuildSim()
        {
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
            // DropDownClosed — 사용자가 고른 때만(프로그램이 SelectedIndex 를 맞출 땐 오지 않는다)
            _simType.DropDownClosed += (s, e) => Call(Analysis.Sim, new { op = "set", type = Value(_simType) });
            _simMaterial.DropDownClosed += (s, e) => Call(Analysis.Sim, new { op = "set", material = Value(_simMaterial) });
            _simSize.DropDownClosed += (s, e) => Call(Analysis.Sim, new { op = "set", size = Value(_simSize) });

            _faces = new ListBox { Height = 130, Background = FieldBg, Foreground = TextMain, BorderThickness = new Thickness(0) };
            _faces.SelectionChanged += (s, e) =>
            {
                if (_filling) return;
                _face = _faces.SelectedItem is FaceItem f ? f.Index : -1;
                _loadBox.IsEnabled = _heatBox.IsEnabled = _face >= 0;
            };

            // 하중 조건 — 응력·진동·좌굴
            _fx = Number(0); _fy = Number(0); _fz = Number(-1000); _pressure = Number(1);
            _loadBox = Stack(
                Row(Btn("고정", () => Call(Analysis.Sim, new { op = "fix", face = _face })),
                    Btn("풀기", () => Call(Analysis.Sim, new { op = "free", face = _face }))),
                Caption("힘 N  (x · y · z)"),
                Row(_fx, _fy, _fz, Btn("걸기", () => Call(Analysis.Sim,
                    new { op = "force", face = _face, force = new[] { Val(_fx), Val(_fy), Val(_fz) } }))),
                Caption("압력 MPa"),
                Row(_pressure, Btn("걸기", () => Call(Analysis.Sim, new { op = "pressure", face = _face, value = Val(_pressure) }))));
            // 열 조건
            _temp = Number(80); _flux = Number(10); _convH = Number(10); _convAmb = Number(20);
            _heatBox = Stack(
                Caption("온도 °C"), Row(_temp, Btn("걸기", () => Call(Analysis.Sim, new { op = "temp", face = _face, value = Val(_temp) }))),
                Caption("열 W"), Row(_flux, Btn("걸기", () => Call(Analysis.Sim, new { op = "flux", face = _face, value = Val(_flux) }))),
                Caption("대류 h · 주변 °C"),
                Row(_convH, _convAmb, Btn("걸기", () => Call(Analysis.Sim,
                    new { op = "convect", face = _face, h = Val(_convH), ambient = Val(_convAmb) }))));

            _simRun = Btn("실행", () => Call(Analysis.Sim, new { op = "run" }));
            _simCancel = Btn("취소", () => Call(Analysis.Sim, new { op = "cancel" }));
            _simConverge = Btn("수렴 확인", () => Call(Analysis.Sim, new { op = "converge" }));
            _simClear = Btn("지우기", () => Call(Analysis.Sim, new { op = "clear" }));
            _runRow = Row(_simRun, _simCancel, _simConverge, _simClear);
            _simShow = Combo(Array.Empty<(string, string)>(), -1);
            _simShow.DropDownClosed += (s, e) => Call(Analysis.Sim, new { op = "set", show = Value(_simShow) });
            _showRow = Row(Caption("색"), _simShow);
            _simResult = Lbl("");
            _facesCaption = Caption("면 — 골라서 조건을 건다");

            return Stack(Row(open, _simClose), Caption("종류"), _simType, Caption("재료"), _simMaterial, Caption("요소"), _simSize,
                         _facesCaption, _faces, _loadBox, _heatBox, _runRow, _showRow, _simResult);
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
            _simClose.IsEnabled = isOpen;
            Show(_facesCaption, isOpen);
            Show(_faces, isOpen);
            Show(_runRow, isOpen);
            Show(_loadBox, isOpen && kind != "heat");
            Show(_heatBox, isOpen && kind == "heat");
            _loadBox.IsEnabled = _heatBox.IsEnabled = _face >= 0;

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

            _simRun.Content = busy ? "푸는 중…" : "실행";
            _simRun.IsEnabled = !busy;
            _simCancel.IsEnabled = busy;
            _simConverge.IsEnabled = !busy && result != null;
            _simClear.IsEnabled = !busy;

            // 결과 색 — 종류마다 고를 수 있는 것이 다르다
            Show(_showRow, result != null);
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
            if (!IsVisible) return;
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

        static Brush Hex(string hex) => (Brush)new BrushConverter().ConvertFromString(hex);

        static string Value(ComboBox box) => (box.SelectedItem as Choice)?.Value;

        static void Select(ComboBox box, string value)
        {
            if (value == null || box.IsDropDownOpen) return;   // 사용자가 고르는 중이면 건드리지 않는다
            for (int i = 0; i < box.Items.Count; i++)
                if (((Choice)box.Items[i]).Value == value && box.SelectedIndex != i) box.SelectedIndex = i;
        }

        static void Show(UIElement e, bool visible) => e.Visibility = visible ? Visibility.Visible : Visibility.Collapsed;

        static ComboBox Combo((string, string)[] items, int selected)
        {
            var box = new ComboBox { Margin = new Thickness(0, 0, 0, 2) };
            foreach (var (text, value) in items) box.Items.Add(new Choice(text, value));
            if (selected >= 0 && selected < items.Length) box.SelectedIndex = selected;
            return box;
        }

        static Slider Track(double lo, double hi, double value) =>
            new Slider { Minimum = lo, Maximum = hi, Value = value, Margin = new Thickness(0, 2, 0, 2) };

        static TextBox Number(double value) => new TextBox
        {
            Text = value.ToString(System.Globalization.CultureInfo.InvariantCulture), Width = 62, Margin = new Thickness(0, 0, 4, 0),
            Background = FieldBg, Foreground = TextMain, BorderBrush = TextDim, VerticalContentAlignment = VerticalAlignment.Center,
        };

        static double Val(TextBox box) =>
            double.TryParse(box.Text, System.Globalization.NumberStyles.Float, System.Globalization.CultureInfo.InvariantCulture, out double v) ? v : 0;

        static Button Btn(string text, Action onClick)
        {
            var b = new Button { Content = text, Margin = new Thickness(0, 2, 4, 2), Focusable = false };
            b.SetResourceReference(StyleProperty, "ToolBtn");   // MainWindow.xaml 의 다크 버튼
            b.Click += (s, e) => onClick();
            return b;
        }

        static CheckBox Check(string text, Action<bool> onChanged)
        {
            var c = new CheckBox { Content = text, Foreground = TextMain, Margin = new Thickness(0, 4, 0, 0) };
            c.Checked += (s, e) => onChanged(true);
            c.Unchecked += (s, e) => onChanged(false);
            return c;
        }

        static TextBlock Lbl(string text) => new TextBlock
        {
            Text = text, Foreground = TextMain, TextWrapping = TextWrapping.Wrap, Margin = new Thickness(0, 4, 0, 2),
        };

        static TextBlock Caption(string text) => new TextBlock
        {
            Text = text, Foreground = TextDim, Margin = new Thickness(0, 8, 0, 2),
        };

        static StackPanel Row(params UIElement[] items)
        {
            var row = new StackPanel { Orientation = Orientation.Horizontal, Margin = new Thickness(0, 2, 0, 2) };
            foreach (var x in items) row.Children.Add(x);
            return row;
        }

        static StackPanel Stack(params UIElement[] items)
        {
            var box = new StackPanel();
            foreach (var x in items) box.Children.Add(x);
            return box;
        }

        static ScrollViewer Scroll(UIElement content) => new ScrollViewer
        {
            Content = content, VerticalScrollBarVisibility = ScrollBarVisibility.Auto,
            HorizontalScrollBarVisibility = ScrollBarVisibility.Disabled,
        };
    }
}
