#!/usr/bin/env python3
import re

sequence = open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_07_ApoI.fasta.txt', 'r')

for line in sequence:
    found = re.findall(r"[AG]AATT[CT]", line)
    if found:
        print(found)

sequence = open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_07_ApoI.fasta.txt', 'r')



long_seq = ''
for line in sequence:
    line = line.strip()
    if not re.search(r"^>", line): #remove header line
        new_seq = re.sub(r"([AG])(AATT[CT])", r"\1^\2", line)
        long_seq+= new_seq
print(long_seq)


list_seq =long_seq.split("^")
print(list_seq)


length_list = []
for seq in list_seq:
    length_list.append(len(seq))
print(length_list)
    
print(sorted(length_list))

