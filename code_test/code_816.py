def clear_tuple(test_tup):
  """
  Write a function to clear the values of the given tuples.
  """
  temp = list(test_tup)
  temp.clear()
  test_tup = tuple(temp)
  return (test_tup) 
