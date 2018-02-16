"""
Find the number of negative numbers in a column-wise / row-wise sorted matrix M[][].

With the given example:
[-3, -2, -1,  1]
[-2,  2,  3,  4]
[4,   5,  7,  8]

Here's the idea:
[-3, -2,  ↓,  ←] -> Found 3 negative numbers in this row
[ ↓,  ←,  ←,  4] -> Found 1 negative number in this row
[ ←,  5,  7,  8] -> No negative numbers in this row

Time complexity O(n + m)
"""
def countNegative(M, n, m):
	count = 0 # initialize result

	# Start with top right corner
	i = 0
	j = m - 1

	# Follow the path shown using arrows above
	while j >= 0 and i < n:
		if M[i][j] < 0:
			# j is the index of the last negative number
			# in this row.  So there must be ( j+1 )
			count += (j + 1)
			# negative numbers in this row.
			i += 1
		else:
			# move to the left and see if we can
			# find a negative number there
			j -= 1
	return count

M = [
  [-3, -2, -1,  1],
  [-2,  2,  3,  4],
  [ 4,  5,  7,  8]
]

print(M)
print(countNegative(M, 3, 4))
