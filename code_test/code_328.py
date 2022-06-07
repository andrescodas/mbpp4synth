def rotate_left(list1,m,n):
  """
  Write a function to rotate a given list by specified number of items to the left direction.
  """
  result =  list1[m:]+list1[:n]
  return result
