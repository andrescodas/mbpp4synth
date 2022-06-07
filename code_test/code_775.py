def odd_position(nums):
	"""
	Write a python function to check whether every odd index contains odd numbers of a given list.
	"""
	return all(nums[i]%2==i%2 for i in range(len(nums)))
