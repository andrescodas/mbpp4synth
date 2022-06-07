def substract_elements(test_tup1, test_tup2):
  """
  Write a function to substract the contents of one tuple with corresponding index of other tuple.
  """
  res = tuple(map(lambda i, j: i - j, test_tup1, test_tup2))
  return (res) 
