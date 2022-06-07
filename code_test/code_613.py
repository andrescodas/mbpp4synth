def maximum_value(test_list):
  """
  Write a function to find the maximum value in record list as tuple attribute in the given tuple list.
  """
  res = [(key, max(lst)) for key, lst in test_list]
  return (res) 
