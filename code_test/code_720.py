def add_dict_to_tuple(test_tup, test_dict):
  """
  Write a function to add a dictionary to the tuple.
  """
  test_tup = list(test_tup)
  test_tup.append(test_dict)
  test_tup = tuple(test_tup)
  return (test_tup) 
