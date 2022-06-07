def swap_List(newList): 
    """
    Write a python function to interchange first and last elements in a given list.
    """
    size = len(newList) 
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp   
    return newList 
