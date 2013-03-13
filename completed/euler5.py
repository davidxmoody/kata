#!/usr/bin/env python3

from operator import mul
from functools import reduce
from itertools import combinations

def check(num):
    return all([num%i==0 for i in range(1, 21)])


nums = list(range(1, 21))
product = 0

while True:
    for i in nums:
        nums.remove(i)
        if check(reduce(mul, nums)):
            continue
        nums.append(i)

    product, old_product = reduce(mul, nums), product
    if product == old_product: break
    print(sorted(nums), product)
