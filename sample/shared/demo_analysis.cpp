// 해석 — 바람 터널 · 물 · 구조 해석. 엔진 해석 패널(ImGui)은 호스트 창 안에서 안 그려져 그 일을 여기서 한다.
// 쓰는 API: CAD_WindTunnel · CAD_Water · CAD_StructuralAnalysis — {"op": …} JSON 을 받아 결과 JSON 을 준다
//           (MCP 도구 wind_tunnel · water · structural_analysis 와 같은 op·인자, 헤더 LotCAD_API.h 의 해석 주석).
//
// 해석 모듈(libLotCADSim · libLotCADCfd)은 엔진 라이브러리 옆(sdk/)에 있어야 한다 — 없으면 start·run 이 error 로 알려 준다.
//
// 호스트가 지킬 것(이 파일이 하는 것)
//   - 2회 호출 규약: out=NULL 로 길이를 먼저 묻고(이때 한 번 실행) 같은 인자로 버퍼를 넘긴다. 작은 버퍼로 먼저
//     불렀다가 모자라 다시 부르면 run·start 가 두 번 들어가 "이미 도는 중" 이 된다.
//   - 엔진이 아직 없는 값은 null 로 준다(켠 직후의 항력 계수 등) — 숫자로 바꾸기 전에 확인.
//   - 상태는 0.25초마다 {"op":"status"} 로 읽는다(켜짐·단계·풀이 끝은 엔진이 프레임마다 바꾼다).
#include "demo_internal.h"

// 만들기 줄임 — 새 C API(CAD_GeVec3 + 결과 코드 + outId)를 옛 꼴(숫자들 → id, 실패 0)로
namespace {
    uint32_t mkBox(double x, double y, double z, double sx, double sy, double sz) {
        uint32_t id = 0;
        CAD_CreateBox(CAD_GeVec3{x, y, z}, CAD_GeVec3{sx, sy, sz}, nullptr, &id);
        return id;
    }
    uint32_t mkCylinder(double x, double y, double z, double r, double h) {
        uint32_t id = 0;
        CAD_CreateCylinder(CAD_GeVec3{x, y, z}, r, h, nullptr, &id);
        return id;
    }
    uint32_t mkSphere(double x, double y, double z, double r) {
        uint32_t id = 0;
        CAD_CreateSphere(CAD_GeVec3{x, y, z}, r, nullptr, &id);
        return id;
    }
}

namespace demo {
namespace {

using AnalysisFn = int (*)(const char*, char*, int);

// 해석 API 한 번. 결과 JSON 원문을 주고, 실패면 err 에 이유(결과의 "error" 또는 GetLastError).
std::string analysisCall(AnalysisFn fn, const std::string& args, std::string& err) {
    const int n = fn(args.c_str(), nullptr, 0);   // 길이 — 이때 한 번 실행된다
    if (n < 0) { err = lastError(); return {}; }
    std::string s(static_cast<size_t>(n) + 1, '\0');
    if (fn(args.c_str(), &s[0], n + 1) < 0) { err = lastError(); return {}; }   // 같은 인자 → 다시 실행하지 않고 그 결과
    s.resize(static_cast<size_t>(n));
    err = jsonString(s, "error");
    return s;
}

// null·없는 값은 "-"
std::string num(const std::string& json, const std::string& path, const char* f) {
    const double v = jsonNumber(json, path, NAN);
    return std::isnan(v) ? "-" : fmt(f, v);
}

std::string cellsText(const std::string& json) {
    const std::vector<double> c = jsonNumbers(json, "cells");
    return c.size() == 3 ? fmt("%.0f × %.0f × %.0f", c[0], c[1], c[2]) : "-";
}

std::vector<uint32_t> selectedIds() {
    // 개수만 먼저(NULL, 0) 묻고 그만큼 칸을 잡아 한 번에 받는다
    std::vector<uint32_t> ids(static_cast<std::size_t>(std::max(0, CAD_GetSelection(nullptr, 0))));
    if (!ids.empty()) {
        const int32_t n = std::max(0, CAD_GetSelection(ids.data(), static_cast<uint32_t>(ids.size())));
        ids.resize(std::min<size_t>(static_cast<size_t>(n), ids.size()));
    }
    ids.erase(std::remove(ids.begin(), ids.end(), 0u), ids.end());
    return ids;
}

const std::vector<std::string> kGridNames = {"빠름", "보통", "정밀"};
const char* const kGrids[] = {"fast", "normal", "fine"};

// 세 데모의 공통 — 호출·오류·상태 폴링
class AnalysisDemo : public Demo {
public:
    void update(double dt) override {
        poll_ += dt;
        if (poll_ < 0.25) return;
        poll_ = 0;
        std::string err;
        const std::string st = analysisCall(fn(), "{\"op\":\"status\"}", err);
        if (!st.empty()) state_ = st;
        onStatus();
    }

protected:
    virtual AnalysisFn fn() const = 0;
    virtual void onStatus() {}

