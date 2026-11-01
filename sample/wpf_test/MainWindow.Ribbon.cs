using System;
using System.Linq;
using System.Windows;
using System.Windows.Controls;
using I = LotCadWpf.RibbonIcon;

namespace LotCadWpf
{
    // 리본 구성 — 어떤 탭·그룹에 어떤 엔진 명령을 둘지. MFC 샘플(LotCAD_MFCDlg_Ribbon.cpp)과 같은 탭·그룹·명령이다.
    // 버튼을 더하거나 빼려면 이 파일만 고치면 된다 — 그리기·마우스는 RibbonBar.cs 가 맡는다.
    //
    // 대부분의 버튼은 엔진 명령행 이름으로 부른다(3D 뷰에서 그대로 쳐도 같은 동작). 엔진 명령이 200개가 넘어
    // 하나씩 C API 를 뚫는 대신 CAD_ExecuteCommand 로 가는 것이 이 샘플의 방침이다.
    // ⚠️ 엔진 명령 중 **자체 패널·대화상자를 여는 것**(array, dp, section, nav, particle …)은 임베드(호스트 창 안)에선
    //    그 창이 그려지지 않아 눌러도 아무 일이 없어 보인다 — 값을 3D 뷰에서 묻는 명령(3a, dim …)이나 C API + 오른쪽 패널로 대신한다.
    //    MFC 샘플의 도구 탭 '단면 · 내비 · 파티클' 은 그 샘플의 호스트 패널이라 여기엔 없다.
    public partial class MainWindow
    {
        // 버튼이므로 진행 중인 도구를 먼저 끝내고 시작한다(StartCommand — 선 그리던 중 사각형 버튼도 바로 바뀜)
        static Action Cmd(string name) => () => CadApi.StartCommand(name);

