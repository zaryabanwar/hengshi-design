"""Final third isolated model revision; original procedural geometry, v1 study.

Source direction: D-066/D-067, selected nature-campus concept, WORLD_EXPERIENCE
and SPATIAL_STORYBOARD. No Atlanta/application inputs, external assets or staff.
This authors a visual layout, not a certified building or navigation controller.
"""
import bpy, math, random, json, hashlib
from pathlib import Path
from mathutils import Vector

OUT = Path(__file__).resolve().parent
random.seed(67)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
scene = bpy.context.scene
scene.unit_settings.system = 'METRIC'
scene.unit_settings.scale_length = 1.0
geo = {}

def material(name, color, roughness=.8):
    m = bpy.data.materials.new(name)
    m.diffuse_color = (*color, 1)
    m.use_nodes = True
    p = m.node_tree.nodes.get('Principled BSDF')
    p.inputs['Base Color'].default_value = (*color, 1)
    p.inputs['Roughness'].default_value = roughness
    return m

timber = material('Honey timber', (.36,.19,.075))
soffit = material('Warm timber soffit', (.58,.34,.14))
paving = material('Warm mineral paving', (.52,.48,.37))
plaster = material('Earth plaster', (.58,.45,.27))
meadow = material('Living roof meadow', (.13,.23,.055))
ground = material('Forest ground', (.13,.19,.055))
leaf = [material('Leaf shade '+str(i), c) for i,c in enumerate([
    (.035,.11,.025),(.09,.19,.045),(.17,.25,.065),(.24,.30,.085)])]
stone = material('River stone', (.30,.33,.25))
water = material('Valley water', (.045,.24,.23), .16)
flower = material('Meadow flowers', (.57,.47,.55))
ink = material('Information board', (.018,.03,.027))
light = material('Board labels', (.78,.72,.55))
glass = material('Glazing', (.22,.32,.23), .12)
glass.node_tree.nodes['Principled BSDF'].inputs['Transmission Weight'].default_value = .75
glass.node_tree.nodes['Principled BSDF'].inputs['IOR'].default_value = 1.45

def mesh(name, vertices, faces, mat):
    vs, fs = geo.setdefault((name,mat.name), ([],[]))
    offset = len(vs)
    vs.extend(vertices)
    fs.extend(tuple(offset+i for i in f) for f in faces)

def box(name, c, size, mat):
    x,y,z = c
    a,b,h = [v/2 for v in size]
    vs = [(x+dx*a,y+dy*b,z+dz*h) for dx,dy,dz in
          [(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]]
    mesh(name,vs,[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)],mat)

def rod(name, a, b, radius, mat, n=8):
    a,b = Vector(a),Vector(b)
    d = (b-a).normalized()
    u = d.cross(Vector((0,0,1)))
    if u.length < .01: u = d.cross(Vector((0,1,0)))
    u.normalize()
    w = d.cross(u)
    vs = [tuple(c+radius*(math.cos(i*math.tau/n)*u+math.sin(i*math.tau/n)*w)) for c in (a,b) for i in range(n)]
    mesh(name,vs,[tuple(range(n-1,-1,-1)),tuple(range(n,n*2))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)],mat)

def crown(name, c, radii, mat, n=9, rings=5):
    vs=[]
    for j in range(rings+1):
        p=math.pi*j/rings
        for i in range(n):
            a=i*math.tau/n
            irregular=1+.09*math.sin(i*3+j*2)
            vs.append((c[0]+radii[0]*math.sin(p)*math.cos(a)*irregular,
                       c[1]+radii[1]*math.sin(p)*math.sin(a)*irregular,c[2]+radii[2]*math.cos(p)))
    mesh(name,vs,[(j*n+i,j*n+(i+1)%n,(j+1)*n+(i+1)%n,(j+1)*n+i) for j in range(rings) for i in range(n)],mat)

modules=[
    dict(name='Reception',x=0,y=16,rx=14,ry=10,h=6.8,z=.8,phase=.3,lobes=3),
    dict(name='Strategy & Transformation',x=-28,y=-3,rx=12,ry=8,h=5.2,z=.8,phase=1.2,lobes=2),
    dict(name='Digital Products & Growth',x=-31,y=30,rx=11,ry=8,h=5.5,z=1.45,phase=2.5,lobes=3),
    dict(name='AI, Data & Automation',x=-12,y=54,rx=12.5,ry=8,h=5.6,z=3.0,phase=.6,lobes=2),
    dict(name='Immersive & Creative',x=47,y=43,rx=12,ry=8,h=5.4,z=2.3,phase=1.8,lobes=3),
    dict(name='Cloud, Reliability & Trust',x=43,y=-5,rx=11,ry=7.5,h=5.0,z=.8,phase=3.1,lobes=2),
]
for m in modules:
    m['rotation']=0 if m['name']=='Reception' else math.atan2(16-m['y'],-m['x'])+math.pi/2

