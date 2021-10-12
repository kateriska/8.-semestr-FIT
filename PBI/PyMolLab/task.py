import pymol

cmd.reinitialize()
cmd.fab("AGK", "prot1")
cmd.mset("1 x60")
angle = 360/60
frame = 1

cmd.select("sel1", "resn ALA")
cmd.select("sel2", "resn LYS")

while (frame <= 60):
  cmd.rotate("x", angle, selection="sel1", object="prot1")
  cmd.rotate("x", angle, selection="sel2", object="prot1")
  cmd.mview("store", frame, object="prot1")
  frame = frame + 1

cmd.mplay()
cmd.movie.produce("movie.mpg", quality=90)
