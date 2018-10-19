#!/usr/bin/env python3

alpaca_all_genes = open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/alpaca_all_genes.tsv', 'r')
alpaca_stemcellproliferation_genes = open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/alpaca_stemcellproliferation_genes.tsv', 'r')
alpaca_pigmentation_genes = open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/alpaca_pigmentation_genes.tsv', 'r')
alpaca_transcriptionfactors = open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/alpaca_transcriptionFactors.tsv', 'r')

all_genes = set()
stemcellproliferation = set()
pigmentation = set()

for line in alpaca_all_genes:
    if line.startswith('ENS'):
        all_genes.add(line)

for line in alpaca_stemcellproliferation_genes:
    if line.startswith('ENS'):
        stemcellproliferation.add(line)

for line in alpaca_pigmentation_genes:
    if line.startswith('ENS'):
        pigmentation.add(line)




#print(all_genes)
#print(stemcellproliferation)
#print(pigmentation)

non_cell_proliferation = all_genes - stemcellproliferation
print('Genes that are not cell proliferation genes:', len(non_cell_proliferation))

both_stem_pigment = stemcellproliferation & pigmentation
print('Genes that are both step cell proliferation genes and pigment genes:', len(both_stem_pigment))

TF = set()

for line in alpaca_transcriptionfactors:
    if line.startswith('ENS'):
        TF.add(line)


TF_proliferation = TF &  stemcellproliferation
print('Geenes that are transcription factors for cell proliferation:', len(TF_proliferation))

TF_sort = sorted(TF)
stemcellproliferation_sort = sorted(stemcellproliferation)

TF_sort_write = open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/TF_sort.tsv', 'w')

TF_sort_write.write(str(TF_sort))

stemcellproliferation_sort_write = open('/Network/Servers/miniserve.cshl.edu/Volumes/KRAKEN/PFB2018/mwo/Desktop/problemsets/data/stemcellproliferation_sort.tsv', 'w')

stemcellproliferation_sort_write.write(str(stemcellproliferation_sort))

                     
