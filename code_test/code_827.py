def sum_column(list1, C):
    """
    Write a function to sum a specific column of a list in a given list of lists.
    """
    result = sum(row[C] for row in list1)
    return result
