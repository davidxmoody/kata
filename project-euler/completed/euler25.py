#!/usr/bin/env python3

def mkfib():
    a, b, i = 1, 1, 1
    while True:
        yield i, a
        a, b, i = b, a+b, i+1


for i, num in mkfib():
    if len(str(num)) >= 1000:
        print(i)
        break
