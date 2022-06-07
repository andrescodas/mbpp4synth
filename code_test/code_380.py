def multi_list(rownum,colnum):
  """
  Write a function to generate a two-dimensional array.
  """
  multi_list = [[0 for col in range(colnum)] for row in range(rownum)]
  for row in range(rownum):
    for col in range(colnum):
        multi_list[row][col]= row*col
  return multi_list
