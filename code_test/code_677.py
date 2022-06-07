def validity_triangle(a,b,c):
 """
 Write a function to check if the triangle is valid or not.
 """
 total = a + b + c
 if total == 180:
    return True
 else:
    return False
