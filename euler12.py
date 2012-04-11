#!/usr/bin/env python3

# tri(n) = SUM from 1 to n of (n) = n/2(n+1)
# Need to find smallest n/2(n+1) which has at least 500 divisors

def get_triangles():
    i = 2
    tri = 1
    while True:
        yield tri
        tri += i
        i += 1

for tri in get_triangles():
    num_factors = 1
    for i in range(1, tri//2):
        if tri%i==0:
            num_factors += 1
    print(tri, num_factors)
    if num_factors > 500:
        print(tri)
        break
