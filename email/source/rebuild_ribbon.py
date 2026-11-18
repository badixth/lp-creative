from pathlib import Path
import bpy,math
from mathutils import Vector
O=Path(__file__).resolve().parents[1];P=O.parent
bpy.ops.wm.open_mainfile(filepath=str(P/'email-layout-v25/source/rewards-platform.blend'));s=bpy.context.scene
blue=bpy.data.materials['Loyal Primus / enamel / sRGB #1D9BF0']
for o in list(s.objects):
 if any(t in o.name for t in ['blue vertical ribbon','lid ribbon','Gift bow /','Bow / polished','silver bow clasp']):bpy.data.objects.remove(o,do_unlink=True)

def sheet(name,rows,closed=False):
 verts=[tuple(v) for row in rows for v in row];faces=[];N=len(rows)
 for i in range(N if closed else N-1):
  j=(i+1)%N;faces.append((2*i,2*i+1,2*j+1,2*j))
 me=bpy.data.meshes.new(name);me.from_pydata(verts,[],faces);me.update();ob=bpy.data.objects.new(name,me);s.collection.objects.link(ob);me.materials.append(blue)
 for f in me.polygons:f.use_smooth=True
 so=ob.modifiers.new('Continuous ribbon thickness','SOLIDIFY');so.thickness=.014;so.offset=0
 be=ob.modifiers.new('Soft finished edges','BEVEL');be.width=.005;be.segments=3
 return ob

def rounded_profile(points,r=.035):
 pts=[Vector(p) for p in points];out=[]
 for i,b in enumerate(pts):
  a=pts[i-1];c=pts[(i+1)%len(pts)];d=min(r,(a-b).length*.25,(c-b).length*.25)
  u=b+(a-b).normalized()*d;v=b+(c-b).normalized()*d
  for j in range(9):
   t=j/8;out.append((1-t)**2*u+2*t*(1-t)*b+t*t*v)
 return out
# Two complete closed bands follow the lid overhang, step inward to the glass walls,
# wrap under the base and return. No separate disconnected side strips.
p=rounded_profile([(-.75,2.496),(1.11,2.496),(1.11,2.31),(1.045,2.27),(1.045,.565),(-.681,.565),(-.681,2.27),(-.75,2.31)])
sheet('Ribbon / continuous front-to-back wrap',[[(-.155,y,z),(.155,y,z)] for y,z in p],True)
p=rounded_profile([(-1.072,2.514),(1.072,2.514),(1.072,2.31),(1.009,2.27),(1.009,.551),(-1.009,.551),(-1.009,2.27),(-1.072,2.31)])
sheet('Ribbon / continuous side-to-side wrap',[[(x,.035,z),(x,.325,z)] for x,z in p],True)

def bez(a,b,c,d,t):return (1-t)**3*a+3*(1-t)**2*t*b+3*(1-t)*t*t*c+t**3*d
for sign in [-1,1]:
 cps=[(-.065,.15,2.65),(-.22,.18,3.03),(-.96,.24,3.40),(-.91,.21,3.03),(-.84,.18,2.74),(-.24,.11,2.56),(-.06,.11,2.61)]
 cps=[Vector((x*sign,y,z)) for x,y,z in cps];rows=[]
 for j in range(161):
  u=j/160;t=u*2 if u<=.5 else (u-.5)*2
  pos=bez(*cps[:4],t) if u<=.5 else bez(*cps[3:],t)
  width=.18+.12*math.sin(math.pi*u)
  axis=Vector((.08*sign*math.sin(math.pi*u),1,.12*math.sin(2*math.pi*u))).normalized()
  rows.append([pos-axis*width/2,pos+axis*width/2])
 sheet('Ribbon / left tied loop' if sign==1 else 'Ribbon / right tied loop',rows)
 # Two short curved tails emerge beneath the knot and rest on the lid.
 cps=[Vector((.04*sign,.10,2.60)),Vector((.16*sign,-.04,2.55)),Vector((.30*sign,-.22,2.535)),Vector((.48*sign,-.42,2.535))];rows=[]
 for j in range(61):
  t=j/60;pos=bez(*cps,t);axis=Vector((.77,.64*sign,0));w=.20+.015*t;rows.append([pos-axis*w/2,pos+axis*w/2])
 sheet('Ribbon / laid tail '+str(sign),rows)
bpy.ops.mesh.primitive_cube_add(size=1,location=(0,.14,2.647));k=bpy.context.object;k.name='Ribbon / rounded central knot';k.scale=(.32,.34,.205);bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);k.data.materials.append(blue);m=k.modifiers.new('Soft tied knot corners','BEVEL');m.width=.085;m.segments=8;k.modifiers.new('Weighted knot normals','WEIGHTED_NORMAL')
for f in k.data.polygons:f.use_smooth=True
prefs=bpy.context.preferences.addons['cycles'].preferences;prefs.compute_device_type='METAL';prefs.get_devices()
for d in prefs.devices:d.use=d.type=='METAL'
s.cycles.device='GPU';s.cycles.samples=512;s.cycles.adaptive_threshold=.004;s.render.filepath=str(O/'assets/rewards-platform.png');s['revision']='v26 rebuilt complete ribbon: two continuous closed wrapping bands with lid-overhang transitions, connected formed loops, central rounded knot and two laid tails. v24 lighting retained.'
bpy.ops.wm.save_as_mainfile(filepath=str(O/'source/rewards-platform.blend'));bpy.ops.render.render(write_still=True);print('RIBBON_DONE',flush=True)
