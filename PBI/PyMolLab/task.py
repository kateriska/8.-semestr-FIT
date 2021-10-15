# Vytvorte tripeptid Ala-Gly-Lys a napiste skript v Pythonu
# (vyuzivajici Pymol API) pro nahodne otaceni krajnich aminokyselin kolem
# stredni po dobu urcenou parametricky. Otacejte kolem uhlu fi a psi.
# Detekujte hrozici kolize a otaceni s kolizi nevykonavejte.

import pymol

cmd.reinitialize()
cmd.fab("AGK", "prot1")
cmd.hide(representation="cartoon")

# selecting atoms to calculate angles
cmd.select("phi1_atoms", "/prot1///ALA`1/C + /prot1///GLY`2/N + /prot1///GLY`2/CA + /prot1///GLY`2/C")
cmd.select("phi2_atoms", "/prot1///GLY`2/C + /prot1///LYS`3/N + /prot1///LYS`3/CA + /prot1///LYS`3/C")

cmd.select("psi1_atoms", "/prot1///ALA`1/N + /prot1///ALA`1/CA + /prot1///ALA`1/C + /prot1///GLY`2/N")
cmd.select("psi2_atoms", "/prot1///GLY`2/N + /prot1///GLY`2/CA + /prot1///GLY`2/C + /prot1///LYS`3/N")

# phi bonds - calculate of angle
cmd.get_dihedral("/prot1///ALA`1/C","/prot1///GLY`2/N","/prot1///GLY`2/CA","/prot1///GLY`2/C",state=0)
cmd.get_dihedral("/prot1///GLY`2/C","/prot1///LYS`3/N","/prot1///LYS`3/CA","/prot1///LYS`3/C",state=0)
# psi bonds - calculate of angle
cmd.get_dihedral("/prot1///ALA`1/N","/prot1///ALA`1/CA","/prot1///ALA`1/C","/prot1///GLY`2/N",state=0)
cmd.get_dihedral("/prot1///GLY`2/N","/prot1///GLY`2/CA","/prot1///GLY`2/C","/prot1///LYS`3/N",state=0)

cmd.mset("1 x120")
angle = 360/120
frame = 1

cmd.center("prot1", state=0, origin=1 )
cmd.select("sel1", "resn ALA + resn LYS")
#cmd.select("sel2", "resn LYS")
#xyz = cmd.get_coords("/prot1///GLY`2/N", 1)

# get coordinates of bond around which is calculated phi or psi angle
phi1_origin = cmd.get_coords("/prot1///LYS`3/N", 1)
phi2_origin = cmd.get_coords("/prot1///GLY`2/N", 1)

psi1_origin = cmd.get_coords("/prot1///GLY`2/CA", 1)
psi2_origin = cmd.get_coords("/prot1///ALA`1/CA", 1)


while (frame <= 120):
  #cmd.rotate("x", angle, selection="sel1", object="prot1", origin=phi1_origin[0])
  #cmd.rotate("x", angle, selection="sel1", object="prot1", origin=phi2_origin[0])
  #cmd.rotate("x", angle, selection="sel1", object="prot1", origin=psi1_origin[0])
  cmd.rotate("x", angle, selection="sel1", object="prot1", origin=psi2_origin[0])
  #cmd.rotate("x", angle, selection="sel2", object="prot1")
  cmd.mview("store", frame, object="prot1")
  frame = frame + 1

cmd.mplay()
#cmd.movie.produce("movie.mpg", quality=90)
