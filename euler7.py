#!/usr/bin/env python3

from euler import primes_below

i = 0
for p in primes_below():
    i += 1
    print(i, p)
    if i==10001: 
        break
