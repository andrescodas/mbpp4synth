def matrix_to_list(test_list):
  """
  Write a function to flatten the given tuple matrix into the tuple list with each tuple representing each column.
  """
  temp = [ele for sub in test_list for ele in sub]
  res = list(zip(*temp))
  return (str(res))
