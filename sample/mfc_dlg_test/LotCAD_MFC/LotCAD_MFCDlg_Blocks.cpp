// LotCAD_MFCDlg_Blocks.cpp: 관리 탭 — 블록 · 외부 참조(XREF) 패널
//
// 블록 정의 표는 CAD_GetBlocksJson 한 번으로 읽는다:
//   {"blocks":[{"name","objects","references"(장면에 넣은 수),"base":[x,y,z],"bounds":{"min","max"}?,
//               "xref"(외부 참조 경로)?,"xrefFound"?,"xrefLoaded"?}]}
// 만들기·편집은 엔진 명령으로 한다 — block 은 이름·기준점을, bedit 은 고른 블록 참조를 명령행에서 받는다.
// 블록 편집은 탭을 여닫으므로 다음 CAD_Tick 에 처리된다. 외부 참조는 C API(CAD_Xref*)로.
//
// ⚠️ 이미 있는 블록 정의를 한 번 더 놓는 C API 는 아직 없다 — 블록 참조를 선택하고 홈 > 복사로 늘린다.
//    외부 참조는 그것이 든 DWG·DXF 를 열면 생긴다(붙이기 명령은 없다).

#include "pch.h"
#include "framework.h"
#include "LotCAD_MFC.h"
#include "LotCAD_MFCDlg.h"
#include "CadText.h"
#include "MiniJson.h"

#include <memory>
#include <string>
#include <vector>

namespace {
	uint64_t SceneRevision()
	{
		uint64_t rev = 0;
		CAD_GetSceneRevision(&rev);
		return rev;
	}
}