def footprint(m,x,y):
    dx=x-m['x'];dy=y-m['y'];a=m['rotation']
    return ((dx*math.cos(a)+dy*math.sin(a))/m['rx'])**2+((-dx*math.sin(a)+dy*math.cos(a))/m['ry'])**2

def point(m,a,r=1):
    radius=1+.15*math.cos(m['lobes']*a+m['phase'])+.07*math.sin(a)
    dx=m['rx']*radius*math.cos(a)*r;dy=m['ry']*radius*math.sin(a)*r
    return (m['x']+dx*math.cos(m['rotation'])-dy*math.sin(m['rotation']),m['y']+dx*math.sin(m['rotation'])+dy*math.cos(m['rotation']))

planned_routes=[]
for m in modules[1:]:
    a=math.atan2(m['y']-16,m['x'])
    start=(*point(modules[0],a,.82),.8)
    end=(*point(m,-math.pi/2,.80),m['z'])
    pts=[]
    for i in range(81):
        t=i/80
        pts.append((start[0]*(1-t)+end[0]*t+math.sin(t*math.pi)*1.6,
                    start[1]*(1-t)+end[1]*t,start[2]*(1-t)+end[2]*t))
    planned_routes.append(dict(destination=m['name'],points=pts,width=3.2))

def river_x(y): return 21+4*math.sin(y*.055)+2*math.sin(y*.12)
def land_z(x,y):
    # A valley with genuine near/middle/far depth, not a distant mountain wall.
    terrace=.8+max(y-20,0)*.065
    banks=max(abs(x)-57,0)*.34
    distance=max(y-72,0)*.19
    height=terrace+banks*(.75+.3*math.sin(y*.046+x*.026))+distance*(.8+.35*math.sin(x*.04))
    for m in modules:
        radius=math.sqrt(footprint(m,x,y))
        if radius<1.6:
            blend=max(0,min(1,(1.6-radius)/.3))
            height=height*(1-blend)+(m['z']-.06)*blend
    # Grade the land around the authored promenade; retain the lower river bed.
    for route in planned_routes:
        for px,py,pz in route['points'][::4]:
            distance=math.hypot(x-px,y-py)
            if distance<5.0: height=min(height,pz-.35)
    return height

N=90
vs=[]
for j in range(N):
    y=-100+j*4.0
    for i in range(N):
        x=-165+i*3.9
        z=land_z(x,y)
        if abs(x-river_x(y))<6: z-=2.5
        vs.append((x,y,z))
mesh('Layered forest valley',vs,[(j*N+i,j*N+i+1,(j+1)*N+i+1,(j+1)*N+i) for j in range(N-1) for i in range(N-1)],ground)
vs=[]
for i in range(120):
    y=-95+i*3.0
    z=land_z(river_x(y),y)-1.8
    vs.extend([(river_x(y)-3.5,y,z),(river_x(y)+3.5,y,z)])
mesh('River below connected terraces',vs,[(2*i,2*i+1,2*i+3,2*i+2) for i in range(119)],water)
for y in (66,103,148):
    x=river_x(y);z=land_z(x,y)-1.8
    mesh('Cascade',[(x-3.3,y,z+1),(x+3.3,y,z+1),(x+3.3,y-1.7,z-.3),(x-3.3,y-1.7,z-.3)],[(0,1,2,3)],light)
for i in range(270):
    y=random.uniform(-80,220);x=river_x(y)+random.choice((-1,1))*random.uniform(4.1,7.2)
    crown('River boulders',(x,y,land_z(x,y)-.8),(random.uniform(.5,1.7),random.uniform(.5,1.4),random.uniform(.5,1.2)),stone)

def roof_z(m,a,r):
    return m['z']+m['h']+1.3*math.sin(m['lobes']*a+m['phase'])*r+.9*math.sin(r*math.pi)
def angular_distance(a,b): return abs((a-b+math.pi)%math.tau-math.pi)
reception_gaps=[-math.pi/2]+[math.atan2(m['y']-16,m['x']) for m in modules[1:]]

