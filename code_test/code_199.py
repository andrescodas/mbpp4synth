def highest_Power_of_2(n): 
    """
    Write a python function to find highest power of 2 less than or equal to given number.
    """
    res = 0; 
    for i in range(n, 0, -1):  
        if ((i & (i - 1)) == 0): 
            res = i; 
            break;      
    return res; 
