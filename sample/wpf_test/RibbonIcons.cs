using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows;
using System.Windows.Media;

namespace LotCadWpf
{
    // 리본 아이콘 — 비트맵 없이 선으로 그린다(DPI 가 바뀌어도 선명하다).
    // MFC 샘플의 RibbonIcons.cpp(GDI+)를 WPF DrawingContext 로 옮긴 것 — 그림 코드는 그대로다.
    // 엔진 리본(ImGui)의 아이콘과 같은 모양을 흉내 낸다.
    public enum RibbonIcon
    {
        None,
        // 홈
        GizmoMove, GizmoRotate, GizmoScale,
        Move, Rotate, Scale, Copy, Array,
        SelectAll, Delete, ClearAll,
        Undo, Redo,
        ZoomExtents, Focus, Projection, ViewIso, ViewTop, ViewFront, ViewRight,
        // 2D
        Line, Rectangle, Circle, Polygon, Arc, Polyline, Text, Dimension,
        Offset, Mirror, Trim, Extend, Fillet, Chamfer,
        // 3D
        Box, Sphere, Cylinder, Cone, Torus,
        Extrude, Revolve, Sweep, Loft, Shell,
        Union, Difference, Intersect, Slice,
        // 도구
        Section, Navigation, Particles,
        // 해석 (엔진 ui/lot_ribbon.cpp 의 SubdIcon::AnaWind · AnaWater · AnaStress 를 옮긴 것)
        AnaWind, AnaWater, AnaStress,
        // 도구 — 모델·이미지
        Graph, Explode, MeshRepair,
        ImageAttach, ImageRotate, ImageFlip, ImageBackground, ImageCrop,
        // 관리 — 도면층·블록·파일
        Layers, Linetype, Block, BlockEdit, Xref,
        FileOpen, FileSave,
    }

    // 리본 색 — MFC 샘플 DarkTheme.h 와 같은 값
    public static class Theme
    {
        public static readonly Color TabBarBg  = Rgb(30, 30, 30);     // 탭 줄
        public static readonly Color BodyBg    = Rgb(43, 43, 45);     // 그룹이 놓이는 본문
        public static readonly Color CaptionBg = Rgb(52, 52, 55);     // 그룹 이름 띠
        public static readonly Color Separator = Rgb(70, 70, 74);     // 그룹 사이 세로선·맨 아래 선
        public static readonly Color Hover     = Rgb(62, 62, 66);
        public static readonly Color Pressed   = Rgb(80, 80, 86);
        public static readonly Color Text      = Rgb(230, 230, 230);
        public static readonly Color TextDim   = Rgb(150, 150, 155);  // 비활성 탭·그룹 이름
        public static readonly Color Accent    = Rgb(107, 171, 245);  // 활성 탭 밑줄·켜진 버튼 (엔진 강조 파랑)
        public static readonly Color AxisX     = Rgb(230, 85, 85);
        public static readonly Color AxisY     = Rgb(115, 200, 95);
        public static readonly Color AxisZ     = Rgb(95, 145, 240);

        public static Color Rgb(byte r, byte g, byte b) => Color.FromRgb(r, g, b);
    }

    public static class RibbonIcons
    {
        static Color Rgb(byte r, byte g, byte b) => Color.FromRgb(r, g, b);

        // 아이콘 좌표계: 중심 (0,0), 가장자리 ±1, y 는 아래로.
        // 단위 좌표 → 픽셀 변환과 펜·채움 붓을 한데 묶어, 아이콘 하나가 몇 줄로 끝나게 한다.
        sealed class Painter
        {
            readonly DrawingContext _dc;
            readonly double _cx, _cy, _r;
            readonly Brush _fill;   // 면 강조 — 강조색 반투명
            Color _color;
            bool _dashed;
            double _width;

            public Painter(DrawingContext dc, double cx, double cy, double r, Color color)
            {
                _dc = dc; _cx = cx; _cy = cy; _r = r; _color = color;
                _width = Math.Max(1.2, r * 0.15);
                _fill = new SolidColorBrush(Color.FromArgb(110, Theme.Accent.R, Theme.Accent.G, Theme.Accent.B));
            }

            Pen Pen
            {
                get
                {
                    var pen = new Pen(new SolidColorBrush(_color), _width)
                    {
                        StartLineCap = PenLineCap.Round, EndLineCap = PenLineCap.Round,
                        LineJoin = PenLineJoin.Round, DashCap = PenLineCap.Round,
                    };
                    // GDI+ DashStyleDash(3:1) 와 비슷하게 — WPF 는 둥근 끝이 대시 길이에 더해진다
                    if (_dashed) pen.DashStyle = new DashStyle(new[] { 1.8, 2.2 }, 0);
                    return pen;
                }
            }

            Point P(double x, double y) => new Point(_cx + x * _r, _cy + y * _r);

            public void SetColor(Color c) => _color = c;
            public void Dashed(bool on)  => _dashed = on;
            public void Width(double factor) => _width = Math.Max(1.2, _r * 0.15) * factor;   // 1 = 기본 굵기

