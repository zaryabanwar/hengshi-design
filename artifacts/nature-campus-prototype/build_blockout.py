import bpy,math,random
from mathutils import Vector
from pathlib import Path
out=Path(r'C:\Users\Zaryab\Documents\Hengshi Design\hengshi-design\artifacts\nature-campus-prototype')
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
random.seed(19)
def mat(name,c,rough=.7):
 m=bpy.data.materials.new(name);m.diffuse_color=(*c,1);m.use_nodes=True;p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*c,1);p.inputs['Roughness'].default_value=rough;return m
wood=mat('Warm timber',(.42,.23,.095));earth=mat('Earthen plaster',(.69,.60,.44));green=mat('Living roof',(.19,.32,.11));leaf=mat('Foliage',(.12,.25,.09));stone=mat('Path',(.59,.57,.46));water=mat('Water',(.08,.35,.36),.25);ink=mat('Display graphite',(.035,.055,.07));cyan=mat('Wayfinding cyan',(.02,.52,.62));glass=mat('Glazing',(.18,.34,.32),.2)
def box(name,loc,size,m):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=name;o.dimensions=size;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(m);return o
def cyl(name,loc,r,depth,m,verts=12):
 bpy.ops.mesh.primitive_cylinder_add(vertices=verts,radius=r,depth=depth,location=loc);o=bpy.context.object;o.name=name;o.data.materials.append(m);return o
def text(body,loc,size=.6,rot=(math.pi/2,0,0),m=ink):
 bpy.ops.object.text_add(location=loc,rotation=rot);o=bpy.context.object;o.data.body=body;o.data.size=size;o.data.extrude=.005;o.data.materials.append(m);return o
def ellipsoid(name,loc,size,m):
 bpy.ops.mesh.primitive_uv_sphere_add(segments=16,ring_count=8,location=loc);o=bpy.context.object;o.name=name;o.scale=size;o.data.materials.append(m);return o
# Broad level visitor zone; landscape beyond it.
box('Terrain',(0,0,-.55),(150,150,1),green)
box('Arrival path',(0,-30,.03),(5,45,.13),stone)
# Stream to side of arrival, decorative only.
for j in range(20):
 y=-65+j*5;x=21+math.sin(j*.65)*6
 ellipsoid('Stream section',(x,y,.03),(5,4,.12),water)
# Pavilion geometry with gently undulating roof edge.
def pavilion(name,x,y,rx=9,ry=7):
 cyl(name+' floor',(x,y,.2),1,.4,stone,48).scale=(rx,ry,1)
 n=48;vs=[]
 for z in (4.9,5.25):
  for i in range(n):
   a=i*2*math.pi/n;vs.append((x+rx*1.1*math.cos(a),y+ry*1.1*math.sin(a),z+.45*math.sin(a*2)))
 faces=[tuple(range(n-1,-1,-1)),tuple(range(n,2*n))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)]
 mesh=bpy.data.meshes.new(name+' roof');mesh.from_pydata(vs,[],faces);mesh.update();o=bpy.data.objects.new(name+' living roof',mesh);bpy.context.collection.objects.link(o);o.data.materials.append(green)
 for i in range(20):
  a=i*2*math.pi/20;cyl(name+' timber column',(x+rx*.94*math.cos(a),y+ry*.94*math.sin(a),2.55),.13,4.7,wood)
 # Rear wall only: open fronts for legible blockout circulation.
 box(name+' rear wall',(x,y+ry*.85,2.4),(rx*1.3,.2,4),earth)
 return x,y
pavilion('Reception',0,0,11,9)
wing_positions=[(-24,-3),(-22,22),(0,30),(22,22),(24,-3)]
names=['Strategy & Transformation','Digital Products & Growth','AI, Data & Automation','Immersive & Creative','Cloud, Reliability & Trust']
for (x,y),name in zip(wing_positions,names):
 pavilion(name,x,y)
 # straight connector between reception and wing
 d=Vector((x,y,0));mid=d*.5;o=box('Accessible connector',(mid.x,mid.y,.04),(3,d.length,.14),stone);o.rotation_euler.z=-math.atan2(x,y)
 text(name,(x-7,y-6.8,1.1),.38)