    // 조작 하나 — 실패하면 패널 아래 "오류" 줄에 남기고, 성공하면 상태를 바로 다시 읽는다
    void call(const std::string& args) {
        std::string err;
        analysisCall(fn(), args, err);
        error_ = err;
        poll_ = 1;   // 다음 update 에서 곧장 status
    }
    bool active() const { return jsonBool(state_, "active"); }
    bool starting() const { return jsonBool(state_, "starting"); }
    std::string idsJson(const std::vector<uint32_t>& ids) const {
        std::string s = "[";
        for (size_t i = 0; i < ids.size(); ++i) s += (i ? "," : "") + std::to_string(ids[i]);
        return s + "]";
    }
    // 대상 — 3D 뷰에서 고른 솔리드가 있으면 그것, 없으면 "예제 … 만들기" 로 만든 것
    std::vector<uint32_t> targets() const {
        std::vector<uint32_t> ids = selectedIds();
        if (ids.empty() && body_) ids.push_back(body_);
        return ids;
    }
    void errorLabel() { label("오류", [this] { return error_; }); }
    // 예제 모델 — 앞서 만든 예제는 지우고 새로. 불러온 모델이 없을 때 바로 해 보도록.
    void replaceExample(uint32_t id) {
        if (body_) CAD_DeleteObject(body_);
        body_ = id;
        CAD_SetSelection(nullptr, 0, CAD_SELECT_REPLACE);   // 선택 비우기 — 만든 객체가 선택돼 기즈모가 뜨지 않게
        CAD_ZoomExtents();
    }

    std::string state_, error_;
    double poll_ = 1;
    uint32_t body_ = 0;
};

// ── 바람 터널 ────────────────────────────────────────────────────────

class WindDemo : public AnalysisDemo {
public:
    const char* id() const override { return "wind"; }
    const char* title() const override { return "해석 — 바람 터널"; }
    const char* summary() const override { return "솔리드 둘레에 바람(+X)을 불어 속도·압력·소용돌이·연기와 항력 계수를 본다"; }

    void setup() override { makeBody(); CAD_SetView(3); }
    void teardown() override { call("{\"op\":\"stop\"}"); }

protected:
    AnalysisFn fn() const override { return CAD_WindTunnel; }
    void onStatus() override {
        status = active() ? "바람 터널 켜짐 — 항력 계수 " + num(state_, "drag_coefficient", "%.3f")
               : starting() ? "켜는 중…" : "꺼짐 — 3D 뷰에서 솔리드를 고르고 시작";
    }

