#!/usr/bin/env python3
import re

fasta_file = open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_07.fasta.txt', 'r')


for line in fasta_file:
    line = line.strip()
    headers = re.findall(r">.+", line)
    #if headers:
        #print(headers)
    for match in re.finditer(r">(\S+)(\s)(.*)", line):
        print("ID:", match.group(1))
        print("desc:", match.group(3))
