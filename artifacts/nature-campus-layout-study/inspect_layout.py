"""Read-only render-geometry diagnostics; not body/navigation/accessibility proof."""
import bpy,json,hashlib,math
from pathlib import Path
from mathutils import Vector
from mathutils.bvhtree import BVHTree
root=Path(__file__).resolve().parent
source=root/'nature-campus-layout.glb'
before=hashlib.sha256(source.read_bytes()).hexdigest()
startup=set(bpy.context.scene.objects)
bpy.ops.import_scene.gltf(filepath=str(source))
objects=[o for o in bpy.context.scene.objects if o.type=='MESH' and o not in startup]
trees={};inventory=[]
for o in objects:
    vs=[o.matrix_world@v.co for v in o.data.vertices]
    o.data.calc_loop_triangles()
    ts=[tuple(t.vertices) for t in o.data.loop_triangles]
    inventory.append({'name':o.name,'vertices':len(vs),'triangles':len(ts),'finite':all(math.isfinite(c) for v in vs for c in v)})
    if any(s in o.name.lower() for s in ['floor','promenade','glazing','frame','branching columns','welcome desk','river below','valley']):
        trees[o.name]=BVHTree.FromPolygons(vs,ts,all_triangles=True)
observations=json.loads((root/'layout-observations.json').read_text())
rows=[]
for route in observations['routes']:
    hits=[];coverage=[];water=[];buried=[]
    pts=route['points']
    for i,p in enumerate(pts):
        if i:
            a=Vector(pts[i-1])+Vector((0,0,1.4));b=Vector(p)+Vector((0,0,1.4));d=b-a
            for name,tree in trees.items():
                if not any(s in name.lower() for s in ['glazing','frame','branching columns','welcome desk']): continue
                point,_,_,distance=tree.ray_cast(a,d.normalized(),d.length)
                if point is not None: hits.append({'object':name,'segment':i,'point':list(point)})
        d=Vector(pts[min(i+1,len(pts)-1)])-Vector(pts[max(i-1,0)])
        side=Vector((-d.y,d.x,0)).normalized()
        for offset in (-1.35,0,1.35):
            q=Vector(p)+side*offset
            floor=[];terrain=[]
            for name,tree in trees.items():
                if not any(s in name.lower() for s in ['floor','promenade','valley','river below']): continue
                point,_,_,_=tree.ray_cast(q+Vector((0,0,20)),Vector((0,0,-1)),40)
                if point is None: continue
                if 'floor' in name.lower() or 'promenade' in name.lower():floor.append({'object':name,'z':point.z})
                elif 'valley' in name.lower():terrain.append(point.z)
                elif 'river below' in name.lower():water.append({'sample':i,'offset':offset,'z':point.z})
            coverage.append({'sample':i,'offset':offset,'floor':floor})
            if floor and terrain and max(terrain)>max(f['z'] for f in floor)+.02:
                buried.append({'sample':i,'offset':offset,'terrain_z':max(terrain),'floor_z':max(f['z'] for f in floor)})
    rows.append({'destination':route['destination'],'sampled_floor_points':len(coverage),
                 'missing_floor_points':[r for r in coverage if not r['floor']],
                 'obstacle_segment_hits':hits,'water_under_sampled_points':len(water),
                 'terrain_above_floor_points':buried})
assert hashlib.sha256(source.read_bytes()).hexdigest()==before
result={'method':'Imported exported render meshes; world triangle BVHs; 81 points and +/-1.35 lateral samples; segments at varying floor+1.4',
        'limits':'No collision controller, swept body, slope/accessibility/structural certification or production budgets',
        'glb_sha256':before,'mesh_count':len(objects),'inventory':inventory,'routes':rows}
(root/'geometry-inspection.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps({r['destination']:{k:v for k,v in r.items() if k not in ('destination','obstacle_segment_hits','terrain_above_floor_points')}|{'hits':len(r['obstacle_segment_hits']),'buried':len(r['terrain_above_floor_points'])} for r in rows}),flush=True)
