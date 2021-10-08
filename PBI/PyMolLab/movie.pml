load 1VA9.pdb
mset 1 x30
util.mroll 1,30,1
viewport 320,240
enable raytracing
set ray_trace_frames=1
set cache_frame=0
os.mkdir("bif")
cd bif
mpng 1va9
