from pathlib import Path
import bpy,sys
O=Path(__file__).resolve().parents[1];P=O.parent

def mat(name,color,metal,rough):
 m=bpy.data.materials.new(name);m.use_nodes=True;b=m.node_tree.nodes.get('Principled BSDF');b.inputs['Base Color'].default_value=(*color,1);b.inputs['Metallic'].default_value=metal;b.inputs['Roughness'].default_value=rough;return m

def assign(o,m):
 o.data.materials.clear();o.data.materials.append(m)

for name,w,h in [('rewards-platform',2400,2400),('capacity-platform',2400,1483),('spreads-tower',2400,1442)]:
 if '--capacity-only' in sys.argv and name!='capacity-platform':continue
 bpy.ops.wm.open_mainfile(filepath=str(P/'email-layout-v21/source'/(name+'.blend')));s=bpy.context.scene
 silver=mat('V22 / satin machined aluminium',(.46,.49,.52),1,.31)
 graphite=mat('V22 / graphite anodised metal',(.018,.024,.033),.88,.28)
 candle_graphite=mat('V22 / legible graphite candle faces',(.075,.09,.11),.88,.29)
 blue=mat('V22 / deep blue anodised metal',(.006,.092,.31),.72,.26)
 top=mat('V22 / black sapphire satin top',(.004,.012,.024),.82,.34)
 grid=mat('V22 / restrained etched grid',(.065,.095,.12),.6,.45)
 # World-height shader makes the ribbed tower fall naturally into black below the object.
 side=mat('V22 / sapphire to black tower',(.01,.025,.04),.85,.34)
 n=side.node_tree.nodes;l=side.node_tree.links;bs=n.get('Principled BSDF');geo=n.new('ShaderNodeNewGeometry');sep=n.new('ShaderNodeSeparateXYZ');l.new(geo.outputs['Position'],sep.inputs[0]);rng=n.new('ShaderNodeMapRange');rng.inputs['From Min'].default_value=-1.05;rng.inputs['From Max'].default_value=.53;l.new(sep.outputs['Z'],rng.inputs['Value']);ramp=n.new('ShaderNodeValToRGB');ramp.color_ramp.elements[0].color=(.0008,.0013,.0025,1);ramp.color_ramp.elements[1].color=(.018,.055,.105,1);l.new(rng.outputs['Result'],ramp.inputs[0]);l.new(ramp.outputs['Color'],bs.inputs['Base Color'])
 for m in bpy.data.materials:
  if not m.node_tree:continue
  b=m.node_tree.nodes.get('Principled BSDF')
  if not b:continue
  if m.name=='Feature / clear optical glass, real wall thickness':
   b.inputs['Roughness'].default_value=.055;b.inputs['IOR'].default_value=1.45
  elif m.name=='Palladium / polished edge':
   b.inputs['Base Color'].default_value=(.48,.51,.55,1);b.inputs['Roughness'].default_value=.24
  elif m.name=='Premium / brushed palladium relief':
   b.inputs['Base Color'].default_value=(.46,.49,.52,1);b.inputs['Roughness'].default_value=.34
  elif m.name=='Loyal Primus / enamel / sRGB #1D9BF0':
   b.inputs['Base Color'].default_value=(.005,.095,.34,1);b.inputs['Metallic'].default_value=.7;b.inputs['Roughness'].default_value=.28
 for o in s.objects:
  if o.type=='LIGHT':
   factors={'Long cool softbox':.92,'Silver edge strip':.80,'Front readable silver':.42,'Rear reflection':.48,'Low silver face reflector':.35,'Brand blue rim':1.4};o.data.energy*=factors.get(o.name,1)
   if o.name!='Brand blue rim':o.data.color=(1,1,1)
  if o.type not in ['MESH','CURVE','FONT']:continue
  nm=o.name.lower()
  if ('tower' in nm and ('rib' in nm or 'front' in nm or 'face' in nm or 'core' in nm)):assign(o,side)
  if ('tower' in nm and ('/ top' in nm or 'machined top' in nm)):assign(o,top)
  if 'fine price graduations' in nm or 'loyal primus hallmark' in nm or 'inset silver plaque' in nm:o.hide_render=True
  if 'token / fine rim reeding' in nm:
   idx=int(o.name.rsplit('.',1)[1]) if '.' in o.name else 0
   if idx%2:o.hide_render=True
  if o.name=='Gift / palladium lid':assign(o,silver)
  if o.name=='Gift / thick front and back wall.001':assign(o,graphite)
  if 'polished inset face' in nm:o.hide_render=True
  if 'solid metal body' in nm:
   idx=int(o.name.split()[1]);assign(o,blue if idx in [1,4] else candle_graphite)
  if 'etched' in nm:
   assign(o,grid)
   if o.name.endswith(('.001','.003')):o.hide_render=True
  if 'blue lower register' in nm:o.hide_render=True
  if o.name.startswith('Ask / solid'):assign(o,silver)
  if o.name.startswith('Bid / solid'):assign(o,blue)
  if 'drifting confetti' in nm and o.name.endswith(('01','04','08')):o.hide_render=True
 s.view_settings.exposure=.05
 # Direct render output: realistic highlights, no streaks or added bloom.
 ng=bpy.data.node_groups.new('V22 / clean photographic finish','CompositorNodeTree');s.compositing_node_group=ng;ng.interface.new_socket(name='Image',in_out='OUTPUT',socket_type='NodeSocketColor');rl=ng.nodes.new('CompositorNodeRLayers');out=ng.nodes.new('NodeGroupOutput');ng.links.new(rl.outputs['Image'],out.inputs['Image'])
 prefs=bpy.context.preferences.addons['cycles'].preferences;prefs.compute_device_type='METAL';prefs.get_devices()
 for d in prefs.devices:d.use=d.type=='METAL'
 s.cycles.device='GPU';s.cycles.samples=512;s.cycles.adaptive_threshold=.004;s.cycles.use_denoising=True;s.cycles.max_bounces=16;s.cycles.transmission_bounces=12
 s.render.resolution_x=w;s.render.resolution_y=h;s.render.resolution_percentage=100;s.render.film_transparent=True;s.render.image_settings.file_format='PNG';s.render.image_settings.color_mode='RGBA';s.render.image_settings.color_depth='8';s.render.filepath=str(O/'assets'/(name+'.png'))
 s['revision']='v22 material and geometry cleanup: distinct satin silver, graphite and blue anodised metal; simplified microdetail; directional neutral lighting; world-height sapphire-black tower shader; no artificial glare.'
 bpy.ops.wm.save_as_mainfile(filepath=str(O/'source'/(name+'.blend')));bpy.ops.render.render(write_still=True);print('CARD_DONE',name,flush=True)