for m in modules:
    name=m['name'];n=80
    for layer,mat,dz in [('living roof',meadow,0),('slatted canopy',soffit,-.24)]:
        vs=[]
        for r in (.23,.40,.65,.90,1.16):
            for i in range(n):
                a=i*math.tau/n;x,y=point(m,a,r)
                vs.append((x,y,roof_z(m,a,r)+dz))
        mesh(name+' '+layer,vs,[(j*n+i,j*n+(i+1)%n,(j+1)*n+(i+1)%n,(j+1)*n+i) for j in range(4) for i in range(n)],mat)
    floor=[(*point(m,i*math.tau/n),m['z']) for i in range(n)]
    mesh(name+' floor',[(m['x'],m['y'],m['z'])]+floor,[(0,i+1,(i+1)%n+1) for i in range(n)],paving)
    for i in range(48):
        a=i*math.tau/48;b=(i+1)*math.tau/48
        mid=(a+b)/2
        gaps=reception_gaps if name=='Reception' else [-math.pi/2]
        if any(angular_distance(mid,g)<.23 for g in gaps): continue
        x,y=point(m,a,.95);xx,yy=point(m,b,.95)
        z=roof_z(m,a,.95)-.4;zz=roof_z(m,b,.95)-.4
        rod(name+' timber frames',(x,y,m['z']),(x,y,z),.09,timber)
        mesh(name+' glazing',[(x,y,m['z']+.04),(xx,yy,m['z']+.04),(xx,yy,zz),(x,y,z)],[(0,1,2,3)],glass)
    for r in (.23,1.16):
        for i in range(n):
            a=i*math.tau/n;b=(i+1)*math.tau/n
            rod(name+' curved roof edge',(*point(m,a,r),roof_z(m,a,r)),(*point(m,b,r),roof_z(m,b,r)),.14,timber)
    for i in range(46):
        a=i*math.tau/46
        for r,r2 in ((.23,.46),(.46,.72),(.72,.98),(.98,1.16)):
            rod(name+' roof ribs',(*point(m,a,r),roof_z(m,a,r)-.28),(*point(m,a,r2),roof_z(m,a,r2)-.28),.055,soffit)
    for i in range(180):
        a=random.uniform(0,math.tau);r=random.uniform(.36,1.08);x,y=point(m,a,r)
        crown(name+' roof planting',(x,y,roof_z(m,a,r)+.09),(.38,.32,.19),random.choice([meadow,*leaf,flower]),7,4)

routes=planned_routes
def ribbon(name, points, width, mat):
    vs=[]
    for i,p in enumerate(points):
        d=Vector(points[min(i+1,len(points)-1)])-Vector(points[max(i-1,0)])
        side=Vector((-d.y,d.x,0)).normalized()*width/2
        vs.extend([tuple(Vector(p)-side),tuple(Vector(p)+side)])
    mesh(name,vs,[(i*2,i*2+1,i*2+3,i*2+2) for i in range(len(points)-1)],mat)
    return vs

arrival=[(.6*math.sin(i/50*math.pi),-54+i*1.30,.8) for i in range(51)]
ribbon('Arrival promenade',arrival,4.0,paving)
for m,route in zip(modules[1:],routes):
    pts=route['points']
    ribbon(m['name']+' connected promenade',pts,3.2,paving)
    # Both river crossings have visible deck, piers and rails, not hovering paths.
    for i,p in enumerate(pts):
        if abs(p[0]-river_x(p[1]))>5.3: continue
        if i%4==0:
            rod(m['name']+' crossing piers',(p[0],p[1],p[2]-2.7),(p[0],p[1],p[2]-.1),.23,stone)
            for side in (-1,1):
                rod(m['name']+' bridge posts',(p[0],p[1]+side*1.65,p[2]),(p[0],p[1]+side*1.65,p[2]+1),.055,timber)
        if i and abs(pts[i-1][0]-river_x(pts[i-1][1]))<5.3:
            for side in (-1,1):
                rod(m['name']+' bridge rail',(pts[i-1][0],pts[i-1][1]+side*1.65,pts[i-1][2]+1),(p[0],p[1]+side*1.65,p[2]+1),.045,timber)

# Reception tree supports frame an unobstructed arrival; the desk is behind it.
for x,y in [(-7,12),(7,12),(-6,20),(6,20)]:
    rod('Reception branching columns',(x,y,.8),(x,y,4.7),.18,timber)
    for dx,dy in [(-2,-1.5),(2,-1.5),(-1.5,2),(1.5,2)]:
        rod('Reception branching columns',(x,y,4.5),(x+dx,y+dy,7),.11,timber)
box('Welcome desk',(0,21,1.75),(5.8,1.5,1.8),timber)

def label(text,c,size,mat=light):
    curve=bpy.data.curves.new(text,'FONT');curve.body=text;curve.size=size;curve.extrude=.002
    obj=bpy.data.objects.new(text,curve);bpy.context.collection.objects.link(obj)
    obj.location=c;obj.rotation_euler=(math.pi/2,0,0);obj.data.materials.append(mat)
