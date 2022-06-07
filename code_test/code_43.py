import re
def text_match(text):
  """
  Write a function to find sequences of lowercase letters joined with an underscore using regex.
  """
  patterns = '^[a-z]+_[a-z]+$'
  if re.search(patterns,  text):
    return ('Found a match!')
  else:
    return ('Not matched!')
