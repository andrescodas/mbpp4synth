from heapq import merge
def combine_lists(num1,num2):
  """
  Write a function to combine two given sorted lists using heapq module.
  """
  combine_lists=list(merge(num1, num2))
  return combine_lists
