import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import LotCadQml

// 도면층 · 선종류 · 블록 패널 — LayersApi(layers_api.h). 엔진 패널(ImGui)은 호스트 창에서 안 그려져 여기서 한다.
// 목록은 Main.qml 의 Timer 가 LayersApi.refresh() 로 맞춘다(객체 수·선택 수는 3D 뷰에서도 바뀐다).
ColumnLayout {
    id: root
    spacing: 8

    property string page: "layers"     // layers | linetypes | blocks — 리본·메뉴가 정한다
    property int    current: -1        // 고른 도면층 id

    function layerById(id) {
        var ls = LayersApi.layers
        for (var i = 0; i < ls.length; ++i) if (ls[i].id === id) return ls[i]
        return null
    }
    function linetypeIndex(id) {
        var lt = LayersApi.linetypes
        for (var i = 0; i < lt.length; ++i) if (lt[i].id === id) return i
        return 0
    }

    TabBar {
        id: tabs
        Layout.fillWidth: true
        currentIndex: ["layers", "linetypes", "blocks"].indexOf(root.page)
        onCurrentIndexChanged: root.page = ["layers", "linetypes", "blocks"][currentIndex]
        TabButton { text: "도면층" }
        TabButton { text: "선종류" }
        TabButton { text: "블록" }
    }

    StackLayout {
        Layout.fillWidth: true
        Layout.fillHeight: true
        currentIndex: tabs.currentIndex

        // ══ 도면층 ══ — 줄을 누르면 고르고, ●/🔒/색 칸을 누르면 바뀐다
        ColumnLayout {
            spacing: 6
            ListView {
                Layout.fillWidth: true
                Layout.fillHeight: true
                clip: true
                model: LayersApi.layers
                delegate: Rectangle {
                    required property var modelData
                    width: ListView.view.width
                    height: 28
                    color: root.current === modelData.id ? "#3d5a80" : "transparent"
                    MouseArea { anchors.fill: parent; onClicked: root.current = modelData.id }
                    RowLayout {
                        Layout.fillWidth: true
                        anchors.fill: parent
                        anchors.leftMargin: 6
                        anchors.rightMargin: 6
                        spacing: 8
                        Label {
                            text: modelData.visible ? "●" : "○"; color: "#ddd"
                            MouseArea { anchors.fill: parent; onClicked: LayersApi.setVisible(modelData.id, !modelData.visible) }
                        }
                        Label {
                            text: modelData.locked ? "🔒" : "🔓"; color: modelData.locked ? "#ddd" : "#666"
                            MouseArea { anchors.fill: parent; onClicked: LayersApi.setLocked(modelData.id, !modelData.locked) }
                        }
                        Rectangle {
                            width: 14; height: 14; radius: 2; border.color: "#888"
                            color: Qt.rgba(modelData.color[0], modelData.color[1], modelData.color[2], 1)
                            // 색 고르기 — 몇 가지 색을 돌아가며(QML 색 대화상자는 3D 뷰 뒤로 숨을 수 있다)
                            MouseArea {
                                anchors.fill: parent
                                onClicked: {
                                    var palette = ["#ffffff", "#ff5252", "#ffd740", "#69f0ae", "#40c4ff", "#7c4dff", "#ff80ab", "#cccccc"]
                                    var cur = Qt.rgba(modelData.color[0], modelData.color[1], modelData.color[2], 1)
                                    var k = 0
                                    for (var i = 0; i < palette.length; ++i) if (Qt.colorEqual(palette[i], cur)) k = i + 1
                                    LayersApi.setColor(modelData.id, palette[k % palette.length])
                                }
                            }
                        }
                        Label { text: modelData.name; color: "#e6e6e6"; Layout.fillWidth: true; elide: Text.ElideRight }
                        Label {
                            color: "#999"
                            text: modelData.objectCount + (modelData.selectedCount ? " (선택 " + modelData.selectedCount + ")" : "")
                        }
                    }
                }
            }
            RowLayout {
                Layout.fillWidth: true
                TextField { id: layerName; Layout.fillWidth: true; Layout.preferredWidth: 60; placeholderText: "이름"; selectByMouse: true }
                Button { text: "새로"; onClicked: { var id = LayersApi.createLayer(layerName.text); if (id >= 0) { root.current = id; layerName.text = "" } } }
                Button {
                    text: "이름"; enabled: root.current >= 0 && layerName.text !== ""
                    onClicked: { LayersApi.renameLayer(root.current, layerName.text); layerName.text = "" }   // 0 층은 고정이라 거절된다
                }
            }
            RowLayout {
                Layout.fillWidth: true
                enabled: root.current >= 0
                Label { text: "선종류"; color: "#bbb" }
                ComboBox {
                    Layout.fillWidth: true
                    Layout.preferredWidth: 80
                    model: LayersApi.linetypes
                    textRole: "name"; valueRole: "id"
                    currentIndex: root.layerById(root.current) ? root.linetypeIndex(root.layerById(root.current).linetypeId) : 0
                    onActivated: LayersApi.setLayerLinetype(root.current, currentValue)
                }
            }
            Button {
                Layout.fillWidth: true; enabled: root.current >= 0
                text: "선택한 객체를 이 도면층으로"
                onClicked: LayersApi.assignSelected(root.current, root.layerById(root.current).name)
            }
        }

        // ══ 선종류 ══
        ColumnLayout {
            spacing: 6
            RowLayout {
                Layout.fillWidth: true
                Label { text: "선종류"; color: "#bbb" }
                ComboBox { id: ltBox; Layout.fillWidth: true; Layout.preferredWidth: 80; model: LayersApi.linetypes; textRole: "name"; valueRole: "id" }
            }
            Button { Layout.fillWidth: true; text: "선택한 객체에 적용"; onClicked: LayersApi.applyLinetype(ltBox.currentValue) }
            Button { Layout.fillWidth: true; text: "선택한 객체를 도면층 선종류로(ByLayer)"; onClicked: LayersApi.applyByLayer() }
            RowLayout {
                Layout.fillWidth: true
                Label { text: "전체 축척(LTSCALE)"; color: "#bbb" }
                TextField { id: ltScale; Layout.fillWidth: true; Layout.preferredWidth: 60; text: "1.0"; validator: DoubleValidator { bottom: 0.0001 } }
                Button { text: "적용"; onClicked: LayersApi.setLinetypeScale(Number(ltScale.text)) }
            }
            Button { Layout.fillWidth: true; text: ".lin 불러오기 (명령 ltload)"; onClicked: LayersApi.loadLinetypes() }
            Item { Layout.fillHeight: true }
        }

        // ══ 블록 ══
        ColumnLayout {
            spacing: 6
            ListView {
                Layout.fillWidth: true
                Layout.fillHeight: true
                clip: true
                model: LayersApi.blocks
                delegate: Label {
                    required property var modelData
                    width: ListView.view.width
                    color: "#e6e6e6"
                    padding: 4
                    text: modelData.name + (modelData.xref ? "  (외부 참조)" : "")
                          + "   객체 " + modelData.objects + " · 삽입 " + modelData.references
                }
            }
            RowLayout {
                Layout.fillWidth: true
                TextField { id: blockName; Layout.fillWidth: true; Layout.preferredWidth: 60; placeholderText: "블록 이름"; selectByMouse: true }
                Button { text: "만들기"; onClicked: { LayersApi.createBlock(blockName.text); blockName.text = "" } }
            }
            Button { Layout.fillWidth: true; text: "선택한 삽입(INSERT) 분해"; onClicked: LayersApi.explodeSelected() }
        }
    }

    Label {
        Layout.fillWidth: true
        visible: text !== ""
        text: LayersApi.message
        color: "#bbb"
        wrapMode: Text.Wrap
    }
}
