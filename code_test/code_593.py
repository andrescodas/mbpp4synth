import re
def removezero_ip(ip):
 """
 Write a function to remove leading zeroes from an ip address.
 """
 string = re.sub('\.[0]*', '.', ip)
 return string
