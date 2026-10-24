# 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
# 생성기: tools/gen_python_binding.py (엔진 빌드의 SDK 내보내기 단계)
"""LotCAD C API — Analysis 영역."""
from __future__ import annotations

import ctypes as _c
from typing import Any, Callable, Sequence  # noqa: F401  (형식 힌트)

from . import _native as _n
from ._types import *  # noqa: F401,F403

__all__ = ['CAD_SIM_STRESS', 'CAD_SIM_HEAT', 'CAD_SIM_MODAL', 'CAD_SIM_BUCKLING', 'CAD_SIM_MAT_STEEL', 'CAD_SIM_MAT_ALUMINUM', 'CAD_SIM_MAT_STAINLESS', 'CAD_SIM_MAT_TITANIUM', 'CAD_SIM_MAT_ABS', 'CAD_SIM_MAT_CUSTOM', 'CAD_SIM_MESH_NORMAL', 'CAD_SIM_MESH_FAST', 'CAD_SIM_MESH_FINE', 'CAD_SIM_UNITS_AUTO', 'CAD_SIM_UNITS_MM', 'CAD_SIM_UNITS_M', 'CAD_SIM_FIX', 'CAD_SIM_FORCE', 'CAD_SIM_PRESSURE', 'CAD_SIM_TEMPERATURE', 'CAD_SIM_HEAT_FLOW', 'CAD_SIM_CONVECTION', 'CAD_SIM_AXIS_X', 'CAD_SIM_AXIS_Y', 'CAD_SIM_AXIS_Z', 'CAD_SIM_STAGE_IDLE', 'CAD_SIM_STAGE_MESH', 'CAD_SIM_STAGE_CURVE', 'CAD_SIM_STAGE_ASSEMBLE', 'CAD_SIM_STAGE_SOLVE', 'CAD_SIM_FIELD_DISPLACEMENT', 'CAD_SIM_FIELD_VON_MISES', 'CAD_SIM_FIELD_STRESS', 'CAD_SIM_FIELD_SAFETY', 'CAD_SIM_FIELD_TEMPERATURE', 'CAD_SIM_FIELD_HEAT_FLUX', 'CAD_SIM_METRIC_MAX_VON_MISES', 'CAD_SIM_METRIC_MAX_DISPLACEMENT', 'CAD_SIM_METRIC_MAX_TEMPERATURE', 'CAD_SIM_METRIC_MIN_TEMPERATURE', 'CAD_SIM_METRIC_MAX_HEAT_FLUX', 'CAD_SIM_METRIC_FREQUENCY', 'CAD_SIM_METRIC_LOAD_FACTOR', 'CAD_WIND_GRID_NORMAL', 'CAD_WIND_GRID_FAST', 'CAD_WIND_GRID_FINE', 'CAD_WIND_FIELD_SPEED', 'CAD_WIND_FIELD_PRESSURE', 'CAD_WIND_FIELD_VORTICITY', 'CAD_WIND_FIELD_SMOKE', 'CAD_WIND_CELL_VELOCITY', 'CAD_WIND_CELL_PRESSURE', 'CAD_WIND_CELL_SOLID', 'CAD_WATER_GRID_NORMAL', 'CAD_WATER_GRID_FAST', 'CAD_WATER_GRID_FINE', 'CAD_WATER_CELL_FILL', 'CAD_WATER_CELL_VELOCITY', 'CAD_WATER_CELL_SOLID', 'CAD_CLOTH_DRAPE', 'CAD_CLOTH_CURTAIN', 'CAD_CLOTH_FABRIC_COTTON', 'CAD_CLOTH_FABRIC_SILK', 'CAD_CLOTH_FABRIC_DENIM', 'CAD_CLOTH_FABRIC_LEATHER', 'CAD_CLOTH_RES_NORMAL', 'CAD_CLOTH_RES_FAST', 'CAD_CLOTH_RES_FINE', 'CAD_WindTunnel', 'CAD_Water', 'CAD_StructuralAnalysis', 'CAD_SimOpen', 'CAD_SimClose', 'CAD_SimClear', 'CAD_SimGetOptions', 'CAD_SimSetOptions', 'CAD_SimGetFaces', 'CAD_SimFindFace', 'CAD_SimSetCondition', 'CAD_SimClearCondition', 'CAD_SimGetConditions', 'CAD_SimRun', 'CAD_SimCancel', 'CAD_SimWait', 'CAD_SimGetState', 'CAD_SimGetSummary', 'CAD_SimGetNodes', 'CAD_SimGetElements', 'CAD_SimGetBoundary', 'CAD_SimGetBoundaryFaces', 'CAD_SimGetNodeField', 'CAD_SimGetModes', 'CAD_SimGetModeShape', 'CAD_SimGetFaceHeat', 'CAD_SimGetConvergence', 'CAD_WindOpen', 'CAD_WindClose', 'CAD_WindGetOptions', 'CAD_WindSetOptions', 'CAD_WindReset', 'CAD_WindSetRunning', 'CAD_WindAdvance', 'CAD_WindGetState', 'CAD_WindGetView', 'CAD_WindSetView', 'CAD_WindGetCellField', 'CAD_WindSample', 'CAD_WindSurfacePressure', 'CAD_WindGetStreamline', 'CAD_WaterOpen', 'CAD_WaterClose', 'CAD_WaterGetOptions', 'CAD_WaterSetOptions', 'CAD_WaterReset', 'CAD_WaterSetRunning', 'CAD_WaterAdvance', 'CAD_WaterSetTilt', 'CAD_WaterSetShake', 'CAD_WaterAddFloaters', 'CAD_WaterClearFloaters', 'CAD_WaterGetState', 'CAD_WaterGetFloaters', 'CAD_WaterGetSurfaceVertices', 'CAD_WaterGetSurfaceTriangles', 'CAD_WaterGetCellField', 'CAD_WaterSample', 'CAD_ClothOpen', 'CAD_ClothClose', 'CAD_ClothGetOptions', 'CAD_ClothSetOptions', 'CAD_ClothSetMaterial', 'CAD_ClothGetMaterial', 'CAD_ClothReset', 'CAD_ClothSetRunning', 'CAD_ClothAdvance', 'CAD_ClothGetState', 'CAD_ClothGetPoints', 'CAD_ClothGetNormals', 'CAD_ClothGetTriangles', 'CAD_ClothBake']

_f = _n.native

CAD_SIM_STRESS = 0
CAD_SIM_HEAT = 1
CAD_SIM_MODAL = 2
CAD_SIM_BUCKLING = 3
CAD_SIM_MAT_STEEL = 0
CAD_SIM_MAT_ALUMINUM = 1
CAD_SIM_MAT_STAINLESS = 2
CAD_SIM_MAT_TITANIUM = 3
CAD_SIM_MAT_ABS = 4
CAD_SIM_MAT_CUSTOM = 100
CAD_SIM_MESH_NORMAL = 0
CAD_SIM_MESH_FAST = 1
CAD_SIM_MESH_FINE = 2
CAD_SIM_UNITS_AUTO = 0
CAD_SIM_UNITS_MM = 1
CAD_SIM_UNITS_M = 2
CAD_SIM_FIX = 1
CAD_SIM_FORCE = 2
CAD_SIM_PRESSURE = 3
CAD_SIM_TEMPERATURE = 4
CAD_SIM_HEAT_FLOW = 5
CAD_SIM_CONVECTION = 6
CAD_SIM_AXIS_X = 1
CAD_SIM_AXIS_Y = 2
CAD_SIM_AXIS_Z = 4
CAD_SIM_STAGE_IDLE = -1
CAD_SIM_STAGE_MESH = 0
CAD_SIM_STAGE_CURVE = 1
CAD_SIM_STAGE_ASSEMBLE = 2
CAD_SIM_STAGE_SOLVE = 3
CAD_SIM_FIELD_DISPLACEMENT = 1
CAD_SIM_FIELD_VON_MISES = 2
CAD_SIM_FIELD_STRESS = 3
CAD_SIM_FIELD_SAFETY = 4
CAD_SIM_FIELD_TEMPERATURE = 5
CAD_SIM_FIELD_HEAT_FLUX = 6
CAD_SIM_METRIC_MAX_VON_MISES = 1
CAD_SIM_METRIC_MAX_DISPLACEMENT = 2
CAD_SIM_METRIC_MAX_TEMPERATURE = 3
CAD_SIM_METRIC_MIN_TEMPERATURE = 4
CAD_SIM_METRIC_MAX_HEAT_FLUX = 5
CAD_SIM_METRIC_FREQUENCY = 6
CAD_SIM_METRIC_LOAD_FACTOR = 7
CAD_WIND_GRID_NORMAL = 0
CAD_WIND_GRID_FAST = 1
CAD_WIND_GRID_FINE = 2
CAD_WIND_FIELD_SPEED = 0
CAD_WIND_FIELD_PRESSURE = 1
CAD_WIND_FIELD_VORTICITY = 2
CAD_WIND_FIELD_SMOKE = 3
CAD_WIND_CELL_VELOCITY = 1
CAD_WIND_CELL_PRESSURE = 2
CAD_WIND_CELL_SOLID = 3
CAD_WATER_GRID_NORMAL = 0
CAD_WATER_GRID_FAST = 1
CAD_WATER_GRID_FINE = 2
CAD_WATER_CELL_FILL = 1
CAD_WATER_CELL_VELOCITY = 2
CAD_WATER_CELL_SOLID = 3
CAD_CLOTH_DRAPE = 0
CAD_CLOTH_CURTAIN = 1
CAD_CLOTH_FABRIC_COTTON = 0
CAD_CLOTH_FABRIC_SILK = 1
CAD_CLOTH_FABRIC_DENIM = 2
CAD_CLOTH_FABRIC_LEATHER = 3
CAD_CLOTH_RES_NORMAL = 0
CAD_CLOTH_RES_FAST = 1
CAD_CLOTH_RES_FINE = 2

