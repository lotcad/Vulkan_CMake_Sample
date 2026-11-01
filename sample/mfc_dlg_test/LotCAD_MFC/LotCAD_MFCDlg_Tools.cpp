// LotCAD_MFCDlg_Tools.cpp: 도구 탭 — 분해도 · 메시 수리 패널, 이미지 붙이기, 노드 그래프, 엔진 이벤트
//
//  분해도   CAD_ExplodeView(JSON → JSON, 2회 호출 규약 — CadCallJson). op: status · solve · auto · clear · amount · play · back ·
//           balloons · bom. 대상 = 선택한 솔리드, 없으면 보이는 솔리드 전부. 분해 막대·풍선·부품표는 엔진이 3D 뷰에 그린다.
//  메시 수리 CAD_CheckMesh · CAD_RepairMeshes · Smooth · Decimate · Stitch · Thicken · Remesh — 반환 = 바꾼 메시 수(음수 = 이유 코드).
//  이미지   붙이기는 파일을 호스트가 고르고 CAD_AttachImageFromFile. 회전·뒤집기·배경 지우기·자르기는 엔진 명령(선택한 이미지에).
//  노드 그래프 명령 graph on|off — 그래프 칸은 엔진이 Vulkan 으로 그리는 오버레이라 호스트 창 안에서도 보인다.
//  이벤트   CAD_AddEventListener — 명령이 끝날 때 만든·지운 객체 수를 명령행 기록에 남긴다.

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
	// 분해도 한 번 — 결과 JSON(ok · error · t · steps · parts · animating …)
	MiniJson::Value Explode(const std::string& argsJson)
	{
		return MiniJson::Parse(CadCallJson(CAD_ExplodeView, argsJson));
	}

	std::string IdsJson(const std::vector<uint32_t>& ids)
	{
		std::string s = "[";
		for (size_t i = 0; i < ids.size(); ++i) s += (i ? "," : "") + std::to_string(ids[i]);
		return s + "]";
	}

	// 메시 함수 결과 — 반환 = 바꾼 메시 수(0 = 고칠 것 없음), 음수 = 이유 코드
	std::wstring MeshResult(const wchar_t* what, int32_t changed)
	{
		if (changed < 0) return std::wstring(what) + L" 실패: " + CadLastError();
		if (changed == 0) return std::wstring(what) + L": 바꾼 메시 없음 (이미 괜찮거나 해당 없음)";
		return std::wstring(what) + L": 메시 " + std::to_wstring(changed) + L"개를 바꿨습니다";
	}
}


// ── 분해도 ──────────────────────────────────────────────────────────────
// 조립품(솔리드 여럿)을 빠지는 방향·순서대로 펼친다. 분해 정도 t = 0(조립) ~ 1(다 펼침).

