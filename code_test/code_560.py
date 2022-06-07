def union_elements(test_tup1, test_tup2):
  """
  Write a function to find the union of elements of the given tuples.
  """
  res = tuple(set(test_tup1 + test_tup2))
  return (res) 
