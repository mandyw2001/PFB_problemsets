#!/usr/bin/env python3

taxa = 'sapiens, erectus, neanderthalensis'
print(taxa)
print(taxa[1])
print(type(taxa), '\n')


species = taxa.split(',')
print(species)
print(species[1])
print(type(species), '\n')


species_sorted = sorted(species)
print(species_sorted)

species_sort_by_len = sorted(species, key=len)
print(species_sort_by_len)



