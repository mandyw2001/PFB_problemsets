#!/usr/bin/env python3
from Bio import SeqIO

filename = "/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_08.fasta.txt"

#filename = "/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/test.fa"

#filename = ' /Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/jfo/problemsets/Python_08/Test.fasta'

sequence_count = 0
num_nt = 0
sequence_records = []
for entry in SeqIO.parse(filename, "fasta"):
    ids = entry.id
    descriptions = entry.description
    sequences = entry.seq
    #print('ID:', ids)
    #print('description', descriptions)
    #print('sequence:', sequences)
    sequence_count+=1
    for sequence in sequences:
        num_nt+=1

    sequence_records.append(str(sequences)) 
    
avg_seq_len = num_nt/sequence_count

sequence_length = []
for sequence in sequence_records:
    length = len(sequence)
    sequence_length.append(length)

sorted_sequence_length = sorted(sequence_length)
#print(sorted_sequence_length)

GC_content = []
all_nt = 0
all_G  = 0
all_C = 0
for sequence in sequence_records:
    total_nt = len(sequence)
    all_nt+=total_nt
    G_count = sequence.count('G')
    C_count = sequence.count('C')
    all_G+=G_count
    all_C+=C_count
    GC_content_value = (G_count+C_count) / total_nt
    GC_content.append('{:.2%}'.format(GC_content_value))

avg_GC = (all_G+all_C)/all_nt
sorted_GC_content = sorted(GC_content)

print('sequence count:', sequence_count)        
print('total number of nucleotides:', num_nt)
print('average length:', '{:.1f}'.format(avg_seq_len))
print('shortest length:', sorted_sequence_length[0])
print('longest length:', sorted_sequence_length[-1])
print('average GC content:', '{:.2%}'.format(avg_GC))
print('lowest GC content:', sorted_GC_content[0])
print('highest GC content:', sorted_GC_content[-1])


