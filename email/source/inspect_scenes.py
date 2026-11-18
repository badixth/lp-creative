import bpy,json
from pathlib import Path
P=Path(__file__).resolve().parents[2]
for name in ['rewards-platform','capacity-platform','spreads-tower']:
 bpy.ops.wm.open_mainfile(filepath=str(P/'email-layout-v21/source'/(name+'.blend')))
 mats=[]
 for m in bpy.data.materials:
  bs=m.node_tree.nodes.get('Principled BSDF') if m.node_tree else None
  if bs:mats.append({'name':m.name,'color':list(bs.inputs['Base Color'].default_value),'metal':bs.inputs['Metallic'].default_value,'rough':bs.inputs['Roughness'].default_value,'transmission':bs.inputs['Transmission Weight'].default_value})
 objs=[{'name':o.name,'type':o.type,'location':list(o.location),'dimensions':list(o.dimensions),'materials':[m.name for m in o.data.materials] if o.type in ['MESH','FONT','CURVE'] else [],'hidden':o.hide_render} for o in bpy.context.scene.objects]
 lights=[{'name':o.name,'energy':o.data.energy,'color':list(o.data.color),'size':getattr(o.data,'size',0)} for o in bpy.context.scene.objects if o.type=='LIGHT']
 (P/'email-layout-v22/review'/(name+'-inspection.json')).write_text(json.dumps({'materials':mats,'objects':objs,'lights':lights},indent=2))
 print(name,'materials',mats,'lights',lights,flush=True)
