def sum_list(lst1,lst2):
  """
  Write a function to sum elements in two lists.
  """
  res_list = [lst1[i] + lst2[i] for i in range(len(lst1))] 
  return res_list
