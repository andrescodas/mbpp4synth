import re
text = 'Python Exercises'
def replace_spaces(text):
  """
  Write a function to replace whitespaces with an underscore and vice versa in a given string by using regex.
  """
  text =text.replace (" ", "_")
  return (text)
  text =text.replace ("_", " ")
  return (text)
