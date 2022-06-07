def count_first_elements(test_tup):
  """
  Write a function to find the element count that occurs before the record in the given tuple.
  """
  for count, ele in enumerate(test_tup):
    if isinstance(ele, tuple):
      break
  return (count) 
