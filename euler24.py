#!/usr/bin/env python3

from itertools import permutations

print(''.join(list(permutations(sorted('0123456789')))[999999]))
