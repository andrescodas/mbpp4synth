def newman_prime(n): 
	"""
	Write a function to find the nth newman–shanks–williams prime number.
	"""
	if n == 0 or n == 1: 
		return 1
	return 2 * newman_prime(n - 1) + newman_prime(n - 2)
