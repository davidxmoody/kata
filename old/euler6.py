# Find sum of squares.
sumsq = 0
for i in range(1, 101): sumsq += i*i

# Find square of sums.
sqsum = 100/2*(100+1)
sqsum *= sqsum

# Print difference.
print sqsum, '-', sumsq, '=', sqsum - sumsq
