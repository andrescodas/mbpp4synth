def unique_sublists(list1):
    """
    Write a function to count number of unique lists within a list.
    """
    result ={}
    for l in  list1: 
        result.setdefault(tuple(l), list()).append(1) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result
