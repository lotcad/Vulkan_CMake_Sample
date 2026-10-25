import UIKit
import CLotCAD
import Foundation

struct CADPoint {
    let x: Float
    let y: Float
    let z: Float
}

// 엔진 좌표(월드 mm, double)
extension CADPoint {
    var ge: CAD_GeVec3 { CAD_GeVec3(x: Double(x), y: Double(y), z: Double(z)) }
}

// macOS 의 LotCADEngine 을 iOS UIView 기반으로 미러링.
// 거의 동일한 API — attach 만 UIView 를 받고, 내부적으로 CAD_AttachView 에 UIView 포인터 전달.
final class LotCADEngine {
    private(set) var isCreated = false
    private var demoObjectIds: [UInt32] = []

    func setRuntimeAssetPath(_ path: String) -> Bool {
        CAD_SetRuntimeAssetPath(path)
    }

    @MainActor func attach(to view: UIView) {
        CAD_AttachView(
            Unmanaged.passUnretained(view).toOpaque(),
            Int32(max(1.0, view.bounds.width)),
            Int32(max(1.0, view.bounds.height)))
    }

    func create() -> Bool {
        guard !isCreated else { return true }
        isCreated = CAD_CreateEngine()
        // 손가락/가상 커서는 마우스만큼 정밀하지 않다 — 스냅 반경(12→18px)과 **선택 탭 픽 반경**
        // (선·폴리선·치수 10→30px)을 같이 키운다. 이 호출이 빠지면 데스크톱과 같은 픽셀 값이라
        // 3배 레티나에선 3pt 남짓 — 치수선·보조선·값 문자를 탭해도 거의 안 잡힌다.
        if isCreated { CAD_SetSnapTouchMode(true) }
        // 모바일에서 치수는 도면 요소보다 "측정 도구" 다 — 줌아웃해도 값이 읽혀야 한다.
        // 켜면 치수 문자만 줌과 무관하게 화면상 같은 크기로 유지된다(선·화살표는 그대로).
        if isCreated { CAD_SetDimensionTextScreenFixed(true) }
        return isCreated
    }

    func tick() -> Bool {
        guard isCreated else { return false }
        return CAD_Tick()
    }

    func resize(to size: CGSize) {
        guard isCreated else { return }
        CAD_ResizeView(
            Int32(max(1.0, size.width)),
            Int32(max(1.0, size.height)))
    }

    func createDemoScene() {
        guard isCreated, demoObjectIds.isEmpty else { return }

        let boxId = createBox(
            center: CADPoint(x: 0.0, y: 0.0, z: 1.0),
            scale: CADPoint(x: 0.5, y: 0.5, z: 0.5))
        if boxId != 0 {
            CAD_SetPosition(boxId, CAD_GeVec3(x: 1.0, y: 0.0, z: 1.5))
            CAD_SetScale(boxId, CAD_GeVec3(x: 0.8, y: 0.8, z: 0.8))
            CAD_SetRotationAxisAngle(boxId, CAD_GeVec3(x: 0.0, y: 0.0, z: 1.0), 0.7853982)
            _ = CAD_SetSelection([boxId], 1, Int32(CAD_SELECT_REPLACE))
        }

        _ = createLine(
            from: CADPoint(x: -3.0, y: -1.4, z: 0.05),
            to: CADPoint(x: -1.2, y: -0.2, z: 0.05))
        _ = createCircle(
            center: CADPoint(x: -2.0, y: 1.0, z: 0.05),
            radius: 0.55,
            normal: CADPoint(x: 0.0, y: 0.0, z: 1.0))
        _ = createPolygon(
            center: CADPoint(x: 0.0, y: -1.3, z: 0.05),
            radius: 0.65,
            sides: 6,
            normal: CADPoint(x: 0.0, y: 0.0, z: 1.0),
            firstVertexDir: CADPoint(x: 1.0, y: 0.0, z: 0.0))
        _ = createArc(
            start: CADPoint(x: 1.1, y: -1.1, z: 0.05),
            through: CADPoint(x: 1.9, y: -0.2, z: 0.05),
            end: CADPoint(x: 2.7, y: -1.1, z: 0.05))
        _ = createPolyline(
            points: [
                CADPoint(x: 1.2, y: 0.7, z: 0.05),
                CADPoint(x: 1.8, y: 1.3, z: 0.05),
                CADPoint(x: 2.5, y: 0.9, z: 0.05),
                CADPoint(x: 2.7, y: 1.6, z: 0.05)
            ],
            closed: false)

        CAD_ZoomExtents()
    }

