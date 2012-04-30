#!/usr/bin/env python3

nums = []

for i in range(2, 1000000):
    if i == sum(int(c)**5 for c in str(i)):
        nums.append(i)

print(sum(nums))
