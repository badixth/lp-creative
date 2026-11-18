from pathlib import Path
import bpy,sys
O=Path(__file__).resolve().parents[1];P=O.parent
for name in ['rewards-platform','capacity-platform','spreads-tower']:
 if '--remaining' in sys.argv and name=='rewards-platform':continue
 bpy.ops.wm.open_mainfile(filepath=str(P/'email-layout-v22/source'/(name+'.blend')));s=bpy.context.scene
 # Lift broad neutral reflections on the objects while leaving the tower material gradient intact.
 for o in s.objects:
  if o.type!='LIGHT':continue
  factors={'Long cool softbox':1.23,'Silver edge strip':1.28,'Front readable silver':1.5,'Low silver face reflector':1.15}
  if name=='capacity-platform':factors={'Long cool softbox':1.42,'Silver edge strip':1.42,'Front readable silver':1.95,'Low silver face reflector':1.2}
  o.data.energy*=factors.get(o.name,1)
  if o.name!='Brand blue rim':o.data.color=(1,1,1)
 for mn,col,rough in [('V22 / satin machined aluminium',(.55,.58,.61,1),.29),('Premium / brushed palladium relief',(.53,.56,.59,1),.30),('V22 / legible graphite candle faces',(.19,.215,.25,1),.27)]:
  m=bpy.data.materials.get(mn)
  if m:
   bs=m.node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=col;bs.inputs['Roughness'].default_value=rough
 # Crisp silver top faces on the dark candles give a clean dimensional read at email size.
 if name=='capacity-platform':
  silver=bpy.data.materials.get('V22 / satin machined aluminium')
  if not silver:
   silver=bpy.data.materials.new('V23 / satin silver candle caps');silver.use_nodes=True;bs=silver.node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=(.55,.58,.61,1);bs.inputs['Metallic'].default_value=1;bs.inputs['Roughness'].default_value=.29
  for o in s.objects:
   if o.type=='MESH' and 'solid metal body' in o.name:
    o.data.materials.append(silver);i=len(o.data.materials)-1
    for poly in o.data.polygons:
     if poly.normal.z>.8:poly.material_index=i
 s['revision']='v23 lifted neutral white reflections and readable candle faces; v22 blue-black tower gradient, object placement and clean finish retained.'
 prefs=bpy.context.preferences.addons['cycles'].preferences;prefs.compute_device_type='METAL';prefs.get_devices()
 for d in prefs.devices:d.use=d.type=='METAL'
 s.cycles.device='GPU';s.cycles.samples=512;s.cycles.adaptive_threshold=.004;s.render.filepath=str(O/'assets'/(name+'.png'))
 bpy.ops.wm.save_as_mainfile(filepath=str(O/'source'/(name+'.blend')));bpy.ops.render.render(write_still=True);print('CARD_DONE',name,flush=True)
