#!/usr/bin/env python3

import sys

low_value = int(sys.argv[1])
high_value = int(sys.argv[2])

for values in range(low_value, high_value+1):
    print(values)

for values in range(low_value, high_value+1):
    if values%2==1:
        print(values)

seq_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for seq in seq_list:
    print(seq)

for seq in seq_list:
    print(len(seq),'\t', seq)

print('\n\n')

tuple_list = [len(seq) for seq in seq_list]# '\t' seq '\n']
print(tuple_list)
print(type(tuple_list))