            public void Line(double x1, double y1, double x2, double y2) => _dc.DrawLine(Pen, P(x1, y1), P(x2, y2));
            public void Rect(double x, double y, double w, double h) => _dc.DrawRectangle(null, Pen, new Rect(P(x, y), new Size(w * _r, h * _r)));
            public void Ellipse(double x, double y, double rx, double ry) => _dc.DrawEllipse(null, Pen, P(x, y), rx * _r, ry * _r);
            public void FillEllipse(double x, double y, double rx, double ry) => _dc.DrawEllipse(_fill, null, P(x, y), rx * _r, ry * _r);

            // start·sweep 은 도(°), 0° = +x, 시계 방향(화면 y 가 아래라서).
            public void Arc(double x, double y, double rad, double start, double sweep) => EllipseArc(x, y, rad, rad, start, sweep);
            public void EllipseArc(double x, double y, double rx, double ry, double start, double sweep)
            {
                const int n = 32;
                var pts = new List<Point>();
                for (int i = 0; i <= n; i++)
                {
                    double a = (start + sweep * i / n) * Math.PI / 180;
                    pts.Add(new Point(x + rx * Math.Cos(a), y + ry * Math.Sin(a)));
                }
                Lines(pts);
            }

            public void Dot(double x, double y)
            {
                double d = Math.Max(1.5, _r * 0.14);
                _dc.DrawEllipse(new SolidColorBrush(_color), null, P(x, y), d, d);
            }

            StreamGeometry Shape(IEnumerable<(double X, double Y)> unit, bool closed, bool filled)
            {
                var pts = unit.Select(p => P(p.X, p.Y)).ToList();
                var geo = new StreamGeometry();
                using (var g = geo.Open())
                {
                    g.BeginFigure(pts[0], filled, closed);
                    g.PolyLineTo(pts.Skip(1).ToList(), true, true);
                }
                geo.Freeze();
                return geo;
            }

            public void Poly(bool closed, params (double X, double Y)[] pts) => _dc.DrawGeometry(null, Pen, Shape(pts, closed, false));
            public void FillPoly(params (double X, double Y)[] pts) => _dc.DrawGeometry(_fill, null, Shape(pts, true, true));
            // 정한 색으로 채우기 (해석 아이콘의 파란 흐름·빨간 응력처럼 강조색이 아닌 것)
            public void FillPolyColor(Color c, byte alpha, params (double X, double Y)[] pts) =>
                _dc.DrawGeometry(new SolidColorBrush(Color.FromArgb(alpha, c.R, c.G, c.B)), null, Shape(pts, true, true));
            public void FillCircleColor(double x, double y, double rad, Color c) =>
                _dc.DrawEllipse(new SolidColorBrush(c), null, P(x, y), rad * _r, rad * _r);
            // 단위 좌표 점 목록 → 꺾은선 (계산으로 만든 곡선용)
            public void Lines(List<Point> unit) => _dc.DrawGeometry(null, Pen, Shape(unit.Select(p => (p.X, p.Y)), false, false));

            // 3차 베지어 한 토막 — 시작점, 조절점 둘, 끝점
            public void Bezier((double X, double Y) a, (double X, double Y) b, (double X, double Y) c, (double X, double Y) d)
            {
                var geo = new StreamGeometry();
                using (var g = geo.Open())
                {
                    g.BeginFigure(P(a.X, a.Y), false, false);
                    g.BezierTo(P(b.X, b.Y), P(c.X, c.Y), P(d.X, d.Y), true, true);
                }
                geo.Freeze();
                _dc.DrawGeometry(null, Pen, geo);
            }

            // (x,y) 가 촉 끝, (dx,dy) 가 가리키는 방향인 화살촉.
            public void Arrow(double x, double y, double dx, double dy)
            {
                double len = Math.Sqrt(dx * dx + dy * dy);
                dx /= len; dy /= len;
                const double a = 0.38, c = 0.866, s = 0.5;   // 길이, cos/sin 30°
                Line(x, y, x + a * (-dx * c + dy * s), y + a * (-dy * c - dx * s));
                Line(x, y, x + a * (-dx * c - dy * s), y + a * (-dy * c + dx * s));
            }

            // 등각 정육면체. face: 0=없음 1=윗면 2=앞(왼쪽)면 3=오른쪽면 을 강조색으로 채운다.
            public void IsoCube(int face = 0)
            {
                (double, double) top = (0, -0.9), ur = (0.8, -0.45), lr = (0.8, 0.45),
                                 bot = (0, 0.9),  ll = (-0.8, 0.45), ul = (-0.8, -0.45), mid = (0, 0);
                if (face == 1) FillPoly(top, ur, mid, ul);
                if (face == 2) FillPoly(ul, mid, bot, ll);
                if (face == 3) FillPoly(mid, ur, lr, bot);
                Poly(true, top, ur, lr, bot, ll, ul);
                Poly(false, ul, mid, ur);
                Line(0, 0, 0, 0.9);
            }

