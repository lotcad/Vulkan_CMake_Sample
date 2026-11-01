using System;
using System.Collections.Generic;
using System.Globalization;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Threading;

namespace LotCadWpf
{
    // 리본 — 탭 줄 + 그룹(큰 버튼 · 작은 버튼 3줄 칸) + 그룹 이름 띠. MFC 샘플 RibbonBar.cpp 와 같은 모양·치수.
    // 무엇을 어디에 둘지는 MainWindow.Ribbon.cs 가 AddTab · AddGroup · AddLarge · AddSmall 로 정한다.
    // 켜짐 표시(isOn)는 엔진에 읽는 함수가 있는 것(투영)·호스트가 아는 것(패널·그래프)을 0.25초마다 다시 본다.
    public sealed class RibbonBar : UserControl
    {
        const double TabH = 26, TabPadX = 12, PadTop = 5, SmallH = 22, CellGap = 2, CaptionGap = 3, CaptionH = 17,
                     PadBottom = 4, GroupGap = 9;
        const int Rows = 3;                                       // 그룹당 작은 버튼 줄 수
        const double GridH = SmallH * Rows + CellGap * (Rows - 1);

        sealed class Tab
        {
            public TextBlock Title;
            public Border Underline;
            public StackPanel Body;
        }

        readonly StackPanel _tabRow = new StackPanel { Orientation = Orientation.Horizontal, Height = TabH };
        readonly Grid _bodyHost = new Grid { Margin = new Thickness(GroupGap, PadTop, 0, PadBottom), ClipToBounds = true };
        readonly List<Tab> _tabs = new();
        readonly List<RibbonButton> _buttons = new();
        readonly DispatcherTimer _timer = new DispatcherTimer { Interval = TimeSpan.FromMilliseconds(250) };
        StackPanel _group, _column;   // 지금 채우는 그룹 줄 · 작은 버튼 칸
        int _active = -1;

        /// <summary>버튼을 누른 뒤 — MainWindow 가 키보드를 렌더 창(엔진)으로 돌린다.</summary>
        public event Action Clicked;

        public RibbonBar()
        {
            var root = new DockPanel { Background = new SolidColorBrush(Theme.BodyBg) };
            var tabBar = new Border { Background = new SolidColorBrush(Theme.TabBarBg), Child = _tabRow };
            DockPanel.SetDock(tabBar, Dock.Top);
            root.Children.Add(tabBar);
            root.Children.Add(_bodyHost);
            Content = new Border
            {
                Child = root, BorderBrush = new SolidColorBrush(Theme.Separator), BorderThickness = new Thickness(0, 0, 0, 1),
            };
            _timer.Tick += (s, e) => Refresh();
            Loaded += (s, e) => _timer.Start();
            Unloaded += (s, e) => _timer.Stop();
        }

        public void AddTab(string title)
        {
            int index = _tabs.Count;
            var tab = new Tab
            {
                Title = new TextBlock
                {
                    Text = title, FontSize = 12, Padding = new Thickness(TabPadX, 0, TabPadX, 0),
                    VerticalAlignment = VerticalAlignment.Center, Foreground = new SolidColorBrush(Theme.TextDim),
                },
                Underline = new Border { Height = 2, Margin = new Thickness(4, 0, 4, 0), VerticalAlignment = VerticalAlignment.Bottom },
                Body = new StackPanel { Orientation = Orientation.Horizontal, Visibility = Visibility.Collapsed },
            };
            var cell = new Grid { Background = Brushes.Transparent, Cursor = Cursors.Hand };
            cell.Children.Add(tab.Title);
            cell.Children.Add(tab.Underline);
            cell.MouseLeftButtonDown += (s, e) => ShowTab(index);
            cell.MouseEnter += (s, e) => tab.Title.Foreground = new SolidColorBrush(Theme.Text);
            cell.MouseLeave += (s, e) => { if (_active != index) tab.Title.Foreground = new SolidColorBrush(Theme.TextDim); };
            _tabRow.Children.Add(cell);
            _bodyHost.Children.Add(tab.Body);
            _tabs.Add(tab);
            _group = _column = null;
            if (_active < 0) ShowTab(0);
        }

        public void ShowTab(int index)
        {
            _active = index;
            for (int i = 0; i < _tabs.Count; i++)
            {
                bool on = i == index;
                _tabs[i].Body.Visibility = on ? Visibility.Visible : Visibility.Collapsed;
                _tabs[i].Title.Foreground = new SolidColorBrush(on ? Theme.Text : Theme.TextDim);
                _tabs[i].Underline.Background = on ? new SolidColorBrush(Theme.Accent) : null;
            }
        }

        public void AddGroup(string caption)
        {
            var body = _tabs[^1].Body;
            if (body.Children.Count > 0)   // 앞 그룹과 사이 세로선
                body.Children.Add(new Border
                {
                    Width = 1, Background = new SolidColorBrush(Theme.Separator), Margin = new Thickness(GroupGap, 2, GroupGap, 0),
                });
            _group = new StackPanel { Orientation = Orientation.Horizontal, Height = GridH };
            _column = null;
            var band = new Border
            {
                Height = CaptionH, Margin = new Thickness(-3, CaptionGap, -3, 0), CornerRadius = new CornerRadius(3),
                Background = new SolidColorBrush(Theme.CaptionBg),
                Child = new TextBlock
                {
                    Text = caption, FontSize = 11, Foreground = new SolidColorBrush(Theme.TextDim),
                    HorizontalAlignment = HorizontalAlignment.Center, VerticalAlignment = VerticalAlignment.Center,
                },
            };
            var box = new StackPanel();
            box.Children.Add(_group);
            box.Children.Add(band);
            body.Children.Add(box);
        }

