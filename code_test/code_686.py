from collections import defaultdict 
def freq_element(test_tup):
  """
  Write a function to find the frequency of each element in the given list.
  """
  res = defaultdict(int)
  for ele in test_tup:
    res[ele] += 1
  return (str(dict(res))) 
