using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text.Json;
using System.Text.Json.Nodes;

namespace LotCadWpf
{
    // 해석 API 를 부르고 결과 JSON 을 읽는 쪽 — 화면은 AnalysisPanel.cs.
    //
    // 세 API(CAD_WindTunnel · CAD_Water · CAD_StructuralAnalysis)는 {"op": …} JSON 을 받아 결과 JSON 을 준다.
    // op·인자는 헤더 LotCAD_API.h 의 해석 주석, MCP 도구 wind_tunnel · water · structural_analysis 와 같다.
    //   바람 터널: status · start {ids, grid, wind} · stop · reset · pause · play · view {field, plane, at, smoke, surface} · wind {value}
    //   물:        status · start {id, level, grid} · stop · reset · pause · play · tilt {x, y} · shake {amplitude}
    //   구조 해석: status(faces) · open {id} · close · clear · run · cancel · converge · set {type, material, size, show}
    //             fix|free {face} · force {face, force[3]} · pressure {face, value} · temp|flux {face, value} · convect {face, h, ambient}
    static class Analysis
    {
        public const string Wind = "wind", Water = "water", Sim = "sim";

        /// <summary>해석 API 한 번 — 결과 JSON. 실패면 {"ok":false,"error":…}.</summary>
        public static JsonObject Call(string which, object args)
        {
            string json = JsonSerializer.Serialize(args);
            CadApi.JsonFn fn = which == Wind ? CadApi.CAD_WindTunnel
                             : which == Water ? CadApi.CAD_Water
                             : (CadApi.JsonFn)CadApi.CAD_StructuralAnalysis;
            string result = CadApi.CallOnce(fn, json);
            if (result == null)
                return new JsonObject { ["ok"] = false, ["error"] = CadApi.LastError() is { Length: > 0 } e ? e : "실패" };
            return JsonNode.Parse(result) as JsonObject ?? new JsonObject();
        }

        public static uint[] SelectedIds()
        {
            var ids = new List<uint>();
            uint n = CadApi.CAD_GetSelectedCount();
            for (uint i = 0; i < n; i++)
                if (CadApi.CAD_GetSelectedObjectId(i, out uint id) && id != 0) ids.Add(id);
            return ids.ToArray();
        }

        // ── JSON 읽기 도우미 — 엔진은 아직 없는 값을 null 로 준다(켠 직후의 항력 계수 등) ──
        public static bool Bool(JsonNode n, string key) => n?[key] is JsonValue v && v.TryGetValue(out bool b) && b;
        public static bool IsFalse(JsonNode n, string key) => n?[key] is JsonValue v && v.TryGetValue(out bool b) && !b;
        public static string Str(JsonNode n, string key) => n?[key] is JsonValue v && v.TryGetValue(out string s) ? s : null;

        public static double? Number(JsonNode n)
        {
            if (n is JsonValue v && v.TryGetValue(out double d)) return d;
            return null;
        }

        /// <summary>숫자 → 글. null 이면 "-".</summary>
        public static string Num(JsonNode n, string format) =>
            Number(n) is double d ? d.ToString(format, CultureInfo.InvariantCulture) : "-";

        public static string Cells(JsonNode n) =>
            n is JsonArray a && a.Count > 0 ? string.Join(" × ", a.Select(x => x?.ToString())) : null;

        /// <summary>법선 → "+Z" 처럼(축에 거의 맞으면), 아니면 숫자 셋.</summary>
        public static string AxisName(JsonNode normal)
        {
            if (normal is not JsonArray a || a.Count < 3) return "";
            for (int i = 0; i < 3; i++)
            {
                double c = Number(a[i]) ?? 0;
                if (Math.Abs(c) > 0.98) return (c > 0 ? "+" : "−") + "XYZ"[i];
            }
            return "(" + string.Join(", ", a.Select(x => Num(x, "0.00"))) + ")";
        }

        /// <summary>구조 해석 결과 → 여러 줄 글.</summary>
        public static string ResultText(JsonNode r)
        {
            if (r is not JsonObject) return "";
            switch (Str(r, "kind"))
            {
                case "stress":
                    return $"최대 응력 {Num(r["max_von_mises_mpa"], "G4")} MPa\n" +
                           $"최대 변위 {Num(r["max_displacement_mm"], "G4")} mm\n" +
                           $"안전율 {Num(r["safety_factor"], "0.0")}\n자유도 {r["dofs"]}";
                case "heat":
                    return $"온도 {Num(r["min_temperature"], "0.0")} ~ {Num(r["max_temperature"], "0.0")} °C\n" +
                           $"최대 열유속 {Num(r["max_flux_w_m2"], "0.0")} W/m²";
                case "modal":
                    return "고유진동수 Hz\n" + string.Join("\n",
                        (r["frequencies_hz"] as JsonArray ?? new JsonArray()).Select((f, i) => $"  {i + 1})  {Num(f, "0.0")}"));
                case "buckling":
                    return "좌굴 배수 (가한 하중 × 배수 = 좌굴 하중)\n" + string.Join("\n",
                        (r["load_factors"] as JsonArray ?? new JsonArray()).Select((f, i) => $"  {i + 1})  {Num(f, "0.00")}"));
                default:
                    return r.ToJsonString();
            }
        }
    }
}
