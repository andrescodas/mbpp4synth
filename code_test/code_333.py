def Sort(sub_li): 
    """
    Write a python function to sort a list according to the second element in sublist.
    """
    sub_li.sort(key = lambda x: x[1]) 
    return sub_li 
