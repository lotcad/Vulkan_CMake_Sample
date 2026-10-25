# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""구조체와 콜백 형식 — 여러 영역이 같이 쓴다."""
from __future__ import annotations

import ctypes as _c
__all__ = ['CAD_CreateOptions', 'CAD_Color', 'CAD_GeVec3', 'CAD_GePlane', 'CAD_GeMatrix', 'CAD_GeArc', 'CAD_GeEllipse', 'CAD_GeIntersection', 'CAD_PostFn', 'CAD_OverlayFrameInfo', 'CAD_OverlayRenderFn', 'CAD_OverlayPointerInfo', 'CAD_OverlayInputFn', 'CAD_OsnapPoint', 'CAD_OsnapOptions', 'CAD_CommandFn', 'CAD_EdInputResult', 'CAD_EdInputFn', 'CAD_EdInputOptions', 'CAD_EdSelectOptions', 'CAD_EdCommandState', 'CAD_EventFn', 'CAD_SketchConstraintInfo', 'CAD_BRepInfo', 'CAD_BRepParameters', 'CAD_BRepFaceInfo', 'CAD_BRepCutInfo', 'CAD_BooleanCylinderCutInfo', 'CAD_InterferenceInfo', 'CAD_MeshCheckInfo', 'CAD_SimOptions', 'CAD_SimCondition', 'CAD_SimFace', 'CAD_SimState', 'CAD_SimSummary', 'CAD_SimConvergence', 'CAD_SimRunOptions', 'CAD_WindOptions', 'CAD_WindState', 'CAD_WindViewOptions', 'CAD_WindPointValue', 'CAD_WindSurfacePoint', 'CAD_WaterOptions', 'CAD_WaterState', 'CAD_WaterFloater', 'CAD_WaterPointValue', 'CAD_ClothOptions', 'CAD_ClothState', 'CAD_FloorplanOpeningDesc']


class CAD_CreateOptions(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("propsFrom", _c.c_uint32),
    ]

class CAD_Color(_c.Structure):
    _fields_ = [
        ("r", _c.c_double),
        ("g", _c.c_double),
        ("b", _c.c_double),
    ]

class CAD_GeVec3(_c.Structure):
    _fields_ = [
        ("x", _c.c_double),
        ("y", _c.c_double),
        ("z", _c.c_double),
    ]

class CAD_GePlane(_c.Structure):
    _fields_ = [
        ("ox", _c.c_double),
        ("oy", _c.c_double),
        ("oz", _c.c_double),
        ("nx", _c.c_double),
        ("ny", _c.c_double),
        ("nz", _c.c_double),
    ]

class CAD_GeMatrix(_c.Structure):
    _fields_ = [
        ("m", _c.c_double * 16),
    ]

class CAD_GeArc(_c.Structure):
    _fields_ = [
        ("cx", _c.c_double),
        ("cy", _c.c_double),
        ("cz", _c.c_double),
        ("nx", _c.c_double),
        ("ny", _c.c_double),
        ("nz", _c.c_double),
        ("rx", _c.c_double),
        ("ry", _c.c_double),
        ("rz", _c.c_double),
        ("radius", _c.c_double),
        ("startAngle", _c.c_double),
        ("endAngle", _c.c_double),
    ]

class CAD_GeEllipse(_c.Structure):
    _fields_ = [
        ("cx", _c.c_double),
        ("cy", _c.c_double),
        ("cz", _c.c_double),
        ("nx", _c.c_double),
        ("ny", _c.c_double),
        ("nz", _c.c_double),
        ("mx", _c.c_double),
        ("my", _c.c_double),
        ("mz", _c.c_double),
        ("majorRadius", _c.c_double),
        ("minorRadius", _c.c_double),
        ("startAngle", _c.c_double),
        ("endAngle", _c.c_double),
    ]

