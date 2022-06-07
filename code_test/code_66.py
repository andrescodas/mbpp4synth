def pos_count(list):
  """
  Write a python function to count positive numbers in a list.
  """
  pos_count= 0
  for num in list: 
    if num >= 0: 
      pos_count += 1
  return pos_count 
