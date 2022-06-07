import heapq
def merge_sorted_list(num1,num2,num3):
  """
  Write a function to merge multiple sorted inputs into a single sorted iterator using heap queue algorithm.
  """
  num1=sorted(num1)
  num2=sorted(num2)
  num3=sorted(num3)
  result = heapq.merge(num1,num2,num3)
  return list(result)
