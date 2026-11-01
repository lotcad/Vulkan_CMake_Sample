import AppKit
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

final class LotCADEngine {
    private(set) var isCreated = false
    private var demoObjectIds: [UInt32] = []

    func setRuntimeAssetPath(_ path: String) -> Bool {
        CAD_SetRuntimeAssetPath(path) == 0   // 결과 코드 — 0 = CAD_OK
    }

    @MainActor func attach(to view: NSView) {
        CAD_AttachView(
            Unmanaged.passUnretained(view).toOpaque(),
            Int32(max(1.0, view.bounds.width)),
            Int32(max(1.0, view.bounds.height)))
    }

    func create() -> Bool {
        guard !isCreated else { return true }
        isCreated = CAD_CreateEngine()
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

    /// 엔진 명령을 이름으로 실행한다 — 하단 명령행에 치는 것과 같다.
    ///
    /// 개별 래퍼(createBox 등)는 자주 쓰는 것만 있고 엔진에는 명령이 200개가 넘는다.
    /// 없는 기능은 이걸로 부르면 된다. 진행 중인 도구엔 값으로 전달된다.
    ///
    ///     engine.execute("trim")
    ///     engine.execute("circle"); engine.execute("2")   // 반지름 2
    @discardableResult
    func execute(_ command: String) -> Bool {
        guard isCreated else { return false }
        return CAD_ExecuteCommand(command) == 0   // 0 = CAD_OK, 모르는 명령 = CAD_E_NOT_FOUND(음수)
    }

    /// 도구 막대·메뉴 버튼용 — 진행 중인 명령·도구를 먼저 끝내고(선택은 그대로) 새 명령을 시작한다(오토캐드 ^C^C).
    /// execute 만 부르면 선 그리던 중 "rec" 가 값으로 먹혀 도구가 안 바뀐다.
    @discardableResult
    func startCommand(_ command: String) -> Bool {
        guard isCreated else { return false }
        _ = CAD_CancelCommand()
        return CAD_ExecuteCommand(command) == 0
    }

    // ── 알림(콜백) ──
    // ⚠️ Swift 클로저를 그대로 넘길 수 없다(C 함수 포인터는 문맥을 못 가진다).
    //    전역에 보관해 두고 C 함수에서 꺼내 쓴다.
    //    호출 시점은 tick() 안이라 여기서 UI 를 바로 고쳐도 된다.
    //    ⚠️ C 함수 포인터는 @convention(c) 라 액터에 속할 수 없다. 그런데 보관소는
    //    @MainActor 다 — 그래서 안에서 assumeIsolated 로 "여기는 메인" 임을 알린다.
    //    거짓말이 아니라 사실이다: 이 콜백들은 전부 CAD_Tick 안에서 불린다.
    //    객체·선택·문서 알림은 CAD_AddEventListener 하나(엔진 2e-1 — 한 칸짜리 CAD_SetOnXxx 는 지워졌다).
    //    리스너 하나를 걸고 kind 로 갈라 보관소의 처리기를 부른다. 엔진이 있어야 걸린다(create 뒤).
    private var eventListenerHandle: UInt32 = 0

    @MainActor
    private func refreshEventListener() {
        guard isCreated else { return }
        if eventListenerHandle != 0 {
            _ = CAD_RemoveEventListener(eventListenerHandle)
            eventListenerHandle = 0
        }
        var kinds: UInt32 = 0
        if LotCADEngineCallbacks.objectCreated != nil { kinds |= UInt32(CAD_EVENT_OBJECT_CREATED) }
        if LotCADEngineCallbacks.objectDeleted != nil { kinds |= UInt32(CAD_EVENT_OBJECT_DELETED) }
        if LotCADEngineCallbacks.selectionChanged != nil { kinds |= UInt32(CAD_EVENT_SELECTION_CHANGED) }
        if LotCADEngineCallbacks.documentDirty != nil { kinds |= UInt32(CAD_EVENT_DOCUMENT_DIRTY) }
        guard kinds != 0 else { return }
        var handle: UInt32 = 0
        let status = CAD_AddEventListener(kinds, { kind, id, _ in
            MainActor.assumeIsolated { LotCADEngineCallbacks.dispatch(kind: kind, id: id) }
        }, nil, 0, &handle)
        if status == 0 { eventListenerHandle = handle }   // 0 = CAD_OK
    }

    @MainActor
    func onSelectionChanged(_ handler: (() -> Void)?) {
        LotCADEngineCallbacks.selectionChanged = handler
        refreshEventListener()
    }

    @MainActor
    func onObjectCreated(_ handler: ((UInt32) -> Void)?) {
        LotCADEngineCallbacks.objectCreated = handler
        refreshEventListener()
    }

    @MainActor
    func onObjectDeleted(_ handler: ((UInt32) -> Void)?) {
        LotCADEngineCallbacks.objectDeleted = handler
        refreshEventListener()
    }

    @MainActor
    func onPrompt(_ handler: ((String) -> Void)?) {
        LotCADEngineCallbacks.prompt = handler
        _ = CAD_SetOnPrompt(handler == nil ? nil : { text in
            let s = text.map { String(cString: $0) } ?? ""
            MainActor.assumeIsolated { LotCADEngineCallbacks.prompt?(s) }
        })
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

    // 도구 시작·선택지 — 엔진 명령 이름으로(명령행에 치는 것과 같은 길)
    func startLineSketch() { execute("line") }
    func startRectangleSketch() { execute("rect") }
    func startCircleSketch() { execute("circle") }
    func startPolygonSketch() { execute("polygon") }
    func cyclePolygonSides() { execute("sides") }
    func startExtrude() { execute("extrude") }
    func startArcSketch() { execute("arc") }
    func cycleArcMode() { execute("arcmode") }
    func startPolylineSketch() { execute("polyline") }
    func startLightPlacement() { execute("light") }
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

    // ── 편집 / 선택 ──
    // 결과 코드 — 0 = CAD_OK, 되돌릴 것이 없으면 CAD_E_NOT_READY(음수)
    func undo() { guard isCreated else { return }; _ = CAD_Undo() }
    func redo() { guard isCreated else { return }; _ = CAD_Redo() }
    var canUndo: Bool { guard isCreated else { return false }; var can = false; return CAD_CanUndo(&can) == 0 && can }
    var canRedo: Bool { guard isCreated else { return false }; var can = false; return CAD_CanRedo(&can) == 0 && can }
    func selectAll()      { execute("selectall") }
    func clearSelection() { guard isCreated else { return }; _ = CAD_SetSelection(nil, 0, Int32(CAD_SELECT_REPLACE)) }   // REPLACE + 0개 = 비우기
    func deleteSelected() { execute("delete") }
    func clearAll()       { guard isCreated else { return }; _ = CAD_ClearAll() }
    var selectedCount: Int { isCreated ? max(0, Int(CAD_GetSelection(nil, 0))) : 0 }

    // ── 솔리드 편집 (인자만으로 결정되는 것들 — 클릭이 필요한 도구는 execute 로) ──
    // C API 는 대상 id 를 받는다 — 화면에서 고른 것을 모아 넘긴다(로프트는 고른 차례가 아니라 id 순)
    // CAD_GetSelection: 개수만 먼저(nil, 0) 묻고 그만큼 칸을 잡아 한 번에 받는다
    private var selectedIds: [UInt32] {
        let n = CAD_GetSelection(nil, 0)
        guard n > 0 else { return [] }
        var ids = [UInt32](repeating: 0, count: Int(n))
        let got = Int(max(0, min(n, CAD_GetSelection(&ids, UInt32(n)))))
        return ids.prefix(got).filter { $0 != 0 }
    }
    func booleanUnion() {
        guard isCreated else { return }
        let ids = selectedIds; var made: UInt32 = 0
        _ = CAD_BooleanUnion(ids, UInt32(ids.count), false, &made)
    }
    func booleanIntersection() {
        guard isCreated else { return }
        let ids = selectedIds; var made: UInt32 = 0
        _ = CAD_BooleanIntersection(ids, UInt32(ids.count), false, &made)
    }
    func loft() {
        guard isCreated else { return }
        let ids = selectedIds; var made: UInt32 = 0
        _ = CAD_Loft(ids, UInt32(ids.count), nil, &made)
    }
    func shell(thickness: Float = 0) {
        guard isCreated else { return }
        let ids = selectedIds; var made = [UInt32](repeating: 0, count: max(ids.count, 1))
        _ = CAD_Shell(ids, UInt32(ids.count), Double(thickness), &made, UInt32(made.count))
    }
    func edgeFillet(distance: Float = 0) {
        guard isCreated else { return }
        let ids = selectedIds; var made = [UInt32](repeating: 0, count: max(ids.count, 1))
        _ = CAD_EdgeFillet(ids, UInt32(ids.count), Double(distance), &made, UInt32(made.count))
    }
    func edgeChamfer(distance: Float = 0) {
        guard isCreated else { return }
        let ids = selectedIds; var made = [UInt32](repeating: 0, count: max(ids.count, 1))
        _ = CAD_EdgeChamfer(ids, UInt32(ids.count), Double(distance), &made, UInt32(made.count))
    }
    func explode(keepOriginal: Bool = false) {
        guard isCreated else { return }
        let ids = selectedIds
        let n = CAD_EntityExplode(ids, UInt32(ids.count), keepOriginal, nil, 0)   // 개수만 묻기(아무것도 안 바뀜)
        guard n > 0 else { return }
        var made = [UInt32](repeating: 0, count: Int(n))
        _ = CAD_EntityExplode(ids, UInt32(ids.count), keepOriginal, &made, UInt32(made.count))
    }

    /// NURBS 로 — 고른 것에 곡선(선·원·호·타원)이 있으면 기하 곡선 → NURBS → 스플라인 객체로 바꿔 끼우고(원본 지움),
    /// 곡선이 없으면 명령 tonurbs 로 SubD 객체를 NURBS B-Rep 솔리드로. 반환 = 바꾼 곡선 수(-1 = tonurbs 로 넘김).
    /// 폴리선은 여러 조각이라 NURBS 하나가 안 된다(CAD_GeCurveToNurbs 실패) — 그대로 둔다.
    @discardableResult
    func convertSelectionToNurbs() -> Int {
        guard isCreated else { return 0 }
        var converted = 0
        var sawCurve = false
        for id in selectedIds {
            var curve: UInt64 = 0
            guard CAD_CurveGetGeCurve(id, &curve) == 0 else { continue }   // 곡선이 아님 = CAD_E_WRONG_TYPE
            sawCurve = true
            var nurbs: UInt64 = 0
            var made: UInt32 = 0
            if CAD_GeCurveToNurbs(curve, &nurbs) == 0, CAD_CreateCurveFromGe(nurbs, nil, &made) == 0 {
                _ = CAD_DeleteObject(id)
                converted += 1
            }
            if nurbs != 0 { _ = CAD_GeCurveFree(nurbs) }
            _ = CAD_GeCurveFree(curve)
        }
        if !sawCurve { execute("tonurbs"); return -1 }
        return converted
    }

    /// 고른 메시 수리(같은 자리 정점 붙이기 → 퇴화·중복 제거 → 방향 통일 → 구멍 메움). 반환 = 고친 메시 수, 음수 = 이유 코드.
    func repairSelectedMeshes() -> Int32 {
        guard isCreated else { return 0 }
        // 하나라도 메시가 아니면(B-Rep 솔리드·곡선) 통째로 거부하므로 검사(CAD_CheckMesh)가 되는 것만 넘긴다
        let ids = selectedIds.filter { var info = CAD_MeshCheckInfo(); return CAD_CheckMesh($0, &info) == 0 }
        guard !ids.isEmpty else { return 0 }
        return CAD_RepairMeshes(ids, UInt32(ids.count), nil)   // nil = 구멍은 둘레 곡면을 따라 둥글게 메움
    }

    /// 분해도 — {"op":"solve"} 처럼 JSON 을 넘기고 결과 JSON 을 받는다(ok·error·steps…).
    @discardableResult
    func explodeView(_ argsJson: String) -> [String: Any] {
        guard isCreated else { return [:] }
        return readJson { CAD_ExplodeView(argsJson, $0, $1) }
    }

    // ── 도면층·선종류 (형식 메뉴) ──
    // 표는 CAD_GetLayersJson 한 번에 — revision 이 바뀌었을 때만 창을 다시 채운다.
    struct Layer {
        let id: UInt32
        let name: String
        let visible: Bool
        let locked: Bool
        let fixed: Bool          // 도면층 "0" — 색·켜기·잠금을 못 바꾼다
        let color: NSColor
        let linetypeId: UInt32
        let objectCount: Int
    }
    func layers() -> (revision: Int, layers: [Layer]) {
        guard isCreated else { return (0, []) }
        let json = readJson { CAD_GetLayersJson($0, $1) }
        let rows = (json["layers"] as? [[String: Any]] ?? []).map { l -> Layer in
            let c = (l["color"] as? [Double]) ?? [1, 1, 1]
            return Layer(id: UInt32(l["id"] as? Int ?? 0), name: l["name"] as? String ?? "",
                         visible: l["visible"] as? Bool ?? true, locked: l["locked"] as? Bool ?? false,
                         fixed: l["fixed"] as? Bool ?? false,
                         color: NSColor(srgbRed: c[0], green: c[1], blue: c[2], alpha: 1),
                         linetypeId: UInt32(l["linetypeId"] as? Int ?? 0), objectCount: l["objectCount"] as? Int ?? 0)
        }
        return (json["revision"] as? Int ?? 0, rows)
    }
    /// 새 도면층. 반환 = id, 실패(같은 이름 등) nil — 이유는 lastError.
    func createLayer(_ name: String) -> UInt32? {
        guard isCreated else { return nil }
        var id: UInt32 = 0
        return CAD_CreateLayer(name, &id) == 0 ? id : nil
    }
    func setLayerVisible(_ id: UInt32, _ on: Bool) { guard isCreated else { return }; _ = CAD_SetLayerVisible(id, on) }
    func setLayerLocked(_ id: UInt32, _ on: Bool)  { guard isCreated else { return }; _ = CAD_SetLayerLocked(id, on) }
    func setLayerColor(_ id: UInt32, _ color: NSColor) {
        guard isCreated, let c = color.usingColorSpace(.sRGB) else { return }
        _ = CAD_SetLayerColor(id, CAD_Color(r: Double(c.redComponent), g: Double(c.greenComponent), b: Double(c.blueComponent)))
    }
    func setLayerLinetype(_ id: UInt32, _ linetypeId: UInt32) { guard isCreated else { return }; _ = CAD_SetLayerLinetype(id, linetypeId) }
    /// 고른 것을 그 도면층으로 — 색도 '도면층을 따름'으로(새로 그린 객체는 자기 색이라 도면층 색이 안 보인다).
    /// 반환 = 바뀐 수(잠긴 도면층 것은 건너뜀).
    func assignSelectionToLayer(_ id: UInt32) -> Int {
        guard isCreated else { return 0 }
        var moved: UInt32 = 0, recolored: UInt32 = 0
        guard CAD_AssignSelectedToLayer(id, &moved) == 0 else { return 0 }
        _ = CAD_SetSelectedColorByLayer(true, &recolored)
        return Int(max(moved, recolored))
    }
    /// 선종류 표(0 = Continuous, 1..8 표준, 100~ 사용자) — (id, 이름).
    func linetypes() -> [(id: UInt32, name: String)] {
        guard isCreated else { return [] }
        let n = CAD_GetLinetypeIds(nil, 0)
        guard n > 0 else { return [] }
        var ids = [UInt32](repeating: 0, count: Int(n))
        _ = CAD_GetLinetypeIds(&ids, UInt32(n))
        return ids.map { id in (id, readString { CAD_GetLinetypeName(id, $0, UInt32($1)) }) }
    }
    var linetypeScale: Double {
        get { var s = 1.0; if isCreated { _ = CAD_GetLinetypeScale(&s) }; return s }
        set { if isCreated { _ = CAD_SetLinetypeScale(newValue) } }
    }

    // ── 문자 글꼴 ──
    // 문자 객체의 속성 font — TrueType 가족 이름(엔진이 OS 글꼴 폴더에서 찾는다, 없으면 비슷한 글꼴·기본 글꼴) 또는 SHX 파일 이름.
    /// 고른 것 중 문자의 글꼴을 바꾼다. 반환 = 바꾼 수.
    func setSelectedTextFont(_ family: String) -> Int {
        guard isCreated else { return 0 }
        guard let data = try? JSONEncoder().encode(family), let quoted = String(data: data, encoding: .utf8) else { return 0 }   // "\"Arial\""
        return selectedIds.filter { objectKind($0) == "text" && CAD_SetObjectProperty($0, "font", quoted) == 0 }.count
    }
    /// 고른 첫 문자의 글꼴(없으면 빈 글).
    var selectedTextFont: String {
        guard let id = selectedIds.first(where: { objectKind($0) == "text" }) else { return "" }
        let raw = readString { CAD_GetObjectProperty(id, "font", $0, UInt32($1)) }   // JSON 글 — "\"Arial\""
        return (try? JSONSerialization.jsonObject(with: Data(raw.utf8), options: .fragmentsAllowed)) as? String ?? ""
    }
    private func objectKind(_ id: UInt32) -> String {
        readJson { CAD_GetObjectJson(id, $0, $1) }["kind"] as? String ?? ""
    }

    // ── 블록·외부 참조 (삽입 메뉴) ──
    /// 고른 것으로 블록 정의 + 그 자리에 INSERT — 기준점 = 고른 것 전체 상자의 왼쪽 아래. 반환 = INSERT id, 실패 nil(이유 lastError).
    func createBlock(named name: String) -> UInt32? {
        guard isCreated else { return nil }
        let ids = selectedIds
        guard !ids.isEmpty else { return nil }
        var lo = CAD_GeVec3(x: .infinity, y: .infinity, z: .infinity)
        for id in ids {
            var a = CAD_GeVec3(), b = CAD_GeVec3()
            if CAD_GetBoundsWorld(id, &a, &b) == 0 { lo = CAD_GeVec3(x: min(lo.x, a.x), y: min(lo.y, a.y), z: min(lo.z, a.z)) }
        }
        if !lo.x.isFinite { lo = CAD_GeVec3() }
        var insert: UInt32 = 0
        return CAD_CreateBlock(name, ids, UInt32(ids.count), lo, &insert) == 0 ? insert : nil
    }
    /// 블록 정의 이름들(CAD_GetBlocksJson 의 blocks[].name).
    func blockNames() -> [String] {
        guard isCreated else { return [] }
        return (readJson { CAD_GetBlocksJson($0, $1) }["blocks"] as? [[String: Any]] ?? []).compactMap { $0["name"] as? String }
    }
    /// 장면에 있는 그 블록의 참조(INSERT) 하나 — 객체 JSON 의 "block" 이 정의 이름.
    func blockReference(named name: String) -> UInt32? {
        guard isCreated else { return nil }
        let n = CAD_QueryObjects(#"{"kind":"insert"}"#, nil, 0)
        guard n > 0 else { return nil }
        var ids = [UInt32](repeating: 0, count: Int(n))
        _ = CAD_QueryObjects(#"{"kind":"insert"}"#, &ids, UInt32(n))
        return ids.first { id in readJson { CAD_GetObjectJson(id, $0, $1) }["block"] as? String == name }
    }
    /// 외부 참조 — 블록 정의 표에서 "xref" 가 있는 것(DXF·DWG 를 열면 따라 들어온다).
    struct Xref { let name: String; let path: String; let found: Bool; let references: Int }
    func xrefs() -> [Xref] {
        guard isCreated else { return [] }
        let blocks = readJson { CAD_GetBlocksJson($0, $1) }["blocks"] as? [[String: Any]] ?? []
        return blocks.compactMap { b in
            guard let path = b["xref"] as? String, !path.isEmpty else { return nil }
            return Xref(name: b["name"] as? String ?? "", path: path,
                        found: !((b["xrefFound"] as? String) ?? "").isEmpty, references: b["references"] as? Int ?? 0)
        }
    }
    enum XrefAction { case reload, bind, detach }
    func xref(_ action: XrefAction, _ name: String) -> Bool {
        guard isCreated else { return false }
        switch action {
        case .reload: return CAD_XrefReload(name) == 0
        case .bind:   return CAD_XrefBind(name) == 0
        case .detach: return CAD_XrefDetach(name) == 0
        }
    }

    // ── 뷰 ──
    // viewType: 0=Front 1=Top 2=Right 3=Isometric 4=Left 5=Bottom 6=Back
    enum ViewType: Int32 { case front = 0, top, right, isometric, left, bottom, back }
    func zoomExtents()   { guard isCreated else { return }; CAD_ZoomExtents() }
    func focusSelected() { guard isCreated else { return }; CAD_FocusSelected() }
    func setView(_ view: ViewType) { guard isCreated else { return }; CAD_SetView(view.rawValue) }
    func toggleProjection() {
        guard isCreated else { return }
        var ortho = false
        if CAD_GetProjection(&ortho) == 0 { _ = CAD_SetProjection(!ortho) }   // 0 = CAD_OK
    }
    func setProjection(ortho: Bool) { guard isCreated else { return }; CAD_SetProjection(ortho) }
    // layout: 0=Single 1=Dual 2=Triple 3=Quad
    func setViewportLayout(_ layout: Int32) { guard isCreated else { return }; CAD_SetViewportLayout(layout) }
    var viewportLayout: Int32 { isCreated ? CAD_GetViewportLayout() : 0 }
    // style: 0=Shaded 1=ShadedEdge 2=Wireframe 3=WireframeEdge 4=HiddenLine
    func setVisualStyle(_ style: Int32) { guard isCreated else { return }; CAD_SetVisualStyle(style) }
    func setGridEnabled(_ enabled: Bool) { guard isCreated else { return }; CAD_SetGridEnabled(enabled) }

    // ── 문서 / 파일 ──
    // 확장자로 포맷이 갈린다. 대화상자는 호스트(NSOpenPanel/NSSavePanel)가 띄운다.
    // 결과 코드(CAD_Status) — 0 = CAD_OK, 음수 = 실패(이유 글은 lastError)
    /// 새 빈 문서(탭). 반환 = 문서 인덱스, 실패 -1.
    @discardableResult
    func newDocument(title: String = "제목 없음") -> Int32 {
        guard isCreated else { return -1 }
        var index: Int32 = -1
        return CAD_NewDocument(title, &index) == 0 ? index : -1
    }
    /// 새 탭으로 연다. 반환 = 문서 인덱스, 실패 -1.
    @discardableResult
    func openDocument(path: String) -> Int32 {
        guard isCreated else { return -1 }
        var index: Int32 = -1
        return CAD_OpenDocument(path, &index) == 0 ? index : -1
    }
    /// 현재 문서에 **추가**한다(가져오기).
    @discardableResult
    func openFile(path: String) -> Bool {
        guard isCreated else { return false }
        return CAD_OpenFile(path) == 0
    }
    /// 확장자로 포맷이 정해진다 — 내보내기(.stl .dxf .obj .glb)도 이것 하나(selectedOnly = 선택만).
    @discardableResult
    func saveAs(path: String, selectedOnly: Bool) -> Bool {
        guard isCreated else { return false }
        return CAD_SaveAs(path, selectedOnly) == 0
    }
    var activeDocumentTitle: String {
        guard isCreated else { return "" }
        let index = CAD_GetActiveDocument()
        return readString { CAD_GetDocumentTitle(index, $0, UInt32($1)) }   // 칸 = uint32
    }
    var isActiveDocumentDirty: Bool {
        guard isCreated else { return false }
        var dirty = false
        return CAD_IsDocumentDirty(CAD_GetActiveDocument(), &dirty) == 0 && dirty
    }

    // ── 상태 문구 ──
    /// 상시 안내(지금 뭘 해야 하는지). onPrompt 콜백과 같은 값 — 초기 표시용.
    var statusMessage: String {
        guard isCreated else { return "" }
        return readString { CAD_GetPrompt($0, UInt32($1)) }   // 칸 = uint32
    }
    /// 일회성 안내(방금 왜 안 됐는지). 없으면 빈 문자열 — 매 틱 폴링해도 싸다.
    var transientMessage: String {
        guard isCreated else { return "" }
        return readString { CAD_GetTransientMessage($0, UInt32($1)) }
    }
    /// 직전 실패 이유(열기·저장 등 결과 코드가 음수였을 때). 없으면 빈 문자열.
    var lastError: String {
        guard isCreated else { return "" }
        return readString { CAD_GetLastError($0, UInt32($1)) }
    }

    // ── 플러그인이 등록한 UI 항목 ──
    // 플러그인은 (이름, 위치, 명령)만 올리고 그리는 건 호스트 몫이다. 메뉴·리본·툴바를
    // 만들 때 이 목록을 읽어 자기 위젯으로 붙이면 플러그인이 임베드 앱에서도 산다.
    struct UiItem {
        enum Kind: Int32 { case menuItem = 0, separator, toolButton, ribbonButton, panel }
        let id: UInt32
        let kind: Kind
        let path: String      // "건축" 또는 "건축/벽체" — '/' 로 위치를 나눈다
        let title: String
        let command: String   // 누르면 execute 할 명령 (구분선·패널은 빈 문자열)
        let icon: String      // 짧은 글자/이모지, 없으면 빈 문자열
    }
    func uiItems() -> [UiItem] {
        guard isCreated else { return [] }
        let count = max(0, CAD_GetUiItemCount())   // 음수 = 이유 코드
        return (0..<UInt32(count)).compactMap { i in
            var rawKind: Int32 = -1
            var id: UInt32 = 0
            guard CAD_GetUiItemKind(i, &rawKind) == 0,             // 0 = CAD_OK
                  CAD_GetUiItemId(i, &id) == 0,
                  let kind = UiItem.Kind(rawValue: rawKind) else { return nil }
            return UiItem(
                id: id,
                kind: kind,
                path: readString { CAD_GetUiItemPath(i, $0, UInt32($1)) },   // 칸 = uint32
                title: readString { CAD_GetUiItemTitle(i, $0, UInt32($1)) },
                command: readString { CAD_GetUiItemCommand(i, $0, UInt32($1)) },
                icon: readString { CAD_GetUiItemIcon(i, $0, UInt32($1)) })
        }
    }
    /// 플러그인이 등록한 콘솔 명령 (이름, 표시 이름).
    func registeredCommands() -> [(name: String, title: String)] {
        guard isCreated else { return [] }
        let count = max(0, CAD_GetRegisteredCommandCount())   // 음수 = 이유 코드
        return (0..<UInt32(count)).map { i in
            (readString { CAD_GetRegisteredCommandName(i, $0, UInt32($1)) },
             readString { CAD_GetRegisteredCommandTitle(i, $0, UInt32($1)) })
        }
    }
    /// 폴더의 플러그인을 올린다. 반환 = 새로 붙인 개수(음수 = 이유 코드 — lastError).
    func loadPlugins(directory: String) -> Int32 {
        guard isCreated else { return 0 }
        return CAD_LoadPlugins(directory)
    }

    @MainActor
    func onDocumentDirty(_ handler: ((Bool) -> Void)?) {
        LotCADEngineCallbacks.documentDirty = handler
        refreshEventListener()
    }

    /// C API 의 "(buf, bufLen) → 길이" 문자열 조회 관례를 Swift String 으로.
    /// 엔진 문구는 전부 짧아서 고정 버퍼면 충분하다(넘치면 엔진이 잘라 준다).
    private func readString(_ read: (UnsafeMutablePointer<CChar>?, Int32) -> Int32) -> String {
        var buf = [CChar](repeating: 0, count: 1024)
        let n = buf.withUnsafeMutableBufferPointer { read($0.baseAddress, Int32($0.count)) }
        guard n > 0 else { return "" }
        // 널 문자 앞까지만 UTF-8 로 (배열을 받는 String(cString:) 은 사용 중단)
        return String(decoding: buf.prefix { $0 != 0 }.map { UInt8(bitPattern: $0) }, as: UTF8.self)
    }

    /// 긴 JSON 출력(도면층·블록 표 등) — 길이를 먼저 묻고(nil, 0) 그만큼 칸을 잡아 한 번 더. 실패·빈 글 = [:].
    private func readJson(_ read: (UnsafeMutablePointer<CChar>?, UInt32) -> Int32) -> [String: Any] {
        let n = read(nil, 0)
        guard n > 0 else { return [:] }
        var buf = [CChar](repeating: 0, count: Int(n) + 1)
        _ = buf.withUnsafeMutableBufferPointer { read($0.baseAddress, UInt32($0.count)) }
        let data = Data(buf.prefix(Int(n)).map { UInt8(bitPattern: $0) })
        return (try? JSONSerialization.jsonObject(with: data)) as? [String: Any] ?? [:]
    }

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

    func keyDown(_ key: Int32, modifiers: Int32) {
        guard isCreated else { return }
        CAD_OnKeyDown(key, modifiers)
    }

    func keyUp(_ key: Int32, modifiers: Int32) {
        guard isCreated else { return }
        CAD_OnKeyUp(key, modifiers)
    }

    func shutdown() {
        for id in demoObjectIds.reversed() {
            CAD_DeleteObject(id)
        }
        demoObjectIds.removeAll()
        if isCreated {
            _ = CAD_DestroyEngine()   // 구독도 엔진과 같이 사라진다
            eventListenerHandle = 0
            isCreated = false
        }
    }

    private func trackDemoObject(_ id: UInt32) {
        if id != 0 {
            demoObjectIds.append(id)
        }
    }
}

/// C 콜백이 꺼내 쓸 보관소.
///
/// C 함수 포인터는 문맥(캡처)을 가질 수 없어서 Swift 클로저를 그대로 못 넘긴다.
/// 여기 담아 두고 C 쪽 함수에서 꺼내 부른다. 호출은 CAD_Tick 안 = 메인 스레드다.
///
/// `@MainActor` 인 이유: Swift 6 는 nonisolated 한 static var 를 "동시성 안전하지 않음" 으로
/// 막는다(MutableGlobalVariable). 실제로 여기 접근하는 곳은 전부 메인 스레드
/// (설정은 UI, 호출은 CAD_Tick)이라 액터를 명시하는 게 사실에 맞고 검사도 통과한다.
@MainActor
enum LotCADEngineCallbacks {
    static var selectionChanged: (() -> Void)?
    static var objectCreated: ((UInt32) -> Void)?
    static var objectDeleted: ((UInt32) -> Void)?
    static var prompt: ((String) -> Void)?
    static var documentDirty: ((Bool) -> Void)?

    /// CAD_AddEventListener 콜백 — kind 로 갈라 위 처리기를 부른다(문서 변경 id = dirty ? 1 : 0, 선택 변경 id = 0).
    static func dispatch(kind: Int32, id: UInt32) {
        switch kind {
        case Int32(CAD_EVENT_OBJECT_CREATED):    objectCreated?(id)
        case Int32(CAD_EVENT_OBJECT_DELETED):    objectDeleted?(id)
        case Int32(CAD_EVENT_SELECTION_CHANGED): selectionChanged?()
        case Int32(CAD_EVENT_DOCUMENT_DIRTY):    documentDirty?(id != 0)
        default: break
        }
    }
}
