def first_repeated_word(str1):
  """
  Write a python function to find the first repeated word in a given string.
  """
  temp = set()
  for word in str1.split():
    if word in temp:
      return word;
    else:
      temp.add(word)
  return 'None'
