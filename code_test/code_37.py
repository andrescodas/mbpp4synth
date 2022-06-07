def sort_mixed_list(mixed_list):
    """
    Write a function to sort a given mixed list of integers and strings.
    """
    int_part = sorted([i for i in mixed_list if type(i) is int])
    str_part = sorted([i for i in mixed_list if type(i) is str])
    return int_part + str_part
