def check_type(test_tuple):
  """
  Write a function to check if all the elements in tuple have same data type or not.
  """
  res = True
  for ele in test_tuple:
    if not isinstance(ele, type(test_tuple[0])):
      res = False
      break
  return (res) 
