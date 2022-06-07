import math
def lateralsurface_cone(r,h):
  """
  Write a function to find the lateral surface area of a cone.
  """
  l = math.sqrt(r * r + h * h)
  LSA = math.pi * r  * l
  return LSA
