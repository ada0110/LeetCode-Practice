# Python implementation of the approach
def find( m, q):
	mx = 0
	org = [10 for i in range(5)]
	pre = [0 for i in range(5)]
	
	for i in range(m):
		# take input a and b
		a,b = q[i][0], q[i][1]
	
		# add 100 at first index and
		# subtract 100 from last index
	
		# pre[1] becomes 100
		pre[a] += 100
		
		# pre[4] becomes -100 and this
		pre[b] -= 100
		
		# continues m times as we input diff. values of a and b
	for i in range(1,5):
	
		# add all values in a cumulative way
		pre[i] += pre[i - 1]
		
		# keep track of max value
		mx = max(mx, pre[i])

	# print(f"pref: {pre}\norg:{org}")

	org = [elem[0]+elem[1] for elem in zip(pre, org)]
	# org = [p+o for p,o in zip(pre, org)]	
	print(f"pref: {pre}\norg:{org}")						
	return max(org)

# Driver Code
m = 2
q = [[1,3], [0,2]]

# Function call
print(find(m,q))

# This code is contributed by rohitsingh07052
