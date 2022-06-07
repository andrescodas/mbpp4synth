from copy import deepcopy
def colon_tuplex(tuplex,m,n):
  """
  Write a function to get a colon of a tuple.
  """
  tuplex_colon = deepcopy(tuplex)
  tuplex_colon[m].append(n)
  return tuplex_colon