    void buildControls() override {
        header("바람 터널 (CAD_WindTunnel)");
        label("대상", [] { return "3D 뷰에서 고른 솔리드(여럿 가능). 없으면 예제 모델"; });
        choice("예제 모양", {"원기둥", "상자", "구"}, [this] { return shape_; }, [this](int k) { shape_ = k; });
        button("예제 모델 만들기", [this] {
            if (active()) call("{\"op\":\"stop\"}");
            makeBody();
        });
        choice("격자", kGridNames, [this] { return grid_; }, [this](int k) { grid_ = k; });
        slider("바람 세기", "", 0.02f, 0.10f, [this] { return wind_; }, [this](float v) {
            wind_ = v;
            if (active()) call(fmt("{\"op\":\"wind\",\"value\":%.4f}", v));
        });
        button("시작", [this] {
            call(fmt("{\"op\":\"start\",\"ids\":%s,\"grid\":\"%s\",\"wind\":%.4f}",
                     idsJson(targets()).c_str(), kGrids[grid_], wind_));
        }, [this] { return !active() && !starting(); });
        button("정지", [this] { call("{\"op\":\"stop\"}"); }, [this] { return active(); });
        toggle("흐름 재생", [this] { return jsonBool(state_, "flowing", true); },
               [this](bool on) { call(on ? "{\"op\":\"play\"}" : "{\"op\":\"pause\"}"); });
        button("초기화", [this] { call("{\"op\":\"reset\"}"); }, [this] { return active(); });

        header("보기");
        choice("색", {"속도", "압력", "소용돌이", "연기"}, [this] { return field_; }, [this](int k) {
            static const char* f[] = {"speed", "pressure", "vortex", "smoke"};
            field_ = k;
            call(fmt("{\"op\":\"view\",\"field\":\"%s\"}", f[k]));
        });
        choice("단면", {"X", "Y", "Z"}, [this] { return plane_; }, [this](int k) { plane_ = k; viewPlane(); });
        slider("단면 위치", "", 0, 1, [this] { return at_; }, [this](float v) { at_ = v; viewPlane(); });
        toggle("표면 압력 색", [this] { return jsonBool(state_, "surface"); },
               [this](bool on) { call(fmt("{\"op\":\"view\",\"surface\":%s}", on ? "true" : "false")); });
        toggle("연기", [this] { return jsonBool(state_, "smoke"); },
               [this](bool on) { call(fmt("{\"op\":\"view\",\"smoke\":%s}", on ? "true" : "false")); });

        header("결과");
        label("항력 계수", [this] { return active() ? num(state_, "drag_coefficient", "%.3f") : "-"; });
        label("레이놀즈 수", [this] { return active() ? num(state_, "reynolds", "%.0f") : "-"; });
        label("격자", [this] { return active() ? cellsText(state_) : "-"; });
        errorLabel();
    }

private:
    void makeBody() {
        replaceExample(shape_ == 0 ? mkCylinder(0, 0, 0, 0.3f, 1.0f)
                     : shape_ == 1 ? mkBox(0, 0, 0.3f, 0.6f, 0.6f, 0.6f)
                                   : mkSphere(0, 0, 0.35f, 0.35f));
    }
    void viewPlane() {
        static const char* p[] = {"x", "y", "z"};
        call(fmt("{\"op\":\"view\",\"plane\":\"%s\",\"at\":%.3f}", p[plane_], at_));
    }

    int shape_ = 0, grid_ = 0, field_ = 0, plane_ = 1;
    float wind_ = 0.06f, at_ = 0.5f;
};

// ── 물 ───────────────────────────────────────────────────────────────

class WaterDemo : public AnalysisDemo {
public:
    const char* id() const override { return "water"; }
    const char* title() const override { return "해석 — 물"; }
    const char* summary() const override { return "닫힌 솔리드(그릇)에 물을 채우고 기울이기·흔들기(공진)로 출렁임을 본다"; }

    void setup() override { makeContainer(); CAD_SetView(3); }
    void teardown() override { call("{\"op\":\"stop\"}"); }

protected:
    AnalysisFn fn() const override { return CAD_Water; }
    void onStatus() override {
        status = active() ? "물 켜짐 — 격자 " + cellsText(state_)
               : starting() ? "켜는 중…" : "꺼짐 — 3D 뷰에서 닫힌 솔리드(그릇)를 고르고 시작";
    }

