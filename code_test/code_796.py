def return_sum(dict):
  """
  Write function to find the sum of all items in the given dictionary.
  """
  sum = 0
  for i in dict.values():
    sum = sum + i
  return sum
