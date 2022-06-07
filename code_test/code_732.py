import re
def replace_specialchar(text):
 """
 Write a function to replace all occurrences of spaces, commas, or dots with a colon.
 """
 return (re.sub("[ ,.]", ":", text))
