import re
def split_lowerstring(text):
 """
 Write a function to split a string at lowercase letters.
 """
 return (re.findall('[a-z][^a-z]*', text))
