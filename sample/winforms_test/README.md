# LotCAD — WinForms 호스트 샘플 (.NET 8)

WinForms 창 안에 LotCAD 엔진을 임베드하는 샘플. `wpf_test` 와 같은 화면에, 도면층·선종류·블록·분해도·메시 수리 같은
데스크톱 CAD 기능을 메뉴와 오른쪽 패널로 더했다. `LotCADCore.dll` 의 C API 를 P/Invoke 로 호출한다
(`CadApi.cs` 는 이 샘플이 쓰는 함수만 — 전체 선언은 `sdk/csharp`).

WPF 와 다른 점은 하나 — WinForms 컨트롤은 처음부터 자기 HWND 가 있어서 `HwndHost` 로 자식 창을 따로 만들 필요 없이
**컨트롤의 `Handle` 을 그대로 엔진에 넘긴다.**

## 구조

| 파일 | 역할 |
|------|------|
| `CadApi.cs` | `LotCADCore.dll` 의 `CAD_*` P/Invoke 선언 |
| `VulkanPanel.cs` | 렌더 영역 `Control` — `OnHandleCreated` 에서 `CAD_AttachView(Handle)` → `CAD_CreateEngine`, `WndProc` 에서 마우스/키 라우팅 |
| `MainForm.cs` | 메뉴 · 툴바(그리기/편집/뷰) · 왼쪽 정보 · 상태바 (디자이너 없이 코드로) + 유휴 루프 → `CAD_Tick`, 엔진 이벤트·F12 |
| `AnalysisPanel.cs` · `Analysis.cs` | 해석 패널 — 바람 터널 · 물 · 구조 해석 |
| `LayerPanel.cs` | 도면 패널 — 도면층 · 선종류 · 블록(외부 참조). 오른쪽 패널 공용 틀 `SidePanel` 도 여기 |
| `ToolsPanel.cs` | 도구 패널 — 분해도 · 메시 수리 |
| `Program.cs` | 진입점 (`ApplicationConfiguration.Initialize` — 고DPI PerMonitorV2) |

## 메뉴

| 메뉴 | 항목 | 부르는 것 |
|------|------|-----------|
| 파일 | 열기 · 다른 이름으로 저장 · 내보내기(STEP·DWG·DXF·STL·OBJ·GLB) | `CAD_OpenFile` · `CAD_SaveAs` — 포맷은 확장자 |
| 도면 | 도면층 · 선종류 · 블록·외부 참조 패널 | `CAD_GetLayersJson` · `CAD_SetLayer*` · `CAD_SetObjectLinetype` · `CAD_GetBlocksJson` · `CAD_Xref*` |
| 도면 | 블록 만들기 · 블록 편집 | 명령 `block`(이름·기준점을 명령행이 묻는다) · `bedit` |
| 도구 | 노드 그래프 | 명령 `graph on/off` — 그래프 칸은 엔진이 Vulkan 으로 그려 창 안에서도 보인다 |
| 도구 | 분해도 · 메시 수리 패널 | `CAD_ExplodeView` · `CAD_CheckMesh` · `CAD_RepairMeshes` 등 |
| 도구 | 이미지 ▸ 붙이기 · 회전 · 뒤집기 · 배경 지우기 · 자르기 | `CAD_AttachImageFromFile` · 명령 `imagerotate` 등(선택한 이미지에) |
| 도구 | 동적 입력 (F12) | 명령 `dyn on/off` — 그리는 중엔 F12 키 |
| 해석 | 바람 터널 · 물 · 구조 해석 패널 | `CAD_WindTunnel` · `CAD_Water` · `CAD_StructuralAnalysis` |

명령이 끝나면 만든·지운 객체 수가 상태바에 뜬다(`CAD_AddEventListener` — 명령 시작·끝·취소, 객체 생성·삭제).

## 핵심 계약 (엔진 측)

```
CAD_SetRuntimeAssetPath(exe 폴더)   // 엔진 생성 전 (0 = CAD_OK)
CAD_AttachView(hwnd, w, h)          // 렌더할 HWND 를 먼저 등록
CAD_CreateEngine()                  // 그 HWND 에 Vulkan 렌더
CAD_Tick()                          // 매 프레임 1회 (Application.Idle + PeekMessage 루프)
CAD_ResizeView(w, h)                // 크기 변경 시 (Tick 안에서 ClientSize 비교)
CAD_OnMouse* / CAD_OnKeyDownVK      // 입력 (VK 코드는 내부에서 GLFW 로 변환)
```

## 빌드 & 실행

```
cd sample/winforms_test
dotnet build -c Debug
dotnet run -c Debug
```

post-build 이 `../../sdk` 의 `LotCADCore.dll` + `models/ textures/ fonts/` 를 출력 폴더로 복사한다
(`CadCoreBuildDir` 로 경로 조정). 실행 파일은 `bin/Debug/net8.0-windows/LotCadWinForms.exe`.

## WinForms 에서 챙긴 것

- **배경 안 칠하기**: `ControlStyles.Opaque | UserPaint | AllPaintingInWmPaint`, 더블버퍼 끔 — 안 하면 GDI 가 Vulkan 화면을 덮어 깜빡인다.
- **키를 엔진으로**: `IsInputKey` 가 전부 `true` — 방향키·Tab(도구 옵션 순환)·ESC 가 폼의 포커스 이동으로 새지 않는다.
  툴바 버튼은 `TabStop=false` 이고 누른 뒤 포커스를 렌더 영역으로 돌린다.
- **버튼 크기**: `AutoSizeMode.GrowAndShrink` — 기본(GrowOnly)은 너비 75 아래로 안 줄어 툴바가 창 밖으로 넘친다.
- **도킹 순서**: 나중에 `Controls.Add` 한 것부터 자리를 잡는다 → 렌더(Fill)를 먼저, 메뉴를 마지막에.
- **x64 고정**: 네이티브 DLL 이 x64 이므로 `PlatformTarget=x64`. AnyCPU 로 두면 BadImageFormat.

- **엔진 이벤트 순서**: 바로 끝나는 명령(cube 등)은 한 틱에 시작 → 끝 → 생성 순으로 온다. '끝' 에서 바로 세면 0 이라
  `BeginInvoke` 로 미뤄 그 틱의 이벤트가 다 온 뒤 적는다. 콜백 델리게이트는 필드로 붙들어 둔다(GC).
- **패널은 엔진보다 먼저 만들어진다**: 폼 필드라서 — 엔진에 묻는 것(선종류 표 등)은 패널이 처음 보일 때부터.

## 미구현 / 다음 단계

- 도면층 지우기·현재 도면층 정하기, 있는 블록 정의를 한 번 더 놓기, 동적 입력 상태 읽기는 C API 에 아직 없다
  (새로 그린 객체는 '선택한 객체를 이 도면층으로', 블록은 블록 참조를 복사, 동적 입력은 호스트가 상태를 들고 있음).
- 마우스 modifiers(Ctrl/Shift) 는 0 고정 — 다중선택 등 필요 시 비트 채우기.
