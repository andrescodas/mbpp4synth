def max_similar_indices(test_list1, test_list2):
  """
  Write a function to find the maximum of similar indices in two lists of tuples.
  """
  res = [(max(x[0], y[0]), max(x[1], y[1]))
   for x, y in zip(test_list1, test_list2)]
  return (res) 
