import re
def multiple_split(text):
  """
  Write a function to split the given string with multiple delimiters by using regex.
  """
  return (re.split('; |, |\*|\n',text))
