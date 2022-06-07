import heapq as hq
def heap_queue_largest(nums,n):
  """
  Write a function to find the largest integers from a given list of numbers using heap queue algorithm.
  """
  largest_nums = hq.nlargest(n, nums)
  return largest_nums
