import sys 
def find_max_val(n, x, y): 
	"""
	Write a function to find the largest possible value of k such that k modulo x is y.
	"""
	ans = -sys.maxsize 
	for k in range(n + 1): 
		if (k % x == y): 
			ans = max(ans, k) 
	return (ans if (ans >= 0 and
					ans <= n) else -1) 
