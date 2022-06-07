def sequential_search(dlist, item):
    """
    Write a function to search an element in the given array by using sequential search.
    """
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, pos
