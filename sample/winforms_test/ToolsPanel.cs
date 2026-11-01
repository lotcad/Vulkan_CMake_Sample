using System;
using System.Linq;
using System.Text.Json;
using System.Text.Json.Nodes;
using System.Windows.Forms;

namespace LotCadWinForms
{
    // 도구 패널 — 분해도 · 메시 수리. 오른쪽에 붙는다(MainForm 의 메뉴 "도구" 가 연다). 틀은 LayerPanel.cs 의 SidePanel.
    //
    //   분해도:   CAD_ExplodeView({"op": …}) → 결과 JSON(ok · error · t · steps · parts · animating …). 2회 호출 규약(CallOnce).
    //             대상 = 선택한 솔리드, 없으면 보이는 솔리드 전부. 분해 막대·풍선·부품표는 엔진이 3D 뷰에 그린다.
    //   메시 수리: CAD_CheckMesh · CAD_RepairMeshes · Smooth · Decimate · Stitch · Thicken · Remesh — 선택한 메시에(B-Rep 솔리드는 아님).
    //             반환 = 바꾼 메시 수(0 = 고칠 것 없음), 음수 = 이유 코드. 여럿이어도 되돌리기 1.
    public sealed class ToolsPanel : SidePanel
    {
        public ToolsPanel() => Init(new[] { "분해도", "메시 수리" }, BuildExplode(), BuildMesh());

        static JsonObject Explode(object args)
        {
            string result = CadApi.CallOnce(CadApi.CAD_ExplodeView, JsonSerializer.Serialize(args));
            if (result == null) return new JsonObject { ["ok"] = false, ["error"] = CadApi.LastError() };
            return JsonNode.Parse(result) as JsonObject ?? new JsonObject();
        }

        // ── 분해도 ──
        TrackBar _amount;
        Label _explodeState;

        Control BuildExplode()
        {
            var page = Page();
            // 선택이 있으면 그 id 들만 — 없으면 ids 를 빼서 엔진이 보이는 솔리드 전부를 고르게
            Func<string, object> targets = op =>
            {
                var ids = Analysis.SelectedIds();
                return ids.Length > 0 ? new { op, ids } : (object)new { op };
            };
            Action<string, object> run = (what, args) =>
            {
                var r = Explode(args);
                Message = Analysis.Bool(r, "ok") ? what : $"{what} 실패: {Analysis.Str(r, "error")}";
            };
            _amount = new TrackBar { Minimum = 0, Maximum = 100, TickStyle = TickStyle.None, Width = 280, AutoSize = false, Height = 28, BackColor = Bg };
            _amount.Scroll += (s, e) => run("분해 정도", new { op = "amount", t = _amount.Value / 100.0 });
            _explodeState = new Label { AutoSize = true, ForeColor = TextMain, Margin = new Padding(0, 8, 0, 2) };

            Add(page, Caption("방향·순서"),
                Btn("자동 순서 — 걸리지 않고 빠지는 방향", () =>
                {
                    var r = Explode(targets("solve"));
                    Message = Analysis.Bool(r, "ok")
                        ? $"단계 {Analysis.Num(r["solved_steps"], "0")}개로 풀었습니다" +
                          ((Analysis.Number(r["unsolved"]) ?? 0) > 0 ? $" (못 뺀 부품 {Analysis.Num(r["unsolved"], "0")}개)" : "")
                        : "자동 순서 실패: " + Analysis.Str(r, "error");
                }),
                Row(Btn("방사형", () => run("방사형으로 펼침", targets("auto"))),
                    Btn("지우기", () => run("분해 방향을 지움", targets("clear")))),
                Caption("분해 정도 (0 조립 ~ 100 다 펼침)"), _amount,
                Row(Btn("펼치기 재생", () => run("펼치는 중", new { op = "play", seconds = 2 })),
                    Btn("조립 재생", () => run("조립하는 중", new { op = "back", seconds = 2 }))),
                Caption("설명"),
                Check("품번 풍선", on => run(on ? "풍선 켬" : "풍선 끔", new { op = "balloons", show = on })),
                Check("부품표", on => run(on ? "부품표 켬" : "부품표 끔", new { op = "bom", show = on })),
                Btn("부품표 CSV 저장...", () =>
                {
                    using var dlg = new SaveFileDialog { Filter = "CSV (*.csv)|*.csv", DefaultExt = "csv" };
                    if (dlg.ShowDialog(this) == DialogResult.OK) run("부품표를 저장했습니다", new { op = "bom", path = dlg.FileName });
                }),
                _explodeState);
            return page;
        }

