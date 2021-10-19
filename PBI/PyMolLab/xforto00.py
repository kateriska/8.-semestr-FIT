# Vytvorte tripeptid Ala-Gly-Lys a napiste skript v Pythonu
# (vyuzivajici Pymol API) pro nahodne otaceni krajnich aminokyselin kolem
# stredni po dobu urcenou parametricky. Otacejte kolem uhlu fi a psi.
# Detekujte hrozici kolize a otaceni s kolizi nevykonavejte.

# https://www.youtube.com/watch?v=1wzVbIzqA2M&ab_channel=TajminStudio

import pymol
import time

def is_clockwise_rotation(angle):
    if angle > 0:
        clockwise_rotate = True
    else:
        clockwise_rotate = False
    return clockwise_rotate

# rotate clockwise by 360 / 120 = 3 degrees or counterclockwise
def rotate_in_direction(clockwise_rotate):
    if clockwise_rotate == True:
        angle = 3
    else:
        angle = -3
    return angle

cmd.reinitialize()

cmd.fab("AGK", "prot1")
cmd.hide(representation="cartoon")

# selecting atoms to calculate angles
cmd.select("phi1_atoms", "/prot1///ALA`1/C + /prot1///GLY`2/N + /prot1///GLY`2/CA + /prot1///GLY`2/C")
cmd.select("phi2_atoms", "/prot1///GLY`2/C + /prot1///LYS`3/N + /prot1///LYS`3/CA + /prot1///LYS`3/C")

cmd.select("psi1_atoms", "/prot1///ALA`1/N + /prot1///ALA`1/CA + /prot1///ALA`1/C + /prot1///GLY`2/N")
cmd.select("psi2_atoms", "/prot1///GLY`2/N + /prot1///GLY`2/CA + /prot1///GLY`2/C + /prot1///LYS`3/N")

# phi bonds - calculate of angle
phi1_angle = cmd.get_dihedral("/prot1///ALA`1/C","/prot1///GLY`2/N","/prot1///GLY`2/CA","/prot1///GLY`2/C",state=0)
phi2_angle = cmd.get_dihedral("/prot1///GLY`2/C","/prot1///LYS`3/N","/prot1///LYS`3/CA","/prot1///LYS`3/C",state=0)

# psi bonds - calculate of angle
psi1_angle = cmd.get_dihedral("/prot1///ALA`1/N","/prot1///ALA`1/CA","/prot1///ALA`1/C","/prot1///GLY`2/N",state=0)
psi2_angle = cmd.get_dihedral("/prot1///GLY`2/N","/prot1///GLY`2/CA","/prot1///GLY`2/C","/prot1///LYS`3/N",state=0)

clockwise_rotate_phi1 = False
clockwise_rotate_phi2 = False
clockwise_rotate_psi1 = False
clockwise_rotate_psi2 = False

# check whether value of angle is positive (clockwise rotation) or negative (counterclockwise rotation)
clockwise_rotate_phi1 = is_clockwise_rotation(phi1_angle)
clockwise_rotate_phi2 = is_clockwise_rotation(phi2_angle)
clockwise_rotate_psi1 = is_clockwise_rotation(psi1_angle)
clockwise_rotate_psi2 = is_clockwise_rotation(psi2_angle)


cmd.center("prot1", state=0, origin=1 )

# get coordinates of bond around which is calculated phi or psi angle
phi1_origin = cmd.get_coords("/prot1///GLY`2/N", 1)
phi2_origin = cmd.get_coords("/prot1///LYS`3/N", 1)

psi1_origin = cmd.get_coords("/prot1///ALA`1/CA", 1)
psi2_origin = cmd.get_coords("/prot1///GLY`2/CA", 1)

# select atoms which will be rotate - in cmd.rotate this should be set to parameter selection = string: atoms whose coordinates should be modified {default: all}
# https://pymol.org/dokuwiki/doku.php?id=command:rotate
# but it doesnt work for movie, so periodical saving .png frames to directory is used
cmd.select("phi1_atoms_to_rotate", "resn LYS and (not (/prot1///GLY`2/N)) and (not (/prot1///GLY`2/H)) + resn GLY")
cmd.select("phi2_atoms_to_rotate", "resn LYS and (not (/prot1///LYS`3/N)) and (not (/prot1///LYS`3/H))")
cmd.select("psi1_atoms_to_rotate", "/prot1///ALA`1/O + /prot1///ALA`1/C + resn GLY + resn LYS")
cmd.select("psi2_atoms_to_rotate", "/prot1///GLY`2/C + /prot1///GLY`2/O + resn LYS")

# choose clockwise or counterclockwise rotation of bond
phi1_angle = rotate_in_direction(clockwise_rotate_phi1)
phi2_angle = rotate_in_direction(clockwise_rotate_phi2)
psi1_angle = rotate_in_direction(clockwise_rotate_psi1)
psi2_angle = rotate_in_direction(clockwise_rotate_psi2)

frame = 1
img_counter = 1
while (frame <= 120):
    # process all rotations and save scene after each to current folder in png format
    cmd.rotate("x", phi1_angle, selection="phi1_atoms_to_rotate", origin=phi1_origin[0])
    cmd.png("transform_" + str(img_counter) + ".png")
    img_counter += 1
    cmd.rotate("x", phi2_angle, selection="phi2_atoms_to_rotate", origin=phi2_origin[0])
    cmd.png("transform_" + str(img_counter) + ".png")
    img_counter += 1
    cmd.rotate("x", psi1_angle, selection="psi1_atoms_to_rotate", origin=psi1_origin[0])
    cmd.png("transform_" + str(img_counter) + ".png")
    img_counter += 1
    cmd.rotate("x", psi2_angle, selection="psi2_atoms_to_rotate", origin=psi2_origin[0])
    cmd.png("transform_" + str(img_counter) + ".png")
    img_counter += 1
    #time.sleep(0.05)
    frame = frame + 1
