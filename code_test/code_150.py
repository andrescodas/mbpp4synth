def does_Contain_B(a,b,c): 
    """
    Write a python function to find whether the given number is present in the infinite sequence or not.
    """
    if (a == b): 
        return True
    if ((b - a) * c > 0 and (b - a) % c == 0): 
        return True
    return False
