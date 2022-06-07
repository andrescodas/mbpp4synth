import re  
regex = r'^[a-z]$|^([a-z]).*\1$'
def check_char(string): 
	"""
	Write a function to check whether the given string starts and ends with the same character or not using regex.
	"""
	if(re.search(regex, string)): 
		return "Valid" 
	else: 
		return "Invalid" 
