from collections import Counter 
	
def second_frequent(input): 
	"""
	Write a function to find out the second most repeated (or frequent) string in the given sequence.
	"""
	dict = Counter(input) 
	value = sorted(dict.values(), reverse=True)  
	second_large = value[1] 
	for (key, val) in dict.items(): 
		if val == second_large: 
			return (key) 
