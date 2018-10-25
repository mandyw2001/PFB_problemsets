#!/usr/bin/env python3
import sys
from Bio import SeqIO

#kmer_length = sys.sgrv[1]
#filename = sys.sgrv[2]
#num_top_kmers = sys.sgrv[3]

filename = '/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/CSHLProgForBiol2018/Exercise_1-counting_kmers/reads.fq'

num_line = 0
list_of_kmers = []

for entry in SeqIO.parse (filename, 'fastq'):
    sequence_raw = str(entry.seq)
    sequences = sequence_raw.rstrip()
    num_line+=1
    
    length = len(sequences)
    left_num = 0
    right_num = 8  ###right_num will equal to kmer_length when doing sys
    #print(sequences[left_num:right_num])
    
    for pos in range(length):
        if right_num <= length:
            list_of_kmers.append(sequences[left_num:right_num])
            #print(sequences[left_num:right_num])
        left_num+=1
        right_num+=1
            

print('nt per sequence =', len(sequences))
print('number of lines =', num_line)
print('number of kmers=', len(list_of_kmers))

    




kmer_dict = {}

for kmer_seq in list_of_kmers:
    if kmer_seq not in kmer_dict.keys():
        kmer_dict[kmer_seq]=1
    else:
        kmer_dict[kmer_seq]+=1
#print(kmer_dict)

## sort by value, return key
kmer_sorted = sorted(kmer_dict, key=kmer_dict.get , reverse=True)

top_kmer = kmer_sorted[0:10] ###num_top_kmers will equal to the top value here when doing sys
#print(top_kmer)

for kmer in top_kmer:
    print(kmer, '\t', kmer_dict[kmer])
