import heapq
def small_nnum(list1,n):
  """
  Write a function to get the n smallest items from a dataset.
  """
  smallest=heapq.nsmallest(n,list1)
  return smallest
