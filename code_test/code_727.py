import re 
def remove_char(S):
  """
  Write a function to remove all characters except letters and numbers using regex
  """
  result = re.sub('[\W_]+', '', S) 
  return result
