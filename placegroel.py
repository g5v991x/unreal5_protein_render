import unreal
import numpy as np

scale=0.02
root=unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor,(0,0,0))
root.set_actor_label("groel")#
objlst=["groelA","groelAA"]
for o in objlst:
	print(o)
	obj=unreal.EditorAssetLibrary.load_asset(f"/Game/groel/{o}.{o}")
	for ii in range(7):
		act=unreal.EditorLevelLibrary.spawn_actor_from_object(obj,(0,0,0), (0,ii*360/7,90))
		act.set_actor_relative_scale3d((scale, scale, scale))
		act.attach_to_actor(root,"none",unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD)
		act.set_actor_label("{}_{:03d}".format(o[o.rfind('.')+1:], ii))
# #

root=unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor,(0,0,0))
root.set_actor_label("groels")
objlst=["groelB","groelC","groelD"]
for o in objlst:
	print(o)
	obj=unreal.EditorAssetLibrary.load_asset(f"/Game/groel/{o}.{o}")
	for ii in range(7):
		act=unreal.EditorLevelLibrary.spawn_actor_from_object(obj,(0,0,0), (0,ii*360/7,90))
		act.set_actor_relative_scale3d((scale, scale, scale))
		act.attach_to_actor(root,"none",unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD)
		act.set_actor_label("{}_{:03d}".format(o[o.rfind('.')+1:], ii))
#
