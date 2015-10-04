#!/usr/bin/env python3

def prop_divisors(n):
    for i in range(1, n//2+1):
        if n%i==0:
            yield i

def amicable_below(upper):
    dnmap = {n: sum(prop_divisors(n)) for n in range(1, upper)} 
    for n, dn in dnmap.items():
        if dn in dnmap:
            if dnmap[dn] == n and n != dn:
                yield n

print(sum(amicable_below(10000)))
