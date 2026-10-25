// LotCAD_MFCDlg_StatusBar.cpp: 상태바 구성 — 맨 아래 토글 버튼과 F3/F8/F10 키
//
// 엔진(3dEngine) 하단 상태바의 오른쪽 버튼 줄과 같은 순서·같은 기능이다.
//   [치수] [그리드] [셰이딩 ▾] [Ortho] [직교(F8)] [극좌표(F10)] [객체스냅 ▾]
// 치수·직교·극좌표·객체스냅은 엔진에 Get 함수가 있어 상태를 매번 엔진에 묻는다 —
// 명령행에 ortho off 처럼 쳐서 바꿔도 버튼이 따라간다. 그리드·스타일·투영은 Set 만 있어 호스트가 들고 있는다.

#include "pch.h"
#include "framework.h"
#include "LotCAD_MFC.h"
#include "LotCAD_MFCDlg.h"

#include "../../../sdk/include/LotCAD_API.h"

namespace {
	// CAD_SetVisualStyle 의 번호 순서 그대로
	const wchar_t* const kVisualStyles[] = {
		L"셰이딩", L"셰이딩+모서리", L"와이어프레임", L"와이어(모서리)", L"숨은선",
	};

	// CAD_SetOSnapModes 의 비트 (헤더 주석: END 1 · MID 2 · CEN 4 · FACE 8 · NODE 16 · QUA 32 · INT 64 · PER 128 · TAN 256 · NEA 512)
	struct SnapMode { uint32_t bit; const wchar_t* name; };
	const SnapMode kSnapModes[] = {
		{   1, L"끝점" },   {   2, L"중간점" }, {   4, L"중심점" }, {   8, L"면 중심" }, {  16, L"노드(점)" },
		{  32, L"사분점" }, {  64, L"교차점" }, { 128, L"수직점" }, { 256, L"접선" },    { 512, L"근처점" },
	};

	// 스냅·직교·극좌표 Get 은 결과 코드를 돌려주고 값은 출력 인자로 준다 — 실패(음수)면 꺼진 것으로 본다.
	bool OSnapOn()     { bool on = false; return CAD_GetOSnapEnabled(&on) == CAD_OK && on; }
	uint32_t OSnapModes() { uint32_t m = 0; return CAD_GetOSnapModes(&m) == CAD_OK ? m : 0; }
	bool OrthoOn()     { bool on = false; return CAD_GetOrthoEnabled(&on) == CAD_OK && on; }
	bool PolarOn()     { bool on = false; return CAD_GetPolarTracking(&on, nullptr) == CAD_OK && on; }   // 각 증분(rad)은 안 읽음
}

void CLotCADMFCDlg::BuildStatusBar()
{
	CCadStatusBar& s = m_statusBar;

	s.AddToggle(L"치수",
		[] { bool v = false; CAD_GetFeatureDimensionsVisible(&v); return v; },
		[] { bool v = false; CAD_GetFeatureDimensionsVisible(&v); CAD_SetFeatureDimensionsVisible(!v); },
		L"선택한 솔리드의 피처 치수 표시 (fdim)\n치수를 더블클릭하면 명령행이 새 값을 기다린다");

	s.AddToggle(L"그리드",
		[this] { return m_gridOn; },
		[this] { m_gridOn = !m_gridOn; CAD_SetGridEnabled(m_gridOn); },
		L"바닥 그리드 표시");

	// 비주얼 스타일 — 누르면 위로 메뉴가 열린다 (엔진의 드롭업과 같은 자리)
	s.AddButton(
		[this] { return std::wstring(kVisualStyles[m_visualStyle]) + L" ▾"; },
		[this](const CRect& rc) {
			CMenu menu;
			menu.CreatePopupMenu();
			for (int i = 0; i < _countof(kVisualStyles); ++i)
				menu.AppendMenu(MF_STRING | (i == m_visualStyle ? MF_CHECKED : 0), i + 1, kVisualStyles[i]);
			// TPM_RETURNCMD — WM_COMMAND 대신 고른 항목 번호를 바로 돌려받는다 (0 = 취소)
			const int picked = menu.TrackPopupMenu(TPM_RETURNCMD | TPM_BOTTOMALIGN | TPM_LEFTALIGN, rc.left, rc.top, this);
			if (picked > 0) {
				m_visualStyle = picked - 1;
				CAD_SetVisualStyle(m_visualStyle);
			}
		},
		L"비주얼 스타일 — 셰이딩 / 모서리 / 와이어프레임 / 숨은선");

	// 투영 — 토글이 아니라 지금 상태를 글자로 보여 주는 버튼 (엔진과 같이 Persp ↔ Ortho)
	s.AddButton(
		[this] { return std::wstring(m_ortho ? L"Ortho" : L"Persp"); },
		[this](const CRect&) { SetOrtho(!m_ortho); },
		L"원근(Persp) / 직교(Ortho) 투영 전환");

	s.AddToggle(L"직교(F8)",
		[] { return OrthoOn(); },
		[this] { ToggleOrthoTracking(); },
		L"직교 추적 — 그리는 방향을 가로·세로로 고정 (F8, 명령 ortho)");

	s.AddToggle(L"극좌표(F10)",
		[] { return PolarOn(); },
		[this] { TogglePolarTracking(); },
		L"극좌표 추적 — 일정 각도마다 추적선 (F10)\n각도는 명령행에 polar 30 처럼");

	// 객체스냅 — 엔진처럼 켜기/끄기와 스냅 종류를 한 메뉴에서. 켜짐 표시도 한다.
	s.AddButton(
		[] { return std::wstring(L"객체스냅 ▾"); },
		[this](const CRect& rc) {
			const uint32_t modes = OSnapModes();
			CMenu menu;
			menu.CreatePopupMenu();
			menu.AppendMenu(MF_STRING | (OSnapOn() ? MF_CHECKED : 0), 1000, L"객체스냅 켜기  (F3)");
			menu.AppendMenu(MF_SEPARATOR);
			for (const SnapMode& m : kSnapModes)
				menu.AppendMenu(MF_STRING | ((modes & m.bit) ? MF_CHECKED : 0), m.bit, m.name);
			const int picked = menu.TrackPopupMenu(TPM_RETURNCMD | TPM_BOTTOMALIGN | TPM_RIGHTALIGN, rc.right, rc.top, this);
			if (picked == 1000)    ToggleOSnap();
			else if (picked > 0)   CAD_SetOSnapModes(modes ^ (uint32_t)picked);   // 고른 종류 하나만 뒤집는다
		},
		L"객체스냅 — 끝점·중간점·중심점… 에 커서가 달라붙는다 (F3)\n누르면 켜기/끄기와 종류를 고른다",
		[] { return OSnapOn(); });
}

// F3 / F8 / F10 과 상태바 버튼이 같이 부른다. 상태는 엔진이 들고 있어 뒤집기만 하면 된다.
void CLotCADMFCDlg::ToggleOSnap()
{
	CAD_SetOSnapEnabled(!OSnapOn());
	m_statusBar.Refresh();
}

void CLotCADMFCDlg::ToggleOrthoTracking()
{
	CAD_SetOrthoEnabled(!OrthoOn());
	m_statusBar.Refresh();
}

void CLotCADMFCDlg::TogglePolarTracking()
{
	CAD_SetPolarTracking(!PolarOn(), 0.0);   // 0 이하 = 각도 증분(rad)은 지금 값 유지
	m_statusBar.Refresh();
}
