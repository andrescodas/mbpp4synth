def rotate_right(list1,m,n):
  """
  Write a function to rotate a given list by specified number of items to the right direction.
  """
  result =  list1[-(m):]+list1[:-(n)]
  return result
