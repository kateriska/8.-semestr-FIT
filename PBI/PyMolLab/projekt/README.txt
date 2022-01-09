Download .pdb file https://www.rcsb.org/structure/1HSG
In PyMol run python get_objects.py - gets you files prot1_prepared.pdb and ligand.sdf
Download and install PyRx (https://sourceforge.net/projects/pyrx/)

Docking with PyRx:
Open PyRx
File -> Load Molecule -> prot1_prepared.pdb
Click on prot1_prepared in left Navigator column -> AutoDock -> Make Macromolecule - this gets you .pdbqt file with which can PyRx work
File -> Import -> Chemical Table File - SDF -> ligand.sdf
Click on ligand in Controls -> Minimize Selected -> OK  - Energy minimization is runned
Click on ligand in Controls -> Convert Selected to AutoDock(pdbqt)
Click on Vina Wizard in Controls -> Forward - Docking is started after specifying search space
Table results of docking are shown in ligand_binding_results.csv and docking_results.png
Generated files from docking are: conf.txt, prot1_uff_E=373.91_out.pdbqt and prot1_prepared.pdbqt

Analyze docking results:
In PyMol run analyze_bindings.py - there are 9 states of possible setting of protein and ligand
Nearby aminoacids and their indexes in fasta sequence of protein are printed in console and also to file nearby_aminoacids.csv
see connected_aminoacids_to_ligand.PNG how to figure out bonded protein and ligand atoms and position of these nearby aminoacids in fasta sequnce of protein
see measure_distances.PNG to see example of measured distances of State 1
