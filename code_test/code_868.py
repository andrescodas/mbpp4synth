def length_Of_Last_Word(a): 
    """
    Write a python function to find the length of the last word in a given string.
    """
    l = 0
    x = a.strip() 
    for i in range(len(x)): 
        if x[i] == " ": 
            l = 0
        else: 
            l += 1
    return l 
