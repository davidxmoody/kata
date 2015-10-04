i = 3
primes = [2]

def div_by_none(x, ls):
	for l in ls:
		if x%l==0: return False
	else: return True

while len(primes)<10001:
	if div_by_none(i, primes): primes.append(i)
	i += 2

print primes[9993:]
