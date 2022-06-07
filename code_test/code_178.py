import re
def string_literals(patterns,text):
  """
  Write a function to search some literals strings in a string.
  """
  for pattern in patterns:
     if re.search(pattern,  text):
       return ('Matched!')
     else:
       return ('Not Matched!')
