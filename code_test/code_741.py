def all_Characters_Same(s) :
    """
    Write a python function to check whether all the characters are same or not.
    """
    n = len(s)
    for i in range(1,n) :
        if s[i] != s[0] :
            return False
    return True