    void buildControls() override {
        header("물 (CAD_Water)");
        label("그릇", [] { return "3D 뷰에서 고른 닫힌 솔리드 — 그 안이 물 칸. 없으면 예제 그릇"; });
        button("예제 그릇 만들기", [this] {
            if (active()) call("{\"op\":\"stop\"}");
            makeContainer();
        });
        choice("격자", kGridNames, [this] { return grid_; }, [this](int k) { grid_ = k; });
        slider("물 높이", "", 0.05f, 0.95f, [this] { return level_; }, [this](float v) { level_ = v; });
        button("시작", [this] {
            const std::vector<uint32_t> ids = targets();
            if (ids.empty()) { error_ = "그릇(닫힌 솔리드)이 없습니다"; return; }
            call(fmt("{\"op\":\"start\",\"id\":%u,\"level\":%.3f,\"grid\":\"%s\"}", ids[0], level_, kGrids[grid_]));
        }, [this] { return !active() && !starting(); });
        button("정지", [this] { call("{\"op\":\"stop\"}"); }, [this] { return active(); });
        toggle("흐름 재생", [this] { return jsonBool(state_, "flowing", true); },
               [this](bool on) { call(on ? "{\"op\":\"play\"}" : "{\"op\":\"pause\"}"); });
        button("초기화", [this] { call("{\"op\":\"reset\"}"); }, [this] { return active(); });

        header("움직이기");
        slider("기울이기 X", "°", -40, 40, [this] { return tiltX_; }, [this](float v) { tiltX_ = v; tilt(); });
        slider("기울이기 Y", "°", -40, 40, [this] { return tiltY_; }, [this](float v) { tiltY_ = v; tilt(); });
        slider("흔들기 세기", "", 0.05f, 1.0f, [this] { return shake_; }, [this](float v) { shake_ = v; });
        // 주기를 비우면 엔진이 첫 출렁임 공진 주기로 흔든다
        button("흔들기(공진)", [this] { call(fmt("{\"op\":\"shake\",\"amplitude\":%.3f}", shake_)); },
               [this] { return active(); });
        button("흔들기 멈춤", [this] { call("{\"op\":\"shake\",\"amplitude\":0}"); }, [this] { return active(); });

        header("상태");
        label("격자", [this] { return active() ? cellsText(state_) : "-"; });
        label("질량 오차", [this] {
            const double d = jsonNumber(state_, "mass_drift", NAN);
            return active() && !std::isnan(d) ? fmt("%.4f %%", d * 100) : "-";
        });
        errorLabel();
    }

private:
    void makeContainer() { replaceExample(mkBox(0, 0, 0.4f, 1.2f, 0.6f, 0.8f)); }
    void tilt() {
        if (active()) call(fmt("{\"op\":\"tilt\",\"x\":%.2f,\"y\":%.2f}", tiltX_, tiltY_));
    }

    int grid_ = 1;
    float level_ = 0.5f, tiltX_ = 0, tiltY_ = 0, shake_ = 0.3f;
};

// ── 구조 해석 ────────────────────────────────────────────────────────

struct Face { int index; std::string text; std::vector<double> normal; };

class SimDemo : public AnalysisDemo {
public:
    const char* id() const override { return "sim"; }
    const char* title() const override { return "해석 — 구조 해석"; }
    const char* summary() const override {
        return "솔리드를 열고 면에 고정·하중을 걸어 응력·변위·안전율(또는 열·진동·좌굴)을 푼다. 예제: 외팔보";
    }

    void setup() override { makeBeam(); CAD_SetView(3); }
    void teardown() override { call("{\"op\":\"close\"}"); }

protected:
    AnalysisFn fn() const override { return CAD_StructuralAnalysis; }

