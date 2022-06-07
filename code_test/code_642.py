def remove_similar_row(test_list):
  """
  Write a function to remove similar rows from the given tuple matrix.
  """
  res = set(sorted([tuple(sorted(set(sub))) for sub in test_list]))
  return (res) 
