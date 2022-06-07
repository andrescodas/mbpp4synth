def left_rotate(s,d):
    """
    Write a python function to left rotate the string.
    """
    tmp = s[d : ] + s[0 : d]
    return tmp  
