from math import radians, sin, cos, acos
def distance_lat_long(slat,slon,elat,elon):
 """
 Write a function to calculate distance between two points using latitude and longitude.
 """
 dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
 return dist
