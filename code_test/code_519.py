import math
def volume_tetrahedron(num):
	"""
	Write a function to calculate volume of a tetrahedron.
	"""
	volume = (num ** 3 / (6 * math.sqrt(2)))	
	return round(volume, 2)
