"""명령행 — 3D 뷰 아래의 오토캐드식 명령 창.

    ┌ 기록 ─────────────────────────────────┐
    │ 명령: c                                │
    │ 원: 중심 클릭 또는 좌표 입력            │
    ├────────────────────────────────────────┤
    │ 원: 반지름 …(앰버)  [ 입력란 ........ ] │
    └────────────────────────────────────────┘

입력은 엔진 명령행과 같은 규칙으로 CAD_ExecuteCommand 에 넘긴다.
  - 도구가 없으면 명령 이름(line / l / 선 …), 도구가 진행 중이면 값(2,3 / 50 …)
  - 빈 Enter: 진행 중 도구엔 Enter 키(폴리선 끝내기·선택 확정), 유휴면 직전 명령 반복
  - Esc: 진행 중 도구 취소,  ↑/↓: 입력 기록
안내문은 엔진이 CAD_SetOnPrompt 로 알려 준다(바뀔 때만, CAD_Tick 안 — 같은 스레드라 바로 위젯을 고쳐도 된다).
"""
from PySide6.QtCore import QEvent, Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit, QVBoxLayout, QWidget

import lotcad

GLFW_KEY_ENTER = 257
LOG_LINES = 4      # 기록 창에 보이는 줄 수
HISTORY_MAX = 50


def tool_active():
    """엔진에 값을 기다리는 도구가 있는가 — 안내문이 있으면 있다."""
    return bool(lotcad.CAD_GetPrompt())


class CommandLine(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("commandLine")

        self.log = QPlainTextEdit(readOnly=True)
        self.log.setMaximumBlockCount(300)   # 무한정 쌓지 않는다
        self.log.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.log.setFixedHeight(self.log.fontMetrics().lineSpacing() * LOG_LINES + 12)

        self.prompt = QLabel("명령:")
        self.prompt.setObjectName("prompt")
        self.edit = QLineEdit()
        self.edit.returnPressed.connect(self.submit)
        self.edit.installEventFilter(self)   # Esc · ↑ · ↓

        row = QHBoxLayout()
        row.addWidget(self.prompt)
        row.addWidget(self.edit, 1)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 6, 6, 6)
        layout.addWidget(self.log)
        layout.addLayout(row)

        self._history = []
        self._history_pos = -1
        self._last_logged = ""
        self.append("명령을 입력하세요 — 예: l (선), c (원), b (박스).  3D 뷰에서 바로 타이핑해도 됩니다.")

        # 파이썬 함수를 그대로 넘긴다 — 바인딩이 붙잡아 둬서 GC 에 거둬지지 않는다
        lotcad.CAD_SetOnPrompt(self._on_prompt)

    def shutdown(self):
        lotcad.CAD_SetOnPrompt(None)

    # ── 기록·안내문 ──
    def append(self, line):
        self.log.appendPlainText(line)

    def _on_prompt(self, text):
        # 엔진 명령행처럼 안내문이 **바뀔 때마다** 기록에 한 줄 — 흐름이 보이게
        if text and text != self._last_logged:
            self.append(text)
            self._last_logged = text
        if not text:
            self._last_logged = ""   # 유휴로 돌아가면 다음 안내문을 다시 기록
        self.prompt.setText(text or "명령:")
        self.prompt.setProperty("active", bool(text))   # 앰버/흐림 — theme.py 의 QSS
        self.prompt.style().unpolish(self.prompt)
        self.prompt.style().polish(self.prompt)

    # ── 입력 ──
    def type_text(self, text):
        """3D 뷰에서 친 글자를 이어받는다 — 오토캐드처럼 뷰를 보면서 바로 타이핑."""
        self.edit.setFocus()
        self.edit.insert(text)

    def submit(self):
        text = self.edit.text().strip()
        self.edit.clear()
        self._history_pos = -1
        if not text:
            if tool_active():
                # 진행 중 도구에 Enter — CAD_ExecuteCommand 는 빈 문자열을 안 받으므로 키로 보낸다
                lotcad.CAD_OnKeyDown(GLFW_KEY_ENTER, 0)
                lotcad.CAD_OnKeyUp(GLFW_KEY_ENTER, 0)
            elif self._history:
                self.run(self._history[-1])   # 유휴 Enter = 직전 명령 반복
            return
        if not self._history or self._history[-1] != text:
            self._history.append(text)
            del self._history[:-HISTORY_MAX]
        self.run(text)

    def run(self, text):
        active = tool_active()
        self.append(("  > " if active else "명령: ") + text)
        if not lotcad.CAD_ExecuteCommand(text):
            self.append("  (진행 중인 도구가 이 값을 받지 않았습니다)" if active else f"알 수 없는 명령: {text}")

    def cancel(self):
        self.edit.clear()
        self._history_pos = -1
        if tool_active():
            self.append("*취소*")
        lotcad.CAD_ExecuteCommand("esc")   # 엔진이 ESC 키로 바꿔 진행 중 도구를 끝낸다

    def _recall(self, step):
        if not self._history:
            return
        n = len(self._history)
        if self._history_pos < 0:
            self._history_pos = n
        self._history_pos = max(0, min(n, self._history_pos + step))
        self.edit.setText(self._history[self._history_pos] if self._history_pos < n else "")

    def eventFilter(self, obj, event):
        if obj is self.edit and event.type() == QEvent.Type.KeyPress:
            key = event.key()
            if key == Qt.Key.Key_Escape:
                self.cancel()
                return True
            if key == Qt.Key.Key_Up:
                self._recall(-1)
                return True
            if key == Qt.Key.Key_Down:
                self._recall(+1)
                return True
        return super().eventFilter(obj, event)
