def check_element(test_tup, check_list):
  """
  Write a function to check if any list element is present in the given list.
  """
  res = False
  for ele in check_list:
    if ele in test_tup:
      res = True
      break
  return (res) 
