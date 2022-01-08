def find_nearby_aminoacids(select_arg):
    three_letter_aa_codes = ['ALA', 'CYS', 'ASP', 'GLU', 'PHE', 'GLY', 'HIS', 'ILE', 'LYS', 'LEU', 'MET', 'ASN', 'PRO', 'GLN', 'ARG', 'SER', 'THR', 'VAL', 'TRP', 'TYR']
    result = []
    print("Nearby aminoacids from ligand - these aminoacids have polar contacts with ligand:")
    for arg in select_arg.split('+'):
        splitted_arg = arg.split('/')
        aminoacid = (splitted_arg[4])[0:3]
        if aminoacid not in three_letter_aa_codes:
            continue
        index = (splitted_arg[4])[4:]

        result.append((aminoacid, index))

    # remove duplicities from list
    result = list(dict.fromkeys(result))
    print(result)
    for item in result:
        print("Aminoacid " + item[0] + " on index in protein sequnce " + str(item[1]))
    return result

cmd.reinitialize()

cmd.load("prot1_prepared.pdbqt", "prot1_prepared")
cmd.load("prot1_uff_E=373.91_out.pdbqt", "ligand")

# see bonds of ligand and protein
preset.ligand_sites(selection='all')

cmd.hide(representation="surface")
cmd.show(representation="cartoon")

cmd.zoom("ligand")

# Mouse -> Selection mode -> Atoms
# Click on each bound and show selected aminoacids in sequence
# selection of nearby aminoacids depends on state - we have 9 states as results of docking - switching of states can be done by right down corner control panel by arrows
# DONT FORGET TO SWICH TO SPECIFIED STATE FOR LOOKING FOR SELECTIONS AND DISTANCES BECAUSE THEY ARE SPECIAL FOR EACH STATE!!

print("STATE 1:")
state_1_arg = "/ligand//N/UNK`1/H + /prot1_prepared//B/ASP`29/OD2 + /ligand//N/UNK`1/O + /prot1_prepared//B/ASP`29/HN + /ligand//N/UNK`1/H + /prot1_prepared//B/GLY`27/O + /ligand//N/UNK`1/H + /prot1_prepared//B/ASP`25/OD1 + /prot1_prepared//B/ASP`25/OD2"
cmd.select("state_1_atoms", "/ligand//N/UNK`1/H + /prot1_prepared//B/ASP`29/OD2 + /ligand//N/UNK`1/O + /prot1_prepared//B/ASP`29/HN + /ligand//N/UNK`1/H + /prot1_prepared//B/GLY`27/O + /ligand//N/UNK`1/H + /prot1_prepared//B/ASP`25/OD1 + /prot1_prepared//B/ASP`25/OD2")
find_nearby_aminoacids(state_1_arg)
'''
cmd.distance("state_1_dist_1", "/prot1_prepared//B/ASP`25/OD2", "/ligand//N/UNK`1/H", cutoff=3)
cmd.distance("state_1_dist_2", "/prot1_prepared//B/ASP`25/OD1", "/ligand//N/UNK`1/H", cutoff=3)
cmd.distance("state_1_dist_3", "/ligand//N/UNK`1/H", "/prot1_prepared//B/GLY`27/O", cutoff=3)
cmd.distance("state_1_dist_4", "/ligand//N/UNK`1/O", "/prot1_prepared//B/ASP`29/HN", cutoff=3)
cmd.distance("state_1_dist_5", "/ligand//N/UNK`1/H", "/prot1_prepared//B/ASP`29/OD2", cutoff=3)
'''

print("STATE 2:")
state_2_arg = "/prot1_prepared//A/GLY`27/O + /ligand//N/UNK`1/H + /ligand//N/UNK`1/H + /ligand//N/UNK`1/O + /prot1_prepared//A/ASP`29/HN + /prot1_prepared//A/ASP`25/OD1 + /prot1_prepared//A/ASP`25/OD2 + /ligand//N/UNK`1/H"
cmd.select("state_2_atoms",state_2_arg)
find_nearby_aminoacids(state_2_arg)
'''
cmd.distance("state_2_dist_1", "/prot1_prepared//A/ASP`29/HN", "/ligand//N/UNK`1/O", cutoff=3)
cmd.distance("state_2_dist_2", "/ligand//N/UNK`1/H", "/prot1_prepared//A/GLY`27/O", cutoff=3)
cmd.distance("state_2_dist_3", "/ligand//N/UNK`1/H", "/prot1_prepared//A/GLY`27/O", cutoff=3)
cmd.distance("state_2_dist_4", "/prot1_prepared//A/ASP`25/OD2", "/ligand//N/UNK`1/H", cutoff=3)
cmd.distance("state_2_dist_5", "/ligand//N/UNK`1/H", "/prot1_prepared//A/ASP`25/OD1", cutoff=3)
'''

print("STATE 3:")
state_3_arg = "/prot1_prepared//B/ASP`25/OD2 + /ligand//N/UNK`1/H"
cmd.select("state_3_atoms",state_3_arg)
find_nearby_aminoacids(state_3_arg)
'''
cmd.distance("state_3_dist_1", "/prot1_prepared//B/ASP`25/OD2", "/ligand//N/UNK`1/H", cutoff=3)
'''