    void onStatus() override {
        // 면 목록·해석 종류·결과 유무가 바뀌면 항목을 다시 만든다(면 선택지·하중/열 조건·색 선택지가 달라진다)
        faces_.clear();
        for (const std::string& f : jsonObjects(state_, "faces")) {
            const int i = static_cast<int>(jsonNumber(f, "index", -1));
            const std::vector<double> n = jsonNumbers(f, "normal");
            faces_.push_back({i, fmt("면 %d  %s  넓이 %.3g", i, axisName(n).c_str(), jsonNumber(f, "area")), n});
        }
        const std::string key = fmt("%zu|%s|%d", faces_.size(), type().c_str(), hasResult() ? 1 : 0);
        if (key != layoutKey_) { layoutKey_ = key; rebuild(); }

        if (busy()) status = "푸는 중…";
        else if (hasResult()) status = resultLine();
        else if (isOpen()) status = fmt("열림 — 면 %zu개, 조건 %zu개", faces_.size(), conditionCount());
        else status = "닫힘 — 3D 뷰에서 솔리드를 고르고 열기";
    }

    void buildControls() override {
        header("구조 해석 (CAD_StructuralAnalysis)");
        label("대상", [] { return "3D 뷰에서 고른 솔리드 하나. 없으면 예제 외팔보(3 × 0.4 × 0.4 m)"; });
        button("예제 외팔보 만들기", [this] {
            if (isOpen()) call("{\"op\":\"close\"}");
            makeBeam();
        });
        button("열기", [this] {
            const std::vector<uint32_t> ids = targets();
            if (ids.empty()) { error_ = "솔리드가 없습니다"; return; }
            face_ = 0;
            call(fmt("{\"op\":\"open\",\"id\":%u}", ids[0]));
        });
        button("닫기", [this] { call("{\"op\":\"close\"}"); }, [this] { return isOpen(); });
        choice("종류", {"응력", "열전도", "진동 모드", "좌굴"}, [this] { return indexOf(kTypes, type()); },
               [this](int k) { call(fmt("{\"op\":\"set\",\"type\":\"%s\"}", kTypes[k])); });
        choice("재료", {"강철(S275)", "알루미늄(6061-T6)", "스테인리스", "티타늄", "ABS"},
               [this] { return indexOf(kMaterials, jsonString(state_, "material")); },
               [this](int k) { call(fmt("{\"op\":\"set\",\"material\":\"%s\"}", kMaterials[k])); });
        choice("요소", kGridNames, [this] { return indexOf(kGrids, jsonString(state_, "size")); },
               [this](int k) { call(fmt("{\"op\":\"set\",\"size\":\"%s\"}", kGrids[k])); });
        if (!isOpen()) { errorLabel(); return; }

        header("면 조건");
        std::vector<std::string> names;
        for (const Face& f : faces_) names.push_back(f.text);
        choice("면", names, [this] { return face_; }, [this](int k) { face_ = k; });
        label("걸린 조건", [this] { return conditionsText(); });
        if (type() != "heat") {
            button("고정", [this] { call(fmt("{\"op\":\"fix\",\"face\":%d}", faceIndex())); });
            button("풀기", [this] { call(fmt("{\"op\":\"free\",\"face\":%d}", faceIndex())); });
            textField("힘 N (x, y, z)", [this] { return force_; }, [this](const std::string& s) { force_ = s; });
            button("힘 걸기", [this] {
                double x = 0, y = 0, z = 0;
                if (std::sscanf(force_.c_str(), "%lf , %lf , %lf", &x, &y, &z) != 3) { error_ = "힘은 x, y, z 세 숫자"; return; }
                call(fmt("{\"op\":\"force\",\"face\":%d,\"force\":[%g,%g,%g]}", faceIndex(), x, y, z));
            });
            textField("압력 MPa", [this] { return pressure_; }, [this](const std::string& s) { pressure_ = s; });
            button("압력 걸기", [this] {
                call(fmt("{\"op\":\"pressure\",\"face\":%d,\"value\":%g}", faceIndex(), std::atof(pressure_.c_str())));
            });
            button("예제 조건 — 왼끝 고정 · 오른끝 -5 kN", [this] { cantileverExample(); });
        } else {
            textField("온도 °C", [this] { return temp_; }, [this](const std::string& s) { temp_ = s; });
            button("온도 걸기", [this] {
                call(fmt("{\"op\":\"temp\",\"face\":%d,\"value\":%g}", faceIndex(), std::atof(temp_.c_str())));
            });
            textField("열 W", [this] { return flux_; }, [this](const std::string& s) { flux_ = s; });
            button("열 걸기", [this] {
                call(fmt("{\"op\":\"flux\",\"face\":%d,\"value\":%g}", faceIndex(), std::atof(flux_.c_str())));
            });
            textField("대류 h, 주변 °C", [this] { return convect_; }, [this](const std::string& s) { convect_ = s; });
            button("대류 걸기", [this] {
                double h = 0, amb = 0;
                if (std::sscanf(convect_.c_str(), "%lf , %lf", &h, &amb) != 2) { error_ = "대류는 h, 주변온도 두 숫자"; return; }
                call(fmt("{\"op\":\"convect\",\"face\":%d,\"h\":%g,\"ambient\":%g}", faceIndex(), h, amb));
            });
        }

        header("해석 실행");
        button("실행", [this] { call("{\"op\":\"run\"}"); }, [this] { return !busy(); });
        button("취소", [this] { call("{\"op\":\"cancel\"}"); }, [this] { return busy(); });
        button("수렴 확인 (요소 × 0.7)", [this] { call("{\"op\":\"converge\"}"); },
               [this] { return !busy() && hasResult(); });
        button("조건 지우기", [this] { call("{\"op\":\"clear\"}"); }, [this] { return !busy(); });
        if (hasResult()) {
            const std::vector<std::string> shows = showValues();
            std::vector<std::string> showNames;
            for (const std::string& s : shows) showNames.push_back(showName(s));
            choice("색", showNames, [this] { return show_; }, [this, shows](int k) {
                show_ = k;
                call(fmt("{\"op\":\"set\",\"show\":\"%s\"}", shows[static_cast<size_t>(k)].c_str()));
            });
        }
        label("결과", [this] { return resultText(); });
        errorLabel();
    }

private:
    static constexpr const char* kTypes[] = {"stress", "heat", "modal", "buckling"};
    static constexpr const char* kMaterials[] = {"steel", "aluminum", "stainless", "titanium", "abs"};
    template <size_t N> static int indexOf(const char* const (&list)[N], const std::string& v) {
        for (size_t i = 0; i < N; ++i) if (v == list[i]) return static_cast<int>(i);
        return 0;
    }

