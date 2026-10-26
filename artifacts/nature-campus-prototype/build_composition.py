import bpy,math,random
from mathutils import Vector
from pathlib import Path
random.seed(47)
out=Path(r'C:\Users\Zaryab\Documents\Hengshi Design\hengshi-design\artifacts\nature-campus-prototype')
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
def material(name,c,rough=.75):
 m=bpy.data.materials.new(name);m.diffuse_color=(*c,1);m.use_nodes=True;p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*c,1);p.inputs['Roughness'].default_value=rough;return m
wood=material('Honey timber',(.48,.29,.13));stone=material('Warm paving',(.64,.61,.51));green=material('Roof meadow',(.18,.29,.10));grass=material('Valley meadow',(.22,.31,.13));leaf=material('Forest green',(.08,.19,.06));leaf2=material('Sunlit leaves',(.20,.29,.08));rock=material('River stone',(.33,.36,.29));water=material('River',(.06,.33,.35),.18);dark=material('Information display',(.025,.04,.045));plaster=material('Earth plaster',(.67,.56,.38));glass=material('Tinted glazing',(.22,.37,.34),.12)
gp=glass.node_tree.nodes.get('Principled BSDF');gp.inputs['Transmission Weight'].default_value=.65;gp.inputs['IOR'].default_value=1.45
buckets={}
def addgeo(name,verts,faces,mat):
 key=(name,mat.name);v,f=buckets.setdefault(key,([],[]));off=len(v);v.extend(verts);f.extend(tuple(off+i for i in face) for face in faces)
def box(name,c,size,mat):
 x,y,z=c;a,b,h=[k/2 for k in size];v=[(x+dx*a,y+dy*b,z+dz*h) for dx,dy,dz in [(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]];addgeo(name,v,[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)],mat)
def rod(name,a,b,r,mat,n=8):
 a=Vector(a);b=Vector(b);d=(b-a).normalized();u=d.cross(Vector((0,0,1)))
 if u.length<.01:u=d.cross(Vector((0,1,0)))
 u.normalize();w=d.cross(u);verts=[tuple(c+r*(math.cos(i*math.tau/n)*u+math.sin(i*math.tau/n)*w)) for c in (a,b) for i in range(n)];faces=[tuple(range(n-1,-1,-1)),tuple(range(n,n*2))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)];addgeo(name,verts,faces,mat)
def blob(name,c,size,mat,n=10,rings=7):
 verts=[]
 for j in range(rings+1):
  a=math.pi*j/rings
  for i in range(n):
   t=math.tau*i/n;verts.append((c[0]+size[0]*math.sin(a)*math.cos(t),c[1]+size[1]*math.sin(a)*math.sin(t),c[2]+size[2]*math.cos(a)))
 faces=[(j*n+i,j*n+(i+1)%n,(j+1)*n+(i+1)%n,(j+1)*n+i) for j in range(rings) for i in range(n)];addgeo(name,verts,faces,mat)
def riverx(y):return 20+7*math.sin(y*.035)+4*math.sin(y*.09)
def terrainz(x,y):
 if -54<x<48 and -35<y<62:return -.12
 distance=max(abs(x)-44,y-62,-y-50,0)
 hill=distance*.10+max(y-65,0)*.14
 return -.12+hill*(.7+.4*math.sin(x*.045+y*.024)+.26*math.cos(x*.08-y*.045))
# Continuous valley topography reaches far beyond campus, with a river depression.
N=100;verts=[]
for j in range(N):
 y=-95+j*3.8
 for i in range(N):
  x=-145+i*3;z=terrainz(x,y)
  if abs(x-riverx(y))<5:z-=1.2
  verts.append((x,y,z))
faces=[(j*N+i,j*N+i+1,(j+1)*N+i+1,(j+1)*N+i) for j in range(N-1) for i in range(N-1)];addgeo('Continuous sculpted valley',verts,faces,grass)
# River ribbons, rock edges; no repeated ellipse puddles.
verts=[]
for i in range(110):
 y=-90+i*3.1;x=riverx(y);z=max(-.38,terrainz(x,y)-.7)
 verts.extend([(x-3.6,y,z),(x+3.6,y,z)])
addgeo('Flowing valley river',verts,[(i*2,i*2+1,i*2+3,i*2+2) for i in range(109)],water)
for i in range(95):
 y=random.uniform(-75,210);x=riverx(y)+random.choice((-1,1))*random.uniform(4,6);z=terrainz(x,y)
 blob('River stones',(x,y,z+.35),(random.uniform(.6,1.4),random.uniform(.5,1.2),.6),rock)