_n.bind("CAD_WindTunnel", _c.c_int, [_c.c_char_p, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_Water", _c.c_int, [_c.c_char_p, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_StructuralAnalysis", _c.c_int, [_c.c_char_p, _c.POINTER(_c.c_char), _c.c_int])
_n.bind("CAD_SimOpen", _c.c_int32, [_c.c_uint32])
_n.bind("CAD_SimClose", _c.c_int32, [])
_n.bind("CAD_SimClear", _c.c_int32, [])
_n.bind("CAD_SimGetOptions", _c.c_int32, [_c.POINTER(CAD_SimOptions)])
_n.bind("CAD_SimSetOptions", _c.c_int32, [_c.POINTER(CAD_SimOptions)])
_n.bind("CAD_SimGetFaces", _c.c_int32, [_c.POINTER(CAD_SimFace), _c.c_uint32])
_n.bind("CAD_SimFindFace", _c.c_int32, [CAD_GeVec3, _c.POINTER(_c.c_int32)])
_n.bind("CAD_SimSetCondition", _c.c_int32, [CAD_SimCondition])
_n.bind("CAD_SimClearCondition", _c.c_int32, [_c.c_int32, _c.c_int32])
_n.bind("CAD_SimGetConditions", _c.c_int32, [_c.POINTER(CAD_SimCondition), _c.c_uint32])
_n.bind("CAD_SimRun", _c.c_int32, [_c.POINTER(CAD_SimRunOptions)])
_n.bind("CAD_SimCancel", _c.c_int32, [])
_n.bind("CAD_SimWait", _c.c_int32, [_c.c_double, _c.POINTER(_c.c_bool)])
_n.bind("CAD_SimGetState", _c.c_int32, [_c.POINTER(CAD_SimState)])
_n.bind("CAD_SimGetSummary", _c.c_int32, [_c.POINTER(CAD_SimSummary)])
_n.bind("CAD_SimGetNodes", _c.c_int32, [_c.POINTER(CAD_GeVec3), _c.c_uint32])
_n.bind("CAD_SimGetElements", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_SimGetBoundary", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_SimGetBoundaryFaces", _c.c_int32, [_c.POINTER(_c.c_int32), _c.c_uint32])
_n.bind("CAD_SimGetNodeField", _c.c_int32, [_c.c_int32, _c.POINTER(_c.c_double), _c.c_uint32])
_n.bind("CAD_SimGetModes", _c.c_int32, [_c.POINTER(_c.c_double), _c.c_uint32])
_n.bind("CAD_SimGetModeShape", _c.c_int32, [_c.c_int32, _c.POINTER(CAD_GeVec3), _c.c_uint32])
_n.bind("CAD_SimGetFaceHeat", _c.c_int32, [_c.c_int32, _c.POINTER(_c.c_double)])
_n.bind("CAD_SimGetConvergence", _c.c_int32, [_c.POINTER(CAD_SimConvergence), _c.c_uint32])
_n.bind("CAD_WindOpen", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.POINTER(CAD_WindOptions)])
_n.bind("CAD_WindClose", _c.c_int32, [])
_n.bind("CAD_WindGetOptions", _c.c_int32, [_c.POINTER(CAD_WindOptions)])
_n.bind("CAD_WindSetOptions", _c.c_int32, [_c.POINTER(CAD_WindOptions)])
_n.bind("CAD_WindReset", _c.c_int32, [])
_n.bind("CAD_WindSetRunning", _c.c_int32, [_c.c_bool])
_n.bind("CAD_WindAdvance", _c.c_int32, [_c.c_int32])
_n.bind("CAD_WindGetState", _c.c_int32, [_c.POINTER(CAD_WindState)])
_n.bind("CAD_WindGetView", _c.c_int32, [_c.POINTER(CAD_WindViewOptions)])
_n.bind("CAD_WindSetView", _c.c_int32, [_c.POINTER(CAD_WindViewOptions)])
_n.bind("CAD_WindGetCellField", _c.c_int32, [_c.c_int32, _c.POINTER(_c.c_double), _c.c_uint32])
_n.bind("CAD_WindSample", _c.c_int32, [_c.POINTER(CAD_GeVec3), _c.c_uint32, _c.POINTER(CAD_WindPointValue), _c.c_uint32])
_n.bind("CAD_WindSurfacePressure", _c.c_int32, [_c.POINTER(CAD_WindSurfacePoint), _c.c_uint32, _c.POINTER(_c.c_double), _c.c_uint32])
_n.bind("CAD_WindGetStreamline", _c.c_int32, [CAD_GeVec3, _c.POINTER(CAD_GeVec3), _c.c_uint32])
_n.bind("CAD_WaterOpen", _c.c_int32, [_c.c_uint32, _c.POINTER(CAD_WaterOptions)])
_n.bind("CAD_WaterClose", _c.c_int32, [])
_n.bind("CAD_WaterGetOptions", _c.c_int32, [_c.POINTER(CAD_WaterOptions)])
_n.bind("CAD_WaterSetOptions", _c.c_int32, [_c.POINTER(CAD_WaterOptions)])
_n.bind("CAD_WaterReset", _c.c_int32, [])
_n.bind("CAD_WaterSetRunning", _c.c_int32, [_c.c_bool])
_n.bind("CAD_WaterAdvance", _c.c_int32, [_c.c_int32])
_n.bind("CAD_WaterSetTilt", _c.c_int32, [_c.c_double, _c.c_double])
_n.bind("CAD_WaterSetShake", _c.c_int32, [_c.c_double, _c.c_double])
_n.bind("CAD_WaterAddFloaters", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.c_double])
_n.bind("CAD_WaterClearFloaters", _c.c_int32, [_c.c_bool])
_n.bind("CAD_WaterGetState", _c.c_int32, [_c.POINTER(CAD_WaterState)])
_n.bind("CAD_WaterGetFloaters", _c.c_int32, [_c.POINTER(CAD_WaterFloater), _c.c_uint32])
_n.bind("CAD_WaterGetSurfaceVertices", _c.c_int32, [_c.POINTER(CAD_GeVec3), _c.c_uint32])
_n.bind("CAD_WaterGetSurfaceTriangles", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_WaterGetCellField", _c.c_int32, [_c.c_int32, _c.POINTER(_c.c_double), _c.c_uint32])
_n.bind("CAD_WaterSample", _c.c_int32, [_c.POINTER(CAD_GeVec3), _c.c_uint32, _c.POINTER(CAD_WaterPointValue), _c.c_uint32])
_n.bind("CAD_ClothOpen", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32, _c.POINTER(CAD_ClothOptions)])
_n.bind("CAD_ClothClose", _c.c_int32, [])
_n.bind("CAD_ClothGetOptions", _c.c_int32, [_c.POINTER(CAD_ClothOptions)])
_n.bind("CAD_ClothSetOptions", _c.c_int32, [_c.POINTER(CAD_ClothOptions)])
_n.bind("CAD_ClothSetMaterial", _c.c_int32, [_c.c_char_p])
_n.bind("CAD_ClothGetMaterial", _c.c_int32, [_c.POINTER(_c.c_char), _c.c_uint32])
_n.bind("CAD_ClothReset", _c.c_int32, [])
_n.bind("CAD_ClothSetRunning", _c.c_int32, [_c.c_bool])
_n.bind("CAD_ClothAdvance", _c.c_int32, [_c.c_double])
_n.bind("CAD_ClothGetState", _c.c_int32, [_c.POINTER(CAD_ClothState)])
_n.bind("CAD_ClothGetPoints", _c.c_int32, [_c.POINTER(CAD_GeVec3), _c.c_uint32])
_n.bind("CAD_ClothGetNormals", _c.c_int32, [_c.POINTER(CAD_GeVec3), _c.c_uint32])
_n.bind("CAD_ClothGetTriangles", _c.c_int32, [_c.POINTER(_c.c_uint32), _c.c_uint32])
_n.bind("CAD_ClothBake", _c.c_int32, [_c.POINTER(_c.c_uint32)])


