import re 
def check_substring(string, sample) : 
  """
  Write a function to check if the given string starts with a substring using regex.
  """
  if (sample in string): 
      y = "\A" + sample 
      x = re.search(y, string) 
      if x : 
          return ("string starts with the given substring") 
      else : 
          return ("string doesnt start with the given substring") 
  else : 
      return ("entered string isnt a substring")
