def add_K_element(test_list, K):
  """
  Write a function to add the k elements to each element in the tuple.
  """
  res = [tuple(j + K for j in sub ) for sub in test_list]
  return (res) 
