#!/usr/bin/env python3
import re

RE_list = open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/bionet.txt', 'r')

RE_dict = {}
for line in RE_list:
    line = line.rstrip()
    for data in re.finditer(r"(\w+\(?.*\)?\S)(\s{7,40})([\w^]+)", line):
        key = data.group(1)
        site = data.group(3) 
        RE_dict[key] = site

print(RE_dict)
    
