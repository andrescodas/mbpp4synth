def find_max(test_list):
  """
  Write a function to find the maximum element of all the given tuple records.
  """
  res = max(int(j) for i in test_list for j in i)
  return (res) 
