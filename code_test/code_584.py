import re
def find_adverbs(text):
  """
  Write a function to find all adverbs and their positions in a given sentence by using regex.
  """
  for m in re.finditer(r"\w+ly", text):
    return ('%d-%d: %s' % (m.start(), m.end(), m.group(0)))
