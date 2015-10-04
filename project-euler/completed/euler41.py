from itertools import permutations
import math

def is_prime(num):
    for i in range(2, math.floor(math.sqrt(num))+1):
        if num%i==0: return False
    return True

def gen_pandigital(num_digits):
    for perm in permutations(range(1, num_digits+1)):
        yield combine_digits(perm)

def combine_digits(digits):
    result = 0
    for index, digit in enumerate(digits):
        result += digit*10**index
    return result

max_pan = 0
for i in range(10):
    for pan in gen_pandigital(i):
        if pan>max_pan and is_prime(pan):
            max_pan = pan

print(max_pan)
