def Split(list): 
    """
    Write a python function to find even numbers from a mixed list.
    """
    ev_li = [] 
    for i in list: 
        if (i % 2 == 0): 
            ev_li.append(i)  
    return ev_li
