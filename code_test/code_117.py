def list_to_float(test_list):
  """
  Write a function to convert all possible convertible elements in the list to float.
  """
  res = []
  for tup in test_list:
    temp = []
    for ele in tup:
      if ele.isalpha():
        temp.append(ele)
      else:
        temp.append(float(ele))
    res.append((temp[0],temp[1])) 
  return (str(res)) 
