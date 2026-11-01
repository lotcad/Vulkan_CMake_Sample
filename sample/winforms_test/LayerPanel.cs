using System;
using System.Collections.Generic;
using System.Drawing;
using System.Globalization;
using System.Linq;
using System.Text.Json.Nodes;
using System.Windows.Forms;

namespace LotCadWinForms
{
    // 도면 패널 — 도면층 · 선종류 · 블록(외부 참조). 오른쪽에 붙는다(MainForm 의 메뉴 "도면" 이 연다).
    // 엔진의 도면층·선종류·블록 창(ImGui)은 호스트 창 안에서 그려지지 않아, 같은 일을 C API 로 여기서 한다.
    //
    //   도면층: CAD_GetLayersJson 한 번으로 표를 읽고, 고른 층에 CAD_SetLayer*·CAD_RenameLayer, 객체는 CAD_AssignSelectedToLayer
    //   선종류: 선택한 객체에 CAD_SetObjectLinetype(도면층 따름 = CAD_LINETYPE_BYLAYER), 축척, 무늬로 새 선종류
    //   블록:   CAD_GetBlocksJson 으로 목록, 만들기·편집은 명령(block · bedit 이름 · bclose), 외부 참조는 CAD_Xref*
    // 장면 번호(CAD_GetSceneRevision)가 바뀔 때만 목록을 다시 읽는다 — 0.5초마다 숫자 하나만 묻는다.
    //
    // ⚠️ 지금 C API 에는 도면층 지우기·"현재 도면층" 정하기와, 있는 블록을 한 번 더 놓는 함수가 없다.
    //    새로 그린 객체는 '선택한 객체를 이 도면층으로' 로 옮기고, 블록은 블록 참조를 복사해 늘린다.
    public sealed class LayerPanel : SidePanel
    {
        static readonly (string Name, double R, double G, double B)[] Colors =
        {
            ("흰색", 1, 1, 1), ("빨강", 1, 0, 0), ("노랑", 1, 1, 0), ("초록", 0, 1, 0),
            ("하늘", 0, 1, 1), ("파랑", 0, 0, 1), ("자홍", 1, 0, 1), ("회색", 0.5, 0.5, 0.5),
        };

        ulong _revision = ulong.MaxValue;   // 마지막으로 읽은 장면 번호 — 처음엔 꼭 읽게 없는 값
        List<(uint Id, string Name)> _linetypes = new();

        // 패널은 엔진보다 먼저 만들어진다(MainForm 필드) — 엔진에 묻는 것은 처음 보일 때(Poll)부터
        public LayerPanel() => Init(new[] { "도면층", "선종류", "블록" }, BuildLayers(), BuildLinetypes(), BuildBlocks());

        protected override void Poll()
        {
            if (_linetypes.Count == 0) FillLinetypes();   // 선종류 표 — 엔진이 준비된 뒤 한 번
            if (CadApi.CAD_GetSceneRevision(out ulong rev) != 0 || rev == _revision) return;
            _revision = rev;
            FillLayers();
            FillBlocks();
        }

        static List<(uint, string)> ReadLinetypes()
        {
            var list = new List<(uint, string)>();
            int n = CadApi.CAD_GetLinetypeIds(null, 0);
            if (n <= 0) return list;
            var ids = new uint[n];
            CadApi.CAD_GetLinetypeIds(ids, (uint)n);
            foreach (uint id in ids)
                list.Add((id, CadApi.ReadText((b, c) => CadApi.CAD_GetLinetypeName(id, b, c))));
            return list;
        }

        // ── 도면층 ──
        ListBox _layers;
        ComboBox _layerColor, _layerLinetype;
        TextBox _layerName, _newLayer;
        JsonArray _layerRows = new();
        bool _filling;   // 목록을 다시 채우는 동안 선택 이벤트 무시

        JsonNode Current => _layers.SelectedIndex >= 0 && _layers.SelectedIndex < _layerRows.Count ? _layerRows[_layers.SelectedIndex] : null;
        uint CurrentId => (uint)(Analysis.Number(Current?["id"]) ?? 0);

