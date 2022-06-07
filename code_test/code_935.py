def series_sum(number):
 """
 Write a function to calculate the sum of series 1²+2²+3²+….+n².
 """
 total = 0
 total = (number * (number + 1) * (2 * number + 1)) / 6
 return total
