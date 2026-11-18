from pathlib import Path
import bpy, math
from mathutils import Vector
O=Path(__file__).resolve().parents[1];P=O.parent
bpy.ops.wm.open_mainfile(filepath=str(P/'email-layout-v17/source/hero-background.blend'))
s=bpy.context.scene
# Brighten the reflective materials, preserving dark glass and recessed details.
updates={
 'Palladium / polished edge':((.52,.58,.65,1),.19),
 'Premium / machined silver edges':((.52,.58,.65,1),.19),
 'Premium / satin palladium':((.36,.40,.46,1),.29),
 'Premium / brushed palladium relief':((.70,.76,.82,1),.22),
 'Premium / satin graphite':((.15,.17,.21,1),.33),
 'Premium / machined champagne gold':((.86,.53,.16,1),.20),
 'Premium / pale champagne relief':((.90,.64,.26,1),.22),
 'Premium / satin champagne gold':((.68,.39,.10,1),.29),
}
for name,(color,roughness) in updates.items():
 bs=bpy.data.materials[name].node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=color;bs.inputs['Roughness'].default_value=roughness
bs=bpy.data.materials['Rail / cyan light'].node_tree.nodes.get('Principled BSDF');bs.inputs['Emission Strength'].default_value=2.2
for name,power in [('Front readable silver',1400),('Long cool softbox',2000),('Hero / broad neutral fill',750),('Hero / white rear softbox',1350)]:bpy.data.objects[name].data.energy=power
bpy.ops.object.light_add(type='AREA',location=(1,-5,6));strip=bpy.context.object;strip.name='Hero / crisp reflection strip';strip.data.energy=650;strip.data.color=(.94,.97,1);strip.data.shape='RECTANGLE';strip.data.size=.45;strip.data.size_y=4.0;strip.rotation_euler=(Vector((0,0,1.8))-strip.location).to_track_quat('-Z','Y').to_euler()
s.view_settings.exposure=.20
# Native HDR finishing: restrained bloom and small optical streaks only on highlights.
ng=bpy.data.node_groups.new('Hero / production highlight finish','CompositorNodeTree');s.compositing_node_group=ng
ng.interface.new_socket(name='Image',in_out='OUTPUT',socket_type='NodeSocketColor')
rl=ng.nodes.new('CompositorNodeRLayers');rl.location=(-600,0)
sat=ng.nodes.new('CompositorNodeHueSat');sat.inputs['Saturation'].default_value=1.12;sat.location=(-360,0);ng.links.new(rl.outputs['Image'],sat.inputs['Image'])
bloom=ng.nodes.new('CompositorNodeGlare');bloom.inputs['Type'].default_value='Fog Glow';bloom.inputs['Quality'].default_value='High';bloom.inputs['Threshold'].default_value=1.6;bloom.inputs['Strength'].default_value=.24;bloom.inputs['Size'].default_value=.20;bloom.location=(-100,0);ng.links.new(sat.outputs['Image'],bloom.inputs['Image'])
streak=ng.nodes.new('CompositorNodeGlare');streak.inputs['Type'].default_value='Streaks';streak.inputs['Quality'].default_value='High';streak.inputs['Threshold'].default_value=3.0;streak.inputs['Strength'].default_value=.15;streak.inputs['Streaks'].default_value=4;streak.inputs['Streaks Angle'].default_value=.35;streak.inputs['Fade'].default_value=.83;streak.inputs['Color Modulation'].default_value=.05;streak.location=(150,0);ng.links.new(bloom.outputs['Image'],streak.inputs['Image'])
out=ng.nodes.new('NodeGroupOutput');out.location=(400,0);ng.links.new(streak.outputs['Image'],out.inputs['Image'])
prefs=bpy.context.preferences.addons['cycles'].preferences;prefs.compute_device_type='METAL';prefs.get_devices()
for device in prefs.devices:device.use=device.type=='METAL'
s.cycles.device='GPU';s.cycles.samples=384;s.cycles.adaptive_threshold=.006;s.cycles.use_denoising=True
s.render.resolution_x=2400;s.render.resolution_y=2560;s.render.resolution_percentage=100
s.render.image_settings.file_format='PNG';s.render.image_settings.color_mode='RGB';s.render.image_settings.color_depth='8';s.render.filepath=str(O/'assets/hero-background.png')
s['revision']='v19 polished silver, richer champagne gold, luminous blue channels, neutral studio lighting with native highlight bloom and optical streaks; approved camera unchanged.'
bpy.ops.wm.save_as_mainfile(filepath=str(O/'source/hero-polished.blend'));bpy.ops.render.render(write_still=True)
print('POLISHED_HERO_DONE',flush=True)
