from itertools import groupby 
def group_element(test_list):
  """
  Write a function to group the 1st elements on the basis of 2nd elements in the given tuple list.
  """
  res = dict()
  for key, val in groupby(sorted(test_list, key = lambda ele: ele[1]), key = lambda ele: ele[1]):
    res[key] = [ele[0] for ele in val] 
  return (res)
