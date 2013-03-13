from itertools import permutations
from math import sqrt

def satisfies(ab):
	a, b = ab
	c = sqrt(a*a + b*b)
	return a<b<c and a + b + c == 1000

ab_pairs = set(permutations(range(1, 1000), 2))

ab_pairs = filter(satisfies, ab_pairs)

a, b = ab_pairs[0]
c = int(sqrt(a*a + b*b))

print 'a =', a
print 'b =', b
print 'c =', c
print 'a*b*c =', int(a*b*c)
