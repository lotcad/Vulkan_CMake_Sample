# LotCAD — WPF 호스트 샘플 (.NET 8)

WPF 창 안에 LotCAD 엔진을 임베드하는 샘플. `LotCADCore.dll` 의 C API 를 P/Invoke 로 호출하고,
`HwndHost` 로 만든 자식 HWND 에 Vulkan 이 렌더한다. 위에는 MFC 샘플과 같은 **리본**(홈 · 2D · 3D · 도구 · 관리),
오른쪽에는 해석 · 도면(도면층·선종류·블록) · 도구(분해도·메시 수리) 패널이 붙는다.
(`CadApi.cs` 는 이 샘플이 쓰는 함수만 — 전체 선언은 `sdk/csharp`.)

## 구조

| 파일 | 역할 |
|------|------|
| `CadApi.cs` | `LotCADCore.dll` 의 `CAD_*` P/Invoke 선언 |
| `VulkanHost.cs` | `HwndHost` — 자식 HWND 생성 → `CAD_AttachView` → `CAD_CreateEngine`, 마우스/키 라우팅(F12 는 창이 받는다) |
| `MainWindow.xaml(.cs)` | 메뉴 · 리본 자리 · 렌더 영역 · 오른쪽 패널 · 상태바 + `CompositionTarget.Rendering` → `CAD_Tick`, 엔진 이벤트·F12 |
| `MainWindow.Ribbon.cs` | 리본 구성 — 어떤 탭·그룹에 어떤 엔진 명령을 둘지(MFC 샘플 `LotCAD_MFCDlg_Ribbon.cpp` 와 같은 구성) |
| `RibbonBar.cs` | 리본 컨트롤 — 탭 줄 · 그룹 · 큰/작은 버튼 · 켜짐 표시 |
| `RibbonIcons.cs` | 리본 아이콘 — 선으로 그린다(MFC 샘플 `RibbonIcons.cpp` 를 옮긴 것) |
| `AnalysisPanel.cs` · `Analysis.cs` | 해석 패널 — 바람 터널 · 물 · 구조 해석 |
| `LayerPanel.cs` | 도면 패널 — 도면층 · 선종류 · 블록(외부 참조). 오른쪽 패널 공용 틀 `SidePanel` 도 여기 |
| `ToolsPanel.cs` | 도구 패널 — 분해도 · 메시 수리 |

## 리본

| 탭 | 그룹 | 부르는 것 |
|----|------|-----------|
| 홈 | 기즈모 · 편집 · 선택 · 실행 · 뷰 | 엔진 명령(`gm` `m` `ro` `3a` `selectall` …) · `CAD_Undo` · `CAD_SetView` · `CAD_SetProjection` |
| 2D | 그리기 · 수정 | 엔진 명령(`l` `rec` `c` `dim` `of` `tr` `fil` …) |
| 3D | 프리미티브 · 형상 · 편집 | 엔진 명령(`b` `cube` `x` `rev` `union` …) · 차집합은 `CAD_BooleanSubtract`(기준 → 뺄 것 두 단계) |
| 도구 | 해석 · 모델 · 이미지 | 해석 패널 · 명령 `graph on/off` · 분해도·메시 수리 패널 · `CAD_AttachImageFromFile` · 명령 `imagerotate` 등 |
| 관리 | 도면층 · 블록 · 파일 | 도면 패널 · 명령 `block` · `bedit` · STEP 열기 · STEP·DWG 저장(`CAD_OpenFile` · `CAD_SaveAs`) |

버튼은 진행 중인 도구를 먼저 끝내고(`CAD_CancelCommand`) 명령을 시작한다. 누른 뒤 키보드는 렌더 창으로 돌아가,
명령이 묻는 값(블록 이름 · 기준점 …)을 3D 뷰에서 바로 친다. 패널을 여는 버튼은 다시 누르면 닫는다.
MFC 샘플 도구 탭의 '단면 · 내비 · 파티클' 은 그 샘플의 호스트 패널이라 여기엔 없다.

