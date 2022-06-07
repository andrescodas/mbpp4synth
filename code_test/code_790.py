def even_position(nums):
	"""
	Write a python function to check whether every even index contains even numbers of a given list.
	"""
	return all(nums[i]%2==i%2 for i in range(len(nums)))
