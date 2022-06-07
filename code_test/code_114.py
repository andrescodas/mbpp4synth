from collections import Counter 
def assign_freq(test_list):
  """
  Write a function to assign frequency to each tuple in the given tuple list.
  """
  res = [(*key, val) for key, val in Counter(test_list).items()]
  return (str(res)) 
