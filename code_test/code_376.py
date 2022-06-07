def remove_replica(test_tup):
  """
  Write a function to remove tuple elements that occur more than once and replace the duplicates with some custom value.
  """
  temp = set()
  res = tuple(ele if ele not in temp and not temp.add(ele) 
				else 'MSP' for ele in test_tup)
  return (res)
