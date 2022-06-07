import heapq as hq
def raw_heap(rawheap):
  """
  Write a function which accepts an arbitrary list and converts it to a heap using heap queue algorithm.
  """
  hq.heapify(rawheap)
  return rawheap