            // 두 원의 불리언 — op: 0=합 1=차(왼쪽−오른쪽) 2=교. 결과 영역만 채운다.
            public void BooleanCircles(int op)
            {
                var a = new EllipseGeometry(P(-0.32, 0), 0.6 * _r, 0.6 * _r);
                var b = new EllipseGeometry(P(0.32, 0), 0.6 * _r, 0.6 * _r);
                var mode = op == 0 ? GeometryCombineMode.Union : op == 1 ? GeometryCombineMode.Exclude : GeometryCombineMode.Intersect;
                _dc.DrawGeometry(_fill, null, new CombinedGeometry(mode, a, b));
                Ellipse(-0.32, 0, 0.6, 0.6);
                if (op == 1) Dashed(true);
                Ellipse(0.32, 0, 0.6, 0.6);
                Dashed(false);
            }

            // 기즈모 세 축 (X 오른쪽 · Y 안쪽 대각 · Z 위). end: 0=화살촉 1=상자.
            public void GizmoAxes(int end)
            {
                const double ox = -0.55, oy = 0.55;
                var axes = new[] { (Theme.AxisX, 0.9, 0.55), (Theme.AxisY, 0.3, -0.3), (Theme.AxisZ, -0.55, -0.9) };
                foreach (var (color, x, y) in axes)
                {
                    SetColor(color);
                    Line(ox, oy, x, y);
                    if (end == 0) Arrow(x, y, x - ox, y - oy);
                    else _dc.DrawRectangle(new SolidColorBrush(color), null, new Rect(P(x - 0.16, y - 0.16), new Size(0.32 * _r, 0.32 * _r)));
                }
            }
        }

