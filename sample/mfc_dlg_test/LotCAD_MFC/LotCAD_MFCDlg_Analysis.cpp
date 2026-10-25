// LotCAD_MFCDlg_Analysis.cpp: 해석 패널 — 바람 터널 · 물 · 구조 해석
//
// 엔진 자체 해석 패널(ImGui)은 호스트 창 안에서 그려지지 않아, 같은 일을 C API 로 여기서 한다.
// 세 API(CAD_WindTunnel · CAD_Water · CAD_StructuralAnalysis)는 {"op": …} JSON 을 받아 결과 JSON 을 준다 —
// op·인자는 헤더 LotCAD_API.h 의 해석 주석, MCP 도구 wind_tunnel · water · structural_analysis 와 같다.
//
//   바람 터널: 솔리드 선택 → 시작(다음 프레임에 켜짐) → 단면·연기·표면 압력으로 보기. 바람은 +X.
//   물:        닫힌 솔리드(그릇) 선택 → 물 높이 → 시작 → 기울이기·흔들기
//   구조 해석: 솔리드 선택 → 열기(면 목록이 온다) → 면 골라 고정·하중 → 실행(작업 스레드) → 결과·색 보기
//
// ⚠️ 2회 호출 규약 — CadCallJson(CadText.h)로만 부른다. 버퍼를 키워 다시 부르면 start·run 이 두 번 실행된다.
// 상태는 엔진이 프레임마다 바꾼다(켜짐·풀이 끝) — 패널이 열려 있는 동안 0.25초마다 {"op":"status"} 로 읽는다.
// 해석 모듈 LotCADSim.dll · LotCADCfd.dll 이 LotCADCore.dll 옆에 있어야 한다(빌드 후 단계가 같이 복사).

#include "pch.h"
#include "framework.h"
#include "LotCAD_MFC.h"
#include "LotCAD_MFCDlg.h"
#include "CadText.h"
#include "MiniJson.h"

#include <algorithm>
#include <cmath>
#include <memory>

namespace {
	// ── JSON 만들기·읽기 도우미 ──
	std::string Num(double v)
	{
		char buf[32];
		sprintf_s(buf, "%.6g", v);
		return buf;
	}

	std::string Ids(const std::vector<uint32_t>& ids)
	{
		std::string s = "[";
		for (size_t i = 0; i < ids.size(); ++i) s += (i ? "," : "") + std::to_string(ids[i]);
		return s + "]";
	}

	std::vector<uint32_t> SelectedIds()
	{
		// 개수만 먼저(NULL, 0) 묻고 그만큼 칸을 잡아 한 번에 받는다
		const int32_t n = CAD_GetSelection(nullptr, 0);
		std::vector<uint32_t> ids(n > 0 ? (size_t)n : 0);
		if (!ids.empty()) {
			const int32_t got = CAD_GetSelection(ids.data(), (uint32_t)ids.size());
			ids.resize(got > 0 ? (std::min)((size_t)got, ids.size()) : 0);
		}
		ids.erase(std::remove(ids.begin(), ids.end(), 0u), ids.end());
		return ids;
	}

	/// 숫자 → 글. 엔진은 아직 없는 값을 null 로 준다(켠 직후의 항력 계수 등) — 그땐 "-".
	std::wstring Fmt(const MiniJson::Value& v, const wchar_t* format)
	{
		if (v.IsNull()) return L"-";
		wchar_t buf[64];
		swprintf_s(buf, format, v.Num());
		return buf;
	}

	std::wstring Cells(const MiniJson::Value& cells)
	{
		std::wstring s;
		for (const auto& c : cells.Items()) s += (s.empty() ? L"" : L" × ") + std::to_wstring(c.Int());
		return s;
	}

	/// 법선 → "+Z" 처럼(축에 거의 맞으면), 아니면 숫자 셋.
	std::wstring AxisName(const MiniJson::Value& n)
	{
		for (int i = 0; i < 3; ++i) {
			const double c = n[i].Num();
			if (std::fabs(c) > 0.98) return std::wstring(c > 0 ? L"+" : L"−") + L"XYZ"[i];
		}
		return L"(" + Fmt(n[0], L"%.2f") + L", " + Fmt(n[1], L"%.2f") + L", " + Fmt(n[2], L"%.2f") + L")";
	}

