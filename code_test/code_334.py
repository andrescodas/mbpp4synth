def check_Validity(a,b,c):  
    """
    Write a python function to check whether the triangle is valid or not if sides are given.
    """
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True        
