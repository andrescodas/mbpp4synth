import re
def remove_extra_char(text1):
  """
  Write a function to remove everything except alphanumeric characters from the given string by using regex.
  """
  pattern = re.compile('[\W_]+')
  return (pattern.sub('', text1))
