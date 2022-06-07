import re 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check_email(email): 
	"""
	Write a function to check if the string is a valid email address or not using regex.
	"""
	if(re.search(regex,email)): 
		return ("Valid Email") 
	else: 
		return ("Invalid Email") 
