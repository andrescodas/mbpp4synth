def extract_nth_element(list1, n):
    """
    Write a function to extract the nth element from a given list of tuples.
    """
    result = [x[n] for x in list1]
    return result
