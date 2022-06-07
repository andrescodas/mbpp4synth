import re
def is_decimal(num):
  """
  Write a function to check the given decimal with a precision of 2 by using regex.
  """
  num_fetch = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
  result = num_fetch.search(num)
  return bool(result)
