def extract_singly(test_list):
  """
  Write a function to extract elements that occur singly in the given tuple list.
  """
  res = []
  temp = set()
  for inner in test_list:
    for ele in inner:
      if not ele in temp:
        temp.add(ele)
        res.append(ele)
  return (res) 
