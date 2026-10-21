#pragma once
// 아주 작은 JSON 읽기 — 해석 API 의 결과(상태·면 목록·결과)를 읽는 데 쓴다.
// 읽기만 한다(쓰기는 문자열을 직접 만든다). 실제 앱이라면 nlohmann/json 같은 파서를 쓰는 편이 낫다 —
// 샘플은 외부 라이브러리 없이 빌드되게 하려고 여기 둔다.
//
//   MiniJson::Value v = MiniJson::Parse(text);
//   if (v["active"].Bool()) …
//   for (const auto& f : v["faces"].Items()) f["index"].Int(), f["normal"][0].Num() …
//   v["drag_coefficient"].IsNull()   // 엔진은 아직 없는 값을 null 로 준다

#include <cstdlib>
#include <map>
#include <memory>
#include <string>
#include <vector>

namespace MiniJson
{
	struct Value
	{
		enum Type { Null, Bool_, Number, String, Array, Object } type = Null;
		bool                         b = false;
		double                       num = 0;
		std::string                  str;       // UTF-8
		std::vector<Value>           items;     // 배열
		std::map<std::string, Value> members;   // 객체

		bool IsNull() const { return type == Null; }
		bool Bool() const { return type == Bool_ && b; }
		bool IsFalse() const { return type == Bool_ && !b; }   // 키가 있고 false (없음·null 과 구분)
		double Num(double fallback = 0) const { return type == Number ? num : fallback; }
		int Int(int fallback = -1) const { return type == Number ? (int)num : fallback; }
		const std::vector<Value>& Items() const { return items; }
		bool Has(const char* key) const { return type == Object && members.count(key) != 0; }

		const Value& operator[](const char* key) const
		{
			static const Value none;
			if (type != Object) return none;
			auto it = members.find(key);
			return it == members.end() ? none : it->second;
		}
		const Value& operator[](size_t i) const
		{
			static const Value none;
			return (type == Array && i < items.size()) ? items[i] : none;
		}
		// v[0] 의 0 이 문자열 키(null 포인터)로도 읽혀 모호해지지 않게 int 를 따로 받는다
		const Value& operator[](int i) const { return (*this)[(size_t)(i < 0 ? items.size() : i)]; }
	};

	namespace detail
	{
		struct Parser
		{
			const char* p;
			const char* end;

			void Ws() { while (p < end && (*p == ' ' || *p == '\t' || *p == '\n' || *p == '\r')) ++p; }
			bool Eat(char c) { Ws(); if (p < end && *p == c) { ++p; return true; } return false; }

			static void PutUtf8(std::string& out, unsigned cp)
			{
				if (cp < 0x80) out += (char)cp;
				else if (cp < 0x800) { out += (char)(0xC0 | (cp >> 6)); out += (char)(0x80 | (cp & 0x3F)); }
				else if (cp < 0x10000) { out += (char)(0xE0 | (cp >> 12)); out += (char)(0x80 | ((cp >> 6) & 0x3F)); out += (char)(0x80 | (cp & 0x3F)); }
				else { out += (char)(0xF0 | (cp >> 18)); out += (char)(0x80 | ((cp >> 12) & 0x3F)); out += (char)(0x80 | ((cp >> 6) & 0x3F)); out += (char)(0x80 | (cp & 0x3F)); }
			}

			std::string Str()
			{
				std::string out;
				++p;   // "
				while (p < end && *p != '"') {
					if (*p == '\\' && p + 1 < end) {
						++p;
						switch (*p) {
						case 'n': out += '\n'; break;
						case 't': out += '\t'; break;
						case 'r': out += '\r'; break;
						case 'b': out += '\b'; break;
						case 'f': out += '\f'; break;
						case 'u': {
							unsigned cp = (unsigned)std::strtoul(std::string(p + 1, p + 5).c_str(), nullptr, 16);
							p += 4;
							if (cp >= 0xD800 && cp < 0xDC00 && p + 6 < end && p[1] == '\\' && p[2] == 'u') {   // 서로게이트 쌍
								unsigned lo = (unsigned)std::strtoul(std::string(p + 3, p + 7).c_str(), nullptr, 16);
								cp = 0x10000 + ((cp - 0xD800) << 10) + (lo - 0xDC00);
								p += 6;
							}
							PutUtf8(out, cp);
							break;
						}
						default: out += *p; break;   // \" \\ \/
						}
						++p;
					} else {
						out += *p++;
					}
				}
				++p;   // "
				return out;
			}

			Value Parse()
			{
				Value v;
				Ws();
				if (p >= end) return v;
				if (*p == '{') {
					v.type = Value::Object;
					++p;
					if (Eat('}')) return v;
					do {
						Ws();
						if (p >= end || *p != '"') return v;
						std::string key = Str();
						if (!Eat(':')) return v;
						v.members[key] = Parse();
					} while (Eat(','));
					Eat('}');
				} else if (*p == '[') {
					v.type = Value::Array;
					++p;
					if (Eat(']')) return v;
					do { v.items.push_back(Parse()); } while (Eat(','));
					Eat(']');
				} else if (*p == '"') {
					v.type = Value::String;
					v.str = Str();
				} else if (end - p >= 4 && std::string(p, p + 4) == "true") {
					v.type = Value::Bool_; v.b = true; p += 4;
				} else if (end - p >= 5 && std::string(p, p + 5) == "false") {
					v.type = Value::Bool_; v.b = false; p += 5;
				} else if (end - p >= 4 && std::string(p, p + 4) == "null") {
					p += 4;
				} else {
					char* stop = nullptr;
					v.num = std::strtod(p, &stop);
					if (stop == p) { ++p; return v; }   // 알 수 없는 글자 — 건너뛴다
					v.type = Value::Number;
					p = stop;
				}
				return v;
			}
		};
	}

	inline Value Parse(const std::string& text)
	{
		detail::Parser parser{ text.data(), text.data() + text.size() };
		return parser.Parse();
	}
}
