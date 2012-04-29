#!/usr/bin/env python3

from math import sqrt

prime_list = [2, 3]
highest_tried = 3

def build_prime_list(limit):
    global highest_tried
    for i in range(highest_tried+2, limit+1, 2):
        sqrti = sqrt(i)
        divisible = False
        for p in prime_list:
            if p > sqrti: 
                break
            if i%p==0:
                divisible = True
                break
        if not divisible:
            prime_list.append(i)
        highest_tried = i

def is_prime(num):
    if num > highest_tried:
        build_prime_list(num)
    return num in prime_list

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
