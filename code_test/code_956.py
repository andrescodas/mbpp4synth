import re
def split_list(text):
  """
  Write a function to split the given string at uppercase letters by using regex.
  """
  return (re.findall('[A-Z][^A-Z]*', text))
