#!/usr/bin/env python3

from Bio import SeqIO


fasta_dict = SeqIO.to_dict(SeqIO.parse('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/human_cds.fasta', 'fasta'))

#print(fasta_dict)

nt_count_dict = {}
total_nt_count = 0

for gene in fasta_dict:
    sequences = fasta_dict[gene].seq
    #nt_count_dict[gene]=len(sequences)
    total_nt_count += len(sequences)
    G_count = sequences.count('G')
    C_count = sequences.count('C')
    GC_content = (G_count + C_count)/len(sequences)
    GC_percent = '{:.2%}'.format(GC_content)
    nt_count_dict[gene]=[len(sequences),GC_percent]
    
print(nt_count_dict)
print(total_nt_count)
    
with open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/fasta_dict_GC.txt', 'w') as output_file:
    output_file.write('Gene ID\tPercent GC\n')
    for gene in nt_count_dict:
        output_file.write(gene+'\t'+nt_count_dict[gene][1]+'\n')
    