        Control BuildLayers()
        {
            var page = Page();
            _layers = List(9);
            _layers.SelectedIndexChanged += (s, e) => { if (!_filling) ShowCurrentLayer(); };
            _layerColor = Combo(Colors.Select(c => c.Name).Append("(다른 색)").ToArray());
            _layerColor.SelectionChangeCommitted += (s, e) =>
            {
                int i = _layerColor.SelectedIndex;
                if (i >= 0 && i < Colors.Length) Report("색 바꿈", CadApi.CAD_SetLayerColor(CurrentId, new CadApi.CadColor(Colors[i].R, Colors[i].G, Colors[i].B)));
            };
            _layerLinetype = Combo(Array.Empty<string>());   // 항목은 FillLinetypes
            _layerLinetype.SelectionChangeCommitted += (s, e) =>
            {
                int i = _layerLinetype.SelectedIndex;
                if (i >= 0) Report("선종류 바꿈", CadApi.CAD_SetLayerLinetype(CurrentId, _linetypes[i].Id));
            };
            _layerName = TextField(200);
            _newLayer = TextField(200, "새 도면층");

            Add(page, _layers,
                Row(Btn("보이기/숨기기", () => Report("보이기 바꿈", CadApi.CAD_SetLayerVisible(CurrentId, !Analysis.Bool(Current, "visible")))),
                    Btn("잠금/풀기", () => Report("잠금 바꿈", CadApi.CAD_SetLayerLocked(CurrentId, !Analysis.Bool(Current, "locked"))))),
                Caption("색 (객체 색이 '도면층 따름' 일 때)"), _layerColor,
                Caption("선종류 (선·폴리선·원·호에 보인다)"), _layerLinetype,
                Caption("이름"), Row(_layerName, Btn("바꾸기", () => Report("이름 바꿈", CadApi.CAD_RenameLayer(CurrentId, CadApi.Utf8(_layerName.Text))))),
                Caption("객체"),
                Btn("선택한 객체를 이 도면층으로", () =>
                {
                    int r = CadApi.CAD_AssignSelectedToLayer(CurrentId, out uint changed);
                    Message = r != 0 ? "옮기기 실패: " + CadApi.LastError()
                            : changed == 0 ? "옮긴 객체 없음 — 3D 뷰에서 먼저 선택하세요" : $"객체 {changed}개를 옮겼습니다";
                }),
                Btn("선택한 객체 색 = 도면층 따름", () =>
                {
                    int r = CadApi.CAD_SetSelectedColorByLayer(true, out uint changed);
                    Message = r == 0 ? $"객체 {changed}개가 도면층 색을 따릅니다" : "실패: " + CadApi.LastError();
                }),
                Caption("새 도면층"),
                Row(_newLayer, Btn("만들기", () =>
                {
                    int r = CadApi.CAD_CreateLayer(CadApi.Utf8(_newLayer.Text), out _);   // 같은 이름 CAD_E_DUPLICATE
                    Message = r == 0 ? "도면층을 만들었습니다 — 목록에서 골라 색·선종류를 정하세요" : "만들기 실패: " + CadApi.LastError();
                })),
                Note("지우기·현재 도면층 정하기는 C API 에 아직 없다. 새로 그린 객체는 위 '이 도면층으로' 로 옮긴다."));
            return page;
        }

