import unreal
import numpy as np
import sequencer_tools_examples, sequencer_fbx_examples

scale=.02
loadfbx=True
loadtxt=False
sequencer_tools_examples.bake_transform("/Game/seqtest")
sequencer_fbx_examples.export_fbx("/Game/Maps/Map_P22","/Game/seqtest", "/Game/seqtest", "D:\\FBX_Test1.fbx")


if loadfbx:
	fbxname="D:\\FBX_Test1.fbx"
	f=open(fbxname,'r')
	lines=f.readlines()
	data=[]

	cv=False
	for ii,l in enumerate(lines):
		if l.startswith("\tAnimationCurve:"):
			print(ii,l)
			cv=True

		if cv and "KeyValueFloat" in l:
			lx=""
			for j in range(1,100):
				if '}' in lines[ii+j]: break
				lx+=lines[ii+j]
			# lx=lines[ii+1]
			lx=lx[lx.find("a:")+2:]
			print(lx)
			lxn=[float(x) for x in lx.split(',') if len(x)>1]
			print(lxn)
			data.append(lxn)
			cv=False

	print([len(d) for d in data])
	data=np.array(data[:3]).T
	data[:,1]*=-1

if loadtxt:
	p=np.loadtxt("D:\\dna_full.txt")
	data=p*4.4*100
	data-=np.mean(data, axis=0)
	data*=scale


print(data.shape)
df=np.diff(data, axis=0)
df=np.linalg.norm(df, axis=1)
# print(df)
step=340*10
step*=scale
datanew=[data[0]]
sm=0
for i in range(1,len(data)-1):
	sm+=df[i-1]
	if sm+df[i]>step:
		datanew.append(data[i])
		sm=0

datanew.append(data[-1])

data=np.array(datanew)
print(data.shape)
df=np.diff(data, axis=0)
df=np.linalg.norm(df, axis=1)
print(np.mean(df), np.max(df))
# print(df)
obj=unreal.EditorAssetLibrary.load_asset("/Game/DNA/dna.dna")

pc=np.mean(data, axis=0)
# data-=pc
root=unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor,(pc[0],pc[1],pc[2]))
root.set_actor_label("dna_000")

# for ii in range(1, len(data)):
nn=len(data)
k=5
total_frames = nn
text_label = "Working!"
dt0=0
with unreal.ScopedSlowTask(total_frames, text_label) as slow_task:
	slow_task.make_dialog(True)               # Makes the dialog visible, if it isn't already


	for ii in range(1,nn):
		if slow_task.should_cancel():         # True if the user has pressed Cancel in the UI
			break

		slow_task.enter_progress_frame(1)     # Advance progress by one frame.

		p0=data[ii-1][:3]
		p=data[ii]
		v=(p[:3]-p0).tolist()
		v=unreal.Vector(v[0],v[1],v[2])
		l=v.length()
		dt=l/340*36*scale+dt0
		dt=dt%360
		dt0=dt
		print(dt)
		rt0=unreal.Rotator(0,dt,90)
		v=v.normal()
		r=v.rotator()
		r=rt0.combine(r)
		act=unreal.EditorLevelLibrary.spawn_actor_from_object(obj,(p[0], p[1], p[2]), r)
		act.set_actor_relative_scale3d((scale, scale, scale))
		act.attach_to_actor(root,"none",unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD,unreal.AttachmentRule.KEEP_WORLD)
		act.set_actor_label("{}_{:03d}".format('dna', ii))


#
