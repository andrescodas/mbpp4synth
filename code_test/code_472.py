def check_Consecutive(l): 
    """
    Write a python function to check whether the given list contains consecutive numbers or not.
    """
    return sorted(l) == list(range(min(l),max(l)+1)) 
