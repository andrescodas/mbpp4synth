def find_lucas(n): 
	"""
	Write a function to find the n'th lucas number.
	"""
	if (n == 0): 
		return 2
	if (n == 1): 
		return 1
	return find_lucas(n - 1) + find_lucas(n - 2) 
