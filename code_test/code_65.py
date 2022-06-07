def recursive_list_sum(data_list):
	"""
	Write a function of recursion list sum.
	"""
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element
	return total
