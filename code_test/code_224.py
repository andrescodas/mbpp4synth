def count_Set_Bits(n): 
    """
    Write a python function to count set bits of a given number.
    """
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 
