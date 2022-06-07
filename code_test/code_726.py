def multiply_elements(test_tup):
  """
  Write a function to multiply the adjacent elements of the given tuple.
  """
  res = tuple(i * j for i, j in zip(test_tup, test_tup[1:]))
  return (res) 
