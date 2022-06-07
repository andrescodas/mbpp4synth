def convert(list): 
    """
    Write a python function to convert a list of multiple integers into a single integer.
    """
    s = [str(i) for i in list] 
    res = int("".join(s))  
    return (res) 