	std::wstring ResultText(const MiniJson::Value& r)
	{
		const std::string kind = r["kind"].str;
		if (kind == "stress")
			return L"최대 응력 " + Fmt(r["max_von_mises_mpa"], L"%.4g") + L" MPa\n최대 변위 " + Fmt(r["max_displacement_mm"], L"%.4g") +
			       L" mm\n안전율 " + Fmt(r["safety_factor"], L"%.1f") + L"\n자유도 " + Fmt(r["dofs"], L"%.0f");
		if (kind == "heat")
			return L"온도 " + Fmt(r["min_temperature"], L"%.1f") + L" ~ " + Fmt(r["max_temperature"], L"%.1f") +
			       L" °C\n최대 열유속 " + Fmt(r["max_flux_w_m2"], L"%.1f") + L" W/m²";
		if (kind == "modal" || kind == "buckling") {
			std::wstring s = kind == "modal" ? L"고유진동수 Hz" : L"좌굴 배수 (가한 하중 × 배수 = 좌굴 하중)";
			const auto& list = r[kind == "modal" ? "frequencies_hz" : "load_factors"].Items();
			for (size_t i = 0; i < list.size(); ++i)
				s += L"\n  " + std::to_wstring(i + 1) + L")  " + Fmt(list[i], kind == "modal" ? L"%.1f" : L"%.2f");
			return s;
		}
		return L"";
	}

	/// 해석 API 한 번 — 결과 JSON. 실패면 error 에 이유.
	MiniJson::Value Call(int (*fn)(const char*, char*, int), const std::string& args, std::wstring& error)
	{
		const std::string text = CadCallJson(fn, args);
		if (text.empty()) {
			error = L"실패: " + CadLastError();
			return {};
		}
		MiniJson::Value v = MiniJson::Parse(text);
		error = Utf8ToWide(v["error"].str.c_str());
		return v;
	}

	const std::vector<std::wstring> kGrids = { L"빠름", L"보통", L"정밀" };
	const char* const kGridValues[] = { "fast", "normal", "fine" };
}


// ── 바람 터널 ────────────────────────────────────────────────────────────

void CLotCADMFCDlg::OpenWindPanel()
{
	struct State {
		int grid = 0, field = 0, plane = 1;
		float speed = 0.06f, at = 0.5f;
		bool active = false;
		std::wstring error;
		std::string Do(const std::string& args) { MiniJson::Value v = Call(CAD_WindTunnel, args, error); return v["ok"].Bool() ? "ok" : ""; }
	};
	auto st = std::make_shared<State>();
	static const char* const kFields[] = { "speed", "pressure", "vortex", "smoke" };
	static const char* const kPlanes[] = { "x", "y", "z" };
	auto view = [st] {
		st->Do(std::string("{\"op\":\"view\",\"plane\":\"") + kPlanes[st->plane] + "\",\"at\":" + Num(st->at) + "}");
	};

	CToolPanel& p = m_panel;
	p.Open(L"바람 터널 — 물체 둘레 공기 흐름", kPanelWind);
	p.AddNote(L"솔리드를 선택하고 시작. 바람은 +X 쪽으로 분다.", 2);
	p.AddChoice(L"격자", kGrids, st->grid, [st](int i) { st->grid = i; });
	p.AddSlider(L"바람 세기", 0.02f, 0.10f, st->speed, 3, [st](float v) {
		st->speed = v;
		if (st->active) st->Do("{\"op\":\"wind\",\"value\":" + Num(v) + "}");
	});
	p.AddButton(L"시작 — 선택한 솔리드 둘레", [st] {
		const auto ids = SelectedIds();
		if (ids.empty()) { st->error = L"3D 뷰에서 대상 솔리드를 먼저 선택하세요"; return; }
		st->Do("{\"op\":\"start\",\"ids\":" + Ids(ids) + ",\"grid\":\"" + kGridValues[st->grid] + "\",\"wind\":" + Num(st->speed) + "}");
	});
	p.AddButtonRow({ { L"정지", [st] { st->Do("{\"op\":\"stop\"}"); } },
	                 { L"일시정지", [st] { st->Do("{\"op\":\"pause\"}"); } },
	                 { L"재생", [st] { st->Do("{\"op\":\"play\"}"); } },
	                 { L"초기화", [st] { st->Do("{\"op\":\"reset\"}"); } } });

	p.AddSection(L"보기");
	p.AddChoice(L"색", { L"속도", L"압력", L"소용돌이", L"연기" }, st->field, [st](int i) {
		st->field = i;
		st->Do(std::string("{\"op\":\"view\",\"field\":\"") + kFields[i] + "\"}");
	});
	p.AddChoice(L"단면", { L"X", L"Y", L"Z" }, st->plane, [st, view](int i) { st->plane = i; view(); });
	p.AddSlider(L"단면 위치", 0, 1, st->at, 2, [st, view](float v) { st->at = v; view(); });
	p.AddToggle(L"표면 압력 색", false, [st](bool on) { st->Do(std::string("{\"op\":\"view\",\"surface\":") + (on ? "true" : "false") + "}"); });
	p.AddToggle(L"연기", false, [st](bool on) { st->Do(std::string("{\"op\":\"view\",\"smoke\":") + (on ? "true" : "false") + "}"); });
	p.AddStatus(4);

	p.onTick = [this, st] {
		std::wstring err;
		const MiniJson::Value w = Call(CAD_WindTunnel, "{\"op\":\"status\"}", err);
		st->active = w["active"].Bool();
		std::wstring text = st->active ? L"켜짐 — 솔리드 " + std::to_wstring(w["ids"].Items().size()) + L"개 둘레, 바람 +X"
		                  : w["starting"].Bool() ? L"켜는 중…" : L"꺼짐 — 솔리드를 선택하고 시작";
		if (st->active) {
			text += L"\n항력 계수 " + Fmt(w["drag_coefficient"], L"%.3f");
			if (!w["cells"].Items().empty()) text += L"   격자 " + Cells(w["cells"]);
			if (w["flowing"].IsFalse()) text += L"\n일시정지됨";
		}
		if (!st->error.empty()) text += L"\n" + st->error;
		m_panel.SetStatus(text);
	};
	p.onClose = [this] { RelayoutNow(); };   // 닫아도 바람 터널은 계속 돈다 — 끄려면 정지
}