# Shaped central plaza and varied organic wings: an actual architectural hierarchy.
modules=[('Reception',-3,12,15,11,7.2,0),('Strategy & Transformation',-29,-5,12,8,5.1,-.3),('Digital Products & Growth',-32,27,14,9,5.5,.4),('AI, Data & Automation',-6,49,13,9,6,.1),('Immersive & Creative',28,39,14,8,5.6,-.45),('Cloud, Reliability & Trust',36,-3,13,9,5.3,.3)]
def contour(a,rx,ry,angle):
 r=1+.17*math.cos(a*2+.6)+.09*math.sin(a*3)
 px=rx*r*math.cos(a);py=ry*r*math.sin(a)
 return px*math.cos(angle)-py*math.sin(angle),px*math.sin(angle)+py*math.cos(angle)
for name,x,y,rx,ry,h,angle in modules:
 n=72;roof=[];floor=[]
 for scale in (.24,.4,.65,.9,1.12):
  for i in range(n):
   a=i*math.tau/n;dx,dy=contour(a,rx,ry,angle);z=h+1.0*math.sin(a*2+.5)+.5*math.sin(scale*math.pi)
   roof.append((x+dx*scale,y+dy*scale,z))
 faces=[(j*n+i,j*n+(i+1)%n,(j+1)*n+(i+1)%n,(j+1)*n+i) for j in range(4) for i in range(n)];addgeo(name+' curved living roof',roof,faces,green)
 for i in range(n):
  a=i*math.tau/n;dx,dy=contour(a,rx,ry,angle);floor.append((x+dx,y+dy,.12))
 addgeo(name+' terrace',floor,[tuple(range(n))],stone)
 # Glazing broken by a wide front entrance, with elegant timber mullions.
 for i in range(36):
  a=i*math.tau/36;a2=(i+1)*math.tau/36;dx,dy=contour(a,rx*.93,ry*.93,angle);ex,ey=contour(a2,rx*.93,ry*.93,angle);z=h+.9*math.sin(a*2+.5)
  if dy<-ry*.72:continue
  rod('Timber columns',(x+dx,y+dy,.12),(x+dx,y+dy,z),.095,wood)
  addgeo(name+' glazing',[(x+dx,y+dy,.25),(x+ex,y+ey,.25),(x+ex,y+ey,z-.2),(x+dx,y+dy,z-.2)],[(0,1,2,3)],glass)
 for scale in (.24,1.12):
  for i in range(n):
   a=i*math.tau/n;b=(i+1)*math.tau/n;dx,dy=contour(a,rx,ry,angle);ex,ey=contour(b,rx,ry,angle)
   rod('Sculpted timber roof edge',(x+dx*scale,y+dy*scale,h+math.sin(a*2+.5)+.5*math.sin(scale*math.pi)),(x+ex*scale,y+ey*scale,h+math.sin(b*2+.5)+.5*math.sin(scale*math.pi)),.16,wood)
 for i in range(24):
  a=i*math.tau/24;dx,dy=contour(a,rx,ry,angle)
  for r,r2 in ((.24,.45),(.45,.7),(.7,.95),(.95,1.12)):
   rod('Branching roof structure',(x+dx*r,y+dy*r,h-.18+math.sin(a*2+.5)+.5*math.sin(r*math.pi)),(x+dx*r2,y+dy*r2,h-.18+math.sin(a*2+.5)+.5*math.sin(r2*math.pi)),.08,wood)
 for i in range(95):
  a=random.uniform(0,math.tau);r=random.uniform(.4,1.05);dx,dy=contour(a,rx,ry,angle);z=h+math.sin(a*2+.5)+.5*math.sin(r*math.pi)
  blob('Roof meadow clusters',(x+dx*r,y+dy*r,z+.1),(.55,.45,.18),random.choice((green,leaf2)),8,4)
# Broad arrival leads directly into central reception; gently sweeping garden connectors.
box('Arrival promenade',(-3,-20,.08),(5,44,.18),stone)
for name,x,y,*_ in modules[1:]:
 start=Vector((-3,12,.09));end=Vector((x,y,.09));d=end-start;side=Vector((-d.y,d.x,0)).normalized()*1.6;v=[]
 for i in range(21):
  t=i/20;c=start+d*t+Vector((math.sin(t*math.pi)*2,0,0));v.extend([tuple(c-side),tuple(c+side)])
 addgeo('Curved connecting promenade',v,[(i*2,i*2+1,i*2+3,i*2+2) for i in range(20)],stone)
