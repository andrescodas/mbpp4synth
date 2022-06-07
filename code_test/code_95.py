def Find_Min_Length(lst):  
    """
    Write a python function to find the minimum length of sublist.
    """
    minLength = min(len(x) for x in lst )
    return minLength 
