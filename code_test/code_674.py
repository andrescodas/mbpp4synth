from collections import OrderedDict
def remove_duplicate(string):
  """
  Write a function to remove duplicate words from a given string using collections module.
  """
  result = ' '.join(OrderedDict((w,w) for w in string.split()).keys())
  return result
