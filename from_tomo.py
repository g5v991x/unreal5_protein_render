import unreal
import numpy as np

scale=0.1
apix=8.8


objlst=["sars_spike_e", "sars_spike_f", "sars_spike_g", "sars_spike_h", "lipidAB"]
objlst2=["sars_spike_a", "sars_spike_b", "sars_spike_c", "sars_spike_d"]

pos=np.loadtxt("spikepos.txt")

pos[:,:3]=pos[:,[2,0,1]]*apix*10
pos[:,[7,8,9]]=pos[:,[9,7,8]]*apix*10

pp=np.mean(pos, axis=0)
# objlst=[]

root0=unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor,(pp[0],pp[1],pp[2]))
root0.set_actor_label(f"virus_00")

dvs=pos[1::2,:3]-pos[0::2,:3]
nsym=1
for ip,pp in enumerate(pos):
	# print(pp)
	v=unreal.Vector(pp[0],pp[1],pp[2])
	q=unreal.Quat(pp[3], pp[4], pp[5], pp[6])
	r1=q.rotator()

	r90=unreal.Rotator(0,0,-90)
	r1=r90.combine(r1)
	root=unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor,(pp[0],pp[1],pp[2]), q.rotator())
	root.set_actor_label(f"sars_spike_{ip:03d}")
	root.attach_to_actor(root0,"none",unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD)

	rootup=unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor,(pp[0],pp[1],pp[2]), q.rotator())
	rootup.set_actor_label(f"top")
	rootup.attach_to_actor(root,"none",unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD)

	rootstalk=unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor,(pp[0],pp[1],pp[2]), q.rotator())
	rootstalk.set_actor_label(f"stalk")
	rootstalk.attach_to_actor(root,"none",unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD)


	vq=r1.get_right_vector()*(-1100)
	v=v.add(vq)
	for o in objlst:
		obj=unreal.EditorAssetLibrary.load_asset(f"/Game/sars/{o}.{o}")

		# act=unreal.EditorLevelLibrary.spawn_actor_from_object(obj,v, q.rotator())
		act=unreal.EditorLevelLibrary.spawn_actor_from_object(obj,v, r1)
		act.set_actor_relative_scale3d((scale, scale, scale))
		# act.set_actor_relative_scale3d((0.02, 0.1, 0.02))
		act.attach_to_actor(rootstalk,"none",unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD)
		act.set_actor_label(o)


	v=unreal.Vector(pp[7],pp[8],pp[9])
	q=unreal.Quat(pp[10], pp[11], pp[12], pp[13])
	r1=q.rotator()
	r90=unreal.Rotator(0,0,-90)
	r1=r90.combine(r1)

	vq=r1.get_right_vector()*(-2200)
	v=v.add(vq)
	for o in objlst2:
		obj=unreal.EditorAssetLibrary.load_asset(f"/Game/sars/{o}.{o}")
		act=unreal.EditorLevelLibrary.spawn_actor_from_object(obj,v, r1)
		act.set_actor_relative_scale3d((scale, scale, scale))
		act.attach_to_actor(rootup,"none",unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD)
		act.set_actor_label(o)
