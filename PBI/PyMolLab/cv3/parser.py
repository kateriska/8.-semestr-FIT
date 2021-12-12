from Bio import SeqIO
import re

# filter potential g-quadruplex in fastq file 

regex = "G{3,}.{1,7}G{3,}.{1,7}G{3,}.{1,7}G{3,}"

file_name = "SRR17175824_2"
filtered_file = open(file_name + "_filtered.fastq", "w+")
filtered_file.close()

file = open(file_name + '.fastq', 'r')
count = 0
entry = list()
write_to_filtered_file = False

for line in file:
    stripped_line = line.strip()
    if count % 4 == 0: # id
        entry = list()
        entry.append(stripped_line)
    elif count % 4 == 1: # sequence
        entry.append(stripped_line)
        if re.findall(regex, stripped_line) != []:
            write_to_filtered_file = True
    elif count % 4 == 2: # separator
        entry.append(stripped_line)
    elif count % 4 == 3: # quality score
        entry.append(stripped_line)
        if write_to_filtered_file == True:
            # if sequence matched regex we write whole entry to filtered file
            filtered_file = open(file_name + "_filtered.fastq", "a")
            for item in entry:
                filtered_file.write(item + "\n")
            filtered_file.close()
            write_to_filtered_file = False

    #print(entry)
    count += 1
