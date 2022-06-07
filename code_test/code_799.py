INT_BITS = 32
def left_Rotate(n,d):   
    """
    Write a python function to left rotate the bits of a given number.
    """
    return (n << d)|(n >> (INT_BITS - d))  
