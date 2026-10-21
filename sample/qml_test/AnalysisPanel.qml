import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import LotCadQml

// 해석 패널 — 바람 터널 · 물 · 구조 해석. 엔진 해석 패널(ImGui)이 호스트 창에선 안 그려져 그 일을 여기서 한다.
//
// 모든 버튼은 AnalysisApi.call(종류, {"op": …}) 하나로 간다 — MCP 도구 wind_tunnel·water·structural_analysis 와
// 같은 op·인자라 헤더(LotCAD_API.h)의 해석 주석을 그대로 따르면 된다. 상태는 Main.qml 의 Timer 가 refresh() 로 읽는다.
//
// 흐름
//   바람 터널: 솔리드 선택 → 시작(다음 프레임에 켜짐) → 단면·연기·표면 압력으로 보기. 바람은 +X.
//   물:        닫힌 솔리드(그릇) 선택 → 물 높이 → 시작 → 기울이기·흔들기
//   구조 해석: 솔리드 선택 → 열기(면 목록이 온다) → 면 골라 고정·하중 → 실행(작업 스레드) → 결과·색 보기
ColumnLayout {
    id: root
    spacing: 8

    property string page: "wind"            // wind | water | sim — 리본·메뉴가 정한다
    property int    selectedFace: -1         // 구조 해석 면 목록에서 고른 면
    property string note: ""                 // 호스트 쪽 안내(선택 없음 등) — 엔진 오류는 AnalysisApi.lastError

    readonly property var wind:  AnalysisApi.wind
    readonly property var water: AnalysisApi.water
    readonly property var sim:   AnalysisApi.sim

    function call(which, args) { note = ""; return AnalysisApi.call(which, args) }
    function selection() {
        var ids = AnalysisApi.selectedIds()
        if (ids.length === 0) note = "3D 뷰에서 대상 솔리드를 먼저 선택하세요"
        return ids
    }
    function num(v, digits) { return v === undefined || v === null ? "-" : Number(v).toFixed(digits) }
    // 법선 → "+Z" 처럼(축에 거의 맞으면), 아니면 숫자 셋
    function axisName(n) {
        if (!n) return ""
        var names = ["X", "Y", "Z"]
        for (var i = 0; i < 3; ++i)
            if (Math.abs(n[i]) > 0.98) return (n[i] > 0 ? "+" : "−") + names[i]
        return "(" + n.map(function (c) { return c.toFixed(2) }).join(", ") + ")"
    }
    function conditionsOn(face) {
        var out = []
        var all = (sim.conditions || []).concat(sim.heat_conditions || [])
        for (var i = 0; i < all.length; ++i) if (all[i].face === face) out.push(all[i].kind)
        return out.join("·")
    }

    TabBar {
        id: tabs
        Layout.fillWidth: true
        currentIndex: root.page === "water" ? 1 : root.page === "sim" ? 2 : 0
        onCurrentIndexChanged: root.page = ["wind", "water", "sim"][currentIndex]
        TabButton { text: "바람 터널" }
        TabButton { text: "물" }
        TabButton { text: "구조 해석" }
    }

    ScrollView {
        Layout.fillWidth: true
        Layout.fillHeight: true
        contentWidth: availableWidth
        clip: true

        StackLayout {
            width: parent.width
            currentIndex: tabs.currentIndex

            // ══ 바람 터널 ══
            ColumnLayout {
                spacing: 6
                Label {
                    Layout.fillWidth: true; wrapMode: Text.Wrap; color: "#ddd"
                    text: wind.active ? "켜짐 — 솔리드 " + (wind.ids || []).length + "개 둘레, 바람 +X"
                        : wind.starting ? "켜는 중…" : "꺼짐 — 솔리드를 선택하고 시작"
                }
                RowLayout {
                    Label { text: "격자"; color: "#bbb" }
                    ComboBox {
                        id: windGrid; Layout.fillWidth: true
                        textRole: "text"; valueRole: "value"
                        model: [{ text: "빠름", value: "fast" }, { text: "보통", value: "normal" }, { text: "정밀", value: "fine" }]
                    }
                }
                Label { text: "바람 세기 " + windSpeed.value.toFixed(3) + "  (격자 단위 0.02 ~ 0.10)"; color: "#bbb" }
                Slider {
                    id: windSpeed; Layout.fillWidth: true
                    from: 0.02; to: 0.10; value: 0.06
                    onMoved: if (wind.active) root.call("wind", { op: "wind", value: value })
                }
                GridLayout {
                    columns: 2; columnSpacing: 6; rowSpacing: 4
                    Layout.fillWidth: true
                    Button { Layout.fillWidth: true;
                        text: "시작"; enabled: !wind.active
                        onClicked: {
                            var ids = root.selection()
                            if (ids.length) root.call("wind", { op: "start", ids: ids, grid: windGrid.currentValue, wind: windSpeed.value })
                        }
                    }
                    Button { Layout.fillWidth: true; text: "정지"; enabled: wind.active === true; onClicked: root.call("wind", { op: "stop" }) }
                    Button { Layout.fillWidth: true;
                        text: wind.flowing === false ? "재생" : "일시정지"; enabled: wind.active === true
                        onClicked: root.call("wind", { op: wind.flowing === false ? "play" : "pause" })
                    }
                    Button { Layout.fillWidth: true; text: "초기화"; enabled: wind.active === true; onClicked: root.call("wind", { op: "reset" }) }
                }

                Label { text: "보기"; color: "#ddd"; font.bold: true; Layout.topMargin: 6 }
                RowLayout {
                    Label { text: "색"; color: "#bbb" }
                    ComboBox {
                        Layout.fillWidth: true
                        textRole: "text"; valueRole: "value"
                        model: [{ text: "속도", value: "speed" }, { text: "압력", value: "pressure" },
                                { text: "소용돌이", value: "vortex" }, { text: "연기", value: "smoke" }]
                        onActivated: root.call("wind", { op: "view", field: currentValue })
                    }
                }
                RowLayout {
                    Label { text: "단면"; color: "#bbb" }
                    ComboBox {
                        id: windPlane; Layout.fillWidth: true
                        model: ["X", "Y", "Z"]; currentIndex: 1
                        onActivated: root.call("wind", { op: "view", plane: ["x", "y", "z"][index], at: windAt.value })
                    }
                }
                Label { text: "단면 위치 " + Math.round(windAt.value * 100) + "%"; color: "#bbb" }
                Slider {
                    id: windAt; Layout.fillWidth: true
                    from: 0; to: 1; value: 0.5
                    onMoved: root.call("wind", { op: "view", plane: ["x", "y", "z"][windPlane.currentIndex], at: value })
                }
                CheckBox { text: "표면 압력 색"; onToggled: root.call("wind", { op: "view", surface: checked }) }
                CheckBox { text: "연기"; onToggled: root.call("wind", { op: "view", smoke: checked }) }

                Label {
                    visible: wind.active === true
                    Layout.fillWidth: true; wrapMode: Text.Wrap; color: "#bbb"
                    text: "항력 계수 " + root.num(wind.drag_coefficient, 3)
                          + (wind.cells ? "   격자 " + wind.cells.join(" × ") : "")
                          + (wind.steps !== undefined ? "   단계 " + wind.steps : "")
                }
            }

            // ══ 물 ══
            ColumnLayout {
                spacing: 6
                Label {
                    Layout.fillWidth: true; wrapMode: Text.Wrap; color: "#ddd"
                    text: water.active ? "켜짐 — 그릇 #" + water.container
                        : water.starting ? "켜는 중…" : "꺼짐 — 닫힌 솔리드(그릇)를 선택하고 시작"
                }
                RowLayout {
                    Label { text: "격자"; color: "#bbb" }
                    ComboBox {
                        id: waterGrid; Layout.fillWidth: true
                        textRole: "text"; valueRole: "value"; currentIndex: 1
                        model: [{ text: "빠름", value: "fast" }, { text: "보통", value: "normal" }, { text: "정밀", value: "fine" }]
                    }
                }
                Label { text: "물 높이 " + Math.round(waterLevel.value * 100) + "%  (그릇 높이 기준)"; color: "#bbb" }
                Slider { id: waterLevel; Layout.fillWidth: true; from: 0.05; to: 0.95; value: 0.5 }
                GridLayout {
                    columns: 2; columnSpacing: 6; rowSpacing: 4
                    Layout.fillWidth: true
                    Button { Layout.fillWidth: true;
                        text: "시작"; enabled: !water.active
                        onClicked: {
                            var ids = root.selection()
                            if (ids.length) root.call("water", { op: "start", id: ids[0], level: waterLevel.value, grid: waterGrid.currentValue })
                        }
                    }
                    Button { Layout.fillWidth: true; text: "정지"; enabled: water.active === true; onClicked: root.call("water", { op: "stop" }) }
                    Button { Layout.fillWidth: true;
                        text: water.flowing === false ? "재생" : "일시정지"; enabled: water.active === true
                        onClicked: root.call("water", { op: water.flowing === false ? "play" : "pause" })
                    }
                    Button { Layout.fillWidth: true; text: "초기화"; enabled: water.active === true; onClicked: root.call("water", { op: "reset" }) }
                }

                Label { text: "기울이기 X " + Math.round(tiltX.value) + "°   Y " + Math.round(tiltY.value) + "°"; color: "#bbb"; Layout.topMargin: 6 }
                Slider { id: tiltX; Layout.fillWidth: true; from: -40; to: 40; value: 0; enabled: water.active === true
                         onMoved: root.call("water", { op: "tilt", x: value, y: tiltY.value }) }
                Slider { id: tiltY; Layout.fillWidth: true; from: -40; to: 40; value: 0; enabled: water.active === true
                         onMoved: root.call("water", { op: "tilt", x: tiltX.value, y: value }) }

                Label { text: "흔들기 세기 " + Math.round(shakeAmp.value * 100) + "% (중력 기준)"; color: "#bbb" }
                Slider { id: shakeAmp; Layout.fillWidth: true; from: 0.05; to: 1.0; value: 0.3 }
                RowLayout {
                    // 주기를 비우면 엔진이 첫 출렁임 공진 주기로 흔든다
                    Button { text: "흔들기(공진)"; enabled: water.active === true
                             onClicked: root.call("water", { op: "shake", amplitude: shakeAmp.value }) }
                    Button { text: "멈춤"; enabled: water.active === true
                             onClicked: root.call("water", { op: "shake", amplitude: 0 }) }
                }
                Label {
                    visible: water.active === true
                    Layout.fillWidth: true; wrapMode: Text.Wrap; color: "#bbb"
                    text: (water.cells ? "격자 " + water.cells.join(" × ") + "   " : "")
                          + "질량 오차 " + root.num((water.mass_drift || 0) * 100, 4) + "%"
                }
            }

            // ══ 구조 해석 ══
            ColumnLayout {
                id: simPage
                spacing: 6
                readonly property string type: sim.type || "stress"
                readonly property bool   open: (sim.faces || []).length > 0

                RowLayout {
                    Button {
                        text: "선택한 솔리드로 열기"
                        onClicked: {
                            var ids = root.selection()
                            if (ids.length) { root.selectedFace = -1; root.call("sim", { op: "open", id: ids[0] }) }
                        }
                    }
                    Button { text: "닫기"; enabled: simPage.open; onClicked: { root.selectedFace = -1; root.call("sim", { op: "close" }) } }
                }

                GridLayout {
                    columns: 2; columnSpacing: 6; rowSpacing: 4
                    Layout.fillWidth: true
                    Label { text: "종류"; color: "#bbb" }
                    ComboBox {
                        Layout.fillWidth: true; textRole: "text"; valueRole: "value"
                        model: [{ text: "응력", value: "stress" }, { text: "열전도", value: "heat" },
                                { text: "진동 모드", value: "modal" }, { text: "좌굴", value: "buckling" }]
                        currentIndex: Math.max(0, ["stress", "heat", "modal", "buckling"].indexOf(sim.type || "stress"))
                        onActivated: root.call("sim", { op: "set", type: currentValue })
                    }
                    Label { text: "재료"; color: "#bbb" }
                    ComboBox {
                        Layout.fillWidth: true; textRole: "text"; valueRole: "value"
                        model: [{ text: "강철(S275)", value: "steel" }, { text: "알루미늄(6061-T6)", value: "aluminum" },
                                { text: "스테인리스", value: "stainless" }, { text: "티타늄", value: "titanium" }, { text: "ABS", value: "abs" }]
                        currentIndex: Math.max(0, ["steel", "aluminum", "stainless", "titanium", "abs"].indexOf(sim.material || "steel"))
                        onActivated: root.call("sim", { op: "set", material: currentValue })
                    }
                    Label { text: "요소"; color: "#bbb" }
                    ComboBox {
                        Layout.fillWidth: true; textRole: "text"; valueRole: "value"
                        model: [{ text: "빠름", value: "fast" }, { text: "보통", value: "normal" }, { text: "정밀", value: "fine" }]
                        currentIndex: Math.max(0, ["fast", "normal", "fine"].indexOf(sim.size || "normal"))
                        onActivated: root.call("sim", { op: "set", size: currentValue })
                    }
                }

                Label { text: "면 — 골라서 조건을 건다"; color: "#ddd"; font.bold: true; visible: simPage.open }
                ListView {
                    id: faceList
                    visible: simPage.open
                    Layout.fillWidth: true
                    Layout.preferredHeight: Math.min(contentHeight, 150)
                    clip: true
                    model: sim.faces || []
                    delegate: ItemDelegate {
                        required property var modelData
                        width: ListView.view.width
                        height: 24
                        highlighted: root.selectedFace === modelData.index
                        onClicked: root.selectedFace = modelData.index
                        contentItem: Text {
                            color: highlighted ? "#ffffff" : "#ccc"
                            font.pixelSize: 12
                            verticalAlignment: Text.AlignVCenter
                            text: "면 " + modelData.index + "   " + root.axisName(modelData.normal)
                                  + "   넓이 " + Number(modelData.area).toPrecision(3)
                                  + (root.conditionsOn(modelData.index) ? "   [" + root.conditionsOn(modelData.index) + "]" : "")
                        }
                    }
                }

                // 하중 조건 — 응력·진동·좌굴
                ColumnLayout {
                    visible: simPage.open && simPage.type !== "heat"
                    enabled: root.selectedFace >= 0
                    spacing: 4
                    RowLayout {
                        Button { text: "고정"; onClicked: root.call("sim", { op: "fix", face: root.selectedFace }) }
                        Button { text: "풀기"; onClicked: root.call("sim", { op: "free", face: root.selectedFace }) }
                    }
                    RowLayout {
                        Label { text: "힘 N"; color: "#bbb" }
                        Num { id: fx; text: "0" } Num { id: fy; text: "0" } Num { id: fz; text: "-1000" }
                        Button { text: "걸기"
                                 onClicked: root.call("sim", { op: "force", face: root.selectedFace,
                                                               force: [Number(fx.text), Number(fy.text), Number(fz.text)] }) }
                    }
                    RowLayout {
                        Label { text: "압력 MPa"; color: "#bbb" }
                        Num { id: pressure; text: "1" }
                        Button { text: "걸기"; onClicked: root.call("sim", { op: "pressure", face: root.selectedFace, value: Number(pressure.text) }) }
                    }
                }
                // 열 조건
                ColumnLayout {
                    visible: simPage.open && simPage.type === "heat"
                    enabled: root.selectedFace >= 0
                    spacing: 4
                    RowLayout {
                        Label { text: "온도 °C"; color: "#bbb" }
                        Num { id: temp; text: "80" }
                        Button { text: "걸기"; onClicked: root.call("sim", { op: "temp", face: root.selectedFace, value: Number(temp.text) }) }
                    }
                    RowLayout {
                        Label { text: "열 W"; color: "#bbb" }
                        Num { id: flux; text: "10" }
                        Button { text: "걸기"; onClicked: root.call("sim", { op: "flux", face: root.selectedFace, value: Number(flux.text) }) }
                    }
                    RowLayout {
                        Label { text: "대류 h"; color: "#bbb" }
                        Num { id: convH; text: "10" }
                        Label { text: "주변 °C"; color: "#bbb" }
                        Num { id: convAmb; text: "20" }
                        Button { text: "걸기"
                                 onClicked: root.call("sim", { op: "convect", face: root.selectedFace,
                                                               h: Number(convH.text), ambient: Number(convAmb.text) }) }
                    }
                }

                GridLayout {
                    columns: 2; columnSpacing: 6; rowSpacing: 4
                    Layout.fillWidth: true
                    visible: simPage.open
                    Button { Layout.fillWidth: true; text: sim.busy ? "푸는 중…" : "실행"; enabled: !sim.busy; onClicked: root.call("sim", { op: "run" }) }
                    Button { Layout.fillWidth: true; text: "취소"; enabled: sim.busy === true; onClicked: root.call("sim", { op: "cancel" }) }
                    Button { Layout.fillWidth: true; text: "수렴 확인"; enabled: !sim.busy && sim.result !== undefined
                             onClicked: root.call("sim", { op: "converge" }) }
                    Button { Layout.fillWidth: true; text: "지우기"; enabled: !sim.busy; onClicked: root.call("sim", { op: "clear" }) }
                }
                BusyIndicator { visible: sim.busy === true; running: visible; Layout.alignment: Qt.AlignHCenter }

                // 결과 색 — 종류마다 고를 수 있는 것이 다르다
                RowLayout {
                    visible: sim.result !== undefined && sim.result !== null
                    Label { text: "색"; color: "#bbb" }
                    ComboBox {
                        id: showBox
                        Layout.fillWidth: true; textRole: "text"; valueRole: "value"
                        model: simPage.type === "heat"
                               ? [{ text: "온도", value: "temp" }, { text: "열 흐름", value: "flux" }]
                               : simPage.type === "stress"
                                 ? [{ text: "응력", value: "stress" }, { text: "변위", value: "disp" }, { text: "안전율", value: "safety" }]
                                 : [1, 2, 3, 4, 5, 6].map(function (k) { return { text: "모드 " + k, value: "mode " + k } })
                        onActivated: root.call("sim", { op: "set", show: currentValue })
                    }
                }

                Label {
                    visible: sim.result !== undefined && sim.result !== null
                    Layout.fillWidth: true; wrapMode: Text.Wrap; color: "#e6e6e6"
                    text: {
                        var r = sim.result
                        if (!r) return ""
                        if (r.kind === "stress")
                            return "최대 응력 " + root.num(r.max_von_mises_mpa, 4) + " MPa\n"
                                 + "최대 변위 " + root.num(r.max_displacement_mm, 6) + " mm\n"
                                 + "안전율 " + root.num(r.safety_factor, 1) + "\n"
                                 + "자유도 " + r.dofs
                        if (r.kind === "heat")
                            return "온도 " + root.num(r.min_temperature, 1) + " ~ " + root.num(r.max_temperature, 1) + " °C\n"
                                 + "최대 열유속 " + root.num(r.max_flux_w_m2, 1) + " W/m²"
                        if (r.kind === "modal")
                            return "고유진동수 Hz\n" + (r.frequencies_hz || []).map(function (f, i) { return "  " + (i + 1) + ")  " + f.toFixed(1) }).join("\n")
                        if (r.kind === "buckling")
                            return "좌굴 배수 (가한 하중 × 배수 = 좌굴 하중)\n" + (r.load_factors || []).map(function (f, i) { return "  " + (i + 1) + ")  " + f.toFixed(2) }).join("\n")
                        return JSON.stringify(r)
                    }
                }
            }
        }
    }

    Label {
        Layout.fillWidth: true
        visible: text !== ""
        text: root.note !== "" ? root.note : AnalysisApi.lastError
        color: "#ff8a80"
        wrapMode: Text.Wrap
    }

    // 숫자 한 칸(좁게) — 힘·온도 입력
    component Num : TextField {
        Layout.preferredWidth: 58
        selectByMouse: true
        validator: DoubleValidator {}
    }
}
