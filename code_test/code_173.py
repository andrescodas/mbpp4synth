import re
def remove_splchar(text): 
 """
 Write a function to remove everything except alphanumeric characters from a string.
 """
 pattern = re.compile('[\W_]+')
 return (pattern.sub('', text))
