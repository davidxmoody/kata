#!/usr/bin/env python3

def primes_below(num=1000000000):
    primes = [2]
    yield 2
    for i in range(3, num, 2):
        if not any((i%p==0 for p in primes)):
            primes.append(i)
            yield i
