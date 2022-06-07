def set_left_most_unset_bit(n): 
    """
    Write a python function to set the left most unset bit.
    """
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 << (pos))) 
