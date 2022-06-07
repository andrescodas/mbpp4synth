def count_range_in_list(li, min, max):
	"""
	Write a function to count the number of elements in a list which are within a specific range.
	"""
	ctr = 0
	for x in li:
		if min <= x <= max:
			ctr += 1
	return ctr
