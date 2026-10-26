"""Read-only geometric observations of the current exported campus.

This is an inspection probe, not a navigation implementation or conformance test.
Probe heights/spacing are diagnostic model units, not accepted body dimensions.
"""
import hashlib
import json
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector
from mathutils.bvhtree import BVHTree

args = sys.argv[sys.argv.index("--") + 1:]
source, destination = map(Path, args)
before = hashlib.sha256(source.read_bytes()).hexdigest()
startup_objects = set(bpy.context.scene.objects)
bpy.ops.import_scene.gltf(filepath=str(source))
objects = [obj for obj in bpy.context.scene.objects
           if obj.type == "MESH" and obj not in startup_objects]
inventory, trees, plan_meshes = [], {}, []
for obj in objects:
    verts = [obj.matrix_world @ vertex.co for vertex in obj.data.vertices]
    obj.data.calc_loop_triangles()
    triangles = [tuple(t.vertices) for t in obj.data.loop_triangles]
    inventory.append({
        "name": obj.name, "vertices": len(verts), "triangles": len(triangles),
        "min": [min(v[axis] for v in verts) for axis in range(3)],
        "max": [max(v[axis] for v in verts) for axis in range(3)],
    })
    if any(token in obj.name.lower() for token in ("terrace", "promenade", "glazing", "flowing valley river")):
        plan_meshes.append({"name": obj.name, "world_vertices": [list(v) for v in verts],
                            "triangles": triangles})
    if any(token in obj.name.lower() for token in (
        "terrace", "promenade", "glazing", "timber columns", "welcome desk",
        "department rear wall", "information display", "table", "chair",
        "flowing valley river", "continuous sculpted valley",
    )):
        trees[obj.name] = BVHTree.FromPolygons(verts, triangles, all_triangles=True)

def vertical_hits(x, y, names):
    hits = []
    for name in names:
        point, normal, index, distance = trees[name].ray_cast(
            Vector((x, y, 30)), Vector((0, 0, -1)), 100
        )
        if point is not None:
            hits.append({"object": name, "z": point.z, "normal_z": normal.z})
    return sorted(hits, key=lambda hit: hit["z"], reverse=True)

floor_names = [name for name in trees if "terrace" in name.lower() or "promenade" in name.lower()]
water_names = [name for name in trees if "flowing valley river" in name.lower()]
terrain_names = [name for name in trees if "continuous sculpted valley" in name.lower()]
obstacle_names = [name for name in trees if any(token in name.lower() for token in (
    "glazing", "timber columns", "welcome desk", "department rear wall",
    "information display", "table", "chair",
))]
modules = [
    ("Strategy & Transformation", -29, -5),
    ("Digital Products & Growth", -32, 27),
    ("AI, Data & Automation", -6, 49),
    ("Immersive & Creative", 28, 39),
    ("Cloud, Reliability & Trust", 36, -3),
]
routes = []
for name, x, y in modules:
    samples = []
    for i in range(201):
        t = i / 200
        px = -3 + (x + 3) * t + 2 * math.sin(math.pi * t)
        py = 12 + (y - 12) * t
        floors = vertical_hits(px, py, floor_names)
        water = vertical_hits(px, py, water_names)
        samples.append({"t": t, "xy": [px, py], "floors": floors,
                        "water": water, "terrain": vertical_hits(px, py, terrain_names)})
    obstruction_hits = []
    # Use the generator's actual 20-segment centreline, at a diagnostic height.
    for i in range(20):
        start_t, end_t = i / 20, (i + 1) / 20
        a = Vector((-3 + (x + 3) * start_t + 2 * math.sin(math.pi * start_t),
                    12 + (y - 12) * start_t, 1.4))
        b = Vector((-3 + (x + 3) * end_t + 2 * math.sin(math.pi * end_t),
                    12 + (y - 12) * end_t, 1.4))
        delta = b - a
        for obj_name in obstacle_names:
            point, normal, index, distance = trees[obj_name].ray_cast(a, delta.normalized(), delta.length)
            if point is not None:
                obstruction_hits.append({"segment": i, "object": obj_name,
                                         "point": list(point), "distance_in_segment": distance})
    routes.append({
        "name": name, "sample_count": len(samples), "samples": samples,
        "samples_without_named_paving_or_terrace": sum(not row["floors"] for row in samples),
        "samples_over_exported_water": sum(bool(row["water"]) for row in samples),
        "diagnostic_height": 1.4, "centreline_obstruction_hits": obstruction_hits,
    })

arrival = []
for i in range(541):
    y = -42 + i * .1
    arrival.append({"xy": [-3, y], "floors": vertical_hits(-3, y, floor_names)})

result = {
    "status": "DOING", "source": str(source), "source_sha256": before,
    "blender_version": bpy.app.version_string,
    "coordinates": "Imported Blender world XY plan, Z vertical; unverified model units",
    "method": "World-space imported mesh triangles; zero-epsilon BVH vertical and segment rays",
    "limits": [
        "Names classify inspected render geometry only; no authored collision authority is inferred.",
        "Sampled centreline coverage is not full-width, continuous, body-clearance or navigation proof.",
        "Probe height 1.4 and sample spacing are diagnostic, not approved human scale or tolerances.",
        "A paving strip above water does not establish bridge support or a valid crossing.",
        "No scene save, render, export, model revision or application change is performed.",
    ],
    "runtime_api_docs": {"FromPolygons": BVHTree.FromPolygons.__doc__, "ray_cast": BVHTree.ray_cast.__doc__},
    "mesh_inventory": inventory, "plan_meshes": plan_meshes, "classified_floor_objects": floor_names,
    "classified_obstacle_objects": obstacle_names, "routes": routes, "arrival": arrival,
}
after = hashlib.sha256(source.read_bytes()).hexdigest()
if after != before:
    raise RuntimeError("Protected input bytes changed during inspection")
destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("CAMPUS_INSPECTION", len(objects), "mesh objects; input unchanged")
for route in routes:
    print(route["name"], "missing named floor", route["samples_without_named_paving_or_terrace"],
          "water samples", route["samples_over_exported_water"],
          "obstructions", sorted({hit["object"] for hit in route["centreline_obstruction_hits"]}))
