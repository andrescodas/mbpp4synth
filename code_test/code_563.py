import re
def extract_values(text):
 """
 Write a function to extract values between quotation marks of a string.
 """
 return (re.findall(r'"(.*?)"', text))
