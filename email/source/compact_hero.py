# v28 compact header: re-frames the approved v19 hero scene (hero-polished.blend) for a wide 600x320 email banner.
# Materials, lighting and compositor are unchanged; only the camera framing and output size differ.
from pathlib import Path
import bpy
O=Path(__file__).resolve().parents[1]
bpy.ops.wm.open_mainfile(filepath=str(O/'source/hero-polished.blend'))
s=bpy.context.scene;cam=s.camera.data
cam.sensor_fit='HORIZONTAL';cam.sensor_width=49.0;cam.shift_x=0.05;cam.shift_y=0.165
s.render.resolution_x=2400;s.render.resolution_y=1280;s.render.resolution_percentage=100
prefs=bpy.context.preferences.addons['cycles'].preferences;prefs.compute_device_type='METAL';prefs.get_devices()
for d in prefs.devices:d.use=d.type=='METAL'
s.cycles.device='GPU';s.cycles.samples=384;s.cycles.adaptive_threshold=.006;s.cycles.use_denoising=True
s.render.image_settings.file_format='PNG';s.render.image_settings.color_mode='RGB';s.render.image_settings.color_depth='8'
s.render.filepath=str(O/'assets/hero-compact-background.png')
s['revision']='v28 compact wide framing of the v19 polished hero; dark upper band reserved for the centered headline.'
bpy.ops.wm.save_as_mainfile(filepath=str(O/'source/hero-compact.blend'));bpy.ops.render.render(write_still=True)
print('COMPACT_HERO_DONE',flush=True)
