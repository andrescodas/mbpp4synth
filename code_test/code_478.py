import re
def remove_lowercase(str1):
 """
 Write a function to remove lowercase substrings from a given string.
 """
 remove_lower = lambda text: re.sub('[a-z]', '', text)
 result =  remove_lower(str1)
 return result
