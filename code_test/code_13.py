from collections import Counter
def count_common(words):
  """
  Write a function to count the most common words in a dictionary.
  """
  word_counts = Counter(words)
  top_four = word_counts.most_common(4)
  return (top_four)
