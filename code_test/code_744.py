def check_none(test_tup):
  """
  Write a function to check if the given tuple has any none value or not.
  """
  res = any(map(lambda ele: ele is None, test_tup))
  return (res) 
