#!/usr/bin/env python3

def unit_fraction(d):
    n = 10
    while True:
        yield n//d, n%d
        n = 10*(n%d)

def longest_chain(d):
    encountered = []
    for pair in unit_fraction(d):
        if pair in encountered:
            return len(encountered[encountered.index(pair):])
        else:
            encountered.append(pair)

length2d = { longest_chain(d): d for d in range(1, 1000) }
print(length2d[max(length2d.keys())])
