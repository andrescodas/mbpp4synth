def sort_on_occurence(lst): 
	"""
	Write a function to sort the given list based on the occurrence of first element of tuples.
	"""
	dct = {} 
	for i, j in lst: 
		dct.setdefault(i, []).append(j) 
	return ([(i, *dict.fromkeys(j), len(j)) 
				for i, j in dct.items()]) 
