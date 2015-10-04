#!/usr/bin/env python3

from math import factorial

print(sum( n for n in range(3, 2540160) if n==sum(factorial(int(i)) for i in str(n)) ))
