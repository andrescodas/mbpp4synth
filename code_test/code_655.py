def fifth_Power_Sum(n) : 
    """
    Write a python function to find the sum of fifth power of n natural numbers.
    """
    sm = 0 
    for i in range(1,n+1) : 
        sm = sm + (i*i*i*i*i) 
    return sm 
