#!/usr/bin/env python3
import sys
import re
from Bio import SeqIO

#filename = sys.sgrv[1]

filename = '/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/CSHLProgForBiol2018/Exercise_2-aligned_reads_to_expression/bowtie2.sam'

names = []
with open(filename, 'r') as original_file:
    for line in original_file:
        line = line.rstrip()
        name = line.split('\t')
        names.append(name)
#print(names)

### pulling out gene name into a new list
#genes_plus = []        
#for entry in names:
#    genes_plus.append(entry[2])
#print(genes_plus)

### only pull out gene names
#genes = []
#for entry in genes_plus:
#    regex = re.search(r'(.+)(\^.+)', entry)
#    genes.append(regex.group(1))
#print(genes)

### build dictionary of gene:set of values

gene_dict = {}
reads_mapped = 0
for entry in names:
    name_plus = entry[2]
    regex = re.search(r'(.+)(\^.+)', name_plus)
    name = regex.group(1)
    value_set = set()
    if name not in gene_dict.keys():
        gene_dict[name]=value_set
    else:
        gene_dict[name].add(entry[0])

for gene in gene_dict:
    reads = len(gene_dict[gene])
    print(gene, '\t', reads)


#print(sorted(gene_dict['CG6024']))
    

    

    
