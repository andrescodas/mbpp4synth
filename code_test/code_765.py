import math 
def is_polite(n): 
	"""
	Write a function to find nth polite number.
	"""
	n = n + 1
	return (int)(n+(math.log((n + math.log(n, 2)), 2))) 
