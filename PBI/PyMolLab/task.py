import pymol

cmd.reinitialize()
cmd.fab("AGK", "prot1")
cmd.hide(representation="cartoon")

# phi bonds
#cmd.get_dihedral("/prot1///ALA`1/C","/prot1///GLY`2/N","/prot1///GLY`2/CA","/prot1///GLY`2/C",state=0)


cmd.mset("1 x60")
angle = 360/120
frame = 1

cmd.center("prot1", state=0, origin=1 )
cmd.select("sel1", "resn ALA + resn LYS")
cmd.select("sel2", "resn LYS")

while (frame <= 120):
  cmd.rotate("x", angle, selection="sel1", object="prot1")
  #cmd.rotate("x", angle, selection="sel2", object="prot1")
  cmd.mview("store", frame, object="prot1")
  frame = frame + 1

cmd.mplay()
#cmd.movie.produce("movie.mpg", quality=90)
