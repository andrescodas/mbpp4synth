import re
def remove_multiple_spaces(text1):
  """
  Write a function to remove multiple spaces in a string by using regex.
  """
  return (re.sub(' +',' ',text1))
