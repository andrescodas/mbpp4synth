def sum_digits(n):
  """
  Write a function to get the sum of a non-negative integer.
  """
  if n == 0:
    return 0
  else:
    return n % 10 + sum_digits(int(n / 10))
