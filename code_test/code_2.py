def similar_elements(test_tup1, test_tup2):
  """
  Write a function to find the similar elements from the given two tuple lists.
  """
  res = tuple(set(test_tup1) & set(test_tup2))
  return (res) 