void CLotCADMFCDlg::OpenExplodePanel()
{
	struct State {
		int amountSlider = 0;
		std::wstring msg = L"솔리드 여럿을 열고 '자동 순서' 를 누른다 (선택이 있으면 그것만)";
	};
	auto st = std::make_shared<State>();

	// 대상 — 선택이 있으면 그 id 들, 없으면 엔진이 보이는 솔리드 전부를 고른다
	auto withTargets = [](const char* op) {
		const std::vector<uint32_t> ids = CadSelectedIds();
		return std::string("{\"op\":\"") + op + "\"" + (ids.empty() ? "" : ",\"ids\":" + IdsJson(ids)) + "}";
	};
	auto run = [st](const wchar_t* what, const std::string& args) {
		const MiniJson::Value r = Explode(args);
		st->msg = r["ok"].Bool() ? std::wstring(what) : std::wstring(what) + L" 실패: " + Utf8ToWide(r["error"].str.c_str());
		return r;
	};

	CToolPanel& p = m_panel;
	p.Open(L"분해도 — 조립품 펼치기", kPanelExplode);

	p.AddSection(L"방향·순서");
	p.AddButton(L"자동 순서 — 걸리지 않고 빠지는 방향", [st, withTargets, run] {
		const MiniJson::Value r = run(L"자동 순서", withTargets("solve"));
		if (r["ok"].Bool())
			st->msg = L"단계 " + std::to_wstring(r["solved_steps"].Int(0)) + L"개로 풀었습니다" +
			          (r["unsolved"].Int(0) > 0 ? L" (못 뺀 부품 " + std::to_wstring(r["unsolved"].Int(0)) + L"개)" : L"");
	});
	p.AddButtonRow({
		{ L"방사형", [withTargets, run] { run(L"방사형으로 펼침", withTargets("auto")); } },
		{ L"지우기", [withTargets, run] { run(L"분해 방향을 지움", withTargets("clear")); } },
	});

	p.AddSection(L"펼치기");
	st->amountSlider = p.AddSlider(L"분해 정도 (%)", 0, 100, 0, 0, [run](float v) {
		char json[64];
		sprintf_s(json, "{\"op\":\"amount\",\"t\":%.3f}", v / 100);
		run(L"분해 정도", json);
	});
	p.AddButtonRow({
		{ L"펼치기 재생", [run] { run(L"펼치는 중", "{\"op\":\"play\",\"seconds\":2}"); } },
		{ L"조립 재생",   [run] { run(L"조립하는 중", "{\"op\":\"back\",\"seconds\":2}"); } },
	});

	p.AddSection(L"설명");
	p.AddToggle(L"품번 풍선", false, [run](bool on) {
		run(on ? L"풍선 켬" : L"풍선 끔", on ? "{\"op\":\"balloons\",\"show\":true}" : "{\"op\":\"balloons\",\"show\":false}");
	});
	p.AddToggle(L"부품표", false, [run](bool on) {
		run(on ? L"부품표 켬" : L"부품표 끔", on ? "{\"op\":\"bom\",\"show\":true}" : "{\"op\":\"bom\",\"show\":false}");
	});
	p.AddButton(L"부품표 CSV 저장...", [this, run] {
		CString path;
		if (!PickPath(true, _T("CSV (*.csv)|*.csv||"), path)) return;
		if (path.Right(4).CompareNoCase(_T(".csv")) != 0) path += _T(".csv");
		// JSON 문자열 안의 \ 는 \\ 로 — 윈도우 경로
		std::string utf8 = WideToUtf8((const wchar_t*)path), escaped;
		for (char c : utf8) { if (c == '\\' || c == '"') escaped += '\\'; escaped += c; }
		run(L"부품표를 저장했습니다", "{\"op\":\"bom\",\"path\":\"" + escaped + "\"}");
	});
	p.AddStatus(4);

	p.onTick = [this, st] {
		const MiniJson::Value s = Explode("{\"op\":\"status\"}");
		const double t = s["t"].Num();
		if (s["animating"].Bool()) m_panel.SetSliderValue(st->amountSlider, (float)(t * 100));   // 재생 중엔 막대가 따라간다
		wchar_t line[128];
		swprintf_s(line, L"\n\n분해 %.0f%% · 단계 %d · 부품 %d%s", t * 100, s["steps"].Int(0),
		           (int)s["parts"].Items().size(), s["animating"].Bool() ? L" · 재생 중" : L"");
		m_panel.SetStatus(st->msg + line);
	};
	p.onClose = [this] { RelayoutNow(); };
}


// ── 메시 수리 ────────────────────────────────────────────────────────────
// STL·OBJ·스캔 메시의 구멍·뒤집힌 면·틈을 고친다. 대상 = 선택한 메시(B-Rep 솔리드는 아님). 여럿이어도 되돌리기 1.

