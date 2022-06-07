def check_greater(test_tup1, test_tup2):
  """
  Write a function to check if each element of the second tuple is greater than its corresponding index in the first tuple.
  """
  res = all(x < y for x, y in zip(test_tup1, test_tup2))
  return (res) 
