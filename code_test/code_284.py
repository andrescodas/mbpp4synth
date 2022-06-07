def check_element(list,element):
  """
  Write a function to check whether all items of a list are equal to a given string.
  """
  check_element=all(v== element for v in list)
  return check_element
