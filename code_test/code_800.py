import re
def remove_all_spaces(text):
 """
 Write a function to remove all whitespaces from a string.
 """
 return (re.sub(r'\s+', '',text))
