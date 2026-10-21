"""리본 — 탭 한 줄 + 그룹(버튼 3줄 격자) + 그룹 이름. 엔진(3dEngine) 리본과 같은 모양.

이 파일은 CAD 를 모른다 — 버튼마다 실행할 함수를 받는다. 어떤 버튼을 둘지는 main_window.py.

    tab = ribbon.add_tab("홈")
    group = tab.add_group("실행")
    group.add("실행취소", lotcad.CAD_Undo)
    group.add("직교 투영", toggle, is_on=lambda: ortho)   # 켜짐 표시가 있는 버튼
"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QGridLayout, QHBoxLayout, QLabel, QTabWidget, QToolButton, QVBoxLayout, QWidget

ROWS = 3   # 그룹당 버튼 줄 수


class RibbonGroup(QFrame):
    def __init__(self, caption):
        super().__init__()
        self.setObjectName("ribbonGroup")
        self._grid = QGridLayout()
        self._grid.setSpacing(2)
        self._count = 0
        self.toggles = []   # (버튼, is_on)

        label = QLabel(caption)
        label.setObjectName("ribbonCaption")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 4, 6, 2)
        layout.setSpacing(2)
        layout.addLayout(self._grid)
        layout.addStretch(1)
        layout.addWidget(label)

    def add(self, text, action, is_on=None, tip=None):
        button = QToolButton()
        button.setText(text)
        button.setToolTip(tip or text)
        button.setFocusPolicy(Qt.FocusPolicy.NoFocus)   # 눌러도 3D 뷰·명령행의 포커스를 뺏지 않는다
        button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        button.clicked.connect(lambda: action())
        if is_on:
            button.setCheckable(True)
            button.setChecked(is_on())
            self.toggles.append((button, is_on))
        # 위 → 아래로 3줄을 채우고 다음 열
        self._grid.addWidget(button, self._count % ROWS, self._count // ROWS)
        self._count += 1
        return button


class RibbonTab(QWidget):
    def __init__(self):
        super().__init__()
        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(4, 4, 4, 4)
        self._layout.setSpacing(6)
        self._layout.addStretch(1)
        self.groups = []

    def add_group(self, caption):
        group = RibbonGroup(caption)
        self._layout.insertWidget(self._layout.count() - 1, group)   # 끝의 여백(stretch) 앞에
        self.groups.append(group)
        return group


class Ribbon(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("ribbon")
        self.setDocumentMode(True)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tabs = []

    def add_tab(self, title):
        tab = RibbonTab()
        self.addTab(tab, title)
        self.tabs.append(tab)
        return tab

    def refresh(self):
        """켜짐 표시 다시 맞추기 — 상태가 메뉴·단축키 등 밖에서 바뀌었을 때."""
        for tab in self.tabs:
            for group in tab.groups:
                for button, is_on in group.toggles:
                    button.setChecked(is_on())
