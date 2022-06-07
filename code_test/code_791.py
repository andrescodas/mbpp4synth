def remove_nested(test_tup):
  """
  Write a function to remove the nested record from the given tuple.
  """
  res = tuple()
  for count, ele in enumerate(test_tup):
    if not isinstance(ele, tuple):
      res = res + (ele, )
  return (res) 
