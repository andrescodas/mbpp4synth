def check_valid(test_tup):
  """
  Write a function to check if the given tuple contains all valid values or not.
  """
  res = not any(map(lambda ele: not ele, test_tup))
  return (res) 