def CAD_WindTunnel(argsJson: str | None) -> str | None:
    """C: int CAD_WindTunnel(const char* argsJson, char* outUtf8, int cap)

    해석 — MCP 도구 wind_tunnel · water · structural_analysis 와 같은 창구(엔진 windTunnelOp·waterOp·simOp). argsJson = {"op": …, …}
    (없으면 status), 결과 JSON(ok·error·message·상태)을 outUtf8 에(cap 바이트, null 이면 길이만). 반환 = 길이, 실패 -1.
    켜기(start)는 다음 프레임에, 구조 해석 풀이(run·converge)는 작업 스레드에서 — status 로 끝을 본다.
    2회 호출(outUtf8 null 로 길이 → 버퍼)은 첫 호출에서 한 번만 실행하고, 같은 인자의 다음 호출엔 그 결과를 준다.
     바람 터널: status · start {ids|id, grid fast|normal|fine, wind 0.02~0.10} · stop · reset · pause · play ·
                view {field speed|pressure|vortex|smoke, plane x|y|z, at 0~1, smoke, surface} · wind {value}      — 바람은 +X
     물:        status · start {id(그릇), level 0~1, grid} · stop · reset · pause · play · tilt {x, y 도} · shake {amplitude 0~1, period}
     구조 해석: status(faces = 면 번호·넓이·가운데·법선) · open {id} · close · clear · run · cancel · converge(요소 × 0.7 로 한 번 더) ·
                set {type stress|heat|modal|buckling, material, size, units mm|m, modes, thermal, ref_temp, wind, wind_speed, show, scale, animate} ·
                fix|free {face} · force {face, force[3] N} · pressure {face, value MPa} · temp {face, value °C} · flux {face, value W} · convect {face, h, ambient}
                face = 번호 또는 그 면 가까운 점 [x,y,z]. 결과는 status 의 result(응력·변위·안전율·온도·진동수·좌굴 배수·convergence).
    """
    _need = _f.CAD_WindTunnel(_n.text(argsJson), None, 0)   # 2회 호출 규약: 길이를 물으며 한 번 실행
    if _need < 0:
        return None
    _cap = _need + 1
    _buf = _c.create_string_buffer(_cap)
    if _f.CAD_WindTunnel(_n.text(argsJson), _buf, _cap) < 0:   # 같은 인자 → 다시 실행하지 않고 결과만
        return None
    return _n.decode(_buf.value)


def CAD_Water(argsJson: str | None) -> str | None:
    """C: int CAD_Water(const char* argsJson, char* outUtf8, int cap)

    해석 — MCP 도구 wind_tunnel · water · structural_analysis 와 같은 창구(엔진 windTunnelOp·waterOp·simOp). argsJson = {"op": …, …}
    (없으면 status), 결과 JSON(ok·error·message·상태)을 outUtf8 에(cap 바이트, null 이면 길이만). 반환 = 길이, 실패 -1.
    켜기(start)는 다음 프레임에, 구조 해석 풀이(run·converge)는 작업 스레드에서 — status 로 끝을 본다.
    2회 호출(outUtf8 null 로 길이 → 버퍼)은 첫 호출에서 한 번만 실행하고, 같은 인자의 다음 호출엔 그 결과를 준다.
     바람 터널: status · start {ids|id, grid fast|normal|fine, wind 0.02~0.10} · stop · reset · pause · play ·
                view {field speed|pressure|vortex|smoke, plane x|y|z, at 0~1, smoke, surface} · wind {value}      — 바람은 +X
     물:        status · start {id(그릇), level 0~1, grid} · stop · reset · pause · play · tilt {x, y 도} · shake {amplitude 0~1, period}
     구조 해석: status(faces = 면 번호·넓이·가운데·법선) · open {id} · close · clear · run · cancel · converge(요소 × 0.7 로 한 번 더) ·
                set {type stress|heat|modal|buckling, material, size, units mm|m, modes, thermal, ref_temp, wind, wind_speed, show, scale, animate} ·
                fix|free {face} · force {face, force[3] N} · pressure {face, value MPa} · temp {face, value °C} · flux {face, value W} · convect {face, h, ambient}
                face = 번호 또는 그 면 가까운 점 [x,y,z]. 결과는 status 의 result(응력·변위·안전율·온도·진동수·좌굴 배수·convergence).
    """
    _need = _f.CAD_Water(_n.text(argsJson), None, 0)   # 2회 호출 규약: 길이를 물으며 한 번 실행
    if _need < 0:
        return None
    _cap = _need + 1
    _buf = _c.create_string_buffer(_cap)
    if _f.CAD_Water(_n.text(argsJson), _buf, _cap) < 0:   # 같은 인자 → 다시 실행하지 않고 결과만
        return None
    return _n.decode(_buf.value)


def CAD_StructuralAnalysis(argsJson: str | None) -> str | None:
    """C: int CAD_StructuralAnalysis(const char* argsJson, char* outUtf8, int cap)

    해석 — MCP 도구 wind_tunnel · water · structural_analysis 와 같은 창구(엔진 windTunnelOp·waterOp·simOp). argsJson = {"op": …, …}
    (없으면 status), 결과 JSON(ok·error·message·상태)을 outUtf8 에(cap 바이트, null 이면 길이만). 반환 = 길이, 실패 -1.
    켜기(start)는 다음 프레임에, 구조 해석 풀이(run·converge)는 작업 스레드에서 — status 로 끝을 본다.
    2회 호출(outUtf8 null 로 길이 → 버퍼)은 첫 호출에서 한 번만 실행하고, 같은 인자의 다음 호출엔 그 결과를 준다.
     바람 터널: status · start {ids|id, grid fast|normal|fine, wind 0.02~0.10} · stop · reset · pause · play ·
                view {field speed|pressure|vortex|smoke, plane x|y|z, at 0~1, smoke, surface} · wind {value}      — 바람은 +X
     물:        status · start {id(그릇), level 0~1, grid} · stop · reset · pause · play · tilt {x, y 도} · shake {amplitude 0~1, period}
     구조 해석: status(faces = 면 번호·넓이·가운데·법선) · open {id} · close · clear · run · cancel · converge(요소 × 0.7 로 한 번 더) ·
                set {type stress|heat|modal|buckling, material, size, units mm|m, modes, thermal, ref_temp, wind, wind_speed, show, scale, animate} ·
                fix|free {face} · force {face, force[3] N} · pressure {face, value MPa} · temp {face, value °C} · flux {face, value W} · convect {face, h, ambient}
                face = 번호 또는 그 면 가까운 점 [x,y,z]. 결과는 status 의 result(응력·변위·안전율·온도·진동수·좌굴 배수·convergence).
    """
    _need = _f.CAD_StructuralAnalysis(_n.text(argsJson), None, 0)   # 2회 호출 규약: 길이를 물으며 한 번 실행
    if _need < 0:
        return None
    _cap = _need + 1
    _buf = _c.create_string_buffer(_cap)
    if _f.CAD_StructuralAnalysis(_n.text(argsJson), _buf, _cap) < 0:   # 같은 인자 → 다시 실행하지 않고 결과만
        return None
    return _n.decode(_buf.value)