## 메뉴

| 메뉴 | 항목 |
|------|------|
| 파일 | 열기 · 다른 이름으로 저장 · 내보내기(STEP·DWG·DXF·STL·OBJ·GLB) — 포맷은 확장자 |
| 도면 | 도면층 · 선종류 · 블록 만들기 · 블록 편집 · 블록·외부 참조 |
| 도구 | 노드 그래프 · 분해도 · 메시 수리 · 이미지 ▸ · 동적 입력(F12) |
| 해석 | 바람 터널 · 물 · 구조 해석 |

명령이 끝나면 만든·지운 객체 수가 상태바에 뜬다(`CAD_AddEventListener` — 명령 시작·끝·취소, 객체 생성·삭제).

## 핵심 계약 (엔진 측)

```
CAD_AttachView(hwnd, w, h)   // 렌더할 HWND 를 먼저 등록
CAD_CreateEngine()           // 그 HWND(Win32NativeViewWindow)에 Vulkan 렌더
CAD_Tick()                   // 매 프레임 1회
CAD_ResizeView(w, h)         // 크기 변경 시
CAD_OnMouse* / CAD_OnKeyDownVK   // 입력 (VK 코드는 내부에서 GLFW 로 변환)
```

## 빌드 & 실행

1. 준비물은 레포의 `sdk/` 에 다 있다 — `LotCADCore.dll` + `models/ textures/ fonts/`.
   (셰이더는 라이브러리에 SPIR-V 로 내장돼 있어 별도 파일이 없다.)

2. WPF 샘플 빌드 (post-build 이 DLL+에셋을 출력 폴더로 자동 복사):
   ```
   cd sample/wpf_test
   dotnet build -c Debug
   ```
   - `LotCadWpf.csproj` 의 `CadCoreBuildDir` 가 `..\..\sdk` 를 가리킴. 경로 다르면 조정.

3. 실행:
   ```
   dotnet run -c Debug
   ```
   또는 `bin/Debug/net8.0-windows/LotCadWpf.exe`.

## 주의

- **x64 고정**: 네이티브 DLL 이 x64 이므로 `PlatformTarget=x64`. AnyCPU 로 두면 BadImageFormat.
- `vulkan-1.dll` 은 GPU 드라이버가 System32 에 설치 (재배포 불필요).
- 런타임 에셋(`fonts/` 등)이 exe 옆에 없으면 치수·문자가 생성되지 않는다 → 상태바에 표시.
- **Airspace**: HwndHost 자식 창이 WPF 컨텐츠 위에 떠서, 렌더 영역 위에 WPF 컨트롤을
  겹칠 수 없다(팝업/오버레이는 별도 처리 필요).
- **키보드**: 렌더 창은 Win32 자식이라 그 안의 키는 WPF 를 거치지 않는다 — F12 는 `VulkanHost` 가 가로채 창에 알린다.
  메뉴·리본으로 명령을 시작한 뒤엔 `VulkanHost.FocusView` 로 키보드를 렌더 창에 돌려준다(메뉴가 닫힌 뒤로 미뤄서).
- **엔진 이벤트 순서**: 바로 끝나는 명령(cube 등)은 한 틱에 시작 → 끝 → 생성 순으로 온다. '끝' 에서 바로 세면 0 이라
  `Dispatcher.BeginInvoke` 로 미뤄 그 틱의 이벤트가 다 온 뒤 적는다. 콜백 델리게이트는 필드로 붙들어 둔다(GC).

## 미구현 / 다음 단계

- 도면층 지우기·현재 도면층 정하기, 있는 블록 정의를 한 번 더 놓기, 동적 입력·노드 그래프 상태 읽기는 C API 에 아직 없다
  (새로 그린 객체는 '선택한 객체를 이 도면층으로', 블록은 블록 참조를 복사, 동적 입력·그래프는 호스트가 상태를 들고 있음).
- 마우스 modifiers(Ctrl/Shift) 전달은 현재 0 고정 — 다중선택 등 필요 시 비트 채우기.
