def last(n):
   return n[-1]
def sort_list_last(tuples):
  """
  Write a function to sort a list in increasing order by the last element in each tuple from a given list of non-empty tuples.
  """
  return sorted(tuples, key=last)
