factors = []

i = 600851475143

x = 2

while i>1:
	if i%x==0: 
		factors.append(x)
		i /= x
		print factors
	else: x += 1
