def palindrome_lambda(texts):
  """
  Write a function to find palindromes in a given list of strings using lambda function.
  """
  result = list(filter(lambda x: (x == "".join(reversed(x))), texts))
  return result
