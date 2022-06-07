def rearrange_numbs(array_nums):
  """
  Write a function to rearrange positive and negative numbers in a given array using lambda function.
  """
  result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
  return result 
