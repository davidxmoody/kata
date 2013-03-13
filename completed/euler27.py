#!/usr/bin/env python3

from itertools import count
import euler

def num_primes(formula):
    for i in count():
        if not euler.is_prime(formula(i)):
            return i

highest = 0
highest_ab = 0

for a in range(-999, 1000):
    print(a)
    for b in range(-999, 1000):
        num = num_primes(lambda n: n**2 + a*n + b)
        if num >= highest:
            highest = num
            highest_ab = a*b

print(highest_ab)
