def re_arrange_tuples(test_list, ord_list):
  """
  Write a function to re-arrange the given tuples based on the given ordered list.
  """
  temp = dict(test_list)
  res = [(key, temp[key]) for key in ord_list]
  return (res) 
