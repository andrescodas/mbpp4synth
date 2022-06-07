def Diff(li1,li2):
    """
    Write a python function to get the difference between two lists.
    """
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))
 
