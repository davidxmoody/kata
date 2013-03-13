x, y = 999, 999

pals = []

def is_palindrome(num):
	strnum = str(num)
	for i in range(len(strnum)/2):
		if strnum[i]!=strnum[-1-i]:
			return False
	return True

while x>0:
	while y>0:
		if is_palindrome(x*y): pals.append(x*y)
		y -= 1
	x -= 1
	y = 999

print 'palindrome is:', max(pals)
