import bpy,math,random
from mathutils import Vector
from pathlib import Path
out=Path(r'C:\Users\Zaryab\Documents\Hengshi Design\hengshi-design\artifacts\nature-campus-prototype')
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
random.seed(19)
def mat(name,c,rough=.7):
 m=bpy.data.materials.new(name);m.diffuse_color=(*c,1);m.use_nodes=True;p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*c,1);p.inputs['Roughness'].default_value=rough;return m
wood=mat('Warm timber',(.42,.23,.095));earth=mat('Earthen plaster',(.69,.60,.44));green=mat('Living roof',(.10,.22,.065));leaf=mat('Foliage',(.09,.20,.055));stone=mat('Path',(.59,.57,.46));water=mat('Water',(.08,.35,.36),.25);ink=mat('Display graphite',(.035,.055,.07));cyan=mat('Wayfinding cyan',(.02,.52,.62));glass=mat('Glazing',(.18,.34,.32),.2)
def box(name,loc,size,m):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=name;o.dimensions=size;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(m);return o
def cyl(name,loc,r,depth,m,verts=12):
 bpy.ops.mesh.primitive_cylinder_add(vertices=verts,radius=r,depth=depth,location=loc);o=bpy.context.object;o.name=name;o.data.materials.append(m);return o
def text(body,loc,size=.6,rot=(math.pi/2,0,0),m=ink):
 bpy.ops.object.text_add(location=loc,rotation=rot);o=bpy.context.object;o.data.body=body;o.data.size=size;o.data.extrude=.005;o.data.materials.append(m);return o
def ellipsoid(name,loc,size,m):
 bpy.ops.mesh.primitive_uv_sphere_add(segments=16,ring_count=8,location=loc);o=bpy.context.object;o.name=name;o.scale=size;o.data.materials.append(m)
 for poly in o.data.polygons: poly.use_smooth=True
 return o
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
 n=64;vs=[]
 # Multiple rings form a curved planted roof around a central skylight.
 for ring in range(6):
  r=.25+ring*.18
  for i in range(n):
   a=i*2*math.pi/n; shape=1+.13*math.sin(a*3+.4)
   z=5.3+.75*math.sin(a*2)+.65*math.sin((r-.25)/.9*math.pi)
   vs.append((x+rx*r*shape*math.cos(a),y+ry*r*shape*math.sin(a),z))
 faces=[(j*n+i,j*n+(i+1)%n,(j+1)*n+(i+1)%n,(j+1)*n+i) for j in range(5) for i in range(n)]
 mesh=bpy.data.meshes.new(name+' curved roof');mesh.from_pydata(vs,[],faces);mesh.update();o=bpy.data.objects.new(name+' planted roof',mesh);bpy.context.collection.objects.link(o);o.data.materials.append(green)
 for f in mesh.polygons:f.use_smooth=True
 def tube(label,points,radius,material):
  curve=bpy.data.curves.new(label,'CURVE');curve.dimensions='3D';curve.bevel_depth=radius;curve.bevel_resolution=2
  sp=curve.splines.new('POLY');sp.points.add(len(points)-1)
  for pt,co in zip(sp.points,points):pt.co=(*co,1)
  obj=bpy.data.objects.new(label,curve);bpy.context.collection.objects.link(obj);obj.data.materials.append(material)
 for ring in (.25,1.15):
  pts=[]
  for i in range(n+1):
   a=i*2*math.pi/n; shape=1+.13*math.sin(a*3+.4)
   pts.append((x+rx*ring*shape*math.cos(a),y+ry*ring*shape*math.sin(a),5.3+.75*math.sin(a*2)+(.2 if ring<.3 else 0)))
  tube(name+' timber roof rim',pts,.16,wood)
 for i in range(28):
  a=i*2*math.pi/28;shape=1+.13*math.sin(a*3+.4)
  px=x+rx*.96*shape*math.cos(a);py=y+ry*.96*shape*math.sin(a);height=5.2+.75*math.sin(a*2)
  # Keep front entrance and board sightline free of columns.
  if math.sin(a)<-.88:continue
  cyl(name+' timber column',(px,py,height/2),.11,height,wood)
  pts=[(x+rx*r*shape*math.cos(a),y+ry*r*shape*math.sin(a),5.15+.75*math.sin(a*2)+.65*math.sin((r-.25)/.9*math.pi)) for r in (.25,.45,.65,.85,1.05,1.15)]
  tube(name+' radial timber rib',pts,.09,wood)
 for i in range(65):
  a=random.uniform(0,math.tau);r=random.uniform(.42,1.05);shape=1+.13*math.sin(a*3+.4)
  z=5.35+.75*math.sin(a*2)+.65*math.sin((r-.25)/.9*math.pi)
  ellipsoid('Roof planting',(x+rx*r*shape*math.cos(a),y+ry*r*shape*math.sin(a),z),(.35,.3,.22),leaf)
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
box('Information board frame',(x-3,y+3.9,2.6),(7,.2,3.4),wood)
box('Information board',(x-3,y+3.72,2.6),(6.6,.08,3.05),ink)
text('Explore our services',(x-5.9,y+3.64,3.5),.4,m=earth)
text('Requirements | Evidence | Conversation',(x-5.9,y+3.64,2.8),.23,m=earth)
text('Visual prototype - no live staff',(x-5.9,y+3.64,2.1),.23,m=earth)
for i in range(3):box('Information card',(x-4.8+i*1.8,y+3.6,1.4),(1.4,.03,.6),cyan)
cyl('Consultation table',(x+1,y,1.05),1.6,.16,wood,32)
cyl('Table pedestal',(x+1,y,.55),.18,.95,wood)
for a in (0,math.pi/2,math.pi,math.pi*1.5):
 cx=x+1+2.2*math.cos(a);cy=y+2.2*math.sin(a)
 box('Seat',(cx,cy,.65),(.85,.85,.15),earth)
 back=box('Chair back',(cx,cy+.4,1.05),(.85,.13,.8),wood)
 for dx,dy in ((-.3,-.3),(.3,-.3),(-.3,.3),(.3,.3)):cyl('Chair leg',(cx+dx,cy+dy,.3),.06,.6,wood)