# Reception and representative department: real architectural space.
box('Welcome desk',(-3,14,1.1),(6,1.4,1.8),wood)
x,y=-29,-5
box('Department rear wall',(x,y+4.8,2.4),(11,.2,4.6),plaster)
box('Information display',(x-1,y+4.6,2.6),(7,.1,2.6),dark)
def text(label,pos,size,mat):
 curve=bpy.data.curves.new(label,'FONT');curve.body=label;curve.size=size;curve.extrude=.003;o=bpy.data.objects.new(label,curve);bpy.context.collection.objects.link(o);o.location=pos;o.rotation_euler=(math.pi/2,0,0);o.data.materials.append(mat)
text('Hengshi Design',(-7,3,4.8),.75,wood)
text('Explore | Evidence | Conversation',(x-4,y+4.52,3.2),.34,stone)
text('Prototype - no live staff',(x-4,y+4.52,2.5),.25,stone)
for i in range(3):box('Information card',(x-3+i*2,y+4.5,1.85),(1.65,.02,.6),stone)
rod('Consultation tabletop',(x+1,y,1),(x+1,y,1.18),1.7,wood,32);rod('Table pedestal',(x+1,y,.2),(x+1,y,1),.18,wood)
for a in (0,math.pi/2,math.pi,math.pi*1.5):
 cx=x+1+2.4*math.cos(a);cy=y+2.4*math.sin(a);box('Chair seat',(cx,cy,.65),(.85,.85,.15),stone);box('Chair back',(cx,cy+.38,1.05),(.85,.12,.85),wood)
 for dx,dy in ((-.3,-.3),(.3,-.3),(-.3,.3),(.3,.3)):rod('Chair legs',(cx+dx,cy+dy,.1),(cx+dx,cy+dy,.6),.05,wood)
# Forest clusters distributed throughout actual terrain depth, avoiding buildings and paths.
for i in range(440):
 x=random.uniform(-100,110);y=random.uniform(-72,230)
 if abs(x-riverx(y))<7:continue
 if -7<x<1 and -46<y<17:continue
 if any(((x-mx)/rx)**2+((y-my)/ry)**2<1.75 for _,mx,my,rx,ry,*_ in modules):continue
 if -45<x<50 and -25<y<62 and random.random()<.8:continue
 z=terrainz(x,y);h=random.uniform(5,12);rod('Forest trunks',(x,y,z),(x,y,z+h*.85),.18,wood)
 for j in range(5):
  a=j*math.tau/5;radius=random.uniform(.5,1.8)
  blob('Layered forest foliage',(x+radius*math.cos(a),y+radius*math.sin(a),z+h+random.uniform(-1.3,1)),(2.1,1.8,2),random.choice((leaf,leaf2)),10,6)
# Low planting beds flank the promenade rather than scattering everywhere.
for side in (-1,1):
 for j in range(38):
  yy=-40+j*1.2;xx=-3+side*random.uniform(3.4,6.5)
  blob('Arrival garden', (xx,yy,.45),(.6,.55,.5),random.choice((leaf,leaf2)),8,5)
# Build only a few dozen batched meshes, avoiding thousands of separate objects.
for (name,matname),(v,f) in buckets.items():
 me=bpy.data.meshes.new(name);me.from_pydata(v,[],f);me.update();o=bpy.data.objects.new(name,me);bpy.context.collection.objects.link(o);o.data.materials.append(bpy.data.materials[matname])
 if any(token in name.lower() for token in ('foliage','valley','roof','meadow','garden','river stones')):
  for p in me.polygons:p.use_smooth=True
scene=bpy.context.scene;scene.world.color=(.4,.5,.6)
bpy.ops.object.light_add(type='SUN',location=(0,0,60));bpy.context.object.rotation_euler=(.5,-.6,-.45);bpy.context.object.data.energy=3
bpy.ops.object.camera_add();cam=bpy.context.object;scene.camera=cam;cam.data.clip_end=1500
scene.render.engine='BLENDER_EEVEE';scene.render.resolution_x=1200;scene.render.resolution_y=800;scene.render.resolution_percentage=100
bpy.ops.wm.save_as_mainfile(filepath=str(out/'nature-campus-composition.blend'))
# Export before renders so the interactive viewer is available first.
bpy.ops.export_scene.gltf(filepath=str(out/'nature-campus.glb'),export_format='GLB',export_cameras=False,export_lights=False)
print('COMPOSITION_EXPORTED',len(buckets),flush=True)
for name,pos,target,lens in [('01-campus-overview',(89,-107,79),(0,16,1),42),('02-arrival',(-3,-26,2.3),(-3,12,3),28),('03-department',(-28,-10,2.2),(-29,1,2.6),24)]:
 cam.location=pos;cam.rotation_euler=(Vector(target)-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.lens=lens;scene.render.filepath=str(out/(name+'.png'));bpy.ops.render.render(write_still=True)
print('COMPOSITION_COMPLETE',flush=True)
