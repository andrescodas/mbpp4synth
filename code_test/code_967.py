def check(string): 
  """
  Write a python function to accept the strings which contains all vowels.
  """
  if len(set(string).intersection("AEIOUaeiou"))>=5: 
    return ('accepted') 
  else: 
    return ("not accepted") 
