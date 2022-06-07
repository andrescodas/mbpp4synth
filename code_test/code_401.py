def add_nested_tuples(test_tup1, test_tup2):
  """
  Write a function to perform index wise addition of tuple elements in the given two nested tuples.
  """
  res = tuple(tuple(a + b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res) 