# Reception furniture and sign
box('Reception desk',(0,1,1),(5,1.2,1.6),wood);text('Hengshi Design',(-4,-7.5,3.8),.75,m=earth)
# Representative department interior (Strategy front left)
x,y=wing_positions[0]
box('Information board frame',(x-3,y+5.5,2.6),(7,.2,3.4),wood)
box('Information board',(x-3,y+5.32,2.6),(6.6,.08,3.05),ink)
text('Explore our services',(x-5.9,y+5.24,3.5),.4,m=earth)
text('Requirements | Evidence | Conversation',(x-5.9,y+5.24,2.8),.23,m=earth)
text('Visual prototype - no live staff',(x-5.9,y+5.24,2.1),.23,m=earth)
for i in range(3):box('Information card',(x-4.8+i*1.8,y+5.2,1.4),(1.4,.03,.6),cyan)
cyl('Consultation table',(x+1,y,1.05),1.6,.16,wood,32)
cyl('Table pedestal',(x+1,y,.55),.18,.95,wood)
for a in (0,math.pi/2,math.pi,math.pi*1.5):
 cx=x+1+2.2*math.cos(a);cy=y+2.2*math.sin(a)
 box('Seat',(cx,cy,.65),(.85,.85,.15),earth)
 for dx,dy in ((-.3,-.3),(.3,-.3),(-.3,.3),(.3,.3)):cyl('Chair leg',(cx+dx,cy+dy,.3),.06,.6,wood)
# Reusable low-poly plants, clear campus circulation.
for i in range(150):
 tx=random.uniform(-68,68);ty=random.uniform(-65,65)
 if abs(tx)<36 and -50<ty<45:continue
 h=random.uniform(5,11);cyl('Tree trunk',(tx,ty,h*.4),.25,h*.8,wood)
 ellipsoid('Tree canopy',(tx,ty,h), (random.uniform(2,4),random.uniform(2,4),random.uniform(2.5,4.5)),leaf)
for i in range(65):
 tx=random.uniform(-40,40);ty=random.uniform(-35,45)
 if abs(tx)<4:continue
 if any((tx-px)**2+(ty-py)**2<120 for px,py in [(0,0)]+wing_positions):continue
 ellipsoid('Shrub',(tx,ty,.7),(1.2,1,.7),leaf)
for i in range(9):
 bpy.ops.mesh.primitive_cone_add(vertices=10,radius1=random.uniform(18,28),radius2=2,depth=random.uniform(25,40),location=(-80+i*20,85,12));bpy.context.object.name='Distant mountain';bpy.context.object.data.materials.append(green)
scene=bpy.context.scene;scene.world.color=(.55,.65,.75)
bpy.ops.object.light_add(type='SUN',location=(0,0,40));bpy.context.object.rotation_euler=(.45,-.5,-.6);bpy.context.object.data.energy=2.5
bpy.ops.object.camera_add();camera=bpy.context.object;scene.camera=camera;camera.data.clip_end=1000
scene.render.engine='BLENDER_EEVEE';scene.render.resolution_x=1200;scene.render.resolution_y=800;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
def view(name,location,target,lens=32):
 camera.location=location;camera.rotation_euler=(Vector(target)-camera.location).to_track_quat('-Z','Y').to_euler();camera.data.lens=lens;scene.render.filepath=str(out/(name+'.png'));bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=str(out/'nature-campus-blockout.blend'))
view('01-campus-overview',(72,-90,67),(0,5,0),38)
view('02-arrival',(0,-28,2.2),(0,0,2.4),28)
view('03-department',(-24,-8,2.1),(-24,1,2),22)
print('PROTOTYPE_COMPLETE',flush=True)
