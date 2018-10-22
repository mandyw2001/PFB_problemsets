#!/usr/bin/env python3

class DNA_seq_org(object):
    def __init__(self, sequence, gene_name, species_name):
        self.sequence = sequence
        self.gene_name = gene_name
        self.species_name = species_name

    def length(self):
        length = len(self.sequence)
        return length

    def nt_comp(self):
        length = len(self.sequence)
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        g_count = self.sequence.count('G')
        c_count = self.sequence.count('C')
        a_content = a_count/length
        t_content = t_count/length
        g_content = g_count/length
        c_content = c_count/length
        nt_content = ('A:'+'{:.2%}'.format(a_content)+', T:'+'{:.2%}'.format(t_content)+', G:'+'{:.2%}'.format(g_content)+', C:'+'{:.2%}'.format(c_content))
        return nt_content

    def gc_content(self):
        length = len(self.sequence)
        g_count = self.sequence.count('G')
        c_count = self.sequence.count('C')
        gc = (g_count+c_count)/length
        gc_content = '{:.2%}'.format(gc)
        return gc_content

    def fasta_formatter(self):
        fasta_format = '>'+self.gene_name+'\n'+self.sequence+'\n'
        return fasta_format

dna_BRCA2 = DNA_seq_org('ACTGATCGTTACGTACGAATC', 'BRCA2', 'Homo sapiens')

print('sequence:', dna_BRCA2.sequence)
print('name:', dna_BRCA2.gene_name)
print('species', dna_BRCA2.species_name)
print('length:', DNA_seq_org.length(dna_BRCA2))
print('nucleotide composition:', DNA_seq_org.nt_comp(dna_BRCA2))
print('GC content:', DNA_seq_org.gc_content(dna_BRCA2))
print('fasta format:\n'+DNA_seq_org.fasta_formatter(dna_BRCA2))

