import re
def remove_uppercase(str1):
  """
  Write a function to remove uppercase substrings from a given string by using regex.
  """
  remove_upper = lambda text: re.sub('[A-Z]', '', text)
  result =  remove_upper(str1)
  return (result)