        /// <summary>큰 버튼 — 아이콘 위, 이름 아래(오피스·오토캐드 리본식). isOn 이 있으면 켜진 동안 강조색.</summary>
        public void AddLarge(string label, RibbonIcon icon, Action onClick, Func<bool> isOn = null)
        {
            _column = null;
            var b = Make(label, icon, true, onClick, isOn);
            b.Margin = new Thickness(0, 0, CellGap * 2, 0);
            _group.Children.Add(b);
        }

        /// <summary>작은 버튼 — 아이콘 왼쪽, 이름 오른쪽. 세 개씩 한 칸에 쌓인다.</summary>
        public void AddSmall(string label, RibbonIcon icon, Action onClick, Func<bool> isOn = null)
        {
            if (_column == null || _column.Children.Count == Rows)
            {
                _column = new StackPanel { Margin = new Thickness(0, 0, CellGap * 2, 0) };
                _group.Children.Add(_column);
            }
            var b = Make(label, icon, false, onClick, isOn);
            if (_column.Children.Count > 0) b.Margin = new Thickness(0, CellGap, 0, 0);
            _column.Children.Add(b);
        }

        RibbonButton Make(string label, RibbonIcon icon, bool large, Action onClick, Func<bool> isOn)
        {
            var b = new RibbonButton(label, icon, large, isOn);
            b.Click += () => { onClick(); Refresh(); Clicked?.Invoke(); };
            _buttons.Add(b);
            return b;
        }

        /// <summary>켜짐 표시를 다시 본다 — 메뉴 등 리본 밖에서 상태를 바꾼 뒤에도 부를 수 있다.</summary>
        public void Refresh()
        {
            foreach (var b in _buttons) b.UpdateOn();
        }

        // 버튼 하나 — 판(켜짐 > 누름 > 호버) · 아이콘 · 이름을 직접 그린다
        sealed class RibbonButton : FrameworkElement
        {
            const double LargeMinW = 54, LargeLabelH = 18, SmallIconW = 24;
            static readonly Typeface Face = new Typeface(SystemFonts.MessageFontFamily, FontStyles.Normal, FontWeights.Normal, FontStretches.Normal);

            readonly string _label;
            readonly RibbonIcon _icon;
            readonly bool _large;
            readonly Func<bool> _isOn;
            bool _on, _hot, _pressed;

            public event Action Click;

            public RibbonButton(string label, RibbonIcon icon, bool large, Func<bool> isOn)
            {
                _label = label; _icon = icon; _large = large; _isOn = isOn;
                Cursor = Cursors.Hand;
                ToolTip = label;
                UpdateOn();
            }

            public void UpdateOn()
            {
                bool on = _isOn != null && _isOn();
                if (on != _on) { _on = on; InvalidateVisual(); }
            }

            FormattedText Text(Color color) => new FormattedText(_label, CultureInfo.CurrentUICulture, FlowDirection.LeftToRight, Face, 12,
                new SolidColorBrush(color), VisualTreeHelper.GetDpi(this).PixelsPerDip);

            protected override Size MeasureOverride(Size available)
            {
                double textW = Text(Theme.Text).WidthIncludingTrailingWhitespace;
                return _large ? new Size(Math.Max(LargeMinW, textW + 14), GridH) : new Size(SmallIconW + textW + 10, SmallH);
            }

            protected override void OnRender(DrawingContext dc)
            {
                var rc = new Rect(0, 0, ActualWidth, ActualHeight);
                double corner = _large ? 5 : 4;
                if (_on)
                {
                    var a = Theme.Accent;
                    dc.DrawRoundedRectangle(new SolidColorBrush(Color.FromArgb((byte)(_pressed ? 140 : 80), a.R, a.G, a.B)),
                                            new Pen(new SolidColorBrush(Color.FromArgb(230, a.R, a.G, a.B)), 1), rc, corner, corner);
                }
                else if (_pressed || _hot)
                    dc.DrawRoundedRectangle(new SolidColorBrush(_pressed ? Theme.Pressed : Theme.Hover), null, rc, corner, corner);
                else
                    dc.DrawRectangle(Brushes.Transparent, null, rc);   // 빈 곳도 마우스를 받게

                var text = Text(Theme.Text);
                if (_large)
                {
                    RibbonIcons.Draw(dc, _icon, rc.Width / 2, (rc.Height - LargeLabelH) / 2, 12, Theme.Text);
                    dc.DrawText(text, new Point((rc.Width - text.Width) / 2, rc.Height - LargeLabelH - 1 + (LargeLabelH - text.Height) / 2));
                }
                else
                {
                    RibbonIcons.Draw(dc, _icon, SmallIconW / 2 + 1, rc.Height / 2, 7, Theme.Text);
                    dc.DrawText(text, new Point(SmallIconW, (rc.Height - text.Height) / 2));
                }
            }

            protected override void OnMouseEnter(MouseEventArgs e) { _hot = true; InvalidateVisual(); }
            protected override void OnMouseLeave(MouseEventArgs e) { _hot = false; InvalidateVisual(); }

            protected override void OnMouseLeftButtonDown(MouseButtonEventArgs e)
            {
                _pressed = true;
                CaptureMouse();
                InvalidateVisual();
                e.Handled = true;
            }

            protected override void OnMouseLeftButtonUp(MouseButtonEventArgs e)
            {
                bool click = _pressed && new Rect(RenderSize).Contains(e.GetPosition(this));   // 누른 채 밖으로 나가 떼면 취소
                _pressed = false;
                ReleaseMouseCapture();
                InvalidateVisual();
                e.Handled = true;
                if (click) Click?.Invoke();
            }
        }
    }
}
