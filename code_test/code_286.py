def max_sub_array_sum_repeated(a, n, k): 
	"""
	Write a function to find the largest sum of contiguous array in the modified array which is formed by repeating the given array k times.
	"""
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far
