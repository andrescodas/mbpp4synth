def binary_to_integer(test_tup):
  """
  Write a function to convert the given binary tuple to integer.
  """
  res = int("".join(str(ele) for ele in test_tup), 2)
  return (str(res)) 
