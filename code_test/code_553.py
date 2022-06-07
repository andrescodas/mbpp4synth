def tuple_to_float(test_tup):
  """
  Write a function to convert the given tuple to a floating-point number.
  """
  res = float('.'.join(str(ele) for ele in test_tup))
  return (res) 
