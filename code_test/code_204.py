def count(s,c) : 
    """
    Write a python function to count the occurrence of a given character in a string.
    """
    res = 0 
    for i in range(len(s)) : 
        if (s[i] == c): 
            res = res + 1
    return res 
