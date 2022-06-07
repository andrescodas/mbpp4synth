def tuple_str_int(test_str):
  """
  Write a function to convert tuple string to integer tuple.
  """
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(', '))
  return (res) 
