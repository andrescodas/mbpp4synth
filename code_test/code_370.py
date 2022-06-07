def float_sort(price):
  """
  Write a function to sort a tuple by its float element.
  """
  float_sort=sorted(price, key=lambda x: float(x[1]), reverse=True)
  return float_sort
