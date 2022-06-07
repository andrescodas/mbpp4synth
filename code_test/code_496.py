import heapq as hq
def heap_queue_smallest(nums,n):
  """
  Write a function to find the smallest integers from a given list of numbers using heap queue algorithm.
  """
  smallest_nums = hq.nsmallest(n, nums)
  return smallest_nums
