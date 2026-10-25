#pragma once
// 문자열 도우미 — CAD_* 는 UTF-8, MFC 유니코드 빌드는 UTF-16(wchar_t). 여러 파일이 같이 쓴다.
//
// ⚠️ 한글이 든 문자열을 CAD_* 에 바로 줄 때는 u8"…" 로 쓴다. 그냥 "…" 는 MSVC 가 시스템 코드 페이지(CP949)로
//    바꿔 넣어 엔진(UTF-8)에서 글자가 깨진다. (프로젝트에 /utf-8 을 켜도 되지만 샘플은 기본 설정 그대로 둔다.)

#include "../../../sdk/include/LotCAD_API.h"

#include <string>

inline std::wstring Utf8ToWide(const char* s)
{
	if (!s) return L"";
	const int n = MultiByteToWideChar(CP_UTF8, 0, s, -1, nullptr, 0);
	std::wstring out(n > 0 ? n - 1 : 0, L'\0');
	if (n > 1) MultiByteToWideChar(CP_UTF8, 0, s, -1, &out[0], n);
	return out;
}

inline std::string WideToUtf8(const std::wstring& s)
{
	const int n = WideCharToMultiByte(CP_UTF8, 0, s.c_str(), -1, nullptr, 0, nullptr, nullptr);
	std::string out(n > 0 ? n - 1 : 0, '\0');
	if (n > 1) WideCharToMultiByte(CP_UTF8, 0, s.c_str(), -1, &out[0], n, nullptr, nullptr);
	return out;
}

// 직전 CAD_* 호출이 실패한 이유 (없으면 빈 문자열)
inline std::wstring CadLastError()
{
	char buf[512] = {};
	CAD_GetLastError(buf, static_cast<uint32_t>(sizeof(buf)));
	return Utf8ToWide(buf);
}

// 메뉴·리본·패널 버튼이 명령을 시작할 때 — 진행 중인 명령·도구를 먼저 끝내고(선택은 그대로) 실행한다(오토캐드 ^C^C).
// CAD_ExecuteCommand 는 명령행에 친 것과 같아서, 선 그리던 중 "rect" 만 보내면 값으로 먹혀 도구가 안 바뀐다.
// 명령행 입력란·진행 중 도구에 값을 넣을 때는 CAD_ExecuteCommand 그대로.
inline CAD_Status CadStartCommand(const char* name)
{
	CAD_CancelCommand();
	return CAD_ExecuteCommand(name);
}

// JSON 을 넘겨 JSON 을 받는 함수(해석 CAD_WindTunnel · CAD_Water · CAD_StructuralAnalysis 등) — 2회 호출 규약.
// out=NULL 로 길이를 물을 때 **한 번 실행**하고, 같은 인자로 버퍼를 주면 다시 실행하지 않고 그 결과를 준다.
// 고정 버퍼로 먼저 불렀다 모자라 다시 부르면 start·run 이 두 번 들어간다("이미 도는 중") — 반드시 이 순서로.
// 실패면 빈 문자열(이유는 CadLastError()).
// 반환 = 전체 길이, 실패 = 음수 CAD_E_*.
using CadJsonFn = int32_t (*)(const char*, char*, uint32_t);
inline std::string CadCallJson(CadJsonFn fn, const std::string& argsJson)
{
	const int32_t need = fn(argsJson.c_str(), nullptr, 0);   // 길이를 물으며 실행
	if (need < 0) return {};
	std::string out(static_cast<size_t>(need) + 1, '\0');
	if (fn(argsJson.c_str(), &out[0], static_cast<uint32_t>(need) + 1) < 0) return {};   // 같은 인자 → 결과만
	out.resize(strlen(out.c_str()));
	return out;
}

// "2회 호출 규약" JSON 읽기 — 먼저 길이를 묻고, 그만큼 버퍼를 잡아 다시 부른다.
//   std::string json = CadReadJson(CAD_GetSectionStateJson);
template <class Fn>
std::string CadReadJson(Fn fn)
{
	const int n = fn(nullptr, 0);
	if (n <= 0) return {};
	std::string out(n + 1, '\0');
	fn(&out[0], n + 1);
	out.resize(strlen(out.c_str()));
	return out;
}
