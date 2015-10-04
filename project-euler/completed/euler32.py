#!/usr/bin/env python3

def check(x, y, digits=sorted('123456789')):
    return sorted(str(x)+str(y)+str(x*y))==digits


nums = []

for x in range(1, 100):
    for y in range(100, 9999):
        if check(x, y) and x*y not in nums:
            nums.append(x*y)

print(sum(nums))
