#!/usr/bin/env python3

with open('euler22-names.txt') as names_file:
    line = names_file.readlines()[0]

names = line.split(',')
names = [name[1:-1] for name in names]
names.sort()

total = 0

for i, name in enumerate(names):
    total += sum(ord(char)-96 for char in name.lower()) * (i+1)

print(total)
