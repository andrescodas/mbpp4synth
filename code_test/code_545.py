def take_L_and_F_set_bits(n) : 
    n = n | n >> 1
    n = n | n >> 2
    n = n | n >> 4
    n = n | n >> 8
    n = n | n >> 16 
    return ((n + 1) >> 1) + 1      
def toggle_F_and_L_bits(n) :  
    """
    Write a python function to toggle only first and last bits of a given number.
    """
    if (n == 1) : 
        return 0 
    return n ^ take_L_and_F_set_bits(n) 
