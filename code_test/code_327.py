def check_isosceles(x,y,z):
  """
  Write a function to print check if the triangle is isosceles or not.
  """
  if x==y or y==z or z==x:
	   return True
  else:
     return False
