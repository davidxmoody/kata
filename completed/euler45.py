from itertools import count

def gen_triangle():
    for n in count(1):
        yield int(n*(n+1)/2)

def gen_pentagonal():
    for n in count(1):
        yield int(n*(3*n-1)/2)

def gen_hexagonal():
    for n in count(1):
        yield n*(2*n-1)

gens = gen_triangle(), gen_pentagonal(), gen_hexagonal()
a, b, c = [(gen.__next__(), gen) for gen in gens]

while True:
    if a[0] == b[0] == c[0]: print(a[0])
    a, b, c = sorted( ((a[1].__next__(), a[1]), b, c), key=(lambda x: x[0]))
