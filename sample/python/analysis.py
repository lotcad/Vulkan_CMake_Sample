"""해석 패널 — 바람 터널 · 물 · 구조 해석. 엔진 해석 패널(ImGui)은 호스트 창 안에서 안 그려져 그 일을 여기서 한다.

세 API(CAD_WindTunnel · CAD_Water · CAD_StructuralAnalysis)는 {"op": …} JSON 을 받아 결과 JSON 을 준다 —
MCP 도구 wind_tunnel · water · structural_analysis 와 같은 op·인자(헤더 LotCAD_API.h 의 해석 주석).

흐름
  바람 터널: 솔리드 선택 → 시작(다음 프레임에 켜짐) → 단면·연기·표면 압력으로 보기. 바람은 +X.
  물:        닫힌 솔리드(그릇) 선택 → 물 높이 → 시작 → 기울이기·흔들기
  구조 해석: 솔리드 선택 → 열기(면 목록이 온다) → 면 골라 고정·하중 → 실행(작업 스레드) → 결과·색 보기

해석 모듈(libLotCADSim · libLotCADCfd)은 엔진 라이브러리 옆(sdk/)에 있어야 한다 — 없으면 start·run 이 error 로 알려 준다.
"""
import ctypes
import json

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (QCheckBox, QComboBox, QDoubleSpinBox, QFormLayout, QHBoxLayout, QLabel, QListWidget,
                               QListWidgetItem, QPushButton, QScrollArea, QSlider, QTabWidget, QVBoxLayout, QWidget)

import lotcad

_FUNCS = {"wind": "CAD_WindTunnel", "water": "CAD_Water", "sim": "CAD_StructuralAnalysis"}


def call(which, args):
    """해석 API 한 번 — 결과 JSON(dict). 실패면 {"ok": False, "error": …}.

    ⚠️ 2회 호출 규약을 직접 지킨다: out=NULL 로 길이를 먼저 묻고(이때 한 번 실행), 같은 인자로 버퍼를 넘기면
    엔진이 다시 실행하지 않고 그 결과를 준다. 자동 생성 바인딩(lotcad.CAD_WindTunnel 등)은 작은 버퍼로 먼저 불렀다가
    모자라면 **버퍼로 다시** 부르므로 run·start 가 두 번 들어가 "이미 도는 중" 이 된다 — 그래서 원시 함수(lotcad.native)로.
    """
    fn = getattr(lotcad.native, _FUNCS[which])
    raw = json.dumps(args).encode("utf-8")
    need = fn(raw, None, 0)
    if need < 0:
        return {"ok": False, "error": lotcad.CAD_GetLastError() or "실패"}
    buf = ctypes.create_string_buffer(need + 1)
    if fn(raw, buf, need + 1) < 0:
        return {"ok": False, "error": lotcad.CAD_GetLastError() or "실패"}
    return json.loads(buf.value.decode("utf-8") or "{}")


def num(value, spec):
    """숫자 → 글. 엔진은 아직 없는 값을 null 로 준다(켠 직후의 항력 계수 등) — 그땐 "-"."""
    return "-" if value is None else format(value, spec)


def selected_ids():
    return [i for i in (lotcad.CAD_GetSelectedObjectId(k) for k in range(lotcad.CAD_GetSelectedCount())) if i]


def axis_name(n):
    """법선 → "+Z" 처럼(축에 거의 맞으면), 아니면 숫자 셋."""
    for i, name in enumerate("XYZ"):
        if abs(n[i]) > 0.98:
            return ("+" if n[i] > 0 else "−") + name
    return "(" + ", ".join(f"{c:.2f}" for c in n) + ")"


def combo(items, current=0):
    """[(보이는 글, 엔진 값)] → QComboBox. 엔진 값은 currentData()."""
    box = QComboBox()
    for text, value in items:
        box.addItem(text, value)
    box.setCurrentIndex(current)
    return box


def slider(lo, hi, value, steps=1000):
    """실수 슬라이더 — QSlider 는 정수라 steps 칸으로 나눈다. value() 대신 .real()."""
    s = QSlider(Qt.Orientation.Horizontal)
    s.setRange(0, steps)
    s.real = lambda: lo + (hi - lo) * s.value() / steps
    s.setValue(round((value - lo) / (hi - lo) * steps))
    return s


def spin(value, lo=-1e6, hi=1e6, decimals=1):
    box = QDoubleSpinBox()
    box.setRange(lo, hi)
    box.setDecimals(decimals)
    box.setValue(value)
    box.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)
    box.setMaximumWidth(80)   # 범위 글자 수로 정해지는 기본 폭이 커서 독이 가로로 넘친다
    return box


