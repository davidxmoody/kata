#!/usr/bin/env python3

from itertools import combinations_with_replacement

print(max([x*y for x, y in combinations_with_replacement(range(999, 0, -1), 2) if str(x*y)==str(x*y)[::-1]]))
