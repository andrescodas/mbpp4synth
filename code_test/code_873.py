def fibonacci(n):
  """
  Write a function to solve the fibonacci sequence using recursion.
  """
  if n == 1 or n == 2:
    return 1
  else:
    return (fibonacci(n - 1) + (fibonacci(n - 2)))
