from itertools import combinations
def sub_lists(my_list):
	"""
	Write a function to generate all sublists of a given list.
	"""
	subs = []
	for i in range(0, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs
