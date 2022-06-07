def merge(lst):  
    """
    Write a python function to merge the first and last elements separately in a list of lists.
    """
    return [list(ele) for ele in list(zip(*lst))] 
