import unreal
import numpy as np

acts=unreal.EditorLevelLibrary.get_all_level_actors()
print(len(acts))
ii=0
pos=[]
es=unreal.EditorActorSubsystem()
xf=unreal.Transform(location=(0,0,3000))
for a in acts:
	s=a.get_actor_label()
	if type(a)==unreal.StaticMeshActor:
		if a.get_attach_parent_actor()==None:
			p = a.get_actor_location()
			p = [p.x, p.y, p.z]
			t=a.get_actor_transform()
			es.set_actor_transform(a, t*xf)


	# 	p = a.get_actor_location()
	# 	r=a.get_actor_rotation()
	# 	pos.append([p.x, p.y, p.z, r.roll, r.pitch, r.yaw])
	# 	ii+=1
		# print(s)
		# st=''.join([x for x in s if not x.isdigit()])
		# dg=''.join([x for x in s if x.isdigit()])
		# lb="{}_{}".format(st,dg)
		# a.set_actor_label(s.replace("a_tube", "p22eject_{:02d}".format(ii)))
		# ii+=1

# pos=np.array(pos)
# print(pos)
# np.savetxt("C:\\Users\\g5v99\\Desktop\\p22\\membrane_pts.txt", pos)
