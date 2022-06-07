def group_tuples(Input): 
	"""
	Write a function to find common first element in given list of tuple.
	"""
	out = {} 
	for elem in Input: 
		try: 
			out[elem[0]].extend(elem[1:]) 
		except KeyError: 
			out[elem[0]] = list(elem) 
	return [tuple(values) for values in out.values()] 
