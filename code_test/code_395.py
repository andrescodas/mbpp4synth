def first_non_repeating_character(str1):
  """
  Write a python function to find the first non-repeated character in a given string.
  """
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None
