def first_repeated_char(str1):
  """
  Write a python function to find the first repeated character in a given string.
  """
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > 1:
      return c 
  return "None"