def CAD_SimOpen(id: int) -> int:
    """C: CAD_Status CAD_SimOpen(uint32_t id)

    닫힌 메시 솔리드 id 를 해석 대상으로 연다(패널도 켬). 열린 동안 선택이 바뀌어도 대상은 그대로.
    없는 id = CAD_E_BAD_HANDLE, 메시가 아님 = CAD_E_WRONG_TYPE, 닫히지 않음 = CAD_E_NOT_CLOSED(meshfix 로 먼저),
    다른 대상에 조건·결과가 있음 = CAD_E_BUSY(CAD_SimClear 먼저). 같은 id 를 다시 열면 그대로(조건 유지)
    """
    return _f.CAD_SimOpen(id)


def CAD_SimClose() -> int:
    """C: CAD_Status CAD_SimClose(void)

    해석을 닫는다(조건·결과·패널) — 풀이 중이면 멈추고 닫음
    """
    return _f.CAD_SimClose()


def CAD_SimClear() -> int:
    """C: CAD_Status CAD_SimClear(void)

    조건과 결과를 지운다(대상·설정은 그대로)
    """
    return _f.CAD_SimClear()


def CAD_SimGetOptions() -> tuple[int, CAD_SimOptions]:
    """C: CAD_Status CAD_SimGetOptions(CAD_SimOptions* out)

    지금 설정 — 부르는 쪽이 out->size = sizeof
    """
    out = CAD_SimOptions()
    out.size = _c.sizeof(CAD_SimOptions)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_SimGetOptions(_c.byref(out))
    return (_r, out)


