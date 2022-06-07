def position_min(list1):
    """
    Write a function to find all index positions of the minimum values in a given list.
    """
    min_val = min(list1)
    min_result = [i for i, j in enumerate(list1) if j == min_val]
    return min_result
