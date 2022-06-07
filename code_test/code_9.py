def find_Rotations(str): 
    """
    Write a python function to find the minimum number of rotations required to get the same string.
    """
    tmp = str + str
    n = len(str) 
    for i in range(1,n + 1): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n 
