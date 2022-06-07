import re 
regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
def check_str(string): 
	"""
	Write a function to check whether the given string is starting with a vowel or not using regex.
	"""
	if(re.search(regex, string)): 
		return ("Valid") 
	else: 
		return ("Invalid") 
