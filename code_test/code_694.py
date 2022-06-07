def extract_unique(test_dict):
  """
  Write a function to extract unique values from the given dictionary values.
  """
  res = list(sorted({ele for val in test_dict.values() for ele in val}))
  return res
