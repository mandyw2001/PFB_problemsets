#!/usr/bin/env python3

import sys
import re

input_file = ''
try:
    input_file = sys.argv[1]
    print("User provided file:", input_file)
except:
    print("please provide a fasta file name")


with open(input_file, 'r') as open_file:

    fasta_dict = {}
    
    for line in open_file:
        line = line.rstrip()
        header = re.search(r"(>\S+)", line)
        if header: 
            seq_name = header.group(1)
            fasta_dict[seq_name]={'A':0, 'T':0, 'G':0, 'C':0 }
        else:
            for nt in line:
                fasta_dict[seq_name][nt]+=1      
               
print(fasta_dict)
             
