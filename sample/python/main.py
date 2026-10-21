"""LotCAD 파이썬 샘플 — PySide6 창 안에 엔진 3D 뷰 + 리본 + 명령행 + 상태바.

준비: setup.bat (Windows) / ./setup.sh (macOS·Ubuntu)
실행: run.bat / ./run.sh

엔진은 sdk/python/lotcad 바인딩으로 부른다 — 헤더(LotCAD_API.h)에서 자동 생성된, 함수 전부가 든 모듈.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "..", "sdk", "python")))

# 엔진의 리눅스 임베드는 X11 창만 받는다 — Wayland 세션에서도 Qt 를 X11(XWayland)로 띄운다.
# (Wayland 로 뜨면 winId() 가 X11 창 번호가 아니라 엔진이 화면을 못 붙인다.) QApplication 보다 먼저.
if sys.platform.startswith("linux"):
    os.environ["QT_QPA_PLATFORM"] = "xcb"

from PySide6.QtWidgets import QApplication  # noqa: E402

import lotcad  # noqa: E402
import theme  # noqa: E402
from main_window import MainWindow  # noqa: E402


def main():
    app = QApplication(sys.argv)
    theme.apply(app)

    # models·fonts·textures 가 있는 SDK 폴더 — 엔진을 만들기 전에.
    lotcad.CAD_SetRuntimeAssetPath(lotcad.SDK_DIR)

    window = MainWindow()
    window.resize(1280, 840)
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
