def get_carol(n): 
	"""
	Write a function to find the n’th carol number.
	"""
	result = (2**n) - 1
	return result * result - 2
