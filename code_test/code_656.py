def find_Min_Sum(a,b,n): 
    """
    Write a python function to find the minimum sum of absolute differences of two arrays.
    """
    a.sort() 
    b.sort() 
    sum = 0  
    for i in range(n): 
        sum = sum + abs(a[i] - b[i]) 
    return sum