# Clustered varied canopies, shrubs and irregular mountain ridges.
foliage=[mat('Foliage variant '+str(i),c) for i,c in enumerate([(.08,.18,.04),(.16,.28,.07),(.23,.32,.10),(.07,.15,.07)])]
for i in range(240):
 tx=random.uniform(-72,72);ty=random.uniform(-68,72)
 if abs(tx)<36 and -50<ty<45:continue
 h=random.uniform(5,12);cyl('Tree trunk',(tx,ty,h*.42),.18,h*.84,wood)
 for j in range(5):
  a=j*math.tau/5;r=random.uniform(.8,1.8)
  ellipsoid('Layered tree canopy',(tx+r*math.cos(a),ty+r*math.sin(a),h+random.uniform(-1,1)),(2,1.8,2.2),random.choice(foliage))
for i in range(180):
 tx=random.uniform(-43,43);ty=random.uniform(-48,48)
 if abs(tx)<4:continue
 if any((tx-px)**2+(ty-py)**2<115 for px,py in [(0,0)]+wing_positions):continue
 ellipsoid('Landscape shrub',(tx,ty,.55),(.8,.7,.55),random.choice(foliage))
 if i%3==0:ellipsoid('River rock',(tx+1,ty,.3),(.8,.5,.4),stone)
# Organic distant topography, not individual cone peaks.
nx=44;ny=14;verts=[]
for j in range(ny):
 for i in range(nx):
  xx=-110+i*5;yy=72+j*5
  zz=3+22*abs(math.sin(i*.23+.7))+10*math.sin(i*.61+j*.31)**2+10*j/ny
  verts.append((xx,yy,zz))
faces=[(j*nx+i,j*nx+i+1,(j+1)*nx+i+1,(j+1)*nx+i) for j in range(ny-1) for i in range(nx-1)]
me=bpy.data.meshes.new('Mountain ridge');me.from_pydata(verts,[],faces);me.update();o=bpy.data.objects.new('Mountain ridge',me);bpy.context.collection.objects.link(o);o.data.materials.append(foliage[0])
for f in me.polygons:f.use_smooth=True
scene=bpy.context.scene;scene.world.color=(.55,.65,.75)
bpy.ops.object.light_add(type='SUN',location=(0,0,40));bpy.context.object.rotation_euler=(.45,-.5,-.6);bpy.context.object.data.energy=2.5
bpy.ops.object.camera_add();camera=bpy.context.object;scene.camera=camera;camera.data.clip_end=1000
scene.render.engine='BLENDER_EEVEE';scene.render.resolution_x=1200;scene.render.resolution_y=800;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
def view(name,location,target,lens=32):
 camera.location=location;camera.rotation_euler=(Vector(target)-camera.location).to_track_quat('-Z','Y').to_euler();camera.data.lens=lens;scene.render.filepath=str(out/(name+'.png'));bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=str(out/'nature-campus-refined.blend'))
view('01-campus-overview',(72,-90,67),(0,5,0),38)
view('02-arrival',(0,-28,2.2),(0,0,2.4),28)
view('03-department',(-24,-8,2.1),(-24,1,2),22)
bpy.ops.export_scene.gltf(filepath=str(out/'nature-campus.glb'),export_format='GLB',export_cameras=False,export_lights=False)
print('REFINED_PROTOTYPE_COMPLETE',flush=True)
