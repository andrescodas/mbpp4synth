import math 
def sum_series(number):
 """
 Write a function to calculate the sum of series 1³+2³+3³+….+n³.
 """
 total = 0
 total = math.pow((number * (number + 1)) /2, 2)
 return total
