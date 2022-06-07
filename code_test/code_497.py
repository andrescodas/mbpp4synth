import math
def surfacearea_cone(r,h):
  """
  Write a function to find the surface area of a cone.
  """
  l = math.sqrt(r * r + h * h)
  SA = math.pi * r * (r + l)
  return SA
