def geometric_sum(n):
  """
  Write a function to calculate the geometric sum of n-1.
  """
  if n < 0:
    return 0
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 1)
