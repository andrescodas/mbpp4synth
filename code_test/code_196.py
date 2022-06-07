def remove_tuples(test_list, K):
  """
  Write a function to remove all the tuples with length k.
  """
  res = [ele for ele in test_list if len(ele) != K]
  return (res) 
