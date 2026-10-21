# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""구조체와 콜백 형식 — 여러 영역이 같이 쓴다."""
from __future__ import annotations

import ctypes as _c
__all__ = ['CAD_OverlayFrameInfo', 'CAD_OverlayRenderFn', 'CAD_OverlayPointerInfo', 'CAD_OverlayInputFn', 'CAD_CommandFn', 'CAD_EventFn', 'CAD_FloorplanOpeningDesc', 'CAD_SketchConstraintInfo', 'CAD_BRepInfo', 'CAD_BRepParameters', 'CAD_BRepFaceInfo', 'CAD_BRepCutInfo', 'CAD_BooleanCylinderCutInfo', 'CAD_InterferenceInfo', 'CAD_MeshCheckInfo']


class CAD_OverlayFrameInfo(_c.Structure):
    _fields_ = [
        ("structSize", _c.c_uint32),
        ("physicalDevice", _c.c_uint64),
        ("device", _c.c_uint64),
        ("graphicsQueue", _c.c_uint64),
        ("renderPass", _c.c_uint64),
        ("commandBuffer", _c.c_uint64),
        ("graphicsQueueFamily", _c.c_uint32),
        ("frameIndex", _c.c_uint32),
        ("frameCount", _c.c_uint32),
        ("framebufferWidth", _c.c_uint32),
        ("framebufferHeight", _c.c_uint32),
        ("windowWidth", _c.c_int),
        ("windowHeight", _c.c_int),
        ("dpiScale", _c.c_float),
        ("pointerX", _c.c_double),
        ("pointerY", _c.c_double),
        ("pointerButtons", _c.c_uint32),
        ("modifiers", _c.c_int),
        ("sampleCount", _c.c_uint32),
    ]

CAD_OverlayRenderFn = _c.CFUNCTYPE(_c.c_uint32, _c.POINTER(CAD_OverlayFrameInfo), _c.c_void_p)

class CAD_OverlayPointerInfo(_c.Structure):
    _fields_ = [
        ("structSize", _c.c_uint32),
        ("windowWidth", _c.c_int),
        ("windowHeight", _c.c_int),
        ("x", _c.c_double),
        ("y", _c.c_double),
        ("buttons", _c.c_uint32),
        ("modifiers", _c.c_int),
    ]

CAD_OverlayInputFn = _c.CFUNCTYPE(_c.c_uint32, _c.POINTER(CAD_OverlayPointerInfo), _c.c_void_p)

CAD_CommandFn = _c.CFUNCTYPE(None, _c.c_void_p)

CAD_EventFn = _c.CFUNCTYPE(None, _c.c_int, _c.c_uint32, _c.c_void_p)

class CAD_FloorplanOpeningDesc(_c.Structure):
    _fields_ = [
        ("type", _c.c_int),
        ("roomAIndex", _c.c_uint32),
        ("roomBIndex", _c.c_int32),
        ("side", _c.c_int),
        ("width", _c.c_float),
        ("height", _c.c_float),
        ("sillHeight", _c.c_float),
        ("alignment", _c.c_int),
        ("offset", _c.c_float),
    ]

class CAD_SketchConstraintInfo(_c.Structure):
    _fields_ = [
        ("id", _c.c_uint32),
        ("type", _c.c_int),
        ("entityA", _c.c_uint32),
        ("pointA", _c.c_int),
        ("entityB", _c.c_uint32),
        ("pointB", _c.c_int),
        ("value", _c.c_float),
        ("driving", _c.c_bool),
        ("enabled", _c.c_bool),
    ]

class CAD_BRepInfo(_c.Structure):
    _fields_ = [
        ("featureType", _c.c_int32),
        ("vertexCount", _c.c_uint32),
        ("edgeCount", _c.c_uint32),
        ("faceCount", _c.c_uint32),
        ("volume", _c.c_double),
        ("surfaceArea", _c.c_double),
    ]

class CAD_BRepParameters(_c.Structure):
    _fields_ = [
        ("featureType", _c.c_int32),
        ("dimensionsX", _c.c_float),
        ("dimensionsY", _c.c_float),
        ("dimensionsZ", _c.c_float),
        ("radius", _c.c_float),
        ("height", _c.c_float),
        ("directionX", _c.c_float),
        ("directionY", _c.c_float),
        ("directionZ", _c.c_float),
    ]

class CAD_BRepFaceInfo(_c.Structure):
    _fields_ = [
        ("faceId", _c.c_uint32),
        ("surfaceType", _c.c_int32),
        ("originX", _c.c_float),
        ("originY", _c.c_float),
        ("originZ", _c.c_float),
        ("normalX", _c.c_float),
        ("normalY", _c.c_float),
        ("normalZ", _c.c_float),
    ]

class CAD_BRepCutInfo(_c.Structure):
    _fields_ = [
        ("cutIndex", _c.c_uint32),
        ("pointCount", _c.c_uint32),
        ("depth", _c.c_float),
        ("throughAll", _c.c_bool),
    ]

class CAD_BooleanCylinderCutInfo(_c.Structure):
    _fields_ = [
        ("cutIndex", _c.c_uint32),
        ("centerX", _c.c_float),
        ("centerY", _c.c_float),
        ("centerZ", _c.c_float),
        ("axisX", _c.c_float),
        ("axisY", _c.c_float),
        ("axisZ", _c.c_float),
        ("radius", _c.c_float),
        ("height", _c.c_float),
    ]

class CAD_InterferenceInfo(_c.Structure):
    _fields_ = [
        ("objectA", _c.c_uint32),
        ("objectB", _c.c_uint32),
        ("volume", _c.c_double),
        ("resultId", _c.c_uint32),
    ]

class CAD_MeshCheckInfo(_c.Structure):
    _fields_ = [
        ("triangles", _c.c_uint32),
        ("vertices", _c.c_uint32),
        ("degenerate", _c.c_uint32),
        ("duplicates", _c.c_uint32),
        ("openEdges", _c.c_uint32),
        ("nonManifoldEdges", _c.c_uint32),
        ("flippedEdges", _c.c_uint32),
        ("holes", _c.c_uint32),
        ("components", _c.c_uint32),
        ("closed", _c.c_bool),
        ("ok", _c.c_bool),
        ("volume", _c.c_double),
        ("area", _c.c_double),
    ]
