def check_subset(test_tup1, test_tup2):
  """
  Write a function to check if one tuple is a subset of another tuple.
  """
  res = set(test_tup2).issubset(test_tup1)
  return (res) 