    @discardableResult
    func createBox(center: CADPoint, scale: CADPoint) -> UInt32 {
        guard isCreated else { return 0 }
        var id: UInt32 = 0
        _ = CAD_CreateBox(center.ge, scale.ge, nil, &id)
        trackDemoObject(id)
        return id
    }

    @discardableResult
    func createLine(from start: CADPoint, to end: CADPoint) -> UInt32 {
        guard isCreated else { return 0 }
        var id: UInt32 = 0
        _ = CAD_CreateLine(start.ge, end.ge, nil, &id)   // 결과 코드(0 = 성공) — 실패면 id 0, 이유는 CAD_GetLastError
        trackDemoObject(id)
        return id
    }

    @discardableResult
    func createCircle(center: CADPoint, radius: Float, normal: CADPoint) -> UInt32 {
        guard isCreated else { return 0 }
        var id: UInt32 = 0
        _ = CAD_CreateCircle(center.ge, Double(radius), normal.ge, nil, &id)
        trackDemoObject(id)
        return id
    }

    @discardableResult
    func createPolygon(
        center: CADPoint,
        radius: Float,
        sides: Int32,
        normal: CADPoint,
        firstVertexDir: CADPoint
    ) -> UInt32 {
        guard isCreated else { return 0 }
        var id: UInt32 = 0
        _ = CAD_CreatePolygon(center.ge, Double(radius), sides, normal.ge, firstVertexDir.ge, nil, &id)
        trackDemoObject(id)
        return id
    }

    @discardableResult
    func createArc(start: CADPoint, through: CADPoint, end: CADPoint) -> UInt32 {
        guard isCreated else { return 0 }
        var id: UInt32 = 0
        _ = CAD_CreateArc(start.ge, through.ge, end.ge, nil, &id)
        trackDemoObject(id)
        return id
    }

    @discardableResult
    func createPolyline(points: [CADPoint], closed: Bool) -> UInt32 {
        guard isCreated, points.count >= 2 else { return 0 }
        let pts = points.map { $0.ge }
        var id: UInt32 = 0
        _ = pts.withUnsafeBufferPointer { buffer in
            CAD_CreatePolyline(buffer.baseAddress, UInt32(pts.count), closed, nil, &id)
        }
        trackDemoObject(id)
        return id
    }

    @discardableResult
    func createRectangle(corner0: CADPoint, corner2: CADPoint) -> UInt32 {
        guard isCreated else { return 0 }
        var id: UInt32 = 0
        _ = CAD_CreateRectangle(corner0.ge, corner2.ge, nil, &id)
        trackDemoObject(id)
        return id
    }

    @discardableResult
    func createExtrude(sourceId: UInt32, height: Float) -> UInt32 {
        guard isCreated else { return 0 }
        var id: UInt32 = 0
        _ = CAD_CreateExtrude(sourceId, Double(height), nil, &id)
        trackDemoObject(id)
        return id
    }

    // ─── 툴바 버튼 (Android MainActivity 미러링) ───
    // 큐브 추가/전체선택/삭제/전체삭제/줌은 appCommands_ 큐를 거쳐 iOS render-on-demand 에서도
    // 자동으로 한 프레임 렌더됨. Undo/Redo 는 즉시 실행이라 C++ 측에서 markInputDirty 처리.
    func addCube()          { startCommand("cube") }
    func selectAll()        { startCommand("selectall") }
    func deleteSelected()   { startCommand("delete") }
    func clearAll()         { guard isCreated else { return }; _ = CAD_ClearAll() }
    func zoomExtents()      { guard isCreated else { return }; CAD_ZoomExtents() }

    // ─── 명령 실행 ───
    // 데스크톱 명령행과 같은 이름을 그대로 쓴다. 진행 중인 도구에 좌표/값도 넘길 수 있다
    // (예: executeCommand("2,3")). 모바일은 키보드를 띄우기 부담스러워 버튼에서 호출한다.
    @discardableResult
    func executeCommand(_ name: String) -> Bool {
        guard isCreated else { return false }
        return CAD_ExecuteCommand(name) == 0   // 0 = CAD_OK, 모르는 명령 = CAD_E_NOT_FOUND(음수)
    }

