def count_reverse_pairs(test_list):
  """
  Write a function to count the pairs of reverse strings in the given string list.
  """
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return str(res)
