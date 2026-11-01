"""도면층 · 선종류 · 블록 패널 — 오른쪽 독. 엔진의 layer·linetype·블록 패널(ImGui)은 호스트 창에서 안 그려져 여기서 한다.

도면층: CAD_GetLayersJson 으로 목록(이름·보이기·잠금·색·선종류·객체 수) → CAD_CreateLayer · CAD_RenameLayer ·
        CAD_SetLayerVisible · CAD_SetLayerLocked · CAD_SetLayerColor · CAD_SetLayerLinetype · CAD_AssignSelectedToLayer.
        (도면층 지우기·현재 도면층 API 는 아직 없다)
선종류: CAD_GetLinetypeIds · CAD_GetLinetypeName → 선택한 객체에 CAD_SetObjectLinetype, 전체 축척 CAD_SetLinetypeScale.
        .lin 불러오기는 명령 ltload.
블록:   CAD_GetBlocksJson 으로 목록 → 선택한 객체로 CAD_CreateBlock(기준점 = 선택 상자 가운데 아래), 삽입(INSERT)은
        CAD_EntityExplode 로 한 단계 분해, 속성 값은 CAD_Get/SetInsertAttributesJson.
"""
import ctypes
import json

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QColorDialog, QComboBox, QDoubleSpinBox, QHBoxLayout, QInputDialog, QLabel,
                               QPushButton, QTableWidget, QTableWidgetItem, QTabWidget, QVBoxLayout, QWidget)

import lotcad


def selected_ids():
    n = lotcad.CAD_GetSelection(None, 0)
    if n <= 0:
        return []
    buf = lotcad.buffer(ctypes.c_uint32, n)
    got = lotcad.CAD_GetSelection(buf, n)
    return list(buf[:max(0, min(n, got))])


def linetypes():
    """[(id, 이름)] — 0 = Continuous(실선)."""
    n = lotcad.CAD_GetLinetypeIds(None, 0)
    if n <= 0:
        return []
    buf = lotcad.buffer(ctypes.c_uint32, n)
    lotcad.CAD_GetLinetypeIds(buf, n)
    return [(i, lotcad.CAD_GetLinetypeName(i) or str(i)) for i in buf[:n]]


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


