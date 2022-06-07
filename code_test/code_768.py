def check_Odd_Parity(x): 
    """
    Write a python function to check for odd parity of a given number.
    """
    parity = 0
    while (x != 0): 
        x = x & (x - 1) 
        parity += 1
    if (parity % 2 == 1): 
        return True
    else: 
        return False
