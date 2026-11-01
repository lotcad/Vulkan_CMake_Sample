// LotCAD_MFCDlg_Layers.cpp: 관리 탭 — 도면층 · 선종류 패널
//
// 엔진의 도면층·선종류 창(명령 layer · linetype)은 ImGui 라 임베드에선 그려지지 않는다.
// 같은 일을 C API(CAD_*Layer* · CAD_*Linetype*)로 하는 패널을 여기서 만든다.
//
// 도면층 표는 CAD_GetLayersJson 한 번으로 읽는다:
//   {"revision","layers":[{"id","name","visible","locked","color":[r,g,b],"opacity","linetypeId","linetype",
//                         "objectCount","selectedCount"(,"fixed":true — 도면층 0)}]}
// 장면 번호(CAD_GetSceneRevision)가 바뀔 때만 다시 읽는다 — 0.25초마다 숫자 하나만 묻는다.
//
// ⚠️ 지금 C API 에는 도면층 지우기와 "현재 도면층"(새로 그리는 객체가 들어갈 층) 정하기가 없다.
//    새로 그린 객체는 엔진의 현재 도면층(처음엔 0)으로 들어가므로, 그린 뒤 '선택한 객체를 이 도면층으로' 를 누른다.

#include "pch.h"
#include "framework.h"
#include "LotCAD_MFC.h"
#include "LotCAD_MFCDlg.h"
#include "CadText.h"
#include "MiniJson.h"

#include <cmath>
#include <memory>
#include <utility>
#include <vector>

namespace {
	// 도면층 색 고르기 — 오토캐드 색 번호 1~7 + 회색. 목록에 없는 색이면 '(다른 색)' 으로 보인다.
	struct NamedColor { const wchar_t* name; double r, g, b; };
	const NamedColor kColors[] = {
		{ L"흰색", 1, 1, 1 }, { L"빨강", 1, 0, 0 }, { L"노랑", 1, 1, 0 }, { L"초록", 0, 1, 0 },
		{ L"하늘", 0, 1, 1 }, { L"파랑", 0, 0, 1 }, { L"자홍", 1, 0, 1 }, { L"회색", 0.5, 0.5, 0.5 },
	};
	const int kColorCount = (int)_countof(kColors);

	int ColorIndex(const MiniJson::Value& rgb)
	{
		for (int i = 0; i < kColorCount; ++i)
			if (std::fabs(rgb[0].Num() - kColors[i].r) < 0.02 && std::fabs(rgb[1].Num() - kColors[i].g) < 0.02 &&
			    std::fabs(rgb[2].Num() - kColors[i].b) < 0.02)
				return i;
		return kColorCount;   // (다른 색)
	}

	// 선종류 표 — id 0 = Continuous(실선), 1~8 표준, 100~ 사용자. 개수를 먼저 묻고 그만큼 받는다.
	std::vector<std::pair<uint32_t, std::wstring>> ReadLinetypes()
	{
		std::vector<std::pair<uint32_t, std::wstring>> out;
		const int32_t n = CAD_GetLinetypeIds(nullptr, 0);
		std::vector<uint32_t> ids(n > 0 ? (size_t)n : 0);
		if (!ids.empty()) CAD_GetLinetypeIds(ids.data(), (uint32_t)ids.size());
		for (uint32_t id : ids) {
			char name[128] = {};
			if (CAD_GetLinetypeName(id, name, (uint32_t)sizeof(name)) >= 0) out.emplace_back(id, Utf8ToWide(name));
		}
		return out;
	}

	int LinetypeIndex(const std::vector<std::pair<uint32_t, std::wstring>>& types, uint32_t id)
	{
		for (size_t i = 0; i < types.size(); ++i) if (types[i].first == id) return (int)i;
		return -1;
	}

	std::vector<std::wstring> LinetypeNames(const std::vector<std::pair<uint32_t, std::wstring>>& types)
	{
		std::vector<std::wstring> names;
		for (const auto& t : types) names.push_back(t.second);
		return names;
	}

	uint64_t SceneRevision()
	{
		uint64_t rev = 0;
		CAD_GetSceneRevision(&rev);
		return rev;
	}
}


