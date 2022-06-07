def same_Length(A,B): 
    """
    Write a python function to check whether the given two numbers have same number of digits or not.
    """
    while (A > 0 and B > 0): 
        A = A / 10; 
        B = B / 10; 
    if (A == 0 and B == 0): 
        return True; 
    return False; 
