def max_run_uppercase(test_str):
  """
  Write a function to find maximum run of uppercase characters in the given string.
  """
  cnt = 0
  res = 0
  for idx in range(0, len(test_str)):
    if test_str[idx].isupper():
      cnt += 1
    else:
      res = cnt
      cnt = 0
  if test_str[len(test_str) - 1].isupper():
    res = cnt
  return (res)
