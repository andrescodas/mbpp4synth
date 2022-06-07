def number_of_substrings(str): 
	"""
	Write a python function to count number of non-empty substrings of a given string.
	"""
	str_len = len(str); 
	return int(str_len * (str_len + 1) / 2); 
