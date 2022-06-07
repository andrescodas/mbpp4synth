def interleave_lists(list1,list2,list3):
    """
    Write a function to interleave lists of the same length.
    """
    result = [el for pair in zip(list1, list2, list3) for el in pair]
    return result
