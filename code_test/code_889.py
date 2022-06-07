def reverse_list_lists(lists):
    """
    Write a function to reverse each list in a given list of lists.
    """
    for l in lists:
        l.sort(reverse = True)
    return lists 
