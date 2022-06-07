import cmath
def polar_rect(x,y):
 """
 Write a function to convert polar coordinates to rectangular coordinates.
 """
 cn = complex(x,y)
 cn=cmath.polar(cn)
 cn1 = cmath.rect(2, cmath.pi)
 return (cn,cn1)
