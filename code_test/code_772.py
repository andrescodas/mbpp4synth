def remove_length(test_str, K):
  """
  Write a function to remove all the words with k length in the given string.
  """
  temp = test_str.split()
  res = [ele for ele in temp if len(ele) != K]
  res = ' '.join(res)
  return (res) 
