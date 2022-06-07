def find_Nth_Digit(p,q,N) :  
    """
    Write a python function to find the nth digit in the proper fraction of two given numbers.
    """
    while (N > 0) : 
        N -= 1;  
        p *= 10;  
        res = p // q;  
        p %= q;  
    return res;  
