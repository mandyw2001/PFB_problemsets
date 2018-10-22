#!/usr/bin/env python3

from Bio import SeqIO
from BCBio.GFF import GFFExaminer

gff_file = '/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/protien_coding_genes.gff'

in_handle = open(gff_file)
for rec in GFF.parse(in_handle):
    print(rec)
in_handle.close()
