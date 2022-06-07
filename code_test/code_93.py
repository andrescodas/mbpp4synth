def power(a,b):
	"""
	Write a function to calculate the value of 'a' to the power 'b'.
	"""
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)
