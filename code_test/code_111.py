def common_in_nested_lists(nestedlist):
    """
    Write a function to find common elements in given nested lists. * list item * list item * list item * list item
    """
    result = list(set.intersection(*map(set, nestedlist)))
    return result