        void BuildRibbon()
        {
            var r = Ribbon;
            // 누른 뒤 키보드는 렌더 창(엔진)으로 — 명령이 묻는 값을 바로 친다. 패널의 입력란은 누르면 다시 포커스를 가져간다
            r.Clicked += FocusViewLater;

            // ── 홈 ──
            r.AddTab("홈");

            r.AddGroup("기즈모");   // 화면 핸들을 끌어 변형 — 기준점을 묻지 않는다
            r.AddLarge("이동", I.GizmoMove,   Cmd("gm"));
            r.AddLarge("회전", I.GizmoRotate, Cmd("gr"));
            r.AddLarge("축척", I.GizmoScale,  Cmd("gs"));

            r.AddGroup("편집");     // 기준점 → 목적지(또는 값 입력)
            r.AddLarge("이동", I.Move,   Cmd("m"));
            r.AddSmall("회전", I.Rotate, Cmd("ro"));
            r.AddSmall("축척", I.Scale,  Cmd("sc"));
            r.AddSmall("복사", I.Copy,   Cmd("cp"));
            r.AddSmall("배열", I.Array,  Cmd("3a"));   // ar 은 대화상자 — 3a 는 "r 열 행 층 dx dy dz" 를 묻는다

            r.AddGroup("선택");
            r.AddLarge("전체 선택",   I.SelectAll, Cmd("selectall"));
            r.AddSmall("삭제",        I.Delete,    Cmd("delete"));
            r.AddSmall("모두 지우기", I.ClearAll,  () => CadApi.CAD_ClearAll());

            r.AddGroup("실행");
            r.AddLarge("실행취소", I.Undo, () => CadApi.CAD_Undo());
            r.AddLarge("다시실행", I.Redo, () => CadApi.CAD_Redo());

            r.AddGroup("뷰");
            r.AddLarge("전체보기",  I.ZoomExtents, () => CadApi.CAD_ZoomExtents());
            r.AddSmall("선택 맞춤", I.Focus,       () => CadApi.CAD_FocusSelected());
            // 켜짐 = 직교 투영. 엔진에 읽는 함수(CAD_GetProjection)가 있어 메뉴로 바꿔도 표시가 맞는다
            r.AddSmall("직교 투영", I.Projection,  CadApi.ToggleProjection, CadApi.IsOrtho);
            r.AddSmall("아이소",    I.ViewIso,     () => CadApi.CAD_SetView(3));   // 0=Front 1=Top 2=Right 3=Iso
            r.AddSmall("평면",      I.ViewTop,     () => CadApi.CAD_SetView(1));
            r.AddSmall("정면",      I.ViewFront,   () => CadApi.CAD_SetView(0));
            r.AddSmall("우측면",    I.ViewRight,   () => CadApi.CAD_SetView(2));

            // ── 2D ──
            r.AddTab("2D");

            r.AddGroup("그리기");
            r.AddLarge("선",       I.Line,      Cmd("l"));
            r.AddSmall("사각형",   I.Rectangle, Cmd("rec"));
            r.AddSmall("원",       I.Circle,    Cmd("c"));
            r.AddSmall("정다각형", I.Polygon,   Cmd("pol"));
            r.AddSmall("호",       I.Arc,       Cmd("a"));
            r.AddSmall("폴리선",   I.Polyline,  Cmd("pl"));
            r.AddSmall("문자",     I.Text,      Cmd("text"));
            r.AddSmall("치수",     I.Dimension, Cmd("dim"));   // 정렬 치수 (dp 는 치수 패널이라 임베드에선 안 보인다)

            r.AddGroup("수정");
            r.AddLarge("오프셋", I.Offset,  Cmd("of"));
            r.AddSmall("대칭",   I.Mirror,  Cmd("mi"));
            r.AddSmall("자르기", I.Trim,    Cmd("tr"));
            r.AddSmall("연장",   I.Extend,  Cmd("ex"));
            r.AddSmall("필렛",   I.Fillet,  Cmd("fil"));
            r.AddSmall("모따기", I.Chamfer, Cmd("cha"));

            // ── 3D ──
            r.AddTab("3D");

            r.AddGroup("프리미티브");
            r.AddLarge("박스",   I.Box,      Cmd("b"));        // 3단계 스케치
            r.AddSmall("큐브",   I.Box,      Cmd("cube"));     // 기본 크기로 바로
            r.AddSmall("구",     I.Sphere,   Cmd("sphere"));
            r.AddSmall("원기둥", I.Cylinder, Cmd("cyl"));
            r.AddSmall("원뿔",   I.Cone,     Cmd("cone"));
            r.AddSmall("토러스", I.Torus,    Cmd("torus"));

            r.AddGroup("형상");     // 닫힌 스케치 → 솔리드
            r.AddLarge("돌출",   I.Extrude, Cmd("x"));
            r.AddSmall("회전체", I.Revolve, Cmd("rev"));
            r.AddSmall("스윕",   I.Sweep,   Cmd("sw"));
            r.AddSmall("로프트", I.Loft,    Cmd("lo"));
            r.AddSmall("셸",     I.Shell,   Cmd("sh"));

            r.AddGroup("편집");
            r.AddLarge("합집합",   I.Union,      Cmd("union"));
            // 켜짐 = 기준을 기억하고 뺄 것을 기다리는 중
            r.AddSmall("차집합",   I.Difference, SubtractStep, () => _subtractBase.Length > 0);
            r.AddSmall("교집합",   I.Intersect,  Cmd("intersect"));
            r.AddSmall("슬라이스", I.Slice,      Cmd("sl"));   // 평면으로 자른다

            // ── 도구 — 엔진에선 자체 패널이 여는 기능들. 임베드에선 그 패널이 안 보여 오른쪽 패널로 연다 ──
            r.AddTab("도구");

            r.AddGroup("해석");
            r.AddLarge("바람 터널", I.AnaWind,   () => TogglePanel(Analysis, 0, () => Analysis.ShowPage(0)), () => IsOpen(Analysis, Analysis.Page, 0));
            r.AddLarge("물",        I.AnaWater,  () => TogglePanel(Analysis, 1, () => Analysis.ShowPage(1)), () => IsOpen(Analysis, Analysis.Page, 1));
            r.AddLarge("구조 해석", I.AnaStress, () => TogglePanel(Analysis, 2, () => Analysis.ShowPage(2)), () => IsOpen(Analysis, Analysis.Page, 2));

            r.AddGroup("모델");
            r.AddLarge("노드 그래프", I.Graph,      ToggleGraph, () => _graphOn);
            r.AddLarge("분해도",      I.Explode,    () => TogglePanel(Tools, 0, () => Tools.ShowPage(0)), () => IsOpen(Tools, Tools.Page, 0));
            r.AddLarge("메시 수리",   I.MeshRepair, () => TogglePanel(Tools, 1, () => Tools.ShowPage(1)), () => IsOpen(Tools, Tools.Page, 1));

            r.AddGroup("이미지");
            r.AddLarge("붙이기",      I.ImageAttach,     AttachImage);
            r.AddSmall("회전",        I.ImageRotate,     Cmd("imagerotate 90"));
            r.AddSmall("뒤집기",      I.ImageFlip,       Cmd("imageflip h"));
            r.AddSmall("배경 지우기", I.ImageBackground, Cmd("imagebg"));     // 지울 배경을 클릭
            r.AddSmall("자르기",      I.ImageCrop,       Cmd("imagecrop"));   // 남길 영역의 두 구석

            // ── 관리 — 도면층·블록·파일 ──
            r.AddTab("관리");

            r.AddGroup("도면층");
            r.AddLarge("도면층", I.Layers,   () => TogglePanel(Layers, 0, () => Layers.ShowPage(0)), () => IsOpen(Layers, Layers.Page, 0));
            r.AddLarge("선종류", I.Linetype, () => TogglePanel(Layers, 1, () => Layers.ShowPage(1)), () => IsOpen(Layers, Layers.Page, 1));

            r.AddGroup("블록");
            r.AddLarge("블록 만들기",    I.Block,     Cmd("block"));   // 고른 객체로 — 이름·기준점은 3D 뷰에서 묻는다
            r.AddSmall("블록 편집",      I.BlockEdit, Cmd("bedit"));   // 고른 블록 참조 하나를 편집 탭으로
            r.AddSmall("블록·외부 참조", I.Xref,      () => TogglePanel(Layers, 2, () => Layers.ShowPage(2)), () => IsOpen(Layers, Layers.Page, 2));

            r.AddGroup("파일");
            r.AddLarge("STEP 열기", I.FileOpen, () => OpenFile("STEP (*.step;*.stp)|*.step;*.stp"));
            r.AddSmall("STEP 저장", I.FileSave, () => SaveFile("STEP AP242 (*.step)|*.step", "STEP 저장"));
            r.AddSmall("DWG 저장",  I.FileSave, () => SaveFile("DWG R2018 (*.dwg)|*.dwg", "DWG 저장"));
        }

