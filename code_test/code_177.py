def answer(L,R): 
    """
    Write a python function to find two distinct numbers such that their lcm lies within the given range.
    """
    if (2 * L <= R): 
        return (L ,2*L)
    else: 
        return (-1) 