class LayersPanel(QWidget):
    """show_page("layers"|"linetypes"|"blocks")."""

    PAGES = ["layers", "linetypes", "blocks"]

    def __init__(self, log, parent=None):
        super().__init__(parent)
        self._log = log            # 명령행에 한 줄 — 결과·실패 이유
        self._layers_key = None
        self.tabs = QTabWidget()
        self.tabs.addTab(self._build_layers(), "도면층")
        self.tabs.addTab(self._build_linetypes(), "선종류")
        self.tabs.addTab(self._build_blocks(), "블록")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.addWidget(self.tabs)
        # 객체 수·선택 수는 밖(3D 뷰·명령)에서 바뀐다 — 보이는 동안 0.5초마다
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.refresh)

    def show_page(self, page):
        self.tabs.setCurrentIndex(self.PAGES.index(page))

    def start_polling(self):
        self._timer.start(500)

    def shutdown(self):
        self._timer.stop()

    def _check(self, status, what):
        """결과 코드 → 실패면 명령행에 이유. 성공 여부를 돌려준다."""
        if status == lotcad.CAD_OK:
            return True
        self._log(f"{what} 실패: {lotcad.CAD_GetLastError() or status}")
        return False

    # ── 도면층 ──
    def _build_layers(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        self.layer_table = QTableWidget(0, 5)
        self.layer_table.setHorizontalHeaderLabels(["이름", "보임", "잠금", "색", "객체"])
        self.layer_table.verticalHeader().hide()
        self.layer_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.layer_table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.layer_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.layer_table.cellClicked.connect(self._layer_cell_clicked)
        self.layer_table.horizontalHeader().setStretchLastSection(True)
        self.layer_linetype = QComboBox()
        self.layer_linetype.activated.connect(self._layer_linetype)
        layout.addWidget(self.layer_table, 1)
        layout.addWidget(row(button("새 도면층", self._new_layer), button("이름 바꾸기", self._rename_layer)))
        layout.addWidget(row(QLabel("선종류"), self.layer_linetype))
        layout.addWidget(button("선택한 객체를 이 도면층으로", self._assign_selected))
        layout.addWidget(QLabel("보임·잠금 칸을 누르면 바뀌고, 색 칸을 누르면 색을 고른다."))
        return page

    def _layers(self):
        try:
            return json.loads(lotcad.CAD_GetLayersJson() or "{}").get("layers", [])
        except ValueError:
            return []

    def _current_layer(self):
        r = self.layer_table.currentRow()
        item = self.layer_table.item(r, 0) if r >= 0 else None
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    def _fill_layers(self, layers):
        current = self._current_layer()
        self.layer_table.setRowCount(len(layers))
        for r, L in enumerate(layers):
            name = QTableWidgetItem(L["name"])
            name.setData(Qt.ItemDataRole.UserRole, L)
            cells = [name, QTableWidgetItem("●" if L.get("visible") else "○"),
                     QTableWidgetItem("🔒" if L.get("locked") else ""), QTableWidgetItem(""),
                     QTableWidgetItem(f"{L.get('objectCount', 0)}" + (f" (선택 {L['selectedCount']})" if L.get("selectedCount") else ""))]
            c = L.get("color", [1, 1, 1])
            cells[3].setBackground(QColor.fromRgbF(c[0], c[1], c[2]))
            for col, item in enumerate(cells):
                if col:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.layer_table.setItem(r, col, item)
            if current and current.get("id") == L["id"]:
                self.layer_table.selectRow(r)
        self.layer_table.resizeColumnsToContents()
        L = self._current_layer()
        if L:
            i = self.layer_linetype.findData(L.get("linetypeId", 0))
            if i >= 0 and not self.layer_linetype.view().isVisible():
                self.layer_linetype.setCurrentIndex(i)

    def _layer_cell_clicked(self, r, col):
        L = self.layer_table.item(r, 0).data(Qt.ItemDataRole.UserRole)
        if col == 1:
            self._check(lotcad.CAD_SetLayerVisible(L["id"], not L.get("visible")), "도면층 보이기")
        elif col == 2:
            self._check(lotcad.CAD_SetLayerLocked(L["id"], not L.get("locked")), "도면층 잠금")
        elif col == 3:
            c = L.get("color", [1, 1, 1])
            picked = QColorDialog.getColor(QColor.fromRgbF(c[0], c[1], c[2]), self, f"도면층 색 — {L['name']}")
            if picked.isValid():
                color = lotcad.CAD_Color(picked.redF(), picked.greenF(), picked.blueF())
                self._check(lotcad.CAD_SetLayerColor(L["id"], color), "도면층 색")
        self.refresh(force=True)

    def _new_layer(self):
        name, ok = QInputDialog.getText(self, "새 도면층", "이름")
        if ok and name:
            st, layer_id = lotcad.CAD_CreateLayer(name)
            if self._check(st, "새 도면층"):
                self._log(f"도면층 '{name}' 만듦 (#{layer_id})")
            self.refresh(force=True)

    def _rename_layer(self):
        L = self._current_layer()
        if not L:
            return self._log("이름 바꾸기: 도면층을 먼저 고르세요")
        name, ok = QInputDialog.getText(self, "도면층 이름 바꾸기", "새 이름", text=L["name"])
        if ok and name and name != L["name"]:
            self._check(lotcad.CAD_RenameLayer(L["id"], name), "이름 바꾸기")   # 0 층은 고정이라 거절된다
            self.refresh(force=True)

    def _layer_linetype(self):
        L = self._current_layer()
        if L:
            self._check(lotcad.CAD_SetLayerLinetype(L["id"], self.layer_linetype.currentData()), "도면층 선종류")
            self.refresh(force=True)

    def _assign_selected(self):
        L = self._current_layer()
        if not L:
            return self._log("도면층을 먼저 고르세요")
        st, changed = lotcad.CAD_AssignSelectedToLayer(L["id"])
        lotcad.CAD_SetSelectedColorByLayer(True)   # 색도 도면층 것(ByLayer) — 안 하면 옮겨도 원래 색 그대로
        if self._check(st, "도면층 옮기기"):
            self._log(f"{changed}개를 도면층 '{L['name']}' 으로" if changed else "옮길 객체가 없습니다 — 3D 뷰에서 먼저 선택")
        self.refresh(force=True)

    # ── 선종류 ──
    def _build_linetypes(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        self.linetype_box = QComboBox()
        self.lt_scale = QDoubleSpinBox()
        self.lt_scale.setRange(0.01, 10000)
        self.lt_scale.setDecimals(2)
        self.lt_scale.setValue(1.0)
        layout.addWidget(row(QLabel("선종류"), self.linetype_box))
        layout.addWidget(button("선택한 객체에 적용", self._apply_linetype))
        layout.addWidget(button("선택한 객체를 도면층 선종류로(ByLayer)", self._bylayer))
        layout.addWidget(row(QLabel("전체 축척(LTSCALE)"), self.lt_scale,
                             button("적용", lambda: self._check(lotcad.CAD_SetLinetypeScale(self.lt_scale.value()), "선종류 축척"))))
        # .lin 불러오기는 API 가 없어 명령으로 — 명령행이 파일 이름을 묻는다
        layout.addWidget(button(".lin 불러오기 (명령 ltload)", self._ltload))
        layout.addStretch(1)
        return page

    def _fill_linetypes(self):
        items = linetypes()
        key = tuple(items)
        if key == getattr(self, "_lt_key", None):
            return
        self._lt_key = key
        for box in (self.linetype_box, self.layer_linetype):
            keep = box.currentData()
            box.clear()
            for i, name in items:
                box.addItem(name, i)
            j = box.findData(keep)
            box.setCurrentIndex(max(0, j))

    def _apply_linetype(self):
        ids = selected_ids()
        if not ids:
            return self._log("선종류: 3D 뷰에서 객체를 먼저 선택하세요")
        st, changed = lotcad.CAD_SetObjectLinetype(ids, len(ids), self.linetype_box.currentData())
        if self._check(st, "선종류"):
            self._log(f"선종류 '{self.linetype_box.currentText()}' — {changed}개")

    def _bylayer(self):
        ids = selected_ids()
        if ids:
            st, changed = lotcad.CAD_SetObjectLinetype(ids, len(ids), lotcad.CAD_LINETYPE_BYLAYER)
            if self._check(st, "선종류"):
                self._log(f"선종류 ByLayer — {changed}개")

    def _ltload(self):
        lotcad.CAD_CancelCommand()
        lotcad.CAD_ExecuteCommand("ltload")

    # ── 블록 ──
    def _build_blocks(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        self.block_table = QTableWidget(0, 3)
        self.block_table.setHorizontalHeaderLabels(["이름", "객체", "삽입 수"])
        self.block_table.verticalHeader().hide()
        self.block_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.block_table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.block_table, 1)
        layout.addWidget(button("선택한 객체로 블록 만들기", self._create_block))
        layout.addWidget(button("선택한 삽입(INSERT) 분해", self._explode_inserts))
        layout.addWidget(button("선택한 삽입의 속성 값 보기", self._show_attributes))
        return page

    def _fill_blocks(self):
        try:
            blocks = json.loads(lotcad.CAD_GetBlocksJson() or "{}").get("blocks", [])
        except ValueError:
            blocks = []
        key = json.dumps(blocks, sort_keys=True)
        if key == getattr(self, "_blocks_key", None):
            return
        self._blocks_key = key
        self.block_table.setRowCount(len(blocks))
        for r, b in enumerate(blocks):
            name = b["name"] + ("  (외부 참조)" if b.get("xref") else "")
            for col, text in enumerate([name, str(b.get("objects", 0)), str(b.get("references", 0))]):
                self.block_table.setItem(r, col, QTableWidgetItem(text))
        self.block_table.resizeColumnsToContents()

    def _create_block(self):
        ids = selected_ids()
        if not ids:
            return self._log("블록: 3D 뷰에서 묶을 객체를 먼저 선택하세요")
        name, ok = QInputDialog.getText(self, "블록 만들기", f"블록 이름 (객체 {len(ids)}개)")
        if not (ok and name):
            return
        base = self._selection_base(ids)
        st, insert_id = lotcad.CAD_CreateBlock(name, ids, len(ids), base)
        if self._check(st, "블록 만들기"):
            self._log(f"블록 '{name}' — 객체 {len(ids)}개, 기준점 ({base.x:.3g}, {base.y:.3g}, {base.z:.3g}), 삽입 #{insert_id}")
        self.refresh(force=True)

    @staticmethod
    def _selection_base(ids):
        """기준점 = 선택 상자의 가운데 아래(바닥 중앙). 상자를 못 읽으면 원점."""
        lo, hi = [1e30] * 3, [-1e30] * 3
        for i in ids:
            try:
                b = json.loads(lotcad.CAD_GetObjectJson(i) or "{}").get("bounds")
            except ValueError:
                b = None
            if b:
                lo = [min(a, v) for a, v in zip(lo, b["min"])]
                hi = [max(a, v) for a, v in zip(hi, b["max"])]
        if lo[0] > hi[0]:
            return lotcad.CAD_GeVec3(0, 0, 0)
        return lotcad.CAD_GeVec3((lo[0] + hi[0]) / 2, (lo[1] + hi[1]) / 2, lo[2])

    def _explode_inserts(self):
        ids = selected_ids()
        if not ids:
            return self._log("분해: 삽입(INSERT)을 먼저 선택하세요")
        made = lotcad.CAD_EntityExplode(ids, len(ids), False, None, 0)   # 결과 id 는 필요 없으니 개수만
        self._log(f"분해: {made}개가 됨" if made > 0 else f"분해 실패: {lotcad.CAD_GetLastError() or made}")
        self.refresh(force=True)

    def _show_attributes(self):
        for i in selected_ids():
            text = lotcad.CAD_GetInsertAttributesJson(i)
            if text is not None:
                self._log(f"삽입 #{i} 속성: {text}")
                return
        self._log("속성: 선택에 삽입(INSERT)이 없습니다")

    # ── 상태 → 화면 ──
    def refresh(self, force=False):
        if not self.isVisible():
            return
        self._fill_linetypes()
        layers = self._layers()
        key = json.dumps(layers, sort_keys=True)
        if force or key != self._layers_key:
            self._layers_key = key
            self._fill_layers(layers)
        self._fill_blocks()
