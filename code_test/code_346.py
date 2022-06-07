def zigzag(n, k): 
	"""
	Write a function to find entringer number e(n, k).
	"""
	if (n == 0 and k == 0): 
		return 1
	if (k == 0): 
		return 0
	return zigzag(n, k - 1) + zigzag(n - 1, n - k)
