def harmonic_sum(n):
  """
  Write a function to calculate the harmonic sum of n-1.
  """
  if n < 2:
    return 1
  else:
    return 1 / n + (harmonic_sum(n - 1))