        void FillLayers()
        {
            uint keep = CurrentId;
            var root = JsonNode.Parse(CadApi.ReadText(CadApi.CAD_GetLayersJson) is { Length: > 0 } j ? j : "{}");
            _layerRows = root?["layers"] as JsonArray ?? new JsonArray();
            _filling = true;
            _layers.Items.Clear();
            int select = 0;
            for (int i = 0; i < _layerRows.Count; i++)
            {
                var l = _layerRows[i];
                if ((uint)(Analysis.Number(l?["id"]) ?? 0) == keep) select = i;
                int sel = (int)(Analysis.Number(l?["selectedCount"]) ?? 0);
                _layers.Items.Add(Analysis.Str(l, "name") +
                                  (Analysis.Bool(l, "visible") ? "" : "  [숨김]") + (Analysis.Bool(l, "locked") ? "  [잠금]" : "") +
                                  $"  · {Analysis.Str(l, "linetype")}  · 객체 {Analysis.Num(l?["objectCount"], "0")}" +
                                  (sel > 0 ? $" (선택 {sel})" : ""));
            }
            if (_layers.Items.Count > 0) _layers.SelectedIndex = select;
            _filling = false;
            ShowCurrentLayer();
        }

        // 고른 층의 색·선종류·이름을 아래 칸에 맞춘다
        void ShowCurrentLayer()
        {
            var l = Current;
            if (l == null) return;
            var rgb = l["color"] as JsonArray;
            int color = Array.FindIndex(Colors, c => rgb != null && rgb.Count == 3 &&
                Math.Abs((Analysis.Number(rgb[0]) ?? -1) - c.R) < 0.02 && Math.Abs((Analysis.Number(rgb[1]) ?? -1) - c.G) < 0.02 &&
                Math.Abs((Analysis.Number(rgb[2]) ?? -1) - c.B) < 0.02);
            _layerColor.SelectedIndex = color >= 0 ? color : Colors.Length;
            int lt = _linetypes.FindIndex(t => t.Id == (uint)(Analysis.Number(l["linetypeId"]) ?? 0));
            if (lt < _layerLinetype.Items.Count) _layerLinetype.SelectedIndex = lt;
            _layerName.Text = Analysis.Str(l, "name");
        }

        // ── 선종류 ──
        ListBox _linetypeList;
        NumericUpDown _objectScale, _globalScale;
        TextBox _ltName, _ltPattern;

        Control BuildLinetypes()
        {
            var page = Page();
            _linetypeList = List(9);   // 항목은 FillLinetypes
            _objectScale = NumberBox(1, 3);
            _globalScale = NumberBox(1, 3);
            _ltName = TextField(280, "내 파선");
            _ltPattern = TextField(280, "0.5, -0.25, 0, -0.25");

            Add(page, Caption("선택한 객체에"), _linetypeList,
                Btn("선택한 객체에 적용", () =>
                {
                    var ids = Analysis.SelectedIds();
                    if (ids.Length == 0) { Message = "먼저 3D 뷰에서 선·폴리선·원·호를 선택하세요"; return; }
                    int i = _linetypeList.SelectedIndex;
                    uint lt = i <= 0 ? CadApi.CAD_LINETYPE_BYLAYER : _linetypes[i - 1].Id;
                    // 하나라도 없거나 잠긴 층이면 아무것도 안 바꾼다(되돌리기 1)
                    int r = CadApi.CAD_SetObjectLinetype(ids, (uint)ids.Length, lt, out uint changed);
                    Message = r == 0 ? $"객체 {changed}개의 선종류를 바꿨습니다 (메시·문자·치수엔 안 보임)" : "적용 실패: " + CadApi.LastError();
                }),
                Caption("축척 — 선택한 객체 · 전체(LTSCALE)"),
                Row(_objectScale, Btn("객체에", () =>
                {
                    int done = Analysis.SelectedIds().Count(id => CadApi.CAD_SetObjectLinetypeScale(id, (double)_objectScale.Value) == 0);
                    Message = done > 0 ? $"객체 {done}개의 축척을 바꿨습니다" : "바꾼 객체 없음 — 선택·값(> 0)을 확인하세요";
                }), _globalScale, Btn("전체에", () =>
                    Message = CadApi.CAD_SetLinetypeScale((double)_globalScale.Value) == 0 ? "전체 선종류 축척을 바꿨습니다" : "실패: " + CadApi.LastError())),
                Caption("새 선종류 — 이름"), _ltName,
                Caption("무늬 (쉼표로, 양수 선 · 음수 빈칸 · 0 점)"), _ltPattern,
                Btn("만들기", () =>
                {
                    var pattern = _ltPattern.Text.Split(',', StringSplitOptions.RemoveEmptyEntries)
                        .Select(s => double.TryParse(s.Trim(), NumberStyles.Float, CultureInfo.InvariantCulture, out double v) ? v : double.NaN)
                        .Where(v => !double.IsNaN(v)).ToArray();
                    int r = CadApi.CAD_CreateLinetype(CadApi.Utf8(_ltName.Text), pattern, (uint)pattern.Length, null, out uint id);
                    Message = r == 0 ? $"선종류 {id} 번을 만들었습니다" : "만들기 실패: " + CadApi.LastError();
                    if (r == 0) FillLinetypes();   // 목록에 바로 보이게
                }));
            return page;
        }