    /// 버튼용 — 진행 중인 명령·도구를 먼저 끝내고(선택은 그대로) 새 명령을 시작한다(오토캐드 ^C^C).
    /// executeCommand 만 부르면 선 그리던 중 "rect" 가 값으로 먹혀 도구가 안 바뀐다.
    @discardableResult
    func startCommand(_ name: String) -> Bool {
        guard isCreated else { return false }
        _ = CAD_CancelCommand()
        return CAD_ExecuteCommand(name) == 0
    }

    /// 진행 중인 명령·도구를 ESC 처럼 그 자리에서 끝낸다(선택은 그대로)
    func cancelCommand() { guard isCreated else { return }; _ = CAD_CancelCommand() }

    /// 직교 ↔ 원근 — 명령("proj")으로 보내면 그리는 중엔 값으로 먹혀 안 바뀐다, 보기 함수로 바로
    func toggleProjection() {
        guard isCreated else { return }
        var ortho = false
        if CAD_GetProjection(&ortho) == 0 { _ = CAD_SetProjection(!ortho) }   // 0 = CAD_OK
    }

    // ─── 측정 — 선택만 하면 값이 나온다 ───
    // 점 찍기·스냅·치수 객체 생성이 전혀 없어서 모바일에서 가장 쓰기 쉬운 경로다.
    // 잴 게 없거나 선택이 비면 0.
    func selectedCount() -> UInt32 { isCreated ? UInt32(max(0, CAD_GetSelection(nil, 0))) : 0 }   // nil, 0 = 개수만
    /// 진행 중인 치수 도구의 점 개수. 비활성이면 -1.
    /// 클라이언트가 클릭을 세면 엔진이 클릭을 거부할 때 어긋나므로 **엔진 값을 본다**.
    /// 엔진은 비활성이면 CAD_E_NOT_READY(음수)를 준다 — 이 래퍼의 약속(-1)으로 맞춘다.
    func dimensionPointCount() -> Int32 {
        guard isCreated else { return -1 }
        let n = CAD_GetDimensionPointCount()
        return n < 0 ? -1 : n
    }

    /// 진행 중인 도구의 안내 문구. 도구가 없으면 빈 문자열.
    /// 도구 종류와 무관하게 "지금 뭘 해야 하는지" 를 엔진에서 그대로 받아 쓴다.
    func prompt() -> String {
        guard isCreated else { return "" }
        var buf = [CChar](repeating: 0, count: 256)
        let n = CAD_GetPrompt(&buf, UInt32(buf.count))   // 반환 = 전체 길이, 넘치면 잘라 담는다
        return n > 0 ? String(decoding: buf.prefix { $0 != 0 }.map { UInt8(bitPattern: $0) }, as: UTF8.self) : ""
    }

    // ─── 그리기 (전부 점 찍기 → 커서로 데스크톱과 동일하게 동작) ───
    func drawLine()      { startCommand("line") }
    func drawRectangle() { startCommand("rec") }
    func drawCircle()    { startCommand("c") }
    func drawArc()       { startCommand("a") }
    func drawPolyline()  { startCommand("pl") }
    func drawPolygon()   { startCommand("pol") }
    func selectionLength() -> Float {
        var v = 0.0
        if isCreated { _ = CAD_GetSelectionLength(&v) }
        return Float(v)
    }
    func selectionArea() -> Float {
        var v = 0.0
        if isCreated { _ = CAD_GetSelectionArea(&v) }
        return Float(v)
    }

    // ─── 치수 (전부 "점 찍기" 방식 — 대화상자 불필요라 모바일에서 그대로 동작) ───
    func dimAligned()  { startCommand("dim") }   // 정렬 치수
    func dimLinear()   { startCommand("dli") }   // 수평·수직
    func dimAngular()  { startCommand("dan") }   // 각도
    func dimRadius()   { startCommand("dra") }   // 반지름
    func dimDiameter() { startCommand("ddi") }   // 지름

