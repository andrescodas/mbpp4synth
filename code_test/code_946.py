from collections import Counter 
def most_common_elem(s,a):
  """
  Write a function to find the most common elements and their counts of a specified text.
  """
  most_common_elem=Counter(s).most_common(a)
  return most_common_elem
