import math
def sum_gp(a,n,r):
 """
 Write a function to find the sum of geometric progression series.
 """
 total = (a * (1 - math.pow(r, n ))) / (1- r)
 return total
