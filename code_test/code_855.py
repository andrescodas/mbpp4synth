def check_Even_Parity(x): 
    """
    Write a python function to check for even parity of a given number.
    """
    parity = 0
    while (x != 0): 
        x = x & (x - 1) 
        parity += 1
    if (parity % 2 == 0): 
        return True
    else: 
        return False
