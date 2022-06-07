from operator import itemgetter 
def index_minimum(test_list):
  """
  Write a function to extract the index minimum value record from the given tuples.
  """
  res = min(test_list, key = itemgetter(1))[0]
  return (res) 
