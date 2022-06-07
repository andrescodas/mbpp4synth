def check_subset(list1,list2): 
    """
    Write a function to check if a nested list is a subset of another nested list.
    """
    return all(map(list1.__contains__,list2)) 
