import re
def occurance_substring(text,pattern):
 """
 Write a function to find the occurrence and position of the substrings within a string.
 """
 for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    return (text[s:e], s, e)
