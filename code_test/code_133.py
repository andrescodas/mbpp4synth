def sum_negativenum(nums):
  """
  Write a function to calculate the sum of the negative numbers of a given list of numbers using lambda function.
  """
  sum_negativenum = list(filter(lambda nums:nums<0,nums))
  return sum(sum_negativenum)
