def test_three_equal(x,y,z):
  """
  Write a python function to count the number of equal numbers from three given integers.
  """
  result= set([x,y,z])
  if len(result)==3:
    return 0
  else:
    return (4-len(result))
