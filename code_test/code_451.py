import re
def remove_whitespaces(text1):
  """
  Write a function to remove all whitespaces from the given string using regex.
  """
  return (re.sub(r'\s+', '',text1))
