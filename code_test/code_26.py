def check_k_elements(test_list, K):
  """
  Write a function to check if the given tuple list has all k elements.
  """
  res = True
  for tup in test_list:
    for ele in tup:
      if ele != K:
        res = False
  return (res) 
