def position_max(list1):
    """
    Write a function to find all index positions of the maximum values in a given list.
    """
    max_val = max(list1)
    max_result = [i for i, j in enumerate(list1) if j == max_val]
    return max_result
