import re
def fill_spaces(text):
  """
  Write a function to replace all occurrences of spaces, commas, or dots with a colon in the given string by using regex.
  """
  return (re.sub("[ ,.]", ":", text))
