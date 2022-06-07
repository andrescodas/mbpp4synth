def sum_of_alternates(test_tuple):
  """
  Write a function to extract the sum of alternate chains of tuples.
  """
  sum1 = 0
  sum2 = 0
  for idx, ele in enumerate(test_tuple):
    if idx % 2:
      sum1 += ele
    else:
      sum2 += ele
  return ((sum1),(sum2)) 
