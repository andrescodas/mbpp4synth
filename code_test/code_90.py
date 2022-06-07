def len_log(list1):
    """
    Write a python function to find the length of the longest word.
    """
    max=len(list1[0])
    for i in list1:
        if len(i)>max:
            max=len(i)
    return max