void CLotCADMFCDlg::OpenMeshPanel()
{
	struct State {
		bool noFill = false, flatFill = false;
		int smoothRow = 0, decimateRow = 0, stitchRow = 0, thickenRow = 0, remeshRow = 0;
		std::wstring msg = L"3D 뷰에서 메시를 선택하고 '검사' 부터";
	};
	auto st = std::make_shared<State>();

	// 선택한 메시에 하나 — 선택이 없으면 안내만
	auto apply = [st](const wchar_t* what, int32_t (*fn)(const uint32_t*, uint32_t, double), double value) {
		const std::vector<uint32_t> ids = CadSelectedIds();
		if (ids.empty()) { st->msg = L"먼저 3D 뷰에서 메시를 선택하세요"; return; }
		st->msg = MeshResult(what, fn(ids.data(), (uint32_t)ids.size(), value));
	};

	CToolPanel& p = m_panel;
	p.Open(L"메시 수리 — 구멍·뒤집힘·틈", kPanelMesh);

	p.AddSection(L"검사 · 수리");
	p.AddButton(L"검사", [st] {
		const std::vector<uint32_t> ids = CadSelectedIds();
		if (ids.empty()) { st->msg = L"먼저 3D 뷰에서 메시를 선택하세요"; return; }
		std::wstring text;
		for (size_t i = 0; i < ids.size() && i < 4; ++i) {
			CAD_MeshCheckInfo info{};
			info.size = sizeof(info);
			if (CAD_CheckMesh(ids[i], &info) != CAD_OK) { text += L"#" + std::to_wstring(ids[i]) + L": " + CadLastError() + L"\n"; continue; }
			wchar_t line[256];
			swprintf_s(line, L"#%u: 삼각형 %u · 구멍 %u · 열린 모서리 %u · 뒤집힘 %u · 덩어리 %u — %s\n",
			           ids[i], info.triangles, info.holes, info.openEdges, info.flippedEdges, info.components,
			           info.ok ? L"괜찮음" : info.closed ? L"닫힘(결함 있음)" : L"열림");
			text += line;
		}
		st->msg = text;
	});
	p.AddToggle(L"구멍은 메우지 않음", st->noFill, [st](bool v) { st->noFill = v; });
	p.AddToggle(L"구멍을 평평하게 (기본 = 둥글게)", st->flatFill, [st](bool v) { st->flatFill = v; });
	// 수리 = 같은 자리 정점 붙이기 → 퇴화·중복 제거 → 방향 통일 → 구멍 메움. 멀쩡한 메시는 건드리지 않는다
	p.AddButton(L"수리", [st] {
		const std::vector<uint32_t> ids = CadSelectedIds();
		if (ids.empty()) { st->msg = L"먼저 3D 뷰에서 메시를 선택하세요"; return; }
		CAD_MeshRepairOptions opt{};
		opt.size = sizeof(opt);
		opt.noFill = st->noFill;
		opt.flatFill = st->flatFill;
		st->msg = MeshResult(L"수리", CAD_RepairMeshes(ids.data(), (uint32_t)ids.size(), &opt));
	});

	p.AddSection(L"다듬기");
	st->smoothRow = p.AddNumbers(L"매끈하게 — 반복 1~500", { 5 }, L"적용", [this, st] {
		const std::vector<uint32_t> ids = CadSelectedIds();
		if (ids.empty()) { st->msg = L"먼저 3D 뷰에서 메시를 선택하세요"; return; }
		st->msg = MeshResult(L"매끈하게", CAD_SmoothMeshes(ids.data(), (uint32_t)ids.size(), (int32_t)m_panel.GetNumbers(st->smoothRow)[0]));
	});
	st->decimateRow = p.AddNumbers(L"삼각형 줄이기 — 남길 비율 0~1", { 0.5 }, L"적용", [this, st, apply] {
		apply(L"줄이기", CAD_DecimateMeshes, m_panel.GetNumbers(st->decimateRow)[0]);
	});
	st->stitchRow = p.AddNumbers(L"틈 꿰매기 — 허용치 mm (0 = 자동)", { 0 }, L"적용", [this, st, apply] {
		apply(L"꿰매기", CAD_StitchMeshes, m_panel.GetNumbers(st->stitchRow)[0]);
	});
	st->thickenRow = p.AddNumbers(L"두께 주기 — 열린 메시 → 솔리드, mm", { 2 }, L"적용", [this, st, apply] {
		apply(L"두께 주기", CAD_ThickenMeshes, m_panel.GetNumbers(st->thickenRow)[0]);
	});
	st->remeshRow = p.AddNumbers(L"다시 나누기 — 모서리 mm (0 = 평균)", { 0 }, L"적용", [this, st, apply] {
		apply(L"다시 나누기", CAD_RemeshMeshes, m_panel.GetNumbers(st->remeshRow)[0]);
	});
	p.AddStatus(5);

	p.onTick = [this, st] { m_panel.SetStatus(st->msg); };
	p.onClose = [this] { RelayoutNow(); };
}


// ── 이미지 붙이기 ────────────────────────────────────────────────────────
// 파일 선택은 호스트가(엔진의 imageattach 는 자기 파일 창을 띄운다). 원점에 긴 변 10 단위로 놓고 골라 둔다 —
// 이어서 리본의 회전·뒤집기·배경 지우기가 바로 그 이미지에 먹는다.

