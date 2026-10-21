"""다크 테마 — 엔진(ImGui)·MFC 샘플과 같은 색. 색을 바꾸려면 여기만 고친다."""
from PySide6.QtGui import QColor, QPalette

TAB_BAR_BG = "#1e1e1e"   # 탭 줄·상태바
BODY_BG = "#2b2b2d"      # 리본 본문·명령행
CAPTION_BG = "#343437"   # 그룹 이름 띠
SEPARATOR = "#46464a"
HOVER = "#3e3e42"
PRESSED = "#505056"
TEXT = "#e6e6e6"
TEXT_DIM = "#96969b"
ACCENT = "#6babf5"       # 켜진 버튼·활성 탭 밑줄 (엔진 강조 파랑)
WINDOW_BG = "#252526"
INPUT_BG = "#1e1e1e"
PROMPT = "#ffd14d"       # 진행 중 도구의 안내문 (엔진 명령행과 같은 앰버)

QSS = f"""
QWidget {{ color: {TEXT}; }}
QMainWindow, QMenu {{ background: {WINDOW_BG}; }}
QMenuBar {{ background: {TAB_BAR_BG}; }}
QMenuBar::item:selected, QMenu::item:selected {{ background: {HOVER}; }}

QTabWidget#ribbon::pane {{ background: {BODY_BG}; border: none; border-bottom: 1px solid {SEPARATOR}; }}
QTabWidget#ribbon QTabBar {{ background: {TAB_BAR_BG}; }}
QTabWidget#ribbon QTabBar::tab {{ background: {TAB_BAR_BG}; color: {TEXT_DIM}; padding: 5px 14px; border: none; }}
QTabWidget#ribbon QTabBar::tab:selected {{ color: {TEXT}; border-bottom: 2px solid {ACCENT}; }}
QTabWidget#ribbon QTabBar::tab:hover {{ color: {TEXT}; }}
QFrame#ribbonGroup {{ background: {BODY_BG}; border-right: 1px solid {SEPARATOR}; }}
QLabel#ribbonCaption {{ background: {CAPTION_BG}; color: {TEXT_DIM}; border-radius: 3px; padding: 1px 6px; }}

QToolButton {{ background: transparent; border: 1px solid transparent; border-radius: 4px; padding: 3px 8px; }}
QToolButton:hover {{ background: {HOVER}; }}
QToolButton:pressed {{ background: {PRESSED}; }}
QToolButton:checked {{ background: rgba(107, 171, 245, 0.30); border-color: {ACCENT}; }}

QStatusBar {{ background: {TAB_BAR_BG}; border-top: 1px solid {SEPARATOR}; }}
QStatusBar::item {{ border: none; }}
QToolButton#statusButton {{ background: {BODY_BG}; border-color: {SEPARATOR}; color: {TEXT_DIM}; margin: 2px 1px; }}
QToolButton#statusButton:checked {{ background: rgba(107, 171, 245, 0.35); border-color: {ACCENT}; color: {TEXT}; }}
QToolButton#statusButton:hover {{ background: {HOVER}; }}

QWidget#commandLine {{ background: {BODY_BG}; border-top: 1px solid {SEPARATOR}; }}
QPlainTextEdit, QLineEdit {{ background: {INPUT_BG}; border: 1px solid {SEPARATOR}; border-radius: 3px; }}
QLineEdit:focus {{ border-color: {ACCENT}; }}
QLabel#prompt {{ color: {TEXT_DIM}; }}
QLabel#prompt[active="true"] {{ color: {PROMPT}; }}
"""


def apply(app):
    app.setStyle("Fusion")   # OS 마다 다른 기본 스타일 대신 — 세 OS 에서 같은 모양
    palette = QPalette()
    for role, color in [
        (QPalette.ColorRole.Window, WINDOW_BG), (QPalette.ColorRole.Base, INPUT_BG),
        (QPalette.ColorRole.AlternateBase, BODY_BG), (QPalette.ColorRole.Button, BODY_BG),
        (QPalette.ColorRole.Text, TEXT), (QPalette.ColorRole.WindowText, TEXT),
        (QPalette.ColorRole.ButtonText, TEXT), (QPalette.ColorRole.Highlight, ACCENT),
        (QPalette.ColorRole.ToolTipBase, BODY_BG), (QPalette.ColorRole.ToolTipText, TEXT),
    ]:
        palette.setColor(role, QColor(color))
    app.setPalette(palette)
    app.setStyleSheet(QSS)
