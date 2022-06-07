def remove_odd(l):
    """
    Write a python function to remove odd numbers from a given list.
    """
    for i in l:
        if i % 2 != 0:
            l.remove(i)
    return l
