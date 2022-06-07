def odd_Equivalent(s,n): 
    """
    Write a python function to find the count of rotations of a binary string with odd value.
    """
    count=0
    for i in range(0,n): 
        if (s[i] == '1'): 
            count = count + 1
    return count 
