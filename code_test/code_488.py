import math
def area_pentagon(a):
  """
  Write a function to find the area of a pentagon.
  """
  area=(math.sqrt(5*(5+2*math.sqrt(5)))*pow(a,2))/4.0
  return area
