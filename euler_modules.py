def primes_below(x):
	
	primes = []
	i = 3
	
	if x>2: primes.append(2)
	
	while i<x:
		if isprime(i): primes.append(i)
		i += 2
	
	return primes


def div_by_none(x, ls):
	for l in ls:
		if x%l==0: return False
	else: return True


def isprime(x):
	if x<2: return False
	if x=2: return True
	if x%2==0: return False
	
	for i in range(3, int(x**0.5)+1, 2):
		if x%i==0: return False
	return True

