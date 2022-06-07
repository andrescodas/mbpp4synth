def set_Bit_Number(n): 
    """
    Write a python function to find the most significant bit number which is also a set bit.
    """
    if (n == 0): 
        return 0; 
    msb = 0; 
    n = int(n / 2); 
    while (n > 0): 
        n = int(n / 2); 
        msb += 1; 
    return (1 << msb)
