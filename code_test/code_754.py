def extract_index_list(l1, l2, l3):
    """
    Write a function to find common index elements from three lists.
    """
    result = []
    for m, n, o in zip(l1, l2, l3):
        if (m == n == o):
            result.append(m)
    return result
