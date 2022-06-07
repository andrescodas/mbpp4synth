from collections import Counter 
def anagram_lambda(texts,str):
  """
  Write a function to find all anagrams of a string in a given list of strings using lambda function.
  """
  result = list(filter(lambda x: (Counter(str) == Counter(x)), texts)) 
  return result
