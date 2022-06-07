import heapq as hq
def heap_replace(heap,a):
  """
  Write a function to delete the smallest element from the given heap and then insert a new item.
  """
  hq.heapify(heap)
  hq.heapreplace(heap, a)
  return heap
