import re
def search_literal(pattern,text):
 """
 Write a function to search a literals string in a string and also find the location within the original string where the pattern occurs.
 """
 match = re.search(pattern, text)
 s = match.start()
 e = match.end()
 return (s, e)
