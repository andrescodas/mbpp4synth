import re
def remove_spaces(text):
 """
 Write a function to remove multiple spaces in a string.
 """
 return (re.sub(' +',' ',text))
