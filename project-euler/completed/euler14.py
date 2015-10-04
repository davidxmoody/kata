#!/usr/bin/env python3

def step(n):
    if n%2==0:
        return n/2
    else:
        return 3*n + 1

def to_one(n):
    count = 0
    while n != 1:
        n = step(n)
        count += 1
    return count
    
def all_chains(highest):
    for i in range(1, highest):
        yield (i, to_one(i))
        

print(max( all_chains(1000000), key=(lambda x: x[1]) ))
