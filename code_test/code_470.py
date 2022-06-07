def add_pairwise(test_tup):
  """
  Write a function to find the pairwise addition of the elements of the given tuples.
  """
  res = tuple(i + j for i, j in zip(test_tup, test_tup[1:]))
  return (res) 