class CAD_GeIntersection(_c.Structure):
    _fields_ = [
        ("x", _c.c_double),
        ("y", _c.c_double),
        ("z", _c.c_double),
        ("x2", _c.c_double),
        ("y2", _c.c_double),
        ("z2", _c.c_double),
        ("param1", _c.c_double),
        ("param2", _c.c_double),
        ("overlap", _c.c_int),
        ("endX", _c.c_double),
        ("endY", _c.c_double),
        ("endZ", _c.c_double),
        ("endParam1", _c.c_double),
        ("endParam2", _c.c_double),
    ]

CAD_PostFn = _c.CFUNCTYPE(None, _c.c_void_p)

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

class CAD_OsnapPoint(_c.Structure):
    _fields_ = [
        ("x", _c.c_double),
        ("y", _c.c_double),
        ("z", _c.c_double),
        ("mode", _c.c_uint32),
        ("id", _c.c_uint32),
    ]

class CAD_OsnapOptions(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("hasPickPoint", _c.c_bool),
        ("hasLastPoint", _c.c_bool),
        ("pickX", _c.c_double),
        ("pickY", _c.c_double),
        ("pickZ", _c.c_double),
        ("lastX", _c.c_double),
        ("lastY", _c.c_double),
        ("lastZ", _c.c_double),
    ]

CAD_CommandFn = _c.CFUNCTYPE(None, _c.c_void_p)

class CAD_EdInputResult(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("kind", _c.c_int32),
        ("status", _c.c_int32),
        ("point", CAD_GeVec3),
        ("value", _c.c_double),
        ("id", _c.c_uint32),
        ("keywordIndex", _c.c_int32),
        ("idCount", _c.c_int32),
        ("textLength", _c.c_int32),
    ]

CAD_EdInputFn = _c.CFUNCTYPE(None, _c.POINTER(CAD_EdInputResult), _c.c_void_p)

class CAD_EdInputOptions(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("flags", _c.c_uint32),
        ("keywords", _c.c_char_p),
        ("hasBase", _c.c_bool),
        ("base", CAD_GeVec3),
        ("hasDefault", _c.c_bool),
        ("defaultValue", _c.c_double),
        ("defaultPoint", CAD_GeVec3),
        ("defaultText", _c.c_char_p),
        ("onDone", CAD_EdInputFn),
        ("user", _c.c_void_p),
    ]
    _text_fields_ = ('keywords', 'defaultText')
    _callback_fields_ = {"onDone": (CAD_EdInputFn, ())}

    def __init__(self, *args, **kw):
        super().__init__(*args, **{k: self._convert(k, v) for k, v in kw.items()})

    def __setattr__(self, key, value):
        super().__setattr__(key, self._convert(key, value))

    @classmethod
    def _convert(cls, key, value):
        if key in cls._text_fields_ and isinstance(value, str):
            return value.encode("utf-8")
        if key in cls._callback_fields_ and callable(value) and not isinstance(value, _c._CFuncPtr):
            from . import _native as _n
            cftype, text_args = cls._callback_fields_[key]
            return _n.callback_once(cftype, value, text_args)
        return value

class CAD_EdSelectOptions(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("crossing", _c.c_bool),
    ]

class CAD_EdCommandState(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("commandActive", _c.c_bool),
        ("inputKind", _c.c_int32),
    ]

CAD_EventFn = _c.CFUNCTYPE(None, _c.c_int, _c.c_uint32, _c.c_void_p)

