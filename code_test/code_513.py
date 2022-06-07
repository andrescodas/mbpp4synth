def add_str(test_tup, K):
  """
  Write a function to convert tuple into list by adding the given string after every element.
  """
  res = [ele for sub in test_tup for ele in (sub, K)]
  return (res) 
