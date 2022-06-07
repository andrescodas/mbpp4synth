import heapq
def cheap_items(items,n):
  """
  Write a function to find the n - cheap price items from a given dataset using heap queue algorithm.
  """
  cheap_items = heapq.nsmallest(n, items, key=lambda s: s['price'])
  return cheap_items
