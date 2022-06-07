def sum_positivenum(nums):
  """
  Write a function to calculate the sum of the positive numbers of a given list of numbers using lambda function.
  """
  sum_positivenum = list(filter(lambda nums:nums>0,nums))
  return sum(sum_positivenum)