def CAD_SimSetOptions(opt: CAD_SimOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_SimSetOptions(const CAD_SimOptions* opt)

    설정을 통째로 바꾼다(NULL = 기본값) — 바뀌면 결과를 지운다. 범위 밖 값 = CAD_E_INVALID_ARG(아무것도 안 바꿈). 대상 없이도 된다
    """
    if opt is None and fields:
        opt = CAD_SimOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_SimOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_SimSetOptions(_p_opt)


def CAD_SimGetFaces(outFaces: Any, capacity: int) -> int:
    """C: int32_t CAD_SimGetFaces(CAD_SimFace* outFaces, uint32_t capacity)

    대상의 면 — 반환 = 면 개수
    """
    return _f.CAD_SimGetFaces(outFaces, capacity)


def CAD_SimFindFace(point: CAD_GeVec3) -> tuple[int, int]:
    """C: CAD_Status CAD_SimFindFace(CAD_GeVec3 point, int32_t* outFace)

    점(월드)에서 가장 가까운 면의 번호
    """
    outFace = _c.c_int32()
    _r = _f.CAD_SimFindFace(point, _c.byref(outFace))
    return (_r, outFace.value)


def CAD_SimSetCondition(condition: CAD_SimCondition) -> int:
    """C: CAD_Status CAD_SimSetCondition(CAD_SimCondition condition)

    면 조건 주기·바꾸기 — 결과를 지운다. 면 번호 범위 밖 = CAD_E_OUT_OF_RANGE, 종류·값이 맞지 않음 = CAD_E_INVALID_ARG
    """
    return _f.CAD_SimSetCondition(condition)


def CAD_SimClearCondition(face: int, kind: int) -> int:
    """C: CAD_Status CAD_SimClearCondition(int32_t face, int32_t kind)

    면 조건 지우기 — kind 의 쪽(구조 1~3 · 열 4~6)만, 0 = 둘 다. 조건이 없던 면이면 그대로 CAD_OK
    """
    return _f.CAD_SimClearCondition(face, kind)


def CAD_SimGetConditions(outConditions: Any, capacity: int) -> int:
    """C: int32_t CAD_SimGetConditions(CAD_SimCondition* outConditions, uint32_t capacity)

    지금 조건 — 구조 조건(면 순) 다음 열 조건(면 순). 반환 = 개수
    """
    return _f.CAD_SimGetConditions(outConditions, capacity)


def CAD_SimRun(opt: CAD_SimRunOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_SimRun(const CAD_SimRunOptions* opt)

    풀이 시작(작업 스레드 — 바로 돌아온다). 고정이 없음·하중이 없음 등 = CAD_E_INVALID_ARG, 해석 모듈 없음 = CAD_E_NOT_SUPPORTED
    """
    if opt is None and fields:
        opt = CAD_SimRunOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_SimRunOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_SimRun(_p_opt)


def CAD_SimCancel() -> int:
    """C: CAD_Status CAD_SimCancel(void)

    풀이 멈춤(멈춘 뒤 CAD_SimWait 는 CAD_E_FAILED "멈춤") — 풀이 중이 아니면 그대로 CAD_OK
    """
    return _f.CAD_SimCancel()


def CAD_SimWait(timeoutSeconds: float) -> tuple[int, bool]:
    """C: CAD_Status CAD_SimWait(double timeoutSeconds, bool* outDone)

    풀이가 끝나기를 기다린다 — timeoutSeconds < 0 = 끝날 때까지, 0 = 기다리지 않고 보기만. 끝났으면 결과를 바로 받는다(CAD_Tick 불필요).
    CAD_OK + *outDone: 참 = 결과 있음, 거짓 = 아직 도는 중(시간 다 됨). 마지막 풀이 실패 = CAD_E_FAILED + 이유, 푼 적 없음 = CAD_E_NOT_READY
    """
    outDone = _c.c_bool()
    _r = _f.CAD_SimWait(timeoutSeconds, _c.byref(outDone))
    return (_r, outDone.value)


def CAD_SimGetState() -> tuple[int, CAD_SimState]:
    """C: CAD_Status CAD_SimGetState(CAD_SimState* out)

    부르는 쪽이 out->size = sizeof
    """
    out = CAD_SimState()
    out.size = _c.sizeof(CAD_SimState)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_SimGetState(_c.byref(out))
    return (_r, out)


def CAD_SimGetSummary() -> tuple[int, CAD_SimSummary]:
    """C: CAD_Status CAD_SimGetSummary(CAD_SimSummary* out)

    결과 요약 — 부르는 쪽이 out->size = sizeof. 결과 없음 = CAD_E_NOT_READY
    """
    out = CAD_SimSummary()
    out.size = _c.sizeof(CAD_SimSummary)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_SimGetSummary(_c.byref(out))
    return (_r, out)


def CAD_SimGetNodes(outNodes: Any, capacity: int) -> int:
    """C: int32_t CAD_SimGetNodes(CAD_GeVec3* outNodes, uint32_t capacity)

    절점 자리(월드, 장면 단위) — 앞쪽이 사면체 꼭짓점, 뒤쪽이 변 가운데 절점. 반환 = 절점 개수
    """
    return _f.CAD_SimGetNodes(outNodes, capacity)


def CAD_SimGetElements(outNodeIndices: Any, capacity: int) -> int:
    """C: int32_t CAD_SimGetElements(uint32_t* outNodeIndices, uint32_t capacity)

    사면체 — 사면체마다 절점 번호 10개(VTK 2차 사면체 순서: 꼭짓점 0~3, 가운데 4 (0,1)·5 (1,2)·6 (0,2)·7 (0,3)·8 (1,3)·9 (2,3)).
    반환 = 값 개수(사면체 × 10)
    """
    return _f.CAD_SimGetElements(outNodeIndices, capacity)


def CAD_SimGetBoundary(outNodeIndices: Any, capacity: int) -> int:
    """C: int32_t CAD_SimGetBoundary(uint32_t* outNodeIndices, uint32_t capacity)

    표면 2차 삼각형 — 삼각형마다 절점 번호 6개(꼭짓점 0~2, 가운데 (0,1)·(1,2)·(2,0)). 반환 = 값 개수(삼각형 × 6)
    """
    return _f.CAD_SimGetBoundary(outNodeIndices, capacity)


def CAD_SimGetBoundaryFaces(outFaces: Any, capacity: int) -> int:
    """C: int32_t CAD_SimGetBoundaryFaces(int32_t* outFaces, uint32_t capacity)

    표면 삼각형마다 면 번호(CAD_SimGetBoundary 와 같은 차례). 반환 = 삼각형 개수
    """
    return _f.CAD_SimGetBoundaryFaces(outFaces, capacity)


def CAD_SimGetNodeField(field: int, outValues: Any, capacity: int) -> int:
    """C: int32_t CAD_SimGetNodeField(int32_t field, double* outValues, uint32_t capacity)

    절점 값 — field = CAD_SIM_FIELD_*(절점마다 값 개수는 그 enum 에, 절점 순서 = CAD_SimGetNodes). 반환 = 값 개수(절점 × 개수).
    그 결과에 없는 값(열 해석의 응력 …) = CAD_E_NOT_READY
    """
    return _f.CAD_SimGetNodeField(field, outValues, capacity)


def CAD_SimGetModes(outValues: Any, capacity: int) -> int:
    """C: int32_t CAD_SimGetModes(double* outValues, uint32_t capacity)

    모드 해석 = 진동수 Hz(작은 것부터), 좌굴 = 하중 배수(준 하중의 몇 배에서 꺾이나, 작은 것부터). 반환 = 개수
    """
    return _f.CAD_SimGetModes(outValues, capacity)


def CAD_SimGetModeShape(mode: int, outShape: Any, capacity: int) -> int:
    """C: int32_t CAD_SimGetModeShape(int32_t mode, CAD_GeVec3* outShape, uint32_t capacity)

    모드(좌굴) 모양 mode(0부터) — 절점마다 방향(가장 큰 크기 1, 단위 없음). 반환 = 절점 개수
    """
    return _f.CAD_SimGetModeShape(mode, outShape, capacity)


def CAD_SimGetFaceHeat(face: int) -> tuple[int, float]:
    """C: CAD_Status CAD_SimGetFaceHeat(int32_t face, double* outWatts)

    열 해석에서 그 면으로 들어온 열 W(조건 없는 면 = 단열이라 0)
    """
    outWatts = _c.c_double()
    _r = _f.CAD_SimGetFaceHeat(face, _c.byref(outWatts))
    return (_r, outWatts.value)


def CAD_SimGetConvergence(outItems: Any, capacity: int) -> int:
    """C: int32_t CAD_SimGetConvergence(CAD_SimConvergence* outItems, uint32_t capacity)

    수렴 확인 결과 — 반환 = 개수(수렴 확인을 안 했으면 0)
    """
    return _f.CAD_SimGetConvergence(outItems, capacity)


def CAD_WindOpen(ids: Sequence | None, count: int, opt: CAD_WindOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_WindOpen(const uint32_t* ids, uint32_t count, const CAD_WindOptions* opt)

    닫힌 메시 솔리드들(ids, count ≥ 1)에 바람을 맞힌다(패널도 켬). 이미 같은 솔리드로 켜져 있으면 설정만 바꾼다(CAD_WindSetOptions 처럼),
    다른 솔리드면 그것으로 처음부터. 없는 id = CAD_E_BAD_HANDLE, 메시가 아님 = CAD_E_WRONG_TYPE, 모듈 없음 = CAD_E_NOT_SUPPORTED,
    격자·셰이더를 못 만듦 = CAD_E_FAILED. 그리는 중(플러그인 명령 안)에 부르면 다음 CAD_Tick 에 켠다(state.starting)
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    if opt is None and fields:
        opt = CAD_WindOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_WindOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_WindOpen(_a_ids, count, _p_opt)


def CAD_WindClose() -> int:
    """C: CAD_Status CAD_WindClose(void)

    끈다(패널도) — 꺼져 있으면 그대로 CAD_OK

    묶음 주석: 닫힌 메시 솔리드들(ids, count ≥ 1)에 바람을 맞힌다(패널도 켬). 이미 같은 솔리드로 켜져 있으면 설정만 바꾼다(CAD_WindSetOptions 처럼),
    다른 솔리드면 그것으로 처음부터. 없는 id = CAD_E_BAD_HANDLE, 메시가 아님 = CAD_E_WRONG_TYPE, 모듈 없음 = CAD_E_NOT_SUPPORTED,
    격자·셰이더를 못 만듦 = CAD_E_FAILED. 그리는 중(플러그인 명령 안)에 부르면 다음 CAD_Tick 에 켠다(state.starting)
    """
    return _f.CAD_WindClose()


def CAD_WindGetOptions() -> tuple[int, CAD_WindOptions]:
    """C: CAD_Status CAD_WindGetOptions(CAD_WindOptions* out)

    지금 설정(꺼져 있으면 다음에 켤 설정) — 부르는 쪽이 out->size = sizeof

    묶음 주석: 닫힌 메시 솔리드들(ids, count ≥ 1)에 바람을 맞힌다(패널도 켬). 이미 같은 솔리드로 켜져 있으면 설정만 바꾼다(CAD_WindSetOptions 처럼),
    다른 솔리드면 그것으로 처음부터. 없는 id = CAD_E_BAD_HANDLE, 메시가 아님 = CAD_E_WRONG_TYPE, 모듈 없음 = CAD_E_NOT_SUPPORTED,
    격자·셰이더를 못 만듦 = CAD_E_FAILED. 그리는 중(플러그인 명령 안)에 부르면 다음 CAD_Tick 에 켠다(state.starting)
    """
    out = CAD_WindOptions()
    out.size = _c.sizeof(CAD_WindOptions)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_WindGetOptions(_c.byref(out))
    return (_r, out)


def CAD_WindSetOptions(opt: CAD_WindOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_WindSetOptions(const CAD_WindOptions* opt)

    설정 바꾸기(NULL = 기본값). 범위 밖 = CAD_E_INVALID_ARG(아무것도 안 바꿈). 꺼져 있으면 다음에 켤 설정으로
    """
    if opt is None and fields:
        opt = CAD_WindOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_WindOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_WindSetOptions(_p_opt)


def CAD_WindReset() -> int:
    """C: CAD_Status CAD_WindReset(void)

    흐름을 처음부터(같은 격자)

    묶음 주석: 설정 바꾸기(NULL = 기본값). 범위 밖 = CAD_E_INVALID_ARG(아무것도 안 바꿈). 꺼져 있으면 다음에 켤 설정으로
    """
    return _f.CAD_WindReset()


def CAD_WindSetRunning(running: bool) -> int:
    """C: CAD_Status CAD_WindSetRunning(bool running)

    거짓 = 멈춤, 참 = 계속

    묶음 주석: 설정 바꾸기(NULL = 기본값). 범위 밖 = CAD_E_INVALID_ARG(아무것도 안 바꿈). 꺼져 있으면 다음에 켤 설정으로
    """
    return _f.CAD_WindSetRunning(running)


def CAD_WindAdvance(steps: int) -> int:
    """C: CAD_Status CAD_WindAdvance(int32_t steps)

    steps 걸음(1~1000000)을 흘릴 때까지 기다린다 — 틱 없이 흐름을 나아가게(스크립트·AI). 그동안 엔진은 멈춘다(그래픽 큐를 같이 씀).
    옮긴 솔리드는 먼저 다시 맞춘다. 그리는 중 = CAD_E_BUSY(CAD_Post 로 틱 밖에서), 계산이 깨짐 = CAD_E_FAILED + 이유
    """
    return _f.CAD_WindAdvance(steps)


def CAD_WindGetState() -> tuple[int, CAD_WindState]:
    """C: CAD_Status CAD_WindGetState(CAD_WindState* out)

    부르는 쪽이 out->size = sizeof

    묶음 주석: steps 걸음(1~1000000)을 흘릴 때까지 기다린다 — 틱 없이 흐름을 나아가게(스크립트·AI). 그동안 엔진은 멈춘다(그래픽 큐를 같이 씀).
    옮긴 솔리드는 먼저 다시 맞춘다. 그리는 중 = CAD_E_BUSY(CAD_Post 로 틱 밖에서), 계산이 깨짐 = CAD_E_FAILED + 이유
    """
    out = CAD_WindState()
    out.size = _c.sizeof(CAD_WindState)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_WindGetState(_c.byref(out))
    return (_r, out)


def CAD_WindGetView() -> tuple[int, CAD_WindViewOptions]:
    """C: CAD_Status CAD_WindGetView(CAD_WindViewOptions* out)

    꺼져 있음 = CAD_E_NOT_READY. 부르는 쪽이 out->size = sizeof

    묶음 주석: steps 걸음(1~1000000)을 흘릴 때까지 기다린다 — 틱 없이 흐름을 나아가게(스크립트·AI). 그동안 엔진은 멈춘다(그래픽 큐를 같이 씀).
    옮긴 솔리드는 먼저 다시 맞춘다. 그리는 중 = CAD_E_BUSY(CAD_Post 로 틱 밖에서), 계산이 깨짐 = CAD_E_FAILED + 이유
    """
    out = CAD_WindViewOptions()
    out.size = _c.sizeof(CAD_WindViewOptions)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_WindGetView(_c.byref(out))
    return (_r, out)


def CAD_WindSetView(opt: CAD_WindViewOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_WindSetView(const CAD_WindViewOptions* opt)

    화면 표시 바꾸기 — NULL = 켠 때의 보기(빠르기·처음 단면·판 보임·연기 켬·나머지 끔), 모르는 칸도 그 값.
    field 가 SMOKE 면 smoke 는 켜진다. 범위 밖 = CAD_E_INVALID_ARG(아무것도 안 바꿈)
    """
    if opt is None and fields:
        opt = CAD_WindViewOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_WindViewOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_WindSetView(_p_opt)


def CAD_WindGetCellField(field: int, outValues: Any, capacity: int) -> int:
    """C: int32_t CAD_WindGetCellField(int32_t field, double* outValues, uint32_t capacity)

    칸 값 — field = CAD_WIND_CELL_*(칸마다 값 개수는 그 enum 에). 반환 = 값 개수(칸 × 개수)
    """
    return _f.CAD_WindGetCellField(field, outValues, capacity)


def CAD_WindSample(points: Sequence | None, count: int, outValues: Any, capacity: int) -> int:
    """C: int32_t CAD_WindSample(const CAD_GeVec3* points, uint32_t count, CAD_WindPointValue* outValues, uint32_t capacity)

    월드 점들(count 개)의 흐름 값 — 칸 사이는 세 방향 선형 보간. 반환 = 점 개수(outValues 엔 capacity 까지 차례대로).
    아직 한 걸음도 안 흘렀음 = CAD_E_NOT_READY
    """
    _a_points = _n.array(CAD_GeVec3, points)
    return _f.CAD_WindSample(_a_points, count, outValues, capacity)


def CAD_WindSurfacePressure(points: Sequence | None, count: int, outCp: Any, capacity: int) -> int:
    """C: int32_t CAD_WindSurfacePressure(const CAD_WindSurfacePoint* points, uint32_t count, double* outCp, uint32_t capacity)

    표면 압력 계수 — 표면 점(자리 + 바깥 법선)마다 법선 쪽 1.5칸의 Cp(화면 표면 압력 색·구조 해석 바람 하중과 같은 계산).
    반환 = 점 개수(outCp 엔 capacity 까지). 법선 길이 0 = CAD_E_INVALID_ARG
    """
    _a_points = _n.array(CAD_WindSurfacePoint, points)
    return _f.CAD_WindSurfacePressure(_a_points, count, outCp, capacity)


def CAD_WindGetStreamline(seed: CAD_GeVec3, outPoints: Any, capacity: int) -> int:
    """C: int32_t CAD_WindGetStreamline(CAD_GeVec3 seed, CAD_GeVec3* outPoints, uint32_t capacity)

    seed(월드)에서 흐름을 따라간 흐름선(반 칸 간격 점, 월드) — 고체·흡수층·느린 곳(바람의 3 %)에 닿으면 끝. 반환 = 점 개수(씨앗이 고체 속이면 0)
    """
    return _f.CAD_WindGetStreamline(seed, outPoints, capacity)


def CAD_WaterOpen(container: int, opt: CAD_WaterOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_WaterOpen(uint32_t container, const CAD_WaterOptions* opt)

    닫힌 메시 솔리드(그릇) container 에 물을 채워 켠다(패널도). 같은 그릇으로 켜져 있으면 설정만 바꾼다(CAD_WaterSetOptions 처럼).
    없는 id = CAD_E_BAD_HANDLE, 메시가 아님 = CAD_E_WRONG_TYPE, 모듈 없음 = CAD_E_NOT_SUPPORTED, 그릇 안이 너무 작음·닫히지 않음 = CAD_E_FAILED.
    그리는 중에 부르면 다음 CAD_Tick 에 켠다(state.starting)
    """
    if opt is None and fields:
        opt = CAD_WaterOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_WaterOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_WaterOpen(container, _p_opt)


def CAD_WaterClose() -> int:
    """C: CAD_Status CAD_WaterClose(void)

    끈다(띄운 것은 띄운 때 자세로) — 꺼져 있으면 그대로 CAD_OK

    묶음 주석: 닫힌 메시 솔리드(그릇) container 에 물을 채워 켠다(패널도). 같은 그릇으로 켜져 있으면 설정만 바꾼다(CAD_WaterSetOptions 처럼).
    없는 id = CAD_E_BAD_HANDLE, 메시가 아님 = CAD_E_WRONG_TYPE, 모듈 없음 = CAD_E_NOT_SUPPORTED, 그릇 안이 너무 작음·닫히지 않음 = CAD_E_FAILED.
    그리는 중에 부르면 다음 CAD_Tick 에 켠다(state.starting)
    """
    return _f.CAD_WaterClose()


def CAD_WaterGetOptions() -> tuple[int, CAD_WaterOptions]:
    """C: CAD_Status CAD_WaterGetOptions(CAD_WaterOptions* out)

    부르는 쪽이 out->size = sizeof

    묶음 주석: 닫힌 메시 솔리드(그릇) container 에 물을 채워 켠다(패널도). 같은 그릇으로 켜져 있으면 설정만 바꾼다(CAD_WaterSetOptions 처럼).
    없는 id = CAD_E_BAD_HANDLE, 메시가 아님 = CAD_E_WRONG_TYPE, 모듈 없음 = CAD_E_NOT_SUPPORTED, 그릇 안이 너무 작음·닫히지 않음 = CAD_E_FAILED.
    그리는 중에 부르면 다음 CAD_Tick 에 켠다(state.starting)
    """
    out = CAD_WaterOptions()
    out.size = _c.sizeof(CAD_WaterOptions)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_WaterGetOptions(_c.byref(out))
    return (_r, out)


def CAD_WaterSetOptions(opt: CAD_WaterOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_WaterSetOptions(const CAD_WaterOptions* opt)

    NULL = 기본값, 범위 밖 = CAD_E_INVALID_ARG

    묶음 주석: 닫힌 메시 솔리드(그릇) container 에 물을 채워 켠다(패널도). 같은 그릇으로 켜져 있으면 설정만 바꾼다(CAD_WaterSetOptions 처럼).
    없는 id = CAD_E_BAD_HANDLE, 메시가 아님 = CAD_E_WRONG_TYPE, 모듈 없음 = CAD_E_NOT_SUPPORTED, 그릇 안이 너무 작음·닫히지 않음 = CAD_E_FAILED.
    그리는 중에 부르면 다음 CAD_Tick 에 켠다(state.starting)
    """
    if opt is None and fields:
        opt = CAD_WaterOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_WaterOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_WaterSetOptions(_p_opt)


def CAD_WaterReset() -> int:
    """C: CAD_Status CAD_WaterReset(void)

    처음 채운 때로(기울기·흔들기 0, 띄운 것은 띄운 때 자세로)

    묶음 주석: 닫힌 메시 솔리드(그릇) container 에 물을 채워 켠다(패널도). 같은 그릇으로 켜져 있으면 설정만 바꾼다(CAD_WaterSetOptions 처럼).
    없는 id = CAD_E_BAD_HANDLE, 메시가 아님 = CAD_E_WRONG_TYPE, 모듈 없음 = CAD_E_NOT_SUPPORTED, 그릇 안이 너무 작음·닫히지 않음 = CAD_E_FAILED.
    그리는 중에 부르면 다음 CAD_Tick 에 켠다(state.starting)
    """
    return _f.CAD_WaterReset()


def CAD_WaterSetRunning(running: bool) -> int:
    """C: CAD_Status CAD_WaterSetRunning(bool running)

    닫힌 메시 솔리드(그릇) container 에 물을 채워 켠다(패널도). 같은 그릇으로 켜져 있으면 설정만 바꾼다(CAD_WaterSetOptions 처럼).
    없는 id = CAD_E_BAD_HANDLE, 메시가 아님 = CAD_E_WRONG_TYPE, 모듈 없음 = CAD_E_NOT_SUPPORTED, 그릇 안이 너무 작음·닫히지 않음 = CAD_E_FAILED.
    그리는 중에 부르면 다음 CAD_Tick 에 켠다(state.starting)
    """
    return _f.CAD_WaterSetRunning(running)


def CAD_WaterAdvance(steps: int) -> int:
    """C: CAD_Status CAD_WaterAdvance(int32_t steps)

    steps 걸음(1~1000000)을 흘릴 때까지 기다린다(기울기·흔들기·띄운 것 그대로, 끝나면 표면도 다시). 그리는 중 = CAD_E_BUSY, 계산이 깨짐 = CAD_E_FAILED
    """
    return _f.CAD_WaterAdvance(steps)


def CAD_WaterSetTilt(xRadians: float, yRadians: float) -> int:
    """C: CAD_Status CAD_WaterSetTilt(double xRadians, double yRadians)

    그릇 기울이기 — X 축·Y 축 둘레 rad(각 ±0.698 = ±40° 안, 밖이면 CAD_E_INVALID_ARG). 중력을 반대로 돌린다
    """
    return _f.CAD_WaterSetTilt(xRadians, yRadians)


def CAD_WaterSetShake(amplitude: float, periodSteps: float) -> int:
    """C: CAD_Status CAD_WaterSetShake(double amplitude, double periodSteps)

    흔들기 — 세기 0~1(중력의 몇 배, 0 = 멈춤), 주기 걸음(0 = 이 그릇의 공명 주기, 그 밖엔 10 이상)
    """
    return _f.CAD_WaterSetShake(amplitude, periodSteps)


def CAD_WaterAddFloaters(ids: Sequence | None, count: int, density: float) -> int:
    """C: int32_t CAD_WaterAddFloaters(const uint32_t* ids, uint32_t count, double density)

    닫힌 메시 솔리드들을 물에 띄운다(강체 — 부력·물 끌림·벽 닿음). density = 물 대비 0.1~0.95. 그릇·메시 아님은 건너뜀. 반환 = 띄운 개수(0 = 하나도 못 띄움 + 이유)
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    return _f.CAD_WaterAddFloaters(_a_ids, count, density)


def CAD_WaterClearFloaters(restore: bool) -> int:
    """C: CAD_Status CAD_WaterClearFloaters(bool restore)

    띄운 것 내리기 — restore 참 = 띄운 때 자세로

    묶음 주석: 닫힌 메시 솔리드들을 물에 띄운다(강체 — 부력·물 끌림·벽 닿음). density = 물 대비 0.1~0.95. 그릇·메시 아님은 건너뜀. 반환 = 띄운 개수(0 = 하나도 못 띄움 + 이유)
    """
    return _f.CAD_WaterClearFloaters(restore)


def CAD_WaterGetState() -> tuple[int, CAD_WaterState]:
    """C: CAD_Status CAD_WaterGetState(CAD_WaterState* out)

    부르는 쪽이 out->size = sizeof

    묶음 주석: 닫힌 메시 솔리드들을 물에 띄운다(강체 — 부력·물 끌림·벽 닿음). density = 물 대비 0.1~0.95. 그릇·메시 아님은 건너뜀. 반환 = 띄운 개수(0 = 하나도 못 띄움 + 이유)
    """
    out = CAD_WaterState()
    out.size = _c.sizeof(CAD_WaterState)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_WaterGetState(_c.byref(out))
    return (_r, out)


def CAD_WaterGetFloaters(outFloaters: Any, capacity: int) -> int:
    """C: int32_t CAD_WaterGetFloaters(CAD_WaterFloater* outFloaters, uint32_t capacity)

    반환 = 개수

    묶음 주석: 닫힌 메시 솔리드들을 물에 띄운다(강체 — 부력·물 끌림·벽 닿음). density = 물 대비 0.1~0.95. 그릇·메시 아님은 건너뜀. 반환 = 띄운 개수(0 = 하나도 못 띄움 + 이유)
    """
    return _f.CAD_WaterGetFloaters(outFloaters, capacity)


def CAD_WaterGetSurfaceVertices(outVertices: Any, capacity: int) -> int:
    """C: int32_t CAD_WaterGetSurfaceVertices(CAD_GeVec3* outVertices, uint32_t capacity)

    물 표면 메시(채움 0.5 면, 월드) — 정점. 반환 = 정점 개수(아직 표면이 없으면 0)
    """
    return _f.CAD_WaterGetSurfaceVertices(outVertices, capacity)


def CAD_WaterGetSurfaceTriangles(outIndices: Any, capacity: int) -> int:
    """C: int32_t CAD_WaterGetSurfaceTriangles(uint32_t* outIndices, uint32_t capacity)

    물 표면 메시 — 삼각형마다 정점 번호 3개. 반환 = 값 개수(삼각형 × 3)
    """
    return _f.CAD_WaterGetSurfaceTriangles(outIndices, capacity)


def CAD_WaterGetCellField(field: int, outValues: Any, capacity: int) -> int:
    """C: int32_t CAD_WaterGetCellField(int32_t field, double* outValues, uint32_t capacity)

    칸 값 — field = CAD_WATER_CELL_*. 반환 = 값 개수(칸 × 개수)
    """
    return _f.CAD_WaterGetCellField(field, outValues, capacity)


def CAD_WaterSample(points: Sequence | None, count: int, outValues: Any, capacity: int) -> int:
    """C: int32_t CAD_WaterSample(const CAD_GeVec3* points, uint32_t count, CAD_WaterPointValue* outValues, uint32_t capacity)

    월드 점들(count 개)의 채움·속도(세 방향 선형 보간, 고체·격자 밖 칸은 0). 반환 = 점 개수(outValues 엔 capacity 까지)
    """
    _a_points = _n.array(CAD_GeVec3, points)
    return _f.CAD_WaterSample(_a_points, count, outValues, capacity)


def CAD_ClothOpen(ids: Sequence | None, count: int, opt: CAD_ClothOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_ClothOpen(const uint32_t* ids, uint32_t count, const CAD_ClothOptions* opt)

    천을 켠다(패널도). 덮기: ids 에 메시 솔리드가 하나 이상(전부 장애물). 커튼: ids 안의 선(LINE·열린 폴리선) 하나가 막대, 나머지 솔리드는 장애물
    — ids 가 없으면(count 0) 원점 위 2 m 높이 1 m 막대. 같은 대상으로 켜져 있으면 설정만 바꾼다(CAD_ClothSetOptions 처럼), 다른 대상이면 처음부터.
    없는 id = CAD_E_BAD_HANDLE, 솔리드·선이 아님(덮기에 선) = CAD_E_WRONG_TYPE, 덮기에 솔리드 없음·선 둘 이상·범위 밖 설정 = CAD_E_INVALID_ARG,
    막대가 세로이거나 너무 짧음 = CAD_E_FAILED. 그리는 중에 부르면 다음 CAD_Tick 에 켠다(state.starting)
    """
    _a_ids = _n.array(_c.c_uint32, ids)
    if opt is None and fields:
        opt = CAD_ClothOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_ClothOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_ClothOpen(_a_ids, count, _p_opt)


def CAD_ClothClose() -> int:
    """C: CAD_Status CAD_ClothClose(void)

    끈다(패널도) — 꺼져 있으면 그대로 CAD_OK

    묶음 주석: 천을 켠다(패널도). 덮기: ids 에 메시 솔리드가 하나 이상(전부 장애물). 커튼: ids 안의 선(LINE·열린 폴리선) 하나가 막대, 나머지 솔리드는 장애물
    — ids 가 없으면(count 0) 원점 위 2 m 높이 1 m 막대. 같은 대상으로 켜져 있으면 설정만 바꾼다(CAD_ClothSetOptions 처럼), 다른 대상이면 처음부터.
    없는 id = CAD_E_BAD_HANDLE, 솔리드·선이 아님(덮기에 선) = CAD_E_WRONG_TYPE, 덮기에 솔리드 없음·선 둘 이상·범위 밖 설정 = CAD_E_INVALID_ARG,
    막대가 세로이거나 너무 짧음 = CAD_E_FAILED. 그리는 중에 부르면 다음 CAD_Tick 에 켠다(state.starting)
    """
    return _f.CAD_ClothClose()


def CAD_ClothGetOptions() -> tuple[int, CAD_ClothOptions]:
    """C: CAD_Status CAD_ClothGetOptions(CAD_ClothOptions* out)

    지금 설정(꺼져 있으면 다음에 켤 설정) — 부르는 쪽이 out->size = sizeof

    묶음 주석: 천을 켠다(패널도). 덮기: ids 에 메시 솔리드가 하나 이상(전부 장애물). 커튼: ids 안의 선(LINE·열린 폴리선) 하나가 막대, 나머지 솔리드는 장애물
    — ids 가 없으면(count 0) 원점 위 2 m 높이 1 m 막대. 같은 대상으로 켜져 있으면 설정만 바꾼다(CAD_ClothSetOptions 처럼), 다른 대상이면 처음부터.
    없는 id = CAD_E_BAD_HANDLE, 솔리드·선이 아님(덮기에 선) = CAD_E_WRONG_TYPE, 덮기에 솔리드 없음·선 둘 이상·범위 밖 설정 = CAD_E_INVALID_ARG,
    막대가 세로이거나 너무 짧음 = CAD_E_FAILED. 그리는 중에 부르면 다음 CAD_Tick 에 켠다(state.starting)
    """
    out = CAD_ClothOptions()
    out.size = _c.sizeof(CAD_ClothOptions)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_ClothGetOptions(_c.byref(out))
    return (_r, out)


def CAD_ClothSetOptions(opt: CAD_ClothOptions | None = None, **fields) -> int:
    """C: CAD_Status CAD_ClothSetOptions(const CAD_ClothOptions* opt)

    설정 바꾸기(NULL = 기본값). 범위 밖 = CAD_E_INVALID_ARG(아무것도 안 바꿈). 꺼져 있으면 다음에 켤 설정으로.
    모양·점 수·크기가 바뀌면 같은 대상으로 처음부터(멈춤은 그대로) — 못 만들면 CAD_E_FAILED + 이유(천은 꺼짐)
    """
    if opt is None and fields:
        opt = CAD_ClothOptions(**fields)
    if opt is not None and not opt.size:
        opt.size = _c.sizeof(CAD_ClothOptions)
    _p_opt = _c.byref(opt) if opt is not None else None
    return _f.CAD_ClothSetOptions(_p_opt)


def CAD_ClothSetMaterial(name: str | None) -> int:
    """C: CAD_Status CAD_ClothSetMaterial(const char* name)

    재질(무늬) — textures 폴더의 재질 이름(확장자 빼고), "none" = 무늬 없이 천 종류 색만, NULL·"" = 천 종류 따라(실크는 색만).
    없는 재질 = CAD_E_INVALID_ARG. 도는 중에도 바로, 꺼져 있으면 다음에 켤 때. 굽기에도 쓴다
    """
    return _f.CAD_ClothSetMaterial(_n.text(name))


def CAD_ClothGetMaterial() -> str | None:
    """C: int32_t CAD_ClothGetMaterial(char* buf, uint32_t capacity)

    재질 설정 — buf 에 NUL 까지 담고(모자라면 잘라서) 전체 길이(NUL 제외). "" = 천 종류 따라, "none" = 색만
    """
    _cap = 256
    while True:
        _buf = _c.create_string_buffer(_cap)
        _r = _f.CAD_ClothGetMaterial(_buf, _cap)
        if _r < 0:
            return None
        if _r >= _cap - 1 and _cap < (1 << 26):   # 모자라 보이면 키워 다시
            _cap = max(_r + 1, _cap * 2)
            continue
        return _n.decode(_buf.value)


def CAD_ClothReset() -> int:
    """C: CAD_Status CAD_ClothReset(void)

    처음 자리·속도 0 으로, 시간 0(설정 그대로) — 깨진 계산도 이걸로

    묶음 주석: 재질 설정 — buf 에 NUL 까지 담고(모자라면 잘라서) 전체 길이(NUL 제외). "" = 천 종류 따라, "none" = 색만
    """
    return _f.CAD_ClothReset()


def CAD_ClothSetRunning(running: bool) -> int:
    """C: CAD_Status CAD_ClothSetRunning(bool running)

    거짓 = 멈춤(돌아오면 더 나아가지 않음), 참 = 계속

    묶음 주석: 재질 설정 — buf 에 NUL 까지 담고(모자라면 잘라서) 전체 길이(NUL 제외). "" = 천 종류 따라, "none" = 색만
    """
    return _f.CAD_ClothSetRunning(running)


def CAD_ClothAdvance(seconds: float) -> int:
    """C: CAD_Status CAD_ClothAdvance(double seconds)

    seconds 초(1/60 초 걸음으로 반올림, 적어도 한 걸음 · 600 초 이하)를 흘릴 때까지 기다린다 — 틱 없이 천을 나아가게(스크립트·AI).
    작업 스레드는 그동안 비켜 서고, 끝나면 이어서 돈다(멈춤이면 그대로). GPU 를 쓰지 않아 그리는 중에도 된다(화면 천은 다음 틱에).
    계산이 깨짐 = CAD_E_FAILED + 이유
    """
    return _f.CAD_ClothAdvance(seconds)


def CAD_ClothGetState() -> tuple[int, CAD_ClothState]:
    """C: CAD_Status CAD_ClothGetState(CAD_ClothState* out)

    부르는 쪽이 out->size = sizeof

    묶음 주석: seconds 초(1/60 초 걸음으로 반올림, 적어도 한 걸음 · 600 초 이하)를 흘릴 때까지 기다린다 — 틱 없이 천을 나아가게(스크립트·AI).
    작업 스레드는 그동안 비켜 서고, 끝나면 이어서 돈다(멈춤이면 그대로). GPU 를 쓰지 않아 그리는 중에도 된다(화면 천은 다음 틱에).
    계산이 깨짐 = CAD_E_FAILED + 이유
    """
    out = CAD_ClothState()
    out.size = _c.sizeof(CAD_ClothState)   # 출력 구조체 — 엔진은 이 크기까지만 쓴다
    _r = _f.CAD_ClothGetState(_c.byref(out))
    return (_r, out)


def CAD_ClothGetPoints(outPoints: Any, capacity: int) -> int:
    """C: int32_t CAD_ClothGetPoints(CAD_GeVec3* outPoints, uint32_t capacity)

    지금 천 점(월드, 장면 단위) — 칸만큼 채우고 전체 개수. 점 번호는 CAD_ClothGetTriangles 의 번호
    """
    return _f.CAD_ClothGetPoints(outPoints, capacity)


def CAD_ClothGetNormals(outNormals: Any, capacity: int) -> int:
    """C: int32_t CAD_ClothGetNormals(CAD_GeVec3* outNormals, uint32_t capacity)

    점마다 법선(단위, 이웃 삼각형 넓이 가중) — 칸만큼 채우고 전체 개수
    """
    return _f.CAD_ClothGetNormals(outNormals, capacity)


def CAD_ClothGetTriangles(outIndices: Any, capacity: int) -> int:
    """C: int32_t CAD_ClothGetTriangles(uint32_t* outIndices, uint32_t capacity)

    천 삼각형 — 삼각형마다 점 번호 3개(한 장, 감김은 쉴 때 그대로). 반환 = 값 개수(삼각형 × 3)
    """
    return _f.CAD_ClothGetTriangles(outIndices, capacity)


def CAD_ClothBake() -> tuple[int, int]:
    """C: CAD_Status CAD_ClothBake(uint32_t* outId)

    지금 모양에 두께(충돌 두께의 0.6배)를 줘 닫힌 메시 객체로 만든다(재질 그대로, 되돌리기 1) — 천은 끈다(그리는 중이면 다음 틱에).
    outId = 새 객체 id. 꺼져 있음 = CAD_E_NOT_READY, 못 만듦 = CAD_E_FAILED
    """
    outId = _c.c_uint32()
    _r = _f.CAD_ClothBake(_c.byref(outId))
    return (_r, outId.value)
