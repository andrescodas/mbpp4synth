import re
def replace_max_specialchar(text,n):
 """
 Write a function to replace maximum n occurrences of spaces, commas, or dots with a colon.
 """
 return (re.sub("[ ,.]", ":", text, n))
