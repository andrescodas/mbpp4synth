def extract_freq(test_list):
  """
  Write a function to extract the frequency of unique tuples in the given list order irrespective.
  """
  res = len(list(set(tuple(sorted(sub)) for sub in test_list)))
  return (res)
