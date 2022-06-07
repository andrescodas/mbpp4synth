def min_k(test_list, K):
  """
  Write a function to find minimum k records from tuple list.
  """
  res = sorted(test_list, key = lambda x: x[1])[:K]
  return (res) 