class CAD_SketchConstraintInfo(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("id", _c.c_uint32),
        ("type", _c.c_int32),
        ("entityA", _c.c_uint32),
        ("pointA", _c.c_int32),
        ("entityB", _c.c_uint32),
        ("pointB", _c.c_int32),
        ("value", _c.c_double),
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

class CAD_SimOptions(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("type", _c.c_int32),
        ("material", _c.c_int32),
        ("youngsModulus", _c.c_double),
        ("poissonRatio", _c.c_double),
        ("yieldStrength", _c.c_double),
        ("density", _c.c_double),
        ("conductivity", _c.c_double),
        ("expansion", _c.c_double),
        ("meshQuality", _c.c_int32),
        ("elementSize", _c.c_double),
        ("units", _c.c_int32),
        ("modeCount", _c.c_int32),
        ("thermalLoad", _c.c_bool),
        ("referenceTemperature", _c.c_double),
        ("windLoad", _c.c_bool),
        ("windSpeed", _c.c_double),
    ]

class CAD_SimCondition(_c.Structure):
    _fields_ = [
        ("face", _c.c_int32),
        ("kind", _c.c_int32),
        ("fixAxes", _c.c_uint32),
        ("fx", _c.c_double),
        ("fy", _c.c_double),
        ("fz", _c.c_double),
        ("value", _c.c_double),
        ("ambient", _c.c_double),
    ]

class CAD_SimFace(_c.Structure):
    _fields_ = [
        ("area", _c.c_double),
        ("cx", _c.c_double),
        ("cy", _c.c_double),
        ("cz", _c.c_double),
        ("nx", _c.c_double),
        ("ny", _c.c_double),
        ("nz", _c.c_double),
    ]

class CAD_SimState(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("open", _c.c_bool),
        ("target", _c.c_uint32),
        ("faceCount", _c.c_int32),
        ("conditionCount", _c.c_int32),
        ("busy", _c.c_bool),
        ("stage", _c.c_int32),
        ("fraction", _c.c_double),
        ("hasResult", _c.c_bool),
        ("resultType", _c.c_int32),
        ("lastRunFailed", _c.c_bool),
    ]

class CAD_SimSummary(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("type", _c.c_int32),
        ("nodeCount", _c.c_int32),
        ("elementCount", _c.c_int32),
        ("boundaryTriangleCount", _c.c_int32),
        ("elementSize", _c.c_double),
        ("minDihedralDeg", _c.c_double),
        ("meshSeconds", _c.c_double),
        ("solveSeconds", _c.c_double),
        ("maxVonMises", _c.c_double),
        ("maxDisplacement", _c.c_double),
        ("safetyFactor", _c.c_double),
        ("maxVonMisesNode", _c.c_int32),
        ("maxDisplacementNode", _c.c_int32),
        ("appliedX", _c.c_double),
        ("appliedY", _c.c_double),
        ("appliedZ", _c.c_double),
        ("reactionX", _c.c_double),
        ("reactionY", _c.c_double),
        ("reactionZ", _c.c_double),
        ("strainEnergy", _c.c_double),
        ("minTemperature", _c.c_double),
        ("maxTemperature", _c.c_double),
        ("maxHeatFlux", _c.c_double),
        ("heatIn", _c.c_double),
        ("heatFixed", _c.c_double),
        ("heatConvection", _c.c_double),
        ("modeCount", _c.c_int32),
        ("windForceX", _c.c_double),
        ("windForceY", _c.c_double),
        ("windForceZ", _c.c_double),
        ("windCpMin", _c.c_double),
        ("windCpMax", _c.c_double),
        ("convergenceCount", _c.c_int32),
        ("coarseElementSize", _c.c_double),
        ("coarseElementCount", _c.c_int32),
    ]

class CAD_SimConvergence(_c.Structure):
    _fields_ = [
        ("metric", _c.c_int32),
        ("coarse", _c.c_double),
        ("fine", _c.c_double),
        ("change", _c.c_double),
    ]

class CAD_SimRunOptions(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("checkConvergence", _c.c_bool),
    ]

class CAD_WindOptions(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("grid", _c.c_int32),
        ("wind", _c.c_double),
        ("pipe", _c.c_bool),
    ]

class CAD_WindState(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("active", _c.c_bool),
        ("starting", _c.c_bool),
        ("running", _c.c_bool),
        ("failed", _c.c_bool),
        ("pipe", _c.c_bool),
        ("steps", _c.c_int64),
        ("stepsPerSecond", _c.c_double),
        ("nx", _c.c_int32),
        ("ny", _c.c_int32),
        ("nz", _c.c_int32),
        ("cellSize", _c.c_double),
        ("origin", CAD_GeVec3),
        ("wind", _c.c_double),
        ("reynolds", _c.c_double),
        ("dragCoefficient", _c.c_double),
        ("forceCoefficient", CAD_GeVec3),
        ("frontalArea", _c.c_double),
        ("objectCount", _c.c_int32),
        ("pipeOpenings", _c.c_int32),
        ("fluidCells", _c.c_int64),
        ("regrids", _c.c_int32),
    ]

class CAD_WindViewOptions(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("field", _c.c_int32),
        ("planeAxis", _c.c_int32),
        ("planeAt", _c.c_double),
        ("planeShown", _c.c_bool),
        ("smoke", _c.c_bool),
        ("surfacePressure", _c.c_bool),
        ("isoSpeed", _c.c_double),
        ("trajectories", _c.c_bool),
    ]

class CAD_WindPointValue(_c.Structure):
    _fields_ = [
        ("velocity", CAD_GeVec3),
        ("speed", _c.c_double),
        ("pressure", _c.c_double),
        ("inFluid", _c.c_bool),
    ]

class CAD_WindSurfacePoint(_c.Structure):
    _fields_ = [
        ("point", CAD_GeVec3),
        ("normal", CAD_GeVec3),
    ]

class CAD_WaterOptions(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("grid", _c.c_int32),
        ("level", _c.c_double),
        ("openTop", _c.c_bool),
        ("speed", _c.c_double),
    ]

class CAD_WaterState(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("active", _c.c_bool),
        ("starting", _c.c_bool),
        ("running", _c.c_bool),
        ("failed", _c.c_bool),
        ("openTop", _c.c_bool),
        ("container", _c.c_uint32),
        ("steps", _c.c_int64),
        ("stepsPerSecond", _c.c_double),
        ("nx", _c.c_int32),
        ("ny", _c.c_int32),
        ("nz", _c.c_int32),
        ("cellSize", _c.c_double),
        ("origin", CAD_GeVec3),
        ("tiltX", _c.c_double),
        ("tiltY", _c.c_double),
        ("shake", _c.c_double),
        ("shakePeriod", _c.c_double),
        ("resonancePeriod", _c.c_double),
        ("massDrift", _c.c_double),
        ("spilledFraction", _c.c_double),
        ("surfaceTriangleCount", _c.c_int32),
        ("floaterCount", _c.c_int32),
        ("restarts", _c.c_int32),
    ]

class CAD_WaterFloater(_c.Structure):
    _fields_ = [
        ("id", _c.c_uint32),
        ("density", _c.c_double),
        ("center", CAD_GeVec3),
        ("velocity", CAD_GeVec3),
        ("submerged", _c.c_double),
        ("tilt", _c.c_double),
        ("wallContacts", _c.c_int32),
    ]

class CAD_WaterPointValue(_c.Structure):
    _fields_ = [
        ("fill", _c.c_double),
        ("velocity", CAD_GeVec3),
    ]

class CAD_ClothOptions(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("mode", _c.c_int32),
        ("fabric", _c.c_int32),
        ("resolution", _c.c_int32),
        ("sizeFactor", _c.c_double),
        ("windSpeed", _c.c_double),
        ("gust", _c.c_double),
        ("fast", _c.c_bool),
    ]

class CAD_ClothState(_c.Structure):
    _fields_ = [
        ("size", _c.c_uint32),
        ("active", _c.c_bool),
        ("starting", _c.c_bool),
        ("running", _c.c_bool),
        ("failed", _c.c_bool),
        ("mode", _c.c_int32),
        ("fabric", _c.c_int32),
        ("pointCount", _c.c_int32),
        ("triangleCount", _c.c_int32),
        ("obstacleCount", _c.c_int32),
        ("rodGiven", _c.c_bool),
        ("time", _c.c_double),
        ("stepMs", _c.c_double),
        ("realtime", _c.c_double),
        ("meanStretch", _c.c_double),
        ("maxStretch", _c.c_double),
        ("maxSpeed", _c.c_double),
        ("thickness", _c.c_double),
        ("unitToMeter", _c.c_double),
    ]

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
