"""메인 창 — 리본(위) · 3D 뷰 · 명령행 · 상태바(아래)를 묶고, 리본 버튼에 엔진 명령을 단다.

대부분의 버튼은 엔진 명령행 이름으로 부른다(CAD_ExecuteCommand — 명령행에 그대로 쳐도 같은 동작).
엔진 명령이 수백 개라 버튼마다 C API 를 따로 두는 대신 이 길을 쓴다. 결과가 필요한 건 C API 를 직접(차집합 등).

⚠️ 엔진 명령 중 **자체 패널·대화상자를 여는 것**(array, dp, section, nav, particle …)은 호스트 창 안에서는
   그 창이 그려지지 않는다. 명령행에서 값을 묻는 명령(3a, dim …)이나 C API 를 쓴다.
"""
import ctypes

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QDockWidget, QFileDialog, QMainWindow, QMessageBox, QVBoxLayout, QWidget

import analysis
import lotcad
from cad_view import CadView
from command_line import CommandLine
from ribbon import Ribbon
from status_bar import CadStatusBar


def command(name):
    """엔진 명령행 이름으로 부르는 버튼 동작."""
    return lambda: lotcad.CAD_ExecuteCommand(name)


def selected_ids():
    return [lotcad.CAD_GetSelectedObjectId(i) for i in range(lotcad.CAD_GetSelectedCount())]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LotCAD — Python (PySide6)")
        self.ortho = True            # 투영 — 엔진 기본은 CAD 식 직교
        self._subtract_base = []     # 차집합 1단계에서 기억한 기준 솔리드

        self.view = CadView()
        self.command_line = CommandLine()
        self.ribbon = Ribbon()
        self._build_ribbon()
        self._build_menu()

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.ribbon)
        layout.addWidget(self.view, 1)
        layout.addWidget(self.command_line)
        self.setCentralWidget(central)

        self.status = CadStatusBar(self)   # self.view 를 쓰므로 뷰 다음에
        self.setStatusBar(self.status)

        # 해석 패널 — 오른쪽 독(처음엔 숨김). 리본 해석 탭·해석 메뉴가 연다.
        self.analysis = analysis.AnalysisPanel()
        self.analysis_dock = QDockWidget("해석", self)
        self.analysis_dock.setWidget(self.analysis)
        self.analysis_dock.setMinimumWidth(340)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.analysis_dock)
        self.analysis_dock.hide()

        self.view.on_engine_ready = self._engine_ready
        self.view.on_key = self._view_key

    # ── 엔진 준비·종료 ──
    def _engine_ready(self):
        # 상태바·리본이 보여 주는 값과 엔진을 처음에 한 번 맞춘다
        lotcad.CAD_SetProjection(self.ortho)
        self.status.apply_initial()
        self.status.refresh()
        self.ribbon.refresh()
        self.analysis.start_polling()

    def closeEvent(self, event):
        # 창이 헐리기 **전에** 엔진을 정리해야 타이머가 사라진 화면에 그리지 않는다
        self.command_line.shutdown()
        self.analysis.shutdown()
        self.view.shutdown()
        super().closeEvent(event)

    # ── 키: 3D 뷰에서 누른 키 ──
    def _view_key(self, event):
        key = event.key()
        if key == Qt.Key.Key_F3:
            self.status.toggle_osnap()
        elif key == Qt.Key.Key_F8:
            self.status.toggle_ortho_tracking()
        elif key == Qt.Key.Key_F10:
            self.status.toggle_polar()
        elif key in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.command_line.submit()
        elif key == Qt.Key.Key_Escape:
            self.command_line.cancel()
        elif event.text() and event.text().isprintable() and not event.text().isspace():
            self.command_line.type_text(event.text())   # 오토캐드처럼 뷰에서 바로 타이핑

    # ── 투영 — 메뉴·리본·상태바가 같은 상태를 본다 ──
    def set_ortho(self, ortho):
        self.ortho = ortho
        lotcad.CAD_SetProjection(ortho)   # True=직교(Ortho) False=원근(Persp)
        self.ribbon.refresh()
        self.status.refresh()

    # ── 메뉴 ──
    def _build_menu(self):
        menu = self.menuBar().addMenu("파일(&F)")
        for text, shortcut, slot in [("열기(&O)...", QKeySequence.StandardKey.Open, self._open),
                                     ("다른 이름으로 저장(&S)...", QKeySequence.StandardKey.SaveAs, self._save_as),
                                     ("내보내기(&E)...", None, self._export)]:
            act = QAction(text, self)
            if shortcut:
                act.setShortcut(shortcut)
            act.triggered.connect(slot)
            menu.addAction(act)
        menu.addSeparator()
        menu.addAction("끝내기(&X)", self.close)

        menu = self.menuBar().addMenu("해석(&A)")
        menu.addAction("바람 터널", lambda: self.open_analysis("wind"))
        menu.addAction("물", lambda: self.open_analysis("water"))
        menu.addAction("구조 해석", lambda: self.open_analysis("sim"))
        menu.addSeparator()
        menu.addAction("모든 해석 끄기", self._stop_analyses)   # 패널을 닫아도 해석은 계속 돈다(엔진 상태)

    # ── 해석 — 엔진 해석 패널 대신 호스트 패널(analysis.py) ──
    def open_analysis(self, page):
        self.analysis.show_page(page)
        self.analysis_dock.show()
        self.analysis_dock.raise_()
        self.analysis.refresh()

    def _stop_analyses(self):
        analysis.call("wind", {"op": "stop"})
        analysis.call("water", {"op": "stop"})
        analysis.call("sim", {"op": "close"})
        self.analysis.refresh()

    # 파일 선택은 호스트(Qt)가 맡고 엔진에는 경로만 넘긴다 — 포맷은 확장자로 엔진이 판별
    def _open(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "열기", "",
            "CAD 파일 (*.lot *.obj *.stl *.dxf *.dwg *.ply *.gltf *.glb);;프로젝트 (*.lot);;모든 파일 (*)")
        if not path:
            return
        if lotcad.CAD_OpenFile(path):
            lotcad.CAD_ZoomExtents()   # 연 것이 화면 밖일 수 있다
        else:
            self._report("열기 실패")

    def _save_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "다른 이름으로 저장", "", "프로젝트 (*.lot)")
        if path and not lotcad.CAD_SaveAs(path if "." in path.split("/")[-1] else path + ".lot", False):
            self._report("저장 실패")

    def _export(self):
        path, _ = QFileDialog.getSaveFileName(self, "내보내기", "", "STL (*.stl);;DXF (*.dxf);;OBJ (*.obj);;glTF (*.glb)")
        if path and not lotcad.CAD_ExportFile(path, False):
            self._report("내보내기 실패")

    def _report(self, fallback):
        # 실패 이유는 엔진이 상태 메시지로 남긴다(포맷 미지원·깨진 파일 등)
        QMessageBox.warning(self, "LotCAD", lotcad.CAD_GetStatusMessage() or fallback)

    # ── 차집합 — 두 번 눌러 기준 → 뺄 것 ──
    # 엔진 선택 목록은 id 순이라 "먼저 고른 것" 을 알 수 없어, 오토캐드 SUBTRACT 처럼 두 단계로 받는다.
    def _subtract_step(self):
        ids = selected_ids()
        log = self.command_line.append
        if not self._subtract_base:
            if not ids:
                log("차집합: 기준이 될 솔리드를 먼저 선택하고 다시 누르세요")
                return
            self._subtract_base = ids
            log(f"차집합: 기준 {len(ids)}개 기억함 — 뺄 솔리드를 선택하고 차집합을 다시 누르세요 (빈 선택이면 취소)")
        else:
            base = self._subtract_base
            cuts = [i for i in ids if i not in base]
            if not cuts:
                log("차집합: 취소")
            else:
                # 목록을 그대로 넘긴다 — 바인딩이 uint32 배열로 바꿔 준다. False, False = 원본 삭제, 기준을 한 덩어리로.
                # 결과 id 칸을 꼭 준다(None 이면 개수만 묻는 것이라 해 본 뒤 되돌린다). 반환 음수 = 이유 코드
                out = lotcad.buffer(ctypes.c_uint32, 1)
                made = lotcad.CAD_BooleanSubtract(base, len(base), cuts, len(cuts), False, False, out, 1)
                log(f"차집합: 기준 {len(base)}개에서 {len(cuts)}개를 뺌" if made > 0
                    else f"차집합 실패: {lotcad.CAD_GetLastError()}")
            self._subtract_base = []
        self.ribbon.refresh()

    # ── 리본 — 엔진 리본과 같은 탭·그룹·명령 ──
    def _build_ribbon(self):
        r = self.ribbon

        home = r.add_tab("홈")
        g = home.add_group("기즈모")          # 화면 핸들을 끌어 변형
        g.add("이동", command("gm"))
        g.add("회전", command("gr"))
        g.add("축척", command("gs"))
        g = home.add_group("편집")            # 기준점 → 목적지(또는 값 입력)
        g.add("이동", command("m"))
        g.add("회전", command("ro"))
        g.add("축척", command("sc"))
        g.add("복사", command("cp"))
        g.add("배열", command("3a"))          # ar 은 대화상자 — 3a 는 명령행에 값을 묻는다
        g = home.add_group("선택")
        g.add("전체 선택", lotcad.CAD_RequestSelectAll)
        g.add("삭제", lotcad.CAD_RequestDeleteSelected)
        g.add("모두 지우기", lotcad.CAD_RequestClearAll)
        g = home.add_group("실행")
        g.add("실행취소", lotcad.CAD_Undo)
        g.add("다시실행", lotcad.CAD_Redo)
        g = home.add_group("뷰")
        g.add("전체보기", lotcad.CAD_ZoomExtents)
        g.add("선택 맞춤", lotcad.CAD_FocusSelected)
        g.add("직교 투영", lambda: self.set_ortho(not self.ortho), is_on=lambda: self.ortho)
        g.add("아이소", lambda: lotcad.CAD_SetView(3))   # 0=정면 1=평면 2=우측 3=아이소
        g.add("평면", lambda: lotcad.CAD_SetView(1))
        g.add("정면", lambda: lotcad.CAD_SetView(0))
        g.add("우측면", lambda: lotcad.CAD_SetView(2))

        two_d = r.add_tab("2D")
        g = two_d.add_group("그리기")
        for text, name in [("선", "l"), ("사각형", "rec"), ("원", "c"), ("정다각형", "pol"),
                           ("호", "a"), ("폴리선", "pl"), ("문자", "text"), ("치수", "dim")]:
            g.add(text, command(name))
        g = two_d.add_group("수정")
        for text, name in [("오프셋", "of"), ("대칭", "mi"), ("자르기", "tr"),
                           ("연장", "ex"), ("필렛", "fil"), ("모따기", "cha")]:
            g.add(text, command(name))

        three_d = r.add_tab("3D")
        g = three_d.add_group("프리미티브")
        g.add("박스", command("b"))                  # 3단계 스케치
        g.add("큐브", lotcad.CAD_RequestAddCube)      # 기본 크기로 바로
        for text, name in [("구", "sphere"), ("원기둥", "cyl"), ("원뿔", "cone"), ("토러스", "torus")]:
            g.add(text, command(name))
        g = three_d.add_group("형상")                # 닫힌 스케치 → 솔리드
        for text, name in [("돌출", "x"), ("회전체", "rev"), ("스윕", "sw"), ("로프트", "lo"), ("셸", "sh")]:
            g.add(text, command(name))
        g = three_d.add_group("불리언")
        g.add("합집합", command("union"))
        g.add("차집합", self._subtract_step, is_on=lambda: bool(self._subtract_base),
              tip="기준 선택 → 차집합 → 뺄 것 선택 → 차집합")
        g.add("교집합", command("intersect"))

        # 해석 — 엔진 리본의 해석 탭과 같은 버튼. 엔진은 자기 패널(ImGui)을 여는데 호스트 창에선 안 그려지므로
        # 호스트 해석 패널을 연다. 대상은 지금 선택한 솔리드.
        ana = r.add_tab("해석")
        g = ana.add_group("유체")
        g.add("풍동", lambda: self.open_analysis("wind"), tip="바람 터널 — 고른 솔리드 둘레 공기 흐름(속도·압력 단면, 연기, 표면 압력)")
        g.add("물", lambda: self.open_analysis("water"), tip="물 — 고른 닫힌 솔리드를 그릇으로 물을 채워 출렁임(기울이기·흔들기)")
        g = ana.add_group("구조")
        g.add("구조해석", lambda: self.open_analysis("sim"), tip="구조·열·진동·좌굴 — 고정 면·하중 면, 재료 고르고 실행")
