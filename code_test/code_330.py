import re
def find_char(text):
  """
  Write a function to find all three, four, five characters long words in the given string by using regex.
  """
  return (re.findall(r"\b\w{3,5}\b", text))
