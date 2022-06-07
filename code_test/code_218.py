import math   
def min_Operations(A,B):  
    """
    Write a python function to find the minimum operations required to make two numbers equal.
    """
    if (A > B): 
        swap(A,B)  
    B = B // math.gcd(A,B);  
    return B - 1
