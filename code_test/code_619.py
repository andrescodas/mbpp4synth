def move_num(test_str):
  """
  Write a function to move all the numbers in it to the given string.
  """
  res = ''
  dig = ''
  for ele in test_str:
    if ele.isdigit():
      dig += ele
    else:
      res += ele
  res += dig
  return (res) 
