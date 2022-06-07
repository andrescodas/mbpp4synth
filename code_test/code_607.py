import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
def find_literals(text, pattern):
  """
  Write a function to search a literals string in a string and also find the location within the original string where the pattern occurs by using regex.
  """
  match = re.search(pattern, text)
  s = match.start()
  e = match.end()
  return (match.re.pattern, s, e)
