def min_difference(test_list):
  """
  Write a function to find the minimum difference in the tuple pairs of given tuples.
  """
  temp = [abs(b - a) for a, b in test_list]
  res = min(temp)
  return (res) 