        protected override void Poll()
        {
            if (!Visible) return;
            var s = Explode(new { op = "status" });
            double t = Analysis.Number(s["t"]) ?? 0;
            if (Analysis.Bool(s, "animating")) _amount.Value = (int)Math.Round(Math.Clamp(t, 0, 1) * 100);   // 재생 중엔 막대가 따라간다
            _explodeState.Text = $"분해 {t * 100:0}% · 단계 {Analysis.Num(s["steps"], "0")} · 부품 {(s["parts"] as JsonArray)?.Count ?? 0}" +
                                 (Analysis.Bool(s, "animating") ? " · 재생 중" : "");
        }

        // ── 메시 수리 ──
        CheckBox _noFill, _flatFill;

        Control BuildMesh()
        {
            var page = Page();
            _noFill = Check("구멍은 메우지 않음", _ => { });
            _flatFill = Check("구멍을 평평하게 (기본 = 둥글게)", _ => { });

            Add(page, Caption("검사 · 수리"),
                Btn("검사", () =>
                {
                    var ids = NeedMeshes();
                    if (ids.Length == 0) return;
                    Message = string.Join("\n", ids.Take(4).Select(id =>
                    {
                        var info = new CadApi.MeshCheckInfo { Size = (uint)System.Runtime.InteropServices.Marshal.SizeOf<CadApi.MeshCheckInfo>() };
                        if (CadApi.CAD_CheckMesh(id, ref info) != 0) return $"#{id}: {CadApi.LastError()}";
                        return $"#{id}: 삼각형 {info.Triangles} · 구멍 {info.Holes} · 열린 모서리 {info.OpenEdges} · 뒤집힘 {info.FlippedEdges} — " +
                               (info.Ok ? "괜찮음" : info.Closed ? "닫힘(결함 있음)" : "열림");
                    }));
                }),
                _noFill, _flatFill,
                // 수리 = 같은 자리 정점 붙이기 → 퇴화·중복 제거 → 방향 통일 → 구멍 메움. 멀쩡한 메시는 건드리지 않는다
                Btn("수리", () =>
                {
                    var ids = NeedMeshes();
                    if (ids.Length == 0) return;
                    var opt = new CadApi.MeshRepairOptions
                    {
                        Size = (uint)System.Runtime.InteropServices.Marshal.SizeOf<CadApi.MeshRepairOptions>(),
                        NoFill = _noFill.Checked, FlatFill = _flatFill.Checked,
                    };
                    Message = MeshResult("수리", CadApi.CAD_RepairMeshes(ids, (uint)ids.Length, ref opt));
                }),
                Caption("다듬기"),
                MeshRow("매끈하게 — 반복 1~500", 5, 0, (ids, v) => CadApi.CAD_SmoothMeshes(ids, (uint)ids.Length, (int)v)),
                MeshRow("삼각형 줄이기 — 남길 비율 0~1", 0.5m, 2, (ids, v) => CadApi.CAD_DecimateMeshes(ids, (uint)ids.Length, v)),
                MeshRow("틈 꿰매기 — 허용치 mm (0 = 자동)", 0, 3, (ids, v) => CadApi.CAD_StitchMeshes(ids, (uint)ids.Length, v)),
                MeshRow("두께 주기 — 열린 메시 → 솔리드, mm", 2, 2, (ids, v) => CadApi.CAD_ThickenMeshes(ids, (uint)ids.Length, v)),
                MeshRow("다시 나누기 — 모서리 mm (0 = 지금 평균)", 0, 2, (ids, v) => CadApi.CAD_RemeshMeshes(ids, (uint)ids.Length, v)));
            return page;
        }

        // 이름 · [값] [적용] 한 묶음
        Control MeshRow(string caption, decimal value, int decimals, Func<uint[], double, int> apply)
        {
            var number = NumberBox(value, decimals);
            var box = new FlowLayoutPanel { AutoSize = true, FlowDirection = FlowDirection.TopDown, WrapContents = false, Margin = new Padding(0) };
            box.Controls.Add(Caption(caption));
            box.Controls.Add(Row(number, Btn("적용", () =>
            {
                var ids = NeedMeshes();
                if (ids.Length > 0) Message = MeshResult(caption.Split(' ')[0], apply(ids, (double)number.Value));
            })));
            return box;
        }

        uint[] NeedMeshes()
        {
            var ids = Analysis.SelectedIds();
            if (ids.Length == 0) Message = "먼저 3D 뷰에서 메시를 선택하세요";
            return ids;
        }

        static string MeshResult(string what, int changed) =>
            changed < 0 ? $"{what} 실패: {CadApi.LastError()}"
            : changed == 0 ? $"{what}: 바꾼 메시 없음 (이미 괜찮거나 해당 없음)"
            : $"{what}: 메시 {changed}개를 바꿨습니다";
    }
}
