import re 
regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
def check_IP(Ip): 
	"""
	Write a function to check whether the given ip address is valid or not using regex.
	"""
	if(re.search(regex, Ip)): 
		return ("Valid IP address") 
	else: 
		return ("Invalid IP address") 
