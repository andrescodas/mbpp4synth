from collections import Counter
import re
def n_common_words(text,n):
  """
  Write a function to find the occurrences of n most common words in a given text.
  """
  words = re.findall('\w+',text)
  n_common_words= Counter(words).most_common(n)
  return list(n_common_words)
