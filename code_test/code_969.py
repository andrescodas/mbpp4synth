def join_tuples(test_list):
  """
  Write a function to join the tuples if they have similar initial elements.
  """
  res = []
  for sub in test_list:
    if res and res[-1][0] == sub[0]:
      res[-1].extend(sub[1:])
    else:
      res.append([ele for ele in sub])
  res = list(map(tuple, res))
  return (res) 
