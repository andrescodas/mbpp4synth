def max_length(list1):
    """
    Write a function to find the list of lists with maximum length.
    """
    max_length = max(len(x) for x in  list1 )  
    max_list = max((x) for x in   list1)
    return(max_length, max_list)
