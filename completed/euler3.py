#!/usr/bin/env python3

from euler import primes_below

num = 600851475143

for i in primes_below(num):
    if num%i==0:
        num /= i
        if num==1:
            print(i)
            break
