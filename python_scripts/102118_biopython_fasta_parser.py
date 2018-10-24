#!/usr/bin/env python3
from Bio import SeqIO

filename = "/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_08.fasta.txt"

#filename = "/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/test.fa"

sequence_count = 0
num_nt = 0

for entry in SeqIO.parse(filename, "fasta"):
    ids = entry.id
    descriptions = entry.description
    sequences = entry.seq
    #print('ID:', ids)
    #print('description', descriptions)
    #print('sequence:', sequences)
    
    if ids:
        sequence_count+=1
    for sequence in sequences:
        num_nt+=1

avg_seq_len = num_nt/sequence_count

        
print(sequence_count)        
print(num_nt)
print('{:.1f}'.format(avg_seq_len))
    
