#!/usr/bin/env python3

# a**2 + b**2 = c**2
# a + b + c = 1000

from itertools import combinations
from math import sqrt, floor

for a, b in combinations(range(1, 500), 2):
    c2 = a**2 + b**2
    c = floor(sqrt(c2))
    if c**2 != c2: 
        continue
    if a + b + c == 1000:
        print(a*b*c)
        break
