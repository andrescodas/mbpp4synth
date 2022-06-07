import re
def split_upperstring(text):
 """
 Write a function to split a string at uppercase letters.
 """
 return (re.findall('[A-Z][^A-Z]*', text))
