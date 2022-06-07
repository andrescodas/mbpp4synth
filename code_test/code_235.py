def even_bit_set_number(n): 
    """
    Write a python function to set all even bits of a given number.
    """
    count = 0;res = 0;temp = n 
    while(temp > 0): 
        if (count % 2 == 1): 
            res |= (1 << count)
        count+=1
        temp >>= 1
    return (n | res) 
