def sum_series(n):
  """
  Write a function to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
  """
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)
