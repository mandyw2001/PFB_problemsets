#!/usr/bin/env python3

values = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
values_it = iter(values)
for value in values_it:
    if value%2==0:
        print(value)
    
for value in sorted(values):
    print(value)
