def is_subset(arr1, m, arr2, n): 
	"""
	Write a function to find whether an array is subset of another array.
	"""
	hashset = set() 
	for i in range(0, m): 
		hashset.add(arr1[i]) 
	for i in range(0, n): 
		if arr2[i] in hashset: 
			continue
		else: 
			return False
	return True		
