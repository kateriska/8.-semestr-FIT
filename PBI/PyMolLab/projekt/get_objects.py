# Script for separate protein and their ligand into separate files used for docking

cmd.reinitialize()

cmd.fetch("1hsg", "prot1")
cmd.remove("solvent")
print(cmd.get_fastastr('all'))
cmd.select("ligand_atoms", "/prot1/C/B/MK1`902/")
cmd.save("ligand.sdf", "ligand_atoms")
cmd.remove("ligand_atoms")
cmd.show(representation="cartoon")
cmd.save("prot1_prepared.pdb", "prot1")
