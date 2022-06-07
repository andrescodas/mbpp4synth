def remove_tuple(test_list):
  """
  Write a function to remove all tuples with all none values in the given tuple list.
  """
  res = [sub for sub in test_list if not all(ele == None for ele in sub)]
  return (str(res)) 
