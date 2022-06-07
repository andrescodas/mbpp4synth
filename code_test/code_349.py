def check(string) :
    """
    Write a python function to check whether the given string is a binary string or not.
    """
    p = set(string) 
    s = {'0', '1'} 
    if s == p or p == {'0'} or p == {'1'}: 
        return ("Yes") 
    else : 
        return ("No") 
