#!/usr/bin/env python3

sumsq = sum([i**2 for i in range(1, 101)])
sqsum = sum(range(1, 101))**2

print(sqsum-sumsq)
