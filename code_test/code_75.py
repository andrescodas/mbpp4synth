def find_tuples(test_list, K):
  """
  Write a function to find tuples which have all elements divisible by k from the given list of tuples.
  """
  res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]
  return (str(res)) 
