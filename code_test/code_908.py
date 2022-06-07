def find_fixed_point(arr, n): 
	"""
	Write a function to find the fixed point in the given array.
	"""
	for i in range(n): 
		if arr[i] is i: 
			return i 
	return -1
