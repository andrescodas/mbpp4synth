def remove_Char(s,c) :  
    """
    Write a python function to remove all occurrences of a character in a given string.
    """
    counts = s.count(c) 
    s = list(s) 
    while counts :  
        s.remove(c) 
        counts -= 1 
    s = '' . join(s)   
    return (s) 
