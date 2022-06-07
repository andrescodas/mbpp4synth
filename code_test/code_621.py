def increment_numerics(test_list, K):
  """
  Write a function to increment the numeric values in the given strings by k.
  """
  res = [str(int(ele) + K) if ele.isdigit() else ele for ele in test_list]
  return res 
