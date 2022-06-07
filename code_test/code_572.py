def two_unique_nums(nums):
  """
  Write a python function to remove two duplicate numbers from a given number of lists.
  """
  return [i for i in nums if nums.count(i)==1]