void CLotCADMFCDlg::AttachImage()
{
	CString path;
	if (!PickPath(false, _T("이미지 (*.png;*.jpg;*.jpeg;*.bmp)|*.png;*.jpg;*.jpeg;*.bmp|모든 파일 (*.*)|*.*||"), path)) return;
	uint32_t id = 0;
	// widthWorld 0 = 긴 변이 10 단위가 되게, origin = 왼쪽 아래. opt NULL = 기본 도면층·색
	if (CAD_AttachImageFromFile(WideToUtf8((const wchar_t*)path).c_str(), 0, CAD_GeVec3{ 0, 0, 0 }, nullptr, &id) != CAD_OK) {
		ReportFailure(_T("이미지 붙이기 실패"));
		return;
	}
	CAD_SetSelection(&id, 1, 0);   // 0 = 바꿔 고르기
	CAD_ZoomExtents();
	m_commandLine.AppendLog(L"이미지를 붙였습니다 — 리본 이미지 버튼으로 회전·뒤집기·배경 지우기");
}


// ── 노드 그래프 ──────────────────────────────────────────────────────────
// 1분할이면 2분할로 바꾸고 오른쪽 칸을 그래프로 쓴다. 노드 추가·연결은 그 칸에서 마우스(오른쪽 클릭 메뉴)로.

void CLotCADMFCDlg::ToggleGraph()
{
	m_graphOn = !m_graphOn;
	CadStartCommand(m_graphOn ? "graph on" : "graph off");
	m_view.SetFocus();
}


// ── 엔진 이벤트 ──────────────────────────────────────────────────────────
// 콜백은 엔진 스레드(= 이 UI 스레드, CAD_Tick 안)에서 프레임 끝에 불린다 — 안에서 창을 고쳐도 된다.
// 바로 끝나는 명령(cube 등)은 한 틱에 시작 → 끝 → 만들기 순으로 온다(만들기가 끝보다 늦다). 그래서 '끝' 에선 기록을
// 메시지로 미뤄 두고(PostMessage), 그 틱의 이벤트가 다 온 뒤 OnEventLog 에서 만든·지운 수를 적고 0 으로 돌린다.

void CLotCADMFCDlg::StartEvents()
{
	const uint32_t kinds = CAD_EVENT_OBJECT_CREATED | CAD_EVENT_OBJECT_DELETED |
	                       CAD_EVENT_COMMAND_STARTED | CAD_EVENT_COMMAND_ENDED | CAD_EVENT_COMMAND_CANCELLED;
	if (CAD_AddEventListener(kinds, &CLotCADMFCDlg::OnEngineEvent, this, 0, &m_eventHandle) != CAD_OK)   // 0 = 호스트
		m_eventHandle = 0;
}

void CLotCADMFCDlg::StopEvents()
{
	if (m_eventHandle) CAD_RemoveEventListener(m_eventHandle);
	m_eventHandle = 0;
}

void CLotCADMFCDlg::OnEngineEvent(int kind, uint32_t, void* user)
{
	CLotCADMFCDlg* self = static_cast<CLotCADMFCDlg*>(user);
	switch (kind) {
	case CAD_EVENT_OBJECT_CREATED: ++self->m_eventCreated; break;
	case CAD_EVENT_OBJECT_DELETED: ++self->m_eventDeleted; break;
	case CAD_EVENT_COMMAND_STARTED: {
		char name[64] = {};
		CAD_EdGetCommandName(name, (uint32_t)sizeof(name));   // 명령행에 친 첫 낱말(소문자)
		self->m_eventCommand = Utf8ToWide(name);
		break;
	}
	case CAD_EVENT_COMMAND_ENDED:
	case CAD_EVENT_COMMAND_CANCELLED:
		self->PostMessage(kEventLogMessage, kind == CAD_EVENT_COMMAND_CANCELLED ? 1 : 0);
		break;
	}
}

// 명령 하나가 끝난 뒤 — wParam 1 = 취소
LRESULT CLotCADMFCDlg::OnEventLog(WPARAM cancelled, LPARAM)
{
	if (cancelled)
		m_commandLine.AppendLog(L"[이벤트] " + m_eventCommand + L" 취소");
	else if (m_eventCreated || m_eventDeleted)
		m_commandLine.AppendLog(L"[이벤트] " + m_eventCommand + L" 끝 — 만든 객체 " + std::to_wstring(m_eventCreated) +
		                        L" · 지운 객체 " + std::to_wstring(m_eventDeleted));
	m_eventCreated = m_eventDeleted = 0;
	return 0;
}
