import collections
def freq_count(list1):
  """
  Write a function to get the frequency of the elements in a list.
  """
  freq_count= collections.Counter(list1)
  return freq_count
