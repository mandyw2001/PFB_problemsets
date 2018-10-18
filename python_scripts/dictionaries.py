#!/usr/bin/env python3

fav = {'book':'Jitterbug Perfume', 'song': 'Tom Petty', 'tree': 'cedar'}
print(fav)

print(fav['book'])
fav_thing = 'book'
print(fav[fav_thing])
print(fav['tree'])
fav['organism']='cat'
fav_thing = 'organism'
print(fav[fav_thing], '\n')

cat_list = []
for cat in fav:
    cat_list.append(cat)
print('Options:', cat_list)

fav_thing = input("Enter your favorite thing: ")
print ("Received input is: ", fav_thing)
print(fav[fav_thing], '\n')

fav['organism']='jellyfish'

fav_thing = input("Enter your favorite type of thing: ")
value_fav_thing = input("enter your favorite thing in that type: ")
fav[fav_thing]=value_fav_thing

print(fav, '\n')

for cat in fav:
    thing = fav[cat]
    print(cat, thing)

    
