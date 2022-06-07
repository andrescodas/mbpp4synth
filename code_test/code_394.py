def check_distinct(test_tup):
  """
  Write a function to check if given tuple is distinct or not.
  """
  res = True
  temp = set()
  for ele in test_tup:
    if ele in temp:
      res = False
      break
    temp.add(ele)
  return (res) 
