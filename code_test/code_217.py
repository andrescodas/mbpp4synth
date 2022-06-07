def first_Repeated_Char(str): 
    """
    Write a python function to find the first repeated character in a given string.
    """
    h = {}
    for ch in str:
        if ch in h: 
            return ch;
        else: 
            h[ch] = 0
    return '\0'
