"""노드 그래프 패널 — 오른쪽 독. 엔진 그래프 편집기(ImGui)는 호스트 창에서 안 그려져 C API 로 같은 일을 한다.

노드를 넣고(CAD_NodeGraphAddNode) 입력 값을 넣고(CAD_NodeGraphSetNumber·SetPoint …) 이으면(CAD_NodeGraphConnect)
엔진이 다음 프레임에 계산해 output 노드가 장면 객체를 만든다. 그래프를 고치면 그 객체도 따라 바뀐다.
"굽기"(CAD_NodeGraphBake)는 그 객체를 그래프에서 떼어 보통 객체로 남긴다.

노드 종류·포트는 CAD_NodeGraphGetKindsJson, 지금 그래프(노드·링크·오류·기다림)는 CAD_NodeGraphGetJson.
⚠️ 종류 목록은 엔진이 한 프레임 돈 뒤에 묻는다(그 전엔 엔진이 죽는다) — 패널을 처음 열 때 읽는다.
⚠️ CAD_ClearAll 은 다음 프레임에 그래프까지 지운다 — 그래프 예제 앞에서 장면을 비우지 않는다.
"""
import json

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (QComboBox, QFormLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget)

import lotcad
from layers import selected_ids as layers_selected


def button(text, slot):
    b = QPushButton(text)
    b.clicked.connect(slot)
    return b


def row(*widgets):
    w = QWidget()
    layout = QHBoxLayout(w)
    layout.setContentsMargins(0, 0, 0, 0)
    for x in widgets:
        layout.addWidget(x)
    return w


