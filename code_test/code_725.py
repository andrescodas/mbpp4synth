import re
def extract_quotation(text1):
  """
  Write a function to extract values between quotation marks of the given string by using regex.
  """
  return (re.findall(r'"(.*?)"', text1))