// ── 물 ──────────────────────────────────────────────────────────────────

void CLotCADMFCDlg::OpenWaterPanel()
{
	struct State {
		int grid = 1;
		float level = 0.5f, tiltX = 0, tiltY = 0, shake = 0.3f;
		std::wstring error;
		void Do(const std::string& args) { Call(CAD_Water, args, error); }
	};
	auto st = std::make_shared<State>();
	auto tilt = [st] { st->Do("{\"op\":\"tilt\",\"x\":" + Num(st->tiltX) + ",\"y\":" + Num(st->tiltY) + "}"); };

	CToolPanel& p = m_panel;
	p.Open(L"물 — 그릇에 물을 채워 출렁임", kPanelWater);
	p.AddNote(L"닫힌 솔리드(그릇)를 선택하고 시작.", 1);
	p.AddChoice(L"격자", kGrids, st->grid, [st](int i) { st->grid = i; });
	p.AddSlider(L"물 높이", 0.05f, 0.95f, st->level, 2, [st](float v) { st->level = v; });
	p.AddButton(L"시작 — 선택한 그릇", [st] {
		const auto ids = SelectedIds();
		if (ids.empty()) { st->error = L"3D 뷰에서 그릇이 될 닫힌 솔리드를 먼저 선택하세요"; return; }
		st->Do("{\"op\":\"start\",\"id\":" + std::to_string(ids[0]) + ",\"level\":" + Num(st->level) +
		       ",\"grid\":\"" + kGridValues[st->grid] + "\"}");
	});
	p.AddButtonRow({ { L"정지", [st] { st->Do("{\"op\":\"stop\"}"); } },
	                 { L"일시정지", [st] { st->Do("{\"op\":\"pause\"}"); } },
	                 { L"재생", [st] { st->Do("{\"op\":\"play\"}"); } },
	                 { L"초기화", [st] { st->Do("{\"op\":\"reset\"}"); } } });

	p.AddSection(L"움직이기");
	p.AddSlider(L"기울이기 X (도)", -40, 40, 0, 0, [st, tilt](float v) { st->tiltX = v; tilt(); });
	p.AddSlider(L"기울이기 Y (도)", -40, 40, 0, 0, [st, tilt](float v) { st->tiltY = v; tilt(); });
	p.AddSlider(L"흔들기 세기", 0.05f, 1.0f, st->shake, 2, [st](float v) { st->shake = v; });
	// 주기를 비우면 엔진이 첫 출렁임 공진 주기로 흔든다
	p.AddButtonRow({ { L"흔들기(공진)", [st] { st->Do("{\"op\":\"shake\",\"amplitude\":" + Num(st->shake) + "}"); } },
	                 { L"멈춤", [st] { st->Do("{\"op\":\"shake\",\"amplitude\":0}"); } } });
	p.AddStatus(4);

	p.onTick = [this, st] {
		std::wstring err;
		const MiniJson::Value w = Call(CAD_Water, "{\"op\":\"status\"}", err);
		const bool active = w["active"].Bool();
		std::wstring text = active ? L"켜짐 — 그릇 #" + std::to_wstring(w["container"].Int())
		                  : w["starting"].Bool() ? L"켜는 중…" : L"꺼짐 — 닫힌 솔리드(그릇)를 선택하고 시작";
		if (active) {
			if (!w["cells"].Items().empty()) text += L"\n격자 " + Cells(w["cells"]);
			const auto& drift = w["mass_drift"];   // 비율 — 퍼센트로 보인다
			wchar_t pct[32] = L"-";
			if (!drift.IsNull()) swprintf_s(pct, L"%.4f%%", drift.Num() * 100);
			text += L"\n질량 오차 " + std::wstring(pct);
			if (w["flowing"].IsFalse()) text += L"   일시정지됨";
		}
		if (!st->error.empty()) text += L"\n" + st->error;
		m_panel.SetStatus(text);
	};
	p.onClose = [this] { RelayoutNow(); };
}


