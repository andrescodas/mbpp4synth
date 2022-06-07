import heapq
def expensive_items(items,n):
  """
  Write a function to find the n - expensive price items from a given dataset using heap queue algorithm.
  """
  expensive_items = heapq.nlargest(n, items, key=lambda s: s['price'])
  return expensive_items
