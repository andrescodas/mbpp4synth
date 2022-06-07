def sum_three_smallest_nums(lst):
	"""
	Write a python function to find the sum of the three lowest positive numbers from a given list of numbers.
	"""
	return sum(sorted([x for x in lst if x > 0])[:3])
