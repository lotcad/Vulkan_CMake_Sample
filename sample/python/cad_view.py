"""3D 뷰 — 엔진이 그리는 네이티브 창(QWindow)을 위젯 안에 넣는다.

엔진을 붙이는 순서 (MFC·WPF·QML 샘플과 같다):
  1) 창이 화면에 나타나고(expose) 실제 크기를 가질 때까지 기다린다
  2) CAD_AttachView(창 핸들, 물리 픽셀 크기) → CAD_CreateEngine
  3) 16ms 마다 CAD_Tick, 크기가 바뀌면 CAD_ResizeView, 마우스는 CAD_OnMouse*
  4) 닫을 때 창이 헐리기 **전에** CAD_DetachView → CAD_DestroyEngine

창 핸들은 winId() — Windows 는 HWND, macOS 는 NSView, 리눅스는 X11 창 번호.
"""
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QWindow
from PySide6.QtWidgets import QVBoxLayout, QWidget

import lotcad

# 엔진 입력은 GLFW 규약을 따른다
GLFW_MOUSE = {
    Qt.MouseButton.LeftButton: 0,
    Qt.MouseButton.RightButton: 1,
    Qt.MouseButton.MiddleButton: 2,
}


def glfw_mods(m):
    mods = 0
    if m & Qt.KeyboardModifier.ShiftModifier:
        mods |= 0x1
    if m & Qt.KeyboardModifier.ControlModifier:
        mods |= 0x2
    if m & Qt.KeyboardModifier.AltModifier:
        mods |= 0x4
    if m & Qt.KeyboardModifier.MetaModifier:
        mods |= 0x8
    return mods


class EngineWindow(QWindow):
    """엔진이 직접 그리는 창. Qt 는 이 창에 아무것도 그리지 않는다."""

    def __init__(self, view):
        super().__init__()
        self._view = view
        self.created = False
        self._last_size = (0, 0)

    def _pixels(self):
        # 엔진엔 물리 픽셀 — 레티나·배율 화면에서 Vulkan 스왑체인 크기와 맞아야 한다
        r = self.devicePixelRatio()
        return max(1, int(self.width() * r)), max(1, int(self.height() * r))

    # ── 생성·크기·정리 ──
    def exposeEvent(self, event):
        # 너무 일찍(크기 0, 화면에 붙기 전) 붙이면 스왑체인을 잘못된 크기로 만들었다가 다시 만들며 깨질 수 있다
        if not self.created and self.isExposed() and self.width() > 0 and self.height() > 0:
            self._create_engine()
        super().exposeEvent(event)

    def _create_engine(self):
        w, h = self._pixels()
        lotcad.CAD_AttachView(int(self.winId()), w, h)
        if not lotcad.CAD_CreateEngine():
            print("[python] CAD_CreateEngine 실패")
            return
        lotcad.CAD_SetIgnoreCloseRequest(True)   # 창은 호스트(Qt)가 닫는다
        self.created = True
        self._last_size = (w, h)
        self._view.engine_created()

    def resizeEvent(self, event):
        if self.created:
            size = self._pixels()
            if size != self._last_size:   # 같은 크기로 다시 부르면 스왑체인을 괜히 새로 만든다
                self._last_size = size
                lotcad.CAD_ResizeView(*size)
        super().resizeEvent(event)

    def destroy_engine(self):
        if self.created:
            lotcad.CAD_DetachView()
            lotcad.CAD_DestroyEngine()
            self.created = False

    # ── 입력 → 엔진 (좌표는 물리 픽셀) ──
    def _xy(self, event):
        r = self.devicePixelRatio()
        p = event.position()
        return p.x() * r, p.y() * r

    def mousePressEvent(self, event):
        if self.created:
            x, y = self._xy(event)
            lotcad.CAD_OnMouseDown(GLFW_MOUSE.get(event.button(), 0), x, y, glfw_mods(event.modifiers()))

    def mouseReleaseEvent(self, event):
        if self.created:
            x, y = self._xy(event)
            lotcad.CAD_OnMouseUp(GLFW_MOUSE.get(event.button(), 0), x, y, glfw_mods(event.modifiers()))

    def mouseMoveEvent(self, event):
        if self.created:
            lotcad.CAD_OnMouseMove(*self._xy(event))

    def wheelEvent(self, event):
        if self.created:
            x, y = self._xy(event)
            d = event.angleDelta()   # 1/8도 단위, 120 = 한 칸
            lotcad.CAD_OnMouseWheel(x, y, d.x() / 120.0, d.y() / 120.0)

    def keyPressEvent(self, event):
        # 키는 화면(호스트)이 먼저 본다 — 글자는 명령행으로, F3/F8/F10 은 상태바 토글로 (MainWindow)
        self._view.key_pressed(event)


class CadView(QWidget):
    """EngineWindow 를 담는 위젯 + 프레임 타이머."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.engine_window = EngineWindow(self)
        container = QWidget.createWindowContainer(self.engine_window, self)
        container.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        container.setMinimumSize(200, 150)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(container)

        self.on_engine_ready = None   # 엔진이 만들어진 직후 한 번 — 처음 설정(투영·그리드 등)
        self.on_key = None            # 3D 뷰에서 누른 키

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)

    @property
    def ready(self):
        return self.engine_window.created

    def engine_created(self):
        self._timer.start(16)   # 약 60fps
        if self.on_engine_ready:
            self.on_engine_ready()

    def _tick(self):
        # 최소화 등으로 화면에 없으면 그릴 곳이 없다 — 그 프레임은 건너뛴다
        if self.engine_window.isExposed():
            lotcad.CAD_Tick()

    def key_pressed(self, event):
        if self.on_key:
            self.on_key(event)

    def shutdown(self):
        self._timer.stop()
        self.engine_window.destroy_engine()
