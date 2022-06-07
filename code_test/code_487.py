def sort_tuple(tup): 
	"""
	Write a function to sort a list of tuples in increasing order by the last element in each tuple.
	"""
	lst = len(tup) 
	for i in range(0, lst): 
		for j in range(0, lst-i-1): 
			if (tup[j][-1] > tup[j + 1][-1]): 
				temp = tup[j] 
				tup[j]= tup[j + 1] 
				tup[j + 1]= temp 
	return tup
