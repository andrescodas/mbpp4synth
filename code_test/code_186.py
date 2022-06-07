import re
def check_literals(text, patterns):
  """
  Write a function to search some literals strings in a string by using regex.
  """
  for pattern in patterns:
    if re.search(pattern,  text):
        return ('Matched!')
    else:
        return ('Not Matched!')
