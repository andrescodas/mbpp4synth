import re 
def extract_max(input): 
	"""
	Write a function to extract the maximum numeric value from a string by using regex.
	"""
	numbers = re.findall('\d+',input) 
	numbers = map(int,numbers) 
	return max(numbers)
