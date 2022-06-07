def str_to_tuple(test_str):
  """
  Write a function to convert the given string of integers into a tuple.
  """
  res = tuple(map(int, test_str.split(', ')))
  return (res) 