print("STATE 4:")
state_4_arg = "/ligand//N/UNK`1/O + /prot1_prepared//B/ILE`50/HN + /prot1_prepared//B/GLY`27/O + /ligand//N/UNK`1/H"
cmd.select("state_4_atoms",state_4_arg)
find_nearby_aminoacids(state_4_arg)
'''
cmd.distance("state_4_dist_1", "/prot1_prepared//B/ILE`50/HN", "/ligand//N/UNK`1/O", cutoff=3)
cmd.distance("state_4_dist_2", "/prot1_prepared//B/GLY`27/O", "/ligand//N/UNK`1/H", cutoff=3)
'''

print("STATE 5:")
state_5_arg = "/prot1_prepared//B/ASP`25/OD2 + /ligand//N/UNK`1/H + /prot1_prepared//B/GLY`48/O + /ligand//N/UNK`1/H + /prot1_prepared//A/GLY`48/O + /ligand//N/UNK`1/HN"
cmd.select("state_5_atoms",state_5_arg)
find_nearby_aminoacids(state_5_arg)
'''
cmd.distance("state_5_dist_1", "/ligand//N/UNK`1/HN", "/prot1_prepared//A/GLY`48/O", cutoff=3)
cmd.distance("state_5_dist_2", "/prot1_prepared//B/ASP`25/OD2", "/ligand//N/UNK`1/H", cutoff=3)
cmd.distance("state_5_dist_3", "/ligand//N/UNK`1/H", "/prot1_prepared//B/GLY`48/O", cutoff=3)
'''

print("STATE 6:")
state_6_arg = "/ligand//N/UNK`1/H + /prot1_prepared//B/ASP`25/OD2 + /prot1_prepared//B/ASP`25/OD1 + /prot1_prepared//A/ASP`25/OD1 + /ligand//N/UNK`1/HN + /prot1_prepared//B/GLY`48/O"
cmd.select("state_6_atoms",state_6_arg)
find_nearby_aminoacids(state_6_arg)

cmd.distance("state_6_dist_1", "/prot1_prepared//B/ASP`25/OD2", "/ligand//N/UNK`1/H", cutoff=3)
cmd.distance("state_6_dist_2", "/prot1_prepared//B/ASP`25/OD1", "/ligand//N/UNK`1/H", cutoff=3)
cmd.distance("state_6_dist_3", "/prot1_prepared//A/ASP`25/OD1", "/ligand//N/UNK`1/H", cutoff=3)
cmd.distance("state_6_dist_4", "/ligand//N/UNK`1/HN", "/prot1_prepared//B/GLY`48/O", cutoff=3)

print("STATE 7:")
state_7_arg = "/prot1_prepared//B/GLY`48/O + /ligand//N/UNK`1/H + /prot1_prepared//B/ILE`50/HN + /ligand//N/UNK`1/O"
cmd.select("state_7_atoms",state_7_arg)
find_nearby_aminoacids(state_7_arg)

cmd.distance("state_7_dist_1", "/ligand//N/UNK`1/H", "/prot1_prepared//B/GLY`48/O", cutoff=3)
cmd.distance("state_7_dist_2", "/ligand//N/UNK`1/O", "/prot1_prepared//B/ILE`50/HN", cutoff=3)

print("STATE 8:")
state_8_arg = "/ligand//N/UNK`1/H + /prot1_prepared//B/ASP`25/OD2 + /ligand//N/UNK`1/O + /prot1_prepared//A/ASP`29/HN + /ligand//N/UNK`1/H + /prot1_prepared//A/GLY`48/O"
cmd.select("state_8_atoms",state_8_arg)
find_nearby_aminoacids(state_8_arg)

cmd.distance("state_8_dist_1", "/prot1_prepared//B/ASP`25/OD2", "/ligand//N/UNK`1/H", cutoff=3)
cmd.distance("state_8_dist_2", "/prot1_prepared//A/GLY`48/O", "/ligand//N/UNK`1/H", cutoff=3)
cmd.distance("state_8_dist_3", "/prot1_prepared//A/ASP`29/HN", "/ligand//N/UNK`1/O", cutoff=3)

print("STATE 9:")
state_9_arg = "/ligand//N/UNK`1/H + /prot1_prepared//B/ASP`25/OD2 + /prot1_prepared//B/GLY`48/O + /ligand//N/UNK`1/H"
cmd.select("state_9_atoms",state_9_arg)
find_nearby_aminoacids(state_9_arg)

cmd.distance("state_9_dist_1", "/prot1_prepared//B/ASP`25/OD2", "/ligand//N/UNK`1/H", cutoff=3)
cmd.distance("state_9_dist_2", "/prot1_prepared//B/GLY`48/O", "/ligand//N/UNK`1/H", cutoff=3)
# Mouse -> Selection mode -> Atoms
# Click on each bound and show selected aminoacids in sequence:
# State 1 -
# State 2
# State 3
# State 4
# State 5
# State 6
# State 7
# State 8
# State 9
# State 10
