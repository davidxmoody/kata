#!/usr/bin/env python3

fibs = [1, 1]
while fibs[-1] < 4000000:
    fibs.append(fibs[-1]+fibs[-2])

print(sum([i for i in fibs if i%2==0]))
