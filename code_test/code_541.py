import math 
def get_sum(n): 
	sum = 0
	i = 1
	while i <= (math.sqrt(n)): 
		if n%i == 0: 
			if n/i == i : 
				sum = sum + i 
			else: 
				sum = sum + i 
				sum = sum + (n / i ) 
		i = i + 1
	sum = sum - n 
	return sum
def check_abundant(n): 
	"""
	Write a function to find if the given number is abundant or not.
	"""
	if (get_sum(n) > n): 
		return True
	else: 
		return False