label('Hengshi Design',(-3,7,5.8),.63,timber)
label('Prototype - no live staff',(-2.4,20.18,2.3),.25)
m=modules[1];x,y,z=m['x'],m['y'],m['z']
box('Department earthen display wall',(x,y+4, z+2.25),(12,.25,4.5),plaster)
box('Department evidence board',(x-.7,y+3.8,z+2.6),(8.7,.15,2.6),ink)
label('Strategy & Transformation',(x-4.6,y+3.70,z+3.25),.32)
label('Explore  |  Evidence  |  Conversation',(x-4.6,y+3.70,z+2.62),.27)
label('Prototype - no live staff',(x-4.6,y+3.70,z+1.9),.25)
rod('Consultation table',(x,y-1,z+.86),(x,y-1,z+1.04),1.55,timber,32)
rod('Consultation pedestal',(x,y-1,z),(x,y-1,z+.9),.19,timber)
for a in (.15,1.75,3.25,4.85):
    cx=x+2.25*math.cos(a);cy=y-1+2.25*math.sin(a)
    box('Consultation seat',(cx,cy,z+.54),(.8,.8,.13),plaster)
    box('Consultation back',(cx,cy+.34,z+.92),(.8,.13,.76),timber)
    for dx,dy in [(-.27,-.27),(.27,-.27),(-.27,.27),(.27,.27)]:
        rod('Chair legs',(cx+dx,cy+dy,z),(cx+dx,cy+dy,z+.5),.035,timber)

def near_path(x,y):
    return any((x-p[0])**2+(y-p[1])**2<10 for r in routes for p in r['points'][::5]) or (abs(x)<3 and -56<y<12)
for i in range(1350):
    x=random.uniform(-140,150);y=random.uniform(-85,245)
    if abs(x-river_x(y))<7 or near_path(x,y): continue
    if any(footprint(m,x,y)<2.9 for m in modules): continue
    z=land_z(x,y);h=random.uniform(5,14)
    rod('Forest trunks',(x,y,z),(x,y,z+h*.8),.13,timber,6)
    for j in range(6):
        a=j*math.tau/6
        crown('Forest canopy',(x+1.3*math.cos(a),y+1.3*math.sin(a),z+h+random.uniform(-1.3,1.3)),(random.uniform(1.8,2.8),random.uniform(1.8,2.8),2),random.choice(leaf),8,4)
# Near-field gardens make buildings part of the ground, with real planting scale.
for m in modules:
    for i in range(115):
        a=random.uniform(0,math.tau);px,py=point(m,a,random.uniform(1.17,1.48))
        if near_path(px,py) or abs(px-river_x(py))<5: continue
        crown('Garden understory',(px,py,m['z']+.45),(.8,.65,.6),random.choice(leaf),7,4)
for (name,matname),(vs,fs) in geo.items():
    data=bpy.data.meshes.new(name);data.from_pydata(vs,[],fs);data.update()
    obj=bpy.data.objects.new(name,data);bpy.context.collection.objects.link(obj)
    obj.data.materials.append(bpy.data.materials[matname])
    if any(s in name for s in ('canopy','planting','understory','boulders','valley','living roof')):
        for p in data.polygons: p.use_smooth=True
scene.world.use_nodes=True
scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.34,.44,.51,1)
scene.world.node_tree.nodes['Background'].inputs[1].default_value=.8
bpy.ops.object.light_add(type='SUN',location=(0,0,80))
bpy.context.object.rotation_euler=(.45,-.48,-.40);bpy.context.object.data.energy=2.3
bpy.ops.object.camera_add();camera=bpy.context.object;scene.camera=camera;camera.data.clip_end=1500
scene.render.engine='BLENDER_EEVEE';scene.render.resolution_x=1200;scene.render.resolution_y=800;scene.render.resolution_percentage=100
scene.view_settings.view_transform='AgX'
scene.view_settings.exposure=.6
views=[('overview',(62,-80,58),(5,22,3),44),('arrival',(0,-24,2.8),(0,16,4.4),30),('department',(-31,-10,2.7),(-28,1,3.2),24)]
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'nature-campus-layout.blend'))
bpy.ops.export_scene.gltf(filepath=str(OUT/'nature-campus-layout.glb'),export_format='GLB',export_cameras=False,export_lights=False)
receipt={'study':'v1','revision_cycle':3,'scale':'1 Blender unit = 1 m for this proposal; dimensions unaccepted',
         'modules':modules,'routes':routes,'views':views,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'blender_version':bpy.app.version_string,'mesh_groups':len(geo),'asset_rights':'Original procedural geometry; no external assets',
         'limits':['No movement, collision controller, streaming, audio or live staff','No production appearance or dimensions acceptance','Solid PBR materials, no realistic surface textures']}
(OUT/'layout-observations.json').write_text(json.dumps(receipt,indent=2),encoding='utf8')
print('LAYOUT_EXPORTED',len(geo),flush=True)
for name,pos,target,lens in views:
    camera.location=pos;camera.rotation_euler=(Vector(target)-camera.location).to_track_quat('-Z','Y').to_euler();camera.data.lens=lens
    scene.render.filepath=str(OUT/(name+'.png'));bpy.ops.render.render(write_still=True)
print('LAYOUT_COMPLETE',flush=True)
