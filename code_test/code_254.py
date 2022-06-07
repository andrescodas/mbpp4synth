import re
def words_ae(text):
 """
 Write a function to find all words starting with 'a' or 'e' in a given string.
 """
 list = re.findall("[ae]\w+", text)
 return list
