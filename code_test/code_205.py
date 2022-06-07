def inversion_elements(test_tup):
  """
  Write a function to find the inversions of tuple elements in the given tuple list.
  """
  res = tuple(list(map(lambda x: ~x, list(test_tup))))
  return (res) 
