def flatten_tuple(test_list):
  """
  Write a function to flatten the tuple list to a string.
  """
  res = ' '.join([idx for tup in test_list for idx in tup])
  return (res) 
