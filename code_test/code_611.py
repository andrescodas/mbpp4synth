def max_of_nth(test_list, N):
  """
  Write a function to find the maximum of nth column from the given tuple list.
  """
  res = max([sub[N] for sub in test_list])
  return (res) 
