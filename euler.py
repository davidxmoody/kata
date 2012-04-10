#!/usr/bin/env python3

from math import sqrt

def primes_below(num=1000000000):
    primes = [2]
    yield 2
    for i in range(3, num, 2):
        if not any((i%p==0 for p in primes)):
            primes.append(i)
            yield i


def primes_below_efficient(num=1000000000):
    primes = [2]
    yield 2
    for i in range(3, num, 2):
        divisible = False
        sqrti = sqrt(i)
        for p in primes:
            if p > sqrti: continue
            if i%p==0: 
                divisible = True
                break
        if not divisible:
            primes.append(i)
            yield i


def prod(xs):
    total = 1
    for x in xs:
        total *= x
    return total
