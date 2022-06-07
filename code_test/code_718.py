def alternate_elements(list1):
    """
    Write a function to create a list taking alternate elements from another given list.
    """
    result=[]
    for item in list1[::2]:
        result.append(item)
    return result 
