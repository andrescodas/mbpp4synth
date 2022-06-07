def first_odd(nums):
  """
  Write a python function to find the first odd number in a given list of numbers.
  """
  first_odd = next((el for el in nums if el%2!=0),-1)
  return first_odd