        // 선종류 표 → 선종류 목록(맨 위 = 도면층 따름)과 도면층 페이지의 선종류 칸
        void FillLinetypes()
        {
            _linetypes = ReadLinetypes();
            int keep = _linetypeList.SelectedIndex;
            _linetypeList.Items.Clear();
            _linetypeList.Items.Add("도면층 따름 (ByLayer)");
            _layerLinetype.Items.Clear();
            foreach (var (id, name) in _linetypes)
            {
                var pattern = new double[8];
                int n = CadApi.CAD_GetLinetypePattern(id, pattern, 8);
                _linetypeList.Items.Add(n > 0 ? $"{name}   {string.Join(", ", pattern.Take(n).Select(v => v.ToString(CultureInfo.InvariantCulture)))}" : name);
                _layerLinetype.Items.Add(name);
            }
            _linetypeList.SelectedIndex = keep > 0 && keep < _linetypeList.Items.Count ? keep : Math.Min(1, _linetypeList.Items.Count - 1);   // 1 = Continuous
            ShowCurrentLayer();
        }

        // ── 블록 · 외부 참조 ──
        ListBox _blocks;
        JsonArray _blockRows = new();

        string BlockName => _blocks.SelectedIndex >= 0 && _blocks.SelectedIndex < _blockRows.Count ? Analysis.Str(_blockRows[_blocks.SelectedIndex], "name") : null;

        Control BuildBlocks()
        {
            var page = Page();
            _blocks = List(8);
            // 고른 블록이 있어야 하는 동작 — 없으면 안내만
            Action<string, Func<byte[], int>> xref = (what, fn) =>
            {
                if (BlockName is not string name) { Message = "먼저 목록에서 블록을 고르세요"; return; }
                Report(what, fn(CadApi.Utf8(name)));
            };
            Add(page, Caption("블록 정의"), _blocks,
                Caption("만들기 · 편집"),
                Btn("선택한 객체로 새 블록", () =>
                {
                    if (Analysis.SelectedIds().Length == 0) { Message = "먼저 3D 뷰에서 블록으로 묶을 객체를 선택하세요"; return; }
                    CadApi.StartCommand("block");   // 이름 → 기준점(Enter = 고른 것의 왼쪽 아래)
                    Message = "3D 뷰를 누르고 블록 이름을 친 뒤 Enter, 이어서 기준점을 찍으세요";
                }),
                Btn("고른 블록 편집 (블록 편집 탭)", () =>
                {
                    if (BlockName is not string name) { Message = "먼저 목록에서 블록을 고르세요"; return; }
                    // bedit 은 뒤의 글 전체를 이름으로 받는다 — 빈칸이 든 이름도 그대로
                    Message = CadApi.StartCommand("bedit " + name) == 0 ? "블록 편집 탭을 열었습니다 — 고친 뒤 '저장하고 닫기'" : "편집 실패: " + CadApi.LastError();
                }),
                Row(Btn("저장하고 닫기", () => { CadApi.StartCommand("bclose save"); Message = "블록을 저장하고 편집 탭을 닫았습니다"; }),
                    Btn("버리고 닫기", () => { CadApi.StartCommand("bclose discard"); Message = "고친 것을 버리고 편집 탭을 닫았습니다"; }),
                    Btn("기준점", () => { CadApi.StartCommand("bbase"); Message = "3D 뷰에서 새 기준점을 클릭하세요 (블록 편집 탭에서만)"; })),
                Note("새 블록은 엔진이 이름·기준점을 묻는다(3D 뷰에서 치고 Enter). 같은 블록을 더 놓으려면 블록 참조를 선택해 복사한다."),
                Caption("외부 참조 (고른 블록이 외부 참조일 때)"),
                Row(Btn("다시 읽기", () => xref("다시 읽음", CadApi.CAD_XrefReload)),
                    Btn("결합", () => xref("도면에 결합함", CadApi.CAD_XrefBind)),
                    Btn("떼기", () => xref("외부 참조를 뗌", CadApi.CAD_XrefDetach))),
                Row(Btn("경로 = 상대", () => xref("상대 경로로", n => CadApi.CAD_XrefSetPath(n, CadApi.Utf8("relative")))),
                    Btn("경로 = 절대", () => xref("절대 경로로", n => CadApi.CAD_XrefSetPath(n, CadApi.Utf8("absolute"))))));
            return page;
        }