void CLotCADMFCDlg::OpenBlockPanel()
{
	struct State {
		MiniJson::Value blocks;            // CAD_GetBlocksJson 의 "blocks"
		uint64_t revision = ~0ull;
		int row = -1, list = 0;
		std::wstring msg = L"블록을 고르고 편집하거나, 객체를 선택해 새 블록을 만든다";

		const MiniJson::Value& Current() const { return blocks[row]; }
		std::string Name() const { return row >= 0 ? Current()["name"].str : std::string(); }   // UTF-8
		bool IsXref() const { return row >= 0 && Current().Has("xref"); }
	};
	auto st = std::make_shared<State>();

	auto reload = [this, st] {
		const std::string keep = st->Name();
		st->blocks = MiniJson::Parse(CadReadJson(CAD_GetBlocksJson))["blocks"];
		st->revision = SceneRevision();
		std::vector<std::wstring> lines;
		st->row = -1;
		for (size_t i = 0; i < st->blocks.Items().size(); ++i) {
			const MiniJson::Value& b = st->blocks[i];
			if (b["name"].str == keep) st->row = (int)i;
			std::wstring line = Utf8ToWide(b["name"].str.c_str()) + L"  · 객체 " + std::to_wstring(b["objects"].Int(0)) +
			                    L" · 참조 " + std::to_wstring(b["references"].Int(0));
			if (b.Has("xref")) line += b["xrefFound"].IsFalse() ? L"  [외부 참조 — 파일 없음]" : L"  [외부 참조]";
			lines.push_back(line);
		}
		m_panel.SetListItems(st->list, lines, st->row);
	};
	// 고른 블록이 있어야 하는 동작 — 없으면 안내만
	auto needRow = [st]() {
		if (st->row >= 0) return true;
		st->msg = L"먼저 목록에서 블록을 고르세요";
		return false;
	};
	// 외부 참조 함수 결과 — 실패 이유는 CAD_GetLastError
	auto onXref = [st](const wchar_t* what, CAD_Status s) {
		st->msg = s == CAD_OK ? std::wstring(what) : std::wstring(what) + L" 실패: " + CadLastError();
	};

	CToolPanel& p = m_panel;
	p.Open(L"블록 — 만들기·편집·외부 참조", kPanelBlocks);

	p.AddSection(L"블록 정의");
	st->list = p.AddList(7, [st](int row) { st->row = row; });

	p.AddSection(L"만들기 · 편집");
	p.AddButton(L"선택한 객체로 새 블록", [this, st] {
		if (CadSelectedIds().empty()) { st->msg = L"먼저 3D 뷰에서 블록으로 묶을 객체를 선택하세요"; return; }
		CadStartCommand("block");   // 이름 → 기준점(Enter = 고른 것의 왼쪽 아래)을 명령행이 묻는다
		st->msg = L"명령행에 블록 이름을 치고 Enter, 이어서 기준점을 찍으세요";
		m_view.SetFocus();
	});
	p.AddButton(L"고른 블록 편집 (블록 편집 탭)", [st, needRow] {
		if (!needRow()) return;
		// bedit 은 뒤의 글 전체를 이름으로 받는다 — 빈칸이 든 이름도 그대로(따옴표로 감싸지 않는다)
		st->msg = CadStartCommand(("bedit " + st->Name()).c_str()) == CAD_OK
		        ? L"블록 편집 탭을 열었습니다 — 고친 뒤 '저장하고 닫기'" : L"편집 실패: " + CadLastError();
	});
	p.AddButtonRow({
		{ L"저장하고 닫기", [st] { CadStartCommand("bclose save");    st->msg = L"블록을 저장하고 편집 탭을 닫았습니다"; } },
		{ L"버리고 닫기",   [st] { CadStartCommand("bclose discard"); st->msg = L"고친 것을 버리고 편집 탭을 닫았습니다"; } },
	});
	p.AddButton(L"편집 중 기준점 바꾸기 (클릭)", [this, st] {
		CadStartCommand("bbase");
		st->msg = L"3D 뷰에서 새 기준점을 클릭하세요 (블록 편집 탭에서만)";
		m_view.SetFocus();
	});
	p.AddNote(L"새 블록은 명령행이 이름·기준점을 묻는다.\n같은 블록을 더 놓으려면 블록 참조를\n선택하고 홈 > 복사", 3);

	p.AddSection(L"외부 참조 (고른 블록이 외부 참조일 때)");
	p.AddButtonRow({
		{ L"다시 읽기", [st, needRow, onXref] { if (needRow()) onXref(L"다시 읽음", CAD_XrefReload(st->Name().c_str())); } },
		{ L"결합",      [st, needRow, onXref] { if (needRow()) onXref(L"도면에 결합함", CAD_XrefBind(st->Name().c_str())); } },
		{ L"떼기",      [st, needRow, onXref] { if (needRow()) onXref(L"외부 참조를 뗌", CAD_XrefDetach(st->Name().c_str())); } },
	});
	p.AddButtonRow({
		{ L"경로 = 상대", [st, needRow, onXref] { if (needRow()) onXref(L"상대 경로로", CAD_XrefSetPath(st->Name().c_str(), "relative")); } },
		{ L"경로 = 절대", [st, needRow, onXref] { if (needRow()) onXref(L"절대 경로로", CAD_XrefSetPath(st->Name().c_str(), "absolute")); } },
	});
	p.AddStatus(4);

	reload();
	p.onTick = [this, st, reload] {
		if (SceneRevision() != st->revision) reload();
		std::wstring detail;
		if (st->row >= 0) {
			const MiniJson::Value& b = st->Current();
			wchar_t base[96];
			swprintf_s(base, L"기준점 (%.1f, %.1f, %.1f)", b["base"][0].Num(), b["base"][1].Num(), b["base"][2].Num());
			detail = L"\n\n" + Utf8ToWide(b["name"].str.c_str()) + L" — " + base;
			if (st->IsXref()) detail += L"\n외부 참조: " + Utf8ToWide(b["xref"].str.c_str());
		}
		m_panel.SetStatus(st->msg + detail);
	};
	p.onClose = [this] { RelayoutNow(); };
}