    std::string type() const { const std::string t = jsonString(state_, "type"); return t.empty() ? "stress" : t; }
    bool isOpen() const { return !faces_.empty(); }
    bool busy() const { return jsonBool(state_, "busy"); }
    bool hasResult() const { return !jsonString(state_, "result.kind").empty(); }
    int faceIndex() const {
        return face_ >= 0 && face_ < static_cast<int>(faces_.size()) ? faces_[static_cast<size_t>(face_)].index : -1;
    }
    size_t conditionCount() const {
        return jsonObjects(state_, "conditions").size() + jsonObjects(state_, "heat_conditions").size();
    }

    static std::string axisName(const std::vector<double>& n) {
        static const char* axes[] = {"X", "Y", "Z"};
        for (size_t i = 0; i < 3 && i < n.size(); ++i)
            if (std::fabs(n[i]) > 0.98) return std::string(n[i] > 0 ? "+" : "-") + axes[i];
        return n.size() == 3 ? fmt("(%.2f, %.2f, %.2f)", n[0], n[1], n[2]) : "?";
    }

    std::string conditionsText() const {
        std::string out;
        for (const char* list : {"conditions", "heat_conditions"})
            for (const std::string& c : jsonObjects(state_, list)) {
                if (!out.empty()) out += "\n";
                out += fmt("면 %d — ", static_cast<int>(jsonNumber(c, "face", -1))) + jsonString(c, "kind");
                const std::vector<double> f = jsonNumbers(c, "force");
                if (f.size() == 3) out += fmt(" (%g, %g, %g) N", f[0], f[1], f[2]);
                const double v = jsonNumber(c, "value", NAN);
                if (!std::isnan(v)) out += fmt(" %g", v);
            }
        return out.empty() ? "없음" : out;
    }

