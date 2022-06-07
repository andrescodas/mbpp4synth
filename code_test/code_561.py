def assign_elements(test_list):
  """
  Write a function to assign with each element, its pair elements from other similar pairs in the given tuple.
  """
  res = dict()
  for key, val in test_list:
    res.setdefault(val, [])
    res.setdefault(key, []).append(val)
  return (res) 
