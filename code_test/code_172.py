def count_occurance(s):
  """
  Write a function to find the occurence of characters 'std' in the given string 1. list item 1. list item 1. list item 2. list item 2. list item 2. list item
  """
  count=0
  for i in range(len(s)):
    if (s[i]== 's' and s[i+1]=='t' and s[i+2]== 'd'):
      count = count + 1
  return count
