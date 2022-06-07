def neg_count(list):
  """
  Write a python function to count negative numbers in a list.
  """
  neg_count= 0
  for num in list: 
    if num <= 0: 
      neg_count += 1
  return neg_count 
