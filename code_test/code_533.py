def remove_datatype(test_tuple, data_type):
  """
  Write a function to remove particular data type elements from the given tuple.
  """
  res = []
  for ele in test_tuple:
    if not isinstance(ele, data_type):
      res.append(ele)
  return (res) 
