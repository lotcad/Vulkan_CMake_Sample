"""상태바 — 창 맨 아래 오른쪽의 토글 버튼 줄. 엔진(3dEngine) 하단 상태바와 같은 순서·기능.

    [치수] [그리드] [셰이딩 ▾] [Ortho] [직교(F8)] [극좌표(F10)] [객체스냅 ▾]

치수·직교·극좌표·객체스냅은 엔진에 Get 함수가 있어 상태를 매번 엔진에 묻는다 —
명령행에 ortho off 처럼 쳐서 바꿔도 버튼이 따라간다(0.5초마다 다시 맞춤).
그리드·스타일·투영은 엔진에 Set 만 있어 이 창이 상태를 들고 있는다(처음 값 = 엔진 기본값).
"""
from PySide6.QtCore import QTimer
from PySide6.QtGui import QAction, QActionGroup
from PySide6.QtWidgets import QMenu, QStatusBar, QToolButton

import lotcad

VISUAL_STYLES = ["셰이딩", "셰이딩+모서리", "와이어프레임", "와이어(모서리)", "숨은선"]   # CAD_SetVisualStyle 번호 순

# CAD_SetOSnapModes 비트 (헤더 주석: END 1 · MID 2 · CEN 4 · FACE 8 · NODE 16 · QUA 32 · INT 64 · PER 128 · TAN 256 · NEA 512)
SNAP_MODES = [(1, "끝점"), (2, "중간점"), (4, "중심점"), (8, "면 중심"), (16, "노드(점)"),
              (32, "사분점"), (64, "교차점"), (128, "수직점"), (256, "접선"), (512, "근처점")]


def polar_on():
    # CAD_GetPolarTracking(float* incrementDeg) 은 켜짐 여부(bool)를 돌려준다. 감싸기 함수는
    # "bool 반환 + 출력 인자" 를 "성공하면 출력값, 아니면 None" 으로 바꾸므로, 켜짐 여부만 볼 땐
    # 원시 함수(lotcad.native)에 NULL 을 넘기는 편이 뜻이 분명하다.
    return bool(lotcad.native.CAD_GetPolarTracking(None))


