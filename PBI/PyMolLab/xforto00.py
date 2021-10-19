# Vytvorte tripeptid Ala-Gly-Lys a napiste skript v Pythonu
# (vyuzivajici Pymol API) pro nahodne otaceni krajnich aminokyselin kolem
# stredni po dobu urcenou parametricky. Otacejte kolem uhlu fi a psi.
# Detekujte hrozici kolize a otaceni s kolizi nevykonavejte.

# Helpful links:
# https://www.youtube.com/watch?v=1wzVbIzqA2M&ab_channel=TajminStudio
# https://proteopedia.org/wiki/index.php/Tutorial:Ramachandran_principle_and_phi_psi_angles

import pymol

def is_clockwise_rotation(angle):
    if angle > 0:
        clockwise_rotate = True
    else:
        clockwise_rotate = False
    return clockwise_rotate

# rotate clockwise by 360 / 120 = 3 degrees or counterclockwise
def rotate_in_direction(clockwise_rotate, frames_count):
    if clockwise_rotate == True:
        angle = 360 / frames_count
    else:
        angle = -360 / frames_count
    return angle

# process all rotations and save scene after each to current folder in png format - only phi1 angle rotation, psi1 angle rotation or combining of both
def process_frames(with_phi1, with_psi1, phi1_angle, psi1_angle, phi1_atoms_to_rotate, psi1_atoms_to_rotate, phi1_origin, psi1_origin, frames_count ):
    frame = 1
    img_counter = 1

    while (frame <= frames_count):
        # process all rotations and save scene after each to current folder in png format - only phi1 angle rotation, psi1 angle rotation or combining of both
        if with_phi1 == True and with_psi1 == False: # process only rotation with phi1 angle
            cmd.rotate("x", phi1_angle, selection="phi1_atoms_to_rotate", origin=phi1_origin[0])
            cmd.png("transformation_phi_" + str(img_counter) + ".png")
            img_counter += 1
        elif with_phi1 == False and with_psi1 == True:# process only rotation with psi1 angle
            cmd.rotate("x", psi1_angle, selection="psi1_atoms_to_rotate", origin=psi1_origin[0])
            cmd.png("transformation_psi_" + str(img_counter) + ".png")
            img_counter += 1
        else: # combine rotation with phi1 angle and then rotation with psi1 angle
            cmd.rotate("x", phi1_angle, selection="phi1_atoms_to_rotate", origin=phi1_origin[0])
            cmd.png("transformation_" + str(img_counter) + ".png")
            img_counter += 1
            cmd.rotate("x", psi1_angle, selection="psi1_atoms_to_rotate", origin=psi1_origin[0])
            cmd.png("transformation_" + str(img_counter) + ".png")
            img_counter += 1


        frame = frame + 1

    return

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

# SINCE THEN IS WORKED ONLY WITH PHI1 AND PSI1 ANGLES
clockwise_rotate_phi1 = False
clockwise_rotate_psi1 = False

# count of frames
frames_count = 120

# check whether value of angle is positive (clockwise rotation) or negative (counterclockwise rotation)
clockwise_rotate_phi1 = is_clockwise_rotation(phi1_angle)
clockwise_rotate_psi1 = is_clockwise_rotation(psi1_angle)

cmd.center("prot1", state=0, origin=1 )

# get coordinates of bond around which is calculated phi or psi angle
phi1_origin = cmd.get_coords("/prot1///GLY`2/N", 1)
psi1_origin = cmd.get_coords("/prot1///ALA`1/C", 1)

# select atoms which will be rotate - in cmd.rotate this should be set to parameter selection = string: atoms whose coordinates should be modified {default: all}
# https://pymol.org/dokuwiki/doku.php?id=command:rotate
# but it doesnt work for movie, so periodical saving .png frames to directory is used
cmd.select("phi1_atoms_to_rotate", "/prot1///GLY`2/H + resn ALA")
cmd.select("psi1_atoms_to_rotate", "/prot1///ALA`1/O + resn GLY + resn LYS")

# choose clockwise or counterclockwise rotation of bond
phi1_angle = rotate_in_direction(clockwise_rotate_phi1, frames_count)
psi1_angle = rotate_in_direction(clockwise_rotate_psi1, frames_count)


#def process_frames(with_phi1, with_psi1, phi1_angle, psi1_angle, phi1_atoms_to_rotate, psi1_atoms_to_rotate, phi1_origin, psi1_origin, frames_count ):
# process only rotation with phi1 angle - frames saved in pymol folder with name "transformation_phi_no.png"
process_frames(True, False, phi1_angle, None, "phi1_atoms_to_rotate", None, phi1_origin, None, frames_count)
# process only rotation with psi1 angle - frames saved in pymol folder with name "transformation_psi_no.png"
process_frames(False, True, None, psi1_angle, None, "psi1_atoms_to_rotate", None, psi1_origin, frames_count)
# combined rotation with phi1 angle and then psi1 angle - frames saved in pymol folder with name "transformation_no.png"
process_frames(True, True, phi1_angle, psi1_angle, "phi1_atoms_to_rotate", "psi1_atoms_to_rotate", phi1_origin, psi1_origin, frames_count)