    /// 경로의 모델/도면을 씬에 연다. 지원: .lot .obj .stl .dxf .ply .gltf .glb
    /// - 주의: `.gltf`(분리형)는 `.bin`·텍스처가 같은 폴더에 있어야 한다.
    ///   모바일 파일 선택기는 파일 하나만 주므로 **단일 파일인 `.glb` 권장**.
    @discardableResult
    func openFile(_ path: String) -> Bool {
        guard isCreated else { return false }
        return CAD_OpenFile(path)
    }
    // viewType: 0=Front 1=Top 2=Right 3=Iso
    func setView(_ viewType: Int32) { guard isCreated else { return }; CAD_SetView(viewType) }
    func undo()             { guard isCreated else { return }; CAD_Undo() }
    func redo()             { guard isCreated else { return }; CAD_Redo() }
    func objectCount() -> UInt32 { isCreated ? UInt32(max(0, CAD_GetObjectCount())) : 0 }

    // ─── 명령 요청 (SwiftUI 버튼/패널용) ───
    // 도구 시작·선택지 — 엔진 명령 이름으로(명령행에 치는 것과 같은 길)
    // 시작은 startCommand(앞 도구를 끝내고), 진행 중 도구의 선택지(sides·arcmode)는 executeCommand(값으로 들어감)
    func startLineSketch() { startCommand("line") }
    func startRectangleSketch() { startCommand("rect") }
    func startCircleSketch() { startCommand("circle") }
    func startPolygonSketch() { startCommand("polygon") }
    func cyclePolygonSides() { executeCommand("sides") }
    func startExtrude() { startCommand("extrude") }
    func startArcSketch() { startCommand("arc") }
    func cycleArcMode() { executeCommand("arcmode") }
    func startPolylineSketch() { startCommand("polyline") }
    func startLightPlacement() { startCommand("light") }
    func cycleMaterial() { guard isCreated else { return }; _ = CAD_CycleMaterial() }
    func removeMaterial() { guard isCreated else { return }; _ = CAD_RemoveMaterial() }
    func adjustTextureScale(_ delta: Float) {
        guard isCreated else { return }
        _ = CAD_AdjustTextureScale(Double(delta))
    }
    func adjustLineWidth(_ deltaPx: Float) {
        guard isCreated else { return }
        _ = CAD_AdjustLineWidth(Double(deltaPx))
    }
    // 옮기기·돌리기·축척·복사·색 — C API 는 대상 id 를 받는다(CAD_Entity*). 돌리기·축척 기준점 = 고른 것 전체 경계 상자 가운데
    // CAD_GetSelection: 개수만 먼저(nil, 0) 묻고 그만큼 칸을 잡아 한 번에 받는다
    private var selectedIds: [UInt32] {
        let n = CAD_GetSelection(nil, 0)
        guard n > 0 else { return [] }
        var ids = [UInt32](repeating: 0, count: Int(n))
        let got = Int(max(0, min(n, CAD_GetSelection(&ids, UInt32(n)))))
        return ids.prefix(got).filter { $0 != 0 }
    }
    private func offset(_ direction: CADPoint, _ distance: Float) -> CAD_GeVec3? {
        let len = (direction.x * direction.x + direction.y * direction.y + direction.z * direction.z).squareRoot()
        guard len > 1e-9 else { return nil }
        let s = Double(distance / len)
        return CAD_GeVec3(x: Double(direction.x) * s, y: Double(direction.y) * s, z: Double(direction.z) * s)
    }
    private func selectionCenter(_ ids: [UInt32]) -> CAD_GeVec3? {
        var lo = CAD_GeVec3(x: .infinity, y: .infinity, z: .infinity), hi = CAD_GeVec3(x: -.infinity, y: -.infinity, z: -.infinity)
        for id in ids {
            var a = CAD_GeVec3(), b = CAD_GeVec3()
            guard CAD_EntityGetExtents(id, &a, &b) == 0 else { continue }   // 0 = CAD_OK
            lo = CAD_GeVec3(x: min(lo.x, a.x), y: min(lo.y, a.y), z: min(lo.z, a.z))
            hi = CAD_GeVec3(x: max(hi.x, b.x), y: max(hi.y, b.y), z: max(hi.z, b.z))
        }
        guard lo.x <= hi.x else { return nil }
        return CAD_GeVec3(x: (lo.x + hi.x) / 2, y: (lo.y + hi.y) / 2, z: (lo.z + hi.z) / 2)
    }
    func moveSelected(direction: CADPoint, distance: Float) {
        guard isCreated, let d = offset(direction, distance) else { return }
        let ids = selectedIds
        _ = CAD_EntityMove(ids, UInt32(ids.count), d)
    }
    func rotateSelected(axis: CADPoint, angleDegrees: Float) {
        guard isCreated else { return }
        let ids = selectedIds
        guard let c = selectionCenter(ids) else { return }
        let a = CAD_GeVec3(x: Double(axis.x), y: Double(axis.y), z: Double(axis.z))
        _ = CAD_EntityRotate(ids, UInt32(ids.count), c, a, Double(angleDegrees) * .pi / 180)   // 각 = rad
    }
    func scaleSelected(factor: Float) {
        guard isCreated, factor > 0 else { return }
        let ids = selectedIds
        guard let c = selectionCenter(ids) else { return }
        _ = CAD_EntityScale(ids, UInt32(ids.count), c, Double(factor))
    }
    func copySelected(direction: CADPoint, distance: Float, count: Int32) {
        guard isCreated, count > 0, let d = offset(direction, distance) else { return }
        let ids = selectedIds
        let zero = CAD_GeVec3()
        var made = [UInt32](repeating: 0, count: ids.count * Int(count))   // 사본 = count × 고른 수
        _ = CAD_EntityArrayRect(ids, UInt32(ids.count), UInt32(count) + 1, 1, 1, d, zero, zero, &made, UInt32(made.count))
    }
    func colorSelected(_ color: CADPoint) {
        guard isCreated else { return }
        for id in selectedIds { _ = CAD_SetColor(id, CAD_Color(r: Double(color.x), g: Double(color.y), b: Double(color.z))) }
    }

