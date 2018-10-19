#!/usr/bin/env python3
import re

nobody_file = open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_07_nobody.txt', 'r')


counter = 0
for line in nobody_file:
    found = re.search(r"Nobody", line)
    counter+=1
    print("line number:", counter, found)

milo = open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/milo.txt', 'w')


nobody_file = open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_07_nobody.txt', 'r')


for line in nobody_file:
    line = line.rstrip()
    new_lines = re.sub(r"Nobody", "Milo", line)
    milo.write(new_lines + '\n')

