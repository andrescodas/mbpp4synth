def maximum_segments(n, a, b, c) : 
	"""
	Write a function to find the maximum number of segments of lengths a, b and c that can be formed from n.
	"""
	dp = [-1] * (n + 10) 
	dp[0] = 0
	for i in range(0, n) : 
		if (dp[i] != -1) : 
			if(i + a <= n ): 
				dp[i + a] = max(dp[i] + 1, 
							dp[i + a]) 
			if(i + b <= n ): 
				dp[i + b] = max(dp[i] + 1, 
							dp[i + b]) 
			if(i + c <= n ): 
				dp[i + c] = max(dp[i] + 1, 
							dp[i + c]) 
	return dp[n]
