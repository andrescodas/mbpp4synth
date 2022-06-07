def concatenate_elements(test_tup):
  """
  Write a function to perform the adjacent element concatenation in the given tuples.
  """
  res = tuple(i + j for i, j in zip(test_tup, test_tup[1:]))
  return (res) 