        static bool IsOpen(UserControl panel, int page, int want) => panel.Visibility == Visibility.Visible && page == want;

        // 리본 버튼은 켜고 끄기 — 이미 그 페이지가 열려 있으면 닫는다(메뉴는 열기만)
        void TogglePanel(UserControl panel, int page, Action show)
        {
            int current = panel is AnalysisPanel a ? a.Page : ((SidePanel)panel).Page;
            if (IsOpen(panel, current, page)) panel.Visibility = Visibility.Collapsed;
            else ShowSide(panel, show);
        }

        // 차집합 — 엔진의 차집합은 기준(A)·빼기(B)를 고르는 대화상자를 여는데 임베드에선 그 창이 안 보인다.
        // 엔진의 선택 목록은 id 순이라 "먼저 고른 것" 도 알 수 없다. 그래서 오토캐드 SUBTRACT 처럼 두 단계로 받는다.
        //   1) 기준 솔리드 선택 → 차집합   : 기준을 기억
        //   2) 뺄 솔리드 선택   → 차집합   : CAD_BooleanSubtract 실행
        uint[] _subtractBase = Array.Empty<uint>();

        void SubtractStep()
        {
            var selected = CadApi.SelectedIds();
            if (_subtractBase.Length == 0)
            {
                if (selected.Length == 0) { StatusText.Text = "차집합: 기준이 될 솔리드를 먼저 선택하고 다시 누르세요"; return; }
                _subtractBase = selected;
                StatusText.Text = $"차집합: 기준 {selected.Length}개 기억함 — 뺄 솔리드를 선택하고 차집합을 다시 누르세요 (빈 선택이면 취소)";
                return;
            }

            // 기준으로 고른 것은 뺄 목록에서 제외 (기준을 선택한 채 뺄 것을 추가로 고른 경우)
            var tools = selected.Except(_subtractBase).ToArray();
            if (tools.Length == 0) StatusText.Text = "차집합: 취소";
            else
            {
                // keepOriginals=false(원본 삭제), perBase=false(한 덩어리 — 오토캐드 SUBTRACT). 결과 id 를 받을 칸을 꼭 준다
                var result = new uint[1];
                int made = CadApi.CAD_BooleanSubtract(_subtractBase, (uint)_subtractBase.Length, tools, (uint)tools.Length, false, false, result, 1);
                StatusText.Text = made > 0 ? $"차집합: 기준 {_subtractBase.Length}개에서 {tools.Length}개를 뺌" : "차집합 실패: " + CadApi.LastError();
            }
            _subtractBase = Array.Empty<uint>();
        }
    }
}