// ── 구조 해석 ────────────────────────────────────────────────────────────

void CLotCADMFCDlg::OpenSimPanel()
{
	struct State {
		int face = -1;                 // 고른 면 번호(엔진의 면 index)
		std::vector<int> listFaces;    // 목록 줄 → 면 번호
		std::string facesKey;          // 면·조건이 바뀌었을 때만 목록을 다시 채운다
		int faceList = 0, force = 0, pressure = 0, temp = 0, flux = 0, convect = 0;   // 패널 컨트롤 번호
		std::wstring error;
		void Do(const std::string& args) { Call(CAD_StructuralAnalysis, args, error); }
		std::string Face() const { return std::to_string(face); }
		bool NeedFace()
		{
			if (face < 0) error = L"목록에서 면을 먼저 고르세요";
			return face >= 0;
		}
	};
	auto st = std::make_shared<State>();
	static const char* const kTypes[] = { "stress", "heat", "modal", "buckling" };
	static const char* const kMaterials[] = { "steel", "aluminum", "stainless", "titanium", "abs" };
	static const char* const kShows[] = { "stress", "disp", "safety", "temp", "flux",
	                                      "mode 1", "mode 2", "mode 3", "mode 4", "mode 5", "mode 6" };

	CToolPanel& p = m_panel;
	p.Open(L"구조 해석 — 응력·열·진동·좌굴", kPanelSim);
	p.AddButtonRow({ { L"선택한 솔리드로 열기", [st] {
	                       const auto ids = SelectedIds();
	                       if (ids.empty()) { st->error = L"3D 뷰에서 대상 솔리드를 먼저 선택하세요"; return; }
	                       st->face = -1;
	                       st->Do("{\"op\":\"open\",\"id\":" + std::to_string(ids[0]) + "}");
	                   } },
	                 { L"닫기", [st] { st->face = -1; st->Do("{\"op\":\"close\"}"); } } });
	p.AddChoice(L"종류", { L"응력", L"열전도", L"진동 모드", L"좌굴" }, 0,
	            [st](int i) { st->Do(std::string("{\"op\":\"set\",\"type\":\"") + kTypes[i] + "\"}"); });
	p.AddChoice(L"재료", { L"강철(S275)", L"알루미늄(6061-T6)", L"스테인리스", L"티타늄", L"ABS" }, 0,
	            [st](int i) { st->Do(std::string("{\"op\":\"set\",\"material\":\"") + kMaterials[i] + "\"}"); });
	p.AddChoice(L"요소", kGrids, 1, [st](int i) { st->Do(std::string("{\"op\":\"set\",\"size\":\"") + kGridValues[i] + "\"}"); });

	p.AddSection(L"면 — 골라서 조건을 건다");
	st->faceList = p.AddList(5, [st](int row) {
		st->face = (row >= 0 && row < (int)st->listFaces.size()) ? st->listFaces[row] : -1;
	});
	p.AddButtonRow({ { L"고정", [st] { if (st->NeedFace()) st->Do("{\"op\":\"fix\",\"face\":" + st->Face() + "}"); } },
	                 { L"풀기", [st] { if (st->NeedFace()) st->Do("{\"op\":\"free\",\"face\":" + st->Face() + "}"); } } });
	// 하중 — 응력·진동·좌굴
	st->force = p.AddNumbers(L"힘 N  (x · y · z)", { 0, 0, -1000 }, L"걸기", [this, st] {
		if (!st->NeedFace()) return;
		const auto f = m_panel.GetNumbers(st->force);
		st->Do("{\"op\":\"force\",\"face\":" + st->Face() + ",\"force\":[" + Num(f[0]) + "," + Num(f[1]) + "," + Num(f[2]) + "]}");
	});
	st->pressure = p.AddNumbers(L"압력 MPa", { 1 }, L"걸기", [this, st] {
		if (!st->NeedFace()) return;
		st->Do("{\"op\":\"pressure\",\"face\":" + st->Face() + ",\"value\":" + Num(m_panel.GetNumbers(st->pressure)[0]) + "}");
	});
	// 열 조건 — 종류가 열전도일 때
	st->temp = p.AddNumbers(L"온도 °C  (열전도)", { 80 }, L"걸기", [this, st] {
		if (!st->NeedFace()) return;
		st->Do("{\"op\":\"temp\",\"face\":" + st->Face() + ",\"value\":" + Num(m_panel.GetNumbers(st->temp)[0]) + "}");
	});
	st->flux = p.AddNumbers(L"열 W  (열전도)", { 10 }, L"걸기", [this, st] {
		if (!st->NeedFace()) return;
		st->Do("{\"op\":\"flux\",\"face\":" + st->Face() + ",\"value\":" + Num(m_panel.GetNumbers(st->flux)[0]) + "}");
	});
	st->convect = p.AddNumbers(L"대류 h · 주변 °C  (열전도)", { 10, 20 }, L"걸기", [this, st] {
		if (!st->NeedFace()) return;
		const auto v = m_panel.GetNumbers(st->convect);
		st->Do("{\"op\":\"convect\",\"face\":" + st->Face() + ",\"h\":" + Num(v[0]) + ",\"ambient\":" + Num(v[1]) + "}");
	});

	p.AddSection(L"풀기");
	p.AddButtonRow({ { L"실행", [st] { st->Do("{\"op\":\"run\"}"); } },
	                 { L"취소", [st] { st->Do("{\"op\":\"cancel\"}"); } },
	                 { L"수렴 확인", [st] { st->Do("{\"op\":\"converge\"}"); } },
	                 { L"지우기", [st] { st->Do("{\"op\":\"clear\"}"); } } });
	p.AddChoice(L"결과 색", { L"응력", L"변위", L"안전율", L"온도", L"열 흐름",
	                          L"모드 1", L"모드 2", L"모드 3", L"모드 4", L"모드 5", L"모드 6" }, 0,
	            [st](int i) { st->Do(std::string("{\"op\":\"set\",\"show\":\"") + kShows[i] + "\"}"); });
	p.AddStatus(7);

	p.onTick = [this, st] {
		std::wstring err;
		const MiniJson::Value s = Call(CAD_StructuralAnalysis, "{\"op\":\"status\"}", err);
		const auto& faces = s["faces"].Items();

		// 면 목록 — 면이나 조건이 바뀔 때만 다시 채운다(고른 줄 유지)
		std::string key;
		for (const auto& f : faces) key += std::to_string(f["index"].Int()) + ",";
		std::vector<std::pair<int, std::string>> conds;   // (면, 종류)
		for (const char* list : { "conditions", "heat_conditions" })
			for (const auto& c : s[list].Items()) {
				conds.emplace_back(c["face"].Int(), c["kind"].str);
				key += c["kind"].str + std::to_string(c["face"].Int()) + ";";
			}
		if (key != st->facesKey) {
			st->facesKey = key;
			std::vector<std::wstring> rows;
			st->listFaces.clear();
			int selected = -1;
			for (const auto& f : faces) {
				const int index = f["index"].Int();
				std::wstring tags;
				for (const auto& c : conds)
					if (c.first == index) tags += (tags.empty() ? L"" : L"·") + Utf8ToWide(c.second.c_str());
				rows.push_back(L"면 " + std::to_wstring(index) + L"   " + AxisName(f["normal"]) + L"   넓이 " +
				               Fmt(f["area"], L"%.3g") + (tags.empty() ? L"" : L"   [" + tags + L"]"));
				if (index == st->face) selected = (int)st->listFaces.size();
				st->listFaces.push_back(index);
			}
			m_panel.SetListItems(st->faceList, rows, selected);
			if (faces.empty()) st->face = -1;
		}

		std::wstring text = faces.empty() ? L"닫힘 — 솔리드를 선택하고 열기"
		                  : s["busy"].Bool() ? L"푸는 중…"
		                  : L"열림 — 면 " + std::to_wstring(faces.size()) + L"개" + (st->face >= 0 ? L", 고른 면 " + std::to_wstring(st->face) : L"");
		const std::wstring result = ResultText(s["result"]);
		if (!result.empty()) text += L"\n" + result;
		if (!st->error.empty()) text += L"\n" + st->error;
		m_panel.SetStatus(text);
	};
	p.onClose = [this] { RelayoutNow(); };   // 닫아도 해석 결과·조건은 엔진에 남는다 — 지우려면 닫기·지우기
}
