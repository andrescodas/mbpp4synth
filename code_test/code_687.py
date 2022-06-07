def recur_gcd(a, b):
	"""
	Write a function to find the greatest common divisor (gcd) of two integers by using recursion.
	"""
	low = min(a, b)
	high = max(a, b)
	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return recur_gcd(low, high%low)
