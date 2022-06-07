def find_equal_tuple(Input, k):
  flag = 1
  for tuple in Input:
    if len(tuple) != k:
      flag = 0
      break
  return flag
def get_equal(Input, k):
  """
  Write a function to find whether all the given tuples have equal length or not.
  """
  if find_equal_tuple(Input, k) == 1:
    return ("All tuples have same length")
  else:
    return ("All tuples do not have same length")
