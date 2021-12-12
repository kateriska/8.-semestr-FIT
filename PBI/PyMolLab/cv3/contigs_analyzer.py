from Bio import SeqIO
import csv

# script for counting length of contigs.fa sequences and ratio of different bases in each sequence
# output is written to contigs_stats.csv

# count ratio of each base in particular sequence
def count_base_ratio_in_sequence(sequence, base):
    sequence_length = len(sequence)
    split_sequence = list(sequence) # split sequence to separate bases
    occurence = 0
    for seq_base in split_sequence:
        if seq_base == base:
            occurence += 1

    ratio = occurence / sequence_length
    return round(ratio * 100,2)


csv_path = 'contigs_stats.csv'


# write head of csv file
with open(csv_path, 'w+') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "Length of Sequence", "Ratio of A Base [%]", "Ratio of G Base [%]", "Ratio of C Base [%]", "Ratio of T Base [%]"])

csv_file.close()

with open("./Assem6/contigs.fa") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        record_id = record.id
        sequence_length = len(str(record.seq))
        A_ratio = str(count_base_ratio_in_sequence(record.seq, 'A'))
        G_ratio = str(count_base_ratio_in_sequence(record.seq, 'G'))
        C_ratio = str(count_base_ratio_in_sequence(record.seq, 'C'))
        T_ratio = str(count_base_ratio_in_sequence(record.seq, 'T'))

        with open(csv_path, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([record.id, str(sequence_length), A_ratio, G_ratio, C_ratio, T_ratio])

        csv_file.close()
