import heapq as hq
def heap_assending(nums):
  """
  Write a function to sort a given list of elements in ascending order using heap queue algorithm.
  """
  hq.heapify(nums)
  s_result = [hq.heappop(nums) for i in range(len(nums))]
  return s_result
