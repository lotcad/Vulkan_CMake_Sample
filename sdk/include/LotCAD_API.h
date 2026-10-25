#pragma once
/* LotCAD C API — all areas. Include this one header, or only the area headers you need (api/lotcad/lotcad_*.h).
 * 모든 영역을 포함하는 헤더. 필요한 영역만 쓰려면 lotcad/lotcad_*.h 를 따로 포함해도 된다(각자 lotcad_types.h 를 포함).
 *
 *   area        ObjectARX counterpart                     contents
 *   types       —                                         CAD_API macro, common rules
 *   geometry    AcGe                                      vectors, matrices, planes, lines, arcs, curve handles, intersection (any thread)
 *   app        AcAp                                      engine lifetime, host view, input, overlay, clipboard, messages
 *   view        AcGs                                      camera, views, projection, viewports, visual style, section, capture
 *   editor      AcEd                                      commands, interactive tools, jig, prompts, picking, selection, snap
 *   events      reactors                                  callbacks, event listeners
 *   plugin      —                                         plugin loading, UI items, plugin entities, entity properties, panels
 *   document    AcDbDatabase / symbol tables              documents, files, transactions, undo, layers, linetypes, blocks, xrefs
 *   objects     AcDbEntity                                ids, properties, JSON, query, transform, color, layer, bounds, measure
 *   curves      AcDbCurve                                 lines, arcs, polylines, splines, sketch constraints
 *   modify      modify commands                           stretch/lengthen/break/offset/trim/extend/align (move/copy/array/mirror = objects)
 *   drawing     annotation                                text, dimensions, leaders, hatches, drawing views, plot, images
 *   solids      AcDb3dSolid / AcBr                        primitives, B-Rep features, booleans, fillets, interference
 *   mesh        —                                         meshes, mesh repair, point clouds, volume meshes
 *   graph       — (Grasshopper / Geometry Nodes)          node graph: nodes, links, values, evaluate, bake
 *   analysis    —                                         wind tunnel, water, structural analysis
 *   effects     —                                         particles, external effects
 *   robot       —                                         URDF robots, joints, rigging
 *   nav         —                                         navigation agents, TCP link, external poses
 *   arch        —                                         rooms, floorplans
 *   ai          —                                         AI requests, AI actions, MCP tools
 */

#include "lotcad/lotcad_types.h"
#include "lotcad/lotcad_geometry.h"
#include "lotcad/lotcad_app.h"
#include "lotcad/lotcad_view.h"
#include "lotcad/lotcad_editor.h"
#include "lotcad/lotcad_events.h"
#include "lotcad/lotcad_plugin.h"
#include "lotcad/lotcad_document.h"
#include "lotcad/lotcad_objects.h"
#include "lotcad/lotcad_curves.h"
#include "lotcad/lotcad_modify.h"
#include "lotcad/lotcad_drawing.h"
#include "lotcad/lotcad_solids.h"
#include "lotcad/lotcad_mesh.h"
#include "lotcad/lotcad_graph.h"
#include "lotcad/lotcad_analysis.h"
#include "lotcad/lotcad_effects.h"
#include "lotcad/lotcad_robot.h"
#include "lotcad/lotcad_nav.h"
#include "lotcad/lotcad_arch.h"
#include "lotcad/lotcad_ai.h"
