
def extract_min_max(test_tup, K):
  """
  Write a function to extract maximum and minimum k elements in the given tuple.
  """
  res = []
  test_tup = list(test_tup)
  temp = sorted(test_tup)
  for idx, val in enumerate(temp):
    if idx < K or idx >= len(temp) - K:
      res.append(val)
  res = tuple(res)
  return (res) 
