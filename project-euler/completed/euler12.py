#!/usr/bin/env python3

import math

def get_triangles():
    i = 2
    tri = 1
    while True:
        yield tri
        tri += i
        i += 1

def num_factors(n):
    # Note that this will be off by one for 1 or for a square number.
    result = 0
    for i in range(1, math.floor(math.sqrt(n))+1):
        if n%i==0: 
            result += 2
    return result


for tri in get_triangles():
    if num_factors(tri) > 500:
        print(tri)
        break
