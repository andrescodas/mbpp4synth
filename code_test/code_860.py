import re 
regex = '[a-zA-z0-9]$'
def check_alphanumeric(string): 
	"""
	Write a function to check whether the given string is ending with only alphanumeric characters or not using regex.
	"""
	if(re.search(regex, string)): 
		return ("Accept") 
	else: 
		return ("Discard") 
