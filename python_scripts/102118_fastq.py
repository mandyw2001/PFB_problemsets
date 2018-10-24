#!/usr/bin/env python3

from Bio import SeqIO

num_quality_nt = {}

with open("/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/trimmed_fastq.fastq", "w") as trimmed:
    for entry in SeqIO.parse('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/four_reads.fastq', 'fastq'):
        gene_name = entry.id
        sequence = entry.seq
        #quality_score = entry.letter_annotations
        quality_score2 = entry.letter_annotations['phred_quality']
        entry_trimmed = entry[5:]
        SeqIO.write(entry_trimmed, trimmed, "fastq")
        num_quality_nt[gene_name]=[quality_score2]

print(num_quality_nt)
#print(type(quality_score2))
#print(type(num_quality_nt['ST-E00273:259:H7WY3ALXX:1:2224:28929:73088']['phred_quality']))
      
high_quality_nt = {}
high_quality_count = 0
for gene in num_quality_nt:
    for scores in num_quality_nt[gene]:
        total_nt_after_trim = len(scores)
        for score in scores:
            if score > 30:
                high_quality_count+=1
                #print(high_quality_count)
                fraction_quality_nt = high_quality_count / total_nt_after_trim
                high_quality_nt[gene]=high_quality_count, '{:.2%}'.format(fraction_quality_nt)
    high_quality_count = 0
                
print(high_quality_nt)

