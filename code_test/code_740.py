def tuple_to_dict(test_tup):
  """
  Write a function to convert the given tuple to a key-value dictionary using adjacent elements.
  """
  res = dict(test_tup[idx : idx + 2] for idx in range(0, len(test_tup), 2))
  return (res) 
