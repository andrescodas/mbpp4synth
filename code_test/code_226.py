def odd_values_string(str):
  """
  Write a python function to remove the characters which have odd index values of a given string.
  """
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
