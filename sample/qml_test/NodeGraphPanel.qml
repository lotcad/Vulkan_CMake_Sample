import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import LotCadQml

// 노드 그래프 패널 — GraphApi(graph_api.h). 엔진 그래프 편집기(ImGui)는 호스트 창에서 안 그려져 C API 로 같은 일을 한다.
// 노드 넣기 → 입력 값 → 잇기 → 엔진이 다음 프레임에 계산해 output 노드가 장면 객체를 만든다. 굽기 = 보통 객체로 떼어 내기.
ColumnLayout {
    id: root
    spacing: 8

    property int selected: -1        // 고른 노드 id

    function node(id) {
        var ns = GraphApi.nodes
        for (var i = 0; i < ns.length; ++i) if (ns[i].id === id) return ns[i]
        return null
    }
    readonly property var current: node(selected)
    readonly property var currentInput: current && inPort.currentIndex >= 0 ? current.inputs[inPort.currentIndex] : null
    readonly property var sources: GraphApi.nodes.filter(function (n) { return n.outputs && n.outputs.length > 0 })

    RowLayout {

        Layout.fillWidth: true
        Button { Layout.fillWidth: true; Layout.preferredWidth: 10; text: "예제"; onClicked: GraphApi.example() }
        Button { Layout.fillWidth: true; Layout.preferredWidth: 10; text: "계산"; onClicked: GraphApi.evaluate() }
        Button { Layout.fillWidth: true; Layout.preferredWidth: 10; text: "굽기"; onClicked: GraphApi.bake() }
        Button { Layout.fillWidth: true; Layout.preferredWidth: 10; text: "지우기"; onClicked: { GraphApi.clear(); root.selected = -1 } }
    }
    RowLayout {
        Layout.fillWidth: true
        ComboBox {
            id: kindBox
            Layout.fillWidth: true
            Layout.preferredWidth: 120
            model: GraphApi.kinds.map(function (k) { return k.group + " · " + k.kind })
        }
        Button {
            text: "넣기"
            onClicked: { var id = GraphApi.addNode(GraphApi.kinds[kindBox.currentIndex].kind); if (id >= 0) root.selected = id }
        }
    }

    ListView {
        Layout.fillWidth: true
        Layout.fillHeight: true
        clip: true
        model: GraphApi.nodes
        delegate: Rectangle {
            required property var modelData
            width: ListView.view.width
            height: 26
            color: root.selected === modelData.id ? "#3d5a80" : "transparent"
            MouseArea { anchors.fill: parent; onClicked: root.selected = modelData.id }
            RowLayout {
                Layout.fillWidth: true
                anchors.fill: parent
                anchors.leftMargin: 6
                anchors.rightMargin: 6
                Label { text: "#" + modelData.id; color: "#999" }
                Label { text: modelData.kind; color: "#e6e6e6"; Layout.fillWidth: true }
                Label { text: modelData.state; color: modelData.state.indexOf("오류") === 0 ? "#ff8a80" : "#9ccc65" }
            }
        }
    }

    GridLayout {
        columns: 2; columnSpacing: 6; rowSpacing: 4
        Layout.fillWidth: true
        enabled: root.current !== null

        Label { text: "입력"; color: "#bbb" }
        ComboBox {
            id: inPort
            Layout.fillWidth: true
            Layout.preferredWidth: 120
            model: root.current ? root.current.inputs.map(function (i) { return i.name + " (" + i.type + ")" + (i.linked ? "  ← 이어짐" : "") }) : []
        }
        Label { text: "값"; color: "#bbb" }
        RowLayout {
            Layout.fillWidth: true
            TextField { id: valueField; Layout.fillWidth: true; Layout.preferredWidth: 80; placeholderText: "숫자 · 참/거짓 · 글자 · 점 x,y,z"; selectByMouse: true }
            Button {
                text: "넣기"
                onClicked: if (root.currentInput) GraphApi.setValue(root.selected, root.currentInput.name, root.currentInput.type, valueField.text)
            }
        }
        Label { text: "이을 것"; color: "#bbb" }
        RowLayout {
            Layout.fillWidth: true
            ComboBox {
                id: fromNode
                Layout.fillWidth: true
                Layout.preferredWidth: 90
                model: root.sources.map(function (n) { return "#" + n.id + " " + n.kind })
            }
            ComboBox {
                id: fromPort
                Layout.preferredWidth: 80
                model: root.sources.length > fromNode.currentIndex && fromNode.currentIndex >= 0
                       ? root.sources[fromNode.currentIndex].outputs.map(function (o) { return o.name }) : []
            }
        }
    }
    RowLayout {
        Layout.fillWidth: true
        enabled: root.currentInput !== null
        Button { Layout.fillWidth: true; Layout.preferredWidth: 10
            text: "잇기"
            onClicked: GraphApi.connectPorts(root.sources[fromNode.currentIndex].id, fromPort.currentText,
                                             root.selected, root.currentInput.name)   // 종류가 다르거나 고리면 거절
        }
        Button { Layout.fillWidth: true; Layout.preferredWidth: 10; text: "끊기"; onClicked: GraphApi.disconnectPort(root.selected, root.currentInput.name) }
        Button { Layout.fillWidth: true; Layout.preferredWidth: 10; text: "노드 지우기"; onClicked: { GraphApi.removeNode(root.selected); root.selected = -1 } }
    }

    Label { Layout.fillWidth: true; text: GraphApi.summary; color: "#bbb" }
    Label { Layout.fillWidth: true; visible: text !== ""; text: GraphApi.message; color: "#ddd"; wrapMode: Text.Wrap }
}
