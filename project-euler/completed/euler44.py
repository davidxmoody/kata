from queue import PriorityQueue
import sys
from itertools import count

def pentagonal(n):
    return int(n*(3*n-1)/2)

numbers = []

def is_pentagonal(p):
    while True:
        if p<numbers[-1]: break
        numbers.append(pentagonal(len(numbers)+1))
    return p in numbers

for s in (pentagonal(n) for n in count(1)):
    numbers.append(s)
    for pk in numbers:
        if pk>=s: break
        pj = s-pk
        d = pk-pj
        if d>0 and pj in numbers and d in numbers:
            print(d)
            sys.exit()
