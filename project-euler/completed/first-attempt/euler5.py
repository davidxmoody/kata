def prod(xs):
	total = 1
	for x in xs: total *= x
	return total

def is_div_by_all(num, xs):
	for x in xs:
		if num%x!=0: return False
	return True


nums = range(1, 21)
index = 0

while index<len(nums):
	sublist = nums[:index] + nums[index+1:]
	if is_div_by_all(prod(sublist), range(1, 21)):
		nums = sublist
	else: index += 1


print prod(nums)