// ── 도면층 ──────────────────────────────────────────────────────────────
// 목록에서 층을 고르고 → 보이기·잠금·색·선종류·이름을 바꾸거나, 선택한 객체를 그 층으로 옮긴다.
// 도면층 표 바꾸기는 되돌리기에 남지 않는다(오토캐드 도면층 관리자처럼). 객체를 옮기는 것은 되돌릴 수 있다.

void CLotCADMFCDlg::OpenLayerPanel()
{
	struct State {
		MiniJson::Value layers;            // CAD_GetLayersJson 의 "layers"
		std::vector<std::pair<uint32_t, std::wstring>> linetypes;
		uint64_t revision = ~0ull;         // 마지막으로 읽은 장면 번호 — 처음엔 꼭 읽게 없는 값
		int row = 0;                       // 고른 줄 (0 = 도면층 0)
		int list = 0, colorChoice = 0, linetypeChoice = 0, nameRow = 0;
		std::wstring msg = L"층을 고르고 아래 버튼으로 바꾼다";

		const MiniJson::Value& Current() const { return layers[row]; }
		uint32_t CurrentId() const { return (uint32_t)Current()["id"].Num(); }
		bool Fixed() const { return Current()["fixed"].Bool(); }   // 도면층 0 — 보이기·색·선종류 고정
	};
	auto st = std::make_shared<State>();
	st->linetypes = ReadLinetypes();

	// 표를 다시 읽어 목록을 채운다. 고른 줄은 같은 id 를 따라간다(층이 늘거나 이름이 바뀌어도).
	auto reload = [this, st] {
		const uint32_t keep = st->layers.Items().empty() ? 0 : st->CurrentId();
		st->layers = MiniJson::Parse(CadReadJson(CAD_GetLayersJson))["layers"];
		st->revision = SceneRevision();
		std::vector<std::wstring> lines;
		st->row = 0;
		for (size_t i = 0; i < st->layers.Items().size(); ++i) {
			const MiniJson::Value& l = st->layers[i];
			if ((uint32_t)l["id"].Num() == keep) st->row = (int)i;
			std::wstring line = Utf8ToWide(l["name"].str.c_str());
			line += l["visible"].Bool() ? L"" : L"  [숨김]";
			line += l["locked"].Bool()  ? L"  [잠금]" : L"";
			line += L"  · " + Utf8ToWide(l["linetype"].str.c_str());
			line += L"  · 객체 " + std::to_wstring(l["objectCount"].Int(0));
			const int sel = l["selectedCount"].Int(0);
			if (sel > 0) line += L" (선택 " + std::to_wstring(sel) + L")";
			lines.push_back(line);
		}
		m_panel.SetListItems(st->list, lines, st->row);
		if (st->layers.Items().empty()) return;
		m_panel.SetChoice(st->colorChoice, ColorIndex(st->Current()["color"]));
		m_panel.SetChoice(st->linetypeChoice, LinetypeIndex(st->linetypes, (uint32_t)st->Current()["linetypeId"].Num()));
		m_panel.SetText(st->nameRow, Utf8ToWide(st->Current()["name"].str.c_str()));
	};
	// 고른 층에 하나 하고 결과를 글로 남긴다. 표가 바뀌면 다음 onTick 이 장면 번호로 알아채 다시 읽는다.
	auto onLayer = [st](const wchar_t* what, CAD_Status s) {
		st->msg = s == CAD_OK ? std::wstring(what) : std::wstring(what) + L" 실패: " + CadLastError();
	};

	CToolPanel& p = m_panel;
	p.Open(L"도면층 — 보이기·잠금·색·선종류", kPanelLayers);

	p.AddSection(L"도면층");
	st->list = p.AddList(8, [st, reload](int row) {
		if (row < 0) return;
		st->row = row;
		reload();   // 고른 층의 색·선종류·이름을 아래 칸에 맞춘다
	});
	p.AddButtonRow({
		{ L"보이기/숨기기", [st, onLayer] { onLayer(L"보이기 바꿈", CAD_SetLayerVisible(st->CurrentId(), !st->Current()["visible"].Bool())); } },
		{ L"잠금/풀기",     [st, onLayer] { onLayer(L"잠금 바꿈",   CAD_SetLayerLocked(st->CurrentId(), !st->Current()["locked"].Bool())); } },
	});
	std::vector<std::wstring> colors;
	for (const NamedColor& c : kColors) colors.push_back(c.name);
	colors.push_back(L"(다른 색)");
	st->colorChoice = p.AddChoice(L"색 (객체 색이 '도면층 따름' 일 때)", colors, 0, [st, onLayer](int i) {
		if (i < 0 || i >= kColorCount) return;
		onLayer(L"색 바꿈", CAD_SetLayerColor(st->CurrentId(), CAD_Color{ kColors[i].r, kColors[i].g, kColors[i].b }));
	});
	st->linetypeChoice = p.AddChoice(L"선종류 (선·폴리선·원·호에 보인다)", LinetypeNames(st->linetypes), 0, [st, onLayer](int i) {
		if (i < 0 || i >= (int)st->linetypes.size()) return;
		onLayer(L"선종류 바꿈", CAD_SetLayerLinetype(st->CurrentId(), st->linetypes[i].first));
	});
	st->nameRow = p.AddText(L"이름", L"", L"바꾸기", [this, st, onLayer] {
		onLayer(L"이름 바꿈", CAD_RenameLayer(st->CurrentId(), WideToUtf8(m_panel.GetText(st->nameRow)).c_str()));
	});

	p.AddSection(L"객체");
	p.AddButton(L"선택한 객체를 이 도면층으로", [st] {
		uint32_t changed = 0;
		const CAD_Status s = CAD_AssignSelectedToLayer(st->CurrentId(), &changed);   // 잠긴 층의 객체는 건너뛴다
		st->msg = s != CAD_OK      ? L"옮기기 실패: " + CadLastError()
		        : changed == 0     ? L"옮긴 객체 없음 — 3D 뷰에서 먼저 선택하세요"
		                           : L"객체 " + std::to_wstring(changed) + L"개를 옮겼습니다";
	});
	p.AddButton(L"선택한 객체 색 = 도면층 따름", [st] {
		uint32_t changed = 0;
		const CAD_Status s = CAD_SetSelectedColorByLayer(true, &changed);
		st->msg = s == CAD_OK ? L"객체 " + std::to_wstring(changed) + L"개가 도면층 색을 따릅니다" : L"실패: " + CadLastError();
	});

	p.AddSection(L"새 도면층");
	auto newRow = std::make_shared<int>(0);   // 버튼 람다가 자기 줄 번호를 알도록 — 줄 번호는 AddText 가 돌려준 뒤에 정해진다
	*newRow = p.AddText(L"이름", L"새 도면층", L"만들기", [this, st, newRow] {
		uint32_t id = 0;
		const CAD_Status s = CAD_CreateLayer(WideToUtf8(m_panel.GetText(*newRow)).c_str(), &id);   // 같은 이름 CAD_E_DUPLICATE
		st->msg = s == CAD_OK ? L"도면층을 만들었습니다 — 목록에서 골라 색·선종류를 정하세요" : L"만들기 실패: " + CadLastError();
	});
	p.AddNote(L"지우기·현재 도면층 정하기는 C API 에\n아직 없다. 새로 그린 객체는 위의\n'선택한 객체를 이 도면층으로' 로 옮긴다", 3);
	p.AddStatus(3);

	reload();
	p.onTick = [this, st, reload] {
		if (SceneRevision() != st->revision) reload();   // 객체 추가·층 바꿈·선택 … 이 있을 때만
		m_panel.SetStatus(st->msg);
	};
	p.onClose = [this] { RelayoutNow(); };
}


