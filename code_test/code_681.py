def smallest_Divisor(n): 
    """
    Write a python function to find the smallest prime divisor of a number.
    """
    if (n % 2 == 0): 
        return 2; 
    i = 3;  
    while (i*i <= n): 
        if (n % i == 0): 
            return i; 
        i += 2; 
    return n; 
