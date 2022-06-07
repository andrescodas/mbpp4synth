def extract_symmetric(test_list):
  """
  Write a function to extract all the pairs which are symmetric in the given tuple list.
  """
  temp = set(test_list) & {(b, a) for a, b in test_list}
  res = {(a, b) for a, b in temp if a < b}
  return (res) 
