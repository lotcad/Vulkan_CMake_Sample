import CLotCAD
import Foundation

@discardableResult
func require(_ condition: Bool, _ message: String) -> Bool {
    if !condition {
        fputs("[swift_api_test] \(message)\n", stderr)
    }
    return condition
}

let sourceFile = URL(fileURLWithPath: #filePath)
let projectRoot = sourceFile
    .deletingLastPathComponent() // LotCADSwiftApiTest
    .deletingLastPathComponent() // Sources
    .deletingLastPathComponent() // swift_api_test
    .deletingLastPathComponent() // samples
    .deletingLastPathComponent() // 3dEngine
// 런타임 에셋(models/ textures/ fonts/)은 sdk/ 바로 아래 — 라이브러리와 같은 층.
let runtimeDirectory = projectRoot.appendingPathComponent("sdk")

guard CAD_SetRuntimeAssetPath(runtimeDirectory.path) else {
    fputs("[swift_api_test] failed to set runtime asset path to \(runtimeDirectory.path)\n", stderr)
    exit(1)
}

print("[swift_api_test] runtime asset path: \(runtimeDirectory.path)")
print("[swift_api_test] create engine")

guard CAD_CreateEngine() else {
    fputs("[swift_api_test] CAD_CreateEngine failed\n", stderr)
    exit(1)
}

let boxId = CAD_CreateBox(0.0, 0.0, 1.0, 0.5, 0.5, 0.5)
guard boxId != 0 else {
    fputs("[swift_api_test] CAD_CreateBox failed\n", stderr)
    CAD_DestroyEngine()
    exit(1)
}

// 결과 코드(CAD_Status) — 0 = 성공, 음수 = 이유 코드(이유 글은 CAD_GetLastError)
CAD_SetPosition(boxId, CAD_GeVec3(x: 1.0, y: 0.0, z: 1.5))
CAD_SetScale(boxId, CAD_GeVec3(x: 0.8, y: 0.8, z: 0.8))
CAD_SetRotationAxisAngle(boxId, CAD_GeVec3(x: 0.0, y: 0.0, z: 1.0), 0.7853982)
CAD_SelectObject(boxId, false)
CAD_RequestZoomExtents()

var p = CAD_GeVec3()
if CAD_GetPosition(boxId, &p) == 0 {
    print("[swift_api_test] box position: \(p.x), \(p.y), \(p.z)")
}

print("[swift_api_test] object count: \(CAD_GetObjectCount())")
print("[swift_api_test] selected count: \(CAD_GetSelectedCount())")
print("[swift_api_test] close the GLFW window to finish")

while !CAD_ShouldClose() {
    if !CAD_Tick() {
        break
    }
    Thread.sleep(forTimeInterval: 1.0 / 60.0)
}

CAD_DeleteObject(boxId)
CAD_DestroyEngine()

print("[swift_api_test] done")
