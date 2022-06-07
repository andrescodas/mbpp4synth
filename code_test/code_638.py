import math
def wind_chill(v,t):
 """
 Write a function to calculate wind chill index.
 """
 windchill = 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
 return int(round(windchill, 0))
