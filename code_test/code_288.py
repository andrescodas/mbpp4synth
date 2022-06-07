def modular_inverse(arr, N, P):
	"""
	Write a function to count array elements having modular inverse under given prime number p equal to itself.
	"""
	current_element = 0
	for i in range(0, N):
		if ((arr[i] * arr[i]) % P == 1):
			current_element = current_element + 1
	return current_element