    // ─── 입력 (터치/제스처 → 엔진 마우스 이벤트) ───
    // 엔진 버튼 규약: 0=left(select), 1=right(orbit), 2=middle(pan)
    func mouseDown(button: Int32, x: Double, y: Double, modifiers: Int32) {
        guard isCreated else { return }
        CAD_OnMouseDown(button, x, y, modifiers)
    }

    func mouseUp(button: Int32, x: Double, y: Double, modifiers: Int32) {
        guard isCreated else { return }
        CAD_OnMouseUp(button, x, y, modifiers)
    }

    func mouseMove(x: Double, y: Double) {
        guard isCreated else { return }
        CAD_OnMouseMove(x, y)
    }

    func mouseWheel(x: Double, y: Double, deltaX: Double, deltaY: Double) {
        guard isCreated else { return }
        CAD_OnMouseWheel(x, y, deltaX, deltaY)
    }

    // (x,y) 에 기즈모 핸들이 있는지 — 1손가락 드래그를 기즈모 조작 vs 궤도회전으로 라우팅.
    func gizmoHitTest(x: Double, y: Double) -> Bool {
        guard isCreated else { return false }
        return CAD_GizmoHitTest(x, y) != 0
    }

    func setGizmoTouchMode(_ enabled: Bool) {
        guard isCreated else { return }
        CAD_SetGizmoTouchMode(enabled)
    }

    func shutdown() {
        for id in demoObjectIds.reversed() {
            CAD_DeleteObject(id)
        }
        demoObjectIds.removeAll()
        if isCreated {
            CAD_DestroyEngine()
            isCreated = false
        }
    }

    private func trackDemoObject(_ id: UInt32) {
        if id != 0 {
            demoObjectIds.append(id)
        }
    }

    // 시험용 명령 "focustext 1018@5" — 그 글자인 문자 객체(같은 글자면 N 번째, 0부터 id 순)를 골라 맞춰 보기
    func focusText(_ spec: String) {
        var want = spec, nth = 0
        if let at = spec.lastIndex(of: "@") { want = String(spec[..<at]); nth = Int(spec[spec.index(after: at)...]) ?? 0 }
        var ids = [UInt32](repeating: 0, count: 20000)
        let n = max(0, Int(CAD_QueryObjects("{\"kind\":\"text\"}", &ids, UInt32(ids.count))))
        var buf = [CChar](repeating: 0, count: 8192)
        for id in ids.prefix(n).sorted() {
            guard CAD_GetObjectJson(id, &buf, UInt32(buf.count)) > 0 else { continue }
            let json = String(decoding: buf.prefix { $0 != 0 }.map { UInt8(bitPattern: $0) }, as: UTF8.self)
            guard json.contains("\"text\":\"\(want)\"") else { continue }
            if nth > 0 { nth -= 1; continue }
            _ = CAD_SetSelection([id], 1, Int32(CAD_SELECT_REPLACE))
            CAD_FocusSelected()
            print("[test] focus text id \(id)")
            return
        }
        print("[test] focus text not found: \(spec)")
    }
}
