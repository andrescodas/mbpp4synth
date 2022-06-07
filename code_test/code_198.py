import math
def largest_triangle(a,b): 
    """
    Write a function to find the largest triangle that can be inscribed in an ellipse.
    """
    if (a < 0 or b < 0): 
        return -1 
    area = (3 * math.sqrt(3) * pow(a, 2)) / (4 * b);  
    return area 
