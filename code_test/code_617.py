def min_Jumps(a, b, d): 
    """
    Write a function to check for the number of jumps required of given length to reach a point of form (d, 0) from origin in a 2d plane.
    """
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
