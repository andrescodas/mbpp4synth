import cmath
def angle_complex(a,b):
  """
  Write a function to get the angle of a complex number.
  """
  cn=complex(a,b)
  angle=cmath.phase(a+b)
  return angle
