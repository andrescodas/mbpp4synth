def nCr(n, r): 
	if (r > n / 2): 
		r = n - r 
	answer = 1 
	for i in range(1, r + 1): 
		answer *= (n - r + i) 
		answer /= i 
	return answer 
def binomial_probability(n, k, p): 
	"""
	Write a function to compute binomial probability for the given number.
	"""
	return (nCr(n, k) * pow(p, k) *	pow(1 - p, n - k)) 
