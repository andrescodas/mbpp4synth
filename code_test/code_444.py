def trim_tuple(test_list, K):
  """
  Write a function to trim each tuple by k in the given tuple list.
  """
  res = []
  for ele in test_list:
    N = len(ele)
    res.append(tuple(list(ele)[K: N - K]))
  return (str(res)) 
