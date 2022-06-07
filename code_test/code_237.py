from collections import Counter 
def check_occurences(test_list):
  """
  Write a function to check the occurrences of records which occur similar times in the given tuples.
  """
  res = dict(Counter(tuple(ele) for ele in map(sorted, test_list)))
  return  (res) 
