#!/usr/bin/env python3
from Bio import SeqIO
import re
import sys

#fasta_filename = '/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_08.fasta.txt'

output_file = open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_08.codons-frame-1.nt', 'w')

class NotDNAError(Exception):
    pass

### if no input is provided
try:
    fasta_filename = sys.argv[1]
    print('User provided file name:', fasta_filename)
    if not fasta_filename.endswith('txt'):
        raise ValueError ('Not a FASTA file')
    fasta = open(fasta_filename, 'r')
    open_fasta = SeqIO.parse(fasta, 'fasta')
except IndexError:
    print('Please provide a file name')
    exit
except IOError:
    print('Can\'t find file:', fasta_filename)
    exit
except ValueError:
    print('File needs to be a FASTA file')
    exit


for entry in open_fasta:
    ids = entry.id
    sequences = str(entry.seq)
    try: 
        if re.findall(r'[^ATGCN]', sequences):
            raise NotDNAError('non-DNA characters found')
    except NotDNAError:
        print('Non-DNA characters found')
        exit
        
    print(ids+'frame-1-codons')
    output_file.write(ids+'-frame-1-codons\n')
    codons1 = re.findall(r'(.{3})', sequences)
    codons1_separated_by_white_space = ' '.join(codons1)
    print(codons1_separated_by_white_space)
    output_file.write(codons1_separated_by_white_space+'\n')
    
    print(ids+'frame-2-codons')
    reading_frame_2 = sequences[1:]
    codons2 =  re.findall(r'(.{3})', reading_frame_2)
    codons2_separated_by_white_space = ' '.join(codons2)
    print(codons2_separated_by_white_space)

    print(ids+'frame-3-codons')
    reading_frame_3 = sequences[2:]
    codons3 =  re.findall(r'(.{3})', reading_frame_3)
    codons3_separated_by_white_space = ' '.join(codons3)
    print(codons3_separated_by_white_space)


    
