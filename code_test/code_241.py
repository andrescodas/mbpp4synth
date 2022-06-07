def array_3d(m,n,o):
 """
 Write a function to generate a 3d array having each element as '*'.
 """
 array_3d = [[ ['*' for col in range(m)] for col in range(n)] for row in range(o)]
 return array_3d
