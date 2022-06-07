def longest_increasing_subsequence(arr): 
	"""
	Write a function to find the length of the longest increasing subsequence of the given sequence.
	"""
	n = len(arr) 
	longest_increasing_subsequence = [1]*n 
	for i in range (1 , n): 
		for j in range(0 , i): 
			if arr[i] > arr[j] and longest_increasing_subsequence[i]< longest_increasing_subsequence[j] + 1 : 
				longest_increasing_subsequence[i] = longest_increasing_subsequence[j]+1
	maximum = 0
	for i in range(n): 
		maximum = max(maximum , longest_increasing_subsequence[i]) 
	return maximum
