#!/usr/bin/env python3
from Bio import SeqIO
import re

fasta_filename = '/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_08.fasta.txt'

output_file = open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_08.codons-frame-1.nt', 'w')

for entry in SeqIO.parse(fasta_filename, "fasta"):
    ids = entry.id
    sequences = str(entry.seq)
    print(ids)
    output_file.write(ids+'-frame-1-codons\n')
    #print(sequences)
    codons = re.findall(r'(.{3})', sequences)
    codons_separated_by_white_space = ' '.join(codons)
    print(codons_separated_by_white_space)
    output_file.write(codons_separated_by_white_space+'\n')
    
