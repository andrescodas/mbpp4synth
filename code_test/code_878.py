def check_tuples(test_tuple, K):
  """
  Write a function to check if the given tuple contains only k elements.
  """
  res = all(ele in K for ele in test_tuple)
  return (res) 