        /// <summary>(cx, cy) 를 중심으로 반지름 r 인 정사각형 안에 그린다. color = 선 색.</summary>
        public static void Draw(DrawingContext dc, RibbonIcon icon, double cx, double cy, double r, Color color)
        {
            var p = new Painter(dc, cx, cy, r, color);

            switch (icon)
            {
                // ── 홈 ──────────────────────────────────────────────────────────────
                case RibbonIcon.GizmoMove:   p.GizmoAxes(0); break;
                case RibbonIcon.GizmoScale:  p.GizmoAxes(1); break;
                case RibbonIcon.GizmoRotate:
                    p.SetColor(Theme.AxisZ); p.Ellipse(0, 0, 0.9f, 0.9f);
                    p.SetColor(Theme.AxisX); p.Ellipse(0, 0, 0.9f, 0.32f);
                    p.SetColor(Theme.AxisY); p.Ellipse(0, 0, 0.32f, 0.9f);
                    break;
                case RibbonIcon.Move:
                    p.Line(-0.9f, 0, 0.9f, 0);  p.Line(0, -0.9f, 0, 0.9f);
                    p.Arrow( 0.9f, 0, 1, 0);    p.Arrow(-0.9f, 0, -1, 0);
                    p.Arrow(0,  0.9f, 0, 1);    p.Arrow(0, -0.9f, 0, -1);
                    break;
                case RibbonIcon.Rotate:
                    p.Arc(0, 0, 0.75f, -60, 290);              // 시계 방향으로 230° 에서 끝난다
                    p.Arrow(-0.48f, -0.57f, 0.77f, -0.64f);    // 끝점에서 진행 방향(접선)으로
                    break;
                case RibbonIcon.Scale:
                    p.Rect(-0.9f, 0.1f, 0.8f, 0.8f);
                    p.Dashed(true);  p.Rect(-0.9f, -0.9f, 1.8f, 1.8f);  p.Dashed(false);
                    p.Line(-0.1f, 0.1f, 0.65f, -0.65f);
                    p.Arrow(0.65f, -0.65f, 1, -1);
                    break;
                case RibbonIcon.Copy:
                    p.Rect(-0.9f, -0.35f, 1.2f, 1.25f);
                    p.Rect(-0.3f, -0.9f, 1.2f, 1.25f);
                    break;
                case RibbonIcon.Array:
                    for (int row = 0; row < 2; ++row)
                        for (int col = 0; col < 3; ++col)
                            p.Rect(-0.9f + col * 0.65f, -0.65f + row * 0.75f, 0.5f, 0.5f);
                    break;
                case RibbonIcon.SelectAll:
                    p.Dashed(true);  p.Rect(-0.9f, -0.9f, 1.8f, 1.8f);  p.Dashed(false);
                    p.FillPoly((-0.45f, -0.45f), (0.45f, -0.45f), (0.45f, 0.45f), (-0.45f, 0.45f));
                    break;
                case RibbonIcon.Delete:
                    p.Line(-0.7f, -0.7f, 0.7f, 0.7f);  p.Line(0.7f, -0.7f, -0.7f, 0.7f);
                    break;
                case RibbonIcon.ClearAll:   // 휴지통
                    p.Line(-0.9f, -0.6f, 0.9f, -0.6f);
                    p.Line(-0.3f, -0.9f, 0.3f, -0.9f);
                    p.Poly(false, (-0.65f, -0.6f), (-0.5f, 0.9f), (0.5f, 0.9f), (0.65f, -0.6f));
                    p.Line(-0.2f, -0.25f, -0.15f, 0.55f);  p.Line(0.2f, -0.25f, 0.15f, 0.55f);
                    break;
                case RibbonIcon.Undo:
                    p.Arc(0, 0.25f, 0.7f, 180, 180);
                    p.Arrow(-0.7f, 0.35f, 0, 1);
                    break;
                case RibbonIcon.Redo:
                    p.Arc(0, 0.25f, 0.7f, 180, 180);
                    p.Arrow(0.7f, 0.35f, 0, 1);
                    break;
                case RibbonIcon.ZoomExtents:   // 네 모서리 괄호 + 가운데 물체
                    p.Poly(false, (-0.9f, -0.4f), (-0.9f, -0.9f), (-0.4f, -0.9f));
                    p.Poly(false, (0.4f, -0.9f), (0.9f, -0.9f), (0.9f, -0.4f));
                    p.Poly(false, (0.9f, 0.4f), (0.9f, 0.9f), (0.4f, 0.9f));
                    p.Poly(false, (-0.4f, 0.9f), (-0.9f, 0.9f), (-0.9f, 0.4f));
                    p.Rect(-0.35f, -0.35f, 0.7f, 0.7f);
                    break;
                case RibbonIcon.Focus:         // 조준선
                    p.Ellipse(0, 0, 0.55f, 0.55f);
                    p.Line(0, -0.95f, 0, -0.55f);  p.Line(0, 0.55f, 0, 0.95f);
                    p.Line(-0.95f, 0, -0.55f, 0);  p.Line(0.55f, 0, 0.95f, 0);
                    p.Dot(0, 0);
                    break;
                case RibbonIcon.Projection:    // 시야 절두체
                    p.Poly(false, (0.9f, -0.8f), (-0.9f, 0), (0.9f, 0.8f));
                    p.Line(0.9f, -0.8f, 0.9f, 0.8f);
                    p.Dashed(true);  p.Line(0.1f, -0.45f, 0.1f, 0.45f);  p.Dashed(false);
                    break;
                case RibbonIcon.ViewIso:   p.IsoCube(0); break;
                case RibbonIcon.ViewTop:   p.IsoCube(1); break;
                case RibbonIcon.ViewFront: p.IsoCube(2); break;
                case RibbonIcon.ViewRight: p.IsoCube(3); break;

                // ── 2D ──────────────────────────────────────────────────────────────
                case RibbonIcon.Line:
                    p.Line(-0.8f, 0.8f, 0.8f, -0.8f);
                    p.Dot(-0.8f, 0.8f);  p.Dot(0.8f, -0.8f);
                    break;
                case RibbonIcon.Rectangle: p.Rect(-0.85f, -0.6f, 1.7f, 1.2f); break;
                case RibbonIcon.Circle:    p.Ellipse(0, 0, 0.85f, 0.85f); p.Dot(0, 0); break;
                case RibbonIcon.Polygon:
                    p.Poly(true, (0.9f, 0), (0.45f, -0.78f), (-0.45f, -0.78f),
                             (-0.9f, 0), (-0.45f, 0.78f), (0.45f, 0.78f));
                    break;
                case RibbonIcon.Arc:
                    p.Arc(0, 0.45f, 0.85f, 200, 140);
                    p.Dot(-0.8f, 0.16f);  p.Dot(0.8f, 0.16f);  p.Dot(0, -0.4f);
                    break;
                case RibbonIcon.Polyline:
                    p.Poly(false, (-0.9f, 0.7f), (-0.3f, -0.5f), (0.3f, 0.4f), (0.9f, -0.7f));
                    p.Dot(-0.9f, 0.7f);  p.Dot(-0.3f, -0.5f);  p.Dot(0.3f, 0.4f);  p.Dot(0.9f, -0.7f);
                    break;
                case RibbonIcon.Text:          // A
                    p.Poly(false, (-0.7f, 0.9f), (0, -0.9f), (0.7f, 0.9f));
                    p.Line(-0.4f, 0.25f, 0.4f, 0.25f);
                    break;
                case RibbonIcon.Dimension:
                    p.Line(-0.9f, -0.6f, -0.9f, 0.9f);  p.Line(0.9f, -0.6f, 0.9f, 0.9f);
                    p.Line(-0.9f, 0.1f, 0.9f, 0.1f);
                    p.Arrow(-0.9f, 0.1f, -1, 0);  p.Arrow(0.9f, 0.1f, 1, 0);
                    p.Line(-0.3f, -0.4f, 0.3f, -0.4f);   // 치수 문자 자리
                    break;
                case RibbonIcon.Offset:        // 같은 중심의 두 호
                    p.Arc(0, 0.9f, 0.55f, 200, 140);
                    p.Dashed(true);  p.Arc(0, 0.9f, 1.0f, 205, 130);  p.Dashed(false);
                    break;
                case RibbonIcon.Mirror:
                    p.Dashed(true);  p.Line(0, -0.95f, 0, 0.95f);  p.Dashed(false);
                    p.Poly(true, (-0.25f, -0.7f), (-0.25f, 0.7f), (-0.9f, 0.7f));
                    p.FillPoly((0.25f, -0.7f), (0.25f, 0.7f), (0.9f, 0.7f));
                    p.Poly(true, (0.25f, -0.7f), (0.25f, 0.7f), (0.9f, 0.7f));
                    break;
                case RibbonIcon.Trim:          // 경계선에서 잘린 쪽은 점선
                    p.Line(0.2f, -0.9f, 0.2f, 0.9f);
                    p.Line(-0.9f, 0, 0.2f, 0);
                    p.Dashed(true);  p.Line(0.2f, 0, 0.9f, 0);  p.Dashed(false);
                    break;
                case RibbonIcon.Extend:        // 경계선까지 늘어난 부분은 점선 + 화살촉
                    p.Line(0.8f, -0.9f, 0.8f, 0.9f);
                    p.Line(-0.9f, 0, 0.0f, 0);
                    p.Dashed(true);  p.Line(0.0f, 0, 0.75f, 0);  p.Dashed(false);
                    p.Arrow(0.75f, 0, 1, 0);
                    break;
                case RibbonIcon.Fillet:
                    p.Line(-0.8f, 0.85f, -0.8f, -0.1f);
                    p.Arc(-0.1f, -0.1f, 0.7f, 180, 90);
                    p.Line(-0.1f, -0.8f, 0.85f, -0.8f);
                    break;
                case RibbonIcon.Chamfer:
                    p.Poly(false, (-0.8f, 0.85f), (-0.8f, -0.1f), (-0.1f, -0.8f), (0.85f, -0.8f));
                    break;

                // ── 3D ──────────────────────────────────────────────────────────────
                case RibbonIcon.Box: p.IsoCube(0); break;
                case RibbonIcon.Sphere:
                    p.Ellipse(0, 0, 0.85f, 0.85f);
                    p.Ellipse(0, 0, 0.85f, 0.3f);
                    p.Ellipse(0, 0, 0.3f, 0.85f);
                    break;
                case RibbonIcon.Cylinder:
                    p.Ellipse(0, -0.6f, 0.7f, 0.25f);
                    p.Line(-0.7f, -0.6f, -0.7f, 0.6f);  p.Line(0.7f, -0.6f, 0.7f, 0.6f);
                    p.EllipseArc(0, 0.6f, 0.7f, 0.25f, 0, 180);   // 바닥은 앞쪽 반만 보인다
                    break;
                case RibbonIcon.Cone:
                    p.Poly(false, (-0.75f, 0.6f), (0, -0.9f), (0.75f, 0.6f));
                    p.Ellipse(0, 0.6f, 0.75f, 0.25f);
                    break;
                case RibbonIcon.Torus:
                    p.Ellipse(0, 0, 0.9f, 0.55f);
                    p.Ellipse(0, -0.05f, 0.38f, 0.18f);
                    break;
                case RibbonIcon.Extrude:       // 바닥 단면 + 위로 화살표
                    p.FillPoly((-0.85f, 0.9f), (0.35f, 0.9f), (0.85f, 0.5f), (-0.35f, 0.5f));
                    p.Poly(true, (-0.85f, 0.9f), (0.35f, 0.9f), (0.85f, 0.5f), (-0.35f, 0.5f));
                    p.Line(0, 0.7f, 0, -0.9f);
                    p.Arrow(0, -0.9f, 0, -1);
                    break;
                case RibbonIcon.Revolve:       // 축 + 둘레를 도는 화살표
                    p.Dashed(true);  p.Line(0, -0.95f, 0, 0.95f);  p.Dashed(false);
                    p.Ellipse(0, 0, 0.85f, 0.32f);
                    p.Arrow(0.15f, 0.32f, 1, 0);
                    break;
                case RibbonIcon.Sweep: {       // 단면이 곡선 경로를 따라감
                    p.Bezier((-0.75f, 0.75f), (-0.6f, -0.3f), (0.4f, 0.6f), (0.85f, -0.7f));
                    p.FillEllipse(-0.75f, 0.75f, 0.22f, 0.22f);
                    p.Ellipse(-0.75f, 0.75f, 0.22f, 0.22f);
                    p.Arrow(0.85f, -0.7f, 0.4f, -1);
                    break;
                }
                case RibbonIcon.Loft:          // 크기가 다른 두 단면을 잇는다
                    p.Ellipse(0, 0.6f, 0.8f, 0.25f);
                    p.Ellipse(0, -0.6f, 0.4f, 0.14f);
                    p.Line(-0.8f, 0.6f, -0.4f, -0.6f);  p.Line(0.8f, 0.6f, 0.4f, -0.6f);
                    break;
                case RibbonIcon.Shell:         // 속이 빈 그릇 단면
                    p.FillPoly((-0.9f, -0.7f), (-0.9f, 0.85f), (0.9f, 0.85f), (0.9f, -0.7f),
                                 (0.6f, -0.7f), (0.6f, 0.55f), (-0.6f, 0.55f), (-0.6f, -0.7f));
                    p.Poly(true, (-0.9f, -0.7f), (-0.9f, 0.85f), (0.9f, 0.85f), (0.9f, -0.7f),
                             (0.6f, -0.7f), (0.6f, 0.55f), (-0.6f, 0.55f), (-0.6f, -0.7f));
                    break;
                case RibbonIcon.Union:      p.BooleanCircles(0); break;
                case RibbonIcon.Difference: p.BooleanCircles(1); break;
                case RibbonIcon.Intersect:  p.BooleanCircles(2); break;
                case RibbonIcon.Slice:
                    p.IsoCube(0);
                    p.SetColor(Theme.Accent);
                    p.Dashed(true);  p.Line(-1.0f, 0.35f, 1.0f, -0.35f);  p.Dashed(false);
                    break;

                // ── 도구 ────────────────────────────────────────────────────────────
                case RibbonIcon.Section:       // 정육면체 + 가로지르는 단면(강조색 면)
                    p.FillPoly((-0.8f, 0.1f), (0, -0.35f), (0.8f, 0.1f), (0, 0.55f));
                    p.IsoCube(0);
                    p.SetColor(Theme.Accent);
                    p.Poly(true, (-0.8f, 0.1f), (0, -0.35f), (0.8f, 0.1f), (0, 0.55f));
                    break;
                case RibbonIcon.Navigation:    // 출발점 → 굽은 경로(점선) → 목적지 깃발
                    p.Dot(-0.8f, 0.75f);
                    p.Dashed(true);
                    p.Poly(false, (-0.8f, 0.75f), (-0.2f, 0.75f), (-0.2f, -0.1f), (0.55f, -0.1f));
                    p.Dashed(false);
                    p.Line(0.55f, -0.1f, 0.55f, -0.95f);
                    p.FillPoly((0.55f, -0.95f), (0.95f, -0.75f), (0.55f, -0.55f));
                    p.Poly(true, (0.55f, -0.95f), (0.95f, -0.75f), (0.55f, -0.55f));
                    break;
                case RibbonIcon.Particles:     // 한 점에서 퍼지는 불티
                    p.Dot(0, 0.75f);
                    p.Line(0, 0.75f, -0.55f, -0.35f);  p.Dot(-0.65f, -0.55f);
                    p.Line(0, 0.75f,  0.0f,  -0.5f);   p.Dot(0, -0.8f);
                    p.Line(0, 0.75f,  0.55f, -0.35f);  p.Dot(0.65f, -0.55f);
                    p.Dot(-0.85f, 0.1f);  p.Dot(0.85f, 0.1f);
                    break;

                // ── 해석 — 엔진 리본(ui/lot_ribbon.cpp)과 같은 그림 ──
                case RibbonIcon.AnaWind: {     // 물체(작은 원) 둘레로 휘어 지나가는 흐름선 셋 + 바람 방향(+X)
                    Color blue = Rgb(89, 179, 255);
                    p.FillCircleColor(0.15f, 0.0f, 0.28f, color);
                    p.SetColor(blue);
                    foreach (float y in new[] { -0.65f, 0.65f }) {   // 위·아래 흐름선은 물체 쪽으로 불룩
                        float bend = y < 0.0f ? -0.25f : 0.25f;
                        var pts = new List<Point>();
                        for (int i = 0; i < 6; ++i) {
                            float x = -0.95f + 1.8f * i / 5.0f;
                            float bump = MathF.Exp(-((x - 0.15f) * (x - 0.15f)) / 0.12f);
                            pts.Add(new Point(x, y + bend * bump));
                        }
                        p.Lines(pts);
                    }
                    p.Line(-0.95f, 0.0f, -0.25f, 0.0f);            // 가운데 흐름선은 물체 앞뒤로 끊긴다
                    p.Line(0.55f, 0.0f, 0.95f, 0.0f);
                    p.FillPolyColor(blue, 255, (0.95f, 0.0f), (0.7f, -0.15f), (0.7f, 0.15f));
                    break;
                }
                case RibbonIcon.AnaWater: {    // 그릇 + 물결
                    Color blue = Rgb(77, 153, 255);
                    p.FillPolyColor(blue, 90, (-0.74f, 0.1f), (0.74f, 0.1f), (0.69f, 0.75f), (-0.69f, 0.75f));
                    p.Poly(false, (-0.85f, -0.7f), (-0.7f, 0.8f), (0.7f, 0.8f), (0.85f, -0.7f));
                    var wave = new List<Point>();
                    for (int i = 0; i < 9; ++i) {
                        float x = -0.76f + 1.52f * i / 8.0f;
                        wave.Add(new Point(x, -0.05f + 0.13f * MathF.Sin(x * 7.0f)));
                    }
                    p.SetColor(blue);
                    p.Width(1.3f);
                    p.Lines(wave);
                    break;
                }
                case RibbonIcon.AnaStress: {   // 벽에 박힌 보 + 끝에 누르는 화살표, 뿌리 쪽 빨강
                    p.FillPolyColor(Rgb(255, 77, 51), 255, (-0.9f, -0.15f), (-0.45f, -0.15f), (-0.45f, 0.2f), (-0.9f, 0.2f));
                    p.Width(1.5f);
                    p.Line(-0.9f, -0.9f, -0.9f, 0.9f);              // 벽
                    p.Width(0.7f);
                    for (float y = -0.8f; y < 0.9f; y += 0.4f) p.Line(-0.9f, y, -1.1f, y + 0.2f);   // 벽 빗금
                    p.Width(1.0f);
                    p.Rect(-0.9f, -0.15f, 1.65f, 0.35f);           // 보
                    p.Line(0.62f, -0.95f, 0.62f, -0.2f);           // 하중
                    p.Arrow(0.62f, -0.2f, 0.0f, 1.0f);
                    break;
                }

                // ── 도구: 모델 ──
                case RibbonIcon.Graph:         // 노드 둘을 잇는 선 — 왼쪽 출력 → 오른쪽 입력
                    p.FillPoly((-0.9f, -0.75f), (-0.2f, -0.75f), (-0.2f, -0.15f), (-0.9f, -0.15f));
                    p.Rect(-0.9f, -0.75f, 0.7f, 0.6f);
                    p.Rect(0.2f, 0.15f, 0.7f, 0.6f);
                    p.Poly(false, (-0.2f, -0.45f), (0.0f, -0.45f), (0.0f, 0.45f), (0.2f, 0.45f));
                    p.Dot(-0.2f, -0.45f);
                    p.Dot(0.2f, 0.45f);
                    break;
                case RibbonIcon.Explode:       // 가운데 상자에서 바깥으로 빠지는 세 조각
                    p.FillPoly((-0.25f, -0.25f), (0.25f, -0.25f), (0.25f, 0.25f), (-0.25f, 0.25f));
                    p.Rect(-0.25f, -0.25f, 0.5f, 0.5f);
                    p.Rect(-0.95f, -0.95f, 0.4f, 0.4f);
                    p.Rect(0.55f, -0.95f, 0.4f, 0.4f);
                    p.Rect(-0.2f, 0.6f, 0.4f, 0.35f);
                    p.Dashed(true);
                    p.Line(-0.3f, -0.3f, -0.55f, -0.55f);
                    p.Line(0.3f, -0.3f, 0.55f, -0.55f);
                    p.Line(0.0f, 0.3f, 0.0f, 0.6f);
                    p.Dashed(false);
                    break;
                case RibbonIcon.MeshRepair:    // 삼각형 망 + 메운 구멍(강조색)
                    p.FillPoly((0.0f, -0.1f), (0.45f, 0.55f), (-0.45f, 0.55f));
                    p.Poly(true, (-0.9f, 0.55f), (0.0f, -0.9f), (0.9f, 0.55f));
                    p.Line(-0.45f, -0.18f, 0.45f, -0.18f);
                    p.Poly(false, (-0.45f, -0.18f), (0.0f, -0.1f), (0.45f, -0.18f));
                    p.Line(0.0f, -0.1f, -0.45f, 0.55f);
                    p.Line(0.0f, -0.1f, 0.45f, 0.55f);
                    p.Line(-0.9f, 0.55f, 0.9f, 0.55f);
                    break;

                // ── 도구: 이미지 ──
                case RibbonIcon.ImageAttach:   // 사진 틀(산 + 해)
                    p.Rect(-0.9f, -0.7f, 1.8f, 1.4f);
                    p.FillPoly((-0.8f, 0.6f), (-0.25f, -0.05f), (0.1f, 0.3f), (0.4f, 0.05f), (0.8f, 0.6f));
                    p.Poly(false, (-0.8f, 0.6f), (-0.25f, -0.05f), (0.1f, 0.3f), (0.4f, 0.05f), (0.8f, 0.6f));
                    p.Ellipse(0.45f, -0.35f, 0.15f, 0.15f);
                    break;
                case RibbonIcon.ImageRotate:   // 사진 틀 + 도는 화살표
                    p.Rect(-0.55f, -0.35f, 1.1f, 0.9f);
                    p.Arc(0.0f, 0.1f, 0.85f, 200.0f, 140.0f);
                    p.Arrow(0.8f, -0.2f, 0.4f, 0.9f);
                    break;
                case RibbonIcon.ImageFlip:     // 가운데 점선 축 + 마주 보는 삼각형
                    p.Dashed(true);
                    p.Line(0.0f, -0.9f, 0.0f, 0.9f);
                    p.Dashed(false);
                    p.FillPoly((-0.15f, -0.6f), (-0.15f, 0.6f), (-0.85f, 0.6f));
                    p.Poly(true, (-0.15f, -0.6f), (-0.15f, 0.6f), (-0.85f, 0.6f));
                    p.Poly(true, (0.15f, -0.6f), (0.15f, 0.6f), (0.85f, 0.6f));
                    break;
                case RibbonIcon.ImageBackground:   // 사진 틀 + 지우개로 지운 자리(점선)
                    p.Rect(-0.9f, -0.7f, 1.8f, 1.4f);
                    p.Dashed(true);
                    p.Ellipse(-0.2f, 0.0f, 0.45f, 0.4f);
                    p.Dashed(false);
                    p.FillPoly((0.25f, 0.15f), (0.65f, -0.25f), (0.95f, 0.05f), (0.55f, 0.45f));
                    p.Poly(true, (0.25f, 0.15f), (0.65f, -0.25f), (0.95f, 0.05f), (0.55f, 0.45f));
                    break;
                case RibbonIcon.ImageCrop:     // 엇갈린 두 꺾쇠
                    p.Poly(false, (-0.55f, -0.9f), (-0.55f, 0.55f), (0.9f, 0.55f));
                    p.Poly(false, (-0.9f, -0.55f), (0.55f, -0.55f), (0.55f, 0.9f));
                    p.FillPoly((-0.55f, -0.55f), (0.55f, -0.55f), (0.55f, 0.55f), (-0.55f, 0.55f));
                    break;

                // ── 관리 ──
                case RibbonIcon.Layers:        // 겹친 판 셋 — 맨 위가 강조
                    p.FillPoly((0.0f, -0.85f), (0.9f, -0.45f), (0.0f, -0.05f), (-0.9f, -0.45f));
                    p.Poly(true, (0.0f, -0.85f), (0.9f, -0.45f), (0.0f, -0.05f), (-0.9f, -0.45f));
                    p.Poly(false, (-0.9f, -0.05f), (0.0f, 0.35f), (0.9f, -0.05f));
                    p.Poly(false, (-0.9f, 0.35f), (0.0f, 0.75f), (0.9f, 0.35f));
                    break;
                case RibbonIcon.Linetype:      // 실선 · 파선 · 일점쇄선
                    p.Line(-0.9f, -0.6f, 0.9f, -0.6f);
                    p.Dashed(true);
                    p.Line(-0.9f, 0.0f, 0.9f, 0.0f);
                    p.Dashed(false);
                    p.Line(-0.9f, 0.6f, -0.35f, 0.6f);
                    p.Dot(-0.15f, 0.6f);
                    p.Line(0.05f, 0.6f, 0.9f, 0.6f);
                    break;
                case RibbonIcon.Block:         // 묶인 도형(원 + 사각형) + 기준점
                    p.Dashed(true);
                    p.Rect(-0.9f, -0.9f, 1.8f, 1.8f);
                    p.Dashed(false);
                    p.Rect(-0.6f, -0.1f, 0.7f, 0.65f);
                    p.FillEllipse(0.3f, -0.25f, 0.35f, 0.35f);
                    p.Ellipse(0.3f, -0.25f, 0.35f, 0.35f);
                    p.Dot(-0.6f, 0.55f);
                    break;
                case RibbonIcon.BlockEdit:     // 블록 테두리 + 연필
                    p.Dashed(true);
                    p.Rect(-0.9f, -0.9f, 1.4f, 1.4f);
                    p.Dashed(false);
                    p.FillPoly((-0.2f, 0.75f), (0.65f, -0.1f), (0.9f, 0.15f), (0.05f, 1.0f));
                    p.Poly(true, (-0.2f, 0.75f), (0.65f, -0.1f), (0.9f, 0.15f), (0.05f, 1.0f), (-0.25f, 1.0f));
                    break;
                case RibbonIcon.Xref:          // 문서 + 고리(바깥 파일을 가리킴)
                    p.Poly(false, (-0.8f, -0.9f), (0.2f, -0.9f), (0.5f, -0.6f), (0.5f, 0.2f));
                    p.Poly(false, (-0.8f, -0.9f), (-0.8f, 0.9f), (-0.1f, 0.9f));
                    p.Ellipse(0.25f, 0.55f, 0.28f, 0.2f);
                    p.Ellipse(0.65f, 0.55f, 0.28f, 0.2f);
                    break;
                case RibbonIcon.FileOpen:      // 열린 폴더
                    p.FillPoly((-0.7f, -0.1f), (0.95f, -0.1f), (0.7f, 0.7f), (-0.95f, 0.7f));
                    p.Poly(false, (-0.9f, 0.7f), (-0.9f, -0.7f), (-0.35f, -0.7f), (-0.2f, -0.5f), (0.6f, -0.5f), (0.6f, -0.1f));
                    p.Poly(true, (-0.7f, -0.1f), (0.95f, -0.1f), (0.7f, 0.7f), (-0.95f, 0.7f));
                    break;
                case RibbonIcon.FileSave:      // 디스켓
                    p.Poly(true, (-0.85f, -0.85f), (0.55f, -0.85f), (0.85f, -0.55f), (0.85f, 0.85f), (-0.85f, 0.85f));
                    p.Rect(-0.45f, -0.85f, 0.8f, 0.5f);
                    p.FillPoly((-0.55f, 0.15f), (0.55f, 0.15f), (0.55f, 0.85f), (-0.55f, 0.85f));
                    p.Rect(-0.55f, 0.15f, 1.1f, 0.7f);
                    break;

                case RibbonIcon.None:
                default:
                    break;
            }
        }
    }
}