    void makeBeam() { replaceExample(mkBox(1.5f, 0, 0.2f, 3.0f, 0.4f, 0.4f)); }

    // 예제 — 법선이 -X 인 면 고정, +X 인 면에 아래로 5 kN. (리눅스 기준값: 최대 응력 ≈ 1.99 MPa · 변위 ≈ 0.101 mm · 안전율 ≈ 138)
    void cantileverExample() {
        int left = -1, right = -1;
        double lo = 2, hi = -2;
        for (const Face& f : faces_) {
            if (f.normal.size() != 3) continue;
            if (f.normal[0] < lo) { lo = f.normal[0]; left = f.index; }
            if (f.normal[0] > hi) { hi = f.normal[0]; right = f.index; }
        }
        if (left < 0 || right < 0 || left == right) { error_ = "X 방향 양 끝 면을 못 찾았습니다"; return; }
        call("{\"op\":\"clear\"}");
        call(fmt("{\"op\":\"fix\",\"face\":%d}", left));
        call(fmt("{\"op\":\"force\",\"face\":%d,\"force\":[0,0,-5000]}", right));
    }

    std::vector<std::string> showValues() const {
        const std::string k = jsonString(state_, "result.kind");
        if (k == "heat") return {"temp", "flux"};
        if (k == "stress") return {"stress", "disp", "safety"};
        std::vector<std::string> v;
        for (int i = 1; i <= 6; ++i) v.push_back(fmt("mode %d", i));
        return v;
    }
    static std::string showName(const std::string& s) {
        if (s == "temp") return "온도";
        if (s == "flux") return "열 흐름";
        if (s == "stress") return "응력";
        if (s == "disp") return "변위";
        if (s == "safety") return "안전율";
        return "모드 " + s.substr(5);
    }

    std::string resultLine() const {
        const std::string k = jsonString(state_, "result.kind");
        if (k == "stress")
            return "최대 응력 " + num(state_, "result.max_von_mises_mpa", "%.4g") + " MPa · 변위 "
                 + num(state_, "result.max_displacement_mm", "%.4g") + " mm · 안전율 "
                 + num(state_, "result.safety_factor", "%.1f");
        return "결과 — " + k;
    }
    std::string resultText() const {
        const std::string k = jsonString(state_, "result.kind");
        if (k.empty()) return busy() ? "푸는 중…" : "-";
        if (k == "stress")
            return "최대 응력 " + num(state_, "result.max_von_mises_mpa", "%.4g") + " MPa\n최대 변위 "
                 + num(state_, "result.max_displacement_mm", "%.4g") + " mm\n안전율 "
                 + num(state_, "result.safety_factor", "%.1f") + "\n자유도 " + num(state_, "result.dofs", "%.0f");
        if (k == "heat")
            return "온도 " + num(state_, "result.min_temperature", "%.1f") + " ~ "
                 + num(state_, "result.max_temperature", "%.1f") + " °C\n최대 열유속 "
                 + num(state_, "result.max_flux_w_m2", "%.1f") + " W/m²";
        const bool modal = k == "modal";
        const std::vector<double> v = jsonNumbers(state_, modal ? "result.frequencies_hz" : "result.load_factors");
        std::string out = modal ? "고유진동수 Hz" : "좌굴 배수 (가한 하중 × 배수 = 좌굴 하중)";
        for (size_t i = 0; i < v.size(); ++i) out += fmt(modal ? "\n  %zu)  %.1f" : "\n  %zu)  %.2f", i + 1, v[i]);
        return out;
    }

    std::vector<Face> faces_;
    int face_ = 0, show_ = 0;
    std::string layoutKey_;
    std::string force_ = "0, 0, -5000", pressure_ = "1", temp_ = "80", flux_ = "10", convect_ = "10, 20";
};

} // namespace

Demo* makeWindDemo() { return new WindDemo(); }
Demo* makeWaterDemo() { return new WaterDemo(); }
Demo* makeSimDemo() { return new SimDemo(); }

} // namespace demo
