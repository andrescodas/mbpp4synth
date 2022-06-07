def count_integer(list1):
    """
    Write a python function to count integers from a given list.
    """
    ctr = 0
    for i in list1:
        if isinstance(i, int):
            ctr = ctr + 1
    return ctr
