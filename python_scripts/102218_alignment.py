#!/usr/bin/env python3
import sys

def reverse_complement(x):
    upper_case = x.upper()
    complement = upper_case.replace('T','a')
    complement_1 = complement.replace('G','c')
    complement_2 = complement_1.replace('A', 't')
    complement_3 = complement_2.replace('C', 'g')
    reverse_complement = complement_3[::-1]
    list_RC = list(reverse_complement)
    return list_RC

sequence1 = 'agtctgtca'
sequence2 = 'gatctctgc'
sequence1 = input('Enter sequence 1:')
sequence2 = input('Enter sequence 2:')


list_seq1 = list(sequence1)
list_seq2 = list(sequence2)
length = len(list_seq1)

alignment_score_1 = 0

for num in range(0,length):
    if list_seq1[num]==list_seq2[num]:
        alignment_score_1+=1
    else:
        alignment_score_1-=1
print(alignment_score_1)

rc_seq1_user = input('Do you want the reverse complement of sequence 1?')



rc_seq1 = reverse_complement(sequence1)
rc_seq2 = reverse_complement(sequence2)


alignment_score_2 = 0
if rc_seq1_user == 'yes':
    for num in range(0,length):
        if rc_seq1[num]==list_seq2[num]:
            alignment_score_2+=1
        else:
            alignment_score_2-=1
print(alignment_score_2)

rc_seq2_user = input('Do you want the reverse complement of sequence 2?')

alignment_score_3 = 0
if rc_seq2_user == 'yes':
    for num in range(0,length):
        if list_seq1[num]==rc_seq2[num]:
            alignment_score_3+=1
        else:
            alignment_score_3-=1
print(alignment_score_3)

rc_both_user = input('Do you want the reverse complement of both sequences?')

alignment_score_4 = 0

if rc_both_user == 'yes':
    for num in range(0,length):
        if rc_seq1[num]==rc_seq2[num]:
            alignment_score_4+=1
        else:
            alignment_score_4-=1
print(alignment_score_4)
