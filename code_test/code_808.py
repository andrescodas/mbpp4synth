def check_K(test_tup, K):
  """
  Write a function to check if the given tuples contain the k or not.
  """
  res = False
  for ele in test_tup:
    if ele == K:
      res = True
      break
  return (res) 
