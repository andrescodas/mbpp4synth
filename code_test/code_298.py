def intersection_nested_lists(l1, l2):
    """
    Write a function to find the nested list elements which are present in another list.
    """
    result = [[n for n in lst if n in l1] for lst in l2]
    return result
