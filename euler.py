#!/usr/bin/env python3

def primes_below(num):
    primes = []
    for i in range(2, num):
        if not any([i%p==0 for p in primes]):
            primes.append(i)
            yield i
