def gen_self_powers(n):
    for i in range(1, n+1):
        yield i**i

print(str(sum(gen_self_powers(1000)))[-10:])