        void FillBlocks()
        {
            string keep = BlockName;
            var root = JsonNode.Parse(CadApi.ReadText(CadApi.CAD_GetBlocksJson) is { Length: > 0 } j ? j : "{}");
            _blockRows = root?["blocks"] as JsonArray ?? new JsonArray();
            _blocks.Items.Clear();
            for (int i = 0; i < _blockRows.Count; i++)
            {
                var b = _blockRows[i];
                _blocks.Items.Add($"{Analysis.Str(b, "name")}  · 객체 {Analysis.Num(b?["objects"], "0")} · 참조 {Analysis.Num(b?["references"], "0")}" +
                                  (b?["xref"] == null ? "" : Analysis.IsFalse(b, "xrefFound") ? "  [외부 참조 — 파일 없음]" : "  [외부 참조]"));
                if (Analysis.Str(b, "name") == keep) _blocks.SelectedIndex = i;
            }
        }

        void Report(string what, int status) => Message = status == 0 ? what : $"{what} 실패: {CadApi.LastError()}";
    }

    // 오른쪽 패널 공용 틀 — 위에 페이지 단추 · ✕, 가운데 페이지, 아래 상태 글. 보이는 동안 0.5초마다 Poll.
    // LayerPanel · ToolsPanel 이 쓴다(AnalysisPanel 과 같은 모양·색).
    public abstract class SidePanel : UserControl
    {
        protected static readonly Color Bg = ColorTranslator.FromHtml("#1E1F22");
        protected static readonly Color FieldBg = ColorTranslator.FromHtml("#2B2D31");
        protected static readonly Color Accent = ColorTranslator.FromHtml("#2D6CDF");
        protected static readonly Color TextMain = ColorTranslator.FromHtml("#E6E6E6");
        protected static readonly Color TextDim = ColorTranslator.FromHtml("#9AA0AA");

        readonly Timer _timer = new Timer { Interval = 500 };
        readonly Label _message = new Label { AutoSize = false, Dock = DockStyle.Bottom, Height = 64, ForeColor = TextDim };
        readonly Panel _pages = new Panel { Dock = DockStyle.Fill };
        Button[] _pageButtons = Array.Empty<Button>();
        Control[] _pageControls = Array.Empty<Control>();

        protected string Message { set => _message.Text = value; }

        protected SidePanel()
        {
            Width = 330;
            Dock = DockStyle.Right;
            Visible = false;
            BackColor = Bg;
            ForeColor = TextMain;
            Padding = new Padding(8, 6, 8, 6);
        }

