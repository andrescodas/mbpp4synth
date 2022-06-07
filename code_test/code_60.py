def max_len_sub( arr, n): 
	"""
	Write a function to find the maximum length of the subsequence with difference between adjacent elements for the given array.
	"""
	mls=[] 
	max = 0
	for i in range(n): 
		mls.append(1) 
	for i in range(n): 
		for j in range(i): 
			if (abs(arr[i] - arr[j]) <= 1 and mls[i] < mls[j] + 1): 
				mls[i] = mls[j] + 1
	for i in range(n): 
		if (max < mls[i]): 
			max = mls[i] 
	return max