class NodeGraphPanel(QWidget):
    def __init__(self, log, parent=None):
        super().__init__(parent)
        self._log = log
        self.kinds = {}            # kind → {group, inputs, outputs}
        self.graph = {}            # CAD_NodeGraphGetJson
        self._graph_key = None
        self._next_x = 0.0

        self.kind_box = QComboBox()
        self.nodes = QTableWidget(0, 3)
        self.nodes.setHorizontalHeaderLabels(["#", "종류", "상태"])
        self.nodes.verticalHeader().hide()
        self.nodes.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.nodes.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.nodes.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.nodes.horizontalHeader().setStretchLastSection(True)
        self.nodes.currentCellChanged.connect(lambda *_: self._fill_ports())

        self.in_port = QComboBox()
        self.value = QLineEdit()
        self.value.setPlaceholderText("숫자 · 참/거짓 · 글자 · 점 x,y,z")
        self.from_node = QComboBox()
        self.from_port = QComboBox()
        self.from_node.activated.connect(lambda *_: self._fill_from_ports())
        self.info = QLabel()
        self.info.setWordWrap(True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.addWidget(row(button("예제 그래프", self.example), button("계산", self._evaluate),
                             button("굽기", self._bake), button("지우기", self._clear)))
        layout.addWidget(row(self.kind_box, button("노드 넣기", self._add)))
        layout.addWidget(self.nodes, 1)
        form = QFormLayout()
        form.addRow("입력", self.in_port)
        form.addRow("값", row(self.value, button("넣기", self._set_value)))
        form.addRow("이을 것", row(self.from_node, self.from_port))
        form.addRow(row(button("이 입력에 잇기", self._connect), button("끊기", self._disconnect),
                        button("노드 지우기", self._remove)))
        layout.addLayout(form)
        layout.addWidget(self.info)

        self._timer = QTimer(self)
        self._timer.timeout.connect(self.refresh)

    # ── 시작·종료 ──
    def start_polling(self):
        if not self.kinds:
            self._load_kinds()
        self._timer.start(500)
        self.refresh()

    def shutdown(self):
        self._timer.stop()

    def _load_kinds(self):
        try:
            kinds = json.loads(lotcad.CAD_NodeGraphGetKindsJson() or "[]")
        except ValueError:
            kinds = []
        self.kinds = {k["kind"]: k for k in kinds}
        self.kind_box.clear()
        for k in kinds:
            self.kind_box.addItem(f"{k['group']} · {k['kind']}", k["kind"])

    def _check(self, status, what):
        if status == lotcad.CAD_OK:
            return True
        self._log(f"그래프 {what} 실패: {lotcad.CAD_GetLastError() or status}")
        return False

    # ── 지금 고른 노드 ──
    def _node(self, node_id):
        for n in self.graph.get("graph", {}).get("nodes", []):
            if n["id"] == node_id:
                return n
        return None

    def _selected(self):
        r = self.nodes.currentRow()
        item = self.nodes.item(r, 0) if r >= 0 else None
        return self._node(int(item.text())) if item else None

    # ── 버튼 ──
    def _add(self):
        kind = self.kind_box.currentData()
        st, node_id = lotcad.CAD_NodeGraphAddNode(kind, self._next_x, 0.0)
        if self._check(st, "노드 넣기"):
            self._next_x += 220.0   # 엔진 그래프 편집기에서 열어도 겹치지 않게 옆으로
            self._log(f"그래프: {kind} #{node_id}")
        self.refresh(select=node_id)

    def _set_value(self):
        n, port = self._selected(), self.in_port.currentData()
        if not n or not port:
            return
        kind = self.kinds.get(n["kind"], {})
        typ = next((i["type"] for i in kind.get("inputs", []) if i["name"] == port), "number")
        text = self.value.text().strip()
        try:
            if typ in ("number", "integer"):
                st = lotcad.CAD_NodeGraphSetNumber(n["id"], port, float(text))
            elif typ == "bool":
                st = lotcad.CAD_NodeGraphSetBool(n["id"], port, text.lower() in ("1", "true", "참", "yes", "on"))
            elif typ == "point":
                x, y, z = (float(v) for v in text.split(","))
                st = lotcad.CAD_NodeGraphSetPoint(n["id"], port, lotcad.CAD_GeVec3(x, y, z))
            elif typ == "text":
                st = lotcad.CAD_NodeGraphSetText(n["id"], port, text)
            else:
                return self._log("그래프: objects 입력은 값이 아니라 다른 노드의 출력을 잇는다")
        except ValueError:
            return self._log(f"그래프: '{text}' 는 {typ} 값이 아닙니다")
        self._check(st, "값 넣기")

    def _connect(self):
        n, port = self._selected(), self.in_port.currentData()
        src, src_port = self.from_node.currentData(), self.from_port.currentData()
        if n and port and src and src_port:
            self._check(lotcad.CAD_NodeGraphConnect(src, src_port, n["id"], port), "잇기")   # 종류가 다르거나 고리면 CONFLICT

    def _disconnect(self):
        n, port = self._selected(), self.in_port.currentData()
        if n and port:
            self._check(lotcad.CAD_NodeGraphDisconnect(n["id"], port), "끊기")

    def _remove(self):
        n = self._selected()
        if n:
            self._check(lotcad.CAD_NodeGraphRemoveNode(n["id"]), "노드 지우기")

    def _evaluate(self):
        bad = lotcad.CAD_NodeGraphEvaluate()
        self._log("그래프 계산: 오류 없음" if bad == 0 else f"그래프 계산: 오류 노드 {bad}개" if bad > 0
                  else f"그래프 계산 실패: {lotcad.CAD_GetLastError()}")

    def _bake(self):
        # 그래프 객체 중 선택한 것만 — 선택이 없으면 그래프 객체 전부(0개를 넘기면 엔진은 지금 선택을 쓴다)
        objs = self.graph.get("objects", [])
        picked = [i for i in layers_selected() if i in objs] or objs
        if not picked:
            return self._log("굽기: 그래프가 만든 객체가 없습니다")
        made = lotcad.CAD_NodeGraphBake(picked, len(picked), None, 0)
        self._log(f"굽기: {made}개를 보통 객체로" if made >= 0 else f"굽기 실패: {lotcad.CAD_GetLastError()}")

    def _clear(self):
        self._next_x = 0.0
        self._check(lotcad.CAD_NodeGraphClear(), "지우기")

    def example(self):
        """상자 → 선형 배열(5개, X 로 150) → 출력. 값을 바꾸면 장면의 상자들이 따라 바뀐다."""
        lotcad.CAD_NodeGraphClear()
        add = lambda kind, x: lotcad.CAD_NodeGraphAddNode(kind, x, 0.0)[1]   # noqa: E731
        box, arr, out = add("box", 0.0), add("array.linear", 220.0), add("output", 440.0)
        self._next_x = 660.0
        lotcad.CAD_NodeGraphSetNumber(box, "width", 100.0)
        lotcad.CAD_NodeGraphSetNumber(arr, "count", 5)
        lotcad.CAD_NodeGraphSetPoint(arr, "offset", lotcad.CAD_GeVec3(150.0, 0.0, 0.0))
        lotcad.CAD_NodeGraphSetText(out, "name", "상자 배열")
        ok = (self._check(lotcad.CAD_NodeGraphConnect(box, "solid", arr, "objects"), "잇기")
              and self._check(lotcad.CAD_NodeGraphConnect(arr, "objects", out, "objects"), "잇기"))
        if ok:
            self._log("그래프 예제: 상자 → 선형 배열(5개) → 출력 — 배열 노드의 count 를 바꿔 보세요")
        self.refresh(select=arr)

    # ── 상태 → 화면 ──
    def refresh(self, select=None):
        if not self.isVisible():
            return
        try:
            self.graph = json.loads(lotcad.CAD_NodeGraphGetJson() or "{}")
        except ValueError:
            return
        g = self.graph.get("graph", {})
        errors = {e.get("id"): e.get("error", "") for e in self.graph.get("errors", []) if isinstance(e, dict)}
        waiting = set(self.graph.get("waiting", []))
        key = json.dumps([g.get("nodes"), g.get("links"), errors, sorted(waiting)], sort_keys=True)
        if key != self._graph_key or select is not None:
            self._graph_key = key
            keep = select if select is not None else (self._selected() or {}).get("id")
            nodes = g.get("nodes", [])
            self.nodes.setRowCount(len(nodes))
            for r, n in enumerate(nodes):
                state = (f"오류: {errors[n['id']]}" if n["id"] in errors else "입력 기다림" if n["id"] in waiting
                         else f"객체 {len(n['sceneIds'])}개" if n.get("sceneIds") else "")
                for col, text in enumerate([str(n["id"]), n["kind"], state]):
                    self.nodes.setItem(r, col, QTableWidgetItem(text))
                if n["id"] == keep:
                    self.nodes.selectRow(r)
            self.nodes.resizeColumnsToContents()
            self._fill_from_nodes()
            self._fill_ports()
        links = len(g.get("links", []))
        self.info.setText(f"노드 {len(g.get('nodes', []))}개 · 링크 {links}개 · 장면 객체 {len(self.graph.get('objects', []))}개"
                          + ("  (계산 대기)" if self.graph.get("pending") else ""))

    def _fill_ports(self):
        n = self._selected()
        keep = self.in_port.currentData()
        self.in_port.clear()
        if not n:
            return
        links = {(l.get("to"), l.get("toPort")) for l in self.graph.get("graph", {}).get("links", []) if isinstance(l, dict)}
        for i in self.kinds.get(n["kind"], {}).get("inputs", []):
            tag = "  ← 이어짐" if (n["id"], i["name"]) in links else ""
            self.in_port.addItem(f"{i['name']} ({i['type']}){tag}", i["name"])
        self.in_port.setCurrentIndex(max(0, self.in_port.findData(keep)))

    def _fill_from_nodes(self):
        keep = self.from_node.currentData()
        self.from_node.clear()
        for n in self.graph.get("graph", {}).get("nodes", []):
            if self.kinds.get(n["kind"], {}).get("outputs"):
                self.from_node.addItem(f"#{n['id']} {n['kind']}", n["id"])
        self.from_node.setCurrentIndex(max(0, self.from_node.findData(keep)))
        self._fill_from_ports()

    def _fill_from_ports(self):
        n = self._node(self.from_node.currentData())
        self.from_port.clear()
        for o in self.kinds.get(n["kind"], {}).get("outputs", []) if n else []:
            self.from_port.addItem(f"{o['name']} ({o['type']})", o["name"])