        protected void Init(string[] titles, params Control[] pages)
        {
            _pageControls = pages;
            foreach (var p in pages) { p.Dock = DockStyle.Fill; p.Visible = false; _pages.Controls.Add(p); }
            var header = new FlowLayoutPanel { Dock = DockStyle.Top, Height = 34, WrapContents = false };
            _pageButtons = new Button[titles.Length];
            for (int i = 0; i < titles.Length; i++)
            {
                int page = i;
                _pageButtons[i] = Btn(titles[i], () => ShowPage(page));
                header.Controls.Add(_pageButtons[i]);
            }
            header.Controls.Add(Btn("✕", () => Visible = false));
            Controls.Add(_pages);   // 채움을 먼저, 위·아래를 나중에(도킹 순서)
            Controls.Add(_message);
            Controls.Add(header);
            _timer.Tick += (s, e) => Poll();
            VisibleChanged += (s, e) => { _timer.Enabled = Visible; if (Visible) Poll(); };
        }

        public void ShowPage(int page)
        {
            _message.Text = "";   // 앞 페이지의 안내는 지운다
            for (int i = 0; i < _pageControls.Length; i++)
            {
                _pageControls[i].Visible = i == page;
                _pageButtons[i].BackColor = i == page ? Accent : FieldBg;
            }
            Visible = true;
        }

        /// <summary>창을 닫을 때 엔진을 헐기 **전에** — 헐린 엔진에 묻지 않게.</summary>
        public void Shutdown() => _timer.Stop();

        protected virtual void Poll() { }

        // ── 컨트롤 도우미 (다크) ──
        protected static Button Btn(string text, Action onClick)
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

        protected static CheckBox Check(string text, Action<bool> onChanged)
        {
            var c = new CheckBox { Text = text, AutoSize = true, ForeColor = TextMain, Margin = new Padding(0, 4, 0, 0) };
            c.CheckedChanged += (s, e) => onChanged(c.Checked);
            return c;
        }

        protected static Label Caption(string text) => new Label
        {
            Text = text, AutoSize = true, ForeColor = TextDim, Margin = new Padding(0, 8, 0, 2),
        };

        protected static Label Note(string text) => new Label
        {
            Text = text, AutoSize = true, MaximumSize = new Size(280, 0), ForeColor = TextDim, Margin = new Padding(0, 6, 0, 2),
        };

        protected static ComboBox Combo(string[] items)
        {
            var box = new ComboBox { DropDownStyle = ComboBoxStyle.DropDownList, Width = 280, BackColor = FieldBg, ForeColor = TextMain,
                                     FlatStyle = FlatStyle.Flat };
            box.Items.AddRange(items);
            return box;
        }

        protected static ListBox List(int lines) => new ListBox
        {
            Width = 280, Height = lines * 17 + 4, BackColor = FieldBg, ForeColor = TextMain, BorderStyle = BorderStyle.None,
            HorizontalScrollbar = true,
        };

        protected static TextBox TextField(int width, string text = "") => new TextBox
        {
            Width = width, Text = text, BackColor = FieldBg, ForeColor = TextMain, BorderStyle = BorderStyle.FixedSingle,
            Margin = new Padding(0, 4, 4, 2),
        };

        protected static NumericUpDown NumberBox(decimal value, int decimals) => new NumericUpDown
        {
            Minimum = -1000000, Maximum = 1000000, DecimalPlaces = decimals, Value = value, Width = 70,
            BackColor = FieldBg, ForeColor = TextMain, BorderStyle = BorderStyle.FixedSingle, Margin = new Padding(0, 4, 4, 2),
        };

        protected static FlowLayoutPanel Row(params Control[] items)
        {
            var row = new FlowLayoutPanel { AutoSize = true, WrapContents = false, Margin = new Padding(0, 2, 0, 2) };
            row.Controls.AddRange(items);
            return row;
        }

        protected static FlowLayoutPanel Page() => new FlowLayoutPanel
        {
            FlowDirection = FlowDirection.TopDown, WrapContents = false, AutoScroll = true, Padding = new Padding(0, 4, 0, 4),
        };

        protected static void Add(Control page, params Control[] items) => page.Controls.AddRange(items);
    }
}