def row(*widgets):
    w = QWidget()
    layout = QHBoxLayout(w)
    layout.setContentsMargins(0, 0, 0, 0)
    for x in widgets:
        layout.addWidget(x)
    return w


def button(text, slot):
    b = QPushButton(text)
    b.clicked.connect(slot)
    return b


GRIDS = [("빠름", "fast"), ("보통", "normal"), ("정밀", "fine")]


class AnalysisPanel(QWidget):
    """오른쪽 독에 넣는 해석 패널. show_page("wind"|"water"|"sim") 로 그 탭을 연다."""

    PAGES = ["wind", "water", "sim"]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.state = {"wind": {}, "water": {}, "sim": {}}
        self._face = -1        # 구조 해석에서 고른 면
        self._faces_key = None  # 면 목록을 다시 채울지 판단

        self.tabs = QTabWidget()
        self.tabs.addTab(self._scroll(self._build_wind()), "바람 터널")
        self.tabs.addTab(self._scroll(self._build_water()), "물")
        self.tabs.addTab(self._scroll(self._build_sim()), "구조 해석")
        self.error = QLabel()
        self.error.setWordWrap(True)
        self.error.setStyleSheet("color: #ff8a80;")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.addWidget(self.tabs, 1)
        layout.addWidget(self.error)

        # 해석 상태는 엔진이 프레임마다 바꾼다(켜짐·단계·풀이 끝) — 보이는 동안 0.3초마다 읽는다
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.refresh)

    def show_page(self, page):
        self.tabs.setCurrentIndex(self.PAGES.index(page))

    def start_polling(self):
        self._timer.start(300)
        self.refresh()

    def shutdown(self):
        # 엔진을 헐기 전에 — 헐린 엔진에 status 를 묻지 않게
        self._timer.stop()

    @staticmethod
    def _scroll(widget):
        area = QScrollArea()
        area.setWidgetResizable(True)
        area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)   # 세로로만 — 독 폭에 맞춘다
        area.setWidget(widget)
        return area

    # ── 엔진 호출 ──
    def call(self, which, args):
        result = call(which, args)
        self.error.setText(result.get("error") or "")
        if "ok" in result:
            self.refresh()
        return result

    def need_selection(self):
        ids = selected_ids()
        if not ids:
            self.error.setText("3D 뷰에서 대상 솔리드를 먼저 선택하세요")
        return ids

    # ── 바람 터널 ──
    def _build_wind(self):
        page = QWidget()
        form = QFormLayout(page)
        self.wind_state = QLabel()
        self.wind_state.setWordWrap(True)
        self.wind_grid = combo(GRIDS)
        self.wind_speed = slider(0.02, 0.10, 0.06)
        self.wind_speed_label = QLabel()
        self.wind_speed.valueChanged.connect(self._wind_speed_moved)
        self.wind_start = button("시작", self._wind_start)
        self.wind_pause = button("일시정지", lambda: self.call(
            "wind", {"op": "play" if self.state["wind"].get("flowing") is False else "pause"}))
        self.wind_running = [button("정지", lambda: self.call("wind", {"op": "stop"})), self.wind_pause,
                             button("초기화", lambda: self.call("wind", {"op": "reset"}))]
        self.wind_field = combo([("속도", "speed"), ("압력", "pressure"), ("소용돌이", "vortex"), ("연기", "smoke")])
        self.wind_field.activated.connect(lambda: self.call("wind", {"op": "view", "field": self.wind_field.currentData()}))
        self.wind_plane = combo([("X", "x"), ("Y", "y"), ("Z", "z")], 1)
        self.wind_at = slider(0.0, 1.0, 0.5, 100)
        self.wind_plane.activated.connect(self._wind_plane)
        self.wind_at.sliderMoved.connect(self._wind_plane)
        surface = QCheckBox("표면 압력 색")
        surface.toggled.connect(lambda on: self.call("wind", {"op": "view", "surface": on}))
        smoke = QCheckBox("연기")
        smoke.toggled.connect(lambda on: self.call("wind", {"op": "view", "smoke": on}))
        self.wind_info = QLabel()
        self.wind_info.setWordWrap(True)

        form.addRow(self.wind_state)
        form.addRow("격자", self.wind_grid)
        form.addRow(self.wind_speed_label, self.wind_speed)
        form.addRow(row(self.wind_start, *self.wind_running))
        form.addRow(QLabel("<b>보기</b>"))
        form.addRow("색", self.wind_field)
        form.addRow("단면", self.wind_plane)
        form.addRow("단면 위치", self.wind_at)
        form.addRow(surface)
        form.addRow(smoke)
        form.addRow(self.wind_info)
        self._wind_speed_moved()
        return page

    def _wind_speed_moved(self):
        self.wind_speed_label.setText(f"바람 세기 {self.wind_speed.real():.3f}")
        if self.state["wind"].get("active") and self.wind_speed.isSliderDown():
            self.call("wind", {"op": "wind", "value": self.wind_speed.real()})

    def _wind_start(self):
        ids = self.need_selection()
        if ids:
            self.call("wind", {"op": "start", "ids": ids, "grid": self.wind_grid.currentData(),
                               "wind": self.wind_speed.real()})

    def _wind_plane(self, *_):
        self.call("wind", {"op": "view", "plane": self.wind_plane.currentData(), "at": self.wind_at.real()})

    # ── 물 ──
    def _build_water(self):
        page = QWidget()
        form = QFormLayout(page)
        self.water_state = QLabel()
        self.water_state.setWordWrap(True)
        self.water_grid = combo(GRIDS, 1)
        self.water_level = slider(0.05, 0.95, 0.5, 90)
        self.water_start = button("시작", self._water_start)
        self.water_pause = button("일시정지", lambda: self.call(
            "water", {"op": "play" if self.state["water"].get("flowing") is False else "pause"}))
        self.tilt_x = slider(-40, 40, 0, 80)
        self.tilt_y = slider(-40, 40, 0, 80)
        for s in (self.tilt_x, self.tilt_y):
            s.sliderMoved.connect(lambda *_: self.call("water", {"op": "tilt", "x": self.tilt_x.real(), "y": self.tilt_y.real()}))
        self.shake_amp = slider(0.05, 1.0, 0.3, 95)
        # 주기를 비우면 엔진이 첫 출렁임 공진 주기로 흔든다
        shake = button("흔들기(공진)", lambda: self.call("water", {"op": "shake", "amplitude": self.shake_amp.real()}))
        unshake = button("멈춤", lambda: self.call("water", {"op": "shake", "amplitude": 0}))
        self.water_running = [button("정지", lambda: self.call("water", {"op": "stop"})), self.water_pause,
                              button("초기화", lambda: self.call("water", {"op": "reset"})),
                              self.tilt_x, self.tilt_y, shake, unshake]
        self.water_info = QLabel()
        self.water_info.setWordWrap(True)

        form.addRow(self.water_state)
        form.addRow("격자", self.water_grid)
        form.addRow("물 높이", self.water_level)
        form.addRow(row(self.water_start, *self.water_running[:3]))
        form.addRow("기울이기 X", self.tilt_x)
        form.addRow("기울이기 Y", self.tilt_y)
        form.addRow("흔들기 세기", self.shake_amp)
        form.addRow(row(shake, unshake))
        form.addRow(self.water_info)
        return page

    def _water_start(self):
        ids = self.need_selection()
        if ids:
            self.call("water", {"op": "start", "id": ids[0], "level": self.water_level.real(),
                                "grid": self.water_grid.currentData()})

    # ── 구조 해석 ──
    def _build_sim(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        self.sim_open = button("선택한 솔리드로 열기", self._sim_open)
        self.sim_close = button("닫기", lambda: (self._pick_face(-1), self.call("sim", {"op": "close"})))
        self.sim_type = combo([("응력", "stress"), ("열전도", "heat"), ("진동 모드", "modal"), ("좌굴", "buckling")])
        self.sim_material = combo([("강철(S275)", "steel"), ("알루미늄(6061-T6)", "aluminum"), ("스테인리스", "stainless"),
                                   ("티타늄", "titanium"), ("ABS", "abs")])
        self.sim_size = combo(GRIDS, 1)
        for box, key in ((self.sim_type, "type"), (self.sim_material, "material"), (self.sim_size, "size")):
            box.activated.connect(lambda _=0, b=box, k=key: self.call("sim", {"op": "set", k: b.currentData()}))
        settings = QFormLayout()
        settings.addRow("종류", self.sim_type)
        settings.addRow("재료", self.sim_material)
        settings.addRow("요소", self.sim_size)

        self.faces = QListWidget()
        self.faces.setMaximumHeight(160)
        self.faces.currentRowChanged.connect(lambda r: self._pick_face(self.faces.item(r).data(Qt.ItemDataRole.UserRole)
                                                                        if r >= 0 else -1))

        face = lambda: self._face   # noqa: E731 — 버튼마다 지금 고른 면
        # 하중 조건 — 응력·진동·좌굴
        self.fx, self.fy, self.fz = spin(0), spin(0), spin(-1000)
        self.pressure = spin(1.0)
        self.load_box = QWidget()
        loads = QFormLayout(self.load_box)
        loads.setContentsMargins(0, 0, 0, 0)
        loads.addRow(row(button("고정", lambda: self.call("sim", {"op": "fix", "face": face()})),
                         button("풀기", lambda: self.call("sim", {"op": "free", "face": face()}))))
        loads.addRow("힘 N", row(self.fx, self.fy, self.fz, button("걸기", lambda: self.call(
            "sim", {"op": "force", "face": face(), "force": [self.fx.value(), self.fy.value(), self.fz.value()]}))))
        loads.addRow("압력 MPa", row(self.pressure, button("걸기", lambda: self.call(
            "sim", {"op": "pressure", "face": face(), "value": self.pressure.value()}))))
        # 열 조건
        self.temp, self.flux, self.conv_h, self.conv_amb = spin(80), spin(10), spin(10), spin(20)
        self.heat_box = QWidget()
        heat = QFormLayout(self.heat_box)
        heat.setContentsMargins(0, 0, 0, 0)
        heat.addRow("온도 °C", row(self.temp, button("걸기", lambda: self.call(
            "sim", {"op": "temp", "face": face(), "value": self.temp.value()}))))
        heat.addRow("열 W", row(self.flux, button("걸기", lambda: self.call(
            "sim", {"op": "flux", "face": face(), "value": self.flux.value()}))))
        heat.addRow("대류 h · 주변 °C", row(self.conv_h, self.conv_amb, button("걸기", lambda: self.call(
            "sim", {"op": "convect", "face": face(), "h": self.conv_h.value(), "ambient": self.conv_amb.value()}))))

        self.sim_run = button("실행", lambda: self.call("sim", {"op": "run"}))
        self.sim_cancel = button("취소", lambda: self.call("sim", {"op": "cancel"}))
        self.sim_converge = button("수렴 확인", lambda: self.call("sim", {"op": "converge"}))
        self.sim_clear = button("지우기", lambda: self.call("sim", {"op": "clear"}))
        self.sim_show = QComboBox()
        self.sim_show.activated.connect(lambda: self.call("sim", {"op": "set", "show": self.sim_show.currentData()}))
        self._show_kind = None
        self.sim_result = QLabel()
        self.sim_result.setWordWrap(True)
        self.sim_result.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        layout.addWidget(row(self.sim_open, self.sim_close))
        layout.addLayout(settings)
        self.faces_label = QLabel("<b>면</b> — 골라서 조건을 건다")
        layout.addWidget(self.faces_label)
        layout.addWidget(self.faces)
        layout.addWidget(self.load_box)
        layout.addWidget(self.heat_box)
        self.run_row = row(self.sim_run, self.sim_cancel, self.sim_converge, self.sim_clear)
        layout.addWidget(self.run_row)
        self.show_row = row(QLabel("색"), self.sim_show)
        layout.addWidget(self.show_row)
        layout.addWidget(self.sim_result)
        layout.addStretch(1)
        return page

    def _sim_open(self):
        ids = self.need_selection()
        if ids:
            self._pick_face(-1)
            self.call("sim", {"op": "open", "id": ids[0]})

    def _pick_face(self, index):
        self._face = index
        for w in (self.load_box, self.heat_box):
            w.setEnabled(index >= 0)

    # ── 상태 → 화면 ──
    def refresh(self):
        if not self.isVisible():
            return
        for which in self.PAGES:
            st = call(which, {"op": "status"})
            if st.get("ok", True):
                self.state[which] = st
        self._show_wind(self.state["wind"])
        self._show_water(self.state["water"])
        self._show_sim(self.state["sim"])

    def _show_wind(self, w):
        active = bool(w.get("active"))
        self.wind_state.setText(f"켜짐 — 솔리드 {len(w.get('ids', []))}개 둘레, 바람 +X" if active
                                else "켜는 중…" if w.get("starting") else "꺼짐 — 솔리드를 선택하고 시작")
        self.wind_start.setEnabled(not active)
        for b in self.wind_running:
            b.setEnabled(active)
        self.wind_pause.setText("재생" if w.get("flowing") is False else "일시정지")
        info = ""
        if active:
            info = f"항력 계수 {num(w.get('drag_coefficient'), '.3f')}"
            if w.get("cells"):
                info += "   격자 " + " × ".join(map(str, w["cells"]))
        self.wind_info.setText(info)

    def _show_water(self, w):
        active = bool(w.get("active"))
        self.water_state.setText(f"켜짐 — 그릇 #{w.get('container')}" if active
                                 else "켜는 중…" if w.get("starting") else "꺼짐 — 닫힌 솔리드(그릇)를 선택하고 시작")
        self.water_start.setEnabled(not active)
        for b in self.water_running:
            b.setEnabled(active)
        self.water_pause.setText("재생" if w.get("flowing") is False else "일시정지")
        info = ""
        if active:
            if w.get("cells"):
                info = "격자 " + " × ".join(map(str, w["cells"])) + "   "
            drift = w.get("mass_drift")
            info += f"질량 오차 {num(None if drift is None else drift * 100, '.4f')}%"
        self.water_info.setText(info)

    def _show_sim(self, s):
        faces = s.get("faces") or []
        is_open = bool(faces)
        kind = s.get("type", "stress")
        busy = bool(s.get("busy"))
        result = s.get("result")
        for box, key, values in ((self.sim_type, "type", None), (self.sim_material, "material", None),
                                 (self.sim_size, "size", None)):
            i = box.findData(s.get(key))
            if i >= 0 and not box.view().isVisible():
                box.setCurrentIndex(i)
        self.sim_close.setEnabled(is_open)
        for w in (self.faces_label, self.faces, self.run_row):
            w.setVisible(is_open)
        self.load_box.setVisible(is_open and kind != "heat")
        self.heat_box.setVisible(is_open and kind == "heat")
        for w in (self.load_box, self.heat_box):
            w.setEnabled(self._face >= 0)

        # 면 목록 — 면이나 조건이 바뀔 때만 다시 채운다(고른 줄 유지)
        conds = (s.get("conditions") or []) + (s.get("heat_conditions") or [])
        key = (json.dumps(faces), json.dumps(conds))
        if key != self._faces_key:
            self._faces_key = key
            self.faces.blockSignals(True)
            self.faces.clear()
            for f in faces:
                tags = "·".join(c["kind"] for c in conds if c.get("face") == f["index"])
                item = QListWidgetItem(f"면 {f['index']}   {axis_name(f['normal'])}   넓이 {f['area']:.3g}"
                                       + (f"   [{tags}]" if tags else ""))
                item.setData(Qt.ItemDataRole.UserRole, f["index"])
                self.faces.addItem(item)
                if f["index"] == self._face:
                    self.faces.setCurrentItem(item)
            self.faces.blockSignals(False)
            if not faces:
                self._face = -1

        self.sim_run.setText("푸는 중…" if busy else "실행")
        self.sim_run.setEnabled(not busy)
        self.sim_cancel.setEnabled(busy)
        self.sim_converge.setEnabled(not busy and bool(result))
        self.sim_clear.setEnabled(not busy)

        # 결과 색 — 종류마다 고를 수 있는 것이 다르다
        self.show_row.setVisible(bool(result))
        if kind != self._show_kind:
            self._show_kind = kind
            self.sim_show.clear()
            items = ([("온도", "temp"), ("열 흐름", "flux")] if kind == "heat"
                     else [("응력", "stress"), ("변위", "disp"), ("안전율", "safety")] if kind == "stress"
                     else [(f"모드 {k}", f"mode {k}") for k in range(1, 7)])
            for text, value in items:
                self.sim_show.addItem(text, value)
        self.sim_result.setText(self._result_text(result))

    @staticmethod
    def _result_text(r):
        if not r:
            return ""
        if r.get("kind") == "stress":
            return (f"최대 응력 {num(r.get('max_von_mises_mpa'), '.4g')} MPa\n"
                    f"최대 변위 {num(r.get('max_displacement_mm'), '.4g')} mm\n"
                    f"안전율 {num(r.get('safety_factor'), '.1f')}\n자유도 {r.get('dofs')}")
        if r.get("kind") == "heat":
            return (f"온도 {num(r.get('min_temperature'), '.1f')} ~ {num(r.get('max_temperature'), '.1f')} °C\n"
                    f"최대 열유속 {num(r.get('max_flux_w_m2'), '.1f')} W/m²")
        if r.get("kind") == "modal":
            return "고유진동수 Hz\n" + "\n".join(f"  {i + 1})  {num(f, '.1f')}" for i, f in enumerate(r.get("frequencies_hz", [])))
        if r.get("kind") == "buckling":
            return "좌굴 배수 (가한 하중 × 배수 = 좌굴 하중)\n" + "\n".join(
                f"  {i + 1})  {num(f, '.2f')}" for i, f in enumerate(r.get("load_factors", [])))
        return json.dumps(r, ensure_ascii=False)
