def extract_missing(test_list, strt_val, stop_val):
  """
  Write a function to extract the ranges that are missing from the given list with the given start range and end range values.
  """
  res = []
  for sub in test_list:
    if sub[0] > strt_val:
      res.append((strt_val, sub[0]))
      strt_val = sub[1]
    if strt_val < stop_val:
      res.append((strt_val, stop_val))
  return (res) 
