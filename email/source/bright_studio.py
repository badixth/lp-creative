from pathlib import Path
import bpy
O=Path(__file__).resolve().parents[1];P=O.parent
for name in ['rewards-platform','capacity-platform','spreads-tower']:
 bpy.ops.wm.open_mainfile(filepath=str(P/'email-layout-v23/source'/(name+'.blend')));s=bpy.context.scene
 for o in s.objects:
  if o.type!='LIGHT':continue
  factors={'Long cool softbox':1.25,'Silver edge strip':1.35,'Front readable silver':2.25,'Low silver face reflector':2.5,'Rear reflection':1.5,'Brand blue rim':1.7}
  o.data.energy*=factors.get(o.name,1)
  if o.name!='Brand blue rim':o.data.color=(1,1,1)
 for m in bpy.data.materials:
  if not m.node_tree:continue
  b=m.node_tree.nodes.get('Principled BSDF')
  if not b:continue
  nm=m.name
  if nm in ['V22 / deep blue anodised metal','Loyal Primus / enamel / sRGB #1D9BF0']:
   b.inputs['Base Color'].default_value=(.008,.24,.72,1);b.inputs['Metallic'].default_value=.55;b.inputs['Roughness'].default_value=.24
  if nm=='V22 / legible graphite candle faces':
   b.inputs['Base Color'].default_value=(.42,.47,.53,1);b.inputs['Roughness'].default_value=.25
  if nm=='V22 / black sapphire satin top':
   b.inputs['Base Color'].default_value=(.012,.04,.085,1);b.inputs['Roughness'].default_value=.29
  if nm=='V22 / sapphire to black tower':
   r=next((x for x in m.node_tree.nodes if x.type=='VALTORGB'),None)
   if r:r.color_ramp.elements[0].color=(.0015,.003,.006,1);r.color_ramp.elements[1].color=(.04,.12,.24,1)
  if nm=='V22 / graphite anodised metal':
   b.inputs['Base Color'].default_value=(.045,.065,.10,1);b.inputs['Roughness'].default_value=.32
 s.view_settings.exposure=.32
 ng=bpy.data.node_groups.new('V24 / luminous studio finish','CompositorNodeTree');s.compositing_node_group=ng;ng.interface.new_socket(name='Image',in_out='OUTPUT',socket_type='NodeSocketColor')
 rl=ng.nodes.new('CompositorNodeRLayers');sat=ng.nodes.new('CompositorNodeHueSat');sat.inputs['Saturation'].default_value=1.12;ng.links.new(rl.outputs['Image'],sat.inputs['Image'])
 bloom=ng.nodes.new('CompositorNodeGlare');bloom.inputs['Type'].default_value='Fog Glow';bloom.inputs['Quality'].default_value='High';bloom.inputs['Threshold'].default_value=2.4;bloom.inputs['Strength'].default_value=.16;bloom.inputs['Size'].default_value=.16;ng.links.new(sat.outputs['Image'],bloom.inputs['Image'])
 streak=ng.nodes.new('CompositorNodeGlare');streak.inputs['Type'].default_value='Streaks';streak.inputs['Quality'].default_value='High';streak.inputs['Threshold'].default_value=4.0;streak.inputs['Strength'].default_value=.08;streak.inputs['Streaks'].default_value=4;streak.inputs['Streaks Angle'].default_value=.35;streak.inputs['Fade'].default_value=.8;streak.inputs['Color Modulation'].default_value=0;ng.links.new(bloom.outputs['Image'],streak.inputs['Image'])
 alpha=ng.nodes.new('CompositorNodeSetAlpha');alpha.inputs['Type'].default_value='Replace Alpha';ng.links.new(streak.outputs['Image'],alpha.inputs['Image']);ng.links.new(rl.outputs['Alpha'],alpha.inputs['Alpha']);out=ng.nodes.new('NodeGroupOutput');ng.links.new(alpha.outputs['Image'],out.inputs['Image'])
 prefs=bpy.context.preferences.addons['cycles'].preferences;prefs.compute_device_type='METAL';prefs.get_devices()
 for d in prefs.devices:d.use=d.type=='METAL'
 s.cycles.device='GPU';s.cycles.samples=512;s.cycles.adaptive_threshold=.004;s.render.filepath=str(O/'assets'/(name+'.png'))
 s['revision']='v24 strong neutral studio fill, vivid sapphire materials, readable silver candles and brighter platform reflections, restrained HDR highlight glow and glare.'
 bpy.ops.wm.save_as_mainfile(filepath=str(O/'source'/(name+'.blend')));bpy.ops.render.render(write_still=True);print('CARD_DONE',name,flush=True)
