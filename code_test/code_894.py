def float_to_tuple(test_str):
  """
  Write a function to convert the given string of float type into tuple.
  """
  res = tuple(map(float, test_str.split(', ')))
  return (res) 
