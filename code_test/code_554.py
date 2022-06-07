def Split(list): 
    """
    Write a python function to find odd numbers from a mixed list.
    """
    od_li = [] 
    for i in list: 
        if (i % 2 != 0): 
            od_li.append(i)  
    return od_li
