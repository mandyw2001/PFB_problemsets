#!/usr/bin/env python3

values = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
values_it = iter(values)
for value in values_it:
    if value%2==0:
        print(value)

print('\n\n')

Sum_even = 0
Sum_odd = 0
for value in sorted(values):
    print(value)
    if value%2==0:
        Sum_even+=value
    else:
        Sum_odd+=value
print('Sum of even numbers =', Sum_even)
print('Sum of odd numbers =', Sum_odd, '\n')

for values in range(100):
    print(values)

print('\n\n')

for values in range(100):
    print(values+1)


values = [value+1 for value in range(100)]
print(values)
        
        
