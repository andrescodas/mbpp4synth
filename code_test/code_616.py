def tuple_modulo(test_tup1, test_tup2):
  """
  Write a function to perfom the modulo of tuple elements in the given two tuples.
  """
  res = tuple(ele1 % ele2 for ele1, ele2 in zip(test_tup1, test_tup2)) 
  return (res) 
