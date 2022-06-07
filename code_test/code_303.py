import sys 
def solve(a,n):   
    """
    Write a python function to check whether the count of inversion of two types are same or not.
    """
    mx = -sys.maxsize - 1
    for j in range(1,n):  
        if (mx > a[j]):  
            return False  
        mx = max(mx,a[j - 1])    
    return True
