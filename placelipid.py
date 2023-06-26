import unreal
import numpy as np

pos=np.loadtxt("membrane_new.txt")
scale=0.02
p=np.mean(pos, axis=0)
# root=unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor,(p[0],p[1],p[2]))
root=unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor,(0,0,0))

# root.set_actor_label("lipid_inner")
# olst=["lipidA", "lipidB"]

# root.set_actor_label("lipid_outer")
# olst=["lipidOC", "lipidOA", "lipidOB"]

root.set_actor_label("cellwall")
olst=["cellwall", "cellwall_lipo"]


objs=[unreal.EditorAssetLibrary.load_asset(f"/Game/Lipid/{o}.{o}") for o in olst]
z0=-999999999
zi=0
rootz=root
cnt=np.array([0,0,2925])

with unreal.ScopedSlowTask(len(pos), "placing cell membrane") as slow_task:
	slow_task.make_dialog(True)               # Makes the dialog visible, if it isn't already
	for ii,p in enumerate(pos.tolist()):
		if slow_task.should_cancel():         # True if the user has pressed Cancel in the UI
			break
		slow_task.enter_progress_frame(1)     # Advance progress by one frame.

		print(p)

		if p[2]!=z0:
			z0=p[2]
			rootz=unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor,(0,0,0))
			rootz.set_actor_label(f"lipid_z{zi:02d}")
			rootz.attach_to_actor(root,"none",unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD)
			zi+=1

		for oi,obj in enumerate(objs):
			o=olst[oi]
			v=pos[ii][:3]-pos[ii-1][:3]
			v=unreal.Vector(v[0], v[1], v[2])
			v.normalize()
			r=v.rotator()
			r90=unreal.Rotator(-p[3],0,0)
			r=r90.combine(r)
			act=unreal.EditorLevelLibrary.spawn_actor_from_object(obj,(p[0], p[1], p[2]), r)
			# act.set_actor_relative_scale3d((1.4, 0.8, 1.4))
			act.set_actor_relative_scale3d((scale, scale, scale))
			act.set_actor_label("{}_{:03d}".format(o[o.rfind('.')+1:], ii))
			if oi==0:
				act.attach_to_actor(rootz,"none",unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD)
				act0=act
			else:
				act.attach_to_actor(act0,"none",unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD)




