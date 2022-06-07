import re
def capital_words_spaces(str1):
  """
  Write a function to put spaces between words starting with capital letters in a given string by using regex.
  """
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)