// ── 선종류 ──────────────────────────────────────────────────────────────
// 선택한 객체에 선종류(또는 '도면층 따름')를 주고, 객체별·전체 축척을 바꾸고, 무늬로 새 선종류를 만든다.
// 무늬 규칙은 오토캐드 .lin 과 같다: 양수 = 선, 음수 = 빈칸, 0 = 점. 단위는 도면 단위.

void CLotCADMFCDlg::OpenLinetypePanel()
{
	struct State {
		std::vector<std::pair<uint32_t, std::wstring>> linetypes;
		int pick = 1;                      // 고른 선종류 줄 (0 = 도면층 따름)
		int patternRow = 0, nameRow = 0, scaleRow = 0;
		std::wstring msg = L"선·폴리선·원·호를 선택하고 선종류를 고른다";
	};
	auto st = std::make_shared<State>();
	st->linetypes = ReadLinetypes();

	// 줄 0 = 도면층 따름(CAD_LINETYPE_BYLAYER), 1~ = 표의 선종류
	std::vector<std::wstring> names = { L"도면층 따름 (ByLayer)" };
	for (const auto& t : st->linetypes) {
		double pattern[8] = {};
		const int32_t n = CAD_GetLinetypePattern(t.first, pattern, 8);   // 요소 수 (실선 0)
		std::wstring line = t.second;
		if (n > 0) {
			line += L"   ";
			for (int i = 0; i < n && i < 8; ++i) {
				wchar_t v[32];
				swprintf_s(v, L"%s%g", i ? L", " : L"", pattern[i]);
				line += v;
			}
		}
		names.push_back(line);
	}
	auto pickedId = [st] { return st->pick == 0 ? CAD_LINETYPE_BYLAYER : st->linetypes[st->pick - 1].first; };

	CToolPanel& p = m_panel;
	p.Open(L"선종류 — 파선·숨은선·중심선", kPanelLinetypes);

	p.AddSection(L"선택한 객체에");
	const int list = p.AddList(8, [st](int row) { if (row >= 0) st->pick = row; });
	p.SetListItems(list, names, st->pick);
	p.AddButton(L"선택한 객체에 적용", [st, pickedId] {
		const std::vector<uint32_t> ids = CadSelectedIds();
		if (ids.empty()) { st->msg = L"먼저 3D 뷰에서 선·폴리선·원·호를 선택하세요"; return; }
		uint32_t changed = 0;
		// 하나라도 없거나 잠긴 층이면 아무것도 안 바꾼다(되돌리기 1)
		const CAD_Status s = CAD_SetObjectLinetype(ids.data(), (uint32_t)ids.size(), pickedId(), &changed);
		st->msg = s == CAD_OK ? L"객체 " + std::to_wstring(changed) + L"개의 선종류를 바꿨습니다 (메시·문자·치수엔 안 보임)"
		                      : L"적용 실패: " + CadLastError();
	});
	st->scaleRow = p.AddNumbers(L"축척 — 선택한 객체 · 전체(LTSCALE)", { 1.0, 1.0 });
	p.AddButtonRow({
		{ L"객체 축척 적용", [this, st] {
			const double v = m_panel.GetNumbers(st->scaleRow)[0];
			int done = 0;
			for (uint32_t id : CadSelectedIds()) if (CAD_SetObjectLinetypeScale(id, v) == CAD_OK) ++done;
			st->msg = done ? L"객체 " + std::to_wstring(done) + L"개의 축척을 바꿨습니다" : L"바꾼 객체 없음 — 선택·값(> 0)을 확인하세요";
		} },
		{ L"전체 축척 적용", [this, st] {
			const double v = m_panel.GetNumbers(st->scaleRow)[1];
			st->msg = CAD_SetLinetypeScale(v) == CAD_OK ? L"전체 선종류 축척을 바꿨습니다" : L"실패: " + CadLastError();
		} },
	});

	p.AddSection(L"새 선종류");
	st->nameRow = p.AddText(L"이름", L"내 파선");
	st->patternRow = p.AddText(L"무늬 (쉼표로, 양수 선 · 음수 빈칸 · 0 점)", L"0.5, -0.25, 0, -0.25");
	p.AddButton(L"만들기 (패널을 다시 열면 목록에 보인다)", [this, st] {
		std::vector<double> pattern;
		const std::wstring text = m_panel.GetText(st->patternRow);
		for (size_t at = 0; at < text.size();) {
			wchar_t* end = nullptr;
			const double v = wcstod(text.c_str() + at, &end);
			const size_t used = (size_t)(end - (text.c_str() + at));
			if (used == 0) { ++at; continue; }   // 쉼표·공백 건너뛰기
			pattern.push_back(v);
			at += used;
		}
		uint32_t id = 0;
		const CAD_Status s = CAD_CreateLinetype(WideToUtf8(m_panel.GetText(st->nameRow)).c_str(), pattern.data(),
		                                        (uint32_t)pattern.size(), nullptr, &id);
		st->msg = s == CAD_OK ? L"선종류 " + std::to_wstring(id) + L" 번을 만들었습니다" : L"만들기 실패: " + CadLastError();
	});
	p.AddStatus(3);

	p.onTick = [this, st] { m_panel.SetStatus(st->msg); };
	p.onClose = [this] { RelayoutNow(); };
}
