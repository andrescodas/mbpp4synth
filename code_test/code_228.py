def all_Bits_Set_In_The_Given_Range(n,l,r):  
    """
    Write a python function to check whether all the bits are unset in the given range or not.
    """
    num = (((1 << r) - 1) ^ ((1 << (l - 1)) - 1)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False
