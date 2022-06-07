def count_Num(n): 
    """
    Write a python function to count numbers whose oth and nth bits are set.
    """
    if (n == 1): 
        return 1
    count = pow(2,n - 2) 
    return count 