class CadStatusBar(QStatusBar):
    def __init__(self, owner):
        super().__init__()
        self._owner = owner   # 투영(Ortho/Persp)은 메뉴·리본과 같이 쓰므로 창이 들고 있다
        self.grid_on = True
        self.visual_style = 0
        self._toggles = []    # (버튼, is_on)

        self._toggle("치수", lambda: lotcad.CAD_GetFeatureDimensionsVisible()[1],   # (결과 코드, 켜짐)
                     lambda: lotcad.CAD_SetFeatureDimensionsVisible(not lotcad.CAD_GetFeatureDimensionsVisible()[1]),
                     "선택한 솔리드의 피처 치수 표시 (fdim) — 치수를 더블클릭하면 명령행이 새 값을 기다린다")
        self._toggle("그리드", lambda: self.grid_on, self._toggle_grid, "바닥 그리드 표시")
        self._style_button()
        self._projection = self._button(self._projection_text(), lambda: owner.set_ortho(not owner.ortho),
                                        "원근(Persp) / 직교(Ortho) 투영 전환")
        self._toggle("직교(F8)", lotcad.CAD_GetOrthoEnabled, self.toggle_ortho_tracking,
                     "직교 추적 — 그리는 방향을 가로·세로로 고정 (F8, 명령 ortho)")
        self._toggle("극좌표(F10)", polar_on, self.toggle_polar,
                     "극좌표 추적 — 일정 각도마다 추적선 (F10). 각도는 명령행에 polar 30 처럼")
        self._snap_button()

        # 상태는 버튼 말고도 바뀐다(명령행 ortho off, fdim …) — 0.5초마다 엔진에 물어 다시 맞춘다
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.refresh)
        self._timer.start(500)

    # ── 버튼 만들기 ──
    def _button(self, text, action, tip):
        button = QToolButton()
        button.setText(text)
        button.setToolTip(tip)
        button.setObjectName("statusButton")
        button.clicked.connect(lambda: (action(), self.refresh()))
        self.addPermanentWidget(button)
        return button

    def _toggle(self, text, is_on, action, tip):
        button = self._button(text, action, tip)
        button.setCheckable(True)
        self._toggles.append((button, is_on))
        return button

    def _style_button(self):
        button = QToolButton()
        button.setObjectName("statusButton")
        button.setToolTip("비주얼 스타일 — 셰이딩 / 모서리 / 와이어프레임 / 숨은선")
        button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)   # 누르면 바로 메뉴
        menu = QMenu(button)
        group = QActionGroup(menu)
        for i, name in enumerate(VISUAL_STYLES):
            act = QAction(name, menu, checkable=True, checked=(i == self.visual_style))
            act.triggered.connect(lambda _=False, i=i: self._set_style(i))
            group.addAction(act)
            menu.addAction(act)
        button.setMenu(menu)
        self._style = button
        self.addPermanentWidget(button)

    def _snap_button(self):
        # 왼쪽(본체) 누르면 켜기/끄기, 오른쪽 화살표로 스냅 종류 — 엔진 객체스냅 버튼과 같은 역할
        button = QToolButton()
        button.setObjectName("statusButton")
        button.setText("객체스냅")
        button.setToolTip("객체스냅 — 끝점·중간점·중심점… 에 커서가 달라붙는다 (F3). ▾ 로 종류 선택")
        button.setCheckable(True)
        button.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)
        button.clicked.connect(lambda: (self.toggle_osnap(), self.refresh()))
        menu = QMenu(button)
        menu.aboutToShow.connect(lambda: self._fill_snap_menu(menu))
        button.setMenu(menu)
        self._toggles.append((button, lotcad.CAD_GetOSnapEnabled))
        self.addPermanentWidget(button)

    def _fill_snap_menu(self, menu):
        menu.clear()
        modes = lotcad.CAD_GetOSnapModes()
        for bit, name in SNAP_MODES:
            act = menu.addAction(name)
            act.setCheckable(True)
            act.setChecked(bool(modes & bit))
            # 고른 종류 하나만 뒤집는다 (메뉴를 열 때의 값을 기준으로 하지 않고 지금 값을 다시 읽는다)
            act.triggered.connect(lambda _=False, bit=bit: lotcad.CAD_SetOSnapModes(lotcad.CAD_GetOSnapModes() ^ bit))

    # ── 동작 (F3·F8·F10 키도 같은 함수) ──
    def _toggle_grid(self):
        self.grid_on = not self.grid_on
        lotcad.CAD_SetGridEnabled(self.grid_on)

    def _set_style(self, index):
        self.visual_style = index
        lotcad.CAD_SetVisualStyle(index)
        self.refresh()

    def toggle_ortho_tracking(self):
        lotcad.CAD_SetOrthoEnabled(not lotcad.CAD_GetOrthoEnabled())
        self.refresh()

    def toggle_polar(self):
        lotcad.CAD_SetPolarTracking(not polar_on(), 0.0)   # 0 = 각도 증분은 지금 값 유지
        self.refresh()

    def toggle_osnap(self):
        lotcad.CAD_SetOSnapEnabled(not lotcad.CAD_GetOSnapEnabled())
        self.refresh()

    def apply_initial(self):
        """엔진이 만들어진 직후 — 이 창이 들고 있는 값을 엔진에 한 번 맞춘다."""
        lotcad.CAD_SetGridEnabled(self.grid_on)
        lotcad.CAD_SetVisualStyle(self.visual_style)

    def _projection_text(self):
        return "Ortho" if self._owner.ortho else "Persp"

    def refresh(self):
        if not self._owner.view.ready:   # 엔진이 없으면 Get 함수가 의미 없다
            return
        for button, is_on in self._toggles:
            button.setChecked(bool(is_on()))
        self._style.setText(VISUAL_STYLES[self.visual_style] + " ")
        self._projection.setText(self._projection_text())
