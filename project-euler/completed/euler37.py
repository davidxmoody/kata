#!/usr/bin/env python3

from euler import is_prime
from itertools import islice
from math import sqrt

def is_prime(num):
    if num == 1: return False
    for i in range(2, int(sqrt(num)+1)):
        if num%i==0:
            return False
    return True

def lchain(number):
    if number < 10: return is_prime(number)
    return is_prime(number) and lchain(int(str(number)[:-1]))

def rchain(number):
    if number < 10: return is_prime(number)
    return is_prime(number) and rchain(int(str(number)[1:]))

def lrchain(number):
    return lchain(number) and rchain(number)

def all_chains():
    for i in range(1000000000):
        if lrchain(i):
            yield i


def genl(nums=[2, 3, 5, 7], possible=list(range(1, 10))):
    for n in nums:
        for p in possible:
            new = int(str(n) + str(p))
            if is_prime(new): 
                yield new

def recl(num):
    if num == 0:
        return genl()
    else:
        return genl(recl(num-1))
        

def genr(nums=[2, 3, 5, 7], possible=list(range(1, 10))):
    for n in nums:
        for p in possible:
            new = int(str(p) + str(n))
            if is_prime(new): 
                yield new

def recr(num):
    if num == 0:
        return genr()
    else:
        return genr(recr(num-1))

total = 0

for i in range(10):
    for l in recl(i):
        for r in recr(i):
            if l == r:
                total += l

print(total)
