from math import tan, pi
def area_polygon(s,l):
  """
  Write a function to calculate the area of a regular polygon.
  """
  area = s * (l ** 2) / (4 * tan(pi / s))
  return area
