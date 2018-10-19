#!/usr/bin/env python3

file1 = open("/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_06.txt", "r")
#content = file1.read()
#print(content)

seq_write = open("/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_06_uc.txt", "w")

for line in file1:
    line = line.upper().rstrip()
    print(line)

#after a for loop, python automatically close the file, so need to reopen file
    
file1 = open("/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_06.txt", "r")
    
for line in file1:
    line = line.upper().rstrip()
    seq_write.write(line + '\n')


file1.close()
seq_write.close()

file2 = open("/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_06.seq.txt", "r")
#content = file2.read()
#print(content)

complement_dic = {'a':'T', 'c':'G','g':'C', 't':'A'}


for line in file2:
    line = line.rstrip().lower()
    id, seq = line.split()
    comp = ''
    for nt in seq:
        comp += complement_dic[nt]
    print(comp[::-1])    
    
file2.close()

fasta = open("/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/Python_06.fastq.txt", "r")

num_line = 0
num_char_total = 0
avg_line_length = 0

for line in fasta:
    line = line.rstrip()
    num_line += 1
    num_char_total += len(line)
print(num_line)
print(num_char_total)
avg =  num_char_total/num_line
print('average line length:', avg)


    
    
    
