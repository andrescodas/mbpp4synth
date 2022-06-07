def largest_pos(list1): 
    """
    Write a python function to find the largest postive number from the given list.
    """
    max = list1[0] 
    for x in list1: 
        if x > max : 
             max = x  
    return max
