#!/usr/bin/env python3

print(sum( i for i in range(2, (9**5)*6) if i == sum(int(c)**5 for c in str(i)) ))
