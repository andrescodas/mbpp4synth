def test_distinct(data):
  """
  Write a python function to determine whether all the numbers are different from each other are not.
  """
  if len(data) == len(set(data)):
    return True
  else:
    return False;
