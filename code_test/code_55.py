import math
def tn_gp(a,n,r):
  """
  Write a function to find t-nth term of geometric series.
  """
  tn = a * (math.pow(r, n - 1))
  return tn
