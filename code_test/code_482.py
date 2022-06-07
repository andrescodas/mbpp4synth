import re 
def match(text): 
		"""
		Write a function to find sequences of one upper case letter followed by lower case letters in the given string by using regex.
		"""
		pattern = '[A-Z]+[a-z]+$'
		if re.search(pattern, text): 
				return('Yes') 
		else: 
				return('No') 
