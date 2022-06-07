def sorted_dict(dict1):
  """
  Write a function to sort a list in a dictionary.
  """
  sorted_dict = {x: sorted(y) for x, y in dict1.items()}
  return sorted_dict
